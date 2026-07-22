# czimmermann2020-visual-defect


<!-- Page 1 -->


sensors


Review Visual-Based Defect Detection and Classiﬁcation Approaches for Industrial Applications—A SURVEY


Tamás Czimmermann * , Gastone Ciuti, Mario Milazzo , Marcello Chiurazzi, Stefano Roccella, Calogero Maria Oddo * and Paolo Dario


The BioRobotics Institute of Scuola Superiore Sant’Anna and Department of Excellence in Robotics and AI of Scuola Superiore Sant’Anna, 56025, Pontedera (PISA), Italy; gastone.ciuti@santannapisa.it (G.C.); m.milazzo@santannapisa.it (M.M.); m.chiurazzi@santannapisa.it (M.C.); stefano.roccella@santannapisa.it (S.R.); paolo.dario@santannapisa.it (P.D.) * Correspondence: t.czimmermann@santannapisa.it (T.C.); calogero.oddo@santannapisa.it (C.M.O.)


 


Received: 9 February 2020; Accepted: 2 March 2020; Published: 6 March 2020


Abstract: This paper reviews automated visual-based defect detection approaches applicable to various materials, such as metals, ceramics and textiles. In the ﬁrst part of the paper, we present a general taxonomy of the different defects that fall in two classes: visible (e.g., scratches, shape error, etc.) and palpable (e.g., crack, bump, etc.) defects. Then, we describe artiﬁcial visual processing techniques that are aimed at understanding of the captured scenery in a mathematical/logical way. We continue with a survey of textural defect detection based on statistical, structural and other approaches. Finally, we report the state of the art for approaching the detection and classiﬁcation of defects through supervised and non-supervised classiﬁers and deep learning.


Keywords: defect detection; classiﬁcation; deep learning; industry 4.0; survey


## 1. Introduction


Defect detection and classiﬁcation are two topics that need to be treated as unique problems related to the ﬁeld of artiﬁcial vision. Digital image processing problems mainly derive from speciﬁc conditions in which researchers aim to mimic or substitute human vision and decision methodologies with artiﬁcial techniques. The general purpose of mimicking human vision is to identify and classify a subject: these two goals are always strictly bonded together. Literature on artiﬁcial visual processing is usually categorized into visual processing algorithms, which consist in the recreations of the human vision, and classiﬁers, which are a remodeling of the human decision techniques. In this paper, we address both categories, but, instead of summarizing all the visual processing methodologies, we focus on the speciﬁc solutions that are strongly related to visual processing methods and, speciﬁcally, on visual inspection techniques for metallic, ceramic or textile surfaces in industrial applications.


Quality control is a crucial aspect in the industrial production line. Several approaches are currently used to assess the quality of a product or the outcome of a process. Depending on the method employed to identify a defect on a surface/volume, quality control strategies can be classiﬁed as destructive or non-destructive, as shown in Figure 1. Non-destructive testings (NDTs) aim at monitoring a component to detect a defect without extracting samples from it, or permanently damaging it. Mostly used in the aeronautic ﬁeld, NDTs are classiﬁed as: visual-based method, dye penetrant inspection, radiography, ultrasonic testing, eddy current approach, and thermography [1].


Sensors 2020, 20, 1459; doi:10.3390/s20051459 www.mdpi.com/journal/sensors


<!-- Page 2 -->


Sensors 2020, 20, 1459 2 of 25


Among them, the visual-based approach for defect detection is one of the most common procedures in industry. However, the traditional visual inspection is a non-measurable process with variable and subjective outcomes. This has pushed researchers to develop new automatic defect detection systems with demanding requirements because of the complexity and uniqueness of any speciﬁc problem to solve. However, such a system depends on the material properties of the surfaces to monitor and on the environmental conditions. In industrial applications, indeed, the environment complicates any implementation, due to dusty or resonating working areas.


The description of a defect and its categorization is a procedure that involves series of subjective decisions. The main attributes of a defect depend on the aimed precision and resolution of the detection procedure, since the size of defects can differ among industrial applications. It is highly advised to establish a quality standard of the product in every industrial quality control application before designing and implementing the automatic system.


This review is organized as follows. in Section 2, we propose a taxonomy of defects that can occur on metal surfaces, which is based on the relevant materials’ properties and objects industrial categorization for quality inspection. In Section 3, we describe the representation and processing of the defects through images. In Section 4, we propose a supplementary list of detection methods for defects and detail them, based on their methodology and efﬁciency. In Section 5, we describe the supervised and unsupervised classiﬁcation methods used for image processing.


Quality control strategies


Destructive


Non-Destructive


Visual-based


approaches


Dye penetrant


inspection


Radiography


Eddy current


approach


Ultrasonic testing


Thermography


…


Figure 1. Categorization of the quality control strategies.


## 2. Taxonomy of Surface Defects


In the industrial production area, quality control aims at maintaining a quality level or at localizing the defects for further repair. Conventional detection methods usually deal with regular, macro-sized and complex variations of surface defects. Almost every artiﬁcial visual defect detection technique aims to detect imperfections and classify them for further processing.


For a proper classiﬁcation, industrial applications need well-structured databases of the possible defect types. However, establishing such a general and comprehensive database for a classiﬁer is challenging, due to the randomness and uniqueness of the defects that can occur in the operation scenarios. In this


<!-- Page 3 -->


Sensors 2020, 20, 1459 3 of 25


regard, although a general categorization approach is highly demanded, almost every application employs a material-based defect classiﬁer. Observing the referred papers in this study and gathering examples from them, we propose a low-level, uniﬁed categorization for defect types, as reported in Figure 2. This taxonomy of surface defects, applicable to any material, is classiﬁed into two major groups: visible and palpable defects. It is worth noting that this categorization is still basic, essentially conceptual and not satisfactory for procedures with speciﬁc requirements, but it provides a strong and reliable basis for a classiﬁcation with artiﬁcial intelligence system. The fundamental assumption of this defect categorization is that the classiﬁcation of a defect is a severely subjective judgement, i.e., it greatly depends on what a defect represents for the human supervisor. This decision is usually based on a threshold and a logical-based representation of the size ratio of both the component and the defect. Therefore, the structure of the taxonomy is mainly organized by size ratios and spatial features.


Figure 2. The category of visible defects contains defects that are hard or almost impossible to be localized by touch. The category of palpable defects contains defects that are signiﬁcantly easier to be localized with the combination of vision and touch. Clearly, the naming of categories does not mean that there are no exceptions in either category.


## 3. Artiﬁcial Visual Processing Techniques


The main goal of visual-based approaches is to understand the world both in its natural and artiﬁcial representations. In the latter, the process to identify images is mostly an attempt to look for a mathematical/logical connection between the input images and representations of the environment. The mathematical/logical connection is a transition from the input image (s) to the model, which reduces the information contained in the image to relevant information for the application domain. Image


<!-- Page 4 -->


Sensors 2020, 20, 1459 4 of 25


representation can be roughly divided into four levels, as described in Figure 3. The hierarchy of image representation and the background functions/algorithms can be further simpliﬁed as low-level and high-level image processing.


Most low-level processing methods do not use any prior knowledge about the content of the image. This means that the methods that belong to this group can be applied to every image without considering any information about the prerecorded environment. This group includes: (1) image compression; (2) pre-processing; (3) sharpening; and (4) edge extraction methods.


The higher-level processing methods are more complex and operate above the mathematical representation of the image (e.g., in the content domain, where unique objects or extra information have been already described) by establishing classiﬁers and where mimicking the human cognition is needed.


## ANALOG


Scene with objects


## RECORD


2D Image


## SAMPLING – INFORMATION LOSS


Scene with objects


## LOW – LEVEL IMAGE PROCESSES


Regions


Edges Textures …


## MID – LEVEL IMAGE PROCESSES


Images with features


## HIGH – LEVEL IMAGE PROCESSES


Detected, unique objects


## DIGITAL


Figure 3. The theoretical levels of image representation for image analysis. The transformation from the analog to the digital domain (with sampling) always results in some information loss.


As depicted in Figure 3, to reach the level of the “images with features”, and to have a picture with content, several attributes of the image—e.g., edges, textures, etc.—have to be described. Two distinct principles apply for naturally occurring visual observations. One is performed according to previous knowledge about the object to be found. The second is performed with no given information about the object, but with knowledge on the environment, considered as normal. Usually, most non-destructive visual inspection methods to ﬁnd surface abnormalities involve textures and/or color analysis, performed by low-level processes. These principles can be replicated in artiﬁcial systems, but employing different approaches. To recognize individual defects on a surface, a descriptor database of the possible defects, such as a classiﬁer, must be established. Although they have to deal with false positive (FP) and false negative (FN) outcomes, classiﬁers, can be used to ensure that the system is able to recognize a defect. Modeling the second principle leads to texture analysis problems, where any deviation from the normal pattern in the texture is recognized and highlighted.


<!-- Page 5 -->


Sensors 2020, 20, 1459 5 of 25


## 4. Textural Defect Detection


Textures provide important and unique information for artiﬁcial visual detection and identiﬁcation systems. The latter use different types of texture analysis and classiﬁcations because the general task of defect detection is mostly a texture analysis problem. The most promising and accurate approach to describe a texture is to extract its unique features, although this turns out to be a challenging task.


Xie et al. [2] categorized the techniques for extracting texture features into four categories with references and their comparison (based on the work of Luo et al. [3]) to distinct papers in this ﬁeld (see Tables 1 and 2), and then Ngan et al. [4] in 2011 made a new extended review.


The statistical and ﬁlter-based approaches have been the most popular approaches used to date. The categorization, provided in [2], is a well-structured analysis and it can be used as a starting point for future summarizations. The four main categories, namely statistical approach, structural approach, ﬁlter-based approach, and model-based approach, could be discussed in the same group, but it is advisable to discuss them separately from the color texture analyzing techniques. The main differences between the two groups are the color related features. Thus, Xie et al. [2] focused only on non-color related methods.


Table 1. Strengths and weaknesses of different image processing techniques.


Approach Method Strengths Weaknesses


Histogram properties Simplicity, invariant to translation and rotation. Requires the assumption that the intensity of defective regions are separable.


Computation and memory requirements are relatively high.


Co-occurrence matrix The spatial relation of extracted image pixels is complete and accurate.


Local binary pattern Gray invariance, can quickly extract discriminative features with rotation. Highly sensitive to noise, scale change.


Statistical


Other gray level statistics Suitable for low resolution images. Low timeliness and no automatic threshold selection.


Auto-correlation Easy to use on textures that are repetitive in nature, such as textiles.


Unsuitable for random textures with irregularly arranged textural elements.


Heavily depends on the keypoint detection algorithms or the similarity measurement strategies.


Registration-based Can mix different sensory images or acquired from different views or at different times.


Primitive measurement Simple, easy to understand and implement. Sensitive to non-linear noises.


Edge features Easy to realize and capable to extract some low-order features of the image.


Susceptible to noise and only suitable for images with low resolution.


Structural


Skeleton representation Built up from multiple statistical histogram analysis as a structure. Mixes their strengths.


Heavily depends on the applied statistical methods’ weaknesses.


Morphological operations Computationally simple and highly suitable for random or natural textures. Only suitable for aperiodic defects.


Computation and memory requirements scale heavily. Translation, expansion and rotation dependent.


Spatial domain ﬁltering Spatial information extraction, possible to use for localization.


Difﬁcult to realize non-interference when dealing with frequency-domain components related to background or defect.


Filter


Frequency domain analysis Invariant to translation, expansion and rotation.


Can outperform space or frequency invariant based methods when the signal and noise overlap in both space and frequency domains.


High complexity. Hard to determine the optimal ﬁlter parameters and no rotation invariance.


Joint spatial/spatial frequency


Fractal model The overall information of images can be expressed by partial features.


Detection accuracy is unsatisfactory and have limitation on images without self-similar.


Can be combined with statistical and spectral methods for segmentation applications to capture the local texture orientation information.


Cannot detect small defects. Not suitable for global texture analysis. Strong spatial constraint.


Random ﬁeld model


Model based


Texem model Potentially useful for image segmentation problems even on colored images.


Requires signiﬁcantly large training dataset to train the model.


Tend to be limited to low-resolution images since memory and computation requirements grow with the size of the image.


Auto-regressive High performance for texture related problems.


<!-- Page 6 -->


