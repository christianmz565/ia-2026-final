#import "elsearticle/elsearticle.typ": *

#set heading(numbering: "1.1")
#set text(lang: "en")
#set figure(placement: auto)

#show: elsearticle.with(
  title: "Comparative Benchmark of Object Detection Algorithms for Surface Defect Recognition in Wood",
  authors: (
    (
      name: "Chambilla Perca Ricardo Mauricio",
      affiliations: ("a",),
      corresponding: true,
      email: "rchambillap@unsa.edu.pe",
    ),
    (
      name: "Jara Mamani Mariel Alison",
      affiliations: ("a",),
      corresponding: true,
      email: "mjarama@unsa.edu.pe",
    ),
    (
      name: "Mestas Zegarra Christian Raul",
      affiliations: ("a",),
      corresponding: true,
      email: "cmestasz@unsa.edu.pe",
    ),
    (
      name: "Noa Camino Yenaro Joel",
      affiliations: ("a",),
      corresponding: true,
      email: "ynoa@unsa.edu.pe",
    ),
    (
      name: "Sequeiros Condori Luis Gustavo",
      affiliations: ("a",),
      corresponding: true,
      email: "lsequeiros@unsa.edu.pe",
    ),
  ),
  affiliations: (
    "a": [Universidad Nacional de San Agustín de Arequipa, Facultad de Ingeniería de Producción y Servicios, Arequipa, Perú],
  ),
  abstract: [
    Automated inspection of surface defects in wood faces challenges arising from severe long-tail class imbalance and high intra-class variability of organic anomalies. This article presents a comparative benchmark evaluating the intersection of three object detection paradigms: one-stage, two-stage, and transformers with four data augmentation strategies: no augmentation, Albumentations with class balancing, BoxAug with noise transformations, and BoxAug with neural harmonization via LibCom. The study is conducted on a dataset of 4,000 images with 8,736 annotations distributed across 8 defect categories, employing a reproducible five-stage pipeline with step caching. Experimental results demonstrate that Cascade R-CNN achieves the highest precision with mAP\@0.5 of 0.711, while YOLO26 exhibits the greatest sensitivity to data augmentation with a relative improvement of 16.3% over its baseline. Object-level augmentation strategies do not produce universal improvement: standard BoxAug degrades RF-DETR performance by 1.9%. Per-class analysis reveals that quartzite obtains an average precision of 0.0 with YOLO26 baseline, highlighting the critical impact of class imbalance. The reasons for the absence of generalized improvement are discussed and future directions are proposed, including class weighting and diffusion-based augmentation.
  ],
  keywords: (
    "defect detection",
    "computer vision",
    "deep learning",
    "wood processing",
    "comparative benchmark",
  ),
  format: "5p",
  paper: "a4",
  lang: "en",
)

// ============================================================
// 1. INTRODUCTION
// ============================================================

= Introduction <sec:intro>

Modern industrial manufacturing depends on automated quality control systems to maintain operational efficiency and reduce costs in supply chains @yang2020using. The integration of computer vision and machine learning technologies has transformed industrial inspection processes, enabling anomaly detection at speeds and precision levels that surpass manual methods @czimmermann2020visual. Quality inspection automation has become an essential component of Industry 4.0, particularly in sectors where natural material variability hinders the standardization of production processes @Ramos2021Industry4. The wood industry represents a significant economic sector globally, where wood constitutes a renewable resource of high structural and commercial importance @Yin2021Drying. Wood processing involves multiple stages from sawing to final finishing, and in each stage material quality directly determines its value and applicability @Chen2023Recognition. Total wood utilization in production processes reaches only between 50% and 70% of volume, due to the presence of defects that must be identified and removed @Chen2023Recognition. This waste rate highlights the urgent need for more efficient inspection systems that maximize resource utilization @Kryl2020Inspection. The integration of these systems in automated plants coordinates with robotic arms and autonomous material handling cells @Ericsson2021Quality.

Automated recognition of surface defects in wood presents specific technical challenges that distinguish it from other object detection applications @Shah2026Review. Surface anomalies encompass live knots, dead knots, drying cracks, resin pockets, fungal stains, and mechanical damage @Chen2023Recognition. The high intra-class variance of defects, where the same anomaly type can exhibit very different visual appearances, constitutes one of the main obstacles @Kodytek2022Dataset. The low contrast between certain defects and healthy wood grain hinders precise segmentation of anomalous regions @minaee2022survey. Variable lighting conditions in sawmill environments, combined with production line speeds that can reach 9.6 m/s, impose strict requirements on inference times of detection algorithms @Kodytek2022Dataset. Additionally, industrial datasets suffer from severe long-tail class imbalance, where rare defects such as marrow or missing knots are underrepresented compared to the high prevalence of standard knots @Kodytek2022Dataset. These factors converge into a research problem that requires specialized algorithmic solutions with high spatial localization and low latency @prunella2023deep.

Historically, wood defect inspection relied on trained personnel who visually examined surfaces for imperfections @Kryl2020Inspection. This manual approach presents significant limitations in terms of speed, consistency, and scalability @Kryl2020Inspection. Operator visual fatigue, subjectivity in evaluation, and inability to process large volumes of material in real time are recurring problems that affect process reliability @Kryl2020Inspection. Previous studies have demonstrated that manual inspection rarely exceeds 70% accuracy in high-speed industrial environments @Kodytek2022Dataset. To overcome these deficiencies, the state of the art evolved progressively from systems based on optoelectronic sensors and classical computer vision @ren2022state. Classical approaches used image processing techniques such as gray-level co-occurrence matrices, local binary patterns, and oriented gradient descriptors (HOG) @dalal2005hog, combined with support vector machine (SVM) classifiers @sugiarto2017wood, @nurthohari2019wood. The Viola-Jones framework @viola2001rapid represented a pioneering advance in real-time object detection using Haar-like features @lienhart2002extended and AdaBoost cascade classifiers @arxiv2022tracking. Image matching evolved from handcrafted descriptors (SIFT, SURF, HOG) to deep hierarchical representations @ma2021image. However, while these classical methods offer interpretability, their ability to handle the high natural variability and low contrast of organic surface defects in wood is severely limited @prunella2023deep.

