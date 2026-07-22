# kryl2020-wood-recognition-inspection


<!-- Page 1 -->


Hindawi Journal of Sensors Volume 2020, Article ID 3217126, 19 pages https://doi.org/10.1155/2020/3217126


Review Article Wood Recognition and Quality Imaging Inspection Systems


Martin Kryl, Lukas Danys, Rene Jaros , Radek Martinek, Pavel Kodytek, and Petr Bilik


Department of Cybernetics and Biomedical Engineering, Faculty of Electrical Engineering and Computer Science, VSBTechnical University of Ostrava, 17. Listopadu 15, 708 33 Ostrava, Czech Republic


Correspondence should be addressed to Rene Jaros; rene.jaros@vsb.cz


Received 27 January 2020; Revised 24 August 2020; Accepted 29 August 2020; Published 17 September 2020


Academic Editor: Giuseppe Quero


Copyright © 2020 Martin Kryl et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


Forestry is an undoubtedly crucial part of today’s industry; thus, automation of certain visual tasks could lead to a signiﬁcant increase in productivity and reduction of labor costs. Eye fatigue or lack of attention during manual visual inspections can lead to falsely categorized wood, thus leading to major loss of earnings. These mistakes could be eliminated using automated vision inspection systems. This article focuses on the comparison of researched methodologies related to wood type classiﬁcation and wood defect detection/identiﬁcation; hence, readers with an intention of building a similar vision-based system have summarized review to build upon.


## 1. Introduction


Wood recognition is crucial technology in various areas of modern industry, for example, covering the construction industry or various manufacturing processes. There are basically two main ways on how to identify timber—either a trained professional inspects each individual log or the whole batch is processed by computer vision. Both ways work very similarly. Various species of wood exhibit certain characteristics or features, which must be recognized to successfully sort each sample [1]. Diﬀerent features can also signiﬁcantly inﬂuence wood quality, thus inﬂuencing quality of the ﬁnal product [2]. Wood material inspection is necessary, as timber of a lower level of quality can only be used for certain purposes.


In constructions, the choice of the right wood type/ quality is crucial, as it inﬂuences material used for a roof truss. Lower quality of chosen wood might lead to instability of the whole roof, which could end in disaster [3]. Similarly, various wood products, such as furniture, require certain quality of used wood material. The right wood type can also inﬂuence quality of manufactured paper [4].


Other than that, certain species of wood are endangered, and their export is banned. However, a signiﬁcant number of these endangered trees are mixed in piles of ordinary wood (criminality further explained below) [5].


As mentioned before, trained human professionals are often used for wood classiﬁcation. However, this process is time-consuming and tedious, so these inspectors tend to be bypassed or have a high identiﬁcation error rate, often caused by fatigue. Various computer vision techniques, discussed further below, can be also used for classiﬁcation. The error rate and reliability of diﬀerent techniques tend to vary as well, but more advanced systems could completely replace the human factor, thus increasing yields of companies signiﬁcantly, as diﬀerent types of wood species have vastly diﬀerent values. These somewhat automated systems can be also used in crime scene investigation, ancient architecture classiﬁcation, or ecology studies focused on relationships between various species.


One of the problems is the number of well-trained inspectors in the current market environment. Their number tends to stagnate or slowly decrease, which contradicts the ever-growing industry. That is why many companies started to develop computer vision alternatives, such as Kenalkayu, achieving a recognition rate of approximately 90% [6].


The article is focused on visible spectrum-based vision systems and other alternative methods presented in Alternative Data Acquisition Methods. Unfortunately, these alternative methods are often lacking and oﬀer lower accuracy than standard vision-based systems; therefore, this section was added to complete the review.


<!-- Page 2 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 2 Journal of Sensors


The ﬁrst part is primarily focused on wood classiﬁcation problematics, the motivation behind it, and intentions of researchers. Samples of some datasets are presented, along with a brief analysis of wood structures and types. Moreover, the summary of all used methods is presented along with a brief description of results.


The second part is structured in a similar way. However, it is focused on wood defect identiﬁcation. In contrast to wood classiﬁcation, the second subsection mainly covers wood defection types. The signiﬁcant part is also focused on the mathematical description of the most frequently used methods. The section is chronological—the newest methods are presented and described as last.


In the ﬁnal part (Conclusion), the future evolution is discussed, along with potentially beneﬁcial ways of research.


## 2. Wood Recognition and Quality


Several papers focused on wood quality, type of wood recognition, and defect recognition tasks have been published, especially by institutes from countries with signiﬁcant wood industrial potential. Since it is necessary to process a signiﬁcant amount of wood in the shortest time possible, the emphasis is placed on speed and quality of assessment. The quality of wood can be assessed based on the following parameters:


(i) Wood type classiﬁcation: [7–22]


(ii) Wood defects:


(a) Knot detection [23–34]


(b) Crack detection [27, 28, 31–35]


(c) Wood grading [35]


(d) Holes [26, 33]


(e) Resin pockets [35]


(f) Discoloration [26]


(g) Joints [28]


(h) Stains [33]


The human eye and magnifying glass have been the most common historical instruments used to assess the quality and type of wood. According to Cao et al. [27], humans can achieve reliability of just around 70% and are error-prone in long-term wood quality assessment, as eye fatigue is an inseparable part of the inspection routine. In addition, demands on inspection speed are signiﬁcantly increasing, leading to the lack of competent manpower.


Recognition is a signiﬁcantly more challenging task in tropical countries, as they have a much higher diversity of tree species in comparison to temperate countries. Highly trained experts are needed to adequately assess wood in these areas, as characteristics of individual trees vary greatly. Over a thousand tree species with unique characteristics which must be cross-referenced by microscopes are currently assessed by trained workers [9]. The process of training


Figure 1: Standard inspection of logs in a Brazil forest. An experienced inspector classify each individual log [37].


requires talent and hard work, which can lead to mastery of regional tree species. Nowadays, the biggest problems lie with the limited manpower and speed of each assessment [12].


Some countries made signiﬁcant investments in speciﬁc areas of the timber industry focusing on their internal issues and interests. Almost every referred article published by Malaysian, Indonesian, or Brazilian Institutes [7–10, 12, 15, 16, 18, 20] is focused on wood type assessment, because of illegal trade within their territory. Thousands of tree species are present in their forest areas (described by [36]), and proper inspection and classiﬁcation of processed pieces in higher volumes are practically impossible, as these countries lack any convenient technology. This leads to smuggling of endangered and rare tree species, or even underpricing at corrupted customs, which leads to signiﬁcant loss of money. Moreover, Paula et al. and Carpentier et al. [11, 14] mentioned in their article that even a trained expert cannot guarantee reliability of his inspections, when some particular features like shape of leaves or needle distribution are not present during truck loading (Figure 1). In the case of observations by a magnifying glass, even a subtle diﬀerence in the wood structure can serve as a key dividing element, thus increasing the error rate of visual inspections.


Scandinavian institutes focus their attention on sawmill automation [13, 30, 35]. Their natural resources consist of European standard coniferous trees. In general, their datasets include fewer tree species in comparison to Malaysians mentioned above, but the structure in cross-section is similar because of natural adaptations to Nordic climatic conditions.


China contributed with signiﬁcant research as well [23, 25, 27–29, 32, 34]. They focus on defect detection. The Chinese timber industry is mainly built on plywood slab production, which provides fundamental material for manufacturing of furniture, decorations, packaging, and construction parts. Defects negatively impact mechanical properties, which subsequently inﬂuence price and overall quality of products. According to Yang et al. [32], the annual output of plywood in China reached up to 170 million cubic meters in 2016.


The identiﬁcation of hardwood has signiﬁcant importance as well. The article presented by Tou et al. [12] pays close attention to structural diﬀerences which are crucial in


<!-- Page 3 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 3 Journal of Sensors


Producer 1


Legal local


flow


Legal wood


flow


Market interaction


Legal wood


flow


Producer 2


Legal local


Illegal local


flow


flow


Illegal wood


flow


Legal wood


flow


Market


Processing


Illegal local


Legal local


Mixed wood


flow


flow


flow


Figure 2: Wood traﬃcking technique often used in developing countries.


civil engineering and could cause fatal failures in case of incorrect building material selection. For instance, the wrong choice of wood type for roof pillars can lead to subsequent collapse of the building.


## 3. Illegal Logging and Trading


Illegal forest activities and illegal logging are a signiﬁcant problem in today’s society. Illegal forest activities were deﬁned by Tacconi et al. [38] as all illegal acts that relate to forest ecosystems, forest-related industries, and timber and nontimber forest products. This deﬁnition however excludes activities such as processing of illegal timber (or illegal processing of timber if the manufacturer does not have appropriate licenses), trading of illegal timber, illegal expropriation of customary forest lands, or even illegal conversion of forest land [39]. Many bigger markets, including the US, the EU, and Australia, adopted laws prohibiting illegally harvested timber products from entering their markets. However, when China introduced a domestic logging ban in 1998, it became the world’s largest importer of tropical timber [5, 40]. It is also a key processing country, manufacturing 40% of global furniture, which is then imported to the US and Europe [41]. Unlike other mentioned countries, China does not have dedicated legislation concerning curbing of illegal timber imports [40].


Illegal logging aﬀects many timber species, which are often rare and endangered, but also highly valuable for export. Many of these endangered species have higher economic values due to their unique physical and chemical properties (including color, texture, odor, and hardness of wood) or even cultural value [42, 43]. Higher value in turn increases rarity/scarcity of harvested trees, intensifying their threatened status or even driving them to extinction. Among these rare species are mahogany, rosewood, and ebony wood. Each of these species has its own characteristics. These wood species are generally used in speciﬁc markets (high-value products) such as parquets, furniture, boats, or musical instruments [44, 45].


During illegal tree harvesting, criminal loggers face serious obstacles, in the form of local residents, inspectors, and law enforcers. Among these people are also forgers of logging permits and timber certiﬁcations. People who can arrange the shift from “illegality” to “legality” are necessary intermediaries between both worlds. Their “pay” may vary greatly, according to quality, type, and amount of wood.


