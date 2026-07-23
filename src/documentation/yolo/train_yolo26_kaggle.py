#!/usr/bin/env python3
"""
Entrenamiento de YOLO26 / YOLOv11 en Kaggle (2x T4 GPUs)
=========================================================
Este script está optimizado para ejecutarse en notebooks de Kaggle utilizando
aceleración dual por GPU (2x NVIDIA T4) mediante PyTorch y la API de Ultralytics.

Características principales:
- Selección de variantes: Small (s), Medium (m), Large (l) con pesos COCO pre-entrenados.
- Entrenamiento rectangular (`rect=True`) manteniendo la relación de aspecto original.
- Entrenamiento en 2 fases: Congelamiento de backbone (Fase 1) -> Fine-tuning (Fase 2).
- baseline estricto: Desactivación total de aumentación de datos (augment=False, mosaic=0, mixup=0).
- Optimizaciones avanzadas de PyTorch: AMP (fp16), cuDNN benchmark, DataLoaders optimizados.
- Monitoreo con tqdm que calcula el promedio de época a partir de la 2da iteración
  y proyecta el tiempo total estimado para garantizar una duración entre 3 y 5 horas.
- Early Stopping y métricas completas por época.
"""

from __future__ import annotations

import os
import sys
import subprocess
import time
from pathlib import Path

def ensure_dependencies():
    """Instala automáticamente las librerías necesarias en Kaggle si no existen."""
    required = ["ultralytics", "pyyaml", "tqdm", "structlog"]
    missing = []
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"📦 Instalando dependencias faltantes en Kaggle: {missing}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"] + missing)

ensure_dependencies()

import yaml
import torch
from tqdm.auto import tqdm
from ultralytics import YOLO

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DEL ENTORNO Y HARDWARE
# -----------------------------------------------------------------------------
def setup_pytorch_optimizations():
    """Aplica optimizaciones globales de PyTorch para máximo rendimiento en GPU."""
    print("⚡ Aplicando optimizaciones de PyTorch y CUDA...")
    if torch.cuda.is_available():
        # Habilitar algoritmo cuDNN para encontrar la mejor convolución en hardware fijo
        torch.backends.cudnn.benchmark = True
        torch.backends.cudnn.deterministic = False
        
        # Permitir TensorFloat-32 (TF32) en GPUs Ampere/Ada si están disponibles
        if hasattr(torch.backends.cuda, "matmul"):
            torch.backends.cuda.matmul.allow_tf32 = True
            torch.backends.cudnn.allow_tf32 = True

        num_gpus = torch.cuda.device_count()
        for i in range(num_gpus):
            props = torch.cuda.get_device_properties(i)
            print(f"  - GPU {i}: {props.name} | VRAM: {props.total_memory / (1024**3):.2f} GB")
        return [i for i in range(num_gpus)]
    else:
        print("⚠️ ALERTA: No se detectó GPU CUDA. El entrenamiento se ejecutará en CPU (muy lento).")
        return "cpu"

# -----------------------------------------------------------------------------
# GESTIÓN DE CONFIGURACIÓN DATASET (data.yaml)
# -----------------------------------------------------------------------------
CLASS_NAMES = [
    "Live_Knot",
    "Dead_Knot",
    "resin",
    "knot_with_crack",
    "Crack",
    "Marrow",
    "Quartzity",
    "Knot_missing",
]

def find_dataset_root(given_path: str | Path) -> Path:
    """Busca dinámicamente la carpeta raíz real que contiene 'train' en Kaggle."""
    given = Path(given_path).resolve()
    
    # 1. Si la ruta dada directamente contiene 'train' o 'split/train'
    if (given / "train").exists():
        return given
    if (given / "split" / "train").exists():
        return given / "split"

    # 2. Lista de rutas conocidas probables en Kaggle
    candidates = [
        Path("/kaggle/input/datasets/frennow/tables/split"),
        Path("/kaggle/input/datasets/frennow/tables"),
        Path("/kaggle/input/frennow/tables/split"),
        Path("/kaggle/input/tables/split"),
        Path("/kaggle/input/table/split"),
        Path("/kaggle/input/tables"),
        Path("/kaggle/input/table"),
    ]
    for cand in candidates:
        if cand.exists() and (cand / "train").exists():
            return cand
        if cand.exists() and (cand / "split" / "train").exists():
            return cand / "split"

    # 3. Búsqueda recursiva dinámica en /kaggle/input/ por el directorio 'train'
    kaggle_input = Path("/kaggle/input")
    if kaggle_input.exists():
        for p in kaggle_input.rglob("train"):
            if p.is_dir():
                print(f"🔍 Búsqueda dinámica encontró 'train' en: {p}")
                return p.parent

    return given


