#set page(
  width: auto,
  height: auto,
  margin: (x: 1.5cm, y: 1cm),
  fill: white
)
#set text(
  font: "Liberation Serif",
  size: 10pt
)

#align(center)[
  #text(weight: "bold", size: 11pt)[Table 3: Performance metrics on the test set for all 12 benchmark configurations]
]
#v(6pt)

#table(
  columns: (110pt, 110pt, 65pt, 80pt, 65pt, 65pt, 65pt),
  stroke: none,
  align: (left, left, center, center, center, center, center),
  table.hline(stroke: 1.2pt),
  table.header(
    [#strong("Model")], [#strong("Augmentation")], [#strong("mAP@50")], [#strong("mAP@50:95")], [#strong("Precision")], [#strong("Recall")], [#strong("F1")]
  ),
  table.hline(stroke: 0.6pt),
  [Cascade R-CNN], [Albumentations], [0.652], [0.380], [0.789], [0.785], [0.787],
  [Cascade R-CNN], [Baseline],       [0.644], [0.386], [0.797], [0.765], [0.780],
  [Cascade R-CNN], [BoxAug LibCom],  [0.677], [0.401], [0.811], [0.785], [0.798],
  [Cascade R-CNN], [BoxAug Std],     [0.659], [0.389], [0.796], [0.773], [0.784],
  table.hline(stroke: 0.4pt),
  [RF-DETR],       [Albumentations], [0.717], [0.425], [0.684], [0.782], [0.730],
  [RF-DETR],       [Baseline],       [0.700], [0.420], [0.667], [0.794], [0.725],
  [RF-DETR],       [BoxAug LibCom],  [0.686], [0.406], [0.665], [0.796], [0.725],
  [RF-DETR],       [BoxAug Std],     [0.676], [0.405], [0.660], [0.794], [0.721],
  table.hline(stroke: 0.4pt),
  [YOLO26],        [Albumentations], [0.598], [0.355], [0.742], [0.748], [0.745],
  [YOLO26],        [Baseline],       [0.618], [0.363], [0.769], [0.738], [0.753],
  [YOLO26],        [BoxAug LibCom],  [0.592], [0.349], [0.760], [0.740], [0.750],
  [YOLO26],        [BoxAug Std],     [0.604], [0.358], [0.754], [0.765], [0.759],
  table.hline(stroke: 1.2pt)
)