For example, in the case of wood traﬃcking from Indonesia to Malaysia, Malaysian businessmen were paid around 10– 20 euros for one cubic meter of meranti wood, while its price on the European market was approximately 200 euros [46].


The wood classiﬁcation system based on computer vision could at least partially bypass a signiﬁcant amount of these illegal “businessmen,” especially the factor of trained wood inspectors, which sort each individual log. However, this system needs a high degree of security, as criminal loggers often employ hackers, who “legalize” wood in internal systems of the aﬀected countries.


Figure 2 represents one of the often used traﬃcking techniques. Two wood producers, apart from supplying the local production, sell their logs to a third party processing plant. However, one of the producers takes part in illegal logging. The third company basically mixes legally and illegally logged wood together, which leads to wood laundering. The ﬁnal processed product is branded as manufactured from legal wood, while it might contain parts from illegal activities.


## 4. Wood Type Classification Dataset


A dataset of Malaysian macroscopic images of tree crosssection acquired by the Centre for Artiﬁcial Intelligence and Robotics (CAIRO) is often used as a starting point of case validation [8, 9, 12, 16, 21, 22, 47]. This dataset consists of over 100 species of tropical trees. Each species has ﬁfty images for training and ﬁfty images for testing. Images were taken by a grayscale Picolo CCD camera with 10x magniﬁcation and can be seen in Figure 3. It is also used for real-world applications, such as Kenalkayu, which is a state-of-the-art pattern recognition technology developed by the earlier mentioned CAIRO. Unfortunately, this dataset is not publicly available.


On the other hand, a more extensive macroscopic dataset was acquired and released by Brazilian University UFPR (Federal University of Parana) in 2010. Figure 4 shows diﬀerent samples from the UFPR dataset. The database consists of colored, JPG, high-resolution photos (3264 × 2448) without compression, counting 41 species of the Brazilian ﬂora. Each species includes at least 50 pictures, and the dataset itself has 2942 pictures in total. It might seem insuﬃcient for neural network application, but since high-resolution photos were obtained, each picture can be sliced into multiple diﬀerent ones. This database, collected by SONY DSC T20 with macro


<!-- Page 4 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 4 Journal of Sensors


Figure 3: Samples from the CAIRO dataset of Malaysian wood [12].


Figure 4: Samples from the UFPR dataset of Brazilian wood [11].


Fir Pine Spruce


Figure 5: Samples from Dmitrii Shustrov’s dataset of coniferous trees [13].


function, was already used by several Brazilian researchers [10, 11, 48]. The dataset is publicly accessible.


In 2011, UFPR released a microscopic database, containing 112 diﬀerent catalogues of forest species [7]. All images were acquired by an Olympus Cx40 microscope with 100x zoom. The database itself consists of 2240 microscopic PNG images, with a resolution of 1024 × 768 pixels, which were labeled by experts in wood anatomy. Of the 112 available species, 37 are softwoods and 75 are hardwoods. This database cannot be used for color-based recognition, since its hue depends on the current used to produce contrast in the microscopic images. All images can be freely converted to grayscale for further work. This database was presented by university staﬀand successfully tested on gray level cooccurrence matrix (GLCM) and Local Binary Pattern (LBP) methods described further below [7].


The only thesis devoted to the classiﬁcation of nontropical wood was published by Shustrov [13]. He worked with a self-made database of 3 coniferous tree types (spruce, ﬁr, and pine) covering 1115 board samples divided into 242938 high-quality image patches. Figure 5 shows diﬀerent samples from Dmitrii Shustrov’s database.


The Brodatz texture dataset is also one of the currently available datasets. This dataset covers 112 grayscaled


256 × 256 textures, which are segmented into 16 disjoint images with a size of 64 × 64. The whole dataset is somewhat outdated, since it was created in 1999 [49], and the resolution is unfortunately pretty low. However, it can be used for GLCM, a texture classiﬁcation method, further described below [50].


A novel idea of autonomous forest inventory gathering using drones was presented by Carpentier et al. [14]. His solution is built on tree type recognition based on bark images. This approach is advantageous in numerous ways, because despite seasonal changes, the bark is always present, and even if logs are cut and stored in a lumber yard, the bark remains. Figure 6 shows diﬀerent samples of bark.


## 5. Wood Type Classification Results


The sum of various results is summarized in Table 1, and crucial settings with the best performance were highlighted. Since multiple methods including either diﬀerent feature extractors or various classiﬁers were mostly tested within each article, all used approaches are mentioned under the “methods” column, so every compared method is listed. A blank ﬁeld means that only one approach was used, and it is listed under the column “features and classiﬁers,” where


<!-- Page 5 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 5 Journal of Sensors


Figure 6: Samples from the dataset of tree bark [14].


in the case of multiple methods, only the most successful one is listed. The dataset column shows the number of pictures used for testing in total, mentioning the image ratio in brackets that is used for training validation and testing. The last values are missing in some cases, signalizing that there was no separate dataset used for the ﬁnal phase of testing. The only exception can be noticed in [14] where 5-fold cross-validation was used. It means that the whole dataset was split into 5 folders, each serving as a validation set in one epoch, while others are used for training. The results of all 5 validations are averaged for the ﬁnal accuracy value. Even though this technique is computationally expensive, it provides an objective conclusion. Dataset expansion methods were found to be very useful as well, as the system accuracy signiﬁcantly increases with bigger datasets. Two types of dataset expansion are listed: subimages and augmentation. The ﬁrst one is based on splitting of the original highresolution picture into multiple low-resolution ones. For instance, Shustrov [13] expanded his dataset of 1115 pictures into 255724 patches and that is one of the main reasons his system performed so well. The other method called augmentation is based on artiﬁcial enhancement of the original picture. Algorithms like ﬂipping, rotation, color jittering, scaling, and cropping are very popular in this area. For example, Tou et al. [16] enlarged his dataset by employing rotational augmentation from the original 12 pictures to 600.


Since diﬀerent datasets and conditions were presented by all authors, it is not totally objective to compare their system performance just by achieved accuracy. Even with the increasing number of categories, the task becomes much more challenging. The general rule says that when the system is trained on bigger datasets, it will perform better on newly acquired data.


Promising results were accomplished by convolutional neural networks [13, 14] which have recently become popular. They are computationally expensive; therefore, signiﬁcant resources are needed for real-time applications. However, as their computation can be accelerated by a Graphic Processing Unit (GPU), satisfactory speed can be obtained. Classical neural networks in the form of classiﬁers have proved to be useful as their accuracy is greater than 95% [9, 21]. Unfortunately, their performance is highly dependent on the choice and setting of a feature extractor. Mentionable performance was achieved by nonneural machine learning classiﬁers Linear Discriminant Analysis (LDA) and support vector machine (SVM) in [10, 18].


A successful methodology was proposed by Hafemann et al. [48], who introduced in-house designed convolutional neural network architecture. Original images were split into


smaller patches leading to an increased training dataset (approx. 3 million images). A lightweight model in combination with the region split voting method (described in Region Split) achieved 97.32% accuracy.


## 6. Wood Defect Description


Many types of defects were introduced and inspected within published articles. Some of those refer to identiﬁcation or localization of basic elements in general [25, 29], like knots, splits, and cracks (Figure 7), but other cases required more speciﬁc classiﬁcation of individual defect types with respect to various mechanical properties [23, 26, 30–35]. Speciﬁc mechanical diﬀerences between individual defects are described by Berthellemy [53], which focuses on timber bridge construction, where not only the exact type of defect must be recognized but also orientation and age which play an important role as a quality indicator.


Basic diﬀerentiation between types of knots was described by Gu et al. [30]. They stated that for most applications, sound knot (Figures 7(a) and 7(b)) along with pin knot (Figure 7(d)) is considered harmless and does not inﬂuence mechanical properties to any signiﬁcant extent. On the contrary, black knots (Figure 7(c)), knot holes (Figure 7(f)), stripes (Figure 7(h)), splits (Figure 7(i)), and wanes (Figure 7(j)) are described as quality reducers. In addition, quality indicators vary according to individual standards and ﬁeld of application. For instance, solution of Yang et al. [32] required just basic diﬀerentiation into 4 categories. The opposite case was introduced by Ruz et al. [33], who managed to distinguish 10 types of defects.


## 7. Wood Defect Classification Results


It might seem that every listed author achieved good results. However, with respect to a number of sorted categories along with extent of the presented dataset, some articles [26, 29] did not present universal and suﬃciently robust solution. On the other hand, there are some [30, 33] which achieved a promising score, both based on SVM classiﬁers. Two exceptions [27, 34] based on Near-Infrared Spectroscopy (NIRS), instead of casual cameras, accomplished competitive results as well, but since the method is based on diﬀerent technology, it cannot be analyzed as equal.


Not all researched papers are included in Table 2, as their methods or results were not comparable in any scale [23, 28, 35]. These were focused more on research and contained no presentable results of described methods. Even so, they could serve as useful inspiration, especially in the case of


<!-- Page 6 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 6 Journal of Sensors


Reference Year Methods Features Classiﬁer Categories Dataset (train./valid./test) Dataset expansion Accuracy (%)


## [8] 2007 — GLCM MLP 5 250 (-/-/-)∗ — 72.00


[9] 2008 — GLCM MLP 20 2100 (93/7/-) — 95.00 [51] 2008 Img. Segm.+SVM/KNN/NN/LDA Img. Segm. NN 7 101 (99/1/-) — 80.00


## [50] 2008 GLCM/DGLC+NN/KNN GLCM MLP 5 500 (50/50/-)∗ — 72.80


[12] 2009 GLCM+thresholding GLCM Thresh. 6 510 (88/12/-)∗ — 80.00


## [21] 2010 — LBP NN 37 3700 (80/20/-)∗ — 96.60


[22] 2010 GLCM/Gabor GLCM+Gabor MLP 30 3000 (90/10/-)∗ — 90.30