Sensors 2020, 20, 1459 6 of 25


Based on several research studies in the ﬁeld of visual inspection (e.g., [5]), it is possible to use the best ﬁtting approach for a speciﬁc problem. It is worth mentioning that providing an exhaustive survey of all texture features is not practical or ie even impossible due to their enormous diversity. All different approaches can be evaluated according to the following features.


Table 2. A selection of most commonly used textural defect detection methods.


Approach Method References


Histogram properties [6–14] Co-occurrence matrix [6,11,15–30] Local binary pattern [12,28,30–38] Other gray level statistics [21,23,39–44] Auto-correlation [23,45,46] Registration-based [47–50]


Statistical


Primitive measurement [51,52] Edge features [53] Skeleton representation [54,55] Morphological operations [51,52,56–60]


Structural


Spatial domain ﬁltering [26,61–70] Frequency domain analysis [22,71–84] Joint spatial/spatial frequency [25,33,39,68,85–116]


Filter based


Fractal model [117–120] Random ﬁeld model [26,121–132] Texem model [133] Auto-regressive [24,37,134–141]


Model based


Color texture analysis for defect detection [36,43,52,69,94,133,142]


## 4.1. Statistical Approaches


Statistical approaches focus on analyzing the spatial distribution of pixel values in a recorded image. In this category, it is possible to count numerous publications and techniques, ranging from low-level to higher-order statistics, such as histogram statistics, autocorrelation, local binary patterns (LBP) and others (see Table 2).


Histogram properties and statistics are useful supports for both higher-level and low-level processes with low computational cost. These processes include operations from statistics, such as sensitivity range, mean, geometric mean, harmonic mean, standard deviation, variance and median. It also includes other histogram comparison statistics used for texture features, such as L1 norm, L2 norm, Mallows or EMD distance, Bhattacharyya distance, Matusita distance, divergence, histogram intersection, Chi-square and the normalized correlation coefﬁcient. Implementations can be found, for instance, in [6,7,143–145], which have proven to be worthy as low-level processes in defect detection. They can be also used as tonality disruptors (e.g., [144,146]) due to their properties of being invariant to translation and rotation, and being insensitive to the exact spatial distribution of color pixels. Yuan et al. [8] proposed an improved Otsu thresholding method, called Weighted Object Variance (WOV), and achieved 94% of detection rate with 8.4% of false alarm rate. In another recent study, the authors also proposed and improved Otsu thresholding method, but without reporting detailed results on the method’s performance [9]. Recently, Dastoorian et al. [10] implemented an Adaptive Generalized Likelihood Ratio (AGLR) approach in a practical case study to inspect 27 samples, each with a unique fault using 3D laser scanning technology. The method detects defects by checking whether the distribution of the observed data is signiﬁcantly different from a baseline historical distribution in an adaptive manner.


<!-- Page 7 -->


Sensors 2020, 20, 1459 7 of 25


• Sensitivity = TP TP+FN • Speci f icity = TN TN+FP • Detection Success Rate = TP+TN TP+FN+TN+FP


where TP, TN, FN and FP stand for true positive, true negative, false negative and false positive, respectively.


Spatial grey level co-occurrence matrices (GLCMs) are one of the most well-known and commonly used texture features [147]. These are statistical methods that measure the spatial relationship of grey-scale pixels into co-occurrence matrices. The GLCM functions characterize the texture of an image by calculating how often pairs of pixels with speciﬁc values and in a speciﬁed spatial relationship occur in an image, given a displacement vector, and then extract texture features such as energy, entropy, contrast, homogeneity and correlation from these matrices. There are several publications describing applications using co-occurrence matrices to detect defects [6,11,15–20]. Despite the high number of applications, the co-occurrence matrix features have several deﬁciencies. Several reports [33] have proved that there is no generally accepted optimization for the displacement vector, and GLCMs have other statistical and computational dependencies. In other comparative studies [16,17], the co-occurrence matrices have shown worse performance in defect detection compared to the Markov Random Fields (MRF), ﬁltering-based, LBP methods. In contrast to other papers, such as [20], the authors showed the opposite result compared to Gabor ﬁlter based approach, with a slightly better performance. Recently, the GLCM method has become a very popular approach: Capizzi et al. [29] proposed an GLCM based detector with a radial basis probabilistic neural network to detect defects on fruits, and achieved 97.25% detection rate with 2.75% false alarm. In [21], the authors used the GLCM and other methods to extract features to train a supervised Support Vector Machine (SVM). In [148,149], the authors achieved 93.4% and 83.3% defect detection rate to replace manual defect inspection, respectively. In [22], the authors used the GLCM for textural feature description and combined it with a Fast Discrete Curvelet Transform (FDCT), achieving 93.3% detection rate with 3.6% false alarm on ferrite magnetic tiles.


The methods using autocorrelation can be applied on textures that contain repetitive patterns, such as textiles. This mathematical algorithm aims at ﬁnding correlation between the texture and its translation with a displacement vector and derives vertexes in case of high regularity. However, this type of method ﬁts for several defect detection problems, due to the high sensitivity to noise interference and the only application capability on patterned textures makes it unsuitable for most of the detection tasks because of their random surface. Zhu et al. [23] published a study about a yarn-dyed fabric defect detector, which combines autocorrelation with the GLCM; however, the system was tested only on 16 samples and no detailed results were reported.


Local binary pattern (LBP) is a computational low cost and very efﬁcient texture operator. It calculates thresholds of the grey-scale pixels and its neighbors in a sliding window, which uses the center pixel of the window as a threshold. It considers the threshold’s result as a binary number. It was ﬁrst published by Ojala et al. [32] as a labeling visual descriptor for textures. The LBP operator is insensitive to changes in illumination and image rotation, and it makes it a robust operator. It has similarities in the logic of computation with co-occurrence matrices, but the LBP seems to achieve lower performance [33]. It has been used in several defect detector applications on varied materials [12,33–35,150] such as ceramics or wood. Recently, Zhang et al. [30] combined the GLCM and LBP methods to extract image features to train a BP Neural Network: it achieved 97.6% detection rate on 90 samples from TILDA database [151]. In [38], Sindagi and Srivastava proposed a modiﬁed LBP method to train a SVM classiﬁer, detecting defects with 93% accuracy on 148,905 samples.


<!-- Page 8 -->


Sensors 2020, 20, 1459 8 of 25


## 4.2. Structural Approaches


Structural Approaches (SA) mostly focus on the spatial location of the texture elements. These elements can be extracted from the texture and described as texture primitives. Applying spatial arrangement rules to texture primitives can result in a dynamic texture model. The texture primitives are mostly simple grey-scale regions, line segments or individual pixels. These elements are always used in a combination with placement rules which are derived from the geometric relationships or spatial statistics of these primitives. After revising several publications about SAs (see Table 2), it is possible to state that this approach performs much better on patterned regular textures.


Several methods for SAs have been developed, such as the one proposed by Chen and Jain [54] that describes a model with a skeleton structure of the texture or the one proposed by Bennamoun and Bodnarova [55] that describes an approach called texture blob detection: both approaches are made for defect detection on fabric images. Wen and Xia [53] examined the surface of leather extracting the edge segments and statistically evaluated them based on their physical attributes. Morphological operators are other SAs, developed by Matheron and Serra [152] in 1964. They give an outstanding opportunity for segmenting defects and general defects detection, as reported in [56]. Recently, Tolba and Raafat [57] proposed a multiscale structural similarity index (MS-SSIM)-based method, which discriminated abnormal features with a 99.1% success rate. Yun, Jong Pil et al. [60] proposed an automatic defect detection optical system based on morphological operations, using backlight technique. Finally, in [58], the authors developed a new method: the prior knowledge guided least squares regression (PG-LSR) and solved the subspace segmentation problem. However, no detailed results of the detection were reported.


## 4.3. Filter-Based Approaches


Images can be described by detected features, such as edges, textures and regions (Figure 3). Filtering these features is one of the earliest attempts in image processing, especially for the extraction of the edge details. It is also a low-level process and the edges can be interpreted as spatial impulsive intensity changes of the image [61]. To extract edges from images, it is possible to use several ﬁlters and algorithms in the spatial domain, such as Sobel, Robert, Canny, Deriche, Laws and Laplacian ﬁlters. Neubauer [62] introduced a method with three 5 × 5 ﬁnite impulse response (FIR) ﬁlters as ﬁrst-order statistics, and performed defect segmentation with TP = 98.3% and TN = 90.6%. Unser and Ade [63,64], and then Monadjemi et al. [33,65], used texture independent ensemble of macro windows called eigenﬁlters as defect detectors. Eigenﬁlters are considered highly sensitive to local distortion and noise; it makes them less suitable for online fabric inspections. However, their low complexity and ability to incorporate various time- and frequency-domain constraints easily compared to other methods, have made eigenﬁlters very commonly used as general approach.


In most cases, operating in the spatial domain involves noise and complications to ﬁnd a direct kernel. Therefore, transforming the images into the frequency domain with Fourier Transformation (FT) gives the leverage to easily ﬁlter the noise and process the image, as described in [71]. The basic logics are to transform the image into Fourier domain, ﬁlter and then re-transform it into the spatial domain. The differences between the original and processed images can be considered as potential defects, based on the applied function in the transformation [72]. Chan and Pang [73] applied a central spatial frequency spectrum, based on the idea that defects usually occur in horizontal and vertical directions. However, these ﬁlters suffer the assumption that textures are periodic. D’Astous and Jernigan [74] used peak and power distribution features to discriminate textures. Optical Fourier transform (OFT) has been used in several applications performed on fabrics, such as in [75] by Hoffer et al.; in [76] by Castellini et al.; in [77] by Ciamberlini et al.; and in [78,79] by Campbell et al. Recently, Shan Gai [80] performed the quaternion


<!-- Page 9 -->


Sensors 2020, 20, 1459 9 of 25


wavelet transform on 10,000 banknote images and achieved 97% defect detection success rate and 0.35% false alarm.


The Fourier transformation depends on the entire image because of its coefﬁcients. This property makes it unable to localize defects in the spatial domain. The most common solution for this problem is to apply a windowed FT for spatial dependency and, if the window function is Gaussian, it results in the well-known Gabor transform. The Gabor transform (GT) attempts the optimal joint localization in spatial and spatial-frequency domains [153]. There are two types of approaches to this method. The ﬁrst is when several ﬁlters have been stored in predetermined frequencies and orientations to cover all possibly occurring frequencies in the image and calculate their correlation [85]. However, this approach can be computationally intensive to achieve high recognition quality. The second approach concerns the implementation of the optimal ﬁlters that correlate with the desired recognition area in parameters, but achieving the optimal settings is hard and crucial [86]. Turner [87] and Clark et al. [88] ﬁrst proposed the use of Gabor ﬁlters (GF) in texture analysis. In the past decades, several applications were published about Gabor ﬁlters [33,68,86,89–94]. Kumar and Pang [91] used only real Gabor functions for fabric defect detection, and then, in [68], they used similar features on plain and twill fabrics in three schemes with no explicit results in the ﬁrst scheme, but with 100% accuracy in the second and third schemes. They also investigated the imaginary part of the Gabor functions as an edge detector. In [86,95], Bodnarova et al. applied a Fisher cost function to select a subset of Gabor functions to perform ﬂaw detection on textiles and achieved 82.86% accuracy with the proposed optimal two-dimensional GF. Escofet et al. [89] performed a multi-scale and multiresolution Gabor ﬁltering in a novelty detection framework. Among the GT methods, Mak and Peng [85] achieved the best detection results on a fair number and quality of samples. They achieved 96.2% success rate with a Gabor wavelet network to extract optimal texture features from a defect-free image and then 97.1% with an only real Gabor ﬁlter for defect detection. Recently, Kang et al. [39] proposed two approaches: an optimized Gabor ﬁlter and a distance-matching-based method called regular band. They achieved a 71.4% detection rate with 0% false alarm with Gabor ﬁltering and a 93.1% detection rate with 4.9% false positives on 85 sample images from TILDA database with regular band. Hu [96] established an elliptical Gabor ﬁlter tuned by a simulated annealing algorithm, but no detailed defect detection results were published.


