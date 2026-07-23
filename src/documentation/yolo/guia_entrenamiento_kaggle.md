# Guía de Entrenamiento en Kaggle: YOLO26 con 2x T4 GPUs

Esta guía explica el procedimiento paso a paso para configurar, ejecutar y monitorear el entrenamiento de **YOLO26** en la plataforma Kaggle utilizando la GPU dual **GPU T4 x2**.

---

## 1. Requisitos Previos en Kaggle

1. Cuenta verificada en [Kaggle](https://www.kaggle.com).
2. Acceso al dataset de defectos de madera con la estructura dividida: `train/`, `val/`, `test/` y etiquetas en formato YOLO (`.txt`).

---

## 2. Paso a Paso para la Configuración del Notebook

### Paso 1: Crear un nuevo Notebook
1. Dirígete a la sección **Code** en Kaggle y haz clic en **New Notebook**.
2. Asigna un nombre al notebook (ejemplo: `Wood_Defects_YOLO26_Training`).

### Paso 2: Vincular el Dataset
1. En el panel derecho **Input**, haz clic en **+ Add Input**.
2. Vincula la base de datos subida (`tables` o `table`).
3. Confirma que la estructura en Kaggle muestre `tables/split` (con las carpetas `test`, `train` y `val` en su interior). La ruta de entrada predeterminada será `/kaggle/input/tables/split`.

### Paso 3: Configurar el Acelerador de Hardware (2x T4)
1. En el panel derecho **Notebook options**, busca la opción **ACCELERATOR**.
2. Selecciona **GPU T4 x2**.
3. Asegúrate de tener activada la conexión a Internet (**Persistence / Internet: On**).

---

## 3. Código de Ejecución en Celda de Kaggle

Copia y ejecuta el siguiente bloque de código dentro de la primera celda del Notebook:

```python
# 1. Instalación de dependencias necesarias
!pip install -q ultralytics pyyaml tqdm structlog

# 2. Descarga o escritura del script oficial train_yolo26_kaggle.py
# Simplemente pega el contenido del archivo buffer/train_yolo26_kaggle.py en este notebook.
```

O directamente ejecutando el script desde la línea de comandos de Kaggle:

```bash
!python /kaggle/working/train_yolo26_kaggle.py \
    --data-dir /kaggle/input/tables/split \
    --variant s \
    --epochs 80 \
    --freeze-epochs 5 \
    --batch 32 \
    --imgsz 640 \
    --patience 15 \
    --output-dir /kaggle/working/runs/yolo26
```

---

## 4. Interpretación del Monitoreo y Ajuste de Tiempo (3 a 5 horas)

Durante la ejecución, la consola desplegará una barra de progreso `tqdm` personalizada:

```text
⏱️ Progreso General Épocas:  15%|███▋                  | 12/80 [25:14<2:22:50, 126.0s/época]

📊 [Época 2/80] Duración: 124.5s | Promedio: 124.5s/época | Proyección Total: 2.76h | Restante: 2.69h
```

### Reglas de Decisión según la Salida:
- **Caso A (Proyección entre 3.0h y 5.0h)**: Excelente. Mantener la variante actual (`--variant s` o `--variant m`) y dejar culminar el entrenamiento.
- **Caso B (Proyección > 5.0h)**: La celda mostrará una advertencia `⚠️ ADVERTENCIA`. En la siguiente ejecución:
  - Disminuir la cantidad de épocas (`--epochs 60`).
  - Reducir la variante de modelo si estabas usando `l` o `m` a `s`.
- **Caso C (Proyección < 3.0h en época 2)**: Puedes incrementar las épocas hasta 100 o cambiar de variante `s` a `m`.

---

## 5. Descarga de Pesos y Artefactos Resultantes

Al finalizar el entrenamiento, los pesos óptimos y gráficos se encontrarán en:
- Ruta de mejores pesos: `/kaggle/working/runs/yolo26/yolo26_s_phase2_full/weights/best.pt`
- Gráficos de evaluación: `/kaggle/working/runs/yolo26/yolo26_s_phase2_full/*.png`

Puedes comprimir los resultados para descargarlos mediante:
```python
import shutil
shutil.make_archive('/kaggle/working/yolo26_results', 'zip', '/kaggle/working/runs/yolo26')
print("📦 Archivo zip generado en /kaggle/working/yolo26_results.zip")
```