[47] 2010 GLCM/Gabor GLCM NN 20 2010 (90/10/-)∗ — 91.00


[11] 2010 Color/GLCM+MLP Color+GLCM MLP 22 1270 (32/18/50)∗ — 80.80


[16] 2009 Gabor/GLCM+KNN Gabor KNN 6 12 (50/50/-)∗ aug. 85.00


Table 1: Comparison of various works focused on wood classiﬁcation methods, based on various classiﬁers.


(A) NN: (Artiﬁcial) Neural Network; BGLAM: Basic Gray Level Aura Matrix; CLBP: Completed Local Binary Patterns; CNN: convolutional neural network; GLCM: gray level covariance matrix; KNN: K-Nearest


Neighbor; LBP: Local Binary Patterns; LDA: Linear Discriminant Analysis; LPQ: Local Phase Quantization; MLP: multilayer perceptron; NN: neural network; SVM: support vector machine; aug.: augmentation;


[15] 2018 DW+LBP+SVM LBP SVM 3 4320 (66/34/-) sub., aug. 85.00


[52] 2014 — GLCM Corr. 10 1050 (95/5/-) — 95.00


## [18] 2013 GLB/SPPD/BGLAM+LDA GLCM+SPPD+BGLAM LDA 52 5200 (70/30/-) — 98.69


[19] 2013 GLCM/Gabor GLCM+Gabor MLP 25 500 (80/10/10)∗ — 92.60


## [7] 2013 LBP/GLCM+KNN/LDA/SVM LBP LDA 112 2240 (40/20/40)∗ — 80.70


[20] 2016 BGLAM+SVM BGLAM SVM 52 5200 (90/10/-) — 99.84 [13] 2018 — — CNN 3 1115 (70/15/15) sub. 99.00


[10] 2014 Color/LBP/LPQ/CLBP/Gabor CLBP, color, LBP SVM 41 2942 (35/15/50)∗ sub. 97.64


[48] 2014 — — CNN 41 3M (5f-cross-valid.)∗ sub. 97.32


[14] 2018 — — CNN 23 1006 (5f-cross-valid.)∗ sub. 97.81


sub.: subimages; ∗: an indication that dataset is available online for free.


<!-- Page 7 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 7 Journal of Sensors


(a) (b) (c) (d) (e)


(f) (g) (h) (i) (j)


Figure 7: Diﬀerent types of defects: (a) sound knot (healthy, normal), (b) sound knot in radial plane, (c) black knot, (d) pin knots, (e) decayed knot, (f) knot hole, (g) resin pocket, (h) core stripe, (i) split, and (j) wane [54].


Table 2: Comparison of various works focused on wood defect detection methods, based on various features/classiﬁers.


Reference Year Methods Features Classiﬁer Categories Dataset (train./valid./test)


Accuracy


(%)


[26] 2006 — Unique BNN/BANN 2 232 (80/20/-) 86.52


[30] 2009 — Color+size SVM 5 1200 (66/34/-)∗ 96.50


[31] 2009 Gabor ﬁlters+AMMLP Gabor ﬁlters AMMLP 3 100 (52/48/-)∗ 97.91


[33] 2009 Color+GLCM+own+


SVM/MLP Color+GLCM+own SVM 10 2200 (50/25/25) 91.39


[29] 2016 LBP/GLCM+NN LBP NN 52 220 (82/18/-) 93.30 [27] 2017 PLS/PLS-DA/LS-SVM/BPNN Nonimage BPNN 4 360 (66/34/-) 97.50 [34] 2017 DPLS/PCA-DPLS/BPNN Nonimage BPNN 4 400 (75/25/-) 92.00 [32] 2018 HOG/FREAK/SURF+BPNN HOG BPNN 4 150 (60/40/-) 90.82


## [55] 2018 — — CNN 18 839 (-)∗ 91.55


[57] 2019 — — Faster R-CNN 4 353+aug. (-) 96.10


AMMLP: artiﬁcial metaplasticity multilayer perceptron; BANN: Bees Algorithm Neural Network; BPNN: Backpropagation Neural Network; DPLS: Discriminant Partial Least Squares; FREAK: Fast Retina Keypoint; GLCM: gray level covariance matrix; HOG: Histogram of Oriented Gradients; LBP: Local Binary Patterns; LS-SVM: least squares support vector machines; MLP: multilayer perceptron; NN: neural network; PCA-DPLS: Principal Component Analysis-Discriminant Partial Least Squares; PLS: Partial Least Squares; PLS-DA: Partial Least Squares and Discriminant Analysis; PSO-GA: particle swarm-genetic hybrid algorithm; SURF: Speed-up Robust Feature; SVM: support vector machine; ∗: an indication that dataset is available online for free.


Kauppinen’s dissertation [35] covering description of multiple color-based machine vision methods.


to implement defect segmentation as well (described more in the next subsection).


The second one, the Faster R-CNN-based solution [57] covers multiple wood veneer defect detection, using a 300


Some articles cover additional information [23, 29, 32, 33], because they cover not only defect recognition but also its localization during preprocessing.


× 300 mm region of interest. The proposed system managed to distinguish between 4 types of defects. With respect to accuracy, the most successful model based on ResNet152 reached up to 96.1% in the case of diﬀerentiating between faulty and nonfaulty regions and up to 80.6% in the case of distinguishing between types of defects. On the contrary, ResNet152 inference time (48.01 ms) was 7 times longer than computationally economical AlexNet architecture, which was in terms of accuracy just 0.6% behind ResNet152.


Two interesting CNN solutions were introduced in recent years. The ﬁrst one [55] employs the method of splitting images into multiple sections, which are evaluated, and faulty segments are identiﬁed using a lightweight CNN model. Even though the used architecture DeCAF [56] is not as computationally intensive as newer successors, the patches managed to cover areas only up to 75 × 75 pixels. However, in real-time deployment, the splitting and evaluation of high-resolution images would lead to a signiﬁcant increase in computational complexity. The authors managed


Although the algorithm was released in 2016, the Faster R-CNN is the newest proposed method among the


<!-- Page 8 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 8 Journal of Sensors


researched papers focusing on wood defect detection [58]. However, it can not be certainly used as state-of-the-art solution. Promising results were achieved by the lastest YOLO-V5 CNN architecture, which was released in June of 2020. A comparison of YOLO and Faster R-CNN was carried out by Dwivedi [59], and all results favored the YOLO-V5. Unfortunately, no additional oﬃcial papers were published by YOLO authors [60]; therefore, the further development of the algorithm is expected. Another promising state-ofthe-art model EﬃcientDet [61] could provide some signiﬁcant improvements as well, since the EﬃcientDet model currently leads to COCO dataset-based ranking [62].


## 8. Defect Segmentation


Defect localization became an attractive machine vision community topic, although for the most of the tasks, bounding boxes are a suﬃcient solution. Nevertheless, in some speciﬁc cases, the precise localization of defect position with respect to pixel resolution can be beneﬁcial.


Unfortunately, only a limited number of publications expressed an eﬀort to locate the exact positions of classiﬁed defects.


In the ﬁrst researched publication, Zhang et al. [29] introduced a method build on assumption, by which every defect has an easily distinguishable edge. In the ﬁrst phase, the image is preprocessed by a canny edge detector. The process is supposed to subtract foreground with a potentially defective area and consequently classify segmented image. Even though the stated results showed potential, in the case of edge detection of knot with hardly spotable edges, the substracted mask does not seem to diﬀerentiate the faulty region from the nonfaulty one (see Figure 8). As only 3 examples were presented and none of them included a picture without defect, the method cannot be objectively evaluated.


A diﬀerent approach was chosen by the Northeast Forestry University research team [34], which evaluated wood quality using near spectroscopy. Their tested segmentation method was based on hit-or-miss transformation (HTM) followed by PCA classiﬁcation of defect. Similarly to Zhang et al. [29], only 3 samples were presented in the publication and none of them included a nondefect scene.


The latest deep learning approach was introduced by Ren et al. [55]. The proposed method was based on lightweight convolutional neural network architecture DeCAF which was originally introduced in 2013 [56]. A pretrained model was used as a feature extractor; thus, the extensive dataset was not required for the initial training. Initially, the image was split into multiple regions, which were assessed individually. In the case of positive defect classiﬁcation, the Class Activation Map (CAM) [63] method was used to identify the discriminative region.


## 9. Alternative Data Acquisition Methods


Even though this research is focused on machine vision recognition image-based systems related to a visible spectrum, some alternative approaches with satisfying results were published as well. One such approach is the analysis


(a) (b) (c)


Figure 8: Image processing sequence: (a) original image, (b) edge detection, and (c) extracted region [29].


of the spectral radiation reﬂected from the surface of the wood using a special radiation source. For example, in some publications, the deployment of Near Infrared (NIR) [27, 64] or Mid-IR [65, 66] was proposed. Another example is ﬂuorescence spectroscopy technology [67]. Such systems consist of a spectrometer, a laser source, and an optical ﬁlter. In [68], a system for wood species recognition was developed, where ultrasonic signals were used as input features. Diﬀerent wood types have diﬀerent elastic reactions which are caused by their own structure of cellular characteristics. The signal that has passed through the radial, tangential, and longitudinal surfaces of the wood is used as input for the classiﬁcation system.


Some alternative nonconventional camera approaches in the ﬁnal testing/recognition phase are based on image processing of acquired data.


Speciﬁc beneﬁcial properties were observed in X-ray sensing. X-ray can be used to localize rotten knots or hollow hearts, as proposed by Mu et al. [25], or even for tree-ring detection as mentioned by Piuri and Scotti’s article [67].


A unique method was tested by Jordan et al. [68] who obtained images of tree bark of cedar and cypress using terrestrial lidar (Figure 9) and managed to achieve accuracy of nearly 90% by using them in a convolutional neural network. However, as Carpentier et al. [14] proposed more accurate and robust solution using standard images, this method was not expanded further.