The transition to deep convolutional neural networks (CNN) has enabled automatic extraction of hierarchical features that capture complex spatial patterns @alzubaidi2021review. The contemporary technological ecosystem offers frameworks for developing high-performance deep detectors @jiao2019survey. Deep convolution-based architectures evolved through two-stage region detectors such as Faster R-CNN @ren2016faster and Mask R-CNN @he2017mask, as well as anchor-based one-stage detectors such as Single Shot MultiBox Detector (SSD) @liu2016ssd, Feature Pyramid Networks (FPN) @lin2017fpn and anchor-free models such as FCOS @tian2019fcos. The YOLO family drove real-time detection from its early versions YOLOv1 @redmon2016yolo, YOLOv2 @redmon2017yolo9000, YOLOv3 @redmon2018yolov3, YOLOv4 @bochkovskiy2020yolov4, to comprehensive revisions of the YOLO paradigm from YOLOv1 to YOLOv8 @hussain2023yolo. More recently, Vision Transformer (ViT)-based models introduced global self-attention mechanisms that capture long-range spatial dependencies in industrial visual inspection @hutten2022vision.

Facing classical descriptors and legacy detectors, the current state of the art demands rigorous evaluation of cutting-edge deep paradigms combined with synthetic data balancing techniques. Advanced convolutional architectures such as Cascade R-CNN @cai2018cascade provide multi-stage bounding box refinement, while YOLO26 @jocher2026ultralyticsyolo26unifiedrealtime incorporates a dual-head design for end-to-end real-time inference without NMS stage and MuSGD optimizer @jocher2026ultralyticsyolo26unifiedrealtime. In the transformer domain, RF-DETR @robinson2026rfdetrneuralarchitecturesearch establishes the precision and latency frontier through neural architecture search @robinson2026rfdetrneuralarchitecturesearch. In parallel, object augmentation techniques (BoxAug @LEE2022104138, Simple Copy-Paste @ghiasi2021simple) integrated with deep composition frameworks and neural harmonization (LibCom @niu2021making, PCT-Net @Guerreiro_2023_CVPR, Latent Bridge Matching @chadebec2025lbmlatentbridgematching) enable mitigating class imbalance without introducing visual artifacts. The main objective of this article is to provide a 3-by-4 matrix evaluation that intersects these three deep paradigms with four data augmentation strategies in surface defect recognition in wood.

The remainder of the article is organized as follows. @sec:related presents related work on wood defect detection using deep learning techniques. @sec:methods describes the materials and methods used, including theoretical foundations, tools and technologies employed, dataset characteristics, and the proposed development method. @sec:results details the obtained results, including performance metrics and comparative analysis. @sec:discussion interprets the main findings, comparing them with existing literature and analyzing the interactions between architectures and augmentation strategies. @sec:conclusions summarizes the study contributions. Finally, @sec:future presents future work and possible research extensions.

// ============================================================
// 2. RELATED WORK
// ============================================================

= Related Work <sec:related>

Urbonas et al. @urbonas2019automated addressed the automated identification of defects on wood veneer surfaces using the Faster R-CNN architecture with transfer learning and data augmentation techniques. The objective was to evaluate the viability of pre-trained region proposal networks for defect detection in a controlled industrial setting. The main contribution was demonstrating that transfer learning with ResNet152 models achieves 96.1% accuracy in combined defect classification. The methodology employed four pre-trained neural networks, AlexNet, VGG16, BNInception, and ResNet152, with data augmentation through rotation and flipping. Results showed that ResNet152 obtained the best performance with 80.6% accuracy in individual defect classification. As a deficiency, the study was limited to a dataset of 4,729 images with only 353 defective samples, which restricted result generalization.

Fang et al. @fang2021yolov5knots proposed an automated system for precise detection of surface knots in sawn wood using the YOLO-v5 model. The objective was to develop a real-time detector capable of identifying multiple knot types with high precision. The contribution was the validation of YOLO-v5 as an efficient alternative to two-stage detectors for wood inspection. The methodology consisted of fine-tuning YOLO-v5 with two wood knot datasets, evaluating precision, recall, and F1-score metrics. Results achieved an F-Score of 91.7% on the first dataset and 97.7% on the second, outperforming YOLO-v3 SPP and Faster R-CNN in speed and model size. The identified deficiency was that the model was evaluated only on the knot class, without considering other defect types such as cracks or stains.

Han et al. @han2023improved presented an improved version of the YOLOv5 algorithm for surface defect detection in wood, incorporating attention mechanisms in the architecture. The objective was to improve the model's ability to detect small and low-contrast defects. The main contribution was the integration of attention modules that allow the model to focus on relevant image regions. The methodology modified YOLOv5's backbone and neck with spatial and channel attention layers. Results demonstrated significant improvements in small defect detection compared to the base model. The deficiency was the lack of standardized comparison with other state-of-the-art detectors on the same dataset.

Zheng et al. @zheng2024gbcdyolo developed GBCD-YOLO, a lightweight and high-precision model for wood defect detection, based on architectural modifications of YOLOv5s. The objective was to reduce computational complexity while maintaining detection precision. The contribution was the combination of Ghost Bottleneck blocks, BiFormer attention, CARAFE upsampling, and DyHead dynamics with CIoU loss. The methodology included architecture optimization and evaluation on a wood defect dataset with 10 categories. Results showed an mAP\@0.5 of 88.72%, a 13.45% improvement over base YOLOv5s, with 15.49% parameter reduction and 6.25% FPS increase. The deficiency was that the model was not compared with transformer-based architectures or two-stage detectors.