With similar properties to the Gabor transform, Wavelet Transform (WT) representations have also been used as defect detectors [25,97–106]. WTs are based on small waves of varying frequency and limited duration called wavelets and provide local information from horizontal, vertical and diagonal directions on any input image [107]. Several approaches managed to achieve 98–100% success rate for defect detection with the Fuzzy Wavelet Analysis [108], multiscale wavelet method [109], WT image restoration schemes [72,100] and adaptive level-selecting scheme to analyze co-occurrence matrices [111]. However, the reliability of these methods is questionable due to a limited dataset of samples used during the tests. In [99,112], Sari-Sarraf and Goddard performed discrete WTs and edge fusions to emphasize the defects from the background on fabric images. The procedure achieved an 89% detection success rate over 3700 images of fabrics, containing 26 distinct kinds of defects. Yang et al. [154] developed an adaptive wavelet-based feature extractor with a Euclidean distance-based detector for fabric images, which achieved 97.5% with a defect-database (480 defect-free and 480 defective samples), and 93.3% without a defect-database (780 defect-free and 180 defective samples). Later, in [113], they outperformed ﬁve other WT-based methods with their new Discriminative Feature Extraction (DFE) method, reaching 95.8% classiﬁcation accuracy. In [114], Lin used one-level Harr wavelet transform to detect ripple defects on chips.


Recently, Zhou et al. [70] proposed two new saliency detection method—region growing geodesic saliency (RGGS) and region growing Euclidean saliency (RGES)—and template matching with multiscale


<!-- Page 10 -->


Sensors 2020, 20, 1459 10 of 25


mean ﬁltering. Their template matching method achieved an 88.83% detection rate, while the RGES method performed with an accuracy of 75.95%.


## 4.4. Model-Based Approaches (MBAs)


Model-based methods are classiﬁed into three groups: (1) fractal models; (2) autoregressive models; and (3) random ﬁeld models. Fractals play a signiﬁcant role in the description of the natural surfaces with self-similar and irregular texture. They were ﬁrstly reported by Mandelbrot [117]. In [118,119], Conci and Proenca introduced a differential box-counting method with non-overlapping copies of images and achieved a 96% success rate on 80/75 defect-free/defective samples. Bu et al. [155] performed defect detection based on four fractal features and support vector data description on seven datasets of 14,378 defect free samples and 3222 defect samples with a 98.3% success rate. Kaneko [156] achieved 93.85% accuracy of classiﬁcation on 65 samples of the Brodatz texture database [157]; however, the method is computationally heavier compared to the technique presented in [158]. In a comparative study by Ohanian and Dubes [120], the fractal method performed well against GLCMs, Gabor ﬁlters and MRF-based methods; however, its success heavily depends on the self-similarity of the texture and therefore it provides weaker performance.


Markov random ﬁelds approaches [121] combine both statistical and structural information of context dependent entities, such as pixels depending on their neighbor pixels, and can be used in texture segmentation [122,123] and classiﬁcation problems [124,125]. Cohen et al. [126] used Gaussian MRF (GMRF) to model defect-free texture on fabric images. They treated the method as a hypothesis testing problem on the statistics derived from the GMRF model. Six 256 × 256 testing images with various defects were divided into non-overlapping sub-blocks, where each block was classiﬁed as defective or non-defective. Although the detection success rate was high, the reliability of the testing is questionable due to a limited dataset of samples. Özdemir and Ercil [127] compared their MRF-based method in fabric inspection and a Karhunen–Loeve (KL)-based method; then, in [26], the authors determined the competitiveness of the MRF model against other statistical and spectral based methods. In 2000, Baykut et al. [130] applied the aforementioned GMRF method in real-time application with a dedicated DSP system. In 2005, Chan et al. [128] proposed a wavelet-domain Hidden Markov Tree model with a level set segmentation technique. Recently, in [129], the authors described a defect pavement detection method, and improved a quality of image segmentation by Markov random ﬁelds and Graph cuts method with an unsupervised Random Forest learning methodology for classiﬁcation. Moradi and Zayed [132] developed a real-time application for defect detection in sewer tunnels by using Hidden Markov Model (HMM) and achieved 82.5% detection rate on 40 samples.


The main concept of the autoregressive model (AR) is to characterize texture features based on the linear dependencies of pixels [24]. Seraﬁm [134,135] applied multiresolution pyramids for leather defect segmentation of natural images based on two-dimensional AR models. Basu and Lin [136] used a multi-scale AR texture model on tress for fabric samples, while, in [137], the authors used one-dimensional AR and a CCD camera for a real-time web inspection. From these studies, it is possible to state that lightning is a crucial component of the inspections. Although the testing outcomes were very promising, no quantitative results were published at the end of the tests [156]. Recently, Zhang et al. [138] proposed a defect identiﬁcation model based on machine learning, where they automatically classiﬁed the reported alarms into true defects and false positives. The authors designed a set of novel features at variable level, called variable characteristics, for building the classiﬁcation model and selected 13 base classiﬁers and two ensemble learning methods for model building. They achieved an 83.36% average accuracy of classiﬁcation. In [159], the authors used a quantitative model characterizing the impact of illumination with a simple classiﬁer and achieved a best of 94% accuracy in 1865 samples.


<!-- Page 11 -->


Sensors 2020, 20, 1459 11 of 25


## 4.5. Resource Dependency Comparison


The application in a real industrial case scenario requires fast and reliable detection and classiﬁcation processes. Clearly, reliability is a crucial point since these procedures are stochastic processes with an efﬁciency that can be improved as the computational cost increases, for example changing the sampling resolution of the system that determines the distance between pixels in digital image. Fine textures require smaller distance between pixels, whereas coarse textures require larger distances. This means that a reduction of resolution (by quantizing the image to fewer levels of intensity) helps to increase the speed of computation, as long as some loss of textural information is acceptable. Although this approach leads to a faster detection process, the success rate can be smaller due to the omission of non-sampled critical features of defects.


Generally speaking, with model-based approaches, the computational complexity is strongly affected by the estimation of stochastic model parameters. Methods such as MRFs, for example, need to be trained before their employment as classiﬁers. Computational cost and efﬁciency of a classiﬁer heavily depend on the dimension of the neural network used for the training phase [29,40].


Fractals, instead, are computationally suitable for PC implementation, but have poor accuracy [160]. Statistical approaches using co-occurrence matrices are computationally expensive, thus not suitable for a real-time defect inspection system. However, several studies have widely demonstrated that these are highly accurate techniques [2].


Other statistical approaches, such as LBPs, have a cheap computational cost in real-time applications for texture classiﬁcation but they have lower performance than co-occurrence matrices and other ﬁltering-based approaches for detecting random textural defects [33].


## 5. Supervised and Non-Supervised Classiﬁers


The main goals of the visual processes are the detection and classiﬁcation of defects that can be solved by establishing classiﬁers. In the previous section, we discuss the approaches that are more related to the low-level image processing level, based on Figure 3. This section compares the methods related to the high-level image processing. Their general goal is to discriminate a speciﬁc defect, texture feature, or pattern. Based on their processing mechanics, these classiﬁers can be classiﬁed in two groups: (1) supervised; and (2) non-supervised or semi-supervised classiﬁers (see Table 3).


Table 3. The taxonomy and a supplementary list of references about supervised and unsupervised or semi-supervised classiﬁers used for defect detection.


Approach Method References


K-nearest neighbor [25,73,90,103,161–163] NNs & Deep learning [6,29,40,59,62,65,75,78,85,99,109,164–191] SOM and SVM [12,13,21,30,31,38,142,148,149,171,192–195]


Supervised classiﬁers


Unsupervised/semiStatistical/Novelty detection [58,65,86,89–92,103,115,129,196–202] supervised classiﬁers Gaussian mixture model [80,203–205]


Supervised classiﬁcation methods incorporate the human model—as discussed in Section 3—where the application is searching for features of a predeﬁned class. Detectable features are predeﬁned and the classiﬁer has to be previously trained to recognize them under supervision [40,65,90,103,142,161–163]. As part of the supervised classiﬁers, the K-Nearest Neighbor (KNN) classiﬁer is a non-parametric learning algorithm where the output object, classiﬁed into classes, uses its local neighborhood to formulate a prediction. The KNN algorithm is among the simplest machine learning algorithms, where K is a


<!-- Page 12 -->


Sensors 2020, 20, 1459 12 of 25


user-deﬁned constant that deﬁnes the number of neighbors to employ for classiﬁcation. A high K value reduces the noise of classiﬁcation, but makes the boundaries between classes less distinct, thus the best choice must be tuned upon the dataset. In [162,163], Lopez et al. used KNN to classify ceramic tile images based on chromatic features and achieved high performance using high K-value, while Mandriota et al. [103] applied KNN to inspect rail surfaces but did not ﬁnd signiﬁcant difference in their dataset performance because of the higher K-value. There are also numerous good classiﬁer-based implementations, e.g., Wiltschi et al. [90] and Latif-Amet et al. [25] classiﬁed images based on the parametric distance. Chan and Pang [73] classiﬁed defects by simulating their main features to describe a classiﬁer. Pernkopf [161] used KNN to classify steel surfaces based on dispersions extracted from hidden Markov random ﬁelds.


Artiﬁcial neural networks are commonly used classiﬁers due to them being universal function approximators [206]. They are computing systems inspired by biological neural networks that can learn from data and store the knowledge of the classiﬁcation. The key feature of the neural networks is the iterative learning process in which teaching-samples are presented to the network in batches or minibatches and the weighted connections between neurons are adjusted by the input values associated with the activation function. A Feed-Forward Neural Network (FFNN), described in [40] by Kumar, was applied to classify extracted texture features of textile images and to solve segmentation problem. Monadjemi et al. [65] established a Back Propagation (BP) Neural Network (NN) combined with lower level processes (e.g., co-occurrence matrices, LBP, Gabor ﬁlters, etc.) and outperformed a KNN in ceramic texture features classiﬁcation. Stojanovic et al. [164] used a three-layer BP NN to detect fabric defects with 86.2% success. Within the last decades, BPNNs have been commonly used and successful methods for defect detection: as reported in [165,166], Kuo et al. achieved 91.88% on 160 defective images and 94.38% success rates on 240 defective images. Hung and Cheng [167] used BPNNs with fuzziﬁcation technique but with unclear success rate. In [168], the authors achieved a 91–100% detection rate on 16-16 samples with BPNNs, while Zhang et al. [169] achieved a 83.4% success rate with a FFNN. Besides the previously mentioned methods, there are numerous studies about applied neural networks, such as studies reported in [6,62,75,78,85,99,109,170]. In 2012, Cord and Chambon [59] proposed an automatic defect detection method by textural pattern recognition based on a supervised learning method, called AdaBoost, and achieved a 91% detection rate with 12.5% false alarm on 6875 samples. In [198], Shipway et al. investigated three methods of modifying the ﬂuorescent penetrant inspection Random Forest (RF) method, based on the individual performance of decision trees within the RF. Their main attempt was to improve the effectiveness of RF at performing automated defect detection.


Other commonly used supervised classiﬁers have been developed, such as Self-Organizing Maps (SOM) mainly used for clustering, feature mapping and SVM to classify defects based on features. SVMs can be an appropriate alternative to FFNNs, because they are computationally easier to train and do not have local minimum problems. Therefore, many studies [171,193] have been published about the SVM in defect detection and the authors of [31,194] reported SOM methods. The authors of [12,13,142] performed unsupervised clustering SOM with supervised sample mapping. Supervised classiﬁcation proved its value in the ﬁeld of visual inspection. However, it strongly depends by the number of samples and training conditions. Accordingly, the training phase of the classiﬁer often takes time and needs a large defect sample database—which is not always available—but it achieves higher success rates with a longer training phase. Recently, in [172], Li et al. proposed a discriminative representation for patterned fabric defect detection and achieved a 95.8% detection rate with 2.5% false alarms on 600 samples. They classiﬁed sample images with the Fisher criterion-based stacked denoising autoencoders (FCSDA) and introduced deep learning for the ﬁrst time in the defect detection ﬁeld. Tural et al. [192] recently developed a system using various image processing and ﬁltering method (Bilateral ﬁltering, Sobel ﬁltering, thresholding, and


<!-- Page 13 -->


Sensors 2020, 20, 1459 13 of 25


morphological closing) in a combination with SVM to detect and classify defects on bullet shells. They achieved 96% accuracy in a real-time production environment.


