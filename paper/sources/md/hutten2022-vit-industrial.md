# hutten2022-vit-industrial


<!-- Page 1 -->


applied sciences


Article Vision Transformer in Industrial Visual Inspection


Nils Hütten * , Richard Meyes and Tobias Meisen *


Chair of Technologies and Management of Digital Transformation, University of Wuppertal, Rainer-Gruenter-Straße 21, 42119 Wuppertal, Germany * Correspondence: nhuetten@uni-wuppertal.de (N.H.); meisen@uni-wuppertal.de (T.M.)


Abstract: Artiﬁcial intelligence as an approach to visual inspection in industrial applications has been considered for decades. Recent successes, driven by advances in deep learning, present a potential paradigm shift and have the potential to facilitate an automated visual inspection, even under complex environmental conditions. Thereby, convolutional neural networks (CNN) have been the de facto standard in deep-learning-based computer vision (CV) for the last 10 years. Recently, attention-based vision transformer architectures emerged and surpassed the performance of CNNs on benchmark datasets, regarding regular CV tasks, such as image classiﬁcation, object detection, or segmentation. Nevertheless, despite their outstanding results, the application of vision transformers to real world visual inspection is sparse. We suspect that this is likely due to the assumption that they require enormous amounts of data to be effective. In this study, we evaluate this assumption. For this, we perform a systematic comparison of seven widely-used state-of-the-art CNN and transformer based architectures trained in three different use cases in the domain of visual damage assessment for railway freight car maintenance. We show that vision transformer models achieve at least equivalent performance to CNNs in industrial applications with sparse data available, and signiﬁcantly surpass them in increasingly complex tasks.


Keywords: deep learning; computer vision; vision transformer; attention mechanism; automated industrial visual inspection; defect detection


Citation: Hütten, N.; Meyes, R.;


Meisen, T. Vision Transformer in


Industrial Visual Inspection. Appl.


Sci. 2022, 12, 11981. https://


## 1. Introduction


doi.org/10.3390/app122311981


Industrial visual inspection (VI) in production and maintenance is under constant pressure from increasing quality requirements due to rising product demands, changing material, and cost speciﬁcations. In addition, there are changing external factors, such as new and constantly changing legal requirements, standards, and norms. Further, the risk of reputational damage from substandard products is steadily increasing due to the growing information availability and distribution through digital channels, such as social media, video sharing platforms, and review websites. Visual quality assurance is still predominantly performed or supported by human inspectors, which has several drawbacks, that have been studied by Steger et al. [1] and Sheehan et al. [2]. These include, but are not limited to, high labor cost, low efﬁciency, and low real-time performance on fast moving inspection objects or large surface areas. According to Swain and Guttmann [3], minimal error rates of 0.1% are reachable for very simple accept/reject tasks, which do account for negative inﬂuences of typical human inconsistency features, such as temporal fatigue. Though highly dependent on the inspection task, the ﬁndings of Drury and Fox [4] state that in more complex tasks error rates of 20% to 30% are observable. This can be seen as a rough general estimate for human error rates in visual inspection.


Academic Editors: Bing Li and


Shivam Kalra


Received: 3 November 2022


Accepted: 21 November 2022


Published: 23 November 2022


Publisher’s Note: MDPI stays neutral


with regard to jurisdictional claims in


published maps and institutional afﬁl


iations.


Copyright: © 2022 by the authors.


Licensee MDPI, Basel, Switzerland.


This article is an open access article


In order to improve efﬁciency and performance, as well as reduce cost, several contributions from the domain of computer vision (CV) have been proposed to automate VI. Recently, deep learning-based models, such as convolutional neural networks (CNN) [5] superseded traditional feature-based methods. In 2017, transformers, the newest type of model in deep learning, started breaking performance records in the ﬁeld of natural


distributed under the terms and


conditions of the Creative Commons


Attribution (CC BY) license (https://


creativecommons.org/licenses/by/


4.0/).


Appl. Sci. 2022, 12, 11981. https://doi.org/10.3390/app122311981 https://www.mdpi.com/journal/applsci


<!-- Page 2 -->


Appl. Sci. 2022, 12, 11981 2 of 16


language processing (NLP) [6–9], but also made its way into CV and claimed benchmarks there in the last two years [10–12]. Recently, there have already been ﬁrst applications of vision transformers in VI [13,14]. While both publications demonstrate the capability of vision transformers in VI, they only cover one speciﬁc task, respectively. The work of Liu et al. [13] features a relatively simple task with small training datasets and low intraclass variation, whereas Wang et al. [14] address a more complex task, regarding number of classes, as well as detection targets per image, with a dataset of approximately twice the size. As we will discuss later, it is not possible to make a general statement about the capability of vision transformer for maintenance VI applications from their results.


To address this we selected a scenario that is a good representation of the area of maintenance VI, as it covers a wide variety of inspection use cases, to investigate the applicability of vision transformers. Our scenario comes from the context of rail freight transport, speciﬁcally, we investigate the inspection of returning freight cars after train decomposition at railroad yards to ensure operational, as well as trafﬁc, safety. Out of the wide variety of possible use cases, we consider three learning tasks, characterized by different challenges such as high intra-class variation, large number of classes, or detection targets per image and small target objects. The ﬁrst use case is damage detection in wagon sheet metal ﬂooring with one distinct damage class that is very small in size and has similar features, as well as complexity to the one addressed by Liu et al. [13]. The second use case covers damage detection in wooden load spaces with three damage classes containing strong intra-class variation, due to different wood textures, as well as deterioration states. This one shows parallels to the work of Wang et al. [14] regarding its properties and complexity. The third use case, the localization and recognition of wagon caption characters as a foundation for matching wagons with an internal database, is characterized by a high number of classes and targets per image. This marks a complexity level beyond previous publications employing vision transformers in the context of AVI. One common challenge of all these use cases is the small amount of labeled training data for vision tasks of their complexity, typical for industrial applications. As a contribution, we evaluate how well three state-of-the-art (SOTA) vision transformer-based models, two of which, to our knowledge, have not been applied to VI before, are able to overcome the aforementioned challenges. They are compared with each other and to four established CNN models, which serve as baselines for the current SOTA in VI. We will show that performance wise the transformer architecture is on par with the CNN’s on the easier tasks, but really shows its strengths with rising task complexity.