## 10. Features and Classifiers


Researchers tend to use various methods in their approach. This section will cover the basics of each individual approach and theoretically describes methods which had the best results according to Tables 1 and 2. Only the works which had the highest performance in respect to the size of dataset and number of categories were selected. These methods have high possibility of deployment in newly developed systems.


Since all values of image pixels cannot be fed to a conventional classiﬁer straight away, as it would lead to poor performance, important features, represented by a vector, must be extracted from the image. Multiple methods were proposed for solving this issue including machine learning-based categorization systems related to machine vision, but not a single universal solution was discovered. The accuracy of the system still partially depends on the designer’s intuition, as diﬀerent types of scenes include diﬀerent recognizable features. These features can be obtained from various mathematical and physical points of view. Some tasks are well


<!-- Page 9 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 9 Journal of Sensors


Figure 9: X-ray image of a rotten knot [25], enhanced X-ray image of cross-section for tree/ring detection [67], and lidar-based image of cypress tree with bark [68].


Classification


SVM, KNN, LDA, etc.


Image acquisition Feature extraction


## 1 8 4 9 6 3 2 I1


O1


MLP, BPNN, NN, etc.


O2


I2


HOG, color, LBP, etc.


O3


I3


Figure 10: Block diagram of feature-based classiﬁcator.


recognized with respect to their color, and others could perform better with distribution of cooccurring pixel values. Furthermore, some articles proved that the combination of diﬀerent feature extractors leads to enhanced overall performance [10, 18, 19, 33].


Most of the researched solutions are based on the model illustrated in Figure 10. Some exceptional experimental approaches were published, where authors choose to create their own features or classiﬁers after observing some similarities or diﬀerences between classes. This approach was presented in [12], where thresholding was used for classiﬁcation. In [30, 33], one set of features was represented as extracted geometrical dimensions of defects. Color-based self-made features could be found in [30]. In [11], the authors unusually choose extraction of particular color channels from diﬀerent color spaces.


## 11. Feature Extraction Methods


11.1. Gray Level Cooccurrence Matrix. In order to capture essential information about the structural arrangement of the surface, two types of texture features can be used. The ﬁrst-order statistical features based on the histogram of an image, and second-order statistical features derived from the GLCM.


The gray level cooccurrence matrix, also called gray level dependency matrix, is therefore deﬁned as a twodimensional gray level histogram for pixel pairs, which are separated by a ﬁxed distance along a speciﬁc direction (usually horizontal, vertical, diagonal, or antidiagonal). Figure 11 illustrates the process of formation of the GLCM for the horizontal direction with a step of 1 [69].


The elements of the GLCM can be considered as probabilities of ﬁnding the relationship between gray level I to gray level j. With respect to those, we can calculate one of the selected features.


Energy feature:


N−1


Pij À Á2: ð1Þ


Energy = 〠


i,j=0


Entropy feature:


N−1


À ÁPij: ð2Þ


−ln Pij


Entropy = 〠


i,j=0


Contrast feature:


N−1


Pij i −j ð Þ2: ð3Þ


Contrast = 〠


i,j=0


Homogeneity feature:


N−1


Pij 1 + i −j ð Þ2 : ð4Þ


Homogeneity = 〠


i,j=0


GLCM was successfully used by Khalid et al. on Universiti Teknologi Malaysia in 2008 [9]. At that time, this research was groundbreaking, as he was the ﬁrst who achieved accuracy greater than 95% on the dataset consisting of 2100 images in 20 categories. The feature vector was categorized by a shallow


<!-- Page 10 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 10 Journal of Sensors


1


## 4 3 2 8 7 6 5 GLCM I


1


8


1


1


5


6


1


2


3


5


7


2


2


4


5


7


1


3


5


8


5


1


2


4


5


6


7


8


1


0


0


0


1


2


0


0


1


0


0


0


0


0


1


0


1


0


0


0


0


0


0


0


1


0


0


0


0


0


0


0


0


1


2


0


1


0


0


0


0


0


0


1


0


0


0


0


0


0


0


0


2


0


0


0


1


0


0


0


0


0


0


0


Figure 11: An example of GLCM computation for a matrix 4 × 5 of eight gray levels represented by numerical values from 0 to 8.


neural network-based classiﬁer. Even though the dataset contained macroscopic monochromatic pictures of tree cross-sections, this solution could be potentially used in a real-time automation system as well.


Khalid et al.’s article was multiple times cited and served as an inspiration for research in this ﬁeld in multiple consequent years. Publications [18, 20], which had a similar approach, managed to improve performance and diﬀerentiated even more categories.


11.2. Gray Level Aura Matrix and Basic Gray Level Aura Matrix. One of the approaches to ﬁnd a feature inside an image is to look at neighboring pixels. These methods work with a so-called structural element, which is the m by n matrix (in some rare cases, it even can be a diﬀerent object), which deﬁnes a pattern inside an image. One of the commonly used image operations in this case is based on a so-called aura, where aura is a measurement of distance of two subsets A and B, both belonging to a structural element s, and denoted by mðA ; BÞ while N is the neighboring system [70]:


m A, B ð Þ = m A, B, N ð Þ = 〠


Ns ∩B j j: ð5Þ


s∈A


The aura of A with respect to B characterizes how the subset B is present in the neighborhood of A. A grayscale algorithm uses only the grayscale variants of original images with intensities in the range of 0–255, to reduce the computational complexity in comparison to fully colored images. A is represented by the following equation:


Â Ã = m Si, Sj


À Á Â Ã, ð6Þ


A = A N ð Þ = aij


where Si is the gray level set corresponding to the ith level of the intensity and mðSi ; SjÞ is the aura measurement between two aura sets given by the equation above. In essence, the Gray Level Aura Matrix (GLAM) of an image characterizes the probability distribution of each gray level in the neighborhood of each other gray level, generalizing the GLCM [71].


Basic GLAM (BGLAM) is GLAM computed from only a single site neighboring pixel system. This approach


was very successful at measuring image similarities for textures, image retrieval, and texture image retrieval or to classify tree species with an improved result compared to GLCM [72, 73].


The ﬁrst paper which provided a promising result by deploying the BGLAM feature extractor (along with SPPD and GLB) on a grayscale wood dataset, consisting of 5200 images from 52 categories, was presented by Yusof et al. [18] from Universiti Teknologi Malaysia in 2013. Yusof et al. greatly enhanced the function of the used algorithm by employing a genetic algorithm which reduced dimensionality of the feature vector. It led to the reduction of computing resources and signiﬁcant improvements of accuracy. Even though the deployment of a genetic algorithm was beneﬁcial, It was not used in any other paper. It can be considered as a promising method for performance enhancement in tasks which are based on combination of feature vector extractor and classiﬁer. Classiﬁcation of Yusof et al.’s solution was performed by the LDA classiﬁer (described in Linear Discriminant Analysis) and reached accuracy of 98.69%.


Yusof et al.’s research was consequently followed by Ruz et al. [33] in 2016, who used the same dataset and increased accuracy to 99.84% by exchanging the LDA classiﬁer with SVM. Even though it has the best results stated in this paper, it cannot be considered as a universal solution since it was not used on new popular extensive datasets (which include thousands of images [1, 2]) and objectively compared with performance of neural networks in general.


Both mentioned articles [18, 20] stated that their results were compared to GLCM and ﬁnd GLCM less accurate than BGLAM especially with the increasing number of categories. Their solutions are in general advantageous for pattern recognition, where rotation invariance is needed, and only a limited dataset is provided for training. These methods could be possibly implemented in an embedded system with limited computational resources.


11.3. Local Binary Patterns and Completed Local Binary Patterns. LBP is based on the combination of GLCM with previously mentioned thresholding. Just as in GLCM, the LBP describes each pixel by the relative graylevels of its neighboring pixels. The descriptor describes the result


<!-- Page 11 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 11 Journal of Sensors


over the neighborhood as a binary number (binary pattern) [74]:


