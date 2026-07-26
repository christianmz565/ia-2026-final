# Fetching Training Results

This guide documents how to synchronize training results from the remote machine (`will-pc`) to the local `results/` directory while excluding intermediate checkpoint files and retaining only the final/best checkpoints along with logs, metrics, and configurations.

---

## 🚀 Quick Command

Run the following command from the project root:

```bash
rsync -avz --delete-excluded \
  --include="epoch_12.pth" \
  --include="epoch_20.pth" \
  --include="epoch30.pt" \
  --exclude="epoch_*.pth" \
  --exclude="checkpoint0*.pth" \
  --exclude="epoch*.pt" \
  root@will-pc:/home/velmork/dev/ia-2026-teo/partials/s3_train/ results/
```

> **Note:** To preview changes before transferring or deleting files, append `--dry-run --itemize-changes` to the command.

---

## 🔍 Model Checkpoint Breakdown

The remote directory `root@will-pc:/home/velmork/dev/ia-2026-teo/partials/s3_train/` contains results for three baseline models:

| Model | Remote Subdirectory | Excluded Intermediate Checkpoints | Retained Latest & Best Checkpoints |
| :--- | :--- | :--- | :--- |
| **Cascade R-CNN** | `cascade_rcnn/baseline/` | `epoch_1.pth` – `epoch_11.pth` (root & `checkpoints/`) | `epoch_12.pth`, `best_coco_bbox_mAP_epoch_12.pth`, `best.pt`, `last_checkpoint` |
| **RF-DETR** | `rf_detr/baseline/` | `checkpoint0009.pth`, `checkpoint0019.pth`, `checkpoints/epoch_10.pth` | `checkpoint.pth`, `checkpoints/epoch_20.pth`, `checkpoint_best_*.pth`, `best.pt` |
| **YOLO26** | `yolo26/baseline/` | `weights/epoch0.pt` – `weights/epoch25.pt` | `weights/epoch30.pt`, `weights/last.pt`, `weights/best.pt`, `best.pt` |

---

## 🛠️ Command Parameters & Logic

- `-a` (`--archive`): Preserves file permissions, timestamps, symlinks, and recursive directories.
- `-v` (`--verbose`): Provides detailed transfer output.
- `-z` (`--compress`): Compresses data during transfer to reduce bandwidth usage.
- `--include="<pattern>"`: Rules evaluated **first** to explicitly allow final epoch checkpoints (e.g., `epoch_12.pth`, `epoch_20.pth`, `epoch30.pt`).
- `--exclude="<pattern>"`: Excludes intermediate epoch files (`epoch_*.pth`, `checkpoint0*.pth`, `epoch*.pt`).
- `--delete-excluded`: Deletes any previously synced intermediate files on the local target (`results/`) that match the exclude rules.