Zheng et al. @cwbyolo2024 proposed CWB-YOLOv8, an improvement of the YOLOv8 algorithm through the incorporation of Parametric Conditional Convolution, Wise-IoU, and BiFormer for wood defect detection. The objective was to improve detection capability for defects varying in size and appearance. The main contribution was the combination of three modules that improve feature extraction, the loss function, and multi-scale attention. The methodology employed a custom dataset of 6,134 images with defects from radiata pine, eucalyptus, and Tuna tree species. Results achieved an mAP\@0.5 of 89.2%, with 3.5% improvement over standard YOLOv8 and precise crack detection with 96% recall and resin with 93% recall. The deficiency was the absence of computational efficiency metrics evaluation such as real-time latency.

Sun @wood2022multicriteria implemented a wood quality defect detection system based on deep learning and a multi-criteria framework. The objective was to develop a system that combined automatic defect detection with a multi-criteria evaluation system for quality classification. The contribution was the integration of a multi-criteria decision framework with deep neural networks for comprehensive wood quality evaluation. The methodology used CNN for internal defect detection combined with multi-criteria analysis for quality classification. Results reported a 99.8% detection rate for internal defects and an average IOU of 74.3%. The deficiency was that the study focused on internal defects without extensive validation on public reference datasets.

Kilic et al. @kilic2025wd presented WD Detector, a deep learning-based hybrid sensor design for wood defect detection, combining CNN feature extraction with classical machine learning classifiers. The objective was to develop a hybrid system leveraging the strengths of both deep learning and traditional machine learning. The contribution was demonstrating that combining Xception-extracted features with classifiers such as CatBoost outperforms pure CNNs. The methodology employed Xception for feature extraction and 12 ML classifiers for final classification. Results achieved 99.32% accuracy with CatBoost as the best classifier. The deficiency was that the system requires a two-stage pipeline that increases implementation complexity.

Ji et al. @ji2024online developed a deep learning-based algorithm for online detection of small target defects in large-format sawn wood. The objective was to solve the problem of detecting small defects in high-resolution images of industrial planks. The contribution was the integration of ELAN (Efficient Layer Aggregation Network) with YOLO and image stitching using SIFT to handle large-format wood processing. The methodology combined SIFT keypoint detection for image joining with a modified YOLO architecture for small defect detection. Results reported 90.37% accuracy with a processing speed of 40 m/min. The deficiency was the dependence on the SIFT algorithm for image stitching, which can be computationally expensive in high-speed environments.

Wolszczak et al. @wolszczak2024bluestain addressed the detection of blue stains caused by fungi in a wood inspection system in sawmills, using neural networks trained for automatic classification of this specific defect type. The objective was to develop an automated system capable of identifying blue stains on wood surfaces during the production process. The contribution was the specific application of neural networks for a defect type particularly difficult to detect by traditional methods. The methodology employed a neural network trained with blue stain images captured in a real industrial environment. Results demonstrated the feasibility of the approach for automated detection of this defect type. The deficiency was that the study was limited to a single defect category without evaluating performance in a multi-class scenario.

Chen et al. @chen2022edgeglued proposed a defect detection system in edge-glued wood panels using deep learning techniques. The objective was to develop a WDD-DL system combining image processing filters with neural network classification. The contribution was the combination of Gabor filters, Harris corner detection, and mathematical morphology with the InceptionResNetV2 network for classification. The methodology implemented a two-stage pipeline: pre-processing with classical filters and classification with CNN. Results achieved 0.97 accuracy, 0.90 recall, and 0.92 F1-score. The deficiency was the complexity of the two-stage pipeline that hinders real-time implementation.

Shah et al. @Shah2026Review conducted a comprehensive review of automated defect detection in wood surface inspection, comparing one-stage models (YOLO and variants) and two-stage models (Faster R-CNN), and investigating emerging zero-shot learning approaches. The objective was to provide an overview of the state of the art in wood defect detection. The contribution was the systematic comparison of one-stage and two-stage models, plus the introduction of zero-shot approaches based on vision-language models such as CLIP. The methodology reviewed recent literature, analyzed public datasets, and compared performance metrics. Results showed that YOLO models are preferred for real-time applications, while Faster R-CNN offers higher precision at the cost of speed. The deficiency was that the review did not include transformer-based models as representatives of the new generation of detectors. @fig:tabla-resumen summarizes the reviewed works in the literature. None of the existing studies evaluate the cross-matrix between the three detection paradigms and advanced object augmentation techniques with neural harmonization under severe class imbalance.

#figure(
  table(
    columns: (1fr, 1.1fr, 1fr, 1fr),
    align: (left, left, center, center),
    table.header([Author], [Approach], [Main Metric], [Deficiency]),
    [Urbonas et al. @urbonas2019automated], [Faster R-CNN + TL], [96.1% acc.], [Small dataset],
    [Fang et al. @fang2021yolov5knots], [YOLO-v5], [97.7% F1], [Knots only],
    [Han et al. @han2023improved], [YOLOv5 + attention], [Improvement over base], [No comparison],
    [Zheng et al. @zheng2024gbcdyolo], [GBCD-YOLO], [88.7% mAP], [No transformers],
    [Zheng et al. @cwbyolo2024], [CWB-YOLOv8], [89.2% mAP], [No efficiency metrics],
    [Sun @wood2022multicriteria], [CNN + multi-criteria], [99.8% det.], [Limited dataset],
    [Kilic et al. @kilic2025wd], [Xception + ML], [99.3% acc.], [Two-stage pipeline],
    [Ji et al. @ji2024online], [YOLO + ELAN + SIFT], [90.4% acc.], [SIFT dependence],
    [Wolszczak et al. @wolszczak2024bluestain], [Neural network], [Binary classif.], [Single class only],
    [Chen et al. @chen2022edgeglued], [Filters + InceptionResNet], [0.92 F1], [Complex pipeline],
    [Shah et al. @Shah2026Review], [General review], [Qualitative comparison], [No empirical matrix benchmark],
  ),
  caption: [Comparative summary of related works on wood defect detection.],
  scope: "parent",
  kind: table,

) <fig:tabla-resumen>

// ============================================================
// 3. MATERIALS AND METHODS
// ============================================================

= Materials and Methods <sec:methods>

