from pathlib import Path

import cv2

PROJECT_ROOT = Path(__file__).parents[3]
IMAGES_DIR = PROJECT_ROOT / "partial" / "s1_integration" / "s1_download" / "wood_defects" / "Images - 1" / "Images - 1"
LABELS_DIR = (
    PROJECT_ROOT
    / "partial"
    / "s1_integration"
    / "s1_download"
    / "wood_defects"
    / "Bounding Boxes - YOLO Format - 1"
    / "Bounding Boxes - YOLO Format - 1"
)
OUTPUT_DIR = PROJECT_ROOT / "paper" / "figures" / "dataset"

WOOD_DEFECT_CLASSES = [
    "Quartzity",
    "Live_Knot",
    "Marrow",
    "resin",
    "Dead_Knot",
    "knot_with_crack",
    "Knot_missing",
    "Crack",
]

BBOX_COLOR = (0, 0, 255)
BBOX_THICKNESS = 6
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 1.8
FONT_THICKNESS = 4

BORDER_MARGIN = 0.05
MIN_AREA_RATIO = 0.005


def parse_label(label_path: Path) -> list[tuple[int, float, float, float, float]]:
    boxes = []
    if not label_path.exists():
        return boxes
    for line in label_path.read_text().strip().splitlines():
        parts = line.strip().split()
        if len(parts) != 5:
            continue
        class_id = int(parts[0])
        coords = [float(x) for x in parts[1:]]
        boxes.append((class_id, *coords))
    return boxes


def score_box(x_center: float, y_center: float, w: float, h: float, img_w: int, img_h: int) -> float:
    area_ratio = (w * img_w) * (h * img_h) / (img_w * img_h)

    dist_x = min(x_center, 1.0 - x_center)
    dist_y = min(y_center, 1.0 - y_center)
    border_penalty = min(dist_x, dist_y) / BORDER_MARGIN
    border_penalty = min(border_penalty, 1.0)

    if area_ratio < MIN_AREA_RATIO:
        size_score = 0.0
    elif area_ratio < 0.02:
        size_score = area_ratio / 0.02
    else:
        size_score = 1.0

    return size_score * 0.6 + border_penalty * 0.4


def find_best_representative(class_id: int) -> tuple[Path, list] | None:
    candidates = []
    for label_file in sorted(LABELS_DIR.glob("*.txt")):
        boxes = parse_label(label_file)
        if not boxes:
            continue

        if not all(b[0] == class_id for b in boxes):
            continue

        img_file = IMAGES_DIR / (label_file.stem + ".jpg")
        if not img_file.exists():
            continue

        img_w, img_h = 2800, 1024

        best_box_score = max(score_box(b[1], b[2], b[3], b[4], img_w, img_h) for b in boxes)
        box_count_penalty = 1.0 / len(boxes)
        total_score = best_box_score * 0.7 + box_count_penalty * 0.3

        candidates.append((total_score, img_file, boxes))

    if not candidates:
        return None

    candidates.sort(key=lambda x: -x[0])
    _, img_file, boxes = candidates[0]
    return img_file, boxes


def draw_boxes(img_path: Path, boxes: list, class_id: int, output_path: Path) -> None:
    img = cv2.imread(str(img_path))
    if img is None:
        print(f"  ERROR: Could not read {img_path}")
        return

    h, w = img.shape[:2]

    for box in boxes:
        _, xc, yc, bw, bh = box
        x1 = int((xc - bw / 2) * w)
        y1 = int((yc - bh / 2) * h)
        x2 = int((xc + bw / 2) * w)
        y2 = int((yc + bh / 2) * h)

        cv2.rectangle(img, (x1, y1), (x2, y2), BBOX_COLOR, BBOX_THICKNESS)

        label = WOOD_DEFECT_CLASSES[class_id]
        (tw, th), baseline = cv2.getTextSize(label, FONT, FONT_SCALE, FONT_THICKNESS)
        tx = x2 - tw
        label_h = th + baseline + 8
        ty = y1 - baseline - 4 if y1 - label_h >= 0 else y2 + baseline + 4
        cv2.rectangle(img, (tx - 4, ty - th - 4), (tx + tw + 4, ty + 4), BBOX_COLOR, -1)
        cv2.putText(img, label, (tx, ty), FONT, FONT_SCALE, (255, 255, 255), FONT_THICKNESS)

    cv2.imwrite(str(output_path), img, [cv2.IMWRITE_JPEG_QUALITY, 95])


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for class_id, class_name in enumerate(WOOD_DEFECT_CLASSES):
        print(f"Processing class {class_id}: {class_name}...")
        result = find_best_representative(class_id)
        if result is None:
            print(f"  WARNING: No suitable image found for {class_name}")
            continue

        img_file, boxes = result
        out_path = OUTPUT_DIR / f"{class_name}.jpg"
        draw_boxes(img_file, boxes, class_id, out_path)
        print(f"  Saved: {out_path.name} (from {img_file.name}, {len(boxes)} box(es))")

    print("Done.")


if __name__ == "__main__":
    main()