The main feature for non-supervised classiﬁers is the capability of detecting every feature that is not part of the texture and pattern. They represent the other approach of the human detection model, in which the detector is trained with normal samples and every deviation is considered as abnormal. This approach is particularly useful when the spatial distribution of the abnormalities is needed. These methods usually exploit distance-based or thresholding rules to discriminate questionable features. Markou and Singh [196,197] published studies on the novelty for detection approaches using statistical and neural-network-based techniques. During visual inspections, statistical parametric approaches are often used [65,86,89–92,103]. The essential hypothesis is the Gaussian natural distribution of the data. Gururajan et al. [203] proposed a Gaussian mixture model with Expectation-Maximization features to detect one speciﬁc kind of defect, and achieved 93% true positive and 95% true negative detection success rates for six types of soils under four categories of laundering treatments. Zhang et al. [204] combined Gabor transformation with a Gaussian mixture model for plain fabric defect detection, with 87% classiﬁcation success rate achieved. In [133], the authors proposed two different mixture models to measure pattern likelihoods by using simple parametric thresholding, automatically determined from training data with a 92.67% overall accuracy. Recently, Zhu et al. [115] applied Gabor ﬁlter as a pre-process method to reduce the complexity of the fabric signal, and built the over-complete basis set via sparse coding. They achieved a 93.7% defect detection success rate with 9.6% false alarms on 284 samples. Susan and Sharma [207] proposed a new unsupervised automated texture defect detection method that uses a Gaussian mixture entropy model to determine the optimal window size for feature extraction. Recently, Mei et al. [205] developed an unsupervised learning based method by using only defect free samples for model training. The approach was carried out by reconstructing image patches with convolutional denoising autoencoder networks at different Gaussian pyramid levels, and synthesizing detection results from these different resolution channels.


Deep Learning for Defect Detection


Deep learning is one of fastest growing ﬁelds in computer sciences, due to its ability to solve highly complex problems [208]. The rich accumulation of traditional machine learning techniques resulted in the evolution of deep learning that also gained its inspiration from statistical learning. Most of the approaches mentioned in the previous sections are considered as traditional solutions, where the focus is on the explicitly engineered features which can be challenging to describe in complex cases. However, deep learning uses data representation learning to perform tasks, that transform data into complex, abstract representations that enable the features to be learnen for systems (e.g., feature learning). This ability of deep learning overcomes the requirement of complex features for a speciﬁc defect. Both deep learning and traditional machine learning are data-driven artiﬁcial intelligence techniques able to successfully model deterministic rules, which are often incomprehensible to humans and relationships between input and output. Moreover, deep learning disposes the capability of performing feature learning, model construction and model training, by selecting different kernels or tuning and optimizing parameters.


In 2018, Wang et al. [209] summarized the capabilities of deep learning for smart manufacturing and highlighted how deep learning changes future trends in industry. Within the past years, a number of relevant studies have been published on defect detection solutions using deep learning [175,210–214]. Lin, Hui et al. [214] developed a CNN called LEDNet to detect and classify defect on LED chips, where they achieved relatively low inaccuracy of 5.05%. Sun et al. [180] compared back-propagation neural networks and learning vector quantization performance in detecting the four commonly seen bur defect on thermal fuses. In 2015, Ren et al. [215] introduced a method by combining the region proposal network (RPN) and


<!-- Page 14 -->


Sensors 2020, 20, 1459 14 of 25


Faster Region-based Convolutional Neural Network (Faster R-CNN) for object detection to generate nearly cost-free region proposals. In [216], the authors used a Faster R-CNN-based visual inspection method to detect and classify ﬁve defect types with 90.6%, 83.4%, 82.1%, 98.1%, and 84.7% average precisions. Notably, their method performed the task signiﬁcantly more quickly than a traditional CNN based method, which is necessary for real-time implementation. Wang et al., [173] developed a faster R-CNN algorithm to solve the speed problem of CNNs and to locate small defects in geometrically complex products where they achieved 72% detection and 81% classiﬁcation accuracy. Liu et al. [174] introduced a defect detection method based on semantic segmentation. For this, they used a development and extension of CNN called Fully Connected Networks (FCN) where they transformed the fully connected layer of a CNN into a convolution layer. They achieved 99.6% accuracy on the German DAGM 2007 dataset. Recently, Kumar et al. [178] used a deep convolutional neural network (DCNN) to detect and classify defect in sewers and achieved and average of 86.2% testing accuracy, 87.7% precision and 90.6% recall. Later, Brackenbury et al. [179] compared three different classiﬁcation strategies for DCNNs to detect structural faults in masonry arch bridges. Their study shows the the importance of the right structure and method choice based on the dataset.


Li et al. [176] combined Gabor ﬁlters and Pulse Coupled Neural Network (PCNN) for fabric defect detection and achieved 98.6% accuracy. The PCNN model was developed by Johnson et al. [217]. It was inspired by the study in [218] by Echorn about the synchronous dynamics of neuronal activity in cat visual cortex. Chen et al. [177] stated that, recently, PCNN models are the most potential method in image processing due to its high potential by resolving the problem of parameter estimation of segmentation problems.


In 2018, Sacco et al. [181] developed a CNN based system for automatic quality control for ﬁber placement manufacturing, however they failed to achieve satisfactory results due to their small (only 200 samples/defect) training dataset that led them to over-ﬁt their network. This factor is one of the most crucial factor by employing CNNs. To solve this common problem, Yang et al. [219] developed a promising and robust method as virtual defect rendering, that can solve the problem of small datasets. In a recent study [182], Yang et al. developed a DCNN based system to detect and classify defects that can occur during laser welding in battery manufacturing. Besides that, they proposed a novel model called Visual Geometry Group (VGG) model to improve the efﬁciency of defect classiﬁcation. Their test on 8000 samples with a 99.87% accuracy proved that the pre-trained VGG model has small model size, lower fault positive rate and shorter training time and prediction time. It is notable that their model is highly suitable for quality inspection in an industrial environment. Following the evolution of the industrial quality control ﬁeld, there is an unequivocal need for general solutions to solve complex challenges that can be served by deep learning.


## 6. Conclusions and Future Directions


This paper provides a review of defect detection methodologies described in more than 220 scientiﬁc contributions. A signiﬁcant amount of works is based on statistical observations and uses statistical or ﬁlter-based methods. The Gabor ﬁlter is one of the most commonly used methods. However, most of the studies present speciﬁc limitations, being heavily dependent on the pattern, material and texture. Solving the segmentation and windowing problems of overlapping objects is still a ponderous topic approached by several researchers. Images having color features can multiply the complexity of these problems.


Neural networks are a powerful technique often employed in artiﬁcial image processing since they can nearly solve every classiﬁcation problem. However, the main drawback is the required large amount of training samples. In artiﬁcial image processing, this issue can be easily solved with labeled datasets, or applying stochastic solutions (i.e., mini-batches). However, in other ﬁelds such as robotics, or other


<!-- Page 15 -->


Sensors 2020, 20, 1459 15 of 25


systems that learn from real-world operations, it is still a challenging problem. Improving the training efﬁciency and convergence capability of neural networks is an ongoing research area. It is also notable that large neural networks used for deep learning require signiﬁcant computational resources, which lead to an unavoidable parallelization of the challenges [220].


Supervised learning methods are well-functioning and straightforward to use. Due to their capabilities, supervised methods are the most preferred for classiﬁcation in industry but in many cases they are time consuming to train and require large datasets.


Unsupervised learning is used for density estimation, dimensionality reduction and clustering problems. However, in many cases, unsupervised methods have shown lower efﬁciencies than supervised learning methods. Natural supervision is an emerging topic in the ﬁeld, due to its similarities to biological learning behaviors. From another perspective, artiﬁcial neural networks are inspired by biological neural networks, but do not necessarily replicate them. Back propagation is the essence to train many artiﬁcial neural networks, although no such mechanism exactly exists in biological networks [221]. This means that biological neural networks gave a good inspiration to develop artiﬁcial neural networks that can be used as classiﬁers; however, sufﬁciently modeling them for technological use is still an unsolved topic.


In artiﬁcial image processing, different textural databases are available for testing, although several studies do not provide satisfactory results due to the lack of testing samples and frequent inconsistency of such databases. Moreover, there is still a huge demand for developing general defect detection methods able to deal with any kind of defect on every kind of material, and also able to establish a general and reliable defect description system. Due to the lack of solutions, there is a huge demand in industry to increase the defect identiﬁcation efﬁciency with multi-sensory systems applications. To this aim, deep learning is the emerging ﬁeld that could solve the generalization requirement and hyper-complexity of problems without drastically increasing computational costs.


Funding: This work was supported by the Tuscany Region by means of the CENTAURO project (CUP D88C15000210008) funded under the FAR-FAS call for proposals.


Acknowledgments: The authors would like to thank the partners of the CENTAURO project, namely Piaggio & Co. SpA, Robot System Automation srl, Roggi srl and Robotech srl.


Conﬂicts of Interest: The authors declare no conﬂict of interest.


## References


1. Bircham, D. Non-destructive testing: Curtis, G. Acoustic emission energy relates to bond strength8 (1975) (5) (October) 249–257. Non-Destr. Test. 1975, 8, 308. [CrossRef] 2. Xie, X. A review of recent advances in surface defect detection using texture analysis techniques. Electron. Lett. Comput. Vis. Image Anal. 2008, 7, 1–22. [CrossRef] 3. Luo, Q.; Fang, X.; Liu, L.; Yang, C.; Sun, Y. Automated Visual Defect Detection for Flat Steel Surface: A Survey. IEEE Trans. Instrum. Meas. 2020. [CrossRef] 4. Ngan, H.Y.; Pang, G.K.; Yung, N.H. Automated fabric defect detection–a review. Image Vis. Comput. 2011, 29, 442–458. [CrossRef] 5. Kumar, A. Computer-vision-based fabric defect detection: A survey. IEEE Trans. Ind. Electron. 2008, 55, 348–363. [CrossRef] 6. Tsai, I.S.; Lin, C.H.; Lin, J.J. Applying an artiﬁcial neural network to pattern recognition in fabric defects. Text. Res. J. 1995, 65, 123–130. [CrossRef] 7. Ng, H.F. Automatic thresholding for defect detection. Pattern Recognit. Lett. 2006, 27, 1644–1649. [CrossRef] 8. Yuan, X.C.; Wu, L.S.; Peng, Q. An improved Otsu method using the weighted object variance for defect detection. Appl. Surf. Sci. 2015, 349, 472–484. [CrossRef]


<!-- Page 16 -->


Sensors 2020, 20, 1459 16 of 25