(


N−1


1 ≥0,


s ni −nc ð Þ2i,  s x ð Þ =


LBPR,N x, y ð Þ = 〠


0, otherwise:


i=0


ð7Þ


In order to code the local image in a better way, Guo et al. proposed the Completed LBP (CLBP) pattern for texture classiﬁcation. CLBP has three diﬀerent components, CLBPS indicates the sign (positive or negative) of diﬀerence between the center pixel and local pixel, CLBP-M indicates the magnitude of the diﬀerence between the center pixel and local pixel, and CLBP-C indicates the diﬀerence between local pixel value and average central pixel value. CLBP-S basically describes conventional LBP [75].


LBP along with PLS, Gabor ﬁlters, fractals, GLCM, and the self-proposed colored-based algorithm were used in the Filho et al. [10] research. Filho et al. were examining performance of each individual feature extractor and subsequently impact of their various combinations. Interestingly enough, CLBP, LBP, and the self-proposed colored-based algorithms were present in every successful combination.


Performance of Filho et al.’s system would not exceed its predecessors without the so-called technique “divide and conquer,” which is described in Region Split. Filho et al. described dependency between the number of splits and their relationship to performance of the whole platform. They stated that image splitting is beneﬁcial only up to a certain number of patches. This approach proved to be beneﬁcial in every solution it was deployed in. The self-made dataset consisting of 2942 pictures and 41 categories was used for training and validation.


## 12. Classification Methods


12.1. Support Vector Machine. SVM is one of the most popular supervised classiﬁcation algorithms with the ability to handle noisy and high-dimensional data. In a simple term, the SVM classiﬁcation tries to ﬁnd an optimal line or a hyperplane, capable of separating objects that have diﬀerent class memberships. The SVM method then tries to separate the given samples by a hyperplane in such a way that the separation between the two classes, denoted as a margin, is as wide as possible (Figure 12) [76].


In mathematic formulation, it is necessary to minimize the vector of marginal distances from a separating “line.” This task is a nonlinear optimization task solved by Karush-KuhnTucker conditions in combination with Langrange multipliers. Improvements can be made using a least square computation together with the support vector machine algorithm, creating a combination called LS-SVM. This idea was used to classify woods together with NIR spectrometry [77] and also solves most disadvantages of SVM [78].


12.2. Linear Discriminant Analysis. In multiple cases, more than just 1 or two features are used for classiﬁcation; it is hard to track the K-Nearest Neighbor (KNN) and any other multi


Y


X


Figure 12: Example of feature space for 2 features and cutoﬀline to separate 2 diﬀerent classes.


space classiﬁcation algorithms. One of the suggested solutions applies statistic methods. LDA uses multiple spaces, to create a new space, and projects data onto a new space in a way to maximize the separation of the two categories, reducing the multidimensional graph into a 1D graph (or at least less dimensions). This is carried out by calculating means and variances. Calculation itself is carried out by the ratio of the variance between the classes to the variance within the classes. Modiﬁcations of LDA can be used to successfully classify whole images, instead of vector spaces only [79]:


μ1 −μ2 ð Þ2


s12 −s22 : ð8Þ


The equation is an example of the multidimensional problem, which is in this case a 2-dimensional problem representing 2 features calculated with the methods mentioned above. The problem is the same for all classiﬁcation methods.


12.3. Artiﬁcial Neural Network. The Artiﬁcial Neural Network (ANN) is a classiﬁcation and machine learning system which attempts to process the information in the same way as a biological neural network does (Figure 13). Biological neural networks consist of an enormous amount of organized nerve cells, called neurons, which interact with each other in parallel.


The logical principle of the neural network is ﬁnding a set of weights, which solve the required problem with a least means square error. It is mostly archived through the process called backpropagation, where the results of forward pass of the neural network are compared with a desired output value (known solution for the required inputs). After evaluation, the given error is backpropagated, and based on gradient computation, a set of new and adjusted weights are conﬁgured in the system [80]:


· μ1 −μ2 ð Þ2


∂oj ∂wij


∂oj ∂netj


∂netj


∂E ∂wij


## = ∂E


## = ∂E


s12 −s22 : ð9Þ


∂oj


∂oj


∂wij


<!-- Page 12 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 12 Journal of Sensors


x1


𝜔1


x2


𝜔2


Inputs


...


...


xm 𝜔m


Weights


Bias


b


y 𝜑(.) Σ


Output


Activation


Sum


function


Figure 13: The mathematical model of artiﬁcial neuron.


12.4. Multilayer Perceptron. One of the possible topologies for a certain layer of neurons is to use multilayer perceptron. Multilayer perceptron (MLP) consists of at least three layers of nodes: an input layer, a hidden layer, and an output layer. Except for the input nodes, each node is a neuron that uses a nonlinear activation function. Some cases of MLP can be constructed of a single hidden layer, and in some cases, each neuron is connected to every single neuron in the previous and also in the next layer of the neural network. An example of this topology was used to classify wood, with 20 hidden neurons and 180 neurons in the output layer and matrix of input layers [81].


Multilayer perceptron (shallow neural network) was used as a classiﬁer in multiple papers. Even though Tou et al. [8, 50] had a limited dataset and results of their methods were relatively poor in comparison to other solutions, their work showed potential of a neural network (NN), as its performance clearly outperformed KNN.


On the contrary, Ruz et al. [33] in 2009 designed a system where the pairwise version of SVM outperformed MPL by 7.51% reaching 91.39%. The research included methods of defect segmentation based on the fuzzy min–max function (FMMI). Only features based on geometrical and color properties of segmented defect were used by the classiﬁer. Cao et al. [27] and Yu et al. [34] presented their solution for defect detection in 2017. They distinguished 4 categories with about 400 samples by using alternative NIR technology for defect classiﬁcation. Overall performance had promising results, exceeding over 92% accuracy in both cases. When analyzing the same 1D dataset, the NN classifying method performed 9% better than PCA-PLS [34], 4.17% better than SVM [27], and 10.83% better than PLS [27].


## 13. Convolutional Neural Networks


The convolutional neural network (CNN) is a modiﬁcation of ANN, where instead of using standard perception layers, a convolution is used (max pooling layers), leading to fully connected layers and output. There are many diﬀerent types of architectures, but the main diﬀerence is that an input to this type of neural network is a 2D array. The convolution


operation is inherited from a frequency property of an image and also together with max pooling can lead to a reduction in transition from layer to layer. This is a valuable property for classiﬁcation, because a huge number of inputs can be reduced to a small number of outputs:


k


k


f ∗h ð Þ x, y ð Þ = 〠


〠


f x −i, y −j ð Þ × h i, j ð Þ: ð10Þ


i=−k


j=−k


One of the modern approaches in CNN includes a massive number of layers and parameters. These factors aﬀect the training time, and in order to train CNN from the scratch, it takes a lot of time even when such computational resources as GPU are used. This task can be solved by the concept of transfer learning [82].


Ever since the CNN algorithm won the ImageNet competition in 2012 [83], its popularity increased rapidly. Nowadays, even greater challenges arose, and with suﬃcient available computational resources, convolutional neural networks represent a revolutionary approach (Figure 14). Moreover, an impressive result was achieved by the You Only Look Once (YOLO) algorithm [84], which is able to segment objects in image and sort them to 9000 categories in real time.


Unfortunately, just a few articles related to wood inspection were published. Two of them were researched [13, 14], and both have an outstanding outcome. In [13], 4 basic CNN architectures were described: AlexNet, VGG-16, GoogLeNet, and ResNet-50. These architectures were consequently tested and compared to each other. Expectedly, the newest GoogLeNet provided the best performance but is computationally the most expensive in comparison to other tested methods. Furthermore, Shustrov [13] was able to process one board patch in 0.02 s (whole board of 25 patches in 0.47 s), but his experiments were performed on the server with two NVIDIA GeForce GTX TITAN Black GPU, Intel Xeon CPU E5-2680, and 128 gigabytes of random access memory.


The convolutional neural network was highly successful in the ImageNet competition in 2012 and proved to be very eﬀective on the extended dataset. CNN shifted focus of


<!-- Page 13 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 13 Journal of Sensors


O1


O2


O3


Figure 14: Block diagram of convolutional neural network.


researchers to the model comprising feature extractors and classiﬁers. Unfortunately, despite the signiﬁcant amount of papers, dedicated to identiﬁcation and localization of defects on various materials, these algorithms were tested on wood only scarcely.


The most promising results were presented in the master’s thesis of Dmitrii Shustrov, who managed to extend his dataset from 1115 to 242938 images. It was achieved by splitting high-resolution pictures to low-resolution pictures. Even though only 3 wood categories were present in the dataset, they had hardly noticeable diﬀerences in wood structure, which could not be processed by human inspectors. This research presents performance comparison of popular CNN models AlexNet, VGG-16, GoogLeNet, and ResNet-50. AlexNet managed to reach accuracy of 98.9% in the ﬁrst evaluation in comparison to GoogLeNet 99.4% in the second.


Carpentier et al. [14] managed to achieve promising results by diﬀerentiating 23 tree categories according to bark images. A training dataset was used for testing of ResNet18, ResNet34 CNN Architectures. The inﬂuence of various batch sizes (8, 16, 32, and 64) was examined, and its inﬂuence on system accuracy was described. Results varied across diﬀerent settings, so it is diﬃcult to decisively select one solution. The best achieved accuracy (97.81%) was further improved by 3.93% by deploying the “divide and conquer” method (described in Region Split).


CNNs are highly dependent on the hardware and its resources. Long training processes require a high amount of random access memory (RAM), and computation itself should be carried out by GPU. Therefore, CNNs can be only used on High-End Desktops (HEDT) or high-performance embedded systems.


13.1. Region Split. Positive accuracy enhancement was in multiple articles [10, 13, 14, 20] accomplished by using the “divide and conquer” method. A whole image is split into multiple parts, and each subimage is evaluated individually. The most recognized category then represents the resulting one according to majority voting (Figure 15).


Some publications [10, 13] explored the dependency test between the number of patches and overall accuracy of the system. According to graphs in Figure 16, it is obvious that, for the majority of methods, image splitting is beneﬁcial, but once a certain point of recognition rate is exceeded, it is no longer dependent on the number of patches.


Advantageous properties of majority voting fusion logic such as robustness or invariance were conﬁrmed in a study by [85] and experiments carried out in a manuscript by [86].


Figure 15: Demonstration of majority voting [14].


## 14. Discussion


In previous chapters, comparisons of late or recent algorithms and methods for classiﬁcation of either wood species or even defects in wood itself were presented. The trend is shifting from manually “hard coded” algorithms to a much more modern artiﬁcial intelligence approach, especially to neural networks, which oﬀer at least the same or even significantly better performance. The deep convolutional neural network is nowadays capable of achieving record-breaking results on highly challenging datasets while using purely supervised learning [83].


Improvement to deep neural networks, the mechanics behind the individual layers [87] or deployment of deep residual learning [88], will as well lead to signiﬁcant improvements to performance of wood species classiﬁcation and error detection. Evaluation of networks of increasing depth based on architecture with very small (3 × 3) convolution ﬁlters shows that a signiﬁcant improvement on the priorart conﬁgurations can be achieved by pushing the depth to 16-19 weight layers [89]. The actual problem in deployment of such deep neural network lies in actual datasets. As mentioned in previous chapters, wood datasets usually contain around 2000 images; however, the dataset for training of a deep neural network can consist of more than 60000 images [90].


Other ways to work around this “gap” is to switch the role of passive learning algorithms, where learning is done by a computer itself and focuses on the role of a teacher. While machine learning focuses on creating new algorithms and improving the accuracy of “learners,” the machine teaching discipline focuses on the eﬃcacy of the “teachers” [91]. The research carried out by Microsoft can improve the performance of wood error detection and classiﬁcation by teaching a neural network based on new breakthrough methods.


<!-- Page 14 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 14 Journal of Sensors


100


95


90


Recognition rate (%)


85


80


75


70


65


60


Full image 64


4 9 25 36 49 100


Number of subimages


Color RGB Gabor LBP


(a)


100


95


90


85


Accuracy (%)


80


75


70


65


60


0 5 10 15 20 25 30 35 40 45 50


Number of used patches for one board wood species identification


ResNet-50 AlexNet GoogLeNet


## VGG-16


(b)


Figure 16: Dependency between number of subimages and accuracy [10, 13].


Neural network complexity reduction along with optimization [92] seems to be a very perspective approach as well. Nowadays, the mobile device market is on the rise and developers are pushing for compact architectures and eﬀective algorithms. Numerous economical models were introduced in recent years, among them MobileNet [93], ShuﬄeNet [94], and ANTNets [95], which gained great popularity. In comparison to the best performing architectures, mobileoriented models use more than 10 times less parameters, while oﬀering slightly worse performance than the original ones.


To ﬁnd correct learning data, multiple images are fed into CNN-Recurrent Neural Networks (CNN-RNN). Some of the valuable features can be acquired with X-ray [96], mechanical or chemical principle-based wood testers, or even by a 3D camera [97]. In the case of evaluation of “image data,” the most valuable source can be found in X-ray wood probing as well as in 3D scanning of the wood. This can also be used as a reliable diﬀerence between diﬀerent types of knots, which were described in chapters before.


The fusion of multiple diﬀerent data sources has a significant impact on the performance of neural networks or other machine learning algorithms. This method, also called multimodal deep learning, shows an improvement in comparison to the standard deep learning and machine learning implementations [98, 99]. Since the multimodal deep learning depends on the input data of diﬀerent sensors, the normalization of data is practically a necessary step. Normalization can be either manual or based on self-normalizing neural networks [100, 101]. This process is often used for multilateral prediction of moving objects and can be used for wood species classiﬁcation and error detection, as long as there is a


reliable model for data fusion [102]. An example of the proposed method can be seen in Figure 17.


The proposed model can then be pushed to a higher-level hierarchy by decentralization of the system, at the cost of issues with spatial and temporal alignments of the information [103]. Solving this issue might lead to a mesh system type, which can work with diﬀerent information sources, and provides a reliable classiﬁer of defects or wood types. However, the framework for wood classiﬁcation is still not standardized, and formalizations with comparison of multiple DL architectures are not yet done. Also, comparing the naive accuracy of diﬀerent models is not suﬃcient to declare that the certain approach is a strict and precise solution [104].


As diﬀerent types of convolutional neural networks are eﬃcient in various tasks, architecture fusion or combination is advantageous in speciﬁc use cases. For instance, autoencoder-based segmentation of the faulty area in pixel precise localization could be applied only to a speciﬁc selected area, premarked by more suitable object detection models like YOLO or Faster R-CNN. Moreover, fusion of CNN with nonconvolutional types of networks could be beneﬁcial as well. One example is systems combined with noncamera-based sensors. Even though none of the researched wood-related articles covered such solution, the methodology was successfully applied in other ﬁelds like mobile traﬃc classiﬁcation [104] or gearbox fault diagnosis [105].


## 15. Conclusions


Multiple industrial sectors are dependent on reliable wood type classiﬁcation, as it provides analytical information regarding characteristics and features of manufactured


<!-- Page 15 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 15 Journal of Sensors


Central algorithm


Data fusion


n+1 level


Data fusion 1 Data fusion N


Camera 1 Camera N 3D model


Figure 17: Model of possible data fusion for multicamera and multisource wood classiﬁcation.


products (mechanical properties, value, etc.). This approach is typical in the furniture industry or wood panel production. This research summarizes worldwide eﬀorts in wood recognition and quality inspection systems.


Nowadays, the analysis is mostly performed by trained humans. In addition to being slow, it also has a nonuniform accuracy, as the experience and attention of workers can vary signiﬁcantly. Automatization of wood classiﬁcation is crucial for further expansion of the furniture industry and wood panel production. Diﬀerent kinds of wood have diﬀerent quality aspects, properties, or value. Correct wood type classiﬁcation is critical, as it inﬂuences price and features of ﬁnal products. For example, in wood panel production, the quantity of used glue is directly inﬂuenced by the used wood type, as the manufacturer has to guarantee prescribed mechanical properties. However, the amount of glue also inﬂuences the ﬁnal price and has impact on the environment. Another important is the paper industry. The wood type inﬂuences the quantity of cellulose in manufactured paper, thus also inﬂuencing its quality.


Human visual inspection is often slow and inﬂuenced by workers’ fatigue. On the other hand, chemical tests are expensive and can be only carried on a small sample. Other than these two methods, it is impossible to identify the wood type from the wood emitted spectrum. Unfortunately, the interpretation of the wood ﬂuorescence spectrum is not an easily achievable task. In the case of wood type identiﬁcation, even a small diﬀerence in the unique set of spectral peaks is meaningful. Therefore, human identiﬁcation of wood types is not accurate or repeatable. Nowadays, a large quantity of recycled wood is used as a basic material in the wood panel industry. Classiﬁcation of a large quantity of chopped or mixed wood slices is not suitable for human assessment of material quality. A custom system based on accurate automatic identiﬁcation of continuous ﬂow of input data from the feeding line of the manufacturing plant is basically necessary. That is why it is crucial to pursue new sophisticated approaches in the ﬁeld of wood quality classiﬁcation.


Interest in research and development of automatic wood defect detection or classiﬁcation methods is rapidly increasing. Investments in this ﬁeld are signiﬁcate, mainly in wood-rich countries, such as Scandinavia. Nowadays, trained


experts are still used for wooden plank inspections (including freckle, bark, pitch pockets, wane, split stain, or various knot types) or wood quality assessment. Long-term wood inspection might lead to eye fatigue, leading to low eﬃciency and accuracy. New imaging techniques, wood image databases, and sophisticated computer vision techniques have made automatic wood inspections an approachable goal, oﬀering performance exceeding human workers.


Many techniques are currently developed and expanded; however, many challenges are still present and remain to be solved.


Conflicts of Interest


The authors declare that there is no conﬂict of interest regarding the publication of this paper.


Acknowledgments


This article was supported by the Ministry of Education of the Czech Republic (Project No. SP2020/151). This work was supported by the European Regional Development Fund in A Research Platform focused on Industry 4.0 and Robotics in Ostrava project, CZ.02.1.01/0.0/0.0/17_049/0008425 within the Operational Programme Research, Development and Education.


## References


[1] W. Schoch, I. Heller, F. H. Schweingruber, and F. Kienast,


Wood Anatomy of Central European Species, Swiss Federal Institute for Forest, 2004. [2] L. A. Jozsa and G. R. Middleton, A Discussion of Wood Quality


Attributes and Their Practical Implications, Forintek Canada Corporation, 1994. [3] E. Y. L. Lew, Design of an intelligent wood recognition system


for the classiﬁcation of tropical wood species, [Ph. D. thesis], Universiti Teknologi Malaysia, 2005. [4] B. Li, H. Li, Q. Zha, R. Bandekar, A. Alsaggaf, and Y. Ni,


“Eﬀects of wood quality and reﬁning process on TMP pulp and paper quality,” BioResources, vol. 6, no. 3, pp. 3569– 3584, 2011.


<!-- Page 16 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 16 Journal of Sensors


[5] D. Kleinschmit, S. Mansourian, C. Wildburger, and A. Purret,


Illegal Logging and Related Timber Trade: Dimensions, Drivers, Impacts and Responses: A Global Scientiﬁc Rapid Response Assessment Report, International Union of Forest Research Organizations (IUFRO), 2016. [6] R. Yusof, N. R. Rosli, and F. N. A. Bakar, “Non-wood anat


omy image detector for tropical wood recognition system,” in 4th Kuala Lumpur International Agriculture, Forestry & Plantation Conference, pp. 162–168, Kuala Lumpur, Malaysia, 2016. [7] J. Martins, L. S. Oliveira, S. Nisgoski, and R. Sabourin, “A


database for automatic classiﬁcation of forest species,” Machine Vision and Applications, vol. 24, no. 3, pp. 567– 578, 2013. [8] J. Y. Tou, P. Y. Lau, and Y. H. Tay, “Computer vision-based


wood recognition system,” in Proceedings of International Workshop on Advanced Image Technology, pp. 1–6, Bangkok, Thailand, 2007. [9] M. Khalid, E. L. Y. Lee, R. Yusof, and M. Nadaraj, “Design of


an intelligent wood species recognition system,” International Journal of Simulation: Systems, Science and Technology, vol. 9, no. 3, pp. 9–19, 2008. [10] P. L. P. Filho, L. S. Oliveira, S. Nisgoski, and A. S. Britto Jr.,


“Forest species recognition using macroscopic images,” Machine Vision and Applications, vol. 25, no. 4, pp. 1019– 1031, 2014. [11] P. L. de Paula, L. S. Oliveira, and R. S. Alceu de Souza Britto


Jr., “Forest species recognition using color-based features,” in 2010 20th International Conference on Pattern Recognition, pp. 4178–4181, Istanbul, Turkey, August 2010. [12] J. Y. Tou, Y. H. Tay, and P. Y. Lau, “Rotational invariant


wood species recognition through wood species veriﬁcation,,” in 2009 First Asian Conference on Intelligent Information and Database Systems, pp. 115–120, Dong Hoi, Vietnam, April 2009. [13] D. Shustrov, Species Identiﬁcation of Wooden Material Using


Convolutional Neural Networks, Master’s Thesis, 2018. [14] M. Carpentier, P. Giguere, and J. Gaudreault, “Tree species


identiﬁcation from bark images using convolutional neural networks,” in 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 1075–1081, Madrid, Spain, October 2018. [15] P. Salma, H. Gunawan, E. Prakasa et al., “Wood identiﬁcation


on microscopic image with Daubechies wavelet method and local binary pattern,” in 2018 International Conference on Computer, Control, Informatics and its Applications (IC3INA), pp. 23–27, Tangerang, Indonesia, November 2018. [16] J. Y. Tou, Y. H. Tay, and P. Y. Lau, “A comparative study for


texture classiﬁcation techniques on wood species recognition problem,” in 2009 Fifth International Conference on Natural Computation, pp. 8–12, Tianjian, China, August 2009. [17] L. K. Seng and T. Guniawan, “An experimental study on the


use of visual texture for wood identiﬁcation using a novel convolutional neural network layer,” in 2018 8th IEEE International Conference on Control System, Computing and Engineering (ICCSCE)., pp. 156–159, Penang, Malaysia, November 2018. [18] R. Yusof, M. Khalid, and A. S. M. Khairuddin, “Application of


kernel-genetic algorithm as nonlinear feature selection in tropical wood species recognition system,” Computers and Electronics in Agriculture, vol. 93, pp. 68–77, 2013.


[19] A. R. Yadav, M. L. Dewal, R. S. Anand, and S. Gupta, “Classi


ﬁcation of hardwood species using ANN classiﬁer,” in 2013 Fourth National Conference on Computer Vision, Pattern Recognition, Image Processing and Graphics (NCVPRIPG), pp. 1–5, Jodhpur, India, December 2013. [20] M. I.'a. P. Zamri, A. S. M. Khairuddin, N. Mokhtar, and


R. Yusof, “Wood species recognition system based on improved basic grey level aura matrix as feature extractor,” Journal of Robotics, Networking and Artiﬁcial Life, vol. 3, no. 3, p. 140, 2016. [21] M. Nasirzadeh, A. A. Khazael, and M. B. Khalid, “Woods


recognition system based on local binary pattern,” in 2010 2nd International Conference on Computational Intelligence, Communication Systems and Networks, pp. 308–313, Liverpool, UK, July 2010. [22] R. Yusof, N. R. Rosli, and M. Khalid, “Using Gabor ﬁlters as


image multiplier for tropical wood species recognition system,” in 2010 12th International Conference on Computer Modelling and Simulation, pp. 289–294, Cambridge, UK, March 2010. [23] Z.-N. Ke, Q.-J. Zhao, C.-H. Huang, P. Ai, and J.-G. Yi,


“Detection of wood surface defects based on particle swarm-genetic hybrid algorithm,” in 2016 International Conference on Audio, Language and Image Processing (ICALIP), pp. 375–379, Shanghai, China, July 2016. [24] H. S. Kauppinen, Development of a color machine vision


method for wood surface inspection, [Ph.D. thesis], Acta Universitatis Ouluensis, 2001. [25] M. Hongbo, D. Qi, M. Zhang, and L. Yu, “Image edge detec


tion of wood defects based on multi-fractal analysis,” in 2008 IEEE International Conference on Automation and Logistics, pp. 1232–1237, Qingdao, China, September 2008. [26] D. Pham, A. Soroka, A. Ghanbarzadeh, E. Koc, S. Otri, and


M. Packianather, “Optimising neural networks for identiﬁcation of wood defects using the bees algorithm,” in 2006 IEEE International Conference on Industrial Informatics, pp. 1346– 1351, Singapore, Singapore, August 2006. [27] J. Cao, H. Liang, X. Lin, W. Tu, and Y. Zhang, “Potential of


near-infrared spectroscopy to detect defects on the surface of solid wood boards,” BioResources, vol. 12, no. 1, 2016. [28] N. Chen, X. Men, C. Hua, X. Wang, X. Han, and H. Chen,


“Research on edge defects image recognition technology based on artiﬁcial neural network,” in 2018 13th IEEE Conference on Industrial Electronics and Applications (ICIEA), pp. 1929–1933, Wuhan, China, 2018. [29] Y. X. Zhang, Y. Q. Zhao, Y. Liu, L. Q. Jiang, and Z. W. Chen,


“Identiﬁcation of wood defects based on LBP features,” in 2016 35th Chinese Control Conference (CCC), pp. 4202– 4205, Chengdu, China, July 2016. [30] I. Y.-H. Gu, H. Andersson, and R. Vicen, “Wood defect


classiﬁcation based on image analysis and support vector machines,” Wood Science and Technology, vol. 44, no. 4, pp. 693–704, 2010. [31] A. Marcano-Cedeno, J. Quintanilla-Dominguez, and D. Andina, “Wood defects classiﬁcation using artiﬁcial metaplasticity neural network,” in 2009 35th Annual Conference of IEEE Industrial Electronics, pp. 3422–3427, Porto, Portugal, November 2009. [32] F. Yang, Y. Wang, S. Wang, and Y. Cheng, “Wood veneer


defect detection system based on machine vision,” in Proceedings of the 2018 International Symposium on Communication


<!-- Page 17 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 17 Journal of Sensors


Engineering & Computer Science (CECS 2018), pp. 413–418, Hohhot, China, July 2018. [33] G. A. Ruz, P. A. Estévez, and P. A. Ramírez, “Automated


visual inspection system for wood defect classiﬁcation using computational intelligence techniques,” International Journal of Systems Science, vol. 40, no. 2, pp. 163–172, 2009. [34] H. Yu, Y. Liang, H. Liang, and Y. Zhang, “Recognition of


wood surface defects with near infrared spectroscopy and machine vision,” Journal of Forestry Research, vol. 30, no. 6, pp. 2379–2386, 2019. [35] H. Kauppinen, “A two stage defect recognition method for


parquet slab grading,” in Proceedings 15th International Conference on Pattern Recognition. ICPR-2000, pp. 803–806, Barcelona, Spain, September 2000. [36] P. B. Menon, “Structure and identiﬁcation of Malayan


woods,” in Forest Research Institute, Forest Department, 1967. [37] Nature Editorials, “Brazil’s new president adds to global


threat to science,” Nature, vol. 563, no. 7729, pp. 5-6, 2018. [38] L. Tacconi, M. Boscolo, and D. Brack, National and Interna


tional Policies to Control Illegal Forest Activities, Royal Institute of International Aﬀairs, 2003. [39] A. Hoare, Tackling Illegal Logging and the Related Trade:


What Progress and Where Next?, Chatham House Report, 2015. [40] The Forest Law of the People’s Republic of China, 1998. [41] E. Richer, Chinese Furniture Exports Reach All-Time High in


2015, Forest Trends, Washington, DC, USA, 2016. [42] R. Rana, R. Langenfeld-Heyser, R. Finkeldey, and A. Polle,


“Functional anatomy of ﬁve endangered tropical timber wood species of the family Dipterocarpaceae,” Trees, vol. 23, no. 3, pp. 521–529, 2009. [43] S. Carcagno, R. Bucknall, J. Woodhouse, C. Fritz, and C. J.


Plack, “Eﬀect of back wood choice on the perceived quality of steel-string acoustic guitars,” The Journal of the Acoustical Society of America, vol. 144, no. 6, pp. 3533–3547, 2018. [44] W. B. Huang and X. F. Sun, Tropical Hardwood Flows in


China: Case Studies of Rosewood and Okoumé, Forest Trends, Washington, DC, USA, 2013. [45] A. Youatt and T. Cmar, “The ﬁght for red gold: ending illegal


mahogany trade from Peru,” Natural Resources & Environment, vol. 23, p. 19, 2008. [46] R. A. Sollund, Ed., Global Harms: Ecological Crime and Spe


ciesism, ser. Environmental Science, Engineering and Technology, Nova Science Publishers, New York, NY, USA, 2011. [47] R. Yusof, N. R. Rosli, and M. Khalid, “Tropical wood species


recognition based on Gabor ﬁlter,” in 2009 2nd International Congress on Image and Signal Processing, pp. 1–5, Tianjin, China, October 2009. [48] L. G. Hafemann, L. S. Oliveira, and P. Cavalin, “Forest species


recognition using deep convolutional neural networks,” in 2014 22nd International Conference on Pattern Recognition, pp. 1103–1107, Stockholm, Sweden, August 2014. [49] P. Brodatz, Textures: A Photographic Album for Artists and


Designers, Dover Pubns, 1999. [50] J. Y. Tou, Y. H. Tay, and P. Y. Lau, “One-dimensional grey


level co-occurrence matrices for texture classiﬁcation,” in 2008 International Symposium on Information Technology, pp. 1–6, Kuala Lumpur, Malaysia, August 2008. [51] A. Mallik, J. Tarrío-Saavedra, M. Francisco-Fernández, and


S. Naya, “Classiﬁcation of wood micrographs by image seg


mentation,” Chemometrics and Intelligent Laboratory Systems, vol. 107, no. 2, pp. 351–362, 2011. [52] Mohan, “An intelligent recognition system for identiﬁcation


of wood species,” Journal of Computer Science, vol. 10, no. 7, pp. 1231–1237, 2014. [53] J. Berthellemy, “Wooden bridges discussed in a new Setra


guide entitled:" how to ensure their durability",” TravauxParis, no. 839, pp. 90–97, 2007. [54] P. Cavalin, L. S. Oliveira, A. L. Koerich, and A. S. Britto,


“Wood defect detection using grayscale images and an optimized feature set,” in IECON 2006 - 32nd Annual Conference on IEEE Industrial Electronics, pp. 3408–3412, Paris, France, November 2006. [55] R. Ren, T. Hung, and K. C. Tan, “A generic deep-learning


based approach for automated surface inspection,” IEEE Transactions on Cybernetics, vol. 48, no. 3, pp. 929–940, 2018. [56] J. Donahue, Y. Jia, O. Vinyals et al., “DeCAF: a deep convolu


tional activation feature for generic visual recognition,” 2013, https://arxiv.org/abs/1310.1531. [57] A. Urbonas, V. Raudonis, R. Maskeliunas, and R. Damasevicius, “Automated identiﬁcation of wood veneer surface defects using faster region-based convolutional neural network with data augmentation and transfer learning,” Applied Sciences, vol. 9, no. 22, p. 4898, 2019. [58] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN:


towards real-time object detection with region proposal networks,” 2016, https://arxiv.org/abs/1506.01497. [59] P. Dwivedi, “YOLOv5 compared to Faster RCNN. Who


wins?,” 2020, https://towardsdatascience.com/yolov5compared-to-faster-rcnn-who-wins-a771cd6c9fb4. [60] “Ultralytics LLC,” https://www.ultralytics.com. [61] M. Tan, R. Pang, and Q. V. Le, “EﬃcientDet: scalable and eﬃ


cient object detection,” 2020, https://arxiv.org/abs/1911.09070. [62] “Papers with code - COCO test-dev benchmark (object


detection),” https://paperswithcode.com/sota/objectdetection-on-coco. [63] “CNN discriminative localization and saliency - MIT,” http://