The remainder of this paper is structured as follows: Section 2 provides an overview of related work regarding transformer models and deep-learning-based industrial VI. Section 3 introduces the learning tasks and describes the corresponding datasets. Subsequently, Section 4 describes the experiment settings and presents the obtained results. Finally, Section 5 concludes the paper with a summary of the results and discusses their implications for the direction of future research.


## 2. Related Work


This chapter is divided into three subsections. Section 2.1 covers the origin and evolution of transformer models in NLP. This is followed by their transfer into CV in Section 2.2 and concluded with Section 2.3 covering recent publications applying CNN, as well as vision transformers to VI use cases, on which we based our model selection.


## 2.1. Transformer Models in NLP


Transformers are sequence to sequence models that were proposed for the ﬁrst time by Vaswani et al. in 2017 [7] in the context of natural language processing (NLP). They demonstrated exemplary performance in a broad range of language tasks, such as text classiﬁcation, machine translation, and question answering [11], improving on previous records set by recurrent neural networks (RNN). This became possible through the combination of several, new or already existing, concepts. Word embeddings enable them to


<!-- Page 3 -->


Appl. Sci. 2022, 12, 11981 3 of 16


capture the semantic relations between words. Multi-head self-attention reﬁnes these raw embeddings in the context of speciﬁc inputs, as well as parallelizes the computation, by working on all input tokens at once, in contrast to the sequential process of RNNs. Lastly, they also utilize residual connections that increase the availability of information from shallower layers across the whole network and improve model convergence capability and speed by increasing gradient ﬂow during backpropagation. The parallelization also makes them extremely scalable, which resulted in model size growth in popular models from 213 million parameters of the original transformer model to 340 million parameters of BERT large [8], 1.5 billion parameters of GPT-2 [15], and 175 billion parameters of GPT-3 [9]. This scaling resulted in an ever-growing performance and ability to generalize, but was not achieved without any drawbacks.


Despite their great capabilities, transformers face similar and, in some cases, ampliﬁed versions of the problems that RNNs had as well. First, like with most state-of-the-art deep learning models, large datasets are required for training. Second, they show slower convergence than, e.g., RNN or CNN models, because their structure does not inject them with prior knowledge their developers deem useful for the task at hand (inductive bias). This results in a larger solution space that is searched during training and, therefore, requires more time to converge. Third, extremely powerful hardware, regarding memory and ﬂoating-point operations per second (FLOPS), is required to train them due to the quadratic scaling of self-attention with the input length.


There have been several efforts to overcome these problems, mainly focused on reducing the complexity of the self-attention computation. Kitaev et al. [16] introduced locality sensitive hashing attention to reduce the complexity of self-attention to O(n log(n)) by approximation. Additionally, they proposed reversible layers, which enable the storage of only the ﬁnal activations for backpropagation, and, therefore, reduce the memory footprint at cost of additional calculations. Wang et al. [17] improve on this with their Linformer, bringing the complexity of the approximation down to O(n) in time and memory space. This is possible because the result of the softmax operation in self-attention, the context mapping matrix P, is of low rank (Equation (1)). Therefore, the self-attention result can still be well approximated with a lower dimensionality linear projection of the key and value matrix (Q, V).


##  QWQKWK





## VWV (1)


√dk


Self-Attention = softmax


| {z } P


## 2.2. Transformer Models in CV


The impressive results of these models in NLP has drawn the attention of CV researchers to adapt them to their domain. To be able to feed image data into transformers it has to be transformed into sequences. Two different lines of pre-processing have been established depending on the role of the transformer model in the overall architecture: for backbone networks such as the vision transformer (ViT) [18] or the shifted windows transformer (Swin) [19] the input image is divided into patches. These are ﬂattened and then each of them serves as one input sequence/token, like in NLP. Detection heads such as the detection transformer (DETR) [20] and the dynamic head transformer (DyHead) [21] process the ﬂattened features extracted by an upstream CNN. In the following, we will present how DETR, deformable DETR (DDETR) [22], as well as Swin are structured and how they adapt ideas from NLP to reduce the complexity of the self-attention computation.


The transformer model in DETR is structurally almost identical to the original model introduced by Vaswani et al. The main differences are: it utilizes features extracted by a CNN backbone as input as visualized in Figure 1. These feature maps are encoded into a sequence with reduced overall dimension using a 1 × 1 convolutional layer. Static two-dimensional positional encodings are added to this sequence, as well as the input to all other encoder and decoder layers instead of only the ﬁrst one. The decoder’s input is


<!-- Page 4 -->


Appl. Sci. 2022, 12, 11981 4 of 16


not a forward masked version of the encoder input, instead so-called object queries are used. The model features two output branches, one for class- and one for bounding box prediction. Additionally, the outputs do not require any non-maximum suppression (NMS) post-processing, because the predictions are optimized to ﬁnd the best bi-partite matching with the ground truth employing the Hungarian matching algorithm [23]. Although, the performance of this model is comparable to F-RCNN’s with the same backbone, it has two problems: slow convergence speed, which was reported to be 48 days on one Nvidia V100 GPU [24], when trained from scratch; and high computational cost due to the use of full (self-)attention.


Figure 1. DETR architecture [20].


DDETR improves on DETR by proposing deformable (self-)attention. It is based on the observation that the attention matrices are very sparse usually and the results are dominated by a small number of keys for each query. Therefore, the number of keys that is considered by a query is limited to k, to reduce the number of required operations. The top center of Figure 2 shows the additional linear layer that is established to learn which k keys, around the reference point pq, associated with the given query features zq, to use for the attention computation. This concept, inspired by deformable convolutions [25], reduces the training time to about 14 V100 days, while also improving the performance [22]. In addition to deformable (self-)attention, Dai et al. propose three additional improvements: extension of deformable attention to multiple feature map scales, iterative bounding box reﬁnement, where each decoder layers further reﬁnes the predictions of the previous one and a two-stage version of the model, with an additional encoder part of DDETR acting as a proposal generator for a full DDETR head.


Figure 2. Illustration of the deformable (self-)attention module [22].


<!-- Page 5 -->


Appl. Sci. 2022, 12, 11981 5 of 16


Opposed to DETR and DDETR the Swin transformer operates on embedded, ﬂattened patches of the input image and can function as the backbone of detection architectures like faster R-CNN (F-RCNN), Retina Net, or Yolo. To reduce the number of operations to compute self-attention, it is not evaluated over all patches, but only for non-overlapping windows containing M × M patches (Figure 3).


