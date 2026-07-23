# Guía de Visualización, Evaluación y Análisis de Resultados (YOLO26)

Esta guía detalla el procedimiento para interpretar las métricas de rendimiento, gráficos de evaluación y realizar inferencias sobre el conjunto de prueba (*test set*) tras culminar el entrenamiento de **YOLO26**.

---

## 1. Métricas Principales de Evaluación

El rendimiento del detector de defectos en madera se cuantifica a través de 4 métricas estándar en visión por computadora:

| Métrica | Definición Matemático/Conceptual | Interpretación Práctica |
| :--- | :--- | :--- |
| **Precision ($P$)** | $P = \frac{TP}{TP + FP}$ | Porcentaje de detecciones de defectos que son verdaderamente correctas. Evita falsas alarmas. |
| **Recall ($R$)** | $R = \frac{TP}{TP + FN}$ | Porcentaje de defectos reales presentes en la madera que el modelo logró detectar. Evita omitir fallas. |
| **mAP@50** | Mean Average Precision con un umbral de solapamiento $\text{IoU} \ge 0.50$. | Precisión media global considerando detección y clasificación básica de la bounding box. |
| **mAP@50-95** | Promedio de $mAP$ evaluado progresivamente en umbrales IoU desde $0.50$ hasta $0.95$ (pasos de 0.05). | Indicador riguroso de la calidad de ajuste fino y precisión geométrica del encuadre. |

---

## 2. Gráficos Autogenerados por Ultralytics y su Interpretación

El pipeline de entrenamiento guarda automáticamente los artefactos de análisis en `/kaggle/working/runs/yolo26/yolo26_s_phase2_full/`.

### 1. `results.png` (Curvas de Pérdida y Métricas por Época)
Muestra la evolución temporal de:
- **`train/box_loss`**, **`train/cls_loss`**, **`train/dfl_loss`**: Pérdidas de caja, clase y focal distribution en entrenamiento.
- **`val/box_loss`**, **`val/cls_loss`**, **`val/dfl_loss`**: Pérdidas en validación. *Si la pérdida de validación asciende mientras la de train baja, indica sobreajuste (overfitting).*
- **`metrics/mAP50(B)`** y **`metrics/mAP50-95(B)`**: Comportamiento de precisión media acumulada.

### 2. `confusion_matrix.png` (Matriz de Confusión)
- Filas: Clases verdaderas (*Ground Truth*).
- Columnas: Clases predichas por YOLO26 (incluye la categoría `background` para detecciones o ausencias no deseadas).
- Permite identificar confusión entre clases similares (ejemplo: `Live_Knot` vs `Dead_Knot` o `Crack` vs `knot_with_crack`).

### 3. `PR_curve.png` (Curva Precision-Recall)
- Visualiza el compromiso entre Precision y Recall para cada una de las 8 clases de madera a distintos umbrales de confianza.
- El área bajo la curva (AUC) corresponde al AP de cada clase.

### 4. `F1_curve.png` (Curva F1-Score vs Confianza)
- Muestra el valor de F1-Score ($2 \cdot \frac{P \cdot R}{P + R}$) en función de la confianza del detector.
- Permite determinar el **umbral óptimo de confianza** (ejemplo: `conf = 0.35`) para desplegar en producción.

---

## 3. Código Python para Evaluación en el Split de Test

Una vez finalizado el entrenamiento, ejecuta el siguiente script en Kaggle para evaluar sobre el dataset de test:

```python
from ultralytics import YOLO
import pandas as pd

# 1. Cargar los mejores pesos guardados
best_model_path = "/kaggle/working/runs/yolo26/yolo26_s_phase2_full/weights/best.pt"
model = YOLO(best_model_path)

# 2. Ejecutar validación sobre el split 'test'
metrics = model.val(data="data_wood.yaml", split="test", rect=True)

# 3. Extraer métricas consolidadas
print("📊 RESUMEN DE MÉTRICAS EN TEST SET:")
print(f"  - mAP@50    : {metrics.box.map50:.4f}")
print(f"  - mAP@50-95 : {metrics.box.map:.4f}")
print(f"  - Precision : {metrics.box.mp:.4f}")
print(f"  - Recall    : {metrics.box.mr:.4f}")

# 4. Desglose de mAP50 por clase
class_df = pd.DataFrame({
    "Clase Defecto": [metrics.names[i] for i in range(len(metrics.box.maps))],
    "mAP@50": metrics.box.maps50,
    "mAP@50-95": metrics.box.maps
})
print("\n📋 MÉTRICAS POR TIPO DE DEFECTO:")
print(class_df.to_string(index=False))
```

---

## 4. Visualización de Predicciones e Inferencias Físicas

Para inspeccionar visualmente cómo detecta las cajas el modelo sobre imágenes reales de prueba:

```python
import matplotlib.pyplot as plt
import cv2
from pathlib import Path

# Ejecutar inferencia en imágenes de prueba
test_images_dir = Path("/kaggle/input/large-scale-image-dataset-of-wood-surface-defects/test/images")
results = model.predict(source=str(test_images_dir), save=True, conf=0.35, rect=True)

# Mostrar las primeras 4 predicciones
saved_predict_dir = Path(results[0].save_dir)
image_files = list(saved_predict_dir.glob("*.jpg"))[:4]

fig, axes = plt.subplots(2, 2, figsize=(14, 14))
for ax, img_path in zip(axes.ravel(), image_files):
    img = cv2.imread(str(img_path))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ax.imshow(img)
    ax.axis("off")
    ax.set_title(img_path.name)

plt.tight_layout()
plt.show()
```