== Theoretical Foundations <sec:fundamentals>

Surface defect formation in wood responds to physiological tree factors and mechanical stresses during processing @Yin2021Drying. Live knots correspond to branch bases integrated into woody tissue, while dead knots represent separated branches that generate discontinuous cavities @Chen2023Recognition. Cracks originate from perpendicular tensile stresses during material drying phases @Yin2021Drying. Resin accumulations, central marrow, and quartzite mineral inclusions alter the physical homogeneity of the surface @Chen2023Recognition. Modern production lines move planed planks at linear speeds of 9.6 m/s before line scan cameras @Kodytek2022Dataset. The time available to capture, process, and classify each image is restricted to intervals of a few milliseconds @Kodytek2022Dataset. High variability in the background wood grain decreases the visual contrast of defective regions @Chen2023Recognition.

Data collection in industrial environments produces annotated sets with severe class imbalance @zhang2021deep. In a long-tail distribution, a reduced fraction of categories accounts for the majority of observations @zhang2021deep. The imbalance ratio measures the relationship between the frequency of the majority class and the minority class. In datasets with a ratio exceeding 30, standard loss functions become dominated by gradients from dominant categories @cui2019classbalanced. The neural network suppresses predictions of rare categories by assigning them deficient confidence scores @tan2020equalization. This phenomenon causes a collapse in the model's discriminative capability for infrequent but structurally dangerous anomalies @wang2021seesaw.

Object-level data augmentation directly modifies the frequency distribution of annotated classes @LEE2022104138. Unlike global affine transformations, the BoxAug technique isolates cropped patches belonging to tail categories @LEE2022104138. Patches are multiplied by applying stochastic scale, rotation, and horizontal flip transformations @LEE2022104138. Through the Simple Copy-Paste procedure, transformed patches are reinserted into training images with low defect density @ghiasi2021simple. To eliminate visual discontinuities from direct pasting, the LibCom framework provides deep composition algorithms @niu2021making. The PCT-Net model estimates pixel-level color transformations to equalize regional luminance @Guerreiro_2023_CVPR. The Latent Bridge Matching method applies a latent space mapping to generate shadows and photometric adaptations in a single inference step @chadebec2025lbmlatentbridgematching. The resulting synthetic samples preserve location labels while offering photometric coherence with the receiving wood @capogrosso2024diffusion.

Cascade R-CNN represents the two-stage convolutional architecture oriented toward high spatial precision @cai2018cascade. The first stage employs a Region Proposal Network to select candidates over convolutional feature maps. The second stage executes a sequence of detection heads trained with progressively stricter Intersection over Union thresholds. This cascaded design gradually refines bounding box coordinates and minimizes false positives in high-defect-density scenarios @cai2018cascade. The computational cost associated with multi-stage refinement translates to longer inference times compared to one-stage detectors, but the localization precision gain justifies its application in scenarios where false positive rate is critical @cai2018cascade.

YOLO26 represents the one-stage convolutional architecture designed for real-time inference @jocher2026ultralyticsyolo26unifiedrealtime. It adopts an anchor-free formulation that directly predicts bounding box centers and dimensions from multi-scale feature maps. Its dual-head design eliminates the need for the non-maximum suppression stage in inference, optimizing processing speed and computational latency @jocher2026ultralyticsyolo26unifiedrealtime. The absence of the NMS stage significantly reduces post-processing time, which is advantageous for real-time applications where every millisecond is critical @jocher2026ultralyticsyolo26unifiedrealtime. However, one-stage architectures may be more susceptible to insufficient training data compared to two-stage detectors.

RF-DETR represents the Vision Transformer-based architecture optimized for real-time detection @robinson2026rfdetrneuralarchitecturesearch. It uses bidirectional global self-attention mechanisms to capture long-range spatial dependencies across the entire image surface @zhao2023detrs. Through Neural Architecture Search, RF-DETR discovers optimal structural configurations on the Pareto frontier between localization precision and processing latency @robinson2026rfdetrneuralarchitecturesearch. Unlike purely convolutional detectors, transformers process the complete image through tokenization and self-attention layers, enabling them to model global relationships between distant regions @zhao2023detrs. This capability is particularly relevant for wood inspection, where defects can be distributed sparsely along the plank surface.

Performance quantification of object detectors integrates spatial precision and computational efficiency metrics @Shah2026Review. Precision measures the proportion of correct positive predictions, while recall evaluates the proportion of actual defects detected @Shah2026Review. The F1 score represents the harmonic mean of both metrics. Intersection over Union evaluates spatial overlap between predicted and actual annotations. Mean average precision mAP\@0.5 and mAP\@0.5:0.95 aggregates performance across multiple overlap thresholds, isolating algorithmic strengths in imbalanced classes @Shah2026Review. Computational efficiency metrics include inference time expressed in milliseconds per image, throughput in frames per second, number of floating-point parameters in millions, and model size stored on disk in megabytes @prunella2023deep.

== Tools and Technologies <sec:tools>

The experiment pipeline development runs on the Python programming language version 3.12. The main deep learning framework corresponds to PyTorch version 2.7.0 with GPU acceleration via CUDA 12.8 libraries. Supplementary computer vision operations employ torchvision version 0.22.0. The Cascade R-CNN architecture is implemented through the MMDetection library version 3.2.0, supported by MMCV version 2.2.0 and MMEngine version 0.10.7. The YOLO26 detector and RT-DETR detector run using the Ultralytics framework version 8.2.0. The RF-DETR architecture is compiled from the official RF-DETR engine version 1.3.0.

Synthetic data processing and photometric augmentations use Albumentations version 1.4.0. Composition and object insertion primitives employ the LibCom library version 0.2.0 integrated in the development environment. Strict pipeline configuration management is programmed via Pydantic version 2.6.1. Accelerated metadata table manipulation uses Polars version 1.43.0 and OpenCV version 5.0.0. The virtual environment and dependency resolution are managed through the uv package manager version 0.6+. All models were trained and evaluated on an NVIDIA RTX 5070 Ti GPU, which establishes the reference point for inference time and computational performance measurements reported in this study.