Figure 3. Visualization of the concept of patches and windows in the Swin transformer.


The window positions are not static, but shifted every layer to enable cross-window information ﬂow, which partly preserves the global modeling power of self-attention. After a speciﬁc number of layers neighboring features are merged, by concatenating groups of 2 × 2 patches, effectively reducing the feature resolution by half but doubling the depth. Figure 4 depicts the location of these patch merging layers found after 2, 4, 10, and 12 transformer blocks in the smallest model version. They fulﬁll a similar function to pooling layers and the increasing number of convolutional kernels in deeper layers in CNNs. There are four different sizes of the model: tiny, small, base, and large, reaching from 36 to 197 million parameters. All size variants of the model reduce the feature resolution to 1/16th of the input, similar to many established CNN backbones. This makes it relatively easy to exchange the backbone in many object detection or segmentation architectures with a Swin transformer.


Figure 4. Swin tiny transformer architecture [19].


Transformer detection heads, such as DETR, as well as backbones, such as Swin, have been shown to yield exceptional performances in object detection posting mean average precision (mAP) above 60% on the COCO benchmark dataset [26] outperforming the best CNN model YOLOR-D6 [27] by more than 2.5%.


## 2.3. Recent Visual Inspection Examples Utilizing Deep Learning


Since CNN’s have made their entrance to CV with AlexNets ﬁrst place in the 2012 Image Net Large Scale Visual Recognition Challenge (ILSVRC) [28], they have advanced the state-of-the art in closely related areas, such as automated visual inspection, by superseding traditional feature-based methods.


Zeng et al. [29] proposed a CNN-based method for the inspection of 23 categories of train-bogey-parts, such as wheels, brakes, springs, bearings, and screws. They utilize a F-RCNN [30] architecture with ResNet-101 [31] backbone enhanced by a FPN [32] and an


<!-- Page 6 -->


Appl. Sci. 2022, 12, 11981 6 of 16


additional RNN submodel. This submodel is establishes a new form of gated recurrent unit (GRU) [33] to learn the strong structural correlation in technical systems. The model is evaluated on a dataset of 1130 images, containing 23 annotation classes in three sizes, where it achieves a mAP of 87.18%. In addition to this, the model is assessed on the benchmark datasets Pascal VOC 2007 and 2012 [34] and attains mAPs of 79.83% and 75.24%, respectively. Chun et al. [35] developed a method for automatic defect detection on asphalt pavements utilizing a Yolo V3 [36] architecture. They trained their model to locate and classify four damage types: longitudinal, transverse, and alligator cracks, as well as potholes with a dataset of approximately 5000 color images and achieved an F1-Score of 60%.


Very recently, one of the ﬁrst VI papers applying a transformer model to crack segmentation in stone and concrete surfaces has been published by Liu et al. [13]. Inspired by SegNet, their architecture follows an encoder–decoder structure [37] with the convolutional layers in encoder and decoder replaced by self-attention blocks. They also proposed a scaling attention block to execute the processing in the feature aggregation path. They achieved new performance records on the public datasets Crack Tree 260 [38], CrackLS 315 [39], and Stone 331 [40], improving the previous results by 0.6%p to 2.1%p. Wang et al. [14] tackled the detection of major, safety critical, components of railway tracks with a transformer model. Their models employs a ResNet-50 or Darknet-53 backbone and transformer detection head, with two parallel feed forward networks, one for class and one bounding box prediction, to generate the output. They achieve a mAP of 61.9% with their best model.


Model Selection Based on Benchmarks and Recent Applications


We selected CNN and transformer models based on their benchmark results on the COCO dataset on the one hand and their occurrence in recent VI research papers on the other hand [29,35,41–43]. The models are DETR, DDETR and Swin, Yolo V3, F-RCNN, and Retina Net. All models except Yolo V3 and Retina Net utilized a ResNet-50 backbone. While Yolo used its original DarkNet-53 backbone, Retina Net was employed with three different ones: ResNet-50 for comparison with the other models; ResNext-101 (Retina Next) as a representative of larger more recent CNN architectures with a similar number of parameters and performance to the transformer models [44]; Swin in its “small” version to have a detection head for the only transformer backbone in this study. To complete the list we would have liked to evaluate the model by Wang et al. as well, but unfortunately it was not accessible.


## 3. Learning Task Description


As stated in the introduction, with this paper we want to reach a more general conclusion about the suitability and performance of vision transformers in industrial VI scenarios with small datasets. For this purpose, we have selected learning tasks from the context of rail freight transport. Speciﬁcally, we investigate the inspection of returning freight cars after train decomposition at railroad yards. The damage register contains over 1000 defect codes that cover things such as damaged load spaces, damaged or disconnected grounding cables, damage to bogie parts such as springs or wheels, but also unreadable captions or warning signs because of abrasion or grafﬁti contamination. Out of the wide variety of possible use cases, we consider three learning tasks, characterized by differences in intra-class variation, number of classes and detection targets per image.


The ﬁrst use case, in the following referred to as sheet metal (SM) use case, covers the detection of small to medium size holes in sheet metal ﬂoorings of wagons, that cover 2 × 10−2% of the inspection image on average. This is important as load, for these wagons usually bulk cargo, induced by vibrations during transport, can fall through the holes, which, on the one hand, is a commercial damage because of the lost goods and on the other hand particles or small gravel-like objects that land on the railway tracks pose a danger to trafﬁc safety.


<!-- Page 7 -->


Appl. Sci. 2022, 12, 11981 7 of 16


Figure 5 illustrates the two main challenges of this use case: On the one hand, the generally small size of the defects (left) and on the other hand the varying light conditions, as well as eventual reﬂections caused by wet surfaces (right).


The task is formulated as a one-class object detection problem. The dataset of this use case consists of 192 top view images, that contain a total of 394 damages, which is equal to 2.05 damages per image.


Figure 5. Top view image with sheet metal ﬂooring damage examples.


The second use case features three different damage types on wooden freight car load spaces (WLS). Its dataset is made up of 156 top view images including 255 annotations, with eight samples for damaged load support bearings or frames, 56 damaged wooden ﬁllings of load supports, and 207 damages to ﬂoor boards (Table 1).


Table 1. Class distribution of wooden load space dataset.