def prepare_data_yaml(dataset_base_path: str | Path, output_yaml: str | Path = "data_wood.yaml") -> Path:
    """Crea un archivo data.yaml dinámico compatible con la estructura de Kaggle (e.g. /kaggle/input/datasets/frennow/tables/split)."""
    base_path = find_dataset_root(dataset_base_path)
    print(f"📂 Ruta base detectada para el dataset: {base_path}")

    # Función robusta para determinar la subcarpeta de imágenes (images o image)
    def find_images_subpath(split_name: str) -> str:
        split_dir = base_path / split_name
        if (split_dir / "images").exists() or not split_dir.exists():
            return f"{split_name}/images"
        elif (split_dir / "image").exists():
            return f"{split_name}/image"
        return f"{split_name}/images"

    train_path = find_images_subpath("train")
    val_path = find_images_subpath("val")
    test_path = find_images_subpath("test")

    yaml_data = {
        "path": str(base_path),
        "train": train_path,
        "val": val_path,
        "test": test_path,
        "names": {idx: name for idx, name in enumerate(CLASS_NAMES)},
        "nc": len(CLASS_NAMES),
    }

    yaml_file = Path(output_yaml)
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(yaml_data, f, sort_keys=False)
    
    print(f"📄 Configuración data.yaml generada en {yaml_file.resolve()}:")
    print(yaml.dump(yaml_data, sort_keys=False))
    return yaml_file.resolve()



# -----------------------------------------------------------------------------
# CALLBACK DE TIMING Y RECOMENDACIÓN CON TQDM
# -----------------------------------------------------------------------------
class EpochTimerCallback:
    """Callback para registrar duraciones por época con tqdm y estimar el tiempo total."""

    def __init__(self, total_epochs: int, target_min_hours: float = 3.0, target_max_hours: float = 5.0):
        self.total_epochs = total_epochs
        self.target_min_hours = target_min_hours
        self.target_max_hours = target_max_hours
        self.epoch_times = []
        self.epoch_start_time = None
        self.pbar = None

    def on_train_begin(self, trainer):
        self.pbar = tqdm(total=self.total_epochs, desc="⏱️ Progreso General Épocas", unit="época")
        print("\n🚀 Inicio del entrenamiento YOLO26...")

    def on_train_epoch_start(self, trainer):
        self.epoch_start_time = time.time()

    def on_train_epoch_end(self, trainer):
        if self.epoch_start_time is None:
            return
        
        duration = time.time() - self.epoch_start_time
        self.epoch_times.append(duration)
        current_epoch = len(self.epoch_times)
        
        if self.pbar:
            self.pbar.update(1)

        # Proyección a partir de la 2da época (la 1ra suele incluir overhead de compilación y warmup)
        if current_epoch >= 2:
            avg_duration_sec = sum(self.epoch_times[1:]) / len(self.epoch_times[1:])
            projected_total_sec = avg_duration_sec * self.total_epochs
            projected_total_hours = projected_total_sec / 3600.0
            remaining_epochs = self.total_epochs - current_epoch
            remaining_hours = (avg_duration_sec * remaining_epochs) / 3600.0

            log_msg = (
                f"\n📊 [Época {current_epoch}/{self.total_epochs}] "
                f"Duración: {duration:.1f}s | Promedio: {avg_duration_sec:.1f}s/época | "
                f"Proyección Total: {projected_total_hours:.2f}h | Restante: {remaining_hours:.2f}h"
            )
            print(log_msg)

            if projected_total_hours > self.target_max_hours:
                print(
                    f"⚠️ ADVERTENCIA: La proyección actual ({projected_total_hours:.2f}h) excede el límite recomendado de "
                    f"{self.target_max_hours}h. Se recomienda reducir el número de épocas o cambiar a una variante menor (ej. 's')."
                )
            elif projected_total_hours < self.target_min_hours and current_epoch == 2:
                print(
                    f"💡 NOTA: El entrenamiento se proyecta en {projected_total_hours:.2f}h, lo cual es más rápido que el objetivo mínimo de {self.target_min_hours}h. "
                    f"Puedes aumentar las épocas si deseas mayor convergencia."
                )

    def on_train_end(self, trainer):
        if self.pbar:
            self.pbar.close()
        if self.epoch_times:
            total_sec = sum(self.epoch_times)
            print(f"\n✅ Entrenamiento finalizado en {total_sec / 3600.0:.2f} horas ({total_sec:.1f} segundos total).")