== Dataset <sec:dataset>

The study uses the filtered and annotated version in YOLO format available on Kaggle @Nomihsa2024KaggleWood, derived from the original Large-scale Image Dataset of Wood Surface Defects published by Kodytek et al. @Kodytek2022Dataset. The original dataset was acquired in a real industrial environment during sawmill production using a JAI SW-4000TL-PMCL line scan camera at a line frequency of 66 kHz @Kodytek2022Dataset. The filtered version used in this work @Nomihsa2024KaggleWood has been preprocessed to exclusively include images containing defects, and its annotations have been converted to the standard YOLO format for direct evaluation of object detection models. The filtered dataset contains a total of 4,000 JPG images with a fixed spatial resolution of 2800 by 1024 pixels @Nomihsa2024KaggleWood. The set stores 8,736 annotated bounding boxes distributed across 8 surface defect categories. On average, each image contains 2.18 defects, reaching a maximum of 15 defects per image. @fig:piechart-clases illustrates the percentage frequency distribution for each defect class.

#figure(
  image("figures/dataset/barchart_classes.svg", width: 95%),
  caption: [Defect class distribution in the filtered dataset @Nomihsa2024KaggleWood.],
  kind: image,
) <fig:piechart-clases>

The annotations provide normalized bounding box coordinates in YOLO format. The class distribution reflects real industrial production conditions @Kodytek2022Dataset. Majority categories correspond to live knots with 3,905 annotations (44.7%) and dead knots with 2,835 annotations (32.5%), combining 77.2% of the set. Intermediate categories include resin with 639 annotations (7.3%), cracks with 505 annotations (5.8%), and knots with cracks with 410 annotations (4.7%). Minority categories comprise marrow with 204 annotations (2.3%), quartzite with 129 annotations (1.5%), and missing knots with 109 annotations (1.2%). The calculated imbalance ratio reaches an approximate value of 35.82. @fig:defectos-ejemplo shows representative examples of the eight annotated defect categories in the dataset.

#[
  #set image(width: 95%)
  #figure(
    grid(
      columns: 4,
      rows: 2,
      gutter: 4pt,
      image("figures/dataset/Live_Knot.jpg"), image("figures/dataset/Dead_Knot.jpg"),
      image("figures/dataset/resin.jpg"), image("figures/dataset/knot_with_crack.jpg"),
      image("figures/dataset/Crack.jpg"), image("figures/dataset/Marrow.jpg"),
      image("figures/dataset/Quartzity.jpg"), image("figures/dataset/Knot_missing.jpg"),
    ),
    caption: [Examples of the eight defect classes annotated in the wood dataset @Nomihsa2024KaggleWood.],
    kind: image,
    scope: "parent",
  ) <fig:defectos-ejemplo>
]

== Proposed Method <sec:proposed>

The proposed method implements a five-stage experiment pipeline designed to ensure reproducibility and fair comparability between configurations. The stages comprise: (1) data preparation, (2) data augmentation, (3) model training, (4) evaluation, and (5) results analysis. Each stage runs independently through a step caching system that stores intermediate results on disk, enabling partial re-execution without reprocessing complete stages. Caching is existence-based: after any code or configuration change the pipeline is re-run end to end with forced execution, and every cache hit is logged with the requesting configuration fingerprint so stale reuse is auditable. The entire pipeline configuration is managed through typed Pydantic models that guarantee parameter validation at compile time @colvin2024pydantic. The command-line interface allows customization of any nested parameter through dot notation, facilitating reproducible experimentation. All random number generators (Python, NumPy, PyTorch) are seeded from a single master seed with fixed per-stage stream ids; cudnn benchmarking and TF32 remain enabled, so small residual run-to-run jitter is disclosed rather than eliminated.

The data preparation stage applies three sequential operations on the raw dataset. First, black edges are cropped through Otsu thresholding segmentation @otsu1979threshold and morphological closing operations, isolating the valid region of the wood plank. Second, images are reduced to half their original resolution through area interpolation. Third, bounding box annotations are transformed to the resulting coordinate space and filtered by a three-rule size gate (minimum absolute dimension 2.0 px unless area reaches 12.0 px² or the major dimension reaches 6.0 px, preserving thin cracks while dropping unusable specks). The resulting set is partitioned into 80% training, 10% validation, and 10% test through greedy iterative stratification that preserves class distribution in each partition @kubat2000addressing. To alleviate imbalance, 35% of training planks containing only the two majority defect classes are then dropped; this intentionally shifts training priors away from the natural validation and test distributions, so reduced majority-class scores are expected even when the balancing works.

Three augmentation strategies were evaluated designed to mitigate class imbalance, aimed at achieving a 33% ratio between the minority and majority class. Each strategy grows the training set by synthesizing minority-class instances, so augmented training sizes differ from the original by design and dataset size is reported per strategy. For the paradigm comparison, three representative architectures of each object detection approach were configured. Evaluation is performed on the test set of 400 images using COCO-standard mAP\@0.5 and mAP\@0.5:0.95, per-class AP\@0.5, and operating-point precision, recall, and F1 at a shared confidence threshold of 0.5 (greedy IoU >= 0.5 matching). Inference time is measured by averaging total processing time across all test set images.

All architectures are trained with effective-number class weighting @cui2019classbalanced (beta 0.999, normalized to mean 1.0, recomputed from each training split) injected into each model's classification loss, using each model's standard loss function otherwise. While techniques such as Focal Loss @lin2017focal and Seesaw Loss @wang2021seesaw target the same imbalance, the study fixes a single loss-level treatment so that augmentation effects remain attributable, leaving alternative loss strategies as future work. Models are evaluated at the shared 0.5 operating point with each model inferring at its own training resolution, so input-size handling cannot favor any paradigm.

