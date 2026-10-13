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

#box(width: 174mm)[
  #align(center)[
    #text(weight: "bold", size: 11pt)[Figure 2: Examples of the eight defect classes annotated in the wood dataset: Live Knot, Dead Knot, Resin, Knot with Crack, Crack, Marrow, Quartzite, and Missing Knot (left to right, top to bottom)]
  ]
  #v(6pt)

  #grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 4pt,
  image("/paper/figures/dataset/Live_Knot.jpg", width: 100%),
  image("/paper/figures/dataset/Dead_Knot.jpg", width: 100%),
  image("/paper/figures/dataset/resin.jpg", width: 100%),
  image("/paper/figures/dataset/knot_with_crack.jpg", width: 100%),
  image("/paper/figures/dataset/Crack.jpg", width: 100%),
  image("/paper/figures/dataset/Marrow.jpg", width: 100%),
  image("/paper/figures/dataset/Quartzity.jpg", width: 100%),
  image("/paper/figures/dataset/Knot_missing.jpg", width: 100%),
)
]
