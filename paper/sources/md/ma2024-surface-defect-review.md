# ma2024-surface-defect-review


<!-- Page 1 -->


Artificial Intelligence Review (2024) 57:333 https://doi.org/10.1007/s10462-024-10956-3


Surface defect inspection of industrial products with object detection deep networks: a systematic review


Yuxin Ma1 · Jiaxing Yin1 · Feng Huang1 · Qipeng Li1


Accepted: 10 September 2024 / Published online: 17 October 2024 © The Author(s) 2024


Abstract One of the focal points in industrial product defect detection lies in the utilization of deep learning-based object detection algorithms. With the continuous introduction of these algorithms and their refined models, notable achievements have been attained. However, challenges persist in industrial settings, such as substantial variations in defect scales, the delicate balance between accuracy and speed, and the detection of small objects. Various methods have been proposed to address these challenges and propel the advancement of defect detection. To comprehensively review the latest developments in deep learningbased industrial product defect detection algorithms and foster further progress, this pa­ per encompasses typical datasets and evaluation metrics used in industrial product defect detection, traces the development history of supervised one-stage and two-stage object detection algorithm-based and unsupervised algorithm-based industrial defect detection methods, discusses major challenges, and outlines future directions. It highlights the po­ tential for further improving the accuracy, speed, and reliability of defect detection sys­ tems in industrial applications.


Keywords  Defect inspection · Industrial products · Object detection · Deep networks


## 1  Introduction


As the manufacturing industry progresses, identifying surface defects in industrial products has emerged as a crucial step in guaranteeing quality, enhancing production efficiency, and minimizing costs. In industrial manufacturing, the significance of quality supervision and control is self-evident, typically representing 15–20% of total revenue (Matt et al. 2020). The precision of surface defect detection plays a vital role in ensuring the quality and reli­ ability of products (Cheng and Yu 2021). Surface defects in industrial products encompass a range of issues, including scratches, flaws, obstructions by foreign objects, and pits on the


Feng Huang


hf@zust.edu.cn


1 School of Mechanical and Energy Engineering, Zhejiang University of Science and Technology, Hangzhou 310023, China


1 3


<!-- Page 2 -->


## 333 Page 2 of 48


Y. Ma et al.


surfaces of inspected samples, which vary in size and appear against intricate backgrounds. Defect detection technologies are versatile across a broad application of industrial prod­ ucts, including steel strips, printed circuit boards (PCBs), metals, plastics, magnetic tiles, textiles, and semiconductors, among others. It boasts not only good detection precision and efficiency but also has a user-friendly and secure operational setting. However, the field of industrial defect detection still confronts numerous challenges, such as a scarcity of data, small-scale target dimensions, reduced visibility of defects, and irregular shapes, which remain to be resolved.


Traditional surface defect detection typically relies on manual inspection. Manual inspection (Lu et al. 2022) allows for focused examination of particular areas, yet it is timeconsuming and labor-intensive, resulting in diminished efficiency and high costs. Besides, manual inspection is also prone to oversights. These limitations render it increasingly inad­ equate for the evolving demands of manufacturing, especially in the face of modern largescale and high-speed production. To improve the efficiency of industrial product defect detection, the adoption of methods that detect and classify types of defects using traditional machine learning models has become widespread. Techniques like Support Vector Machines (SVM) (Li et al. 2002a), Decision Trees (Pastor-López et al. 2012), and Naive Bayes clas­ sifiers (Zhang et al. 2011) are employed. Nonetheless, these approaches primarily capture superficial image characteristics and might underperform in scenarios involving substantial variations in defect sizes, the detection of minor defects, and a wide range of defect types.


Recently, deep learning-based surface defect detection approaches have gained wide­ spread adoption for their exceptional ability to generalize across different contexts and scenarios (Luo et al. 2018). Leveraging Convolutional Neural Networks (CNN) to automat­ ically extract an object’s deep-level features has become a powerful method. This method typically utilizes general image classification, object detection, and semantic segmentation models. Object detection finds extensive application in detecting surface defects in indus­ trial products due to its ability to precisely locate defects, identify various defect types, and meet real-time, large-scale industrial inspection requirements. Common methods for object detection based on deep learning technology encompass both supervised and unsupervised approaches, which are extensively applied in defect detection on industrial product surfaces. Currently, numerous researchers are conducting in-depth studies in this area.


This review delves into the evolution of object detection deep learning architectures and the enhancement techniques of prevalent algorithms specifically tailored for defect detec­ tion in industrial products. It also introduces the widely recognized and publicly accessible datasets related to industrial product defects, and the frequently-used model performance evaluation metrics. Based on the analysis of the related deep network evolution, this study highlights critical challenges currently faced in the field of industrial product defect detec­ tion, and points out potential improvement aspects in the future. The principal contributions of our research are outlined as follows:


Offering comprehensive datasets tailored for surface defect detection within industrial contexts.


Exploring the evolution of object detection deep learning models for detecting defects in industrial products.


Summarizing the latest enhancement strategies for surface defect detection deep networks.


1 3


<!-- Page 3 -->


Page 3 of 48 333


Surface defect inspection of industrial products with object detection…


Emphasizing the deep learning research work on industrial product detection in the future.


The organization of this paper is outlined as follows: In Sect. 2, we offer an overview of the prevalent databases utilized for industrial surface defect detection, alongside an intro­ duction to the widely accepted evaluation metrics for deep network models. Section 3 pres­ ents the development of surface defect detection in industrial products using supervised learning algorithms. It provides a detailed explanation of the existing one-stage and twostage object detection models. Section 4 discusses unsupervised learning models, including AutoEncoder and Generative Adversarial Network (GAN) in detail. Section 5 engages in a thorough discussion and analysis of methodologies for enhancing deep learning-based surface defect detection on industrial products, including an exploration of the principal challenges and prospective directions for future advancements. It also discusses the com­ parison between supervised and unsupervised methods. The challenges when deploying these deep learning methods in real industry scenarios are also elaborated in this section. Finally, Sect. 6 summarizes the findings of this research.


## 2  Typical datasets and evaluation metrics


## 2.1  Typical datasets for defect detection


The ongoing progress in surface defect detection deep learning algorithms owes much to the significant contributions of extensive datasets. The efficacy of these algorithms hinges directly on the quality of the datasets they’re trained on, underscoring the importance of precise and dependable data annotation (Bagherzadeh et al. 2023). In the realm of industrial product defect detection, prominent public datasets include NEU-DET, GC10-DET, MPCG, HRIPCB, Severstal, DAGM, MT, and APDDD, along with MVTec AD. Table 1 provides


Table 1  The typical public datas­ ets for surface defect detection


Dataset Application Number Defect Category


Image Resolution Pixels NEU-DET Hot-rolled steel strip


1800 6 120 × 120


GC10-DET Steel strip 2294 10 2048 × 1000 PVMulti-Defect Solar pho­ tovoltaic panels


307 5 5800 × 3504


HRIPCB HRIPCB 1386 6 600 × 600 Severstal Strip Steel 18,074 4 1600 × 256 DAGM Textured background


16,100 6 800 × 800


MPCG Mobile phone glass


11,808


MT Magnetic tile


329 5


APDDD Aluminum 3005 10 2560 × 1920 MVTec AD Industrial products


5354 700 × 700/ 1024 × 1024


1 3


<!-- Page 4 -->


## 333 Page 4 of 48


Y. Ma et al.


a comprehensive overview of the fundamental characteristics of these datasets, whereas Fig. 1 counts the usage of these datasets in this research area.


(1)	 NEU-DET: The NEU-DET (Song and Yan 2023) dataset, provided by a team from


Northeastern University (NEU), is a specialized collection for detecting surface defects on steel plates, comprising 1,800 grayscale samples of hot-rolled steel strip surface defects. It encompasses six types of defects, including Rolled-in Scale (Rs), Patches (Pa), Cracks (Cr), Pitted Surfaces (Ps), Inclusion (In), and Scratches (Sc), with each defect type represented by 300 samples. The images are rendered at a resolution of 200 × 200 pixels. As one of the most popular datasets for steel surface defect detection, NEU-DET offers a valuable resource for evaluating algorithms in this domain, thereby facilitating research and development in the field of steel plate surface defect detection. (2)	 GC10-DET: The GC10-DET (2023) dataset is a comprehensive collection of 2294


grayscale images sourced from real-world industrial settings, specifically capturing surface defects on steel materials. This dataset categorizes ten distinct types of defects, namely Punching (Pu), Weld Lines (Wl), Crescent Gap (Cg), Water Spot (Ws), Oil Spot (Os), Silk Spot (Ss), Inclusions (In), Rolling Pits (Rp), Crease (Cr), and Waist Folding (Wf), offering an extensive resource for the development and testing of defect detection algorithms in the steel industry. (3)	 PV Multi-Defect: The PV Multi-Defect dataset (2023) is a specialized collection tai­


lored for the detection of multiple defects in solar photovoltaic (PV) panels. This data­ set is collected from original high-resolution images, each snapped by cameras from PV


Fig. 1  The statistics of the usage of the datasets in industrial product defect detection according to the references in this review


1 3


<!-- Page 5 -->


Page 5 of 48 333


Surface defect inspection of industrial products with object detection…


modules measuring 1.65 m by 0.991 m and featuring 60 cells. It serves as a crucial tool for algorithmic assessment of surface defects on solar PV panels. These defects, which include but are not limited to scratches, cracks, and stains, can significantly impair the panels’ performance and efficiency. The PV Multi-Defect dataset encompasses 307 images, each with a resolution of 5800 × 3504 pixels. The dataset provides a detailed breakdown of defect types, including Hot Spots (49.09%), Scratches (36.62%), Black Borders (6.02%), No Electricity (4.28%), and Broken (3.99%), making it a valuable resource for advancing PV panel inspection and maintenance technologies. (4)	 HRIPCB: The HRIPCB (2019) dataset, curated by the HRI Laboratory at Peking Uni­


versity, stands as a premier resource for PCB defect analysis. This dataset is a syntheti­ cally generated, publicly accessible collection of 1386 high-quality images, comprised of six defect types: Missing Hole (Mh), Mouse Bite (Mb), Open Circuit (Oc), Short (Sh), Spur (Sp), and Spurious Copper (Sc). It is tailored for advancing the detection and classification techniques specific to PCB anomalies. Each category of defect is represented by 115 images, with the dimensions of these images varying between 3034 × 2464 and 2904 × 1521 pixels, thereby offering a diverse and extensive dataset for research and development in PCB inspection technology. (5)	 Severstal: The Severstal (2020) dataset is an assembled collection designed to aid in the


detection of surface defects on steel strips. This dataset encompasses a variety of defect types, namely pitting, scratches, cracks, and plate issues. With a total of 12,568 images in the training set and an additional 5,506 in the test set, it provides a robust foundation for model training and evaluation. Specifically, the training set is balanced with 6,666 defective images and 5,902 pristine images. Each image within the dataset is presented in a high-resolution format of 1600 × 256 pixels, allowing for detailed analysis and clas­ sification of steel strip surface anomalies. (6)	 DAGM: The DAGM (2023) dataset focuses on identifying defects amidst textured


backgrounds, featuring an extensive collection of 8,050 images for both the training and testing sets. Each image within this dataset is rendered in an 800 × 800 pixels resolution. (7)	 MT: The Magnetic-tile Defect Datasets (2023), unveiled by the Institute of Automation


at the Chinese Academy of Sciences, present an extensive collection of 1,344 images. This dataset is designed to encompass a broad spectrum of the most prevalent magnetic tile defects, offering a rich resource for both original and mask images. Specifically, it includes detailed representations of porosity, fractures, cracks, wear, and uneven sur­ face textures. (8)	 APDDD: Offered by Alibaba, the Aluminum Profile Surface Detection Database (2023)


features a diverse collection of defects categorized into ten distinct types: dents, nonconductivity, abrasions, orange peel texture, coating misses, impact damage, pitting, bulging, coating cracks, and stains. This dataset includes a total of 3,005 images, each with a high resolution of 2560 × 1920 pixels. (9)	 MVTec AD: The MVTec AD (Bergmann et al. 2019) dataset is designed to simulate


real-world industrial inspection scenarios and is primarily used for unsupervised defect and anomaly detection. This dataset consists of 15 categories, with 5 categories repre­ senting different types of textures and the remaining 10 categories representing various types of objects. It includes 3,629 images for training and validation, and an additional 1,725 images for testing.


1 3


<!-- Page 6 -->


## 333 Page 6 of 48


Y. Ma et al.


## 2.2  Evaluation metrics


Evaluating the performance of deep learning models is a critical aspect of machine learning research. For a comprehensive analysis of a model’s performance and efficacy, research­ ers often rely on a suite of evaluation metrics. These metrics facilitate the categorization of subjects into positive and negative examples. True Positives (TP) denote the instances accurately predicted as positive by the model, while True Negatives (TN) reflect accurate predictions of negative instances. False Positives (FP) occur when negative instances are incorrectly classified as positive, and False Negatives (FN) occur when positive instances are mistakenly classified as negative. Based on these, key metrics utilized in the model evaluation of defect detection include Accuracy, Average Precision (AP), Mean Average Precision (mAP), Precision (P), Recall (R), and the F1 Score. Each of these metrics provides valuable insights into different facets of model performance, as defined below:


(1)	 Accuracy: The term signifies the ratio of accurately predicted samples among all sam­


ples, determined through the following formula:


Accuracy = (TP+FN) (TP+FP+TP+FN) (1)


(2)	 Precision: The term denotes the proportion of accurately detected boxes among all pre­


dicted boxes in a single image, expressed as:


Precision = TP TP+FP  (2)


(3)	 Recall: The term denotes the proportion of correctly matched ground truth instances out


of the total ground truth instances, determined through the following formula:


Recall = TP TP+FN  (3)


(4)	 F1 Score: The F1 score serves as a holistic evaluation of precision and recall, expressed


through the following formula:


Precision+Recall  (4)


F1 = 2× Precision× Recall


(5)	 AP: Average Precision, indicative of the likelihood of accurate category prediction, is


measured by the area beneath the Precision-Recall curve. Calculation formula:


P (R) dR  (5)


## AP =


Where P represents Precision, R represents Recall.


1 3


<!-- Page 7 -->


Page 7 of 48 333


Surface defect inspection of industrial products with object detection…


(6)	 mAP: The mean AP value, the area under the PR curve, also represents the probability


of predicting categories. Calculation formula:


C


## C  (6)


i=1APi


mAP =


Where C denotes the total number of categories, and APi represents the AP value of the ith category.


(7)	 Params and FPS


“Params” denotes the total count of parameters within a model, essentially the variables that need to be learned during training. In the realm of deep learning, a model’s size is largely gauged by its parameter count, as it directly influences the model’s complexity and the amount of storage it necessitates. On the other hand, FPS (Frames Per Second) is a metric utilized in computer vision to quantify the processing speed of systems or algorithms when handling images. It measures the number of frames a system can process each second, serving as a crucial benchmark for assessing the performance speed of target detection algo­ rithms. Consequently, a higher FPS indicates faster image processing capabilities.


## 3  Supervised defect detection methods


Supervised learning requires a labeled dataset for training (Liu et al. 2017). In this approach, each input data is paired with a corresponding output label. The goal of the model is to learn the relationship between inputs and outputs, allowing it to make accurate predictions on new, unseen data. Supervised defect detection methods mainly include one-stage and twostage object detection algorithms. Below is a detailed introduction to the use of these two types of algorithms.


Object detection algorithms based on deep learning can be categorized into two types based on network structure: two-stage algorithms and one-stage algorithms. Figure 2 illus­ trates the comparison between one-stage and two-stage object detection deep learning algo­ rithms. Two-stage algorithms revolve around the concept of candidate regions and involve steps such as extracting features from candidate boxes, generating a set of object proposals, and conducting object classification and regression. Notable algorithms in this category include R-CNN, Mask-RCNN, Faster-RCNN, and others. Conversely, one-stage object detection algorithms directly yield the targets’ category probabilities and positional coordi­ nates without the intermediate step of candidate region generation. Examples of prominent algorithms in this class include the YOLO series, SSD, and Retina Net, among others. The progression of surface defect detection in industrial products with one-stage and two-stage object detection deep learning algorithms is outlined in Fig. 3.


## 3.1  Two-stage defect detection methods


Two-stage object detection algorithms are structured around two principal phases: the extraction of region proposals, and the subsequent classification and accurate localization of


1 3


<!-- Page 8 -->


## 333 Page 8 of 48


Y. Ma et al.


Fig. 2  Comparison of one-stage and two-stage object detection deep learning algorithms


Fig. 3  The progression of surface defect detection in industrial products with object detection deep learn­ ing algorithms


1 3


<!-- Page 9 -->


Page 9 of 48 333


Surface defect inspection of industrial products with object detection…


these candidate areas. These distinct stages are generally executed by different components within the network, ensuring a comprehensive and precise approach to object detection.


## 3.1.1  R-CNN


The R-CNN algorithm was introduced by Girshick et al. (2014), which set a new bench­ mark for accuracy and efficiency in the field of object detection. Despite its advancements, R-CNN faces challenges, including the need to extract features from 2,000 candidate boxes, which introduces significant computational redundancy. Moreover, its scaling process can distort the aspect ratios of target objects, leading to information loss and a decrease in the precision of detection outcomes.


## 3.1.2  Faster-RCNN


In 2017, Ren et al. (2017) unveiled the Faster R-CNN, an evolution in object detection that replaces the selective search algorithm with a Region Proposal Network (RPN). It repre­ sents a significant advancement in the field of object detection, and has been widely applied to industrial product surface defect detection. Despite its advancements, Faster R-CNN still struggles to achieve real-time monitoring; the process of obtaining region proposals and then classifying each proposal remains computationally intensive. With continual improve­ ments by researchers and engineers, the model has shown strong performance and flexibility in adapting to various detection needs and enhancing detection efficiency. Figure 4 depicts the architecture of Faster R-CNN.