# -----------------------------------------------------------------------------
# FUNCIÓN PRINCIPAL DE ENTRENAMIENTO
# -----------------------------------------------------------------------------
def train_yolo26(
    data_dir: str = "/kaggle/input/datasets/frennow/tables/split",
    variant: str = "s",  # 's', 'm', o 'l'
    epochs: int = 80,
    freeze_epochs: int = 5,
    batch_size: int = 32,
    imgsz: int = 640,
    patience: int = 15,
    output_dir: str = "/kaggle/working/runs/yolo26",
):
    """
    Ejecuta el entrenamiento de YOLO26 en Kaggle con 2x T4 GPUs.
    
    Args:
        data_dir: Ruta base del dataset split (ej. /kaggle/input/datasets/frennow/tables/split).
        variant: Variante del modelo ('s': small, 'm': medium, 'l': large).
        epochs: Número total de épocas.
        freeze_epochs: Número de épocas iniciales con el backbone congelado.
        batch_size: Tamaños de lote combinado para las 2 GPUs.
        imgsz: Resolución de imagen (se respeta formato rect=True sin alteración).
        patience: Épocas para Early Stopping.
        output_dir: Directorio de salida para guardar pesos y métricas.
    """
    # 1. Configuración de Hardware
    devices = setup_pytorch_optimizations()
    device_arg = devices if isinstance(devices, list) else 0

    # 2. Configurar data.yaml
    data_yaml_path = prepare_data_yaml(data_dir, output_yaml="data_wood.yaml")

    # 3. Mapeo de variante de modelo pre-entrenado COCO
    # Para la serie YOLO, usaremos los pesos pre-entrenados COCO (yolo11 / yolo26)
    model_name = f"yolo11{variant}.pt"  # O yolo26{variant}.pt según disponibilidad
    print(f"\n📦 Cargando modelo pre-entrenado COCO: {model_name}...")
    model = YOLO(model_name)

    # 4. FASE 1: Entrenamiento con Backbone Congelado
    if freeze_epochs > 0:
        print(f"\n❄️ FASE 1: Congelando backbone durante las primeras {freeze_epochs} épocas...")
        # Congelar los primeros 10-14 bloques (backbone) del modelo
        freeze_layer_count = 10
        model.train(
            data=str(data_yaml_path),
            epochs=freeze_epochs,
            batch=batch_size,
            imgsz=imgsz,
            rect=True,              # Entrenar manteniendo la relación de aspecto original
            augment=False,           # Baseline: SIN aumentaciones (mosaic=0, fliplr=0, etc.)
            hsv_h=0.0, hsv_s=0.0, hsv_v=0.0,
            degrees=0.0, translate=0.0, scale=0.0, shear=0.0, perspective=0.0,
            flipud=0.0, fliplr=0.0, mosaic=0.0, mixup=0.0, copy_paste=0.0,
            device=device_arg,       # Usa las 2 GPUs: [0, 1]
            amp=True,                # Precision Mixta FP16
            freeze=freeze_layer_count,# Congelar capas 0..9 del backbone
            project=output_dir,
            workers=4,
            exist_ok=True,
            verbose=True,
        )
        print("✅ FASE 1 completada. Procediendo a descongelar el backbone para Fine-Tuning completo.")
        phase1_weights = Path(output_dir) / f"yolo26_{variant}_phase1_freeze" / "weights" / "best.pt"
        if not phase1_weights.exists():
            phase1_weights = Path(output_dir) / f"yolo26_{variant}_phase1_freeze" / "weights" / "last.pt"
        
        print(f"📦 Cargando pesos resultantes de la Fase 1 ({phase1_weights}) para iniciar la Fase 2...")
        model = YOLO(str(phase1_weights))

    # 5. FASE 2: Fine-Tuning Completo (Unfreeze)
    remaining_epochs = max(1, epochs - freeze_epochs)
    print(f"\n🔥 FASE 2: Fine-tuning completo por {remaining_epochs} épocas restantes...")
    
    timer_callback = EpochTimerCallback(total_epochs=remaining_epochs)
    model.add_callback("on_train_begin", timer_callback.on_train_begin)
    model.add_callback("on_train_epoch_start", timer_callback.on_train_epoch_start)
    model.add_callback("on_train_epoch_end", timer_callback.on_train_epoch_end)
    model.add_callback("on_train_end", timer_callback.on_train_end)

    results = model.train(
        data=str(data_yaml_path),
        epochs=remaining_epochs,
        batch=batch_size,
        imgsz=imgsz,
        rect=True,               # Entrenamiento rectangular
        augment=False,            # Sin modificacion de datos/aumentaciones para baseline
        hsv_h=0.0, hsv_s=0.0, hsv_v=0.0,
        degrees=0.0, translate=0.0, scale=0.0, shear=0.0, perspective=0.0,
        flipud=0.0, fliplr=0.0, mosaic=0.0, mixup=0.0, copy_paste=0.0,
        device=device_arg,        # Aceleración dual 2x T4 [0, 1]
        amp=True,                 # Mixed Precision
        freeze=0,                 # Descongelar todo el modelo
        patience=patience,        # Early stopping
        project=output_dir,
        name=f"yolo26_{variant}_phase2_full",
        workers=4,
        plots=True,               # Generar curvas PR, F1, Matriz de Confusión automáticamente
        exist_ok=True,
        verbose=True,
    )

    print("\n🎉 Proceso de entrenamiento concluido exitosamente.")
    print(f"📁 Resultados guardados en: {output_dir}/yolo26_{variant}_phase2_full")
    return results