9. Aminzadeh, M.; Kurfess, T. Automatic thresholding for defect detection by background histogram mode extents. J. Manuf. Syst. 2015, 37, 83–92. [CrossRef] 10. Dastoorian, R.; Elhabashy, A.E.; Tian, W.; Wells, L.J.; Camelio, J.A. Automated Surface Inspection Using 3D Point Cloud Data in Manufacturing: A Case Study. In Proceedings of the ASME 2018 13th International Manufacturing Science and Engineering Conference, Los Angeles, CA, USA, 18–22 June 2018. 11. Asha, V.; Bhajantri, N.U.; Nagabhushan, P. GLCM-based chi-square histogram distance for automatic detection of defects on patterned textures. arXiv 2012, arXiv:1212.0383. 12. Niskanen, M.; Silvén, O.; Kauppinen, H. Color and texture based wood inspection with non-supervised clustering. In Proceedings of the Scandinavian Conference on Image Analysis, Bergen, Noreg, 11–14 June 2001; pp. 336–342. 13. Kauppinen, H.; Rautio, H.; Silven, O. Nonsegmenting defect detection and SOM-based classiﬁcation for surface inspection using color vision. In Polarization and Color Techniques in Industrial Inspection; Marszalec, E.A., Trucco, E., Eds.; International Society for Optics and Photonics; (SPIE): Bellingham, WA, USA, 1999; Volume 3826, pp. 270–280. doi:10.1117/12.364334. [CrossRef] 14. Kim, C.W.; Koivo, A.J. Hierarchical classiﬁcation of surface defects on dusty wood boards. Pattern Recognit. Lett. 1994, 15, 713–721. [CrossRef] 15. Conners, R.W.; Mcmillin, C.W.; Lin, K.; Vasquez-Espinosa, R.E. Identifying and locating surface defects in wood: Part of an automated lumber processing system. IEEE Trans. Pattern Anal. Mach. Intell. 1983, 6, 573–583. [CrossRef] [PubMed] 16. Siew, L.H.; Hodgson, R.M.; Wood, E.J. Texture measures for carpet wear assessment. IEEE Trans. Pattern Anal. Mach. Intell. 1988, 10, 92–105. [CrossRef] 17. Iivarinen, J.; Rauhamaa, J.; Visa, A. Unsupervised segmentation of surface defects. In Proceedings of the 13th International Conference on Pattern Recognition, Vienna, Austria, 25–29 August 1996; pp. 356–360. 18. Bodnarova, A.; Williams, J.A.; Bennamoun, M.; Kubik, K.K. Optimal textural features for ﬂaw detection in textile materials. In Proceedings of the IEEE TENCON’97, IEEE Region 10 Annual Conference, Speech and Image Technologies for Computing and Telecommunications (Cat. No. 97CH36162), Brisbane, Australia, 4 December 1997; pp. 307–310. 19. Raheja, J.L.; Ajay, B.; Chaudhary, A. Real time fabric defect detection system on an embedded DSP platform. Optik 2013, 124, 5280–5284. [CrossRef] 20. Raheja, J.L.; Kumar, S.; Chaudhary, A. Fabric defect detection based on GLCM and Gabor ﬁlter: A comparison. Optik 2013, 124, 6469–6474. [CrossRef] 21. Samy, M.P.; Foong, S.; Soh, G.S.; Yeo, K.S. Automatic optical & laser-based defect detection and classiﬁcation in brick masonry walls. In Proceedings of the 2016 IEEE Region 10 Conference (TENCON), Marina Bay Sands, Singapore, 22–25 November 2016; pp. 3521–3524. 22. Li, X.; Jiang, H.; Yin, G. Detection of surface crack defects on ferrite magnetic tile. NDT E Int. 2014, 62, 6–13. [CrossRef] 23. Zhu, D.; Pan, R.; Gao, W.; Zhang, J. Yarn-dyed fabric defect detection based on autocorrelation function and GLCM. Autex Res. J. 2015, 15, 226–232. [CrossRef] 24. Haralick, R.M. Statistical and structural approaches to texture. Proc. IEEE 1979, 67, 786–804. [CrossRef] 25. Latif-Amet, A.; Ertüzün, A.; Erçil, A. An efﬁcient method for texture defect detection: Sub-band domain co-occurrence matrices. Image Vis. Comput. 2000, 18, 543–553. [CrossRef] 26. Ozdemir, S.; Baykut, A.; Meylani, R.; Ercil, A.; Ertuzun, A. Comparative evaluation of texture analysis algorithms for defect inspection of textile products. In Proceedings of the Fourteenth International Conference on Pattern Recognition (Cat. No.98EX170), Brisbane, Australia, 20–20 August 1998; pp. 1738–1740. 27. Shiranita, K.; Miyajima, T.; Takiyama, R. Determination of meat quality by texture analysis. Pattern Recognit. Lett. 1998, 19, 1319–1324. [CrossRef] 28. Iivarinen, J. Surface defect detection with histogram-based texture features. In Proceedings of the Intelligent Robots and Computer Vision XIX: Algorithms, Techniques, and Active Vision, International Society for Optics and Photonics, Boston, MA, USA, 11 October 2000; Volume 4197, pp. 140–145.


<!-- Page 17 -->


Sensors 2020, 20, 1459 17 of 25