In 2019, Wei and Bi (2019) introduced an advancement to the Faster R-CNN framework by developing a new model tailored for the detection of surface defects in aluminum. By employing data augmentation techniques, they effectively expanded their dataset, enriching the diversity of defect examples. This enhanced version of the Faster R-CNN integrates the Feature Pyramid Network (FPN) principles to improve multi-scale object detection by combining features from various layers, thereby boosting the model’s defect detection capa­ bilities. Upon evaluating this innovative model on the APDDD dataset, it demonstrated remarkable performance, achieving a mAP of 75.8%, showcasing its efficacy in identifying surface defects with high precision.


In 2020, Hu and Wang (2020) unveiled a sophisticated approach that merges an optimized Faster R-CNN framework with FPN techniques, employing the Guided Anchor Region Pro­


Fig. 4  The structure diagram of Faster R-CNN


1 3


<!-- Page 10 -->


## 333 Page 10 of 48


Y. Ma et al.


posal Network (GARPN) for enhanced precision in anchor point prediction. This novel method, augmented with residual modules from ShuffleNetV2, proved to be well-suited for production environments, especially for PCB defect detection tasks. Leveraging the robust ResNet50, equipped with a FPN as its feature extraction backbone, the model exhibited decent effectiveness in identifying minute defects on PCBs. Upon deploying this advanced model for evaluating actual PCB data within a factory environment, it showcased a mAP of 95.6%, achieving a 10.4% increase in detection performance compared to the conventional Faster R-CNN. Moreover, it registered an 11.1% rise in recall and an enhancement in run­ time efficiency, with a 0.093-second reduction per image.


In 2021, Zhao et al. (2021b) made progress in refining the Faster R-CNN algorithm, crafting an innovative approach tailored for steel surface defect detection. They trans­ formed the feature extraction process by incorporating deformable convolutions, enhancing the algorithm’s ability to adapt to complex patterns. A strategic integration of FPNs facili­ tated the fusion of multi-scale features, amplifying the detection capabilities. In addition, improvements were made to Non-Maximum Suppression (NMS), a commonly used postprocessing technique in object detection that removes redundant boxes and retains the most optimal ones. The introduction of Soft NMS was crucial in reducing false positives and false negatives, thereby enhancing the precision of the detection process. Upon evaluating this enhanced algorithm on the NEU-DET dataset, it achieved a mAP of 75.2%, showcasing a leap of 12.6% over the Cascade R-CNN.


In 2021, Huang et al. (2021) unveiled a significant enhancement to the Faster R-CNN with the introduction of the innovative Cascade Tri-DFPN model, specifically designed for pinpointing defects on the outer surfaces of plastic relays. To construct a robust dataset, they leveraged advanced offline augmentation techniques, including mosaic and mixup. Mosaic technology creates a composite image by combining multiple images, while mixup enhances model performance, reduces overfitting, and improves robustness to various inputs by generating diverse training samples. They also complemented this with online methods, such as flipping and shifting. Architecturally, the model saw a refinement of the ResNet101 backbone through strategic modifications to downsampling and convolutional layers, thereby enriching the representation of multi-scale information. The integration of strengthened branch connections and the implementation of non-local feature space atten­ tion mechanisms further optimized feature fusion. Enhanced by the introduction of dense connections across feature layers, the model achieved commendable precision in defect localization. When applied to a proprietary relay dataset, this refined model achieved an impressive mAP of 88.75%, representing a substantial 13.14% improvement over the con­ ventional Faster R-CNN. Moreover, the F1-score soared to 86.70, marking an increase of 0.2222 from the original Faster-RCNN framework. Additionally, robustness testing results indicate that the proposed network can handle images with poor quality, such as those with blurriness.


In 2021, Xia et al. (2021) proposed an enhanced defect detection method for polarizer surfaces using the Faster-RCNN framework. They utilized a feature extraction network incorporating the ResNet-101 convolutional neural network with a FPN. The introduction of the Region of Interest (ROI) Align, based on the bilinear interpolation algorithm, was a key innovation. Additionally, they employed the k-means + + clustering algorithm to gener­ ate a new anchor scheme. Experiments demonstrated that this approach achieved a mAP of 93.5% on the polarizer defect dataset, marking a 23% improvement over the original


1 3


<!-- Page 11 -->


Page 11 of 48 333


Surface defect inspection of industrial products with object detection…


Faster-RCNN model. Furthermore, the FPS increased by 5.173 compared to the original Faster R-CNN model.


In 2022, Wu et al. (2022) introduced enhancements to the Faster-RCNN algorithm, tar­ geting the detection of defects on steel strips. Their innovative approach incorporated a deformable convolution module and a multi-scale detection module from the FPN into the backbone architecture. Furthermore, they enriched the RPN with the Convolutional Block Attention Module (CBAM), aiming to refine the model’s focus and thereby elevate the accuracy of steel strip surface defect detection. CBAM is a lightweight attention mechanism that enhances the feature representation of CNNs. It introduces channel and spatial atten­ tion, weighting feature maps along these dimensions to help the network focus on the most important features. Experimental results showcased on the NEU-DET dataset demonstrated a notable improvement, with the mAP achieving 79.5%, an uplift of 8.4% over previous benchmarks.


## 3.1.3  Mask R-CNN


In 2017, He et al. (2017) proposed Mask R-CNN, a model capable of not only object detec­ tion but also instance segmentation. Mask R-CNN typically replaces ROI Pooling with ROI Align. This innovative shift to ROI Align leveraged bilinear interpolation across sub-grids, significantly boosting the accuracy of object detection and facilitating instance segmenta­ tion. Despite its effectiveness, this approach was characterized by considerable annotation expenses and limitations in real-time applicability.


In 2023, Yang et al. (2023) innovatively advanced the Mask R-CNN framework by cre­ ating a novel algorithm tailored for detecting defects on metal surfaces. This enhancement strategically built upon the foundational FPN, integrating two additional bottom-up path­ ways for feature fusion, significantly amplifying the capacity for effective feature informa­ tion integration. Further sophistication was introduced to the ResNet model through the incorporation of the CBAM attention mechanism and deformable convolutions, enriching the model’s contextual awareness and adaptability. Optimizing the Intersection over Union (IOU) loss involves minimizing the error between the predicted and ground truth boxes using a defined formula, which enhances the model’s localization accuracy. The introduc­ tion of the Distance-IOU (DIOU) loss function improved detection accuracy. Rigorous test­ ing on a specialized dataset confirmed the efficacy of this enhanced algorithm, achieving a mAP of 78.6%.


In 2023, Zhu et al. (2023) developed an improved network based on the Swin Trans­ former, using Mask R-CNN as the baseline framework for detecting steel surface defects. Transformers gained significant attention in the computer vision community due to their proficiency in capturing long-range dependencies within input sequences, owing to their attention-based deep learning architecture. Swin Transformer was a self-attention-based model built on the Transformer architecture, and it demonstrated exceptional performance in the field of computer vision. They introduced a deep Multilayer Perceptron (MLP) mod­ ule that combines the feature extraction capabilities of CNN with the global dependency construction abilities of the Swin Transformer. Additionally, they proposed a Convolutional Embedding Module and an Attention Block Fusion Module to enhance feature fusion. To allow for more interaction computation of complete defects across different blocks, a novel window shifting strategy was introduced. When tested on the NEU-DET dataset, the new


1 3


<!-- Page 12 -->


## 333 Page 12 of 48


Y. Ma et al.


model achieved a mAP@0.5 of 81.2%. Additionally, testing on datasets such as GC10DET and PCB showed that the new model outperformed other models in terms of detection performance.


## 3.1.4  Cascade R-CNN


In 2018, Cai et al. (2018) introduced the innovative Cascade R-CNN framework. The Cas­ cade R-CNN method refined detection accuracy by progressively escalating the IOU thresh­ old, allowing for remarkably precise object localization and classification. By employing a cascading architecture, it diminished the dependency on high-quality anchor points and significantly enhanced the model’s ability to generalize across various scenarios. Despite its strengths, the model incurred a higher computational demand due to the layered cascading of detection phases, which not only extended the inference duration but also amplified the model’s intricacy.


In 2023, Li et al. (2023e) introduced a significant enhancement to the Cascade R-CNN framework, developing the CR-RFPR101 algorithm specifically tailored for detecting sur­ face defects on steel plates. By incorporating the ResNeXt-101-64 × 4d network into the backbone, they aimed to boost the model’s accuracy. Building upon the foundational FPN, they added a feedback mechanism and the reapplication of the backbone module, introduc­ ing the concept of a recursive feature pyramid. For feature extraction, the team opted for the Switchable Atrous Convolution (SAC) in place of traditional convolution, optimizing the receptive field for detecting steel plate surface defects. Additionally, they replaced the conventional NMS module with a Soft-NMS module based on linear weighting. The experi­ ments conducted on the NEU-DET dataset revealed that defect detection with this model achieved mAP of 83.4%, marking a 7.3% increase over the original network and surpassing YOLOv3, SSD, and Faster R-CNN by 3.7%, 3.9%, and 1.9%, respectively.


In 2023, Akhyar et al. (2023) enhanced the Cascade R-CNN algorithm by introducing the FDD algorithm tailored for detecting surface defects on steel. They integrated ResNext modules into the FPN. To accommodate the diversity of defect shapes, the team built upon the foundational architecture of Cascade R-CNN, employing deformable convolutions and deformable ROI pooling operations for refinement. A GARPN was introduced to replace the conventional RPN head, significantly improving the precision of bounding boxes. When tested across common datasets, the new model achieved mAP of 78.3% on the Severstal steel dataset, marking a 10.8% improvement over the original model. On the NEU-DET dataset, the mAP reached 83.4%, with a 4.1% increase.


## 3.1.5  Others


In 2022, Hu et al. (2022) unveiled a two-stage defect detection model, UPM-DenseNet, leveraging deep learning and computer vision to identify defects on the surface of mag­ netic tiles. This network executed both object detection and classification tasks simul­ taneously. In the first stage, a localization network processed the original image data to highlight areas potentially having defects, effectively minimizing the impact of complex backgrounds within a feasible scope. The second stage utilized the resulting feature maps as input for a classification network, which then carries out the detection of magnetic tile defects. The introduction of an on-demand Feature Restoration Module (FRM) enhanced


1 3


<!-- Page 13 -->


Page 13 of 48 333


Surface defect inspection of industrial products with object detection…


the ROI capabilities of the classification network, boosting overall performance. Moreover, the implementation of the Bottleneck Attention Module (BAM) focused the model’s atten­ tion mechanism, enabling precise defect detection on the MT defect dataset. The model achieved an accuracy rate of 96.385%, surpassing DenseNet121 by 3.639%. It operated with 26.32 million parameters at a speed of 11.109 FPS.


## 3.1.6  Summary


The analysis underscores the superior accuracy of two-stage object detection methods, par­ ticularly excelling in identifying small-sized defects and their stability under challenging conditions such as noise and obstructions. All the above two-stage object detection methods in industrial defect detection and their performance evaluations are summarized and listed in Table 2. For instance, UPM-DenseNet performed best on the same MT defect dataset, with the new model simultaneously executing object detection and classification tasks. By incorporating the BAM and FRM, the model achieved a mAP of 96.385%. Moving forward, refining the architecture and parameters of two-stage frameworks is essential to maintain precision while meeting the real-time demands of industrial environments.


Table 2  Performance comparison of two-stage surface defect detection methods Model Object Author Dataset mAP (%)


Faster-RCNN Aluminium Ruofeng Wei


Pre­ ci­ sion (%)


Recall (%)


FPS F1(%) Ac­ cra­ cy(%)


## APDDD 75.8


## PCB BING HU


Selfmanaged datasets


Steel Weidong Zhao


## NEUDET


Plastic relays Feng Huang


Selfmanaged datasets


Polarizer Yu Xia Selfmanaged datasets


Steel Jiansh­ eng Wu


## NEUDET


MASK-RCNN Metal Fan Yang Self


managed datasets


Steel Wei Zhu NEUDET


Cascade R-CNN Steel Xuelu Li NEUDET


95.6 83.7


75.2


88.57 82.4 94.58 86.7


93.5 96.9 89.8 7.042 93.2


79.5


78.6


78.2 76.5 11.6


83.4 -


Steel Akhyar Severstal 78.3 12 NEUDET


83.4 12


Other Magnetic tile Cong Hu MT 96.38


1 3


<!-- Page 14 -->


## 333 Page 14 of 48


## 3.2  One-stage defect detection methods


Y. Ma et al.


One-stage object detection algorithms are designed to identify both the location and cat­ egory of objects within an input image in a single step, eliminating the need for proposing candidate regions and enabling genuine end-to-end processing. By redefining object detec­ tion as a regression challenge, these algorithms streamline the detection process. Notable examples of one-stage models include the YOLO (You Only Look Once) and SSD (Single Shot MultiBox Detector) series, which stand as benchmarks in the field for their efficiency and accuracy. SSD (Liu et al. 2016), a one-stage detection model utilizing VGG16 architec­ ture, excels in detecting objects across sizes but faces challenges in small object detection due to sparse convolutions and increased computational demands from multi-scale feature pyramid implementation.


## 3.2.1  Defect detection with YOLO series


The YOLO series has progressed from YOLOv1 (Redmon et al. 2016) to the latest iteration, YOLOv9. YOLOv1 achieved real-time object detection, but limited each grid to predicting a single object. YOLOv2 (Redmon and Farhadi 2017) introduced an anchor mechanism to improve anchor box predictions and enhance recall rates. YOLOv3 (Redmon and Farhadi 2018) utilized the Darknet-53 network and an FPN-inspired architecture for multi-scale feature fusion. YOLOv6 (Li et al. 2022b) integrated the EfficientRep baseline and Rep-PAN bottleneck networks, adopting an anchor-free approach to improve detection accuracy. To further enhance detection accuracy, YOLOv6 employed the SimOTA (Ge et al. 2021) label­ ing strategy and SIOU (Gevorgyan 2022) bounding box regression loss, pushing perfor­ mance to a high level. In 2023, Wang et al. (2023c) introduced YOLOv7, which integrated Extended Efficient Layer Aggregation Networks (E-ELAN) and a composite model scaling method to improve network stability and accuracy. However, YOLOv7 still faces challenges in detecting small objects. In 2024, Wang et al. (2024) unveiled YOLOv9, which leverages Programmable Gradient Information (PGI) for weight adjustments and merges CSPNet and ELAN into the Generalized Efficient Layer Aggregation Network (GELAN), achieving 55.6% AP on the MS COCO dataset and surpassing YOLOv8 by 1.7%. An overview of the network architectures from YOLOv1 to YOLOv8 is shown in Fig. 5. In 2024, YOLOWorld (Cheng et al. 2024) introduced a novel Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) along with region-text contrast loss. On the challeng­ ing LVIS dataset, YOLO-World achieved a detection accuracy of 35.4 AP while maintaining an impressive speed of 52.0 FPS, outperforming many existing state-of-the-art methods.


## 3.2.2  YOLOv3


In 2020, Zhang et al. (2020) developed Classification Priority YOLOv3 DenseNet (CPYOLOv3-Dense), a variant designed for detecting surface defects on steel, building on the YOLOv3 architecture. They replaced two residual network modules with Densely Connected Convolutional Network (DenseNet) to enhance feature fusion utilization. The K-means clustering algorithm was used to analyze clusters of images in the dataset during the detection process, helping in identifying optimal anchor box sizes. Experiments on the NEU-DET dataset for defect detection showed that this new algorithm achieved mAP of


1 3


<!-- Page 15 -->


Page 15 of 48 333


Surface defect inspection of industrial products with object detection…


Fig. 5  Overview of Network Architectures for YOLOv1-YOLOv8 Series Algorithms


1 3


<!-- Page 16 -->


## 333 Page 16 of 48


Y. Ma et al.


82.73%, with an average detection time of 9.68 ms per image, outperforming the standard YOLOv3, which achieved mAP of 77.57% under the same conditions.


In 2021, Xian et al. (2021) enhanced the YOLOv3 framework by developing the YOLOv3 combined triplet loss network (YOT-Net), a specialized algorithm designed for the detec­ tion of surface defects on copper. Central to the YOT-Net architecture were three innovative modules: the Triplet Data Input Module, the YOLOv3 Module, and the LCCT (LocationConfidence-Class Probability-Triplet) Loss Module. This holistic approach yielded prog­ ress in experiments conducted on the self-built TJ-CE-DET dataset, where the YOT-Net achieved a mAP of 67.42%. This represented significant improvements over the existing models, with an 8.23% increase over YOLOv3, a 9.53% increase over Faster R-CNN, and a 7.01% increase over SSD, demonstrating the YOT-Net’s decent capability in pinpointing defects on copper surfaces.


In 2022, Chen et al. (2022) improved YOLOv3 for the purpose of online monitoring of defects on the surface of hot-rolled steel. By integrating the efficient MobileNetV2 network for feature extraction, they were able to enhance the overall speed of the network. They introduced an innovative detection approach using an Extended Feature Pyramid Network (EFPN), making it adept at detecting objects of varying sizes, and designed a Feature Fusion Module (FFM) specifically to capture intricate detail regions. Testing their refined model on the open NEU-DET dataset for hot-rolled steel yielded a mAP of 86.96%, representing a substantial improvement of 17.86% over the original YOLOv3’s mAP of 69.10%. More­ over, the model’s parameters were reduced to 107.4, decreasing by 141.8, which signifies a notable optimization in model efficiency. The new model is more accurate and faster than other comparative algorithms, enabling real-time, high-precision detection of surface defects in products.