Damage Type Number of Occurences


Load support bearing 8 Damaged wooden ﬁlling 56 Damaged board 206


The three damage types are depicted by example in Figure 6: the leftmost image shows that the connection to the bearing of a foldable load support has been detached by overstrain. In the middle one, a part of the wooden ﬁlling of a load support broke out of its frame and the one right shows a broken ﬂoor board. Broken ﬂoor boards mainly pose the threat of injury to loading or maintenance personal, when stepping on them, while damages to the load supports are inﬂuencing the proper securing of the cargo. The dataset characteristics are high color variety of the wooden components and a higher number of classes compared to sheet metal, as well as strong class imbalance.


The third use case, character recognition (CR), is the recognition of errors of captions on the side of the cars, such as loading tables, maximum load volume, length of the wagon from buffer to buffer, and other speciﬁcations. Most of these captions must be present and properly readable for the wagons to be legally in operation. Additionally, caption matching with an internal database can be the corner stone for a future system that automatically detects damage, assigns them to the database entry of the corresponding wagon and schedules its next workshop maintenance date. Figure 7 depicts some examples of captions. The base for the caption matching is the localization and classiﬁcation of 43 different characters including letters, numbers, and special characters. The corresponding dataset features 200 side view greyscale images containing 21,571 bounding boxes, which is equal to 108 per image on average. Figure 8 visualizes the strongly imbalanced distribution of the 43 classes, which is one of its challenges, in addition to it featuring a lot of classes and detection targets per image.


<!-- Page 8 -->


Appl. Sci. 2022, 12, 11981 8 of 16


Figure 6. Top view image with wooden loadspace damage examples.


Figure 7. Side view image with character recognition examples.


Figure 8. Class distribution of the character recognition dataset.


For all three tasks, large-scale, high-deﬁnition, line-scan images with heights from 2048 to 4096 pixels and variable width are used as input data. The images were captured throughout day and night, across all seasons, at railroad yards in different locations from frames spanning over the tracks. Therefore, the light conditions vary from normal daylight to artiﬁcial lighting at night. Due to the widths of some images reaching more than 20,000 pixels, they are resized to limit their memory consumption in model training. The dimensions are adjusted so that the longer side, which is usually the width, is exactly


<!-- Page 9 -->


Appl. Sci. 2022, 12, 11981 9 of 16


3072 pixels and the height is set accordingly to keep the aspect ratio constant. Table 2 summarizes detailed information about all datasets.


Table 2. Characteristics of the datasets utilized in this study.


Task # Images # Annotations # Classes Input Size (w, h) Step Size


Sheet metal ﬂooring 192 394 1 (3072, *) -


Sheet metal ﬂooring, windowed 219 223 1 (1024, 1024) 800, 800


Wooden load space 156 255 3 (3072, *) -


Wood load space, windowed 746 957 3 (512, 1024) 400, 400


Characters 200 21.571 43 (3072, *) -


Characters, windowed 1871 27.81 43 (1024, 1024) 800, 800


* corresponding height to keep aspect ratio.


## 4. Experiments and Results 4.1. Experiment Settings


The experiments were executed with the complete resized images, as well as with crops generated by a sliding window approach, applied to the full resolution original images, as input. Due to the tall and narrow shapes of the damages in the wooden load space (WLS) use case, we chose a rectangular window shape of 1024 × 512, while the sheet metal and character recognition (CR) use cases utilize a square shape of 1024 × 1024. The crop resulting from a certain window position is only used if it contains a visible bounding box as this showed to yield the best performance. Table 2 summarizes the characteristics of the six utilized datasets. The datasets are split into training, validation, and test sets with a ratio of 80%, 10%, and 10%, respectively. We balanced the ratio of classes for WLS and CR in all sets equally so that the ratio was the same as in the original data to avoid under-representation of certain classes.


Transfer learning is utilized by initialization with weights from models pre-trained on COCO to reduce the training time and number of required samples. We selected the AdamW optimizer [45] due to its good performance on benchmark datasets in CV [19,20,46–49]. To achieve better optimized weights due to smaller possible increments of adaptation, the initial learning rate of 1 · 10−4 is decayed by a factor of 0.1 at epoch 40 for the DETR family models and at epoch 100 for the CNN models Supplementary the gradients of DETR and DDETR are limited to L2-Norm ≤0.1 during training to prevent exploding gradients. Data augmentation is used according to the original publications’ speciﬁcations [20,22,30,36,50]. This means random ﬂipping with a probability of 50% for Retina Net and F-RCNN. DETR and DDETR utilize random ﬂipping and random crops with resizing. For Yolo v3, a variety of photometric distortions, random crops and random ﬂipping augment the input. Additionally, the inputs for all models are padded to a shape that makes them divisible by 32, to achieve a constant input size, which is required by all detection heads. Our models were implemented with MMDetection, an open source object detection toolbox [51], which offers modularity for models and train/test pipelines, as well as a wide variety of pre-trained models and utility functions. We trained all models for 150 epochs on eight Nvidia V100 GPUs with 32 GB memory, with the maximum batch size the memory allows for (details in Table 3). By doing so, we utilized the full capacity of the hardware, but lost some comparability between the models, because of the differing batch sizes. The loss of comparability can be justiﬁed by more stable training and better generalization as shown in the next chapter.


<!-- Page 10 -->


Appl. Sci. 2022, 12, 11981 10 of 16


Table 3. Model performances; bold numbers highlight the best performance for each use case.


Model Epoch Batch Size mAP50,test F1-Scoreinitial F1-Scoreadjusted IoU


DDETR 120 1 × 8 0.699 0.640 0.704 0.25 DETR 130 1 × 8 0.061 0.098 0.164 0.1 F-RCNN 80 5 × 8 0.245 0.340 0.472 0.2 Retina 100 20 × 8 0.511 0.645 0.813 0.1 Yolo V3 120 3 × 8 0.595 0.574 0.713 0.2 RetinaNext 150 2 × 8 0.112 0.240 0.380 0.2 Retina Swin 130 2 × 8 0.532 0.705 0.791 0.25


Sheet metal


DDETR 110 1 × 8 0.414 0.491 0.526 0.25 DETR 110 1 × 8 0.047 0.135 0.157 0.4 F-RCNN 70 5 × 8 0.393 0.415 0.453 0.3 Retina 60 7 × 8 0.389 0.475 0.644 0.2 Yolo V3 150 2 × 8 0.522 0.531 0.571 0.3 RetinaNext 150 2 × 8 0.056 0.195 0.244 0.4 Retina Swin 70 2 × 8 0.335 0.407 0.556 0.1