29. Capizzi, G.; Sciuto, G.L.; Napoli, C.; Tramontana, E.; Wo´zniak, M. Automatic classiﬁcation of fruit defects based on co-occurrence matrix and neural networks. In Proceedings of the 2015 Federated Conference on Computer Science and Information Systems (FedCSIS), Lodz, Poland, 13–16 September 2015; pp. 861–867. 30. Zhang, L.; Jing, J.; Zhang, H. Fabric defect classiﬁcation based on LBP and GLCM. J. Fiber Bioeng. Inf. 2015, 8, 81–89. [CrossRef] 31. Mäenpää, T.; Turtinen, M.; Pietikäinen, M. Real-time surface inspection by texture. Real-Time Imaging 2003, 9, 289–296. doi:10.1016/S1077-2014(03)00041-X. [CrossRef] 32. Ojala, T.; Pietikäinen, M.; Harwood, D. A comparative study of texture measures with classiﬁcation based on featured distributions. Pattern Recognit. 1996, 29, 51–59. [CrossRef] 33. Monadjemi, A. Non-Destructive Testing. Insight –Non-Destr. Test. Cond. Monit. 2004, 46, 573–579. doi:10.1784/insi.46.9.573.40849. [CrossRef] 34. Niskanen, M.; Kauppinen, H.; Silvén, O. Real-time aspects of SOM-based visual surface inspection. In Proceedings of the International Society for Optics and Photonics Machine Vision Applications in Industrial Inspection X, San Jose, CA, USA, 8 March 2002; Volume 4664, pp. 123–134. 35. Mäenpää, T.; Pietikäinen, M. Texture analysis with local binary patterns. In Handbook of Pattern Recognition and Computer Vision; World Scientiﬁc: Singapore, 2005; pp. 197–216. 36. Mäenpää, T.; Viertola, J.; Pietikäinen, M. Optimising colour and texture features for real-time visual inspection. Pattern Anal. Appl. 2003, 6, 169–175. [CrossRef] 37. Wang, J.; Li, Q.; Gan, J.; Yu, H.; Yang, X. Surface Defect Detection via Entity Sparsity Pursuit with Intrinsic Priors. IEEE Trans. Ind. Inf. 2019, 16, 141–150. [CrossRef] 38. Sindagi, V.A.; Srivastava, S. Oled panel defect detection using local inlier-outlier ratios and modiﬁed LBP. In Proceedings of the 2015 14th IAPR International Conference on Machine Vision Applications (MVA), Tokyo, Japan, 18–22 May 2015; pp. 214–217. 39. Kang, X.; Yang, P.; Jing, J. Defect detection on printed fabrics via gabor ﬁlter and regular band. J. Fiber Bioeng. Inf. 2015, 8, 195–206. [CrossRef] 40. Kumar, A. Neural network based detection of local textile defects. Pattern Recognit. 2003, 36, 1645–1659. doi:10.1016/S0031-3203(03)00005-0. [CrossRef] 41. Chetverikov, D. Structural defects: General approach and application to textile inspection. In Proceedings of the 15th International Conference on Pattern Recognition, Barcelona, Spain, 3–7 September 2000; pp. 521–524. 42. Schael, M. Texture defect detection using invariant textural features. In Joint Pattern Recognition Symposium; Springer: Berlin, Germany, 2001; pp. 17–24. 43. Tsai, D.M.; Tsai, Y.H. Defect detection in textured surfaces using color ring-projection correlation. Mach. Vis. Appl. 2003, 13, 194–200. [CrossRef] 44. Cho, C.S.; Chung, B.M.; Park, M.J. Development of real-time vision-based fabric inspection system. IEEE Trans. Ind. Electron. 2005, 52, 1073–1079. [CrossRef] 45. Wood, E.J. Applying Fourier and associated transforms to pattern characterization in textiles. Text. Res. J. 1990, 60, 212–220. [CrossRef] 46. Huang, Y.; Chan, K.L. Texture decomposition by harmonics extraction from higher order statistics. IEEE Trans. Image Process. 2004, 13, 1–14. [CrossRef] [PubMed] 47. Lopez, F.; Acebron, F.; Valiente, J.; Perez, E. A study of registration methods for ceramic tile inspection purposes. In Proceedings of the IX Spanish Symposium on Pattern Recognition and Image Analysis, Benicasim, Spain, 16–18 May 2001; pp. 145–150. 48. Shippen, J.; Westra, R.; Freear, N. Printing quality control using template independent neurofuzzy defect classiﬁcation. In EUFIT’99 (Abstract Booklet with CD Rom); ELITE Foundation (ELITE Foundation (European Laboratory for Intelligent Techniques Engineering): Aachen, Germany, 1999. 49. Costa, C.E.; Petrou, M. Automatic registration of ceramic tiles for the purpose of fault detection. Mach. Vis. Appl. 2000, 11, 225–230. [CrossRef] 50. Xie, P.; Guan, S.U. A golden-template self-generating method for patterned wafer inspection. Mach. Vis. Appl. 2000, 12, 149–156. [CrossRef]


<!-- Page 18 -->


Sensors 2020, 20, 1459 18 of 25


51. Kittler, J.; Marik, R.; Mirmehdi, M.; Petrou, M.; Song, J. Detection of Defects in Colour Texture Surfaces. In Proceedings of the IAPR Workshop on Machine Vision Applications (MVA), Kawasaki, Japan, 13–15 December 1994; pp. 558–567. 52. Song, K.Y.; Kittler, J.; Petrou, M. Defect detection in random colour textures. Image Vis. Comput. 1996, 14, 667–683. [CrossRef] 53. Wen, W.; Xia, A. Verifying edges for visual inspection purposes. Pattern Recognit. Lett. 1999, 20, 315–328. [CrossRef] 54. Chen, J.; Jain, A.K. A structural approach to identify defects in textured images. In Proceedings of the 1988 IEEE International Conference on Systems, Man, and Cybernetics, Beijing, China, 8–12 August 1988; pp. 29–32. 55. Bennamoun, M.; Bodnarova, A. Automatic visual inspection and ﬂaw detection in textile materials: Past, present and future. In Proceedings of the 1998 IEEE International Conference on Systems, Man, and Cybernetics (Cat. No. 98CH36218), San Diego, CA, USA, 14 October 1998; pp. 4340–4343. 56. Mallik-Goswami, B.; Datta, A.K. Detecting defects in fabric with laser-based morphological image processing. Text. Res. J. 2000, 70, 758–762. [CrossRef] 57. Tolba, A.; Raafat, H.M. Multiscale image quality measures for defect detection in thin ﬁlms. Int. J. Adv. Manuf. Technol. 2015, 79, 113–122. [CrossRef] 58. Cao, J.; Zhang, J.; Wen, Z.; Wang, N.; Liu, X. Fabric defect inspection using prior knowledge guided least squares regression. Multimed. Tools Appl. 2017, 76, 4141–4157. [CrossRef] 59. Cord, A.; Chambon, S. Automatic Road Defect Detection by Textural Pattern Recognition Based on AdaBoost. Comput.-Aided Civ. Infrastruct. Eng. 2012, 27, 244–259, doi:10.1111/j.1467-8667.2011.00736.x. [CrossRef] 60. Yun, J.P.; Lee, S.J.; Koo, G.; Shin, C.; Park, C. Automatic defect inspection system for steel products with exhaustive dynamic encoding algorithm for searches. Opt. Eng. 2019, 58, 023107. 61. Marr, D.; Hildreth, E. Theory of edge detection. Philos. Trans. R. Soc. Lond. Ser. B 1980, 207, 187–217. 62. Neubauer, C. Segmentation of defects in textile fabric. In Proceedings of the 11th IAPR International Conference on Pattern Recognition, The Hague, The Netherlands, 30 August–3 September 1992; pp. 688–691. 63. Unser, M.; Ade, F. Feature extraction and decision procedure for automated inspection of textured materials. Pattern Recognit. Lett. 1984, 2, 185–191. [CrossRef] 64. Ade, F. Application of principal component analysis to the inspection of industrial goods. In Proceedings of the Applications of Digital Image Processing V. International Society for Optics and Photonics, Geneva, Switzerland, 26 October 1983; Volume 397, pp. 216–223. 65. Monadjemi, A.; Mirmehdi, M.; Thomas, B. Restructured eigenﬁlter matching for novelty detection in random textures. Learning 2004, 5, 13. 66. Ade, F.; Lins, N.; Unser, M. Comparison of various ﬁlter sets for defect detection in textiles. In Proceedings of the International Conference on Pattern Recognition, Montreal, QC, Canada, 30 July–2 August 1984; Volume 1, pp. 428–431. 67. Zhou, H.; Kassim, A.A.; Ranganath, S. A fast algorithm for detecting die extrusion defects in IC packages. Mach. Vis. Appl. 1998, 11, 37–41. [CrossRef] 68. Kumar, A.; Pang, G.K. Defect detection in textured materials using Gabor ﬁlters. IEEE Trans. Ind. Appl. 2002, 38, 425–440. [CrossRef] 69. Habib, H.A.; Yousaf, M.H.; Mohibullah, M. Modiﬁed laws energy descriptor for inspection of ceramic tiles. In Proceedings of the National Conference on Emerging Technologies, Kyoto, Japan, 7–8 October 2004; Volume 34, pp. 138–140. 70. Zhou, X.; Wang, Y.; Xiao, C.; Zhu, Q.; Lu, X.; Zhang, H.; Ge, J.; Zhao, H. Automated visual inspection of glass bottle bottom with saliency detection and template matching. IEEE Trans. Instrum. Meas. 2019, 68, 4253–4267. [CrossRef] 71. Tsai, D.M.; Hsieh, C.Y. Automated surface inspection for directional textures. Image Vis. Comput. 1999, 18, 49–62. [CrossRef] 72. Tsai, D.M.; Huang, T.Y. Automated surface inspection for statistical textures. Image Vis. Comput. 2003, 21, 307–323. [CrossRef]


<!-- Page 19 -->


Sensors 2020, 20, 1459 19 of 25


73. Chan, C.H.; Pang, G.K. Fabric defect detection by Fourier analysis. IEEE Trans. Ind. Appl. 2000, 36, 1267–1276. [CrossRef] 74. d’Astous, F.; Jernigan, M. Texture discrimination based on detailed measures of the power spectrum. In Proceedings of the International Conference on Pattern Recognition, Montreal, QC, Canada, 30 July–2 August 1984; Volume 3, pp. 83–86. 75. Hoffer, L.M.; Francini, F.; Tiribilli, B.; Longobardi, G. Neural networks for the optical recognition of defects in cloth. Opt. Eng. 1996, 35, 3183–3190. doi:10.1117/1.601057. [CrossRef] 76. Castellini, C.; Francini, F.; Longobardi, G.; Tiribilli, B.; Sansoni, P. On-line textile quality control using optical Fourier transforms. Opt. Lasers Eng. 1996, 24, 19–32. doi:10.1016/0143-8166(95)00044-O. [CrossRef] 77. Ciamberlini, C.; Francini, F.; Longobardi, G.; Poggi, P.; Sansoni, P.; Tiribilli, B. Weaving defect detection by Fourier imaging. In Vision Systems: Applications; Kammenos, P.A., Nickolay, B., Eds.; International Society for Optics and Photonics (SPIE): Bellingham, WA, USA, 1996; Volume 2786, pp. 9–18. doi:10.1117/12.248573. [CrossRef] 78. Campbell, J.G.; Hashim, A.A.; McGinnity, T.M.; Lunney, T.F. Flaw detection in woven textiles by neural network. In Proceedings of the 5th Irish Neural Networks Conference, Maynooth, Ireland, 11–13 September 1995; pp. 92–99. 79. Campbell, J.; Hashim, A.; Murtagh, F. Flaw Detection in Woven Textiles Using Space-Dependent Fourier Transform; University of Ulster: Princeton, NJ, USA, 1997. 80. Gai, S. New banknote defect detection algorithm using quaternion wavelet transform. Neurocomputing 2016, 196, 133–139. [CrossRef] 81. Hosseini Ravandi, S.A.; Toriumi, K. Fourier transform analysis of plain weave fabric appearance. Text. Res. J. 1995, 65, 676–683. [CrossRef] 82. Xu, B. Identifying fabric structures with fast Fourier transform techniques. Text. Res. J. 1996, 66, 496–506. 83. Chen, P.W.; Liang, T.C.; Yau, H.F.; Sun, W.L.; Wang, N.C.; lin, H.C.; Lien, R.C. Classifying textile faults with a back-propagation neural network using power spectra. Text. Res. J. 1998, 68, 121–126. [CrossRef] 84. Escofet, J.; Garcia-Verela, M.S.M.; Abril, H.C.; Torrecilla, E. Inspection of fabric resistance to abrasion by Fourier analysis. In Proceedings of the Optics in Computing’98. International Society for Optics and Photonics, Bruges, Belgium, 22 May 1998; Volume 3490, pp. 207–210. 85. Mak, K.L.; Peng, P. An automated inspection system for textile fabrics based on Gabor ﬁlters. Rob. Comput. Integr. Manuf. 2008, 24, 359–369. [CrossRef] 86. Bodnarova, A.; Bennamoun, M.; Latham, S. Optimal Gabor ﬁlters for textile ﬂaw detection. Pattern Recognit. 2002, 35, 2973–2991. [CrossRef] 87. Turner, M.R. Texture discrimination by Gabor functions. Biol. Cybern. 1986, 55, 71–82. 88. Clark, M.; Bovik, A.C.; Geisler, W.S. Texture segmentation using Gabor modulation/demodulation. Pattern Recognit. Lett. 1987, 6, 261–267. [CrossRef] 89. Escofet, J.; Navarro, R.B.; Millan, M.S.; Pladellorens, J.M. Detection of local defects in textile webs using Gabor ﬁlters. Opt. Eng. 1998, 37. 90. Wiltschi, K.; Pinz, A.; Lindeberg, T. An automatic assessment scheme for steel quality inspection. Mach. Vis. Appl. 2000, 12, 113–128. [CrossRef] 91. Kumar, A.; Pang, G.K. Fabric defect segmentation using multichannel blob detectors. Opt. Eng. 2000, 39, 3176–3191. 92. Tsa, D.M.; Wu, S.K. Automated surface inspection using Gabor ﬁlters. Int. J. Adv. Manuf. Technol. 2000, 16, 474–482. [CrossRef] 93. Bennamoun, M.; Bodnarova, A. Digital image processing techniques for automatic textile quality control. Syst. Anal. Model. Simul. 2003, 43, 1581–1614. [CrossRef] 94. Tsai, D.M.; Lin, C.P.; Huang, K.T. Defect detection in coloured texture surfaces using Gabor ﬁlters. Imaging Sci. J. 2005, 53, 27–37. [CrossRef] 95. Bodnarova, A.; Bennamoun, M.; Latham, S.J. A constrained minimisation approach to optimise Gabor ﬁlters for detecting ﬂaws in woven textiles. In Proceedings of the 2000 IEEE International Conference on Acoustics, Speech, and Signal Processing, Istanbul, Turkey, 5–9 June 2000; pp. 3606–3609.


<!-- Page 20 -->


Sensors 2020, 20, 1459 20 of 25


96. Hu, G.H. Optimal ring Gabor ﬁlter design for texture defect detection using a simulated annealing algorithm. In Proceedings of the 2014 International Conference on Information Science, Electronics and Electrical Engineering, Sapporo, Japan, 26–28 April 2014; pp. 860–864. 97. Jasper, W.J.; Garnier, S.J.; Potlapalli, H. Texture characterization and defect detection using adaptive wavelets. Opt. Eng. 1996, 35. [CrossRef] 98. Kim, S.; Lee, M.H.; Woo, K.B. Wavelet analysis to fabric defects detection in weaving processes. In Proceedings of the IEEE International Symposium on Industrial Electronics (Cat. No. 99TH8465), Bled, Slovenia, 12–16 July 1999; pp. 1406–1409. 99. Sari-Sarraf, H.; Goddard, J.S. Vision system for on-loom fabric inspection. In Proceedings of the 1998 IEEE Annual Textile, Fiber and Film Industry Technical Conference (Cat. No. 98CH36246), Charlotte, NC, USA, 5–7 May 1998; pp. 8–1. 100. Tsai, D.M.; Hsiao, B. Automatic surface inspection using wavelet reconstruction. Pattern Recognit. 2001, 34, 1285–1305. [CrossRef] 101. Ralló, M.; Millán, M.; Escofet, J.; Navarro, R. Wavelet based techniques for textile inspection. Opt. Eng 2003, 26, 838–844. 102. Yang, X.; Pang, G.; Yung, N. Fabric defect classiﬁcation using wavelet frames and minimum classiﬁcation error training. In Proceedings of the Conference Record of the 2002 IEEE Industry Applications Conference (Cat. No. 02CH37344), Pittsburgh, PA, USA, 13–18 October 2002; pp. 290–296. 103. Mandriota, C.; Nitti, M.; Ancona, N.; Stella, E.; Distante, A. Filter-based feature selection for rail defect detection. Mach. Vis. Appl. 2004, 15, 179–185. [CrossRef] 104. Scharcanski, J. Stochastic texture analysis for monitoring stochastic processes in industry. Pattern Recognit. Lett. 2005, 26, 1701–1709. [CrossRef] 105. Yang, X.; Pang, G.; Yung, N. Robust fabric defect detection and classiﬁcation using multiple adaptive wavelets. IEE Proc.-Vis. Image Signal Process. 2005, 152, 715–723. [CrossRef] 106. Liu, J.J.; MacGregor, J.F. Estimation and monitoring of product aesthetics: Application to manufacturing of “engineered stone” countertops. Mach. Vis. Appl. 2006, 16, 374. [CrossRef] 107. Mallat, S.G. A theory for multiresolution signal decomposition: The wavelet representation. IEEE Trans. Pattern Anal. Mach. Intell. 1989, 11, 674–693. [CrossRef] 108. Mufti, M.; Vachtsevanos, G. Automated fault detection and identiﬁcation using a fuzzy-wavelet analysis technique. In Proceedings of the Conference Record AUTOTESTCON’95.’Systems Readiness: Test Technology for the 21st Century’, Atlanta, GA, USA, 8–10 August 1995; pp. 169–175. 109. Lambert, G.; Bock, F. Wavelet methods for texture defect detection. In Proceedings of the International Conference on Image Processing, Santa Barbara, CA, USA, 26–29 October 1997; pp. 201–204. 110. Tsai, D.M.; Chiang, C.H. Automatic band selection for wavelet reconstruction in the application of defect detection. Image Vis. Comput. 2003, 21, 413–431. [CrossRef] 111. Han, Y.; Shi, P. An adaptive level-selecting wavelet transform for texture defect detection. Image Vis. Comput. 2007, 25, 1239–1248. [CrossRef] 112. Sari-Sarraf, H.; Goddard, J. Robust defect segmentation in woven fabrics. In Proceedingsof the 1998 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (Cat. No. 98CB36231), Santa Barbara, CA, USA, 25 June 1998; pp. 938–944. 113. Yang, X.; Pang, G.; Yung, N. Discriminative training approaches to fabric defect classiﬁcation based on wavelet transform. Pattern Recognit. 2004, 37, 889–899. [CrossRef] 114. Lin, H.D. Automated visual inspection of ripple defects using wavelet characteristic based multivariate statistical approach. Image Vis. Comput. 2007, 25, 1785–1801. [CrossRef] 115. Zhu, Q.; Wu, M.; Li, J.; Deng, D. Fabric defect detection via small scale over-complete basis set. Text. Res. J. 2014, 84, 1634–1649. [CrossRef] 116. Campbell, J.G.; Murtagh, F.D. Automatic visual inspection of woven textiles using a two-stage defect detector. Opt. Eng. 1998, 37. [CrossRef] 117. Mandelbrot, B.B. The Fractal Geometry of Nature; WH Freeman: New York, NY, USA, 1983; Volume 173.


<!-- Page 21 -->


Sensors 2020, 20, 1459 21 of 25


118. Conci, A.; Proença, C.B. A fractal image analysis system for fabric inspection based on a box-counting method. Comput. Netw. ISDN Syst. 1998, 30, 1887–1895. doi:10.1016/S0169-7552(98)00211-6. [CrossRef] 119. Conci, A.; Proença, C.B. A System for Real-Time Fabric Inspection and Industrial Decision. In Proceedings of the 14th International Conference on Software Engineering and Knowledge Engineering, Ischia, Italy, 15–19 July 2002; pp. 707–714. 120. Ohanian, P.P.; Dubes, R.C. Performance evaluation for four classes of textural features. Pattern Recognit. 1992, 25, 819–833. doi:10.1016/0031-3203(92)90036-I. [CrossRef] 121. Kindermann, R. Markov random ﬁelds and their applications. Am. Math. Soc. 1980, 97, 3923–3931. 122. Wilson, R.; Chang-Tsun Li. A class of discrete multiresolution random ﬁelds and its application to image segmentation. IEEE Trans. Pattern Anal. Mach. Intell. 2003, 25, 42–56. doi:10.1109/TPAMI.2003.1159945. [CrossRef] 123. Marroquin, J.L.; Santana, E.A.; Botello, S. Hidden Markov measure ﬁeld models for image segmentation. IEEE Trans. Pattern Anal. Mach. Intell. 2003, 25, 1380–1387. [CrossRef] 124. Huawu Deng.; Clausi, D.A. Gaussian MRF rotation-invariant features for image classiﬁcation. IEEE Trans. Pattern Anal. Mach. Intell. 2004, 26, 951–955. doi:10.1109/TPAMI.2004.30. [CrossRef] 125. Wang, L.; Liu, J. Texture classiﬁcation using multiresolution Markov random ﬁeld models. Pattern Recognit. Lett. 1999, 20, 171–182. doi:10.1016/S0167-8655(98)00129-9. [CrossRef] 126. Cohen, F.S.; Fan, Z.; Attali, S. Automated inspection of textile fabrics using textural models. IEEE Trans. Pattern Anal. Mach. Intell. 1991, 8, 803–808. [CrossRef] 127. Ozdemir, S.; Ercil, A. Markov random ﬁelds and Karhunen-Loeve transforms for defect inspection of textile products. In Proceedings of the 1996 IEEE Conference on Emerging Technologies and Factory Automation, Kauai, HI, USA,18–21 November 1996; pp. 697–703. doi:10.1109/ETFA.1996.573989. [CrossRef] 128. Chan, H.Y.; Raju, C.; Sari-Sarraf, H.; Hequet, E.F. A general approach to defect detection in textured materials using a wavelet domain model and level sets. In Wavelet Applications in Industrial Processing III; Truchetet, F., Laligant, O., Eds.; International Society for Optics and Photonics; Society of Photographic Instrumentation Engineers (SPIE): Bellingham, WA, USA, 2005; Volume 6001, pp. 102–107. doi:10.1117/12.633204. [CrossRef] 129. Nguyen, H.; Nguyen, L.; Sidorov, D.N. A robust approach for road pavement defects detection and classiﬁcation. J. Comput. Eng. Math. 2016, 3, 40–52. [CrossRef] 130. Baykut, A.; Atalay, A.; Erçil, A.; Güler, M. Real-time defect inspection of textured surfaces. Real-Time Imaging 2000, 6, 17–27. [CrossRef] 131. Pernkopf, F. 3D surface inspection using coupled HMMs. In Proceedings of the 17th International Conference on Pattern Recognition, Cambridge, UK, 26 August 2004; pp. 223–226. 132. Moradi, S.; Zayed, T. Real-time defect detection in sewer closed circuit television inspection videos. Pipelines 2017, 295–307. 133. Xie, X.; Mirmehdi, M. TEXEMS: Texture Exemplars for Defect Detection on Random Textured Surfaces. IEEE Trans. Pattern Anal. Mach. Intell. 2007, 29, 1454–1464. doi:10.1109/TPAMI.2007.1038. [CrossRef] 134. Limas Seraﬁm, A.F. Multiresolution pyramids for segmentation of natural images based on autoregressive models: Application to calf leather classiﬁcation. In Proceedings of the 1991 International Conference on Industrial Electronics, Control and Instrumentation, Kobe, Japan, 28 October–1 November 1991; pp. 1842–1847. doi:10.1109/IECON.1991.239061. [CrossRef] 135. Limas Seraﬁm, A.F. Segmentation of natural images based on multiresolution pyramids linking of the parameters of an autoregressive rotation invariant model. Application to leather defects detection. In Proceedingsof the 11th IAPR International Conference on Pattern Recognition, The Hague, The Netherlands, 30 August–3 September 1992; pp. 41–44. doi:10.1109/ICPR.1992.201923. [CrossRef] 136. Basu, M.; Lin, Z. Multi-scale modeling of textures. In Proceedings of the 11th IAPR International Conference on Pattern Recognition, The Hague, The Netherlands, 30 August–3 September 1992; pp. 421–424. doi:10.1109/ICPR.1992.202013. [CrossRef] 137. Hajimowlana, S.H.; Muscedere, R.; Jullien, G.A.; Roberts, J.W. 1D autoregressive modeling for defect detection in web inspection systems. In Proceedings of the 1998 Midwest Symposium on Circuits and Systems (Cat.


<!-- Page 22 -->


Sensors 2020, 20, 1459 22 of 25


No. 98CB36268), Notre Dame, IN, USA, 9–12 August 1998; pp. 318–321. doi:10.1109/MWSCAS.1998.759496. [CrossRef] 138. Zhang, Y.; Xing, Y.; Gong, Y.; Jin, D.; Li, H.; Liu, F. A variable-level automated defect identiﬁcation model based on machine learning. Soft Comput. 2020, 24, 1045–1061. [CrossRef] 139. Wang, H.; Zhang, J.; Tian, Y.; Chen, H.; Sun, H.; Liu, K. A Simple Guidance Template-Based Defect Detection Method for Strip Steel Surfaces. IEEE Trans. Ind. Inf. 2018, 15, 2798–2809. [CrossRef] 140. Zhou, S.; Wu, S.; Liu, H.; Lu, Y.; Hu, N. Double low-rank and sparse decomposition for surface defect segmentation of steel sheet. Appl. Sci. 2018, 8, 1628. [CrossRef] 141. Yang, J.; Li, X.; Xu, J.; Cao, Y.; Zhang, Y.; Wang, L.; Jiang, S. Development of an optical defect inspection algorithm based on an active contour model for large steel roller surfaces. Appl. Opt. 2018, 57, 2490–2498. [CrossRef] 142. Silvén, O.; Niskanen, M.; Kauppinen, H. Wood inspection with non-supervised clustering. Mach. Vis. Appl. 2003, 13, 275–285. [CrossRef] 143. Swain, M.J.; Ballard, D.H. Color indexing. Int. J. Comput. Vis. 1991, 7, 11–32. [CrossRef] 144. Thai, B.; Healey, G. Modeling and classifying symmetries using a multiscale opponent color representation. IEEE Trans. Pattern Anal. Mach. Intell. 1998, 20, 1224–1235. [CrossRef] 145. Pietikäinen, M.; Mäenpää, T.; Viertola, J. Color texture classiﬁcation with color histograms and local binary patterns. In Proceedings of the Workshop on Texture Analysis in Machine Vision, Florence, Italy, 7–13 October 2002. 146. Xie, X.; Mirmehdi, M.; Thomas, B. Colour tonality inspection using eigenspace features. Mach. Vis. Appl. 2006, 16, 364–373. [CrossRef] 147. Haralick, R.M.; Shanmugam, K.; Dinstein, I.H. Textural features for image classiﬁcation. IEEE Trans. Syst. Man Cybern. 1973, 6, 610–621. [CrossRef] 148. Çelik, H.; Dülger, L.; Topalbekiro˘glu, M. Development of a machine vision system: Real-time fabric defect detection and classiﬁcation with neural networks. J. Text Inst. 2014, 105, 575–585. [CrossRef] 149. Yang, S.W.; Lin, C.S.; Lin, S.K.; Chiang, H.T. Automatic defect recognition of TFT array process using gray level co-occurrence matrix. Optik 2014, 125, 2671–2676. [CrossRef] 150. Ojala, T.; Pietikäinen, M.; Mäenpää, T. Multiresolution gray-scale and rotation invariant texture classiﬁcation with local binary patterns. IEEE Trans. Pattern Anal. Mach. Intell. 2002, 24, 971–987. [CrossRef] 151. Germany, D. Tilda Textile Texture Database. 1996. Available online: https://lmb.informatik.uni-freiburg.de/ resources/datasets/tilda.en.html (accessed on 9 February 2020). 152. Matheron, G.; Serra, J. The birth of mathematical morphology. In Proceedings of the 6th International Symp. Mathematical Morphology, Sydney, Australia, 3–5 April 2002; pp. 1–16. 153. Daugman, J.G. Two-dimensional spectral analysis of cortical receptive ﬁeld proﬁles. Vis. Res. 1980, 20, 847–856. [CrossRef] 154. Yang, X.; Pang, G.; Yung, N. Discriminative fabric defect detection using adaptive wavelets. Opt. Eng. 2002, 41, 3116–3125. [CrossRef] 155. gang Bu, H.; Wang, J.; bao Huang, X. Fabric defect detection based on multiple fractal features and support vector data description. Eng. Appl. Artif. Intell. 2009, 22, 224–235. doi:10.1016/j.engappai.2008.05.006. [CrossRef] 156. Kaneko, H. A generalized fractal dimension and its application to texture analysis-fractal matrix model. In Proceedings of the International Conference on Acoustics, Speech, and Signal Processing, Glasgow, UK, 23–26 May 1989; pp. 1711–1714. 157. Trygve, R. Brodatz Texture Database. 2010. Available online: http://www.ux.uis.no/~tranden/brodatz.html (accessed on 9 February 2020). 158. Kasparis, T.; Tzannes, N.; Bassiouni, M.; Chen, Q. Texture description using fractal and energy features. Comput. Electr. Eng. 1995, 21, 21–32. doi:10.1016/0045-7906(94)00012-6. [CrossRef] 159. Xi, J.; Shentu, L.; Hu, J.; Li, M. Automated surface inspection for steel products using computer vision approach. Appl. Opt. 2017, 56, 184–192. [CrossRef] 160. Chaudhuri, B.B.; Sarkar, N. Texture segmentation using fractal dimension. IEEE Trans. Pattern Anal. Mach. Intell. 1995, 17, 72–77. doi:10.1109/34.368149. [CrossRef]


<!-- Page 23 -->


Sensors 2020, 20, 1459 23 of 25


161. Pernkopf, F. Detection of surface defects on raw steel blocks using Bayesian network classiﬁers. Pattern Anal. Appl. 2004, 7, 333–342. doi:10.1007/BF02683998. [CrossRef] 162. López, F.; Valiente, J.M.; Baldrich, R.; Vanrell, M. Fast Surface Grading Using Color Statistics in the CIE Lab Space. In Pattern Recognition and Image Analysis; Marques, J.S., Pérez de la Blanca, N., Pina, P., Eds.; Springer: Berlin/Heidelberg, Germany, 2005; pp. 666–673. 163. López, F.; Valiente, J.M.; Prats, J.M. Surface Grading Using Soft Colour-Texture Descriptors. In Progress in Pattern Recognition, Image Analysis and Applications; Sanfeliu, A., Cortés, M.L., Eds.; Springer: Berlin/Heidelberg, Germany, 2005; pp. 13–23. 164. Stojanovic, R.; Mitropulos, P.; Koulamas, C.; Karayiannis, Y.; Koubias, S.; Papadopoulos, G. Real-Time Vision-Based System for Textile Fabric Inspection. Real-Time Imaging 2001, 7, 507–518. doi:10.1006/rtim.2001.0231. [CrossRef] 165. Kuo, C.F.J.; Lee, C.J.; Tsai, C.C. Using a neural network to identify fabric defects in dynamic cloth inspection. Text. Res. J. 2003, 73, 238–244. [CrossRef] 166. Kuo, C.F.J.; Lee, C.J. A back-propagation neural network for recognizing fabric defects. Text. Res. J. 2003, 73, 147–151. [CrossRef] 167. Huang, C.C.; Chen, I.C. Neural-fuzzy classiﬁcation for fabric defects. Text. Res. J. 2001, 71, 220–224. [CrossRef] 168. Yin, Y.; Zhang, K.; Lu, W. Textile ﬂaw classiﬁcation by wavelet reconstruction and BP neural network. In International Symposium on Neural Networks; Springer: Berlin/Heidelberg, Germany, 2009; pp. 694–701. 169. Zhang, Y.; Lu, Z.; Li, J. Fabric defect classiﬁcation using radial basis function network. Pattern Recognit. Lett. 2010, 31, 2033–2042. doi:10.1016/j.patrec.2010.05.030. [CrossRef] 170. Karayiannis, Y.A.; Stojanovic, R.; Mitropoulos, P.; Koulamas, C.; Stouraitis, T.; Koubias, S.; Papadopoulos, G. Defect detection and classiﬁcation on web textile fabric using multiresolution decomposition and neural networks. In Proceedings of the ICECS ’99, 6th IEEE International Conference on Electronics, Circuits and Systems (Cat. No.99EX357), Pafos, Cyprus, 5–8 September 1999; pp. 765–768. doi:10.1109/ICECS.1999.813221. [CrossRef] 171. Kumar, A.; Shen, H.C. Texture inspection for defects using neural networks and support vector machines. In Proceedings of the International Conference on Image Processing, Rochester, NY, USA, 22–25 September 2002. doi:10.1109/ICIP.2002.1038978. [CrossRef] 172. Li, Y.; Zhao, W.; Pan, J. Deformable Patterned Fabric Defect Detection With Fisher Criterion-Based Deep Learning. IEEE Trans. Autom. Sci. Eng. 2017, 14, 1256–1264. doi:10.1109/TASE.2016.2520955. [CrossRef] 173. Wang, Y.; Liu, M.; Zheng, P.; Yang, H.; Zou, J. A smart surface inspection system using faster R-CNN in cloud-edge computing environment. Adv. Eng. Inf. 2020, 43, 101037. [CrossRef] 174. Liu, Y.T.; Yang, Y.N.; Chao, W.; Xu, X.Y.; Zhang, T. Research on Surface Defect Detection Based on Semantic Segmentation. DEStech Trans. Comput. Sci. Eng. 2019. [CrossRef] 175. Weimer, D.; Scholz-Reiter, B.; Shpitalni, M. Design of deep convolutional neural network architectures for automated feature extraction in industrial inspection. CIRP Ann. 2016, 65, 417–420. [CrossRef] 176. Li, Y.; Zhang, C. Automated vision system for fabric defect inspection using Gabor ﬁlters and PCNN. SpringerPlus 2016, 5, 1–12. [CrossRef] [PubMed] 177. Chen, Y.; Park, S.K.; Ma, Y.; Ala, R. A new automatic parameter setting method of a simpliﬁed PCNN for image segmentation. IEEE Trans. Neural Netw. 2011, 22, 880–892. [CrossRef] [PubMed] 178. Kumar, S.S.; Abraham, D.M.; Jahanshahi, M.R.; Iseley, T.; Starr, J. Automated defect classiﬁcation in sewer closed circuit television inspections using deep convolutional neural networks. Autom. Constr. 2018, 91, 273–283. [CrossRef] 179. Brackenbury, D.; Brilakis, I.; DeJong, M. Automated Defect Detection For Masonry Arch Bridges. In International Conference on Smart Infrastructure and Construction 2019 (ICSIC) Driving Data-Informed Decision-Making; ICE Publishing: London, UK, 2019, pp. 3–9. 180. Sun, T.H.; Tien, F.C.; Tien, F.C.; Kuo, R.J. Automated thermal fuse inspection using machine vision and artiﬁcial neural networks. J. Intell. Manuf. 2016, 27, 639–651. [CrossRef]


<!-- Page 24 -->


Sensors 2020, 20, 1459 24 of 25


181. Sacco, C.; Radwan, A.B.; Harik, R.; Van Tooren, M. Automated Fiber Placement Defects: Automated Inspection and Characterization. In Proceedings of the SAMPE 2018 Conference and Exhibition, Long Beach, CA, USA, 21–24 May 2018. 182. Yang, Y.; Pan, L.; Ma, J.; Yang, R.; Zhu, Y.; Yang, Y.; Zhang, L. A High-Performance Deep Learning Algorithm for the Automated Optical Inspection of Laser Welding. Appl. Sci. 2020, 10, 933. [CrossRef] 183. Liu, Y.; Geng, J.; Su, Z.; Zhang, W.; Li, J. Real-time classiﬁcation of steel strip surface defects based on deep CNNs. In Proceedings of 2018 Chinese Intelligent Systems Conference; Springer: Singapore, 2019, pp. 257–266. 184. Li, J.; Su, Z.; Geng, J.; Yin, Y. Real-time detection of steel strip surface defects based on improved yolo detection network. IFAC-PapersOnLine 2018, 51, 76–81. [CrossRef] 185. Song, L.; Lin, W.; Yang, Y.G.; Zhu, X.; Guo, Q.; Xi, J. Weak micro-scratch detection based on deep convolutional neural network. IEEE Access 2019, 7, 27547–27554. [CrossRef] 186. Liu, Y.; Xu, K.; Xu, J. Periodic Surface Defect Detection in Steel Plates Based on Deep Learning. Appl. Sci. 2019, 9, 3127. [CrossRef] 187. He, D.; Xu, K.; Zhou, P. Defect detection of hot rolled steels with a new object detection framework called classiﬁcation priority network. Comput. Ind. Eng. 2019, 128, 290–297. [CrossRef] 188. Cha, Y.J.; Choi, W.; Büyüköztürk, O. Deep learning-based crack damage detection using convolutional neural networks. Comput.-Aided Civ. Infrastruct. Eng. 2017, 32, 361–378. [CrossRef] 189. Ren, R.; Hung, T.; Tan, K.C. A generic deep-learning-based approach for automated surface inspection. IEEE Trans. Cybern. 2017, 48, 929–940. [CrossRef] [PubMed] 190. Tao, X.; Zhang, D.; Ma, W.; Liu, X.; Xu, D. Automatic metallic surface defect detection and recognition with convolutional neural networks. Appl. Sci. 2018, 8, 1575. [CrossRef] 191. Liong, S.T.; Gan, Y.; Huang, Y.C.; Yuan, C.A.; Chang, H.C. Automatic defect segmentation on leather with deep learning. arXiv 2019, arXiv:1903.12139. 192. Tural, S.; Samet, R. Automated Defect Detection on Surface of Militarz Cartridges. J. Mod. Technol. Eng. 2019, 4, 178–189. 193. Occhipinti, L.; Spoto, G.; Branciforte, M.; Doddo, F. Defects detection and characterization by using cellular neural networks. In Proceedings of the 2001 IEEE International Symposium on Circuits and Systems (Cat. No.01CH37196), Sydney, Australia, 6–9 May 2001; pp. 481–484. doi:10.1109/ISCAS.2001.921352. [CrossRef] 194. Jain, A.K.; Duin, R.P.W.; Mao, J. Statistical pattern recognition: A review. IEEE Trans. Pattern Anal. Mach. Intell. 2000, 22, 4–37. doi:10.1109/34.824819. [CrossRef] 195. Pereira, R.F.; Medeiros, C.M.; Rebouças Filho, P.P. Goat leather quality classiﬁcation using computer vision and machine learning. In Proceedings of the 2018 International Joint Conference on Neural Networks (IJCNN), Rio de Janeiro, Brazil, 8–13 July 2018; pp. 1–8. 196. Markou, M.; Singh, S. Novelty detection: A review—part 1: Statistical approaches. Signal Process. 2003, 83, 2481–2497. doi:10.1016/j.sigpro.2003.07.018. [CrossRef] 197. Markou, M.; Singh, S. Novelty detection: A review—part 2: Neural network based approaches. Signal Process. 2003, 83, 2499–2521. [CrossRef] 198. Shipway, N.; Huthwaite, P.; Lowe, M.; Barden, T. Performance based modiﬁcations of random forest to perform automated defect detection for ﬂuorescent penetrant inspection. J. Nondestr. Eval. 2019, 38, 37. [CrossRef] 199. Schlegl, T.; Seeböck, P.; Waldstein, S.M.; Schmidt-Erfurth, U.; Langs, G. Unsupervised anomaly detection with generative adversarial networks to guide marker discovery. In International Conference on Information Processing in Medical Imaging; Springer: Berlin, Germany, 2017; pp. 146–157. 200. Youkachen, S.; Ruchanurucks, M.; Phatrapomnant, T.; Kaneko, H. Defect segmentation of hot-rolled steel strip surface by using convolutional auto-encoder and conventional image processing. In Proceedings of the 2019 10th International Conference of Information and Communication Technology for Embedded Systems (IC-ICTES), Bangkok, Thailand, 25–27 March 2019; pp. 1–5. 201. Zhao, Z.; Li, B.; Dong, R.; Zhao, P. A Surface Defect Detection Method Based on Positive Samples. In Paciﬁc Rim International Conference on Artiﬁcial Intelligence; Springer: Berlin, Germany, 2018, pp. 473–481.


<!-- Page 25 -->


Sensors 2020, 20, 1459 25 of 25


202. Di, H.; Ke, X.; Peng, Z.; Dongdong, Z. Surface defect classiﬁcation of steels with a new semi-supervised learning method. Opt. Lasers Eng. 2019, 117, 40–48. [CrossRef] 203. Gururajan, A.; Hequet, E.F.; Sari-Sarraf, H. Objective evaluation of soil release in fabrics. Text. Res. J. 2008, 78, 782–795. [CrossRef] 204. Zhang, Y.; Lu, Z.; Li, J. Fabric defect detection and classiﬁcation using gabor ﬁlters and gaussian mixture model. In Asian Conference on Computer Vision; Springer: Berlin, Germany, 2009; pp. 635–644. 205. Mei, S.; Yang, H.; Yin, Z. An unsupervised-learning-based approach for automated defect inspection on textured surfaces. IEEE Trans. Instrum. Meas. 2018, 67, 1266–1277. [CrossRef] 206. Hornik, K.; Stinchcombe, M.; White, H. Multilayer feedforward networks are universal approximators. Neural Netw. 1989, 2, 359–366. doi:10.1016/0893-6080(89)90020-8. [CrossRef] 207. Susan, S.; Sharma, M. Automatic texture defect detection using Gaussian mixture entropy modeling. Neurocomputing 2017, 239, 232–237. [CrossRef] 208. Zhao, Z.Q.; Zheng, P.; Xu, S.T.; Wu, X. Object detection with deep learning: A review. IEEE Trans. Neural Netw. Learn. Syst. 2019, 30, 3212–3232. [CrossRef] [PubMed] 209. Wang, J.; Ma, Y.; Zhang, L.; Gao, R.X.; Wu, D. Deep learning for smart manufacturing: Methods and applications. J. Manuf. Syst. 2018, 48, 144–156. [CrossRef] 210. Psuj, G. Multi-sensor data integration using deep learning for characterization of defects in steel elements. Sensors 2018, 18, 292. [CrossRef] [PubMed] 211. Soukup, D.; Huber-Mörk, R. Convolutional neural networks for steel surface defect detection from photometric stereo images. In International Symposium on Visual Computing; Springer: Berlin, Germany, 2014; pp. 668–677. 212. Tabernik, D.; Šela, S.; Skvarˇc, J.; Skoˇcaj, D. Segmentation-based deep-learning approach for surface-defect detection. J. Intell. Manuf. 2020, 31, 759–776. [CrossRef] 213. Gopalakrishnan, K.; Khaitan, S.K.; Choudhary, A.; Agrawal, A. Deep Convolutional Neural Networks with transfer learning for computer vision-based data-driven pavement distress detection. Constr. Build. Mater. 2017, 157, 322–330. [CrossRef] 214. Lin, H.; Li, B.; Wang, X.; Shu, Y.; Niu, S. Automated defect inspection of LED chip using deep convolutional neural network. J. Intell. Manuf. 2019, 30, 2525–2534. [CrossRef] 215. Ren, S.; He, K.; Girshick, R.; Sun, J. Faster r-cnn: Towards real-time object detection with region proposal networks. IEEE Trans. Pattern Anal. Mach. Intell. 2017, 39, 1137–1149. [CrossRef] 216. Cha, Y.J.; Choi, W.; Suh, G.; Mahmoudkhani, S.; Büyüköztürk, O. Autonomous structural visual inspection using region-based deep learning for detecting multiple damage types. Comput.-Aided Civ. Infrastruct. Eng. 2018, 33, 731–747. [CrossRef] 217. Johnson, J.L.; Padgett, M.L. PCNN models and applications. IEEE Trans. Neural Netw. 1999, 10, 480–498. [CrossRef] [PubMed] 218. Eckhorn, R.; Reitboeck, H.J.; Arndt, M.; Dicke, P. Feature linking via synchronization among distributed assemblies: Simulations of results from cat visual cortex. Neural Comput. 1990, 2, 293–307. [CrossRef] 219. Yang, H.; Haist, T.; Gronle, M.; Osten, W. Realistic simulation of camera images of micro-scale defects for automated defect inspection. In Forum Bildverarbeitung 2016; KIT Scientiﬁc Publishing: Karlsruhe, Germany, 2016; Volume 84, p. 63. 220. Edwards, C. Growing pains for deep learning. Commun. ACM 2015, 58, 14–16. [CrossRef] 221. Crick, F. The recent excitement about neural networks. Nature 1989, 337, 129–132. [CrossRef]


c⃝2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).