In 2023, Jiang et al. (2023b) developed DCR-YOLO, an algorithm specifically tailored for detecting surface defects on printed circuit boards, building upon the YOLOv3 frame­ work. The core of DCR-YOLO’s backbone was designed with two Cross Residual Blocks (CR-blockbody) and a single Residual Block (R-blockbody), forming the DCR-backbone. To prevent the loss of feature information between the backbone feature extraction module and the feature fusion module, a Pooling Convolutional Residual (PCR) structure was intro­ duced. To enhance the detection capabilities for small object defects, the Same-DirectionDouble-Top Feature Pyramid Network (SDDT-FPN) feature fusion module was designed to integrate deep features into shallow ones, thereby bolstering the feature fusion layer for small object prediction heads, YOLO Head-P3. This not only strengthens shallow feature representation but also amplifies the focus on small object defect features. Additionally, a C5ECA structure comprising two convolutional structures, one residual convolution, and one Effificient Channel Attention Network (ECANet), was designed to enhance the feature extraction capability across the SDDT-FPN network layers. Experiments on the HRIPCB dataset demonstrated that DCR-YOLO achieved a mAP of 95.32%, a recall rate of 80.33%, and a frame rate of 103.15 FPS, marking a 10.14% improvement in mAP over YOLOv3 under the same experimental conditions.


## 3.2.3  YOLOv4


In 2020, Bochkovskiy et al. (2020) developed YOLOv4, an advancement built on the foun­ dation of YOLOv3. YOLOv4 delivered good detection accuracy and speed, all while ensur­


1 3


<!-- Page 17 -->


Page 17 of 48 333


Surface defect inspection of industrial products with object detection…


ing real-time processing capabilities. At its core, it employed Cross Stage Partial Network 53 (CSPDarknet53) as the backbone network, significantly boosting the model’s feature extraction prowess. CSPDarknet53 features convolutional layers, residual blocks, and CSP modules. The CSP module splits the input feature map into two parts—one for convolution and one for direct output—reducing computational load while preserving information flow. With its sophisticated integration of multi-scale features, YOLOv4 excelled in identifying objects of diverse sizes with remarkable efficiency. Although it represents a leap forward in optimization compared to its predecessors, YOLOv4’s sophisticated architecture requires considerable computational power, particularly good during its training phase.


In 2021, Liao et al. (2021) unveiled YOLOv4-MN3, a tailored algorithm designed for pinpointing surface defects on PCBs. This innovative adaptation replaced YOLOv4’s CSPDarknet53 backbone with the more streamlined MobileNetV3 network, coupled with refined optimizations to the activation functions. To ascertain the new model’s efficacy, it underwent testing on a bespoke dataset, where it demonstrated exceptional defect detec­ tion capabilities, recording mAP of 98.64% and an F1 score of 97.83%. This enhancement markedly reduced the model’s parameter count from 63.96 M to a more efficient 39.59 M, showcasing its improved performance and efficiency.


In 2021, Xin et al. (2021) advanced the YOLOv4 framework by developing a novel model tailored for pinpointing surface defects on PCBs. This enhanced model leveraged CSPDarknet53 for its backbone and integrates Spatial Pyramid Pooling (SPP) combined with Path Aggregation Network (PAN) in the neck architecture, significantly refining the model’s detection precision. SPP enhances CNNs’ capability to handle images of various sizes by pooling features across multiple scales, thus improving accuracy and robustness. PAN aggregates features from different layers to enhance resolution and contextual infor­ mation. Through rigorous testing on HRIPCB, this refined model demonstrated a remark­ able improvement in detection capability, elevating the mAP from 89.60% to an impressive 96.88%, underscoring its superior performance over the original YOLOv4. Additionally, the new method has been found to be more effective for detecting small objects.


In 2021, Zhao et al. (2021a) innovatively refined the YOLOv4 architecture to create a sophisticated model specifically designed for detecting surface defects on metal. This model strategically incorporated an FPN module following YOLOv4’s Concat module, enhancing the model’s ability to represent defect features in feature maps at both 80 × 80 and 40 × 40 resolutions. This enhancement directly contributed to improved accuracy in object detec­ tion. When tested on the selected 720 images from the NEU-DET dataset, this advanced model outperformed the original YOLOv4 framework, demonstrating a good detection mAP of 92.5%.


In 2021, Ma et al. (2022) tackled the challenges of large-scale computation and spe­ cific hardware requirements for automated defect detection in aluminum strips. They chose YOLOv4 as their architectural foundation. This network structure was primarily composed of a backbone featuring linear bottlenecks and inverse residuals, and a neck equipped with multiple SPP modules of varying scales. This configuration effectively extracted and inte­ grated defect features across different scales, enhancing detection precision and prediction efficiency. The team introduced an innovative lightweight convolutional block that merges depthwise (DW) separable convolutions (DSConv) with a dual-channel attention mecha­ nism, integrating both channel and spatial attentions into a parallel dual-channel attention module. Among them, DSConv reduced computation and model parameters by breaking


1 3


<!-- Page 18 -->


## 333 Page 18 of 48


Y. Ma et al.


down standard convolution into depthwise and pointwise operations. Embedded within the residual structure of the backbone convolutional blocks, this module boosted the network’s capability to extract spatial information. Applying the refined algorithm to aluminum strip surface defect data from the cold rolling workshop of Liuzhou Yinhai Aluminum Industry Co., Ltd., they observed mAP of 96.28%, with detection speeds tripling that of the original YOLOv4 model.


In 2022, Xie et al. (2022) crafted the FE-YOLO model, leveraging the YOLOv4 archi­ tecture for the precise identification of surface defects on both steel and PCB surfaces. By streamlining the original YOLO model with the innovative use of DSConv and dense connections, they enhanced its efficiency. The introduction of the Dense Feature Pyramid Network (DFPN), which automatically adjusted weights and integrated multi-scale features, represented a significant advancement in enhancing the model’s multi-scale detection capa­ bilities and improving the accuracy of small target detection. Furthermore, the implementa­ tion of a novel bounding box regression loss function aimed to sharpen detection precision, especially at higher IOU thresholds. The development of an improved k-means + + algo­ rithm, grounded in statistical analysis for optimal anchor box selection, resulted in a model that is approximately 80% lighter than YOLOv4. Through rigorous testing, the FE-YOLO model demonstrated outstanding defect detection performance, achieving mAP of 83.9% on the NEU-DET dataset and a good mAP of 98.9% on the DeepPCB (2018) dataset, showcas­ ing its exceptional efficacy and lightweight nature. Additionally, on the NEU-DET dataset, the model’s detection speed reached 90 FPS, further highlighting its potential for real-time defect detection applications.


In 2022, Huang et al. (2022b) innovatively refined YOLOv4, launching SO-YOLO, a cutting-edge network engineered specifically for detecting defects on the surfaces of chips. This model elevated detection efficiency through a strategic expansion of shallow feature fusion, refinement of anchor box dimensions and quantities using k-means + + clustering, and streamlining by removing superfluous branches from the YOLO head network. Dis­ tinctively, SO-YOLO differentiated itself from its predecessor by integrating the advanced PANet architecture. Tested on a dataset amassed from factory environments, SO-YOLO showcased superior capabilities in identifying smaller objects and simplifying the model’s architecture. Achieving a mAP of 82.59%, the new model registered a 0.61% improvement over the original YOLOv4.


In 2023, Li et al. (2023b) advanced the capabilities of YOLOv4 by developing the EFDYOLOv4 model, specifically engineered for the detection of surface defects on steel. This model introduced an innovative enhanced path module that integrates a convolutional encoder-decoder within residual blocks to amplify learning efficacy. Furthermore, an Effi­ cient Channel Attention (ECA) mechanism was strategically incorporated to emphasize fea­ tures with rich spatial details and suppress redundant features. For comprehensive detection tasks, the model employed three decoupled heads dedicated to classification and regression, respectively. Testing of the new model on the NEU-DET dataset revealed mAP of 79.88%, and on the GC10-DET dataset, it achieved 54.65% mAP.


In 2022, Zhu et al. (2022) innovated by merging the MobileNetV2 algorithm with a refined version of the YOLOv4 model, crafting a novel approach for pinpointing surface defects on PCBs. The new model could not only perform object detection but also clas­ sification. They tailored the backbone architecture with the introduction of ADD-path and DSCBlock-W modules, enhancing the integration of features across multiple layers


1 3


<!-- Page 19 -->


Page 19 of 48 333


Surface defect inspection of industrial products with object detection…


and maximizing the utilization of fundamental feature data. This strategic design enabled YOLOv4 to detect smaller defects with heightened accuracy. Through rigorous testing on an updated version of the public PCB defect dataset originally proposed by Ding et al. (2019), the revamped model demonstrated exceptional performance, achieving mAP of 99.71%, which represents an 18.15% improvement over the baseline model. Additionally, the mod­ el’s complexity was significantly reduced, with the parameter count dropping from 258 to 95.6, illustrating an advancement in defect detection efficiency. In 2022, Fan et al. (2022) refined YOLOv4, unveiling a novel algorithm designed for the detection of surface defects on steel. They introduced online data augmentation and the Mosaic data enhancement method to enrich the training dataset. Within YOLOv4, they incorporated the lightweight Ghost network, replacing the original CSPDarknet53 back­ bone, to accelerate detection speeds. The Ghost network is a lightweight convolutional neural network that replaced standard convolution with Ghost Modules. It decomposed standard convolution into a 1 × 1 convolution and a depthwise separable convolution to achieve efficient feature map generation and feature extraction. The integration of the CBAM attention mechanism was aimed at increasing network accuracy. Testing of the new model on the NEU-DET dataset for defect detection revealed mAP of 82.78%, signifying a 4.52% improvement over the traditional YOLOv4 model. The experimental results met expectations and have significant practical value for steel plate defect detection and improv­ ing product quality.


In 2023, Wang et al. (2023b) innovated on the YOLOv4 framework to create YOLOACG, a streamlined algorithm designed specifically for detecting surface defects on steel plates. By integrating an Atrous Spatial Pyramid Pooling (ASPP) module into the back­ bone architecture, they significantly enlarged the model’s receptive field. Additionally, the incorporation of a Channel Attention (CA) mechanism markedly improved the algorithm’s feature fusion capabilities. Through rigorous testing on the DAGM dataset, YOLO-ACG demonstrated decent performance, achieving mAP of 92.49% and FPS of 102.9, showcas­ ing its effectiveness and efficiency in defect detection tasks.


In 2023, Li et al. (2023c) advanced the YOLOv4 framework with the creation of the M2-BL-YOLOv4 model, specifically designed for the detection of surface defects on alumi­ num. This innovation reimagined the complex CSPDarkNet53 backbone of YOLOv4 with an inverted residual structure, drastically reducing the number of model parameters and enhancing detection speed. A pioneering feature fusion network, BiFPN-Lite, was devel­ oped to bolster the network’s integration capability, leading to improved detection accu­ racy. Demonstrated through rigorous testing on the APDDD dataset, this refined lightweight YOLOv4 variant achieved mAP of 93.5%. Remarkably, it managed to decrease the model’s parameter volume to just 60% of its original size while increasing the FPS rate to 52.99, thus elevating detection speed by 30%. The new model provides efficient detection of aluminum surface defects and meets real-time requirements.


## 3.2.4  YOLOv5


In 2020, Jocher (2021) built upon YOLOv4 to introduce YOLOv5, significantly enhanc­ ing both its speed and accuracy. At the input stage, YOLOv5 incorporated Mosaic data augmentation and adaptive anchor box calculation, enriching the dataset and improving the detection of small objects. Between the backbone and the final output head layer, FPN


1 3


<!-- Page 20 -->


## 333 Page 20 of 48


Y. Ma et al.


and PAN structures were inserted to enhance feature integration. The head output layer saw major improvements with the introduction of the Generalized Intersection Over Union Loss (GIOU_LOSS) for training and Distance Intersection Over Union Non-Max Suppression (DIOU_NMS) for filtering predicted boxes, optimizing the model’s precision. However, YOLOv5 still requires improvements in detecting small objects and may experience detec­ tion omissions or false positives when dealing with dense targets. Continuous refinement by researchers is necessary to enhance the model further.


In 2022, Wang et al. (2022a) introduced a novel method for detecting defects on metal surfaces using the YOLOv5 framework. During the data preprocessing stage, they utilized Mosaic for data augmentation and employed an effective loss function to tackle the challenge of detecting small-sized object defects. Building on YOLOv5, they retained the structure of CSPDarknet53 and incorporated the Focus structure to further refine the model’s capabili­ ties. To address the detection of small-sized objects, they enhanced the backbone with an additional feature layer of size 152 × 152, based on the three effective layers extracted from CSPDarknet53 (sizes 76 × 76, 38 × 38, and 19 × 19), and integrated it into the neck of the network. Following the feature extraction network, features were further extracted and aug­ mented through the SPP module and a combined FPN and PAN module. When tested on the GC10-DET dataset for defect detection, the model achieved a mAP of 74.1%, representing an 11.4% improvement over Faster R-CNN.


In 2022, Shi et al. (2022) refined the YOLOv5 algorithm, tailoring it for steel surface defect detection. This enhanced version integrated a CBAM between the Backbone and Neck phases, significantly improving the precision in identifying small-scale targets. The adaptation of the k-means clustering algorithm further augmented the model’s capability to detect objects with extreme aspect ratios effectively. This novel YOLOv5 + CBAM model, when evaluated on the NEU-DET defect detection dataset, demonstrated a notable increase in mAP by 4.57%. This advancement enabled precise localization and classification of sur­ face imperfections on steel materials.


In 2022, Guo et al. (2022) pioneered an advancement in the YOLOv5 model for steel surface defect detection by integrating Transformer-based improvements, resulting in the MSFT-YOLO model. They embedded the TRANS model, developed with Transformer technology, into both the backbone and detection head, significantly enhancing feature inte­ gration. By replacing PANet with Bi-directional Feature Pyramid Network (BiFPN) in the backbone, they facilitated better communication and fusion of feature maps across various scales. Deploying this modified MSFT-YOLO on the NEU-DET dataset for defect detec­ tion yielded mAP of 75.2%, marking a 7% increase over the traditional model and an 18% improvement over Faster R-CNN.


In 2024, Liu et al. (2024) refined the YOLOv5 algorithm for its application in detecting damage on the surface of steel cables. Within the backbone, they incorporated the Ghost­ Conv module and introduced the ShuffleC3 module, endowing the network with higher detection performance and a lighter structure. The ShuffleC3 structure enhanced feature extraction performance and reduced parameter count and computational complexity by replacing the C3 module in YOLOv5 with ShuffleNet Bottleneck, incorporating the CBAM attention mechanism, 3 × 3 convolutions, and SiLU activation function. The head section was also enhanced to reduce the network’s parameter count and computational complex­ ity, conserving computational costs while maintaining average precision in detection. When tested on the in-house Cable Damage dataset, the improved network outperformed


1 3


<!-- Page 21 -->


Page 21 of 48 333


Surface defect inspection of industrial products with object detection…


YOLOv5s by achieving a 1.1% increase in mAP. Furthermore, the parameters and compu­ tational demand were reduced by 43.4% and 31%, respectively, with the model size seeing a 42.3% reduction.


In 2023, Liang et al. (2023) advanced the YOLOv5-n algorithm specifically for the task of identifying defects in traction steel wire ropes. Their enhancements focused on streamlin­ ing the backbone network, notably by substituting the initial 6 × 6 convolutional kernel used for downsampling with a pair of 3 × 3 convolutional kernels. They further optimized the Conv-BN-SiLU module by replacing its conventional convolutional layer with a DWConv, effectively slimming down the model’s parameter footprint. Additionally, the C3 module within the backbone was augmented with the CBAM attention mechanism, sharpening the model’s focus by filtering out extraneous information. The head module saw an expansion from three to four scale detection heads, broadening its detection capabilities. Upon evalu­ ation on our proprietary dataset, this refined network demonstrated mAP@0.5 of 98.1%, surpassing the original model’s accuracy by 4.9% and achieving an 11% reduction in parameters. This upgrade ensured the model’s efficacy and efficiency in practical engineer­ ing scenarios for detecting defects in traction steel wire ropes.


In 2023, Yasir et al. (2023) introduced an enhanced real-time model for detecting surface defects on metals, based on the YOLOv5 framework. Tailored to improve detection capa­ bilities for small-sized defects, they incorporated the lightweight ShuffleNetv2 architecture, adding 3 × 3 DW convolutions and 1 × 1 convolutions within the residual branches. When evaluated on the NEU-DET surface defect dataset, the model achieved mAP@0.5 of 77.5%.


In 2023, Zhou et al. (2023a) advanced the YOLOv5s algorithm to elevate its perfor­ mance in detecting defects on metal surfaces. This innovation involved substituting the original C3 module with a CSPlayer module, a change that not only streamlined the model but also boosted its efficacy in identifying smaller objects. Global Attention Mechanism (GAM) enhanced the model’s ability to focus on small target positions, adaptively learning their size and location, which improved the accuracy of small target detection. Upon evalu­ ation using the GC10-DET dataset, this refined version of YOLOv5s demonstrated a good improvement, achieving a 5.3% increase in precision over the original YOLOv5, along with a 1.4% rise in mAP@0.5 and a 1.7% enhancement in mAP@0.5:0.95.


