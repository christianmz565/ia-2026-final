# Data source

The data source used for this study is available at [https://www.kaggle.com/datasets/nomihsa965/large-scale-image-dataset-of-wood-surface-defects](https://www.kaggle.com/datasets/nomihsa965/large-scale-image-dataset-of-wood-surface-defects). It contains a large-scale image dataset of wood surface defects, which is used for training and evaluating the defect detection models in this benchmark pipeline. The data source is pre-processed in memory and stored in disk for compatibility with the training and evaluation modules.

# CLI Usage Guide

Command-line interface (CLI) reference and execution guide for the Wood Surface Defect Detection benchmark pipeline.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Global Pipeline CLI (`src`)](#global-pipeline-cli-src)
  - [Syntax](#syntax)
  - [Global Flags](#global-flags)
  - [Per-Section Overrides Syntax](#per-section-overrides-syntax)
  - [Per-Section Configuration Parameters](#per-section-configuration-parameters)
- [Standalone Module Execution](#standalone-module-execution)
  - [Section 1: Data Preparation (`src.s1_prepare`)](#section-1-data-preparation-srcs1_prepare)
  - [Section 2: Data Augmentations (`src.s2_augments`)](#section-2-data-augmentations-srcs2_augments)
  - [Section 3: Model Training (`src.s3_train`)](#section-3-model-training-srcs3_train)
  - [Section 4: Evaluation & Inference (`src.s4_evaluate`)](#section-4-evaluation--inference-srcs4_evaluate)
  - [Section 5: Analysis & Visualization (`src.s5_analysis`)](#section-5-analysis--visualization-srcs5_analysis)
  - [Section 6: Single-Image Prediction (`src.s6_predict`)](#section-6-single-image-prediction-srcs6_predict)
- [Logging Configuration](#logging-configuration)
- [Common Execution Examples](#common-execution-examples)

---

## Quick Start

Run the entire pipeline end-to-end with default settings:

```bash
uv run python -m src
```

Display global CLI help:

```bash
uv run python -m src --help
```

> **Rerun protocol:** step caching is existence-based. After any code or config
> change, re-run end-to-end with per-section `force` (or delete `partials/`);
> otherwise stale artifacts are silently reused. Cache hits are logged as
> `step_cached` warnings with the requesting config fingerprint for audit.

---

## Global Pipeline CLI (`src`)

### Syntax

```bash
uv run python -m src [GLOBAL_FLAGS] [--s1_prepare KEY=VALUE ...] [--s2_augments KEY=VALUE ...] [--s3_train KEY=VALUE ...] [--s4_evaluate KEY=VALUE ...] [--s5_analysis KEY=VALUE ...]
```

### Global Flags

| Flag | Type | Allowed Values | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `--only` | string list | `s1_prepare`, `s2_augments`, `s3_train`, `s4_evaluate`, `s5_analysis` | `None` (runs all) | Select specific pipeline section(s) to execute in order. |
| `--log_level` | string | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` | `INFO` | Configures structured logging verbosity across all modules. |
| `-h`, `--help` | flag | N/A | N/A | Displays CLI usage instructions and exits. |

### Per-Section Overrides Syntax

Sections accept space-separated `key=value` pairs following dot-notation for nested fields.

- **Booleans**: Parsed case-insensitively (`true`, `yes`, `false`, `no`).
- **Numbers**: Automatically coerced to integer or float.
- **Lists**: Specified as comma-separated values (e.g. `models=rf_detr,yolo26`).

Example:

```bash
uv run python -m src \
  --only s1_prepare s3_train \
  --s1_prepare download.force_redownload=true split.seed=100 \
  --s3_train models=yolo26 yolo26.epochs=50 yolo26.batch=32
```

---

### Per-Section Configuration Parameters

#### Section 1: `--s1_prepare`

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `download.kaggle_dataset` | string | `"nomihsa965/large-scale-image-dataset-of-wood-surface-defects"` | Kaggle dataset identifier slug. |
| `download.force_redownload` | boolean | `false` | Force re-download dataset even if local copy exists. |
| `preprocess.scale_factor` | float | `0.5` | Rescaling factor applied to input images. |
| `preprocess.min_label_size_px` | float | `4.0` | Minimum bounding box side length (px) post-scaling. |
| `preprocess.black_threshold` | integer | `10` | Grayscale threshold for background filtering. |
| `split.seed` | integer | `42` | Random seed for split generation. |
| `split.stratify_by_class` | boolean | `true` | Enable multi-label greedy iterative stratification. |

#### Section 2: `--s2_augments`

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `augment.methods` | list | `albumentations_balanced,boxaug_standard,boxaug_libcom` | Augmentation strategies to generate. |

#### Section 3: `--s3_train`

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `models` | list | `rf_detr,cascade_rcnn,yolo26` | Architectures to train. |
| `augments` | list | `baseline,albumentations_balanced,boxaug_standard,boxaug_libcom` | Dataset splits to train models on. |
| `yolo26.model_size` | string | `"yolo26m.pt"` | Pretrained YOLO26 checkpoint/variant. |
| `yolo26.epochs` | integer | `100` | Number of training epochs for YOLO26. |
| `yolo26.imgsz` | integer | `640` | Input image size for YOLO26. |
| `yolo26.batch` | integer | `16` | Batch size for YOLO26 training. |
| `yolo26.lr0` | float | `0.01` | Initial learning rate for YOLO26. |
| `yolo26.device` | string | `cuda:0` / `cpu` | Target compute device for YOLO26. |
| `yolo26.freeze_layer_count` | integer | `None` | Number of initial backbone layers to freeze during training. |
| `cascade_rcnn.config_file` | string | `"cascade_rcnn_r50_fpn_1x_coco.py"` | MMDetection config filename. |
| `cascade_rcnn.epochs` | integer | `12` | Training epochs for Cascade R-CNN. |
| `cascade_rcnn.imgsz` | integer | `640` | Image scale for Cascade R-CNN. |
| `cascade_rcnn.batch_size` | integer | `8` | Batch size for Cascade R-CNN. |
| `cascade_rcnn.lr` | float | `0.0001` | Learning rate for Cascade R-CNN. |
| `cascade_rcnn.device` | string | `cuda:0` / `cpu` | Target compute device for Cascade R-CNN. |
| `rf_detr.model_size` | string | `"rfdetr-m.pt"` | Pretrained RF-DETR variant. |
| `rf_detr.epochs` | integer | `50` | Number of training epochs for RF-DETR. |
| `rf_detr.imgsz` | integer | `512` | Input image size for RF-DETR. |
| `rf_detr.batch` | integer | `8` | Batch size for RF-DETR training. |
| `rf_detr.lr0` | float | `0.001` | Initial learning rate for RF-DETR. |
| `rf_detr.device` | string | `cuda:0` / `cpu` | Target compute device for RF-DETR. |

#### Section 4: `--s4_evaluate`

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `models` | list | `rf_detr,cascade_rcnn,yolo26` | Model architectures to evaluate. |
| `augments` | list | `baseline,albumentations_balanced,boxaug_standard,boxaug_libcom` | Dataset augmentations to evaluate. |
| `eval.model_path` | string | `""` | Path to specific model checkpoint. |
| `eval.data_dir` | string | `""` | Directory containing evaluation dataset. |
| `eval.predictions` | string | `""` | Path to saved predictions file. |
| `eval.ground_truth` | string | `""` | Path to ground truth COCO JSON. |
| `eval.output_path` | string | `""` | Output path for evaluation metrics JSON. |
| `eval.iou_threshold` | float | `0.5` | IoU threshold for evaluation metrics. |
| `eval.conf_threshold` | float | `0.25` | Score confidence threshold. |
| `eval.device` | string | `cuda:0` / `cpu` | Evaluation compute device. |

#### Section 5: `--s5_analysis`

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `results_dir` | string | `""` | Path to evaluation results directory. |
| `analysis.input` | string | `""` | Path to aggregated results JSON file. |
| `analysis.output_dir` | string | `""` | Destination path for output figures and tables. |
| `analysis.output_format` | string | `"latex"` | Table format (`latex`, `markdown`, `csv`). |
| `analysis.figure_dpi` | integer | `300` | DPI resolution for generated figures. |
| `analysis.figure_backend` | string | `"Agg"` | Matplotlib rendering backend. |

---

## Standalone Module Execution

Individual stage modules can be executed directly as Python modules. Standalone CLI flags automatically map from Pydantic config schemas using kebab-case (`--flag-name`). All standalone modules accept `--log_level` for verbosity control.

### Command Pattern

```bash
uv run python -m src.<section_name>.<module_name> [FLAGS]
```

---

### Section 1: Data Preparation (`src.s1_prepare`)

#### 1. Download Dataset
```bash
uv run python -m src.s1_prepare.download [--kaggle-dataset SLUG] [--force-redownload]
```

#### 2. Preprocess Images
```bash
uv run python -m src.s1_prepare.preprocess [--scale-factor FLOAT] [--min-label-size-px FLOAT] [--black-threshold INT]
```

#### 3. Split Dataset
```bash
uv run python -m src.s1_prepare.split [--ratios RATIOS] [--seed INT]
```

#### 4. Explore Dataset
```bash
uv run python -m src.s1_prepare.explore [--input-dir PATH]
```

#### 5. Convert to COCO Format
```bash
uv run python -m src.s1_prepare.convert_coco
```

#### 6. Complete S1 Pipeline
```bash
uv run python -m src.s1_prepare.pipeline [--download DOWNLOAD] [--preprocess PREPROCESS] [--split SPLIT]
```

---

### Section 2: Data Augmentations (`src.s2_augments`)

#### Run Augmentations Pipeline
```bash
uv run python -m src.s2_augments.pipeline
```

---

### Section 3: Model Training (`src.s3_train`)

#### 1. Train YOLO26 Model
```bash
uv run python -m src.s3_train.yolo26 \
  --data-dir PATH \
  [--output-dir PATH] \
  [--model-size VARIANT] \
  [--epochs INT] \
  [--imgsz INT] \
  [--batch INT] \
  [--lr0 FLOAT] \
  [--device DEV] \
  [--freeze-layer-count INT]
```

#### 2. Train Cascade R-CNN Model
```bash
uv run python -m src.s3_train.cascade_rcnn \
  --data-dir PATH \
  [--output-dir PATH] \
  [--config-file FILE] \
  [--epochs INT] \
  [--imgsz INT] \
  [--batch-size INT] \
  [--lr FLOAT] \
  [--device DEV]
```

#### 3. Train RF-DETR Model
```bash
uv run python -m src.s3_train.rf_detr \
  --data-dir PATH \
  [--output-dir PATH] \
  [--model-size VARIANT] \
  [--epochs INT] \
  [--imgsz INT] \
  [--batch INT] \
  [--lr0 FLOAT] \
  [--device DEV]
```

#### 4. Complete S3 Pipeline
```bash
uv run python -m src.s3_train.pipeline [--models MODEL1,MODEL2] [--augments AUG1,AUG2]
```

---

### Section 4: Evaluation & Inference (`src.s4_evaluate`)

#### 1. Compute Metrics
```bash
uv run python -m src.s4_evaluate.metrics \
  --predictions PATH \
  --ground-truth PATH \
  [--model-path PATH] \
  [--data-dir PATH] \
  [--output-path PATH] \
  [--iou-threshold FLOAT] \
  [--conf-threshold FLOAT] \
  [--device DEV] \
  [--max-images INT]
```

#### 2. Run Inference
```bash
uv run python -m src.s4_evaluate.inference \
  --model-path PATH \
  --data-dir PATH \
  [--output-path PATH] \
  [--conf-threshold FLOAT] \
  [--device DEV] \
  [--max-images INT]
```

#### 3. Export Evaluation Results
```bash
uv run python -m src.s4_evaluate.export
```

#### 4. Complete S4 Pipeline
```bash
uv run python -m src.s4_evaluate.pipeline [--models MODEL1,MODEL2] [--augments AUG1,AUG2]
```

---

### Section 5: Analysis & Visualization (`src.s5_analysis`)

#### 1. Aggregate Results
```bash
uv run python -m src.s5_analysis.aggregate [--results-dir PATH]
```

#### 2. Generate Figures
```bash
uv run python -m src.s5_analysis.figures \
  --input PATH \
  [--output-dir PATH] \
  [--output-format FORMAT] \
  [--figure-dpi INT] \
  [--figure-backend STR]
```

#### 3. Complete S5 Pipeline
```bash
uv run python -m src.s5_analysis.pipeline
```

---

### Section 6: Single-Image Prediction (`src.s6_predict`)

#### Run Inference Grid on a Single Image
```bash
uv run python -m src.s6_predict.pipeline \
  --image-path PATH \
  [--output-dir PATH] \
  [--conf-threshold FLOAT]
```

---

## Logging Configuration

Control output log level globally using `--log_level`:

```bash
uv run python -m src --log_level DEBUG
```

Supported log levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

---

## Common Execution Examples

### 1. Run Data Preparation and Augmentation Stages Only
```bash
uv run python -m src --only s1_prepare s2_augments
```

### 2. Force Re-downloading and Custom Seed Splitting
```bash
uv run python -m src \
  --only s1_prepare \
  --s1_prepare download.force_redownload=true split.seed=2026
```

### 3. Fast Trial Training Run (YOLO26 with 5 Epochs)
```bash
uv run python -m src \
  --only s3_train \
  --s3_train models=yolo26 yolo26.epochs=5 yolo26.batch=8
```

### 4. Evaluate Specific Model Paradigms
```bash
uv run python -m src \
  --only s4_evaluate \
  --s4_evaluate models=rf_detr,yolo26 eval.iou_threshold=0.5
```

### 5. Generate Markdown Format Analysis Tables
```bash
uv run python -m src \
  --only s5_analysis \
  --s5_analysis analysis.output_format=markdown
```

### 6. Single-Image Prediction with All Trained Models
```bash
uv run python -m src.s6_predict.pipeline --image-path photo.jpg --conf-threshold 0.3
```