load space


Wooden


DDETR 150 4 × 8 0.998 0.927 - - DETR 130 4 × 8 0.886 0.833 - - F-RCNN 120 18 × 8 0.931 0.826 0.913 0.3 Retina 60 7 × 8 0.938 0.913 - - Yolo V3 80 12 × 8 0.895 0.872 - - RetinaNext 150 6 × 8 0.727 0.773 0.818 - Retina Swin 70 6 × 8 0.899 0.870 0.913 0.4


Sheet metal


window


DDETR 150 6 × 8 0.928 0.878 0.898 0.3 DETR 150 6 × 8 0.433 0.613 0.639 0.2 F-RCNN 110 24 × 8 0.926 0.887 0.906 0.4 Retina 100 28 × 8 0.942 0.913 0.922 0.4 Yolo V3 110 14 × 8 0.862 0.779 0.802 0.4 RetinaNext 150 6 × 8 0.498 0.759 0.802 0.1 Retina Swin 70 6 × 8 0.949 0.907 0.927 0.3


load space


window


Wooden


DDETR 150 6 × 8 0.676 0.779 0.912 0.2 DETR 150 10 × 8 0.383 0.522 0.616 0.2 F-RCNN 140 18 × 8 0.62 0.764 0.879 0.1 Retina 70 20 × 8 0.581 0.744 0.821 0.1 Yolo V3 120 10 × 8 0.621 0.776 0.885 0.1 RetinaNext 150 6 × 8 0.492 0.725 0.788 0.2 Retina Swin 90 6 × 8 0.617 0.773 0.885 0.1


recognition


Character


window


## 4.2. Results


Figure 9 shows the development of the mAP with at least 50% IoU between predicted bounding boxes and ground truth on the validation set (mAP50,val) of the sheet metal use case. The strong oscillation in the performance of the transformer models is present during training of all full image use cases and makes it hard to determine if the models have converged. This instability is caused by the low batch size utilized with these models due to their high memory requirements, and further ampliﬁed by the large size of the input images.


Figure 10 visualizes the mAP50,val during training of the sliding window version of the wooden load space use case. It is clearly visible that the stability of the training process is positively inﬂuenced by the possibility to use higher batch sizes due to smaller input images. Retina Net and Retina Swin converge the fastest approximately at epoch 50, followed by DDETR, Yolo, and F-RCNN around epoch 110 and DETR at epoch 120. Retina Next seems to keep improving until epoch 150 and could possibly still beneﬁt from continued training based on the curve’s upward gradient. This shows on the one hand how effective the improvements of DDETR on DETR are in low-data environments, and on the other hand that DDETR has a comparable convergence speed to commonly used CNN models, even


<!-- Page 11 -->


Appl. Sci. 2022, 12, 11981 11 of 16


with lower batch size due to high memory requirements. Retina Swin converges as fast as the fastest pure CNN in Retina Net with even better precision.


Figure 9. mAP50,val development during training of the sheet metal use case.


Figure 10. mAP50,val development during training of the wooden load space use case.


In order to determine the best weights for each model, checkpoints were saved every 10 epochs from epoch 50 onwards and evaluated on the test set. The checkpoint with best mAP50,test at the lowest epoch is selected for the following comparison. As neither recall nor precision can be neglected in industrial visual inspection, we choose their harmonic mean, also known as F1-Score, as the performance metric.


For the initial F1-Score (F1-Scoreinitial) a prediction is considered to be correct, if it achieves 50% IoU and prediction conﬁdence, which are the usual values used on benchmark datasets. Compared to benchmarks such as COCO, perfect alignment of predicted bounding boxes is not as important in real world applications as long as the targets are recognized.


<!-- Page 12 -->


Appl. Sci. 2022, 12, 11981 12 of 16


Therefore, the reduction in the models’ IoU threshold for the given task can improve


F1-Scoreinitial, in many cases without drawbacks to F1-Scoreadjusted. The adjusted IoU values for each model are listed in Table 3 in the last column. The prediction conﬁdence correctness threshold is still kept at 50% to retain the same prediction quality as for F1-Scoreinitial. In the following, we will analyze the performance of all models summarized in Table 2, use case by use case regarding mAP50,test, F1-Scoreinitial and F1-Scoreadjusted.


## 4.2.1. Full Images


In the sheet metal (SM) use case, the DDETR model achieves the highest mAP50,test of 69.9%, when looking at F1-Scoreinitial it is surpassed by Retina Swin by 6.5%p. Probably, this is due to DDETRs matching loss, which optimizes the model to preferably output only one prediction per ground truth bounding box. This, in turn, leads to lower recall compared to the Retina architecture models and, therefore, to a lower F1-Score. After adjusting the IoU threshold, Retina Net takes the lead with 81.3% F1-Scoreadjusted, while Retina Swin comes in second at 79.1%. The reason for this could be the fact that the weights of Retina Nets backbone and head used for transfer learning have been optimized jointly on COCO before, while the Swin weights and Retina head of Retina Swin are loaded separately before training on the SM use case. Yolo also slightly outperforms DDETR by 0.9%p. The DETR model signiﬁcantly suffers from the low batch and general dataset size, as expected, resulting in the worst performance of all evaluated models in all metrics.


For the wooden load space (WLS) use case, the best performing models are Yolo V3, considering 52.2% mAP50,test, respectively, 53.1% F1-Scoreinitial and Retina Net with the best F1-Scoreadjusted, amounting to 64.4%. This can be explained by the greater number of generated predictions before NMS of Retina Net compared to Yolo V3 (100k vs. 10k), which results in a higher recall and, consequently, a higher F1-Score. DDETR ranks third in


mAP50,test, second in F1-Scoreinitial and third again in F1-Scoreadjusted, with values of 41.4%, 49.1% and 52.6%, respectively. Generally, the models performed worse compared to the SM use case, due to the higher difﬁculty caused by more damage classes, as well as higher intra-class variability. The complexity of the character recognition (CR) use case cannot be handled by any of the evaluated models, none of them were able learn to predict overlapping bounding boxes on the full images at the utilized resolution. Higher resolution training was not explored as for the DETR family models, it would have exceeded the memory capacity of our hardware.


