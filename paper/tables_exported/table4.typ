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
  #text(weight: "bold", size: 11pt)[Table 4: Per-class recall with simultaneous 95% family-wise CIs (Bonferroni) for the best configuration of each paradigm, with test support $n$]
]
#v(6pt)

#table(
  columns: (110pt, 125pt, 125pt, 125pt, 40pt),
  stroke: none,
  align: (left, center, center, center, center),
  table.hline(stroke: 1.2pt),
  table.header(
    [#strong("Class")], [#strong("RF-DETR (Alb.)")], [#strong("Cascade (LibCom)")], [#strong("YOLO26 (Base.)")], [#strong([$n$])]
  ),
  table.hline(stroke: 0.6pt),
  [Quartzite],       [0.733 [0.389, 0.922]], [0.467 [0.190, 0.766]], [0.400 [0.149, 0.718]], [15],
  [Live Knot],       [0.754 [0.691, 0.809]], [0.792 [0.731, 0.843]], [0.729 [0.664, 0.786]], [395],
  [Marrow],          [0.857 [0.561, 0.966]], [0.857 [0.561, 0.966]], [0.905 [0.614, 0.983]], [21],
  [Resin],           [0.891 [0.741, 0.959]], [0.813 [0.649, 0.910]], [0.703 [0.533, 0.831]], [64],
  [Dead Knot],       [0.767 [0.692, 0.828]], [0.763 [0.688, 0.825]], [0.788 [0.715, 0.846]], [287],
  [Knot with Crack], [0.787 [0.591, 0.905]], [0.766 [0.568, 0.891]], [0.702 [0.503, 0.846]], [47],
  [Missing Knot],    [0.833 [0.441, 0.969]], [0.750 [0.369, 0.939]], [0.417 [0.142, 0.756]], [12],
  [Crack],           [0.922 [0.758, 0.978]], [0.902 [0.733, 0.969]], [0.706 [0.515, 0.845]], [51],
  table.hline(stroke: 1.2pt)
)
