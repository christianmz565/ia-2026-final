# Cascade R-CNN Baseline para Detección de Defectos en Madera (`src/casc_rcnn/agy`)

Este módulo contiene la implementación completa y ejecutable del modelo baseline **Cascade R-CNN** con backbone **ConvNeXt** y cuello **PAFPN** (Path Aggregation Feature Pyramid Network) para la detección de objetos en imágenes de superficie de madera.

---

## 🏗️ Arquitectura y Configuración del Modelo

- **Detector Head:** Cascade R-CNN con 3 etapas secuenciales (umbrales IoU: $0.5$, $0.6$, $0.7$) para refinamiento iterativo de bounding boxes.
- **Backbone:** ConvNeXt (`convnext_tiny` o `convnext_small`) con pesos preentrenados en COCO (Transfer Learning).
- **Neck (Cuello):** PAFPN (Path Aggregation Feature Pyramid Network), combinando rutas top-down (FPN) y bottom-up para mayor retención de características multiescala.
- **Optimizaciones CUDA:** 
  - **Precisión Mixta Automática (AMP FP16)** mediante `torch.amp.GradScaler`.
  - Habilitación de `torch.backends.cudnn.benchmark = True`.
  - Carga optimizada con `pin_memory=True` y workers paralelos en `DataLoader`.

---

## 🧹 Sanitización de Datos y Reglas del Baseline

Antes de iniciar el entrenamiento, el pipeline ejecuta una fase de validación estricta y ligera (`DataSanitizer`):
1. **Detección y descarte de imágenes corruptas o inasibles.**
2. **Validación de anotaciones:**
   - Descarte de cajas con $área \le 0$.
   - Descarte de coordenadas inválidas ($x_{max} \le x_{min}$ o $y_{max} \le y_{min}$).
   - Descarte de coordenadas fuera de límites.
3. **Tratamiento Restrictivo (Baseline):**
   - **PROHIBIDO** redimensionar o recortar las imágenes válidas.
   - **PROHIBIDO** aplicar aumentos de datos (Data Augmentation) geométricos o fotométricos.
   - Cada imagen se procesa a su **resolución nativa original**.

---

## 🚀 Guía de Ejecución

### Comandos de Ejecución

```bash
# Instalar/sincronizar dependencias
uv sync

# Ejecutar entrenamiento pipeline baseline
uv run python -m src.s3_train.cascade_rcnn.train
```

### Argumentos de Línea de Comandos (Opcionales)

```bash
uv run python -m src.s3_train.cascade_rcnn.train \
  --data-dir dataset/split \
  --train-json dataset/split/train_coco.json \
  --val-json dataset/split/val_coco.json \
  --output-dir outputs/cascade_rcnn \
  --backbone convnext_tiny \
  --epochs 12 \
  --batch-size 2
```

---

## 📁 Entregables y Resultados Generados

Los artefactos y reportes se guardan en la carpeta configurada (`outputs/casc_rcnn_baseline/`):
- `best_cascade_rcnn.pth`: Pesos del mejor modelo según métrica de validación ($mAP_{50:95}$).
- `latest_cascade_rcnn.pth`: Último checkpoint guardado.
- `sanitization_report.json` & `sanitization_report.md`: Reporte detallado de limpieza de datos e imágenes descartadas.
- `summary_report.json` & `summary_report.md`: Informe final con épocas completadas, tiempo transcurrido y métricas $mAP_{50}$ y $mAP_{50:95}$.
- `training_pipeline.log`: Log completo de la ejecución por época.