## 4.2.2. Sliding Window Approach


In the sliding window version of the SM use case the DDETR outperforms the other models in all the evaluated performance metrics, followed by Retina Net in mAP50,test and Retina Net, Retina Swin, as well as F-RCNN regarding F1-Scoreadjusted. The higher training batch size enables the DDETR to perform very close to 100%, while the other models do also show improvements they cannot match this. The DETR and Retina Next models also show strong improvements of their results of 30 to 40%p. There is also no performance gain in reducing the IoU threshold for DDETR, DETR, Retina Net and Yolo V3 in this use case. Compared to the SM use case with full images, the performance of all models improved signiﬁcantly, because of the higher resolution input and increased pool of training samples.


Retina Swin shows the best performance considering mAP50,test, F1-Scoreadjusted in the sliding window version of the WLS use case with 0.7%p and 0.5%p better results than Retina Net. This indicates that for damage characterized by a wider color variety, such as on these wooden surfaces, the global feature relations modelling capability of the Swin transformer backbone is superior to the ResNet-50. Retina Next, as well as DETR, show signiﬁcant improvements over their results on full images. DETR’s convergence is still slower due to its lower inductive bias, compared to the sliding kernel of a CNN-like Retina Next, which assumes strong connections between local features.


In the sliding window version of the CR use case, DDETR bests F-RCNN considering mAP50,test by 5.5%p. Regarding F1-Scoreinitial, the performances are very close, differing


<!-- Page 13 -->


Appl. Sci. 2022, 12, 11981 13 of 16


only by 0.3%p between DETR and Yolo v3, while they are more distinct when looking at F1-Scoreadjusted with 2.7%p difference. Retina Swin’s performance is very similar to Yolo v3. The distinction between many and sometimes very similar letter shapes seems to be the strength of the DDETR detection head, possibly due to the different emphasis of the attention heads. As the inputs are greyscale images the seemingly limited feature extraction capability of the CNN backbones compared to Swin, noted in the sliding window version of the WLS use case, does not have negative impact here.


Overall, the performance of all models is signiﬁcantly improved by the sliding window approach, as to be expected with higher feature resolution and larger batch sizes due to smaller inputs, at the cost of additional computation. Additionally, there is less area of the inputs that does not contain any damages, which reduces the difﬁculty of the task.


## 5. Conclusions and Outlook


In this paper, we evaluated the capability of state of the art vision transformer models for industrial VI in three representative low data use cases. These use cases are from the context of damage assessment of freight cars after train decomposition at railroad yards. The three use cases are: damage detection in sheet metal ﬂooring, damage detection in wooden load spaces, and character localization and recognition as a foundation for matching wagons with an internal database. The last of the three marks a complexity level beyond previous publications employing vision transformers in the context of AVI.


We trained three different transformer-based architectures, DETR, DDETR, and (Retina-)Swin, of which the last two to our knowledge have not been applied to VI before. For comparison we also trained four established CNN-based architectures—F-RCNN, Retina Net, Yolo V3, and RetinaNext—that represent the current SOTA in VI as baselines. Each use case was evaluated on downscaled, full images and patches generated by a sliding window method, due to the large dimensions of the input images.


The DDETR model achieves the best results in the detection of holes in sheet metal and the recognition of characters utilizing a sliding window approach with a F1-Scoreadjusted of 92.7% and 77.9%. It seems to be very good at the differentiation between many similarly shaped objects. The Swin model with a Retina detection head delivers the best performance in the windowed version of the wooden load space use case with a F1-Scoreadjusted of 92.7%. It appears its capability to exchange information between the attention windows is especially useful when damages spread across wide areas of the images and have a high level of color variety. Considering the full image versions of the use cases the transformer models cannot surpass the CNN models, because the high memory requirements resulting from the large images limit their potential. After our studies, we can give the clear recommendation to apply vision transformer models to industrial visual inspection scenarios with typical input image sizes as they:


• Perform better than typically used CNN models; • Show no signiﬁcant difference in convergence speed compared to CNNs; • Handle small datasets commonly utilized in industrial VI well.


Yet there is still room for improvement as the models were not modiﬁed to speciﬁcally ﬁt the intricacies of the presented VI use cases to, e.g., better handle very large-scale input data, improve detection of small damages or become injected with prior knowledge of the typical hierarchical structure of the inspected technical systems. Based on our results it seems the combination of a Swin backbone with a DDETR detection head would achieve optimal VI results and should be evaluated in future work. Since the acquisition of labelled data is generally very expensive, other approaches are needed. Unsupervised learning offers promising concepts, such as masked patch reconstruction [52] and the soft-teacher approach [24], that need to be further explored. Solely supervised training also limits the achievable performance gains by scaling models up, which is why unsupervised pretraining played a key part in unlocking model dimensions and performances that GPT-3 exhibits in NLP, as a prime example model from the transformer family. This also enabled the concept of having one large general-purpose foundation model and use its outputs for


<!-- Page 14 -->


Appl. Sci. 2022, 12, 11981 14 of 16


zero- or few-shot learning of small task speciﬁc adapter models. The adaptation of this concept to VI could also prove highly valuable, as it would alleviate the labeling efforts and extremely shorten or even completely negate training time.


Author Contributions: Conceptualization, methodology, formal analysis, investigation, writing— original draft preparation N.H.; writing—review and editing, R.M. and T.M.; project administration, funding acquisition, R.M.; supervision, resources, T.M. All authors have read and agreed to the published version of the manuscript.


Funding: This research was funded by the German Federal Ministry for Digital and Transport in the program “future rail freight transport” under grant number 53T20011UW.


Institutional Review Board Statement: Not applicable.


Informed Consent Statement: Not applicable.


Data Availability Statement: Restrictions apply to the availability of these data. Data were obtained from Deutsche Bahn Cargo and are available from the authors with the permission of Deutsch Bahn Cargo.


Conﬂicts of Interest: The authors declare no conﬂicts of interest.


Abbreviations


The following abbreviations are used in this manuscript:


BERT Bidirectional encoder representations from transformers CNN Convolutional neural network COCO Common objects in context (object detection) dataset CR Character recognition CV Computer vision DETR Detection transformer DDETR Deformable detection transformer FLOPS Floating-point operations per second FPN Feature pyramid network F-RCNN Faster regional convolutional neural network GPU Graphics processing unit GPT Generative Pre-trained Transformer GRU Gated recurrent unit mAP Mean average precision (Common object detection performance metric) NLP Natural language processing NMS Non-maximum suppression Pascal VOC Pascal visual object classes (object detection dataset) RNN Recurrent neural network SM Sheet metal SOTA State-of-the-art VI Visual inspection WLS Wooden load spaces Yolo You only look once (Object detection model)


## References


1. Steger, C.; Ulrich, M.; Wiedemann, C. Machine Vision Algorithms and Applications; John Wiley & Sons: Hoboken, NJ, USA, 2018. 2. Sheehan, J.J.; Drury, C.G. The analysis of industrial inspection. Appl. Ergon. 1971, 2, 74–78. [CrossRef] [PubMed] 3. Swain, A.D.; Guttmann, H.E. Handbook of Human-Reliability Analysis with Emphasis on Nuclear Power Plant Applications; Final Report; Sandia National Labs.: Albuquerque, NM, USA, 1983. [CrossRef] 4. Drury, C.G.; Fox, J.G. Human Reliability in Quality Control: Papers; Taylor & Francis: London, UK, 1975. 5. Zheng, X.; Zheng, S.; Kong, Y.; Chen, J. Recent advances in surface defect inspection of industrial products using deep learning techniques. Int. J. Adv. Manuf. Technol. 2021, 113, 35–58. [CrossRef] 6. Kalyan, K.S.; Rajasekharan, A.; Sangeetha, S. AMMUS: A Survey of Transformer-based Pretrained Models in Natural Language Processing. arXiv 2021, arXiv:2108.05542.


<!-- Page 15 -->


Appl. Sci. 2022, 12, 11981 15 of 16


7. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. Attention Is All You Need. arXiv 2017, arXiv:1706.03762. 8. Devlin, J.; Chang, M.W.; Lee, K.; Toutanova, K. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv 2018, arXiv:1810.04805. 9. Brown, T.B.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J.; Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell, A.; et al. Language Models are Few-Shot Learners. Adv. Neural Inf. Process. Syst. 2020, 33, 1877–1901. 10. Han, K.; Wang, Y.; Chen, H.; Chen, X.; Guo, J.; Liu, Z.; Tang, Y.; Xiao, A.; Xu, C.; Xu, Y.; et al. A Survey on Vision Transformer. IEEE Trans. Pattern Anal. Mach. Intell. 2022. [CrossRef] 11. Khan, S.; Naseer, M.; Hayat, M.; Zamir, S.W.; Khan, F.S.; Shah, M. Transformers in Vision: A Survey. ACM Comput. Surv. 2022, 2, T2. [CrossRef] 12. Xu, Y.; Wei, H.; Lin, M.; Deng, Y.; Sheng, K.; Zhang, M.; Tang, F.; Dong, W.; Huang, F.; Xu, C. Transformers in computational visual media: A survey. Comput. Vis. Media 2022, 8, 33–62. [CrossRef] 13. Liu, H.; Miao, X.; Mertz, C.; Xu, C.; Kong, H. CrackFormer: Transformer Network for Fine-Grained Crack Detection. In Proceedings of the 2021 IEEE/CVF International Conference on Computer Vision (ICCV), Montreal, QC, Canada, 10–17 October 2021. 14. Wang, T.; Zhang, Z.; Yang, F.; Tsui, K.L. Automatic Rail Component Detection Based on AttnConv-Net. IEEE Sens. J. 2022, 22, 2379–2388. [CrossRef] 15. Radford, A.; Wu, J.; Child, R.; Luan, D.; Amodei, D.; Sutskever, I. Language models are unsupervised multitask learners. OpenAI Blog 2019, 1, 9. 16. Kitaev, N.; Kaiser, Ł.; Levskaya, A. Reformer: The Efﬁcient Transformer. arXiv 2020, arXiv:2001.04451. 17. Wang, S.; Li, B.Z.; Khabsa, M.; Fang, H.; Ma, H. Linformer: Self-Attention with Linear Complexity. arXiv 2020, arXiv:2006.04768. 18. Dosovitskiy, A.; Beyer, L.; Kolesnikov, A.; Weissenborn, D.; Zhai, X.; Unterthiner, T.; Dehghani, M.; Minderer, M.; Heigold, G.; Gelly, S.; et al. An Image is Worth 16 × 16 Words: Transformers for Image Recognition at Scale. arXiv 2020, arXiv:2010.11929. 19. Liu, Z.; Lin, Y.; Cao, Y.; Hu, H.; Wei, Y.; Zhang, Z.; Lin, S.; Guo, B. Swin Transformer: Hierarchical Vision Transformer using Shifted Windows. In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), Montreal, QC, Canada, 10–17 October 2021. 20. Carion, N.; Massa, F.; Synnaeve, G.; Usunier, N.; Kirillov, A.; Zagoruyko, S. End-to-End Object Detection with Transformers. In European Conference on Computer Vision; Springer: Cham, Switzerland, 2020. 21. Dai, X.; Chen, Y.; Xiao, B.; Chen, D.; Liu, M.; Yuan, L.; Zhang, L. Dynamic Head: Unifying Object Detection Heads with Attentions. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Nashville, TN, USA, 19–25 June 2021. 22. Zhu, X.; Su, W.; Lu, L.; Li, B.; Wang, X.; Dai, J. Deformable DETR: Deformable Transformers for End-to-End Object Detection. arXiv 2020, arXiv:2010.04159. 23. Kuhn, H.W. The Hungarian method for the assignment problem. Nav. Res. Logist. Q. 1955, 2, 83–97. [CrossRef] 24. Xu, M.; Zhang, Z.; Hu, H.; Wang, J.; Wang, L.; Wei, F.; Bai, X.; Liu, Z. End-to-End Semi-Supervised Object Detection with Soft Teacher. In Proceedings of the IEEE/CVF International Conference on Computer Vision, Montreal, QC, Canada, 10–17 October 2021. 25. Dai, J.; Qi, H.; Xiong, Y.; Li, Y.; Zhang, G.; Hu, H.; Wei, Y. Deformable Convolutional Networks. arXiv 2017, arXiv:1703.06211. https://doi.org/10.48550/ARXIV.1703.06211. 26. Lin, T.Y.; Maire, M.; Belongie, S.; Bourdev, L.; Girshick, R.; Hays, J.; Perona, P.; Ramanan, D.; Zitnick, C.L.; Dollár, P. Microsoft COCO: Common Objects in Context. arXiv 2014, arXiv:1405.0312. https://doi.org/10.48550/arXiv.1405.0312. 27. Wang, C.Y.; Yeh, I.H.; Liao, H.Y.M. You Only Learn One Representation: Uniﬁed Network for Multiple Tasks. arXiv 2021, arXiv:2105.04206. 28. Krizhevsky, A.; Sutskever, I.; Hinton, G.E. ImageNet classiﬁcation with deep convolutional neural networks. Commun. ACM 2017, 60, 84–90. [CrossRef] 29. Chen, C.; Zou, X.; Zeng, Z.; Cheng, Z.; Zhang, L.; Hoi, S.C.H. Exploring Structural Knowledge for Automated Visual Inspection of Moving Trains. IEEE Trans. Cybern. 2022, 52, 1233–1246. [CrossRef] [PubMed] 30. Ren, S.; He, K.; Girshick, R.; Sun, J. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. Adv. Neural Inf. Process. Syst. 2015, 28, 91–99. [CrossRef] 31. He, K.; Zhang, X.; Ren, S.; Sun, J. Deep Residual Learning for Image Recognition. arXiv 2015, arXiv:1512.03385. 32. Lin, T.Y.; Dollár, P.; Girshick, R.; He, K.; Hariharan, B.; Belongie, S. Feature Pyramid Networks for Object Detection. arXiv 2016, arXiv:1612.03144. 33. Chung, J.; Gulcehre, C.; Cho, K.; Bengio, Y. Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling. arXiv 2014, arXiv:1412.3555. 34. Everingham, M.; van Gool, L.; Williams, C.K.I.; Winn, J.; Zisserman, A. The Pascal Visual Object Classes (VOC) Challenge. Int. J. Comput. Vis. 2010, 88, 303–338. [CrossRef] 35. Opara, J.N.; Thein, A.B.B.; Izumi, S.; Yasuhara, H.; Chun, P.J. Defect Detection on Asphalt Pavement by Deeplearning. Int. J. Geomate 2021, 21, 87–94. [CrossRef] 36. Redmon, J.; Farhadi, A. YOLOv3: An Incremental Improvement. arXiv 2018, arXiv:1804.02767. 37. Badrinarayanan, V.; Kendall, A.; Cipolla, R. SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation. arXiv 2015, arXiv:1511.00561.