cnnlocalization.csail.mit.edu/. [64] S. Tsuchikawa, Y. Hirashima, Y. Sasaki, and K. Ando, “Near


infrared spectroscopic study of the physical and mechanical properties of wood with meso- and micro-scale anatomical observation,” Applied Spectroscopy, vol. 59, no. 1, pp. 86–93, 2016. [65] M. H. Nuopponen, G. M. Birch, R. J. Sykes, S. J. Lee, and


D. Stewart, “Estimation of wood density and chemical composition by means of diﬀuse reﬂectance mid-infrared Fourier transform (DRIFT-MIR) spectroscopy,” Journal of Agricultural and Food Chemistry, vol. 54, no. 1, pp. 34–40, 2006. [66] C. R. Orton, D. Y. Parkinson, P. D. Evans, and N. L. Owen,


“Fourier transform infrared studies of heterogeneity, photodegradation, and lignin/hemicellulose ratios within hardwoods and softwoods,” Applied Spectroscopy, vol. 58, no. 11, pp. 1265–1271, 2016. [67] V. Piuri and F. Scotti, “Design of an automatic wood types


classiﬁcation system by using ﬂuorescence spectra,” IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), vol. 40, no. 3, pp. 358–366, 2010. [68] R. Jordan, F. Feeney, N. Nesbitt, and J. A. Evertsen, “Classiﬁ