In 2023, Hu et al. (20232023b) innovatively enhanced the YOLOv5 algorithm, specifi­ cally tailoring it for the intricate demands of PCB defect detection. Confronting the unique challenges, such as the diminutive size and fluctuating scale of defects in PCBs, they pro­ posed the Multi-Branch Attention Mechanism (MBAM) algorithm. This novel approach was adept at harnessing feature information from varied dimensions, subsequently con­ solidating these through a process of global average pooling before concatenation. This strategic refinement culminated in achieving an impressive AP50 of 96.7%, outperforming the baseline YOLOv5’s 94.7% by a significant margin of 2% points. With detection speed remaining largely unchanged, the model can more precisely identify PCB defect types.


In 2023, Zhao et al. (2023b) made advancements to the YOLOv5 algorithm, tailoring it for the detection of surface defects on steel strips. They developed a novel, lightweight network and feature fusion algorithm, dubbed LSD-YOLOv5, which introduced a refined approach to the model’s architecture. This involved modifying the first convolution in the original backbone to an R-Stem, which was a shallow feature enhancement module called R-Stem, and incorporating a new feature extraction network, CA-MbV2, into the bottleneck structure of MobileNetV2. Additionally, a lightweight attention module, BiFPN-S, was inte­


1 3


<!-- Page 22 -->


## 333 Page 22 of 48


Y. Ma et al.


grated into the Neck to enhance feature integration and attention. The adoption of SoftDIOU-NMS for the selection of prediction frames reduced the rate of missed detections and improved the efficiency of overlapping object selection. When evaluated on the GC10DET dataset, this innovative model achieved a considerable reduction in parameters by 61.5% and computational demand by 42.8%, while detection speed increased by 28.7% and accuracy improved by 2.4%. Post-dataset analysis revealed a remarkable 27.8% increase in mAP. This shows that the model strikes an ideal balance between detection accuracy and speed, all while maintaining a lightweight structure.


In 2023, Li et al. (2023a) made an improvement to the YOLOv5 algorithm, beginning with the optimization of initial images through compression and cropping, followed by enlargement to enhance detail visibility. To bolster the detection of smaller objects, they innovatively added dedicated prediction heads and integrated the BottleneckCSP. The incorporation of GhostConv marked a stride forward in increasing computational efficiency while simultaneously reducing the model’s parameter count. By employing a combination of FPN and PAN architectures, they adeptly classified features, leading to a substantial enhancement in model performance. Upon evaluation on the PV Multi-Defect dataset, these strategic enhancements propelled the model’s mAP by at least 27.8%.


In 2023, Zhao et al. (2023a) refined the YOLOv5 algorithm by developing RDD-YOLO, specifically aimed at enhancing defect detection on steel surfaces. This innovation lev­ eraged Res2Net as its backbone to expand the receptive field, enabling the extraction of multi-scale features with greater efficiency. The model introduced a double feature pyramid network (DFPN) within its neck architecture to deepen the network’s capacity for feature integration and to effectively repurpose features from earlier layers. A distinctive decoupled head design separated the regression and classification processes, significantly boosting the model’s accuracy. On the NEU-DET and GC10-DET datasets, RDD-YOLO achieved impressive mAP scores of 81.1% and 75.2%, respectively, outperforming YOLOv5 by mar­ gins of 4.3% and 5.8%, showcasing its superior detection capabilities. RDD-YOLO met the demands for both accuracy and detection speed in their task.


In 2023, Gao et al. (2023) innovated upon the YOLOv5 framework, introducing the TWRD-NET algorithm, tailored specifically for detecting defects in traction steel wire ropes. They revamped the backbone network by enhancing the C3 module with Deeply Separable Convolutions (DSConv) and integrating a lightweight bottleneck module, LWBottleNeck, culminating in the creation of the LW-C3 module. Within the neck network, the PAN was replaced with a Cross-Level Weighted Feature Pyramid Network (CLW-FPN). Furthermore, the complete intersection over union (CIOU) loss function was modified to a β-CIOU loss function, employing a β coefficient to amplify boundary regression gradients and further minimize bounding box loss. The new model demonstrated remarkable preci­ sion on the in-house TWRD dataset, achieving an accuracy and mAP of 99.4%, which rep­ resents a 2.3% improvement over the original model, and a frame rate of 151FPS, marking a 42FPS increase. Due to its high accuracy, compact size, and fast detection speed, the new model offers valuable reference for industrial equipment quality inspectors.


In 2023, Li et al. (2023d) utilized YOLOv5s as the foundational framework to develop a novel algorithm specifically designed for detecting surface defects on magnetic tiles. To streamline the network, they replaced the original CSPDarknet of YOLOv5 with an enhanced version of the Combined EfficientNetV2 network. The CIOU loss function was substituted with the Focal-EIOU loss function to improve localization accuracy and expedite


1 3


<!-- Page 23 -->


Page 23 of 48 333


Surface defect inspection of industrial products with object detection…


convergence. They further refined the model by swapping the SE module in the Efficient­ NetV2 network for the ShuffleAttention attention mechanism and introduced a dual Shuffle­ Attention mechanism at the backend of the network for augmented focus. The adoption of the GELU activation function ensured gradient stability. When tested on the MT dataset, the algorithm achieved mAP of 82.5%, marking a 3.9% improvement over the original model, and reached a frame rate of 41.3 FPS. This performance met the practical requirements for defect detection in magnetic tile production lines within industrial settings.


In 2023, Li et al. (2023) unveiled an innovative model based on YOLOv5, specifically designed for identifying defects in hot-pressed Light Guide Plates (LGP). This model com­ bined the spatial attention mechanisms of CBAM with the channel attentiveness of ECANet to forge a Hybrid Attention Module (HAM), which was placed behind each C3 module within the backbone network. To further enhance the model, the traditional pyramid archi­ tecture was substituted with a newly devised multi-layer convolution module, effectively reducing the loss of critical feature information. The deployment of this model on indus­ trially sourced images yielded a mAP of 98.9%, marking a 1.1% enhancement over its predecessor, alongside a rapid detection capability of 417FPS, showcasing its potential for real-world industrial applications in LGP defect detection.


In 2023, Jiang et al. (2023a) made an advancement of the YOLOv5 algorithm, debuting the MA-YOLO model tailored for detecting defects on aluminum surfaces. By leveraging the K-Means + + clustering algorithm, they refined the optimization of anchor boxes, intro­ ducing a layer of precision in targeting defects. The introduction of a Multi-scale Feature Fusion Network (FFN) marked a pivotal enhancement, boosting the model’s sensitivity and adaptability to defects of varying scales. To tackle the challenges posed by high similar­ ity among defects and the distracting influences of background noise, they innovated with the Max Pooling Average Pooling (MA) attention mechanism, significantly sharpening the model’s ability to pinpoint smaller defects. The MA attention mechanism combined max pooling and average pooling operations to capture diverse spatial information from feature maps. When tested on the open APDDD dataset, the MA-YOLO model achieved an 88.1% mAP—a 2.9% uplift over its predecessor, coupled with a F1 score of 84.9%. The new model enhanced the accuracy and efficiency of aluminum profile surface defect detection while maintaining a lightweight design.


In 2023, Li et al.  (2023f) unveiled a cutting-edge algorithm specifically designed for the detection of surface defects on magnetic tiles, an enhancement based on the YOLOv5 model. This novel approach integrated the CBAM attention mechanism, considerably refin­ ing the precision of target detection. Moreover, the team introduced crucial modifications to the loss function and meticulously redefined the algorithm’s backbone by adding four detec­ tion layers, thereby enriching the network’s depth. This further enhanced the algorithm’s proficiency in identifying defects in densely crowded scenes. When tested against the MT dataset, this advanced method demonstrated an increase in mAP@0.5, surpassing the origi­ nal YOLOv5 and Faster R-CNN by 3.21% and 7.22%, respectively.


In 2023, Zhuang et al. (2023) unveiled an approach for detecting defects on plastic labels, leveraging the synergy between YOLOv5 and Generative Adversarial Networks (GAN). By introducing the Defect-GAN network, they achieved remarkable data augmentation and enhancement for small sample sets, significantly boosting the accuracy and precision of their detection efforts. When the model was deployed on a custom-collected plastic dataset


1 3


<!-- Page 24 -->


## 333 Page 24 of 48


Y. Ma et al.


from actual industrial production environments, it reached a mAP of 99.5%, representing an enhancement of 27.8% compared to the baseline model.


In 2024, Zheng et al. (2024)  enhanced the Yolov5 algorithm for defect detection and introduced MD-YOLO, a model specifically designed for detecting surface defects in com­ plex industrial environments. They developed a Multi-Channel Fusion (MCF) module to improve feature extraction capabilities. To further enhance performance in classification and regression tasks, they incorporated a dynamic head block (Dyhead Block) into the detection head. To evaluate the model’s effectiveness, they tested it on the NEU-DET dataset, where it achieved a mAP of 78.2% in defect detection.


In 2024, Yu et al. (2024) enhanced YOLOv5 and introduced LCG-YOLO, a new model specifically designed for real-time metal surface defect detection. They replaced the resid­ ual modules in the backbone with the LSandGlass (LSG) module, which improved fea­ ture extraction capabilities while maintaining low computational complexity. To optimize the architecture, they adjusted the number of network channels, modified the convolution kernel sizes, and introduced the lightweight Ghost model. Additionally, they incorporated the CBAM attention mechanism to enhance detection accuracy. Testing on a custom metal component dataset showed that the new model achieved a mAP@0.5 of 95.5%, a 5.7% improvement over the original YOLOv5 model, and increased the inference speed by 21 FPS to a total of 95 FPS.


In 2024, Li et al. (2024) proposed a new model to enhance YOLO using a hybrid atten­ tion mechanism, tailored for detecting solder joint defects in Surface Mount Technology (SMT) within industrial settings. This model built upon the Transformer’s core multi-head self-attention mechanism, introducing the Enhanced Multi-Head Self-Attention (EMSA) in their study. EMSA aimed to bolster the network’s ability to perceive contextual infor­ mation. The Coordinate Attention (CA) mechanism, which could effectively enhance the correlation between different channels and improve the network’s ability to perceive longdistance spatial information, was also introduced in the model. By integrating EMSA with the CA mechanism within the FPN, experimental results showed a 4.3% improvement in mAP compared to YOLOv5 on soldering datasets.


## 3.2.5  YOLOv7


In 2022, Wang et al.  (2020a) advanced the capabilities of the YOLOv7 model, tailoring it for the detection of surface defects on aluminum profiles. They incorporated a Deformable Feature Pyramid Network (DFPN), enhancing the model’s adaptability to the diverse shapes of defects. By employing the K-means clustering algorithm, they optimized the dimensions of the anchor boxes to better match the defect profiles. When applied to the APDDD dataset, the refined model achieved a mAP of 76.92%, demonstrating its improved performance in identifying surface defects on aluminum profiles.


In 2022, Wang et al. (2022b) enhanced the YOLOv7 model for the purpose of detect­ ing surface defects on steel strips. Within the backbone of the model, the ECA (Efficient Channel Attention) mechanism was integrated to direct the model’s focus more effectively. The introduction of a reweighted BiFPN significantly improved the model’s capability in feature fusion, thereby reducing the loss of information during convolution processes. By replacing the CIOU loss function with the SIOU loss function, the model’s efficiency in handling minor defects saw improvement. Testing on two datasets, GC10-DET and NEU


1 3


<!-- Page 25 -->


Page 25 of 48 333


Surface defect inspection of industrial products with object detection…


DET, yielded good results. On the GC10-DET dataset, the model achieved mAP of 80.2%, marking an improvement of 4.6% over the original model. Similarly, on the NEU-DET dataset, the mAP reached 81.9%, also surpassing the original model’s performance by 4.6%.


In 2023, Zhang et al. (2024) made an advancement to the YOLOv7 algorithm, targeting the detection of surface defects on steel. They replaced the first and last E-ELAN modules within the backbone’s feature extraction network with ConvNeXt-CBS modules, enhancing the model’s ability to extract relevant features. Furthermore, within the feature fusion net­ work, the YOLOv7’s E-ELAN modules were upgraded to the more advanced C3 modules from YOLOv5. Comprising CBS and Bottleneck Blocks, the C3 modules facilitated the learning of defect features across a broader range of scales. By incorporating the SimAM attention mechanism into Multi-Path Convolution (MPConv), and creating the MPCS mod­ ule, they reduced the occurrence of false positives and negatives. This refined model, when tested on the NEU-DET dataset, achieved mAP of 80.2%, indicating a 3.9% increase in performance compared to theYOLOv7.


In 2023, Chen et al. (2023) made improvements to the YOLOv7 framework, tailoring it for the precise task of detecting defects in PCBs. They transformed the backbone network by introducing FasterNet, incorporating a cutting-edge Partial Convolution (PConv) opti­ mization rule for convolutions that significantly enhanced the speed of feature extraction. The Spatial Pyramid Pooling Cross-Stage Partial Channel (SPPCSPC) module was also incorporated to extract features at various scales and fully utilize the spatial information in images. Furthermore, the model’s perceptiveness towards critical defect features was sub­ stantially boosted by embedding the CBAM attention mechanism into the final output layer of the SPPCSPC structure in the head section. After being tested on the HRIPCB dataset, this modification had demonstrated enhancement effects. The refined model elevated the mAP@0.5 to 97.5%. These enhancements in speed and accuracy make it a more effective solution for PCB defect detection.


In 2023, Zhang et al. (2023b) innovated upon the YOLOv7 framework to enhance its capability in detecting insulator defects. They introduced a novel, lightweight, deep convo­ lution module, DSC-SE, engineered to ensure the network’s precise extraction of defects. The DSC-SE module was designed using a Depthwise Separable Convolution (DSC) fused Squeeze-and-Excitation (SE) channel attention mechanism to substitute the SC (Standard Convolution) of the YOLOv7. In the feature fusion segment, the standard convolution SC was substituted with a hybrid convolution termed GSConv (Grid Sensitive Convolution), seamlessly incorporating SC, DSC, and shuffle operations. This adaptation, along with the integration of GSConv and the VoV-GSCSP network within the feature fusion architecture, significantly bolstered the model’s accuracy in detection tasks. Furthermore, the substitution of CIOU loss with EIOU-loss (Efficient-IOU) in the prediction head marked a significant improvement. On the custom dataset, the refined model demonstrated a mAP of 93.8%. Compared to the original YOLOv7 model, the inference speed increased by 2FPS, while the accuracy mAP improved by 4.9%, demonstrating a good balance between efficiency and precision in insulator defect detection.


In 2023, Zhou et al. (2023b) tackled the challenge of insufficient feature extraction in the original YOLOv7 algorithm, particularly for detecting defects on PCB bare boards. They revolutionized the algorithm’s backbone network by integrating the Flexible Rectified Linear Unit (FReLU) activation function, substituting the Conv_BN_SiLU module with a more advanced Conv2D_BN_FReLU configuration. The new model incorporated the SE


1 3


<!-- Page 26 -->


## 333 Page 26 of 48


Y. Ma et al.


attention mechanism by integrating SE_blocks into the existing network structure, with the aim of enhancing the weight given to small target detection channels and improving the model’s accuracy in detecting small targets. Enhancements were also applied to the feature fusion network to enable the assimilation of deeper, shallow-level feature informa­ tion. The introduction of skip connections played a crucial role in mitigating the loss of feature information during the transmission through the network. Rigorous testing on a PCB defect dataset demonstrated that these improvements significantly boosted the performance of the YOLOv7 model, achieving mAP of 95.89% and an F1 score of 95.32%. These figures marked notable increases of 3.36% and 3.91%, respectively, over the original model, show­ ing an improvement of efficiency and accuracy in PCB defect detection.


In 2024, Gao et al. (2024a) advanced the YOLOv7 framework, unveiling the CDNYOLOv7 variant specifically tailored for detecting surface defects on steel materials. This innovation introduced the CARAFE upsampling operator, a strategic replacement for the nearest-neighbor interpolation method previously used in YOLOv7. This enhancement not only broadened the receptive field but also significantly improved the model’s feature fusion capabilities. They crafted a cutting-edge head network design that includes scale-aware and spatially cascaded attention mechanisms (DY-Block) along with decoupled heads, finetuning the model’s focus and precision. Additionally, the conventional CIOU loss function was substituted with the more robust Focal-EIOU loss function, further refining detection accuracy. The enhancements culminated in the CDN-YOLOv7 achieving a mAP of 80.3% in defect detection on the NEU-DET dataset, marking a substantial 5.9% improvement over the original model. Furthermore, the model’s inference speed soared to 60.8 FPS, ensuring its capability to meet the demands of real-time applications.


In 2024, Gao et al. (2024b) enhanced the YOLOv7 algorithm and introduced a new model, SRN-YOLO, specifically designed for detecting defects on steel surfaces. They developed a split residual convolution network (SResNet) to capture gradient feature information and retain shallower details, thereby improving the detection of small defects. Additionally, they constructed a feature fusion pyramid RPN and designed an NWD-CIOU loss function, which combined Normalized Wasserstein Distance (NWD) and Complete Intersection Over Union (CIOU). Experimental results demonstrated that the new model achieved a mAP of 81.2% on the NEU-DET dataset and 71.6% on the GC10-DET dataset.


In 2024, Xie et al. (2024) innovatively enhanced the YOLOv7 algorithm for the task of detecting surface defects in steel materials. They developed a groundbreaking “transformerinception” module by synergizing Transformer Blocks with InceptionDWConvolution, subsequently integrating this module into the FPN layers. To further bolster the model’s capability, they infused multiple GAM into the FPN layers, improving the extraction of critical features. They revamped the traditional SPPCSPC into a more sophisticated and feature-enhanced Spatial Pyramid Pooling with Feature Context Spatial Pyramid Convolu­ tion SPPFCSPC module. Additionally, the Mish activation function replaced the SiLU func­ tion in the feature extraction network, optimizing the activation process. The introduction of Minimum Partial Distance Intersection over Union (MPDIOU) in place of CIOU loss for calculating location loss marked a leap in boundary regression accuracy. Tests on the NEU-DET dataset revealed that this refined model outperformed the original by achieving a 6% increase in mAP. The results demonstrated that the proposed algorithm enhanced the detection of minor defects on steel surfaces.