# -----------------------------------------------------------------------------
# PUNTO DE ENTRADA CLI DE KAGGLE
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Entrenamiento YOLO26 en Kaggle (2x T4 GPUs)")
    parser.add_argument("--data-dir", type=str, default="/kaggle/input/datasets/frennow/tables/split", help="Ruta al dataset (ej. /kaggle/input/datasets/frennow/tables/split)")
    parser.add_argument("--variant", type=str, choices=["s", "m", "l"], default="s", help="Variante del modelo (s, m, l)")
    parser.add_argument("--epochs", type=int, default=80, help="Total de épocas recomendadas para 3-5h")
    parser.add_argument("--freeze-epochs", type=int, default=5, help="Épocas congelando backbone")
    parser.add_argument("--batch", type=int, default=32, help="Batch size global (repartido en 2 GPUs)")
    parser.add_argument("--imgsz", type=int, default=640, help="Tamaño de entrada de imágenes")
    parser.add_argument("--patience", type=int, default=15, help="Patience para Early Stopping")
    parser.add_argument("--output-dir", type=str, default="/kaggle/working/runs/yolo26")

    # Usar parse_known_args() ignora los argumentos del kernel de Jupyter/Kaggle (-f kernel-xxx.json)
    args, _ = parser.parse_known_args()

    train_yolo26(
        data_dir=args.data_dir,
        variant=args.variant,
        epochs=args.epochs,
        freeze_epochs=args.freeze_epochs,
        batch_size=args.batch,
        imgsz=args.imgsz,
        patience=args.patience,
        output_dir=args.output_dir,
    )



