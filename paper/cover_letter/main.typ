// Cover letter for journal submission to Machine Vision and Applications, Springer Nature
#set page(paper: "a4", margin: (x: 2.0cm, top: 1.5cm, bottom: 1.5cm))
#set text(font: "DejaVu Serif", size: 10pt, lang: "en")
#set par(justify: true, leading: 0.55em, spacing: 0.7em)

#align(right)[
  Christian Raul Mestas Zegarra \
  Systems Engineering Professional Program \
  Universidad Nacional de San Agustín \
  Arequipa 04001, Peru \
  cmestasz\@unsa.edu.pe \
  October 14, 2026
]

#v(0.5em)

Prof. Ying Wu \
Editor-in-Chief, Machine Vision and Applications \
Department of Electrical and Computer Engineering \
Northwestern University, Evanston, IL, USA \

#v(0.3em)

Dear Prof. Wu,

#v(0.3em)

We are pleased to submit our manuscript entitled “Wood Surface Defect Detection Under Severe Long-Tail Imbalance: A Comparative Benchmark of Cascade R-CNN, YOLO26, and RF-DETR” by Christian Raul Mestas Zegarra, Luis Gustavo Sequeiros Condori, Yenaro Joel Noa Camino, Mariel Alison Jara Mamani, and Yasiel Pérez Vera, for consideration as an original Research Article in Machine Vision and Applications. High-speed lumber processing presents a Industry 4.0 inspection challenge: conveyor lines transport planed timber at speeds up to 9.6 m/s, where optical automated defect detection must contend with a class imbalance ratio of approximately 35.3 to 1, high intra-class morphological variability, and subtle contrast against natural grain. In this study, we investigated how modern vision architectures across distinct design paradigms handle severe long-tail imbalance and whether neural image harmonization can systematically resolve minority-class scarcity without compromising industrial throughput.

To answer this question, we established a systematic 3-by-4 benchmark intersecting three detection paradigms, represented by two-stage Cascade R-CNN, one-stage YOLO26, and the RF-DETR vision transformer, with four augmentation strategies across 4,000 industrial timber images and 8,888 annotated defects. Because fixed confidence cutoffs distort comparisons across architectures with differing calibration behaviors, we tuned operating thresholds through validation max-F1 sweeps. Under this calibrated protocol, neural copy-paste blending using BoxAug with LibCom significantly improves minority-class recall and yields an operating F1-score of 0.798 on Cascade R-CNN alongside a 0.033 gain in mAP\@0.50, whereas one-stage detectors show distinct sensitivity requiring careful regularization. Furthermore, RF-DETR establishes superior ranking precision at 0.717 mAP\@0.50, and our latency profiling spanning 7.5 ms to 25.7 ms per image provides actionable trade-offs directly informing physical deployment choices on factory floors.

This work directly aligns with the aims and scope of Machine Vision and Applications, specifically in real-world visual inspection, industrial machine vision systems, and applied deep learning in automated manufacturing. Rather than reporting isolated evaluations on synthetic benchmarks, we deliver a systematic multi-paradigm matrix under severe industrial long-tail imbalance. We believe this work will be of high interest to the journal’s readership across automated optical inspection and applied computer vision.

We confirm that this manuscript has not been published elsewhere and is not under consideration by another journal. All authors have approved the manuscript and agree with its submission to Machine Vision and Applications. We further confirm that we have had no prior discussions with a Springer Nature editor concerning this work, and no related manuscripts are under consideration in any Springer Nature publication. Declarations regarding ethics, data availability, code availability, and competing interests are fully disclosed in the manuscript and submission portal. Christian Raul Mestas Zegarra serves as the corresponding author on behalf of all co-authors.

Thank you for your time and consideration of our submission.

#v(0.6em)

Sincerely, \
\
Christian Raul Mestas Zegarra \
On behalf of all co-authors