1 3


<!-- Page 27 -->


Page 27 of 48 333


Surface defect inspection of industrial products with object detection…


## 3.2.6  YOLOv8


In the YOLOv8 (Jocher et al. 2023) architecture, the backbone’s traditional C3 modules were upgraded to the more advanced C2f configuration, which introduced additional crosslayer connections through its structure, thereby enhancing the model’s gradient flow. How­ ever, the incorporation of Split operations in the C2f design tended to be less optimal for deployment on certain hardware platforms. Moving to the model’s head, YOLOv8 adopted a Decoupled-head strategy, segregating the classification and detection tasks into separate entities and transitioning from an Anchor-Based to an Anchor-Free approach. Despite these innovations, YOLOv8 might face challenges in accurately detecting smaller targets and could encounter higher rates of false positives or misses in more complex environments.


In 2023, Wang et al. (2023a) embarked on refining the YOLOv8s model to enhance its detection of minuscule surface defects on barrel rollers, a task where the original model fell short. Their modifications targeted the model’s feature learning capabilities for small objects; specifically, they replaced the original model’s stride-2 convolutional downsam­ pling with a more detailed SPD-Conv (scale = 2) module. Furthermore, they enriched the PANet with a Generalized Feature Pyramid Network (GFPN) for feature fusion, orchestrat­ ing a more effective exchange of information between deep and shallow layers, and between large and small scale details. By integrating an additional detection head into the model, they improved its proficiency in identifying small defects. They also innovated in the loss function, substituting CIOU with Wise-IOU for bounding box loss calculation, and employ­ ing an outlier β for a more accurate anchor box evaluation. Tests conducted on a proprietary dataset showed that the improved YOLOv8s model achieved a mAP@0.5 of 97.5%, repre­ senting a 6.4% performance increase compared to its predecessor.


In 2023, Cui et al. (2024) somewhat advanced the capabilities of the YOLOv8n model with the development of the MCB-FAH-YOLOv8 algorithm, tailored for the intricate task of detecting surface defects on steel. To broaden the spectrum of training data, they utilized mosaic data augmentation, thereby enriching data diversity. Innovatively, they replaced the conventional CBAM attention mechanism with the Multi-Channel Block (MCB), which facilitated the acquisition of richer gradient information and bolstered the extraction process for densely packed targets. The team also refined the feature pyramid structure from Spatial Pyramid Pooling - Fast (SPPF) to SimCSPSPPF. The SimCSPSPPF module integrated the strengths of CSP and SPPF with a lightweight design, achieving an increase in accuracy while only slightly compromising speed. By integrating contextual information into the original FPN and upgrading it to a BiFPN, they achieved effective feature fusion. Moreover, the introduction of a four-headed Adaptive Feature Fusion ASFF detection head improved the detection of minuscule objects. Testing on the NEU-DET dataset, the newly developed model demonstrated a mAP of 81.8%, surpassing the original model by 5.1% and achieving substantial improvements in both accuracy and processing speed.


In 2023, Wang et al. (2024) developed an improvement to the YOLOv8 model, intro­ ducing YOLOv8-VSC, a lightweight detection model optimized for identifying surface defects on strip steel. The backbone of this model utilized the VanillaNet module, which was comprised solely of basic convolutional and pooling layers, serving as the network’s feature extraction mechanism. They also integrated a special SPD (2022) downsampling module within the backbone feature extraction network, expanding the channel count by four times to ensure no loss of defect information in the twice-downsampled feature data.


1 3


<!-- Page 28 -->


## 333 Page 28 of 48


Y. Ma et al.


In the feature fusion module, the lightweight upsampling operator CARAFE was employed to learn the relationships between pixels in adjacent areas, thereby enhancing the preci­ sion of defect detection. CARAFE addressed the problems of traditional upsampling opera­ tors, which often overlook semantic information in feature maps and have limited receptive fields. When tested on the NEU-DET dataset, the new model achieved a mAP increase from the original 79.0–80.8%, demonstrating an advancement in the model’s ability to detect defects on strip steel surfaces.


In 2023, Huang et al. (2023b) refined YOLOv8, introducing the WFRE-YOLOv8s model tailored specifically for detecting surface defects on steel. To simplify the network, they replaced the C2f module with the Convolutional Feature Network (CFN) module. The intro­ duction of the Efficient Multi-Scale Attention (EMA) mechanism significantly enhanced the precision of steel surface detection. Additionally, integrating the WIOU loss function ensured balanced data quality. Following an evaluation of defect detection performance on the NEU-DET dataset, the new model achieved a mAP0.5 of 79.4%, surpassing YOLOv8s by 4.7%. Furthermore, defect detection was conducted on the GC10-DET dataset, where the new model achieved a mAP@0.5 of 69.4%, representing a 3.8% improvement over the original model. These refinements have achieved good balanced accuracy and speed in the new model.


In 2024, Dou et al. (2024) enhanced YOLOv8 by developing a lightweight, small-sample steel plate defect detection algorithm. To address the challenge of insufficient sample sizes, they employed an interactive data augmentation algorithm based on fuzzy search. They introduced the lightweight Woo Multi-Scale Residual Network (LMSRNet), which served as a substitute for the YOLOv8 backbone, to the architecture. Within this network, the addi­ tion of Context Bidirectional Feature Pyramid Network (CBFPN) and Efficient Channel Spatial Attention (ECSA) modules significantly bolstered the capability to extract defect features. Furthermore, the Wise-IOU loss function was adopted in place of the traditional CIOU loss function, refining the model’s precision. Testing the improved network on a pro­ prietary dataset revealed an increase in mAP by 5.5% compared to the original model, mark­ ing an advancement in detecting defects on steel plates with limited sample availability.


In 2024, Song et al. (2024) introduced a model built upon YOLOv8, specifically tailored for the intricate task of detecting surface defects on steel. They enhanced the model’s back­ bone by integrating Deformable Convolutional Networks (DCN), somewhat improving its ability to interpret complex textures and the nuanced shapes of defects. To facilitate robust multi-scale feature fusion, they employed a BiFPN. BiFPN constructed a feature pyramid through a bottom-up and top-down bidirectional information flow and weighted fusion tech­ niques. Additionally, the adoption of the BiFormer attention mechanism within the back­ bone directly addressed and ameliorated the challenge of low detection accuracy for smaller objects. By transitioning the loss function from Complete-Intersection Over Union (CIOU) to Wise-IOUv3 (WIOUv3), they effectively countered the overfitting issue associated with low-quality bounding boxes. When evaluated on the NEU-DET dataset specifically for steel surface defect detection, the model demonstrated a mAP increase of 6.9% over the original YOLOv8, signifying progress in defect detection accuracy and reliability.


1 3


<!-- Page 29 -->


Page 29 of 48 333


Surface defect inspection of industrial products with object detection…


## 3.2.7  Others


In 2022, Ahmed et al. (2023) introduced a new model, DSTEELNet, engineered specifi­ cally for detecting defects on the surface of strip steel. This architecture was distinguished by three parallel dilated convolution blocks, designed to capture an extensive range of fea­ tures. Furthermore, Ahmed proposed DSTEELNet-ASPP, a module incorporating ASPP to expand the receptive field and integrate multi-scale contextual information. When tested on an augmented NEU-DET dataset, the DSTEELNet model achieved an F1-score of 97.0%, marking a substantial 13% improvement over YOLOv5. Additionally, the model demon­ strated an F1-score of 96.0% in defect detection tasks on the Severstal dataset, showcasing its robust performance in identifying surface anomalies.


In 2023, Zhang et al. (2023a) crafted a cutting-edge, lightweight CNN specifically tailored for identifying defects on PCBs and steel surfaces. They pioneered a new CAM backbone network, harnessing the synergy of Inverse Residual Blocks (IRB) and the CA mechanism for superior feature extraction. This innovative model DSConv has cross-layer connections and a weighted feature fusion approach, all underpinned by an attention-driven multi-scale feature fusion strategy, dubbed the Bidirectional Weighted Feature Pyramid Network (BWFPN). Demonstrating its prowess, the model achieved a mAP of 78.64% on the NEU-DET dataset and a mAP of 91.95% on HRIPCB.


In 2023, Liu et al. (2023) crafted the MSC-DNet, a model specifically designed for identifying surface defects in strip steel. They engineered the Multi-Scale Context Detec­ tion Network (MSC-DNet), featuring the innovative Feature Enhancement and Selection Module (FESM) to sharpen its defect detection capabilities. Deployed on the NEU-DET dataset, this advanced network demonstrated its effectiveness by achieving mAP of 79.4%. Furthermore, when tested on the GC10-DET dataset, it recorded an impressive mAP of 71.6%, showcasing its good performance in detecting surface defects across different steel substrates.


## 3.2.8  Summary


The summary highlights that one-stage object detection offers the advantage of speed. For evaluation of one-stage object detection methods in industrial defect detection, please refer to Table 3. In all the referenced studies with the APDDD dataset, the M2-BL-YOLOv4 model performed best, achieving a mAP of 93.5% with innovations such as the BiFPN-Lite feature fusion network. On the GC10-DET dataset, the new model (2022) achieved the best results by incorporating the ECA mechanism, a de-weighted BiFPN structure, and the SIOU loss function, resulting in a mAP of 80.2%. The new model (2023) showed the best performance on the HRIPCB dataset. It incorporated the FasterNet, cutting-edge PConv, SPPCSPC module, and the CBAM attention mechanism, achieving a mAP@0.5 of 97.5%. However, its performance in detecting small objects or under low-light conditions was lim­ ited. Looking ahead, future improvements in one-stage detection techniques should focus on balancing speed and accuracy to meet the rigorous demands of real-world industrial defect detection.


1 3


<!-- Page 30 -->


## 333 Page 30 of 48


Y. Ma et al.


## 4  Unsupervised defect detection methods


In response to the limitations of supervised methods, some researchers have shifted their attention toward unsupervised defect detection methods (Barlow 1989). Unsupervised defect detection methods can extract information from unlabeled data, automatically iden­ tifying and locating target objects in images. Without relying on manually labeled training data, it can uncover intrinsic features and relationships within the data, enabling automatic classification. This approach can address issues that supervised methods may not detect. In the field of defect detection, commonly used unsupervised algorithms include AutoEncoder and GAN, among others. The progression of surface defect detection in industrial products using unsupervised deep learning algorithms is summarized in Fig. 6. Correspondingly, the performance of some unsupervised detection methods in industrial defect detection can be referred to in Table 4.


## 4.1  AutoEncoder


The primary components of an AutoEncoder are the encoder and the decoder. The encoder effectively learns a good low-dimensional representation of the input signal, while the decoder, corresponding to the model’s output layer, aims to reconstruct the input signal as accurately as possible. Recently, many researchers have developed new surface defect detection models based on AutoEncoder.


In 2019, Yang et al. (2019) introduced the Multiscale Feature-Clustering-Based Fully Convolutional AutoEncoder (MS-FCAE), capable of efficiently detecting defects from a small number of defect-free samples. This method constructed multiple feature-clusteringbased fully convolutional AutoEncoder (FCAE) sub-networks operating at different scale levels to effectively reconstruct various textured background images. Each FCAE sub-net­ work extracted feature maps directly from input images using a fully convolutional neural network and enhanced the discriminative power of encoded feature maps through feature clustering. The new model achieved a precision of 92.0% and a detection time of 82 ms when tested on the self-built dataset at a resolution of 1920 × 1080 pixels.


In 2020, Wang et al. (2020b) have combined Vector Quantized Variational AutoEncoder (VQ-VAE) with the deep autoregressive model PixelSnail to create a discrete latent space and estimate the distribution of normal images, effectively avoiding unnecessary reconstruc­ tion of anomalous regions. During the detection phase, PixelSnail resampled the discrete latent codes that deviate from the normal distribution. After resampling, the decoder recon­ structed the indexed table into the restored image. Researchers evaluated the new model on the industrial inspection image dataset MVTec AD. The experimental results demonstrated that the area under the receiver operating characteristic (AUROC) curve value of the pro­ posed model had seen a 15% enhancement over that of the conventional AutoEncoder.


In 2021, Tsai et al. (2021) proposed an unsupervised learning method based on convo­ lutional AutoEncoder for detecting surface defects in industrial products. They introduced a regularized Convolutional Autoencoder (λ-CAE) to improve the feature distribution of defect-free samples, ensuring that the feature vectors of training samples were as close as possible to the average feature vector. The regularization strategy concentrated the feature vectors of normal samples, thereby increasing the model’s sensitivity to anomalous samples.


1 3


<!-- Page 31 -->


Page 31 of 48 333


Surface defect inspection of industrial products with object detection…


Yolov3 Steel Jiaqiao Zhang NEU-DET 82.73 85.7 82.3 83.9 Copper Yuanqing Xian TJ-CE-DET 67.42 73.33 64.71 68.75 Steel Xuechun Chen NEU-DET 86.96 98.37 95.48 107.4 M 80.96 96.90 PCB Yuanyuan Jiang HRIPCB 98.58 97.24 103.15 7.73 MB Yolov4 PCB Xinting Liao Self-managed datasets 98.64 56.98 97.83 PCB HaoJia xin HRIPCB 96.88 Metal Haili Zhao NEU-DET 92.5 Aluminium Zhuxi MA Self-managed datasets 96.28 96.26 95.6 21.537 97 40.81 MB Steel Yongfang Xie NEU-DET 83.9 10.36 M 90 PCB Yongfang Xie DeepPCB 98.9 83 Steel Shaoxiong Li GC10-DET 54.64 NEU-DET 79.88 PCB Hongjin Zhu Self-managedatasets 99.71 95.6 MB 33


(%) Recall (%) Parameters FPS F1(%) Model


Size


Model Object Author Dataset mAP (%) Precision


Table 3  Performance comparison of one-stage surface defect detection methods


Steel BeiBei Fan NEU-DET 82.78 Aluminium Songsong Li APDDD 93.5 52.99 Yolov5 Metal Kun Wang GC10-DET 74.1 Steel Jiangting Shi NEU-DET 84.61 Steel Zexuan Guo NEU-DET 75.2 30.6 Steel Jichi Liu Cable Damage 84.7 88.9 82.1 3.97 M 64.5 85.36 8.3 MB Metallic Siddiqui Muhammad


Metal Chuande Zhou GC10-DET 82.8 mAP@0.5 93.8 76.05 79.4 83.97 Strip Steel Huan Zhao GC10-DET 67.9 69.8 66.8 2.71 90.1 PV Longlong Li PV Multi-Defect 97.8 ± 0.02 96.4 ± 0.02 93.3 ± 0.02 Steel Wire Rope Gao Jia Self-managed datasets 99.4 98.0 97.4 6.72 151 97.70 Magnetic tile Yan Li MT 99.49 98.56 98.14 55.3


Yasir NEU-DET 77.50 mAP@0.5


1 3


<!-- Page 32 -->


## 333 Page 32 of 48


(%) Recall (%) Parameters FPS F1(%) Model


Size


Y. Ma et al.


Aluminium LingJie Jiang APDDD 88.1 81.1 81.1 84.9 Magnetic tile Tiejun Li MT 82.5 85 82 41.3 Plastic Changqian Zhuang Self-managed datasets 99.5 99.7 99.9 Solder Joint Ang Li Self-managed datasets 97.8 90.8 91.1 159.8 Yolov7 Aluminium Juan Wang APDDD 76.92 Strip Steel Yang Wang GC10-DET 80.2 82.0 70.3 105.2 75.7 NEU-DET 81.9 79.2 76.5 55.56 77.83 Steel Yateng Zhang NEU-DET 80.2 38 76 Steel Yinghong Xie NEU-DET 82.4 25.6 PCB Boyuan Chen HRIPCB 97.5mAP@0.5 96.9 95.6 83.3 96.25 Insulator Yulu Zhang Self-managed datasets 93.8 95.2 87.6 3.74 52 91.24 Steel Chunyan Gao NEU-DET 80.3 81.0 72.2 73.4 60.83 76.35 Yolov8 Drum roller Anjing Wang Self-managed datasets 93.0 92.3 98.81 40.2 95.44 Steel Kebin Cui NEU-DET 81.8 Strip Chunmei Wang NEU-DET 80.8 1.96 263 Steel Yao Huang NEU-DET 79.4 73.6 75.9 GC10-DET 69.4 64.8 62.6 Steel Zhi Dou Self-managed datasets 94.8 93.1 88.8 0.96 167 Steel Xuan Song NEU-DET 84.8 3.4 142.8 Others Steel Rongqiang Liu NEU-DET 79.4 GC10-DET 71.6 Steel Khaled R. Ahmed NEU-DET 96.1 97.0 Severstal 96.0 96.0


Guide Plates Junfeng Li Self-managed datasets 98.9 99.5 417


Model Object Author Dataset mAP (%) Precision


Hot-pressed Light


Table 3  (continued)


1 3


<!-- Page 33 -->


Page 33 of 48 333


Surface defect inspection of industrial products with object detection…


Fig. 6  The progression of surface defect detection in industrial products with unsupervised detection algorithms deep learning algorithms


1 3


<!-- Page 34 -->


## 333 Page 34 of 48


Y. Ma et al.


The new algorithm had achieved an accuracy improvement of 5–10% in defect detection tasks on the DAGM dataset compared to the conventional CAE algorithm.