Albumentations with class balancing employs six active pixel-level transformations with the following application probabilities: horizontal flip at 0.5, vertical flip at 0.5, rotation-scale-translation at 0.5, random contrast and brightness at 0.4, color variation at 0.3, and Gaussian blur at 0.2 (90° rotation is disabled at 0.0 to preserve the fixed wide-plank aspect). Dataset generation identifies rare classes below the target threshold and selectively augments images containing them, appending the synthesized images to the training set.

Standard BoxAug implements an object cut-and-paste approach. For each rare class, it crops instances from a pre-built object bank, applies stochastic patch-level transformations including scale jitter between 0.8 and 1.2, rotation, flipping, random cropping, different noise types, and morphological operations, and pastes them at valid spatial positions calculated from class-specific location guides. Each run regenerates from a clean copy of the training split and accumulates pastes in memory before writing, with capped placement retries that raise on exhaustion. Spatial guides encode domain knowledge: for example, missing knots tend to be located at image edges, while quartzite appears predominantly in the central region.

BoxAug with LibCom uses the same cut-and-paste procedure as standard BoxAug, but replaces direct insertion with deep composition through the LibCom library @niu2021making. Border operations employ neural harmonization modes that eliminate visual discontinuities at the margins between background and overlaid image. Geometric transformations are limited to scale jitter and horizontal/vertical flipping, excluding pixel-level noise transformations. The default blending mode is Poisson composition; every paste records its effective blending mode in a run manifest so degraded runs are visible.

Cascade R-CNN represents the two-stage paradigm. It has a convolutional architecture based on ResNet-50 with Feature Pyramid Network (FPN) @cai2018cascade. It is trained for 24 epochs following the standard MMDetection 2x schedule with AdamW optimizer with learning rate of 0.0001 and weight decay of 0.0001, batch size of 8 and input resolution of 960 by 384 pixels preserving aspect ratio. Validation evaluation runs each epoch using the COCO bbox metric with early stopping at patience 15 and minimum improvement 0.005, and the checkpoint with highest mAP bbox is selected. This relatively conservative training configuration with low learning rate seeks to exploit the multi-stage refinement capabilities of the architecture without risk of divergence @cai2018cascade.

YOLO26 represents the one-stage paradigm. It has an anchor-free convolutional architecture with dual-head design that eliminates the NMS stage @jocher2026ultralyticsyolo26unifiedrealtime. It is configured with the yolo26m variant, rectangular training resolution of 960 by 384 pixels, batch size of 16 and initial learning rate of 0.01. Training uses early stopping with the Ultralytics default patience of 100 epochs and saves checkpoints every 5 epochs. The maximum number of epochs is 100.

RF-DETR represents the transformer-based paradigm. It has an architecture with neural architecture search @robinson2026rfdetrneuralarchitecturesearch. The rfdetr-m variant is used with resolution of 512 by 512 pixels, batch size of 8, learning rate of 0.0001 and weight decay of 1e-4. Training includes warmup of 5 epochs, early stopping with patience of 15 per official guidance, and gradient checkpointing to reduce memory consumption. The maximum number of epochs is 50.

= Results <sec:results>

@fig:matrix-map50 presents the mAP\@0.5 performance matrix for the 12 model-augmentation strategy combinations. Cascade R-CNN dominates the top row with values between 0.701 and 0.711, showing minimal variation between augmentation strategies with a range of 0.010. RF-DETR occupies the middle position with values between 0.633 and 0.668, and YOLO26 shows the greatest dispersion with values between 0.539 and 0.626. This pattern indicates that augmentation sensitivity varies significantly between paradigms, with one-stage detectors being more receptive to data transformations than two-stage detectors.

#figure(
  image("figures/results/aug_paradigm_map50_heatmap.png", width: 95%),
  caption: [mAP\@0.5 performance matrix intersecting three detection paradigms with four augmentation strategies.],
  kind: image,
) <fig:matrix-map50>

@fig:tabla-principal summarizes the complete metrics for all 12 configurations. Cascade R-CNN with Albumentations achieves the highest mAP\@0.5 of 0.711, while Cascade R-CNN with BoxAug LibCom reaches the best mAP\@0.5:0.95 of 0.409, the highest precision of 0.546, and the best F1 of 0.471. YOLO26 baseline presents the lowest performance across all metrics, with mAP\@0.5 of 0.539 and F1 of 0.307. These results confirm that Cascade R-CNN offers the best spatial localization, while YOLO26 has greater room for improvement through data augmentation.

#figure(
  table(
    columns: (1fr, 1fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr),
    align: (left, left, center, center, center, center, center),
    table.header([Model], [Augmentation], [mAP\@50], [mAP\@50:95], [Precision], [Recall], [F1]),
    [Cascade R-CNN], [Albumentations], [0.711], [0.400], [0.495], [0.396], [0.440],
    [Cascade R-CNN], [Baseline], [0.704], [0.400], [0.494], [0.406], [0.446],
    [Cascade R-CNN], [BoxAug LibCom], [0.702], [0.409], [0.546], [0.414], [0.471],
    [Cascade R-CNN], [BoxAug Std], [0.701], [0.406], [0.542], [0.411], [0.468],
    [RF-DETR], [Albumentations], [0.668], [0.377], [0.508], [0.391], [0.442],
    [RF-DETR], [Baseline], [0.646], [0.371], [0.493], [0.366], [0.420],
    [RF-DETR], [BoxAug LibCom], [0.648], [0.384], [0.505], [0.368], [0.426],
    [RF-DETR], [BoxAug Std], [0.633], [0.367], [0.479], [0.367], [0.416],
    [YOLO26], [Albumentations], [0.618], [0.348], [0.482], [0.357], [0.410],
    [YOLO26], [Baseline], [0.539], [0.286], [0.333], [0.284], [0.307],
    [YOLO26], [BoxAug LibCom], [0.605], [0.341], [0.403], [0.334], [0.365],
    [YOLO26], [BoxAug Std], [0.626], [0.350], [0.433], [0.341], [0.381],
  ),
  caption: [Performance metrics on the test set for all 12 benchmark configurations.],
  scope: "parent",
  kind: table,

) <fig:tabla-principal>