<!-- Page 16 -->


Appl. Sci. 2022, 12, 11981 16 of 16


38. Zou, Q.; Cao, Y.; Li, Q.; Mao, Q.; Wang, S. CrackTree: Automatic crack detection from pavement images. Pattern Recognit. Lett. 2012, 33, 227–238. [CrossRef] 39. Zou, Q.; Zhang, Z.; Li, Q.; Qi, X.; Wang, Q.; Wang, S. DeepCrack: Learning Hierarchical Convolutional Features for Crack Detection. IEEE Trans. Image Process. 2018, 28, 1498–1512. [CrossRef] 40. König, J.; Jenkins, M.; Mannion, M.; Barrie, P.; Morison, G. Optimized Deep Encoder-Decoder Methods for Crack Segmentation. Digit. Signal Process. 2021, 108, 102907. [CrossRef] 41. Chen, J.; Liu, Z.; Wang, H.; Nunez, A.; Han, Z. Automatic Defect Detection of Fasteners on the Catenary Support Device Using Deep Convolutional Neural Network. IEEE Trans. Instrum. Meas. 2018, 67, 257–269. [CrossRef] 42. Sun, X.; Gu, J.; Huang, R.; Zou, R.; Giron Palomares, B. Surface Defects Recognition of Wheel Hub Based on Improved Faster R-CNN. Electronics 2019, 8, 481. [CrossRef] 43. Liu, Z.; Lyu, Y.; Wang, L.; Han, Z. Detection Approach Based on an Improved Faster RCNN for Brace Sleeve Screws in High-Speed Railways. IEEE Trans. Instrum. Meas. 2020, 69, 4395–4403. [CrossRef] 44. Xie, S.; Girshick, R.; Dollár, P.; Tu, Z.; He, K. Aggregated Residual Transformations for Deep Neural Networks. arXiv 2016, arXiv:1611.05431. 45. Loshchilov, I.; Hutter, F. Decoupled Weight Decay Regularization. arXiv 2017, arXiv:1711.05101. 46. Dai, Z.; Cai, B.; Lin, Y.; Chen, J. UP-DETR: Unsupervised Pre-training for Object Detection with Transformers. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Nashville, TN, USA, 19–25 June 2021. 47. Liu, Z.; Hu, H.; Lin, Y.; Yao, Z.; Xie, Z.; Wei, Y.; Ning, J.; Cao, Y.; Zhang, Z.; Dong, L.; et al. Swin Transformer V2: Scaling up Capacity and Resolution. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, New Orleans, LA, USA, 19–20 June 2022. 48. Yang, J.; Li, C.; Zhang, P.; Dai, X.; Xiao, B.; Yuan, L.; Gao, J. Focal Self-attention for Local-Global Interactions in Vision Transformers. arXiv 2021, arXiv:2107.00641. 49. Dai, Z.; Liu, H.; Le V, Q.; Tan, M. CoAtNet: Marrying Convolution and Attention for All Data Sizes. Adv. Neural Inf. Process. Syst. 2021, 34, 3965–3977. 50. Lin, T.Y.; Goyal, P.; Girshick, R.; He, K.; Dollár, P. Focal Loss for Dense Object Detection. In Proceedings of the IEEE International Conference on Computer Vision, Venice, Italy, 22–29 October 2017. 51. Chen, K.; Wang, J.; Pang, J.; Cao, Y.; Xiong, Y.; Li, X.; Sun, S.; Feng, W.; Liu, Z.; Xu, J.; et al. MMDetection: Open MMLab Detection Toolbox and Benchmark. arXiv 2019, arXiv:1906.07155. 52. Xie, Z.; Zhang, Z.; Cao, Y.; Lin, Y.; Bao, J.; Yao, Z.; Dai, Q.; Hu, H. SimMIM: A Simple Framework for Masked Image Modeling. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, New Orleans, LA, USA, 19–20 June 2022.