In 2022, Pierer et al. (2022) proposed an Anomaly Quantification Analysis (AQA) model that utilizes CNNs within an AutoEncoder-like structure to detect defects in KTL-coated aluminum parts. Unlike traditional AutoEncoder, AQA used binary maps as ground truth to identify defect pixels and classifies defects based on complexity of the perimeter, the size (quantitate of pixels), and texture features obtained through the Gray-Level Co-occurrence Matrix (GLCM). The model enhanced generalization through data augmentation techniques such as gamma correction, linear contrast adjustment, and rotation enhancement. Aiming to improve the detection of complex or subtle defects, additional factors affecting defect detec­ tion, including pixel addition at saturation thresholds, brightness, compactness, color impact (in RGB format), and polygon characteristics, would be explored in their future research.


In 2023, Huang et al. (2023c) introduced Contrastive Masked AutoEncoder (CMAE) as a self-supervised pre-training method. This approach integrated contrastive learning and masked image modeling to improve the quality and discriminative capability of visual rep­ resentations. CMAE comprised two pivotal branches: an online branch reconstructed origi­ nal images from latent representations of masked ones, while a momentum branch enhanced feature discriminability through contrastive learning. Furthermore, extensive experiments substantiated CMAE’s achievement of good performance in object detection tasks.


In 2024, Shiferaw et al. (2024) proposed an unsupervised surface defect detection method based on AutoEncoder, specifically for inspecting defects on the surfaces of industrial prod­ ucts. To improve image reconstruction and defect detection, they enhanced the AutoEncod­ er’s loss function by introducing the Adaptive Weighted Structural Similarity (AW-SSIM) loss. The AW-SSIM loss improved surface defect detection in unsupervised learning by dynamically adjusting the weights of luminance, contrast, and structure components, and by fine-tuning the Gaussian window’s standard deviation to balance noise reduction and detail preservation. The research team also developed an Artificial Defect Generation Algorithm (ADGA) to create defect samples, aimed at improving the performance of the AutoEncoder in defect detection. The new model was trained in two stages: the first stage used normal samples, and the second stage combined normal samples with artificial defect samples. In the second stage, the loss function combined Learned Perceptual Image Patch Similarity (LPIPS) and AW-SSIM to enhance the quality of normal background reconstruction while maintaining accurate defect detection. Tested on six samples from the MVTec AD dataset, the model achieved an average AUROC of 97.69%. The experiments demonstrated that the new model was able to achieve high-quality reconstruction of normal backgrounds while effectively detecting defects.


## 4.2  GAN


GAN have gained significant attention in surface defect detection (Xia et al. 2022). The GAN architecture includes a generator and a discriminator. The generator creates realistic data, while the discriminator distinguishes between generated and real data, calculating the discrimination loss. Through adversarial training, the generator improves its ability to pro­ duce realistic data, and the discriminator enhances its accuracy. The ultimate goal of this model is to learn the underlying patterns of real data, predict and estimate the distribution or density of real data, and generate new data based on the acquired knowledge. GANs have


1 3


<!-- Page 35 -->


Page 35 of 48 333


Surface defect inspection of industrial products with object detection…


Table 4  Performance comparison of unsupervised surface defect detection methods Model Object Author Dataset Pre­ ci­ sion (%)


AutoEncoder Fabric Ruofeng Wei


Selfman­ aged datasets


Industrial Products


Lu Wang


MVTec AD


Industrial Products


DuMing Tsai


Re­ call (%)


F1Score (%)


Accuracy(%) AUROC(%) FPS


73.4 41.9 53.3


95.6 83.7 85


## DAGM 95


KTLcoated Aluminum


Alex­ ander Pierer


Selfman­ aged datasets


Industrial Products


Tesfaye Ge­ tachew Shiferaw


MVTec AD


GAN Industrial Products


Lin Zhang


MVTec AD


Steel Chao Zhang


Selfman­ aged datasets


Screw rods And Hex nuts.


Kengo Ishida


Selfman­ aged datasets


MVTec AD


99.9


97.69


94.3


72.98 86.38


97.6 25.0


97.1


achieved notable success in surface defect detection, and researchers have proposed various improvements to enhance their performance.


In 2020, Tang et al. (2020) developed the Dual AutoEncoder Generative Adversarial Network (DAGAN) to address sample imbalance issues. This innovative model improved surface defect detection in industrial products. By combining skip connections with a dual AutoEncoder architecture, DAGAN enhanced image reconstruction and training stability. The model was evaluated on public industrial detection datasets, including MVTec AD, smartphone screen glass, and wood defect detection datasets. In the MVTec AD dataset, the AUROC for the category “Metal Nut” was 76.8%. DAGAN achieved superior AUROC compared to previous GAN-based anomaly detection models.


In 2022, Zhang et al. (2022) introduced the GAN method leveraging attention-based feature fusion for detecting surface defects in industrial products. This method utilized an encoder-decoder architecture with skip connections to integrate features effectively. An Attention Feature Fusion (AFF) mechanism was incorporated to enhance the network’s focus on image channel features. The AFF mechanism improved image reconstruction and captured richer channel features by enhancing the network’s focus on pixel correlations.


1 3


<!-- Page 36 -->


## 333 Page 36 of 48


Y. Ma et al.


Experimental results on the MVTec AD dataset demonstrated that the proposed model achieved an average AUROC that was 4.1% points higher than the next best model.


In 2023, Zhang et al. (2023c) introduced an innovative inpainting GAN utilizing both global and local generators. This new model enhanced image inpainting quality while reducing the necessary data volume. By incorporating periodic noise injection technology, the number of training images was increased, thereby improving the network’s detection performance. The new model achieved an AUCROC of 86.38% when tested on the steel dataset.


## 4.3  Others


In 2023, ISHIDA et al. (2023) enhanced the capabilities of industrial product surface inspec­ tion by introducing SA-PatchCore. This method incorporated a self-attention mechanism into the local anomaly detection model PatchCore, thereby improving the model’s accuracy in detecting co-occurrence anomalies. The PatchCore model in industrial anomaly detection can evaluate each pixel in an image for anomalies. This detailed scoring mechanism not only determined if the entire image was abnormal but also precisely pinpointed the spe­ cific areas of abnormality. Experimental results showed that on the custom dataset, the new model achieved an AUROC of 97.6% and an average inference time of 25 ms per image. On the MVTec AD dataset, the model achieved an AUROC of 97.1%. SA-PatchCore emerges as a promising model in the field of industrial anomaly detection.


In 2024, Ramachandran et al. (2024) introduced a novel method for surface defect detection based on CLAMP-ViT, an unsupervised detection approach. CLAMP-ViT was a data-free post-training quantization technique for vision Transformers. It enhanced feature extraction capabilities through the integration of a Hybrid Attention Module (HAM) and a Multi-Dilation Convolution Module (MCM). Experimental results demonstrated that this method improves the mAP value compared to existing approaches.


## 5  Discussion


Currently, deep learning algorithms play a pivotal role in advancing automation and intel­ ligence in industrial production. This paper introduces various deep learning-based algo­ rithms for detecting defects in industrial products, along with relevant datasets. To further clarify the need of computational resources for different types of deep defect detection models, a comparison of typical two-stage, one-stage, and unsupervised detection algo­ rithms was presented in Table 5. From the table, it is evident that the unsupervised model has the largest number of parameters, followed by the two-stage detection model, while the one-stage detection model has the fewest parameters. Although the one-stage model has the lowest FLOPS, indicating lower computational demand, it achieves the highest FPS, signifying the fastest processing speed. Despite two-stage object detection algorithms excelling in classifying and precisely refining candidate areas, their slower speed and high computational demands require substantial resources and advanced technical knowledge for training and optimization, significantly increasing development costs and complexity. One-stage object detection algorithms are suitable for real-time applications and scenarios with limited computational resources due to their fast detection speed. However, compared


1 3


<!-- Page 37 -->


Page 37 of 48 333


Surface defect inspection of industrial products with object detection…


Table 5  Comparison of computational resources for supervised one-stage and two-stage object detection algorithms, and unsupervised detection algorithms Model Name Params (M)


## FPS FLOPS (G)


Image Resolution(pixel)


Hardware De­ vices (GPU) Two-stage ob­ ject detection


IDD-Net (Zhang et al. 2023d) 43.96 40 24.9 640 × 640 NVIDIA Ge­ Force RTX 6000 One-stage ob­ ject detection


FE-YOLO (2022) 10.36 88 17.0 200 × 200 NVIDIA GeForce RTX 2080Ti Unsupervised detection


CFLOW-AD (Gudovskiy et al. 2022)


## 96 34 - 256 × 256/512 × 512 NVIDIA 1080 8GB GPU


FOUND (Siméoni et al. 2023)


## 770 80 - - NVIDIA V100


to two-stage detectors, one-stage detectors may sacrifice some precision and accuracy in complex scenes, especially with multiple objects. While unsupervised detection saves on data annotation costs, it requires complex models and substantial computational resources, and its accuracy may not match that of supervised algorithms. Therefore, in industrial prod­ uct defect detection, the choice of model must consider both computational resources and accuracy requirements. For real-time applications, one-stage algorithms are recommended; for high-precision requirements, two-stage algorithms are preferred; and for scenarios with high data annotation costs, unsupervised detection algorithms are suggested.


Currently, there is more research on supervised defect detection methods compared to unsupervised methods. Some supervised methods have been applied in real industry. How­ ever, unsupervised methods are on the rise and attract the attention of many new research­ ers. Supervised learning relies on labeled datasets, offering high accuracy and clear learning goals, but it involves costly data annotation and has limited generalization capability. In contrast, unsupervised learning uses unlabeled data, providing greater adaptability but typi­ cally lower accuracy, complex training processes, and challenging evaluation. Since unsu­ pervised learning lacks defect label information, it can only distinguish between normal and abnormal data. It can segment abnormal regions but cannot accurately classify defect types. In addition, except for the MVTec AD dataset, there are very few datasets for the research of unsupervised methods. In practical applications, the choice of method depends on specific requirements and data availability. Supervised learning is suitable when data annotation is feasible and high precision is needed, while unsupervised learning suits situations where data annotation is challenging and exploratory analysis is required. These approaches can also complement each other: unsupervised learning can uncover data features that enhance predictive capabilities in supervised learning.


As can be seen from the number of studies, the field of supervised one-stage defect detec­ tion is the most popular and has attracted significant research interest at present, with efforts largely directed towards improving the precision of these algorithms (Wang et al. 2023d). Innovations in network design, loss function refinement, and the integration of attention mechanisms have enabled one-stage defect detection algorithms to achieve and sometimes exceed the accuracy levels of their two-stage counterparts. As summarized in Table 6, a variety of advanced modification techniques are employed, notably the use of multi-scale feature fusion to adeptly manage objects and background information across varying scales. By incorporating feature maps of multiple scales or applying convolutional kernels of


1 3


<!-- Page 38 -->


## 333 Page 38 of 48


Y. Ma et al.


Table 6  Methods for improving one-stage defect detection models Input Data augmentation


Moscia Mix up


(Fan and Li 2022), (Cui and Jiao 2024)


Feature extraction


Build light­ weight structures


ShuffleC3 GhostConv DWConv ShuffleNetV2 MobileNetV2 LW-Bottle­ Neck LMSRNet DSC-SE


(Liu et al. 2024) (Liu et al. 2024), (Li et al. 2023a), (Zhang et al. 2023b) (Liang et al. 2023), (Gao et al. 2023) (Yasir and Ahn 2023) (Chen et al. 2022) (Gao et al. 2023) (Dou et al. 2024) (Zhang et al. 2023b)


Additive atten­ tion mechanism


## CBAM GAM MBAM CA MCB ECA MA SE EMNA


(Liang et al. 2023), (Fan and Li 2022), (Li and Yang 2023), (Shi et al. 2022), (Li and Yang 2023) (Zhou et al. 2023a), (Xie et al. 2024) (Hu et al. 2024) (Wang et al. 2023b) (Cui and Jiao 2024) (Wang et al. 2022b), (Li et al. 2023b) (Jiang et al. 2023b) (Zhou et al. 2023b) (Huang et al. 2023b) Optimized feature fusion


## PCR SCA JASPP EFPN SPPFCSPC CARAFE FFN CLW-FPN SDDT-FPN


(Jiang et al. 2023b) (Li et al. 2023e) (Hu et al. 2022) (Chen et al. 2022) (Xie et al. 2024) (Gao et al. 2024a), (Gao et al. 2024b) (Jiang et al. 2023a) (Gao et al. 2023) (Jiang et al. 2023b) Prediction stage


Optimized anchor frame


k-means k-means++


(Shi et al. 2022), (Wang et al. 2002a) (Xia et al. 2021), (Xie et al. 2022), (Huang et al. 2022b) Improved NMS Soft NMS (Zhao et al. 2021b), (Li et al. 2023e), (Zhou et al. 2023a) Optimize IOU losses


DIOU Loss B-CIOU Focal-EIOU SIOU EIOU Loss MPDIOU BECLoss CIOU Loss Wise-IOU


(Yang et al. 2023) (Gao et al. 2023) (Gao et al. 2024a), (Li et al. 2023d) (Wang et al. 2022b) (Zhang et al. 2023b) (Xie et al. 2024) (Wang et al. 2024) (Zheng et al. 2024a) (Wang et al. 2023a), (Dou et al. 2024)


diverse sizes, these models adeptly grasp the semantic and spatial details of targets, leading to superior detection outcomes. Additionally, researchers have introduced more streamlined network architectures, such as MobileNet and GhostNet, significantly boosting inference speeds while still preserving accuracy. Moreover, the application of reinforcement learn­ ing to object detection allows for optimized decision-making in complex scenarios (2020). Through dynamic interaction with the environment, models are trained to discern optimal strategies and actions, thus enhancing the robustness and overall performance of object detection.


1 3


<!-- Page 39 -->


Page 39 of 48 333


Surface defect inspection of industrial products with object detection…


With the comprehensive review of deep learning methods for defect detection, the fol­ lowing improvement areas can be further expanded and enhanced to improve the perfor­ mance of one-stage defect detection.


(1)	 Leveraging advanced data augmentation strategies to enrich the training dataset for


industrial product target detection. Among these techniques are the copy-paste data augmentation, the Mosaic data augmentation, and several refined methods that build upon the Mosaic framework. These enhancements significantly diversify and expand the training samples, empowering more robust model training. (2)	 Crafting lightweight model architectures, incorporating techniques like DSConv, Shuf­


fleNet, and GhostConv, aimed at minimizing the network’s parameter footprint. Select­ ing an optimal lightweight model becomes crucial for effective deployment within real-world industrial settings. (3)	 By integrating attention mechanisms, fine-tuning the model’s focus on specific regions


automatically, thereby boosting its adaptability across different tasks. This includes employing sophisticated techniques such as the GAM and CBAM, among others. (4)	 Harnessing feature fusion strategies is essential, especially when confronting the diver­


sity in size and structure of targets in industrial product defect detection. It’s crucial, during the feature extraction phase, to integrate a comprehensive field of view with multi-scale features. These methods include employing SPP-block for pooling and con­ catenating multi-scale local region features, constructing a spatial pyramid to expand the field of view, and introducing a multi-branch RFB-PANET feature fusion method to enhance detection performance across various scales. (5)	 Integrating Transform modules, particularly within the Backbone and Neck layers,


could significantly enhance the focused learning of target features, optimizing the mod­ el’s ability to discern and classify with greater precision. (6)	 Incorporating weakly supervised and unsupervised approaches to mitigate the challenge


faced in industrial product defect detection, where deep learning models are extensively dependent on costly and labor-intensive pixel-level annotations for training. By adopt­ ing these methods, it can lessen the reliance on extensive datasets and significantly improve the model’s capacity to generalize across varied scenarios. (7)	 Incorporating GANs into the framework. GANs excel in generating data of superior


quality by employing adversarial learning to iteratively refine the interplay between the generator and discriminator, thereby significantly boosting the realism of the produced data. (8)	 Enhancing performance by meticulously optimizing anchor boxes, advancing NMS


techniques, and refining IOU metrics.


## 5.1  Challenges in real-world industrial applications


Through an analysis of the NEU-DET dataset-based research with deep learning methods, we found that the mAP values for this dataset typically hover around 80%, with the highest performance reaching 86.96%. Figure 7 illustrates the mAP values of different algorithms for the NEU-DET dataset. This suggests that these algorithms exhibit relatively high accu­ racy and stability on the NEU-DET dataset, but there is still considerable room for improve­


1 3


<!-- Page 40 -->


## 333 Page 40 of 48


Y. Ma et al.


Fig. 7  The mAP values of different algorithms for the NEU-DET dataset


ment. The field of industrial product defect detection faces numerous challenges, including intricate product designs and diverse defect types, spanning from variations in size and proportions to surface and internal flaws, all of which pose significant detection challenges. Additionally, existing deep learning algorithms lack robustness in detecting defects against complex backgrounds, making them susceptible to changes in perspective and environmen­ tal conditions.


Beyond external challenges, there is a pressing need to address and balance the intrinsic contradictions within object detection systems. These include the tension between algorithm sophistication and the requirement for real-time capabilities, as well as the delicate balance between high accuracy and limited computational resources. Object detection is crucial in the industrial sector, enhancing both product quality and production efficiency. However, the process is resource-intensive, especially during data preparation, where achieving met­ rics like AP requires significant time and effort in creating and annotating extensive datasets. The use of specialized equipment for defect data acquisition further escalates costs. While multi-scale detection techniques offer significant benefits, they also increase model com­ plexity and computational expenses. Pursuing higher AP scores may necessitate trade-offs in frame rate, demanding more intricate model architectures that escalate the need for compu­ tational resources and costs. Post-processing techniques like NMS, although beneficial for AP enhancement, add to computational expenditures. Therefore, achieving a cost-effective and sustainable object detection solution in the industry requires a careful balance between model performance, hardware capabilities, processing speed, and financial considerations.