@fig:delta-baseline shows the impact of each augmentation strategy relative to the baseline for each model. YOLO26 presents the greatest augmentation sensitivity: Albumentations contributes +0.080, BoxAug LibCom +0.067, and standard BoxAug +0.088 absolute improvement in mAP\@0.5. In contrast, Cascade R-CNN is practically insensitive: the three strategies produce changes within the range of -0.003 to +0.007. RF-DETR shows mixed behavior: Albumentations contributes +0.022, but standard BoxAug degrades performance by -0.012.

#figure(
  image("figures/results/aug_delta_vs_baseline.png", width: 95%),
  caption: [Impact of augmentation strategies relative to baseline (Δ mAP\@0.5).],
  kind: image,
) <fig:delta-baseline>

@fig:heatmap-clase presents the average AP per class in mAP\@0.5:0.95 for all 12 configurations. The easiest class is marrow, with AP up to 0.506 with Cascade R-CNN, while quartzite is the hardest, with AP between 0.0 and 0.153. YOLO26 baseline and YOLO26 standard BoxAug obtain AP = 0.0 for quartzite, indicating complete detection failure for this class. Live knots and dead knots show moderate AP values of 0.198 to 0.250 despite being the majority classes, suggesting high intra-class variance.

#figure(
  image("figures/results/per_class_ap_heatmap.png", width: 95%),
  caption: [Heatmap of average precision per defect class (AP\@0.5:0.95).],
  kind: image,
) <fig:heatmap-clase>

@fig:velocidad-precision illustrates the trade-off between inference speed and precision. YOLO26 processes each image in 5.4 ms on average across the four configurations, RF-DETR in 10.3 ms, and Cascade R-CNN in 24.5 ms. Cascade R-CNN is 4.5 times slower than YOLO26 but achieves 14.2% higher mAP\@0.5. RF-DETR offers an intermediate point with 10.3 ms and average mAP\@0.5 of 0.649.

#figure(
  image("figures/results/speed_accuracy_tradeoff.png", width: 95%),
  caption: [Trade-off between inference speed (ms/image) and precision (mAP\@0.5).],
  kind: image,
) <fig:velocidad-precision>

@fig:curvas-convergencia shows the mAP\@0.5 validation convergence curves throughout training epochs. RF-DETR converges earlier, with best epoch between 8 and 21, Cascade R-CNN stabilizes around epoch 9 and 12, and YOLO26 requires more epochs to reach its maximum, between 16 and 28. YOLO26 curves show greater oscillation, particularly in the standard BoxAug configuration. This convergence pattern suggests that transformers need fewer iterations to capture relevant features, while one-stage convolutional architectures require more epochs to stabilize their weights. The oscillation in YOLO26 may indicate sensitivity to training sample variability in each batch.

#figure(
  image("figures/results/training_curves_map.png", width: 95%),
  caption: [mAP\@0.5 validation convergence curves during training.],
  kind: image,
) <fig:curvas-convergencia>

@fig:tiempo-entrenamiento compares total training time per configuration. YOLO26 is the most efficient, between 0.24 and 0.37 hours, followed by Cascade R-CNN, between 0.46 and 0.49 hours, and RF-DETR, between 0.40 and 0.68 hours. RF-DETR training time varies significantly between configurations due to early stopping: the baseline trains 31 epochs for 0.68 h while Albumentations trains only 18 epochs for 0.40 h. This variability in RF-DETR indicates that data augmentation can accelerate convergence by providing more representative samples.

#figure(
  image("figures/results/training_time_comparison.png", width: 95%),
  caption: [Comparison of total training time per configuration.],
  kind: image,
) <fig:tiempo-entrenamiento>

= Discussion <sec:discussion>

The results obtained in this benchmark reveal patterns that warrant detailed analysis of the interactions between detection architectures and data augmentation strategies in the context of severe class imbalance typical of industrial wood inspection. Cascade R-CNN's superiority in absolute precision, with mAP\@0.5 of 0.711, is consistent with its two-stage design oriented toward high spatial localization @cai2018cascade. The progressive bounding box refinement mechanism through the Region Proposal Network and cascaded heads with increasing Intersection over Union thresholds minimizes false positives in high-defect-density scenarios @cai2018cascade. However, Cascade R-CNN's insensitivity to augmentation strategies, with variations within the range of -0.003 to +0.007 in mAP\@0.5, indicates that two-stage architectures with greater representational capacity may be limited by factors other than data volume, such as network architecture or standard loss function.

YOLO26 presents the greatest sensitivity to data augmentation, with relative improvements of up to 16.3% over its baseline, going from mAP\@0.5 of 0.539 to 0.626 with standard BoxAug. This behavior is consistent with literature indicating that one-stage detectors are more dependent on training data volume @hussain2023yolo. Augmentation effectively mitigates underrepresentation of rare classes for this architecture, as evidenced by quartzite improvement from AP = 0.0 in baseline to AP = 0.192 with standard BoxAug. The greater oscillation observed in YOLO26 convergence curves, particularly in the standard BoxAug configuration, may be attributed to variability introduced by synthetic samples in a model that lacks Cascade R-CNN's multi-stage refinement mechanism. This result suggests that one-stage detectors are the primary beneficiaries of object augmentation techniques in severe imbalance scenarios.

RF-DETR shows mixed behavior: Albumentations improves performance by +0.022, but standard BoxAug degrades it by -0.012. This result is particularly relevant for the research community in transformers for industrial vision @hutten2022vision. Patch-level noise transformations introduce artifacts that bidirectional global self-attention mechanisms interpret as relevant patterns, generating confusion during training. Unlike convolutional models that process local information through sliding filters, transformers capture long-range spatial dependencies that can amplify the influence of local artifacts @zhao2023detrs. This result suggests that object augmentation strategies require careful adaptation when applied to self-attention-based architectures.