cation of wood species by neural network analysis of ultrasonic signals,” Ultrasonics, vol. 36, no. 1-5, pp. 219–222, 1998.


<!-- Page 18 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 18 Journal of Sensors


[69] “GLCM texture feature,” 2019, https://support.echoview


.com/WebHelp/Windows_and_Dialog_Boxes/Dialog_ Boxes/Variable_properties_dialog_box/Operator_pages/ GLCM_Texture_Features.htm#Energy. [70] X. Qin and Y.-H. Yang, “Basic gray level aura matrices: theory


and its application to texture synthesis,” in Tenth IEEE International Conference on Computer Vision (ICCV'05) Volume 1, pp. 128–135, Beijing, China, October 2005. [71] I. M. Elfadel and R. W. Picard, “Gibbs random ﬁelds,


cooccurrences, and texture modeling,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 16, no. 1, pp. 24–37, 1994. [72] X. Qin and Y.-H. Yang, “Similarity measure and learning


with gray level aura matrices (GLAM) for texture image retrieval,” in Proceedings of the 2004 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2004. CVPR 2004, pp. 326–333, Washington, DC, USA, 2004. [73] M. I.’a. P. Zamri, F. Cordova, A. S. M. Khairuddin,


N. Mokhtar, and R. Yusof, “Tree species classiﬁcation based on image analysis using improved-basic gray level aura matrix,” Computers and Electronics in Agriculture, vol. 124, pp. 227–233, 2016. [74] M. Heikkilä, M. Pietikäinen, and C. Schmid, “Description of


interest regions with local binary patterns,” Pattern Recognition, vol. 42, no. 3, pp. 425–436, 2009. [75] S. Nagaraja, C. J. Prabhakar, and P. P. Kumar, “Complete


local binary pattern for representation of facial expression based on curvelet transform,” in International Conference on Multimedia Processing, Communication and Information Technology (MPCIT), pp. 48–56, Shimoga, India, December 2013. [76] J. A. K. Suykens and J. Vandewalle, “Least squares support


vector machine classiﬁers,” Neural Processing Letters, vol. 9, no. 3, pp. 293–300, 1999. [77] R. P. Cogdill, L. R. Schimleck, P. D. Jones, G. F. Peter, R. F.


Daniels, and A. Clark III, “Estimation of the physical wood properties ofPinus TaedaL. radial strips using least squares support vector machines,” Journal of Near Infrared Spectroscopy, vol. 12, no. 4, pp. 263–269, 2017. [78] H. Wang and D. Hu, “Comparison of SVM and LS-SVM


for regression,” in 2005 International Conference on Neural Networks and Brain, pp. 279–283, Beijing, China, October 2005. [79] J. Ye, R. Janardan, and Q. Li, “Two-dimensional linear


discriminant analysis,” in Advances in neural information processing systems, pp. 1569–1576, Vancouver, Canada, December 2005. [80] P. Kodytek, Neural Networks, 2019, http://education


.pkodytek.com/artiﬁcial-intelligence/12_neural_network/. [81] I. Cetiner, “Classiﬁcation using artiﬁcial neural network of


knot images on wood,” Journal of New Results in Science, vol. 5, pp. 264–271, 2016. [82] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE


Transactions on Knowledge and Data Engineering, vol. 22, no. 10, pp. 1345–1359, 2010. [83] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet


classiﬁcation with deep convolutional neural networks,” in Advances in Neural Information Processing Systems 25 (NIPS 2012), pp. 1097–1105, Nevada, USA, 2012. [84] “YOLO: real-time object detection,” https://pjreddie.com/


darknet/yolo/.


[85] D. Ciuonzo, A. De Maio, and P. Salvo Rossi, “A systematic


framework for composite hypothesis testing of independent Bernoulli trials,” IEEE Signal Processing Letters, vol. 22, no. 9, pp. 1249–1253, 2015. [86] A. Goel, A. Patel, K. G. Nagananda, and P. K. Varshney,


“Robustness of the counting rule for distributed detection in wireless sensor networks,” IEEE Signal Processing Letters, vol. 25, no. 8, pp. 1191–1195, 2018. [87] Y. LeCun, L. Bottou, Y. Bengio, and P. Haﬀner, “Gradient


based learning applied to document recognition,” Proceedings of the IEEE, vol. 86, no. 11, pp. 2278–2324, 1998. [88] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning


for image recognition,” in 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 770–778, Las Vegas, NV, USA, 2016. [89] K. Simonyan and A. Zisserman, “Very deep convolutional


networks for large-scale image recognition,” 2014, https:// arxiv.org/abs/1409.1556. [90] “CIFAR-10 and CIFAR-100 datasets,,” 2010, https://www.cs


.toronto.edu/~kriz/cifar.html. [91] P. Y. Simard, S. Amershi, D. M. Chickering et al., “Machine


teaching: a new paradigm for building machine learning systems,” 2017, https://arxiv.org/abs/1707.06742. [92] T. Sinha, B. Verma, and A. Haidar, “Optimization of convo


lutional neural network parameters for image classiﬁcation,” in 2017 IEEE Symposium Series on Computational Intelligence (SSCI), pp. 1–7, Honolulu, HI, USA, 2017. [93] A. G. Howard, M. Zhu, B. Chen et al., “MobileNets: eﬃcient


convolutional neural networks for mobile vision applications,” 2017, https://arxiv.org/abs/1704.04861. [94] X. Zhang, X. Zhou, M. Lin, and J. Sun, “ShuﬄeNet: an


extremely eﬃcient convolutional neural network for mobile devices,” in 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 6848–6856, Salt Lake City, UT, USA, 2018. [95] Y. Xiong, H. J. Kim, and V. Hedau, “ANTNets: mobile convo


lutional neural networks for resource eﬃcient image classiﬁcation,” 2019, https://arxiv.org/abs/1904.03775. [96] X. Xiao, A multiple sensors approach to wood defect detection,


[Ph. D. thesis], Virginia Tech, 1998. [97] A. Sioma, “Assessment of wood surface defects based on 3d


image analysis,” Wood Research, vol. 60, no. 3, pp. 339–350, 2015. [98] G. Aceto, D. Ciuonzo, A. Montieri, and A. Pescapè,


“MIMETIC: mobile encrypted traﬃc classiﬁcation using multimodal deep learning,” Computer Networks, vol. 165, article 106944, 2019. [99] J. Ngiam, A. Khosla, M. Kim, J. Nam, H. Lee, and A. Y. Ng,


“Multimodal deep learning,” in Proceedings of the 28th International Conference on International Conference on Machine Learning, pp. 689–696, Washington, USA, 2011. [100] T. Salimans and D. P. Kingma, “Weight normalization: a sim


ple reparameterization to accelerate training of deep neural networks,” Advances in Neural Information Processing Systems, pp. 901–909, 2016. [101] G. Klambauer, T. Unterthiner, A. Mayr, and S. Hochreiter,


“Self-normalizing neural networks,” Advances in Neural Information Processing Systems, pp. 971–980, 2017. [102] W. Du and J. Piater, “Data fusion by belief propagation for


multi-camera tracking,” in 2006 9th International Conference on Information Fusion, pp. 1–8, Florence, Italy, July 2006.


<!-- Page 19 -->


9161, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/3217126 by Cochrane Peru, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 19 Journal of Sensors


[103] F. Castanedo, “A review of data fusion techniques,” Scientiﬁc


World Journal, vol. 2013, pp. 1–19, 2013. [104] G. Aceto, D. Ciuonzo, A. Montieri, and A. Pescapé, “Toward


eﬀective mobile encrypted traﬃc classiﬁcation through deep learning,” Neurocomputing, vol. 409, pp. 306–315, 2020. [105] L. Jing, T. Wang, M. Zhao, and P. Wang, “An adaptive


multi-sensor data fusion method based on deep convolutional neural networks for fault diagnosis of planetary gearbox,” Sensors, vol. 17, no. 2, p. 414, 2017.