In real industrial environments, surface defect detection encounters challenges such as varying defect scales, the detection of small target defects, and data imbalance issues. To effectively address multi-scale variation detection, techniques such as using dilated convo­ lutions to reduce the downsampling rate, multi-scale training, optimizing anchor size design, and fusing deep and shallow features can be employed to enhance robustness and detection


1 3


<!-- Page 41 -->


Page 41 of 48 333


Surface defect inspection of industrial products with object detection…


capabilities. For the detection of small targets, techniques such as integrating Transformers, visual attention mechanisms, and high-resolution lightweight networks can be employed.


In addition to the above issues, there are still other challenges in deploying, scaling, and integrating defect detection models into existing systems in real-world applications. Firstly, object detection models are highly complex, and, although lightweight pre-trained models can be fine-tuned for specific tasks, they still require high-performance hardware support. When selecting GPUs and computing resources, it is crucial to consider computational power, memory capacity, data transfer bandwidth, calculation precision and efficiency, data processing needs, and real-time requirements. GPUs with high floating-point performance (TFLOP) may be needed to handle large-scale datasets. Secondly, obtaining and labeling a large amount of defect data is time-consuming and difficult, which requires a lot of man­ power and material resources. The incorporation of supervised and unsupervised learning methods would be a promising approach. Additionally, most models are only designed for a specific defect detection application, and the generalization is poor. Enhancing model scalability can be achieved by incorporating transfer learning for feature transfer and select­ ing appropriate models. Deploying trained deep learning models into existing systems can leverage edge computing and cloud computing technologies. This involves running the model on edge devices near the production line, using GPU acceleration for real-time inference, or uploading images to cloud servers, utilizing cloud computing resources for defect detection, and returning results to the local system. Moreover, to face the changing industrial site environment and potential new defect types, regularly updating and retrain­ ing deep learning models based on actual operational data is essential to maintain detection accuracy and adaptability. Besides, when integrating with existing systems, it is crucial to establish interfaces and communication protocols for the defect detection model, ensuring it can operate on the existing hardware platform.


Furthermore, as mentioned above, it emphasizes here that balancing accuracy and speed in actual deployment presents significant challenges. Either low accuracy or slow speed may make practical use fail. In industrial defect detection, real-time processing is crucial for promptly identifying and addressing defects on the production line. Current models improve detection speed through lightweight design and robust hardware support. At the same time, high precision is required, which can be achieved by optimizing model architecture, incor­ porating transfer learning, and integrating new attention mechanisms. Nonetheless, an emphasis on accuracy tends to escalate model complexity, consequently slowing down the detection process. Conversely, prioritizing speed can simplify the model’s architecture, but at the cost of reduced accuracy. Finding the right balance requires selecting suitable model architectures and optimization strategies, along with fully utilizing hardware resources to develop an efficient and precise defect detection system.


## 5.2  Integration with emerging technologies


Large Language Models (LLMs) are currently experiencing rapid development, and their application in industrial defect detection is becoming increasingly widespread and profound. LLMs can automate the annotation process by understanding descriptive language related to defects, thereby automatically generating or assisting in generating training data annota­ tions, which reduces the need for manual labeling. LLMs can perform multimodal detection by combining visual and linguistic information to improve the accuracy of defect detection.


1 3


<!-- Page 42 -->


## 333 Page 42 of 48


Y. Ma et al.


For example, these models can simultaneously process image data and related technical documents. LLMs also enable interactive detection, providing an interactive defect detec­ tion experience that allows operators to obtain detailed information and suggestions through natural language queries. Furthermore, LLMs can be applied across different fields due to their versatility, making them useful for defect detection in various industrial sectors such as automotive, semiconductor, and food processing. However, there are challenges in applying LLMs to industrial defect detection. These include meeting real-time performance requirements and addressing integration compatibility issues, which may require substantial computational resources and increased model complexity. Additionally, integrating LLMs into existing industrial systems may involve overcoming technical and operational compat­ ibility issues.


Besides traditional industrial areas, surface defect detection is also expanded to new industrial applications such as the additive manufacturing. Deep learning-based surface defect detection is regarded as a powerful tool in the field of laser additive manufacturing (LAM), used to enhance the quality and efficiency of the manufacturing process (Chen et al. 2024a). LAM relies on machine learning and deep learning models to predict potential defects using multi-sensor data. Recently, Chen et al. (2021) used in-situ point cloud pro­ cessing and machine learning for rapid defect identification in DED-type additive manu­ facturing.  Huang et al. (2022a) designed a non-contact 3D laser profilometry inspection system for wire arc additive manufacturing (WAAM). The use of surface defect detection technology in additive manufacturing holds great potential for improving product quality and production efficiency, making its development particularly important.


In addition, surface defect detection also finds extensive applications in other multidisci­ plinary fields. For instance, in the medical field it has been used to detect the surface defects in dental nails based on Yolov8n (Chen et al. 2024b). In the field of information science, it is also important to inspect defects such as on the wafer surface during semiconductor manufacturing, which has attracted the attention of related researchers (Zhao et al. 2024). Moreover, it also sees good applications in more disciplines, such as detection of citrus epidermis defect (Hu et al. 2023a) in agriculture, pavement defect detection (Chen et al. 2023) in the civil engineering, and etc. Beyond surface defect detection, object detection as a generic technology also showcases remarkable adaptability and innovation in more appli­ cations, such as lung nodule detection (Xu et al. 2023) in medical image analysis. In a word, surface defect detection with deep networks is of great significance to multiple disciplines.


## 6  Conclusion


In summary, ongoing improvements have greatly enhanced the performance of surface defect detection algorithms. However, challenges remain in multi-scale detection, identify­ ing small defects, handling insufficient data samples, balancing detection accuracy with speed, and practical deployment, emphasizing the necessity of further improvements.


Author contributions  Yu-xin Ma: Methodology, Investigation, Writing - Original Draft. Jia-xing Yin: Data curation, Investigation.Feng Huang: Methodology, Supervision, Writing - Review & Editing, Funding acqui­ sition.Qi-peng Li: Data curation, Resources.


1 3


<!-- Page 43 -->


Page 43 of 48 333


Surface defect inspection of industrial products with object detection…


Funding  This study was funded by Zhejiang Provincial Natural Science Foundation of China (Grant No. LY20E050013), Graduate Research Innovation Fund and Basic Research Fund of Zhejiang University of Science and Technology (2023yjskc02, 2023JLZD001).


Data availability  No datasets were generated or analysed during the current study.


Declarations


Conflict of interest  The authors declare no conflict of interest.


Open Access  This article is licensed under a Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.


## References


Ahmed KR (2023) Dsteelnet: a real-time parallel dilated cnn with atrous spatial pyramid pooling for detect­


ing and classifying defects in surface steel strips. Sensors 23(1):544. https://doi.org/10.3390/s23010544 Akhyar F, Liu Y, Hsu CY et al (2023) FDD: a deep learning-based steel defect detectors. Int J Adv Manuf


Tech 126(3–4):1093–1107. https://doi.org/10.1007/s00170-023-11087-9 APDDD Database (2023) https://tianchi.aliyun.com/dataset/148297. Accessed 16 Mar 2023 Bagherzadeh F, Shafighfard T, Khan RMA et al (2023) Prediction of maximum tensile stress in plain-weave


composite laminates with interacting holes via stacked machine learning algorithms: a comparative study. Mech Syst Signal Process 195:110315. https://doi.org/10.1016/j.ymssp.2023.110315 Bergmann P, Fauser M, Sattlegger D et al (2019) MVTec AD–A comprehensive real-world dataset for unsu­


pervised anomaly detection. In: Proceedings of the IEEE/CVF conference on computer vision and pat­ tern recognition, pp 9592–9600. https://doi.org/10.1109/CVPR.2019.00982 Bochkovskiy A, Wang CY, Liao HYM et al (2020) Yolov4: Optimal speed and accuracy of object detection.


arXiv preprint arXiv:2004.10934. https://doi.org/10.48550/arXiv.2004.10934 Cai Z, Vasconcelos N (2018) Cascade r-cnn: delving into high quality object detection. In: Proceedings of the


IEEE conference on computer vision and pattern recognition. pp 6154–6162. https://doi.org/10.48550/ arXiv.1712.00726 Chen BY, Dang ZC (2023) Fast PCB defect detection method based on FasterNet backbone network and


CBAM attention mechanism integrated with feature fusion module in improved YOLOv7. IEEE Access 11:95092–95103. https://doi.org/10.1109/access.2023.3311260 Chen L, Yao X, Xu P et al (2021) Rapid surface defect identification for additive manufacturing with in-situ


point cloud processing and machine learning. Virtual Phys Prototyp 16(1):50–67. https://doi.org/10.10 80/17452759.2020.1832695 Chen XC, Lv J, Fang YL et al (2022) Online detection of surface defects based on improved YOLOV3. Sen­


sors 22(3). https://doi.org/10.3390/s22030817 Chen J, Wen Y, Nanehkaran YA et al (2023) Multiscale attention networks for pavement defect detection.


IEEE Trans Instrum Meas 72:1–12. https://doi.org/10.1109/TIM.2023.3298391 Chen L, Bi G, Yao X et al (2024a) In-situ process monitoring and adaptive quality enhancement in laser


additive manufacturing: a critical review. J Manuf Syst 74:527–574. https://doi.org/10.1016/j. jmsy.2024.04.013 Chen X, Jiang Z, Piao Y et al (2024b) SF-Yolov8n: a novel ultra lightweight and high-precision model for


detecting surface defects of dental nails. IEEE Sens J. https://doi.org/10.1109/JSEN.2024.3392674 Cheng X, Yu J (2021) RetinaNet with difference channel attention and adaptively spatial feature fusion for steel


surface defect detection. IEEE T Instrum Meas 70:1–11. https://doi.org/10.1109/TIM.2020.3040485


1 3


<!-- Page 44 -->


## 333 Page 44 of 48


Y. Ma et al.


Cheng TH, Lin S, Ge YX et al (2024) YOLO-World: real-time open-vocabulary object detection. In: Pro­


ceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp 16901–16911. https://doi.org/10.48550/arXiv.2401.17270 Cui KB, Jiao JY (2024) Steel surface defect detection algorithm based on MCB-FAH-YOLOv8. J Graph


45(01):112–125. https://link.cnki.net/urlid/10.1034.t.20231019.1107.002 DAGM dataset (2023) https://hci.iwr.uni-heidelberg.de/content/weakly-supervised-learning-industrial-opti­


cal-inspection. Accessed 11 July 2023 DeepPCB (2018) https://gitee.com/dengzhiguang/DeepPCB. Accessed15 Dec 2018 Din NU, Javed K, Bae S et al (2020) A novel GAN-based network for unmasking of masked face. IEEE


Access 8:44276–44287. https://doi.org/10.1109/ACCESS.2020.2977386 Ding R, Dai L, Li G et al (2019) TDD-net: a tiny defect detection network for printed circuit boards. CAAI


TRIT 4(2):110–116. https://doi.org/10.1049/trit.2019.0019 Dou Z, Gao HR, Liu GQ (2024) Small sample steel plate defect detection algorithm of lightweight YOLOv8.


Comput Eng Appl 0990–100. https://doi.org/10.3778/j.issn.1002-8331.2311-0070 Fan BB, Li W (2022) Application of GCB-net based on defect detection algorithm for steel plates. https://doi.


org/10.21203/rs.3.rs-1550068/v1 Gao J, Liu T, Wang XF (2023) TWDR-Net: a real-time detection network algorithm for traction wire rope


defects. Chin J Sci Instrum 44(06):223–235. https://doi.org/10.19650/j.cnki.cjsi.J2311233 Gao CY, Qin S, Li MH (2024a) Research on steel surface defect detection with improved YOLOv7 algo­


rithm. Comput Eng Appl 60(07):282–291. https://doi.org/10.3778/j.issn.1002-8331.2308-0414 Gao SS, Chu MH, Zhang L (2024b) A detection network for small defects of steel surface based on YOLOv7.


Digit Signal Process 149:104484. https://doi.org/10.1016/j.dsp.2024.104484 GC10-DET dataset (2023) https://github.com/lvxiaoming2019/GC10-DET-metallic-surface-defect-datasets.


Accessed 11 July 2023 Ge Z, Liu S, Wang F et al (2021) Yolox: exceeding yolo series in 2021. arXiv Preprint. https://doi.


org/10.48550/arXiv.2107.08430 Getachew Shiferaw T, Yao L (2024) Autoencoder-based unsupervised surface defect detection using two


stage training. J Imaging 10(5):111. https://doi.org/10.3390/jimaging10050111 Gevorgyan Z (2022) SIoU loss: more powerful learning for bounding box regression. arXiv Preprint. https://


doi.org/10.48550/arXiv.2205.12740. arXiv:2205.12740 Girshick R, Donahue J, Darrell T et al (2014) Rich feature hierarchies for accurate object detection and


semantic segmentation. In: Proceedings of the IEEE conference on computer vision and pattern recog­ nition, pp 580–587. https://doi.org/10.48550/arXiv.1311.2524 Gudovskiy D, Ishizaka S, Kozuka K (2022) CFLOW-AD: real-time unsupervised anomaly detection with


localization via conditional normalizing flows. In: Proceedings of the IEEE/CVF winter conference on applications of computer vision, pp 98–107. https://doi.org/10.1109/WACV51458.2022.00188 Guo ZX, Wang CS, Yang G et al (2022) MSFT-YOLO: improved YOLOv5 based on transformer for detect­


ing defects of steel surface. Sensors 22(9). https://doi.org/10.3390/s22093467 He K, Gkioxari G, Dollár P (2017) al Mask r-cnn. In Proceedings of the IEEE international conference on


computer vision, pp 2961–2969. https://doi.org/10.48550/arXiv.1703.06870 HRIPCB Defects Dataset (2019) https://www.kaggle.com/datasets/akhatova/pcb-defects. Accessed 22 Hu B, Wang J (2020) Detection of PCB surface defects with improved faster-RCNN and feature pyramid


network. IEEE Access 8:108335–108345. https://doi.org/10.1109/access.2020.3001349 Hu C, Liao HW, Zhou T et al (2022) Online recognition of magnetic tile defects based on UPM-DenseNet.


Mater Today Commun 30:103105. https://doi.org/10.1016/j.mtcomm.2021.103105 Hu W, Xiong J, Liang J et al (2023a) A method of citrus epidermis defects detection based on an improved


YOLOv5. Biosyst Eng 227:19–35. https://doi.org/10.1016/j.biosystemseng.2023.01.018 Hu X, Hu S, Ma LJ et al (2023b) PCB defect detection method based on fusion of MBAM and YOLOv5. J


Graph Theor 45(1):47–55. https://doi.org/10.11996/JG.j.2095-302X.2024010047 Huang C, Wang G, Song H et al (2022a) Rapid surface defects detection in wire and arc additive man­


ufacturing based on laser profilometer. Measurement 189:110503. https://doi.org/10.1016/j. measurement.2021.110503 Huang HX, Tang XD, Wen F et al (2022b) Small object detection method with shallow feature fusion network


for chip surface defect detection. Sci Rep 12(1):3914. https://doi.org/10.1038/s41598-022-07654-x Huang F, Wang BW, Li QP et al (2023a) Texture surface defect detection of plastic relays with an enhanced


feature pyramid network. J Intell Manuf 34(3):1409–1425. https://doi.org/10.1007/s10845-021-01864-2 Huang Y, Tan W, Li L et al (2023b) WFRE-YOLOv8s: a new type of defect detector for steel surfaces. Coat­


ings 13(12). https://doi.org/10.3390/coatings13122011 Huang Z, Jin X, Lu C et al (2023c) Contrastive masked autoencoders are stronger vision learners. IEEE Trans


Pattern Anal Mach Intell. https://doi.org/10.1109/TPAMI.2023.3336525


1 3


<!-- Page 45 -->


Page 45 of 48 333


Surface defect inspection of industrial products with object detection…


Ishida K, Takena Y, Nota Y et al (2023) SA-PatchCore: Anomaly detection in dataset with co-occur­


rence relationships using self-attention. IEEE Access 11:3232–3240. https://doi.org/10.1109/ ACCESS.2023.3234745 Jiang LJ, Yuan BX, Wang YQ et al (2023a) MA-YOLO: a method for detecting surface defects of alu­


minum profiles with attention guidance. IEEE Access 11:71269–71286. https://doi.org/10.1109/ access.2023.3291598 Jiang YY, Cai MN, Zhang D (2023b) Lightweight network DCR-YOLO for surface defect detection on


printed circuit boards. Sensors 23(17). https://doi.org/10.3390/s23177310 Jocher G (2021) Yolov5. https://github.com/ultralytics/yolov5 Jocher G, Chaurasia A, Qiu J YOLO by, Ultralytics et al (2023) Jan. GitHub. https://github.com/ultralytics/


ultralytics. Kong X, Li X, Zhu X et al (2024) Detection model based on improved faster-RCNN in apple orchard envi­


ronment. Intell Syst Appl 21:200325. https://doi.org/10.1016/j.iswa.2024.200325 Li JF, Yang YX (2023) HM-YOLOv5: a fast and accurate network for defect detection of hot-pressed light


guide plates. Eng Appl Artif Intel 117. https://doi.org/10.1016/j.engappai.2022.105529 Li QZ, Wang MH, Gu WK (2002a) Computer vision based system for apple surface defect detection. Comput