Per-class analysis reveals counterintuitive results that challenge the assumption that class frequency directly determines detection difficulty. Quartzite, with only 129 annotations (1.5% of dataset), obtains the worst performance with AP between 0.0 and 0.153, which is expected given its low visual contrast against wood grain. However, marrow, being the second least frequent class with only 204 annotations, obtains the highest AP of up to 0.506. This disparity indicates that defect visual distinguishability is a determining factor that interacts with class frequency. Defects with distinctive visual patterns, such as marrow with its characteristic central line appearance, are more susceptible to automatic detection regardless of their representation in the dataset @Chen2023Recognition.

Live knots and dead knots, which together represent 77.2% of the dataset, show moderate AP values of 0.198 to 0.250 despite their high prevalence. This finding confirms that the high intra-class variance of these defects, where the same anomaly type can exhibit very different visual appearances @Kodytek2022Dataset, constitutes a challenge that is not resolved solely with greater data volume. Variability in the background wood grain, combined with different presentations of live and dead knots, generates a feature distribution that hinders model convergence toward robust discriminative representations. The absence of class weighting in loss functions amplifies the effect of imbalance, particularly visible in quartzite, which obtains AP = 0.0 with YOLO26 baseline. This result confirms that data augmentation alone is insufficient for classes with less than 2% dataset representation @cui2019classbalanced. The combination of data-level augmentation techniques with loss strategies such as Focal Loss @lin2017focal or Seesaw Loss @wang2021seesaw could offer a more comprehensive solution for severe class imbalance.

In terms of computational efficiency, the speed-precision trade-off manifests differentially across the three paradigms. YOLO26 offers the best speed-precision ratio for real-time deployment at 5.4 ms per image and mAP\@0.5 of 0.626, which is relevant for production lines with speeds up to 9.6 m/s @Kodytek2022Dataset. Cascade R-CNN is preferred when precision is prioritized over latency at 24.5 ms per image and mAP\@0.5 of 0.711, being 4.5 times slower than YOLO26. RF-DETR offers an intermediate point at 10.3 ms and average mAP\@0.5 of 0.649, positioning itself as a viable alternative for applications where the speed-precision trade-off must be balanced with the ability to capture long-range spatial dependencies. The selection of the optimal architecture will depend on the specific requirements of the industrial application, considering factors such as production line speed, false positive tolerance, and available computational resources.

= Conclusions <sec:conclusions>

This study presented a comparative benchmark of three object detection paradigms with four data augmentation strategies for surface defect recognition in wood, evaluating 12 configurations on a dataset with severe imbalance of 1 to 35.82. The main results demonstrate that Cascade R-CNN achieves the highest absolute precision with mAP\@0.5 of 0.711, YOLO26 presents the greatest augmentation sensitivity with a relative improvement of 16.3%, and RF-DETR shows mixed behavior where standard BoxAug degrades performance. Per-class analysis reveals that detection difficulty depends on both frequency and visual distinguishability of the defect. Data augmentation alone proves insufficient for classes with less than 2% dataset representation, underscoring the need for complementary class weighting strategies.

= Limitations and Future Work <sec:future>

The results of this study open several promising research directions. The most immediate direction corresponds to incorporating class weighting in loss functions. Techniques such as Focal Loss @lin2017focal, class-balanced loss @cui2019classbalanced, and Seesaw Loss @wang2021seesaw are specifically designed to mitigate bias toward majority classes. Given that quartzite obtains AP = 0.0 with YOLO26 baseline, the combination of data augmentation with class weighting could recover instances of this class that are currently completely lost. The second priority direction corresponds to diffusion-based augmentation. The cut-and-paste methods evaluated, such as BoxAug, are limited by the number of rare instances available for cropping from the original dataset. With only 129 quartzite annotations, the object bank is too small to generate diverse augmentation. Conditional diffusion models such as Stable Diffusion with ControlNet can generate synthetic instances of rare classes without relying on existing crops, offering a potentially more effective alternative for severe imbalance @capogrosso2024diffusion.

Expanding the dataset to other wood species with different grain patterns and defects is essential to validate generalization beyond the current species and industrial environment. In parallel, model quantization to INT8 and FP16 could reduce inference times for deployment on production lines with hardware constraints, while evaluating transformer architectures such as DINO and Grounding DINO could determine whether global self-attention mechanisms improve detection of low-contrast defects. The combination of multiple research directions, including class weighting, diffusion-based augmentation, and model optimization, could lead to more robust and efficient inspection systems for the wood industry. These future directions seek to address the limitations identified in the present benchmark and bring automated detection systems closer to the operational requirements of wood processing plants. The development of reproducible experimental pipelines, such as the one employed in this study, will facilitate comparative evaluation of new techniques emerging from these research directions.

#heading(numbering: none)[Author Contribution Statement]
Chambilla Perca R.M. declares roles in Software and Writing. Jara Mamani M.A. declares roles in Data Curation, Resources, and Methodology. Mestas Zegarra C.R. declares roles in Project Administration, Conceptualization, and Writing. Noa Camino Y.J. declares roles in Acquisition and Investigation. Sequeiros Condori L.G. declares roles in Conceptualization, Investigation, and Software.

#heading(numbering: none)[Conflict of Interest Declaration]

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this article.


#heading(numbering: none)[Ethics Declaration]

This study does not involve any experiments with humans or animals, so no ethical authorization was required. Therefore, it is not appropriate to include an ethics statement.
.
#heading(numbering: none)[Consent for Participation]

Not applicable

#heading(numbering: none)[Consent for Publication]

Not applicable

#heading(numbering: none)[Funding]

Not applicable

#heading(numbering: none)[Acknowledgments]

Not applicable

#heading(numbering: none)[Code Availability]

Custom analysis scripts and source code generated during this study are publicly available at the GitHub repository: https://github.com/christianmz565/ia-2026-final, licensed under the AGPL-3.0 license.

#heading(numbering: none)[Data Availability]

The data used in this study are publicly available on Kaggle: https://www.kaggle.com/datasets/nomihsa965/large-scale-image-dataset-of-wood-surface-defects, licensed under the CC BY 4.0 license.

#bibliography("references.bib", style: "ieee", title: [References])
