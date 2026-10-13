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
  #text(weight: "bold", size: 11pt)[Table 2: Training hyperparameters per paradigm]
]
#v(6pt)

#table(
  columns: (180pt, 140pt, 220pt),
  stroke: none,
  align: (left, left, left),
  table.hline(stroke: 1.2pt),
  table.header(
    [#strong("Model")], [#strong("Parameter")], [#strong("Value")]
  ),
  table.hline(stroke: 0.6pt),
  table.cell(rowspan: 7)[Cascade R-CNN (ResNet-50 + FPN)], [Input resolution], [$960 times 384$, keep-ratio],
  [Batch size], [8],
  [Optimizer], [AdamW (adapted for fine-tuning; 1x uses SGD)],
  [Learning rate], [$1 times 10^(-4)$],
  [Weight decay], [$1 times 10^(-4)$],
  [Schedule], [LinearLR warmup + MultiStepLR],
  [Epoch budget], [12 (MMDetection 1x), patience 8, min-delta 0.005],
  table.hline(stroke: 0.4pt),
  table.cell(rowspan: 6)[YOLO26m (anchor-free, dual-head)], [Input resolution], [$960 times 384$ rectangular],
  [Batch size], [16],
  [Optimizer], [Ultralytics default (auto), MuSGD design],
  [Initial learning rate (lr0)], [0.01 (Ultralytics default)],
  [Precision], [AMP FP16],
  [Epoch budget], [50, patience 50 (effectively off), checkpoint every 5],
  table.hline(stroke: 0.4pt),
  table.cell(rowspan: 7)[RF-DETR-m (NAS transformer)], [Input canvas], [$960 times 384$ rectangular],
  [Batch size], [8],
  [Optimizer], [AdamW (official default)],
  [Learning rate], [$1 times 10^(-4)$ (official default)],
  [Weight decay], [$1 times 10^(-4)$ (official default)],
  [Warmup], [5 epochs (explicit stabilization; official default 0)],
  [Memory], [Gradient checkpointing],
  [Epoch budget], [max 50, actual 21--23, patience 15, min-delta 0.005],
  table.hline(stroke: 1.2pt)
)