Electron Agric 36(2–3):215–223. https://doi.org/10.1016/S0168-1699(02)00093-5 Li CY, Li LL, Jiang HL et al (2022b) YOLOv6: a single-stage object detection framework for industrial appli­


cations. arXiv Preprint. https://doi.org/10.48550/arXiv.2209.02976. arXiv:2209.02976 Li LL, Wang ZF, Zhang TT (2023a) Photovoltaic panel defect detection based on ghost convolution with


BottleneckCSP and tiny target prediction head incorporating YOLOv5. https://doi.org/10.48550/ arXiv.2303.00886 Li S, Kong F, Wang R et al (2023b) EFD-YOLOv4: a steel surface defect detection network with encoder


decoder residual block and feature alignment module. Measurement 220:113359. https://doi. org/10.1016/j.measurement.2023.113359 Li SS, Guo SR, Han ZL et al (2023c) Aluminum surface defect detection method based on a lightweight


YOLOv4 network. Sci Rep 13(1):11077. https://doi.org/10.1038/s41598-023-38085-x Li TJ, Luo J, Fu LX (2023d) Research on surface defect detection method of magnetic tile based on improved


YOLOv5. Inf Technol Inf 12139–141. https://doi.org/10.3969/j.issn.1672-9528.2023.12.032 Li XL, Chu MX, Yang YH (2023e) Surface defect detection of steel plate based on CR-RFPR101. J Hefei


Univ Technol (Nat Sci) 46(12):1651–1658. https://doi.org/10.3969/j.issn.1003-5060.2023.12.010 Li Y, Fang J (2023f) Detection of surface defects of magnetic tiles based on improved YOLOv5. J Sens


2023(1):2466107. https://doi.org/10.1155/2023/2466107 Li A, Hamzah R, Rahim S et al (2024) YOLO algorithm with hybrid attention feature pyramid network


for solder joint defect detection. IEEE Trans Compon Packag Manuf Technol. https://doi.org/10.1109/ TCPMT.2024.3409773 Liang B, Song XF, Gao J et al (2023) Defect detection method of steel wire rope based on YOLO algorithm.


Nondestruct Inspect 47(06):1–4. https://doi.org/10.13689/j.cnki.cn21-1230/th.2023.06.011 Liao XT, Lv SQ, Li DH et al (2021) YOLOv4-MN3 for PCB surface defect detection. Appl Sci 11(24).


https://doi.org/10.3390/app112411701 Liu W, Anguelov D, Erhan D et al (2016) Ssd: Single shot multibox detector. In: Computer Vision–ECCV


2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part I 14. pp 21–37. https://doi.org/10.1007/978-3-319-46448-0_2 Liu K, Wang H, Chen H et al (2017) Steel surface defect detection using a new haar–weibull-variance


model in unsupervised manner. IEEE Trans Instrum Meas 66(10):2585–2596. https://doi.org/10.1109/ TIM.2017.2712838 Liu R, Huang M, Gao Z et al (2023) MSC-DNet: an efficient detector with multi-scale context for defect


detection on strip steel surface. Measurement 209. https://doi.org/10.1016/j.measurement.2023.112467 Liu JC, Lu HK, Li W (2024) YOLO-based surface damage detection of steel cables. Comput Syst Appl


33(01):134–140. https://doi.org/10.15888/j.cnki.csa.009364 Lu P, Zhao TS, Wang J et al (2022) Review on damage identification and health monitoring of steel structures


based on computer vision. Ind Constr 52(10):22–27. https://doi.org/10.13204/j.gyjzg22071401 Luo QW, Sun YC, Li PC et al (2018) Generalized completed local binary patterns for time-efficient steel


surface defect classification. IEEE Trans Instrum Meas 68(3):667–679. https://doi.org/10.1109/ TIM.2018.2852918 Ma ZX, Li YB, Huang MH et al (2022) A lightweight detector based on attention mechanism for aluminum


strip surface defect detection. Comput Ind 136. https://doi.org/10.1016/j.compind.2021.103585 Magnetic-Tile-Defect dataset (2023) https://github.com/abin24/Magnetic-tile-defect-datasets. Accessed 11


July 2023 Matt DT, Modrák V, Zsifkovits H (2020) Industry 4.0 for SMEs: Challenges, opportunities and requirements.


https://doi.org/10.1007/978-3-030-25425-4


1 3


<!-- Page 46 -->


## 333 Page 46 of 48


Y. Ma et al.


NEU-DET Surface Defect Database (2023) http://faculty.neu.edu.cn/songkc/en/zdylm/263265. Accessed 11


July 2023 Pastor-López I, Santos I, Santamaría-Ibirika A et al (2012) Machine-learning-based surface defect detection


and categorisation in high-precision foundry. In: 2012 7th IEEE Conference on Industrial Electronics and Applications. Singapore, pp 1359–1364. https://doi.org/10.1109/ICIEA.2012.6360934 Pierer A, Hauser M, Hoffmann M et al (2022) Inline quality monitoring of reverse extruded aluminum parts


with cathodic dip-paint coating (KTL). Sensors 22:9646. https://doi.org/10.3390/s22249646 PV Multi-Defect Dataset (2023) https://github.com/houhou34/PV-Multi-Defect. Accessed 16 Jan 2023 Ramachandran A, Kundu S, Krishna T (2024) CLAMP-ViT: contrastive data-free learning for adaptive post


training quantization of ViTs. https://doi.org/10.48550/arXiv.2407.05266 Redmon J, Farhadi A (2017) YOLO9000: better, faster, stronger. In: Proceedings of the IEEE conference on


computer vision and pattern recognition. pp 7263–7271. https://doi.org/10.1109/cvpr.2017.690 Redmon J, Farhadi A (2018) Yolov3: an incremental improvement. arXiv Preprint arXiv 02767. https://doi.


org/10.48550/arXiv.1804.02767 Redmon J, Divvala S, Girshick R et al (2016) You only look once: Unified, real-time object detection. In:


Proceedings of the IEEE conference on computer vision and pattern recognition. pp 779–788. https:// doi.org/10.1109/cvpr.2016.91 Ren S, He K, Girshick R et al (2017) Faster r-cnn: towards real-time object detection with region proposal


networks. Adv Neural Inf Process Syst 39(6):1137–1149. https://doi.org/10.1109/TPAMI.2016.2577031 Ruan Z, Chang P, Cui S et al (2023) A precise crop row detection algorithm in complex farmland for unmanned


agricultural machines. Biosyst Eng 232:1–12. https://doi.org/10.1016/j.biosystemseng.2023.06.010 Severstal Dataset (2020)  https://www.kaggle.com/c/severstal-steeldefect-detection/data. Accessed 25 Oct


2019 Shi JT, Yang J, Zhang YT (2022) Research on steel surface defect detection based on YOLOv5 with attention


mechanism. Electron-Switz 11(22). https://doi.org/10.3390/electronics11223735 Siméoni O, Sekkat C, Puy G et al (2023) Unsupervised object localization: Observing the background to


discover objects. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recog­ nition, pp 3176–3186. https://doi.org/10.1109/CVPR52729.2023.00310 Song X, Cao S, Zhang J et al (2024) Steel surface defect detection algorithm based on YOLOv8. Electronics


13(5). https://doi.org/10.3390/electronics13050988 Sunkara R, Luo T (2022) No more strided convolutions or pooling: A new CNN building block for low-res­


olution images and small objects. In: Joint European Conference on Machine Learning and Knowledge Discovery in Databases. pp 443–459. https://doi.org/10.48550/arXiv.2208.03641 Tang TW, Kuo WH, Lan JH et al (2020) Anomaly detection neural network with dual auto-encoders GAN


and its industrial inspection applications. Sensors 20(12):3336. https://doi.org/10.3390/s20123336 Tsai DM, Jen PH (2021) Autoencoder-based anomaly detection for surface defect inspection. Adv Eng Inf


48:101272. https://doi.org/10.1016/j.aei.2021.101272 Uzkent B, Yeh C, Ermon S (2020) Efficient object detection in large images using deep reinforcement learn­


ing. In: Proceedings of the IEEE/CVF winter conference on applications of computer vision. pp 1824– 1833. https://doi.org/10.1109/WACV45572.2020.9093447 Wang CM, Liu H (2024) YOLOv8-VSC: lightweight algorithm for strip surface defect detection. J Front


Comput Sci Technol 18(01):151–160. https://doi.org/10.3778/j.issn.1673-9418.2308060 Wang J, Meng ZH (2020a) Deformable feature pyramid network for aluminum profile surface defect detec­


tion. J Phys: Conf Ser 1544(1). https://doi.org/10.1088/1742-6596/1544/1/012074 Wang L, Zhang D, Guo J et al (2020b) Image anomaly detection using normal data only by latent space


resampling. Appl Sci 10:8660. https://doi.org/10.3390/app10238660 Wang K, Teng ZX, Zou TY (2022a) Metal defect detection based on Yolov5. J Phys Conf Ser 2218(1). https://


doi.org/10.1088/1742-6596/2218/1/012050 Wang Y, Wang HY, Xin Z (2022b) Efficient detection model of steel strip surface defects based on YOLO-V7.


IEEE Access 10:133936–133944. https://doi.org/10.1109/access.2022.3230894 Wang AJ, Yuan JL, Zhu YJ (2023a) Drum roller surface defect detection algorithm based on improved YOLOv8s.


J Zhejiang Univ (Eng Sci) 58(02):370–380. https://doi.org/10.3785/j.issn.1008-973X.2024.02.015 Wang CQ, Sun MX, Cao Y et al (2023b) Lightweight network-based surface defect detection method for steel


plates. Sustainability-Basel 15(4). https://doi.org/10.3390/su15043733 Wang C-Y, Bochkovskiy A, Liao H-YM (2023c) YOLOv7: Trainable bag-of-freebies sets new state-of-the


art for real-time object detectors. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp 7464–7475. https://doi.org/10.1109/CVPR52729.2023.00721 Wang LY, Bai J, Li W et al (2023d) Research progress of YOLO series target detection algorithms. Comput


Eng Appl 1415–29. https://doi.org/10.3778/j.issn.1002-8331.2301-0081 Wang CY, Yeh IH, Liao HYM (2024) YOLOv9: learning what you want to learn using programmable gradi­


ent information. arXiv Preprint. https://doi.org/10.48550/arXiv.2402.13616. arXiv:2402.13616


1 3


<!-- Page 47 -->


Page 47 of 48 333


Surface defect inspection of industrial products with object detection…


Wei RF, Bi YB (2019) Research on recognition technology of aluminum profile surface defects based on deep


learning. Materials 12(10):1681. https://doi.org/10.3390/ma12101681 Wu JS, Wang JQ, Fu MX et al (2022) Determination of defect-testing for steel strips based on improved faster


RCNN algorithm. Angang Technol 06:23–28. https://doi.org/10.3969/j.issn.1006-4613.2022.06.005 Xia Y, Xiao JQ, Weng YS (2021) Surface defect detection of polarizer based on improved Faster-RCNN. Opt


Tech 47(6):695–702. https://doi.org/10.13741/j.cnki.11-1879/o4.2021.06.010 Xia X, Pan X, Li N et al (2022) GAN-based anomaly detection: a review. Neurocomputing 493:497–535.


https://doi.org/10.1016/j.neucom.2021.12.093 Xian Y, Liu G, Fan J et al (2021) YOT-Net: YOLOv3 combined triplet loss network for copper elbow surface


defect detection. Sens (Basel) 21(21). https://doi.org/10.3390/s21217260 Xie YF, Hu WT, Xie SW et al (2022) Surface defect detection algorithm based on feature-enhanced YOLO.


Cogn Comput 15(2):565–579. https://doi.org/10.1007/s12559-022-10061-z Xie YH, Yin B, Han XW et al (2024) Improved YOLOv7-based steel surface defect detection algorithm.


Math Biosci Eng 21(1):346–368. https://doi.org/10.3934/mbe.2024016 Xin HJ, Chen ZB, Wang BY (2021) PCB electronic component defect detection method based on improved


YOLOv4 algorithm. J Phys Conf Ser 1827(1). https://doi.org/10.1088/1742-6596/1827/1/012167 Xu J, Ren H, Cai S et al (2023) An improved faster R-CNN algorithm for assisted detection of lung nodules.


Comput Biol Med 153:106470. https://doi.org/10.1016/j.compbiomed.2022.106470 Yang H, Chen Y, Song K et al (2019) Multiscale feature-clustering-based fully convolutional autoencoder for


fast accurate visual inspection of texture surface defects. IEEE Trans Autom Sci Eng 16(3):1450–1467. https://doi.org/10.1109/TASE.2018.2886031 Yang F, Huo J, Cheng Z et al (2023) An improved mask R-CNN micro-crack detection model for the surface


of metal structural parts. Sensors 24(1). https://doi.org/10.3390/s24010062 Yasir SM, Ahn H (2023) Faster metallic surface defect detection using deep learning with channel shuffling.


Cmc-Comput Mater Con 75(1):1847–1861. https://doi.org/10.32604/cmc.2023.035698 Yu JL, Shi XN, Wang WH et al (2024) LCG-YOLO: a real-time surface defect detection method for metal


components. IEEE Access 12:41436–41451. https://doi.org/10.1109/ACCESS.2024.3378999 Zhang YT, Huang J (2024) Steel surface defect detection based on YOLOv7. Laser J 45(03):87–93. https://


doi.org/10.14016/j.cnki.jgzz.2024.03.087 Zhang XW, Ding YQ, L YY et al (2011) A vision inspection system for the surface defects of strongly


reflected metal based on multi-class SVM. Expert Syst Appl 38(5):5930–5939. https://doi.org/10.1016/j. eswa.2010.11.030 Zhang JQ, Kang X, Ni HJ et al (2020) Surface defect detection of steel strips based on classification priority


YOLOv3-dense network. Ironmak Steelmak 48(5):547–558. https://doi.org/10.1080/03019233.2020.1 816806 Zhang L, Dai Y, Fan F et al (2022) Anomaly detection of GAN industrial image based on attention feature


fusion. Sensors 23(1):355. https://doi.org/10.3390/s23010355 Zhang D, Hao X, Wang D et al (2023a) An efficient lightweight convolutional neural network for industrial sur­


face defect detection. Artif Intell Rev 56(9):10651–10677. https://doi.org/10.1007/s10462-023-10438-y Zhang YL, Li JZ, Fu W et al (2023b) A lightweight YOLOv7 insulator defect detection algorithm based on


DSC-SE. PLoS ONE 18(12):e0289162. https://doi.org/10.1371/journal.pone.0289162 Zhang C, Dai W, Isoni V et al (2023c) Automated anomaly detection for surface defects by dual genera­


tive networks with limited training data. IEEE Trans Ind Inf 20(1):421–431. https://doi.org/10.1109/ TII.2023.3263517 Zhang Z, Zhou M, Wan H et al (2023d) IDD-Net: industrial defect detection method based on deep-learning.


Eng Appl Artif Intell 123:106390. https://doi.org/10.1016/j.engappai.2023.106390 Zhao HL, Yang ZF, Li J et al (2021a) Detection of metal surface defects based on YOLOv4 algorithm. J Phys


Conf Ser 1907. https://doi.org/10.1088/1742-6596/1907/1/012043 Zhao W, Chen F, Huang H et al (2021b) A new steel defect detection algorithm based on deep learning. Com­


put Intell Neurosci (2021):1–13. https://doi.org/10.1155/2021/5592878 Zhao C, Shu X, Yan X et al (2023a) RDD-YOLO: a modified YOLO for detection of steel surface defects.


Measurement 214:112776. https://doi.org/10.1016/j.measurement.2023.112776 Zhao H, Wan F, Lei GB et al (2023b) LSD-YOLOv5: a steel strip surface defect detection algorithm based


on lightweight network and enhanced feature fusion mode. Sensors 23(14). https://doi.org/10.3390/ s23146558 Zhao Z, Wang J, Tao Q et al (2024) An unknown wafer surface defect detection approach based on incre­


mental learning for reliability analysis. Reliab Eng Syst Saf 244:109966. https://doi.org/10.1016/j. ress.2024.109966 Zheng H, Chen X, Cheng H et al (2024) MD-YOLO: surface defect detector for industrial complex environ­


ments. OPT Laser Eng 178:108170. https://doi.org/10.1016/j.optlaseng.2024.108170


1 3


<!-- Page 48 -->


## 333 Page 48 of 48


Y. Ma et al.


Zheng HX, Chen XX, Cheng H et al (2024b) MD-YOLO: surface defect detector for industrial complex


environments. Opt Laser Eng 178:108170. https://doi.org/10.1016/j.optlaseng.2024.108170 Zhou CD, Lu ZY, Lv ZL et al (2023a) Metal surface defect detection based on improved YOLOv5. Sci Rep


13(1):20803. https://doi.org/10.1038/s41598-023-47716-2 Zhou YX, Zhu JH, Wang Y et al (2023b) PCB bare board defect detection based on improved YOLOv7


algorithm. Radioengineering 53(12):2791–2797. https://doi.org/10.3969/j.issn.1003-3106.2023.12.008 Zhu H, Xing L, Fan H et al (2022) New PCB defect identification and classification method combining


MobileNet algorithm and improved YOLOv4 model. https://doi.org/10.21203/rs.3.rs-1544671/v1 Zhu W, Zhang H, Zhang C et al (2023) Surface defect detection and classification of steel using an efficient


Swin Transformer. Adv Eng Inf 57:102061. https://doi.org/10.1016/j.aei.2023.102061 Zhuang CQ, Li JW (2023) Industrial defect detection of plastic labels based on YOLOv5 and generative


adversarial networks. Comput Meas Control 31(07):91–98. https://doi.org/10.16526/j.cnki.11-4762/ tp.2023.07.014


Publisher’s note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


1 3
