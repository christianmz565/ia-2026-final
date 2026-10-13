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
  #text(weight: "bold", size: 11pt)[Table 1: Comparative summary of related works on wood defect detection]
]
#v(6pt)

#table(
  columns: (130pt, 140pt, 110pt, 140pt),
  stroke: none,
  align: (left, left, left, left),
  table.hline(stroke: 1.2pt),
  table.header(
    [#strong("Author")], [#strong("Approach")], [#strong("Main Metric")], [#strong("Deficiency")]
  ),
  table.hline(stroke: 0.6pt),
  [Urbonas et al. (2019)], [Faster R-CNN + TL], [96.1% acc.], [Small dataset],
  [Fang et al. (2021)], [YOLO-v5], [97.7% F1], [Knots only],
  [Han et al. (2023)], [YOLOv5 + attention], [Improvement over base], [No comparison],
  [Zheng et al. (2024)], [GBCD-YOLO], [88.7% mAP], [No transformers],
  [CWB-YOLO (2024)], [CWB-YOLOv8], [89.2% mAP], [No efficiency metrics],
  [Wood et al. (2022)], [CNN + multi-criteria], [99.8% det.], [Limited dataset],
  [Kilic et al. (2025)], [Xception + ML], [99.3% acc.], [Two-stage pipeline],
  [Ji et al. (2024)], [YOLO + ELAN + SIFT], [90.4% acc.], [SIFT dependence],
  [Wolszczak et al. (2024)], [Neural network], [Binary classif.], [Single class only],
  [Chen et al. (2022)], [Filters + InceptionResNet], [0.92 F1], [Complex pipeline],
  [Shah et al. (2026)], [General review], [Qualitative comparison], [No empirical matrix benchmark],
  table.hline(stroke: 1.2pt)
)
