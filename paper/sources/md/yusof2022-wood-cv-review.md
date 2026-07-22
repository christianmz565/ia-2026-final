# yusof2022-wood-cv-review


<!-- Page 1 -->


Review Computer Vision-Based Wood Identiﬁcation: A Review


José Luís Silva 1,* , Rui Bordalo 1, José Pissarra 2 and Paloma de Palacios 3


1 Research Center for the Science and Technology of the Arts, School of Arts, Universidade Católica Portuguesa, 4169-005 Porto, Portugal 2 Green UPorto and Department of Biology, Faculty of Sciences, University of Porto, 4169-005 Porto, Portugal 3 Department of Natural Systems and Resources, School of Forestry and Natural Environment Engineering, Universidad Politécnica de Madrid, 28040 Madrid, Spain * Correspondence: jlamorimdasilva@gmail.com


Abstract: Wood identiﬁcation is an important tool in many areas, from biology to cultural heritage. In the ﬁght against illegal logging, it has a more necessary and impactful application. Identifying a wood sample to genus or species level is difﬁcult, expensive and time-consuming, even when using the most recent methods, resulting in a growing need for a readily accessible and ﬁeld-applicable method for scientiﬁc wood identiﬁcation. Providing fast results and ease of use, computer visionbased technology is an economically accessible option currently applied to meet the demand for automated wood identiﬁcation. However, despite the promising characteristics and accurate results of this method, it remains a niche research area in wood sciences and is little known in other ﬁelds of application such as cultural heritage. To share the results and applicability of computer vision-based wood identiﬁcation, this paper reviews the most frequently cited and relevant published research based on computer vision and machine learning techniques, aiming to facilitate and promote the use of this technology in research and encourage its application among end-users who need quick and reliable results.


Keywords: computer vision; machine learning; deep learning; convolutional neural networks; image recognition; wood anatomy; wood identiﬁcation; illegal logging


Citation: Silva, J.L.; Bordalo, R.;


Pissarra, J.; de Palacios, P. Computer


Vision-Based Wood Identiﬁcation: A


Review. Forests 2022, 13, 2041.


## 1. Introduction


https://doi.org/10.3390/f13122041


Illegal logging is one of the most pressing environmental issues, particularly in tropical countries with large forest areas and botanical groups that are highly valued in international markets. Illegal logging is currently the most proﬁtable ecological crime worldwide, accounting for 10 to 30% of the global timber trade [1,2].


Academic Editors: Christian Brischke


and Cristina Nabais


Received: 21 October 2022


Although Amazonian forests are traditionally seen as the hotspot of illegal logging, areas such as Southeast Asia, Central Africa and Russia, home to roughly 60% of the world’s forests, are unfortunately experiencing a surge in this crime [1,3]. The ﬁnancial impact of illegal logging is estimated at 52 to 157 billion dollars a year [1], but, more importantly, the environmental damage, in many cases irreversible, can also have a global ecological impact [4].


Accepted: 29 November 2022


Published: 30 November 2022


Publisher’s Note: MDPI stays neutral


with regard to jurisdictional claims in


published maps and institutional afﬁl


iations.


Several institutional and international legal measures have been put in place to prevent overexploitation and irreversible loss of species and habitats [5–7]. Innovative programmes are emerging [8,9], solid research is under way [10–14], and research with signiﬁcant impact and news items are being shared worldwide [15].


Copyright: © 2022 by the authors.


The impact of wood identiﬁcation extends beyond illegal trading and ecological issues. Wood identiﬁcation is paramount for the timber industry, civil and structural engineering, criminology, archaeology, art history, ethnography, and conservation and restoration, and many other disciplines.


Licensee MDPI, Basel, Switzerland.


This article is an open access article


distributed under the terms and


conditions of the Creative Commons


Despite the multiple wood identiﬁcation methods now available, the varied results, costs, accessibility, deployment time and limiting factors hinder their applicability to realworld identiﬁcation. This paper presents an overview of the changes that have occurred in


Attribution (CC BY) license (https://


creativecommons.org/licenses/by/


4.0/).


Forests 2022, 13, 2041. https://doi.org/10.3390/f13122041 https://www.mdpi.com/journal/forests


<!-- Page 2 -->


Forests 2022, 13, 2041 2 of 26


wood identiﬁcation methods and a review of computer vision-based wood identiﬁcation, which is currently one of the fastest developing research areas in artiﬁcial intelligence (AI) with very promising results and high identiﬁcation accuracy. In this technique, visual data are processed from any given image to extract the relevant features in order to make a decision.


Analogic and Digital Systems


Historically, wood identiﬁcation methods mainly comprised the study of chemical and physical and anatomical features aspects of wood. Methods such as macroscopy, which uses the physical characteristics of wood observable to the naked eye or with a 10× hand lens, and microscopy, which resorts to light compound microscopes to the observation of multiple cell typologies that constitute the wood, were the ﬁrst to be used. The main limitation of these methods is that wood cannot always be identiﬁed at the species level. As a result, there has been an emergence of multiple techniques such as near-infrared spectroscopy [16–18], DNA barcoding [19–21], mass spectrometry [22–24], and X-ray tomography [25–27], with optical microscopy still used as a conﬁrmation method for the results of these techniques.


However, an important contribution was made with the advent of computer-based technologies, which rapidly became a preferred option for constructing species databases and hosting identiﬁcation tools. Several wood identiﬁcation databases and software based on digital technology have been made available, including GUESS [28,29], CSIROID [30] and the DELTA system [31], three of the most signiﬁcant early programmes in achieving the goal of wood identiﬁcation. As a proof of concept, the importance of these systems was fundamental for the development of what is today deﬁned as computer-assisted wood identiﬁcation. The results they obtained made considerable progress compared to earlier methods, especially with regard to the time required and identiﬁcation accuracy. The DELTA-Intkey for commercial timbers is the only one of these three systems still in use.


## 2. Online Reference Databases for Wood Identiﬁcation


This section brieﬂy describes all the digital reference databases available online, to the best of our knowledge. The common objective of online identiﬁcation keys is to enable and facilitate analysis of wood anatomical features and, ultimately, identiﬁcation of the wood. Table 1 summarises the computer-assisted wood identiﬁcation systems mentioned above.


2.1. Commercial Timbers: Descriptions, Illustrations, Identiﬁcation and Information Retrieval


Among the several DELTA-INTKEY online identiﬁcation keys that have been developed, including CITESwoodID and Softwoods, this interactive identiﬁcation key developed in 2000 and updated in 2018–2019 is an integrated database of microscopic descriptions and illustrations of 409 internationally traded hardwood taxa [32]. It covers major forest regions of the world and is freely available online.


## 2.2. Anatomy of European and North American Woods


Created in 2000, this system includes 426 wood taxa [33] and provides an interactive identiﬁcation key for the common non-commercial wood species of Europe and North America. It includes 325 hardwood species and 101 softwood species (native and introduced) with 145 features and 15 sets. It has two extra sets that isolate the features applicable to identiﬁcation of modiﬁed and carbonised wood from palaeobotanical contexts. A useful feature, which is missing from the commercial timbers key, is a set that isolates the features extracted from the IAWA standards.


<!-- Page 3 -->


Forests 2022, 13, 2041 3 of 26


Table 1. Summary of computer-assisted wood identiﬁcation systems.


Year Name Taxa Area Identiﬁcation Number of


## 2000 Commercial timbers: descriptions,


404 hardwoods Major forest regions of the


Images Access Comments Reference


Microscopic descriptions


illustrations, identiﬁcation, and


and illustrations n.a. Freely available - [32]


information retrieval


world


Europe


## 2000 Anatomy of European and North


325 hardwoods 101 softwoods


Includes features adapted to identiﬁcation of carbonised woods


Microscopic descriptions


and North America


and illustrations n.a. Freely available


American Woods


## 2003 Wood database of the Forestry and


[33]


from archaeological contexts


Forest Products Research Institute 781 Japan Microscopic descriptions


and illustrations n.a. Freely available - [34]


7653 modern hardwoods; 235 modern softwoods;


58,146 modern hardwoods;


3807 fossil hardwoods; 1482 modern softwoods


Global Microscopic descriptions


## 2004 InsideWood


Freely available Includes 61,578 searchable images [35]


and illustrations


2173 fossil hardwoods


Includes macroscopic and


133 hardwoods and softwoods Europe Microscopic descriptions


## 2004 Wood anatomy of central European


and illustrations n.a. Freely available


species


## 44 CITES woods; 31 look-a-like species


Speciﬁc forest regions of the


microscopic images and


[36]


descriptions


Macroscopic descriptions


and illustrations n.a. Freely available Includes abundant extra


## 2005 CITESwoodID


world


## 2005 Key to a Selection of Arid Australian Hardwoods and


information [37]


58 hardwoods and softwoods Australia Microscopic descriptions


and illustrations n.a. Freely available Detailed information about each


Softwoods


species [38]


2010 Brazilian Commercial Timbers 275 species Brazil Macroscopic features; chemical and physical tests n.a. Freely available - [39]


## 2011 Pl@ntwood 110 hardwoods Amazonia Microscopic descriptions


and illustrations n.a. - - [40]


## 2013 Forest Species Database—Microscopic


112 hardwoods and softwoods Tropical forests Microscopic descriptions


and illustrations 2240 Freely available Includes 2240 searchable


microscopic images [41,42]


<!-- Page 4 -->


Forests 2022, 13, 2041 4 of 26


Table 1. Cont.


Year Name Taxa Area Identiﬁcation Number of


## 2014 Forest Species Database—Macroscopic


Images Access Comments Reference


41 hardwoods and softwoods Brazil Macroscopic descriptions


and illustrations 2942 Freely available Includes 2942 searchable


macroscopic images [43,44]


## 2016 MacroHOLZdata 150 hardwoods and softwoods Global Macroscopic descriptions


and illustrations n.a. Free of charge on


112 hardwoods and softwoods


Available in English, German and


Spanish [45]


request


Macroscopic and microscopic illustrations 5182 Freely available


- [46] 41 hardwoods and softwoods Freely available


## 2018 Forest Species Classiﬁer


Brazil


2018 Charcoal 44 hardwoods Brazil Microscopic features 528 Available for research only - [47]


## 2019 Charkey 507 hardwoods and softwoods French Guiana


n.a. Freely available Highly detailed SEM images [48]


Microscopic descriptions


and illustrations


n.a. Softwood Retrieval System for


Coniferous Wood 180 softwoods China ≥1000 n.a. Under development [49]


2021 UTForest—UTFPR Classiﬁcador 44 hardwoods and softwoods Brazil Macroscopic descriptions 1318 Freely available - [50]


Under develop


Mader app n.a. n.a. Microscopic features 26,000 n.a. Database with 1000 images per


ment


n.a.—not available.


species [51]


<!-- Page 5 -->


Forests 2022, 13, 2041 5 of 26


## 2.3. Wood Database of the Forestry and Forest Products Research Institute


This online database created in 2003 focuses on the identiﬁcation of 781 Japanese tree species, substantiating the descriptions on the IAWA list of hardwood features [52]. It includes a multiple-entry key and an image database and is freely available online [34].


## 2.4. InsideWood


Developed in 2004, InsideWood is by far the largest and best-known online identiﬁcation key [35]. It is a multiple access key based on the IAWA hardwood list [52] and is freely available online. It includes keys for hardwoods, softwoods and fossil hardwoods, and more than 10,030 microscopic anatomic descriptions covering all regions of the world, with more than 63,435 searchable images. It is a centralised database that integrates all the anatomical data available for modern wood.


## 2.5. Wood Anatomy of Central European Species


This is a completely revised and updated version of Schweingruber’s work [53], created in 2004 [36] and last updated in 2007. It is a web-based identiﬁcation key with 133 species, accompanied by macroscopic and microscopic descriptions. It also provides information such as sample preparation, staining and other procedures, and is freely available online.


## 2.6. CITESwoodID


CITES (Convention on International Trade in Endangered Species of Wild Fauna and Flora) [54] is an agreement that was drawn up in 1963 after a meeting of members of IUCN (The World Conservation Union). One of many initiatives intended to contribute to the goals of the agreement, CITESwoodID was developed in 2005 [37] and last updated in 2017. As the name indicates, the platform focuses on CITES species and is an interactive identiﬁcation key of macroscopic descriptions with an integrated database. It includes illustrations of 44 CITES protected woods and 31 look-a-like trade species. It provides comprehensive, detailed information about each species, with advice on how to avoid misinterpretations, and numerous explanatory notes of the relevant features and procedures for description and identiﬁcation. It is freely available online.


## 2.7. Key to a Selection of Arid Australian Hardwoods and Softwoods


Stemming from doctoral research [38], this interactive key focuses on Australian woods. It is hosted on the Lucid website and includes 58 wood-producing species of arid Australia, particularly non-commercial species. It is mostly based on specimens from northeast South Australia, southwest Queensland and far western New South Wales and is freely available online.


## 2.8. Brazilian Commercial Timbers—Interactive Wood Identiﬁcation Key


As the name suggests, this is an interactive identiﬁcation system focusing on Brazilian species. Made available in 2010 [39], it was developed in collaboration with the Forest Products Laboratory (LPF) and the Brazilian Forest Service (SFB). It is hosted on the Lucid website and includes 275 species, among them Brazilian CITES-listed timber species. All the nomenclature was revised in 2020 according to the Brazilian Flora Species List. The key works by analysing macroscopic features and chemical and physical tests on the woods. It is freely available online.


## 2.9. Pl@ntwood


Pl@ntwood [40] was developed in 2011 and is described by the authors as an interactive graphical identiﬁcation tool based on the IDAO system, speciﬁcally designed to be user friendly. It comprises 110 Amazonian tree species belonging to 34 angiosperm families and includes microscopic morphological features.


<!-- Page 6 -->


Forests 2022, 13, 2041 6 of 26


## 2.10. The Forest Species Database—Microscopy (FSDM)


Created in 2013, this online database [41,42] comprises 2240 microscopic images of 112 species, 85 genera and 30 families of both hardwoods and softwoods. It is freely available online.


## 2.11. The Forest Species Database—Macroscopy (FSDM)


This online database for forest species identiﬁcation [43,44] was made available in 2014. It includes 2942 macroscopic images of 41 Brazilian forest species and is freely available online.


## 2.12. MacroHOLZdata


MacroHOLZdata [45], created in 2002 and made available for the ﬁrst time in 2016, is another interactive identiﬁcation key with an integrated database for macroscopic wood descriptions. Completely redesigned in 2022, it is available in German, English and Spanish, and includes 150 common hardwood and softwood commercial timbers. The database is free of charge.


## 2.13. Forest Species Classiﬁer


Made available in 2018, Forest Species Classiﬁer is the result of a master’s degree [46]. It is a user-friendly online database focusing on Brazilian forest species. It uses macroscopic [43] and microscopic [41] databases and includes microscopic images of 112 species and macroscopic images of 41 species, with a total of 5182 images. It is freely available online.


## 2.14. UTForest—UTFPR Classiﬁcador


This new version of the Forest Species Classiﬁer platform [50] has been available since 2021. It allows macroscopic identiﬁcation of 44 native species of Brazil and includes 1318 images.


## 2.15. Charcoal


Developed in 2018, this database comprises charcoal samples of 44 Brazilian hardwood forest species, using 528 images [47,55]. It is available for research purposes only.


## 2.16. CharKey


This 2019 electronic identiﬁcation key is described by the authors [48] as the ﬁrst computer-aided identiﬁcation key designed for charcoals from French Guiana. It uses SEM photographs to illustrate the anatomical features of 507 species belonging to 274 genera and 71 families. Most of the descriptions were taken from Détienne et al. [56], and follow the IAWA list of microscopic features for hardwood identiﬁcation [52]. The key contains 289 “items”, and its main aim is to identify specimens to the genus level. It is freely available online.


## 2.17. Softwood Retrieval System (SRS) for Coniferous Wood


The Softwood Retrieval System (SRS) for Coniferous Wood [49] is an online identiﬁcation key with descriptions and micrographs of 180 Chinese coniferous wood species (155 species with descriptions and microphotographs and 25 species with only microphotographs) from nine families and more than 1000 images showing anatomical details. The system is searchable by an interactive multiple-entry key. The microphotographs were collected from slices of 115 coniferous species provided by the Wood Collection of the Chinese Academy of Forestry (Beijing, CAFw) and 40 coniferous species from the Herbarium of Southwest Forestry University (Kunming, SWFUw). The descriptions use features from the IAWA List of Microscopic Features for Softwood Identiﬁcation [57]. The system supports three retrieval methods for coniferous wood retrieval: species name, anatomical characteristics, and microscopic anatomical images (in test).


<!-- Page 7 -->


Forests 2022, 13, 2041 7 of 26


## 2.18. Mader App


This mobile app is under development. Its goal is to contribute to the global wood identiﬁcation effort and the ﬁght against illegal logging using AI [51]. The project comprises 26 species, with a vast image database of 1000 images per species, aiming to obtain maximum intraspeciﬁc variability for each species. The images were taken using a portable microscope and the app aims to obtain real-time recognition of samples. Preliminary data from the authors indicate that accuracy is 95%. The authors intend to make the app available soon on the Play Store, and the database used will be freely available for neural network training [51].


## 3. Computer Vision-Based Wood Identiﬁcation


The digital systems described above are the foundation of the systems which, despite their limitations, are currently used to identify wood, mostly based on computer vision technology. They are applicable to several ﬁelds of research and industry, including neurobiology, autonomous vehicles, and facial recognition. Computer vision systems process visual data from any given image or video to extract the required and relevant features to make a decision [58].


This image recognition ability, also known as image classiﬁcation, is one of the most important research areas in AI and is most frequently based on supervised learning. In this case, the network is required to create a model that learns from labelled images to determine classiﬁcation rules, then it classiﬁes the input data based on these same rules (generally used for image classiﬁcation). In the case of unsupervised learning, it is the model that obtains unknown information through unlabelled data (generally used for image clustering) [59].


Machine learning can also decide what to do without human assistance from the data recognised by computer vision (input data), using predesigned algorithms [60,61]. This removes the need to teach the model the necessary features or procedures for wood identiﬁcation [62].


Computer vision technology is very appealing to many researchers because of its veriﬁable potential for ﬁeld application [63] and proven ability to recognise and quantify wood structure variations that are not easily discernible using strictly “human” analysis. It is also an affordable resource [64] and, therefore, scalable. However, for the software to correctly interpret the speciﬁc architecture structure of the samples analysed to such a high level of precision, reference material must be constantly entered into the image database so that it can recognise natural variations in wood structure [12].


Computer vision-based wood identiﬁcation is the real-world application of combining two types of software with different approaches within AI [65,66].


Figure 1 shows a pipeline of this method.


Figure 1. General scheme of machine learning method for image classiﬁcation (based on [62,67]).


## 3.1. Machine Learning


Machine learning operates primarily as software that recognises patterns from input images that are processed to deﬁne a descriptive structure to which the unknown image will be referenced [68]. This involves various stages, as follows.


<!-- Page 8 -->


Forests 2022, 13, 2041 8 of 26


## 3.2. Image Acquisition


The most frequently used types of image are macroscopic images (obtained without magniﬁcation using a normal digital camera) [69–72], stereograms (stereoscopic images obtained with hand lens magniﬁcation, ca. 10×) [65,66,73–75], micrographs (optical microscopic images) [76–78], SEM images (up to 10,000×) [79], and X-ray computed tomography (CT) images [26,80].


Light control and uniformity are signiﬁcant issues in image processing [66,81,82]. They include techniques that are used to ﬁlter and normalise image brightness [83–85].


## 3.3. Image Datasets


Image dataset construction or availability is one of the most signiﬁcant factors among the multiple issues that can affect the performance of computer vision-based wood identiﬁcation systems.


The more extensive the dataset is, the more naturally occurring biological variations within a species will be accessed and learned by the model. However, because constructing a dataset of wood samples is such a difﬁcult and time-consuming task, most studies use wood collections for references [41,69,74,81,86–89].


This limitation is countered to some extent by initiatives such as ImageNet [90]. Aiming to advance computer vision and deep learning research, the ImageNet dataset was made freely available to researchers worldwide. It contains 14.2 million images across more than 20,000 classes. A similar process is under way with herbaria digitalisation [91–93]. However, despite the efforts made [42,78,87,94,95], the lack of free access to worldwide wood image datasets continues to be the main constraint for computer vision-based wood identiﬁcation [62].


Table 2 shows the main currently available datasets that have useful data for computer vision-based wood identiﬁcation research.


Table 2. Wood image datasets available for computer vision-based wood identiﬁcation research, adapted from [62].


Dataset Description Image Type Number of


CAIRO Commercial hardwood species of Malaysia


Number of


Images Accessibility Reference


Species


37 3700


[96]


## FRIM 52 5200 [97]


Inaccessible


Stereo


LignoIndo Commercial hardwood species of Indonesia 809 4854 [98]


ZAFU WS 24 Wood species at Zhejiang A&F University 24 480 [75]


RMCA Commercial wood species of Central Africa


77 1221


[78]


Micro


XDD Major Fagaceae species of Japan 18 2449 [87]


Lauraceae species of East Asia 39 1658 [94]


WOOD-AUTH Wood species of Greece


## UFPR


Wood species of Brazil


Open


12 4272 [95]


Macro


41 2942 [44]


UFPR Micro 112 2240 [42]


## 3.4. Image Processing


Machine learning comprises two independent procedures: feature processing, also known as extraction (extraction of relevant features from input images), and classiﬁcation (learning extracted features and querying image classiﬁcation). There is, however, a previous step to image processing.


Pre-processing aims to convert the image into data that a speciﬁc algorithm can use to extract the required features, thus reducing computational complexity and facilitating subsequent processing [99]. The techniques used for this include greyscale conversion and image cropping [71,74,78,88,100,101], ﬁltering [83,85], image sharpening [74,102] and denoising [79,103,104].


<!-- Page 9 -->


Forests 2022, 13, 2041 9 of 26


Another important pre-processing procedure is data splitting, where the dataset is split into subsets, most commonly training, validation, and test sets. Data splitting is ultimately used to create a training set, a validation set and a test set in order to later evaluate the model performance. To understand the reasons for these sets, one should think that machine learning systems mimic the human learning process based on examples. From this training set, the system will learn to generalise in order to correctly classify the images. The validation set is used to avoid the system learning the images “from memory” during this generalization process. Finally, the test set is used to check the reliability of the learning process. The use of these distinct data samples is one of the earliest pre-processing steps needed to evaluate any model’s performance.


More speciﬁcally, the system will interpret the images extracted from the designated training set as nothing more than a combination of pixels. Each pixel will have a speciﬁc intensity represented by a number, and in this way a matrix of numbers is formed. Image processing is based on extracting elements such as points, blobs, angles, corners and edges, and the patterns they form. Variability in the anatomy of each wood species is represented as patterns of distinct pixel intensities, arrangement, distribution, and aggregation. The variations detected by computer vision will be learned by machine learning. This process is the fundamental operating system of computer vision for all applications, including wood identiﬁcation [62].


After the extracted features have been learned, a classiﬁcation model is established by a classiﬁer and a test set is formed to evaluate the system’s learning. The images are then input, allowing the classiﬁcation model to complete the identiﬁcation through feedback of the predicted classes of each image [62].


Computer vision detects and “sees” the input image using multiple feature extraction algorithms, while machine learning selects the types of features to be extracted, in most cases texture and local features.


Texture features work with the combination and arrangement of image elements (pixel intensities and resulting patterns) [65,74,96,102,105]. The most frequently used techniques are grey level co-occurrence matrix (GLCM), grey level aura matrix (GLAM), local binary pattern (LBP), higher local order autocorrelation (HLAC), and Gabor ﬁlter-based features (GFBF). Despite the individual capabilities of each technique, texture fusion of different types of texture features has shown superior classiﬁcation accuracy [101,106,107].


Local features differ from texture features by not describing an image as a unit, but by describing signiﬁcant and important speciﬁc features (keypoints) such as edges, corners or points. The most frequently used algorithms are scale-invariant feature transform (SIFT), speeded up robust features (SURF), oriented features-from-accelerated-segment-test (FAST) and rotated binary-robust-independent-elementary-feature (BRIEF) (ORB), and Accelerated-KAZE (AKAZE).


Beyond features typology, factors such as dimensionality reduction and feature selection are also important, as a large number of features extracted from an image can substantially reduce the computational efﬁciency of classiﬁcation models. To achieve this balance, methods such as R AutoEncoder [108], principal component analysis (PCA), linear discriminant analysis (LDA), and genetic algorithms (GA) are used for dimension reduction of data sets [109].


Another important element is the classiﬁcation models created to learn the extracted features and establish classiﬁcation rules. The most frequently used classiﬁers are knearest neighbours (k-NN), support vector machines (SVM), and artiﬁcial neural networks (ANN) [110,111]. These classiﬁcation procedures can be executed either in on-site hardware [112] or on a cloud-based interface [89].


Machines can be easily misled by factors such as the source of images, which can be acquired in the field using mobile phones [89] or in a laboratory-controlled environment [70,113], and variables including different thicknesses, orientation, staining, digital artefacts and other variations, which is why many thin sections from historical wood collections are useful only to the trained human eye [10].


<!-- Page 10 -->


Forests 2022, 13, 2041 10 of 26


## 4. Deep Learning


Deep learning is among the most notable and promising of the many branches of machine learning research.


As a neural network that attempts to simulate the function, structure and behaviour of the human brain (Figure 2), it has the capacity to process and “learn” large amounts of data [114,115].


Figure 2. General pipeline of deep learning models for image classiﬁcation (based on [62,67]).


Its multiple different architectures include ANN [116], deep neural networks (DNN) [117], recurrent neural networks (RNN) [118], deep reinforcement learning (DRL) [119], and convolutional neural networks (CNN) [120]. The fields to which these have been applied are so vast that they are very difﬁcult to summarise, but they include computer vision [121], forensic research [122], climate science [123], machine translation [124], classic literature [125] and bioinformatics [126], to name just a few.


Among these multiple architectures, it is mostly ANNs and CNNs that are applied to wood characterisation and identiﬁcation.


Table 3 summarises this research and the applications of deep learning technologies.


## 4.1. Artiﬁcial Neural Networks (ANN)


Artificial neural networks are not only one of the main investigation methods, but also constitute the foundation of deep learning [62]. These mathematical structures inspired by biological neural networks are a form of supervised or unsupervised learning that show high ability to learn from examples given to them and extrapolate the information when applied to future non-identified samples. This ability to reproduce, model and “learn” nonlinear processes has given ANNs widespread applications in multiple disciplines [78,116].


<!-- Page 11 -->


Forests 2022, 13, 2041 11 of 26


Table 3. Research and applications of deep learning technologies.


Species Geographic


Anatomically


Image


Section


Number of Species


Number of


Reference Database


Similar Species


Type


Type


Images


Origin


Transverse Tangential


[127] Samples from natural forests


Canary Islands


Biometric


Image Analysis


PreProcessing


Features Descriptor Classiﬁers CNN Model Classiﬁcation


Accuracy


Program


Images


Feedforward multilayer perceptron


## 2 Yes n.a. WinCell PCA n.a.


(Spain)


data


Radial


n.a. 92.0%


network


Hardwoods vs.


softwoods (LOOCV) 89%,


[79] No speciﬁc source Global SEM Transverse 7 No 101 n.a. LDA GLCM Multiple classiﬁcation


Transverse Tangential


[128] Samples from natural forests Turkey Micro


## (EVT) 93%.


methods


7 species (LOOCV) 81%, (EVT)


80%.


SVM with linear kernel


## 3 Yes n.a. n.a. n.a. n.a.


Radial


n.a. 95.2%


function


[77] LWA-UFP Brazil Micro n.a. 112 No 2240 n.a. n.a. GLCM


Macro


## 41 No 2050


[129] LWA-UFP Brazil


Transverse


Micro 112 No 2240


SVM


LBP n.a. SVM—98.6%


LBP


## LBP—86%


LBP


GF CLBP Colour-based


SVM


95.77%


features


n.a. n.a.


3-ConvNeta


## LBP GLCM


## SVM 97.32%


## LPQ LPQ + GLCM


Texture


Two-level divide-and-conquer n.a. 97.77%


[71] LWA-UFP Brazil Macro Transverse 41 No 2942 n.a. n.a.


Transverse Tangential


[130] Samples from natural forests Iberian Peninsula Biometric


fusion strategy


Resilient backpropaga


Feedforward multilayer perceptron


## 2 Yes n.a. WinCell n.a.


data


Radial


[131] Samples from the


n.a. 81.2%


tion algorithm


network


timber industry Korea Macro Transverse 5 Yes 33.730 n.a. n.a. n.a. n.a. LeNet3 99.3%


Democratic Republic of the


## [78] TXWD-RMCA


Micro Transverse 77 No 1221


Congo


CellB (version


LPQ


LDA


88% species level 89% genus level 90% family level


LBP


GSC


n.a.


3.2, Olympus)


LDA


KNN


<!-- Page 12 -->


Forests 2022, 13, 2041 12 of 26


Table 3. Cont.


Species Geographic


Anatomically


Image


Section


Number of Species


Number of


Reference Database


Similar Species


Type


Type


Images


Origin


Image Analysis


PreProcessing


Features Descriptor Classiﬁers CNN Model Classiﬁcation


Accuracy


Program


Images


## IMAGE


## DATA GENERA


[86] LWA-UFP Brazil Macro Transverse 41 No 47.024 n.a.


SJRw; MADw;


Central and South America,


n.a. n.a. Resnet50 98.3%


TOR class of KERAS


Stereo Transverse 10 Yes 2303 n.a. n.a. n.a. End-to-end trained


[112]


RBw


Africa


image classiﬁers VGG16 87.4%–97.5%


[47] LWA-UFP Brazil Micro Transverse 44 No 528 n.a. n.a. LBP RF SVM n.a. 93.9%


Macro


41


2942


[132] LWA-UFP Brazil


Transverse


No


Micro 112 2240


[133] Samples from the


Inception_v3 n.a. TL 95.7%


Scale dataset 100%


Macroscopic dataset


n.a. n.a. n.a. n.a. n.a.


98.73%


Microscopic dataset


99.11%


Multiple


timber industry Korea Macro Transverse Tangential 5 Yes 33,815 n.a. n.a. n.a. n.a.


Tangential


Radial & between


[134] FFPRI Japan NIR


models ensemble


98%


## 38 No n.a. n.a. n.a. n.a. n.a. PCA 90.5%


HSI


the two


planes


SJRw; MADw;


Transverse Tangential


Central and South


[135]


America Micro


## 3 Yes n.a. n.a. n.a. n.a. SVM n.a. 91.4%


RBw


Radial


## TXWD-RMCA;


HNM; MADw; CM, Inc.;


Slivers for metabolome


Central America and Central Africa


## DARTTOFMS


## 10 No n.a. n.a. Binning threshold n.a. RF n.a. 82.2%


[136]


proﬁling


## OSU;


PV


[73] Samples from natural forests


Amazonia Atlantic region Macro Transverse 21 No 2000 n.a. Adapthisteq GLCM SVM n.a. 97.7%


<!-- Page 13 -->


Forests 2022, 13, 2041 13 of 26


Table 3. Cont.


Species Geographic


Anatomically


Image


Section


Number of Species


Number of


Reference Database


Similar Species


Type


Type


Images


Origin


## TXWD-RMCA;


HNM; MADw; CM, Inc.;


[66]


Image Analysis


PreProcessing


Features Descriptor Classiﬁers CNN Model Classiﬁcation


Accuracy


Program


Images


Species level


81.9%


Central America and Central Africa Stereo Transverse 10 No n.a. n.a. n.a. n.a. n.a. ResNet34


## OSU;


PV


Genus level


96.1%


[81] DSB-FWRC North America Stereo Transverse 10 No 1869 n.a. n.a. n.a. n.a. Inception V4_ResNetV2 92.6%


Transverse Tangential


[137] 2012 ImageNet Brazil Stereo


## 281 No n.a. n.a. n.a. RiLPQ kNN DenseNet 98.8%


Radial


[69] CVLO-CELOS Suriname Macro Transverse 14 No 1.2 million n.a. Threshold n.a. n.a. Inception-v3 98%


[76] [76] Neotropical


regions Micro Transverse 112 No 2240 n.a. n.a. LBP SVM ResNet101 95.6%


[138] Samples from


ResNet-50 DenseNet-121


Lumber yard North America Macro Tangencial 11 No 3158 n.a. n.a. n.a. SGD optimizer Adam optimizer


Tangential


Radial &


in between


98.2%


MobileNet


V2


## 48 No n.a. n.a. n.a. n.a. n.a. 1D CNN model 99%


[139] GACD Global XRF


the two


planes


Collected from trunks of


Residual convolutional


Wood patch classiﬁcation—93%


encoder network


Europe Macro Transverse 14 No n.a. n.a. n.a. Train set n.a.


[72]


leaﬁng trees


Democratic Republic of the


Transverse Tangential


## [140] TXWD-RMCA


Micro


Wood core classiﬁcation—98.7%


## 77 No n.a. n.a. GSC LPQ MVRF n.a. 95%


Congo


Radial


n.a. not available. Institutions: CM, Inc.—Carlton McLendon, Inc.; CVLO-CELOS—Centrum voor Landbouwkundig Onderzoek/Centre for Agricultural Research in Suriname;


DSB-FWRC—Department of Sustainable Bioproducts/Forest and Wildlife Research Center; FFPRI—Forestry and Forest Products Research Institute (Japan); GACD—Garman Art


<!-- Page 14 -->


Forests 2022, 13, 2041 14 of 26


Conservation Department, SUNY—Buffalo State; HNM—IB—Herbario Nacional de México; Instituto de Biología; LWA-UFP—Laboratory of Wood Anatomy at the Federal


University of Parana; MADw—USDA Forest Products Laboratory Wood Collection of Madison, Wisconsin; OSU—Oregon State University; PV—Private vendor; RBw—Botanic


Garden of Rio de Janeiro, Brazil; SJRw—Samuel J. Record Collection; TXWD-RMCA—Tervuren Xylarium Wood Database—Royal Museum for Central Africa. Models &


Techniques: DART-TOFMS—Direct Analysis in Real Time, Time of Flight Mass Spectrometry; EVT—External validation test; GLCM—Grey level co-occurrence matrix; GSC—Grey


scale conversion; kNN—k-nearest neighbours; LDA—linear discriminant analysis; LOOCV—Leave-one-out-cross-validation; MVRF—Multi-view random forest; PCA—Principal


component analysis; RF—Random Forests; RiLPQ—Rotation Invariant Local Phase Quantisation; SGD optimizer—Stochastic gradient descent; SVM—Support vector machine;


TL—Transfer learning; XRF—X-ray ﬂuorescence spectrometry.


<!-- Page 15 -->


Forests 2022, 13, 2041 15 of 26


In the ﬁeld of wood differentiation and identiﬁcation, examples of research applying ANNs include:


- Esteban et al. [127] used a feedforward multilayer perceptron (MLP) network, which uses a similar structure to ANN to distinguish between Juniperus cedrus and J. phoenicea var. canariensis, obtaining a 92% probability of correctly differentiating the species; - Mallik et al. [79] applied SEM to wood cross sections with 1500× magniﬁcation to obtain species-level identiﬁcation through the shape, number, area and distribution of earlywood tracheids, processed by image segmentation, object recognition and statistical methods. Their results showed that when distinguishing between hardwoods and softwoods, a 0.89 accuracy was obtained using leave-one-out cross-validation and 0.93 using an external validation test (EVT), and when differentiating seven wood species, they obtained a 0.81 accuracy using one-leave-out cross-validation and 0.80 using an EVT; - The same microscopic features analysis was applied by Martins et al. [77], who used microscopic transverse sections applying local phase quantisation (LPQ), local binary patterns (LBP) and grey-level co-occurrence matrix (GLOM) to identify Brazilian species. The process was applied to 112 species, 85 genera and 30 families, obtaining a recognition rate of 98.6% for differentiation of hardwoods and softwoods and 86% for discrimination of the 112 species; - Turhan [128] used the SVM as a machine learning algorithm to differentiate Salix alba, S. caprea and S. eleagnos, obtaining a 95.2% success rate; - Filho et al. [71] used a two-level divide-and-conquer classiﬁcation strategy to differentiate 41 species of Brazilian ﬂora, obtaining the highest accuracy level, of 97.77%; - Esteban et al. [130] used a multilayer perceptron (MP) to differentiate Pinus sylvestris L. and P. nigra Arn subsp. salzmannii (Dunal) Franco, obtaining 81.2% accuracy in the testing set; - Silva et al. [78] used microscopic images of cross sections of 77 commercial wood species from the Democratic Republic of the Congo for surface texture analysis, reporting 88% successful identiﬁcations at species level, 89% at genus level and 90% at family level. - He et al. [135] applied machine learning classiﬁers SVM, Naive Bayes (NB), Decision Tree C5.0 and ANN) to discriminate between Swietenia macrophylla King, S. mahagoni (L.) Jacq and S. humilis Zucc. The best results were obtained with SVM, with an overall accuracy of 91.4%; - Deklerck et al. [136] used machine learning not for image-based data processing, but for metabolome proﬁle obtained through direct analysis in real-time (DART™) ionisation combined with time-of-ﬂight mass spectrometry (TOFMS) to study the heartwood of 175 samples of 10 species of the Meliaceae family. Combining these techniques resulted in accuracy levels of 82.2%; - de Andrade et al. [73] generated 2000 macroscopic images of 21 species using a smartphone and samples manually polished with a knife to replicate ﬁeld conditions. A grey level co-occurrence matrix for the development of classiﬁers based on SVM was used, resulting in accuracies of 97.7%; - Silva et al. [140] used 77 Congolese wood species as a reference base for applying a multi-view random forest (MVRF) model for species-level identiﬁcation. To ensure information was not missed, the authors used images of the three anatomical planes. The results showed that the concatenation of features from the transverse and tangential planes clearly outperforms transverse-only analysis, while adding the radial plane minimally improves the results obtained. The use of the MVRF model outperformed concatenation of LPQ features. The results showed that the supplementary information added using three planes analysis and the model type considerably improve the ﬁnal results. Moreover, when evaluating the performance of the systems developed, using the k-fold cross-validation scheme could have led to overestimation of the results, so the authors applied a leave-k-tree-out approach during cross-validation.


<!-- Page 16 -->


Forests 2022, 13, 2041 16 of 26


The results showed that implementing this approach dramatically decreased accuracy compared with traditional cross-validation schemes.


## 4.2. Convolutional Neural Networks (CNN)


Convolutional neural networks are one of the most signiﬁcant applications of ANNs. In the AI context, a CNN is a class of feedforward ANN that has been successfully applied to digital image processing analysis.


A CNN processes images more effectively by applying filtering techniques to ANNs [115]. This is a powerful and accurate way of solving classiﬁcation problems, and CNNs are mainly credited for their role in image analysis, recognition, and classiﬁcation. The architecture of a CNN typically has multiple layers between input and output: three convolutional layers, a pooling layer and a fully connected layer. These layers process different tasks during the image’s course. As the images progress through the distinct layers, features such as edges, colours and shapes are extracted and interpreted. These features are then learned and classiﬁed by the deep neural network, resulting ultimately in the network’s ability to identify a speciﬁc object [62,115,141]. Other advantages are the capacity of automatically recognise important features without human supervision.


CNNs have difﬁculty dealing with variance in the data presented, as tilted or rotated images. This results in a limitation to encode an object’s orientation and position or process spatially invariant data.


Research examples applied to wood identiﬁcation include:


- Hafemann et al. [129] applied the CNN model 3-ConvNeta to identify macro images of 41 species and micro images of 112 species. The results obtained 95.77% accuracy for macroscopic images and 97.32% accuracy for microscopic images; - Kwon et al. [131] applied six LeNet and MiniVGGNet CNN models to identify ﬁve Korean softwood species (Cryptomeria japonica, Chamaecyparis obtuse, Pinus koraiensis, P. densiﬂora, Larix kaempferi), using an iPhone 7 camera to obtain macroscopic images of rough sawn surfaces from cross sections. Of all the CNN models tested, LeNet3 achieved the highest results and stability, with two extra layers added to the original LeNet architecture. The identiﬁcation accuracy obtained was 99.3%. The authors reported that the software weight of the CNN created is small enough for installation on a mobile device such as a smartphone; - Maintaining the objective of ensuring ﬁeld applicability, Kwon et al. [133] acknowledged the real-world limitations of not including longitudinal wood surfaces. Using mobile device cameras to obtain macroscopic images, they applied a combination of models, obtaining the best results with LeNet2, LeNet3 and MiniVGGNet4. Their results showed an overall accuracy of 98% and an improvement on their earlier study, particularly in the case of P. koraiensis and P. densiﬂora; - Figueroa-Mata et al. [86] applied deep convolutional networks for identiﬁcation of 41 Brazilian forest species from xylotheque samples at species level, achieving an accuracy of 98.3%; - Ravindran et al. [112] used CNNs to identify 10 neotropical species in the Meliaceae family (Cabralea canjerana, Carapa guianensis, Guarea glabra, G. grandifolia, Khaya ivorensis, K. senegalensis, and the CITES-listed Swietenia macrophylla, S. mahagoni, Cedrela ﬁssilis, and C. odorata), using only the transverse surface. The results showed an accuracy of 87.4 to 97.5%; - To develop an automatic classiﬁcation system for charcoal, Maruyama et al. [47] applied two LBP conﬁgurations of as texture descriptors. As state-of-the-art machine learning classiﬁers, SVM and random forests (RF) have shown the best results. Inception_v3 CNN was applied for representation learning evaluation. The database comprised 44 charcoal samples from Brazilian native species from natural forests. The authors reported that both handcrafted features and RL achieved results of around 95% recognition rate;


<!-- Page 17 -->


Forests 2022, 13, 2041 17 of 26


- Oliveira et al. [132] used databases developed by Filho et al. [71] and Martins et al. [77] to access cross sections of 2942 wood macroscopic images of 41 species and 2240 microscopic images of 112 species, applying CNNs to create three models. Based on the results, the authors reported 100% recognition accuracy for the scale model, 98.73% for the macroscopic model, and 99.11% for the microscopic model; - Kanayama et al. [134] applied a deep CNN approach to near-infrared hyperspectral imaging (NIR-HSI) using a principal component (PC) algorithm to identify 120 samples of 38 hardwood species. The results obtained showed 90.5% accuracy; - A CNN was also used by Ravindran and Wiedenhoeft [66] to compare the macroscopic ﬁeld identiﬁcation programme XyloTron, using an ImageNet pre-trained ResNet34 CNN, with mass spectrometry to differentiate 10 Meliaceae species used by Deklerck et al. [136]. The results showed identiﬁcation accuracy of 81.9% at the species level and 96.1% at the genus level compared to 74.9% and 91.4%, respectively, in the work by Deklerck et al. [136]; - Lopes et al. [81] applied the InceptionV4_ResNetV2 CNN to analyse macroscopic images of the end-grain of 10 xylarium North American hardwood species, producing 1869 images using a smartphone ﬁtted with a 14× macro lens. Their results showed an accuracy of 92.6%; - de Geus et al. [137] applied the DenseNet CNN to recognise 281 species, using the largest dataset of microscopic transverse, radial and tangential images available at the time. Rotation invariant LPQ (RiLPQ) showed the best results of the feature descriptors used. The authors reported an identiﬁcation accuracy of 98.8%; - Olschofsky and Köhl [69] applied Inception-v3, an image classiﬁcation model using a CNN for feature recognition and classiﬁcation, pre-trained with 1.2 million images. The CITES-protected species Cedrella odorata was chosen and compared with 13 other tropical tree species for recognition. The results with the pre-trained CNNs had 98% accuracy, but when other tree species not used for training were added, the classiﬁcation accuracy fell to 87%; - The ResNet101 CNN, associated with an SVM as classiﬁer, was applied by Lens et al. [76] to species-level identiﬁcation of 112 mainly neotropical tree species, using only transverse sections but focusing on microscopic rather than macroscopic analysis. The results showed successful identiﬁcation in 95.6% of cases; - Wu et al. [138] applied deep convolutional neural networks (CNNs) for the identiﬁcation of 11 rough saw hardwood North American species based on tangential plane images only. CNNs ResNet-50, DenseNet-121, as well as MobileNet-V2 were tested, resulting in an overall accuracy of 98.2%. - Shugar et al. [139] combined X-ray ﬂuorescence spectrometry (XRF) and a CNN to identify 48 wood specimens of both hardwoods and softwoods, mostly from heartwood and using either tangential or radial sections. They reported 99% identiﬁcation accuracy from the 66 datasets; - In the study by Fabija´nska et al. [72], a CNN with residual connections was tested to identify 312 wood core scanned images of 14 European softwood and hardwood tree species, developing a wood patch classiﬁcation and a wood core classiﬁcation. The results showed that the proposed model correctly recognised patch images in 93% of cases and wood core images in 98.7%. Comparison of the results also showed that this model outperformed the state-of-the-art convolutional neural network-based model.


## 4.3. Generative Adversarial Networks (GANs)


Within deep learning, GANs [142] are described as neural networks that can learn to generate realistic samples from the data on which they were trained.


They use a neural network as a generator that takes a random distribution of data as input and learns to map that information to output the desired distribution of data. A second neural network, known as a discriminator (a binary classiﬁer), will use the input and output images to determine the probability of the image originating as a training image


<!-- Page 18 -->


Forests 2022, 13, 2041 18 of 26


(real) or on the generator (fake), thus assessing the most likely class to which the output image belongs [143].


Generative adversarial networks can produce highly realistic images using CNNs in an unsupervised manner [144]. Their application extends to multiple ﬁelds of scientiﬁc research, but they remain poorly explored in wood sciences [145–147].


- Addressing the possibility of eliminating economic and processing burdens in acquiring images of worldwide wood species for machine-learning training purposes, Lopes et al. [144] accessed 119 hardwood species references on the publicly available Xylarium Digital Database [87]. Applying a style-based GAN, they successfully generated highly realistic and anatomically meaningful synthetic microscopic cross-sectional images of hardwood species which they reported as virtually indistinguishable from real cross-sectional images. - To evaluate the resemblance, quality and pattern evaluation between the synthetic and real cross sections, a structural similarity index measure (SSIM) and Fréchet inception distance (FID) were applied and a visual Turing test (VTT) was performed by wood anatomists to conﬁrm the usefulness and realism of the GAN-generated images. The results showed that the artiﬁcially generated images were indistinguishable from real microscopic cross-sectional images. - The authors [144] reported that it is even feasible to generate synthetic hybrids based on microscopic cross-sectional images from two parental species. This would have considerable implications on wood science and technology, especially for estimating the wood permeability, strength, density, or hydraulic potential, for example, of a species that has not even been planted.


## 5. Field Applicable Wood Identiﬁcation Systems


One of the most interesting features of computer vision-based wood identiﬁcation systems is their ﬁeld application capability. Despite the consensus that it will be a long time before this technology becomes readily available not only to researchers and law enforcement bodies, but also the general public, it is evident that this goal is reachable. Programmes already developed or under development to respond to ﬁeld application needs include:


## 5.1. MyWood-ID


Described as an automated wood identiﬁcation mobile app [89], MyWood-ID uses a smartphone with a retroﬁtted macro lens and machine vision for macroscopic wood identiﬁcation. The system uses a database of 20 species of timber native to Malaysia and provides a simple and effective way to acquire macroscopic wood digital images. The images are then uploaded to a cloud server via an internet connection for immediate identiﬁcation results. It is intended to be cost-effective, easily accessible and intuitive, and to provide fast results.


These characteristics are evident when compared with other ﬁeld deployable systems [64,74]. As differentiating features of their wood identiﬁcation system, the authors cite its portability, lower initial cost, faster ﬁeld deployment time, intuitive use, and continual online database update. However, it requires a constant internet connection for results and is operating-system-dependent (running only on iPhone 6 and 7). The main limitation of this system is the lack of consistent light control for wood image acquisition, although the authors indicate that this can be mitigated using the learning capability of a deep learning algorithm. The results achieved by this system have an accuracy of 96% to 98%. It is a paid app.


## 5.2. MyWood-Premium


This is an update of the previous app, developed by FRIM (Wood Anatomy Lab of Forest Research Institute Malaysia) and UTAR (Universiti Tunku Abdul Rahman) [148]. The updated version comprises a database of 100 wood species native to Malaysia. It is


<!-- Page 19 -->


Forests 2022, 13, 2041 19 of 26


available only on iPhone, iPod touch and Mac, and requires iOS 8.0 or later. It recommends the Ollo-clip™Macro Lens with 21× magniﬁcation for optimum performance. It is a free app.


## 5.3. Xylorix


Another recent approach to rapid ﬁeld wood identiﬁcation is Xylorix [149,150], a platform that combines a suite of apps, tools and services. Xylorix Inspector is a wood identiﬁcation mobile app that uses macroscopic features for automated identiﬁcation. It is based on trained AI models to automatically identify the wood genus or species. However, a Xylorix WIDK-24X01 illuminated macro lens must be attached to the mobile phone camera for correct performance. It is available on either Apple iOS or Android operating systems and is supported by most mobile phones. Of the 24 species in the system database, 11 are free and the other 13 are paid.


## 5.4. XyloTron


XyloTron is a paid, open-source, image-based macroscopic ﬁeld identiﬁcation programme designed for wood and charcoal identiﬁcation [64,151]. It features adjustable and controlled visible light, UV illumination capacity, and all the necessary software to control the device, capture images, and deploy the trained classiﬁcation models.


It works by capturing high-quality images of wood or charcoal samples with visible or UV light. The identiﬁcation accuracy for wood is described as 97.7%, increasing with the use of UV light to 99.1% (e.g., identiﬁcation confusion between Albizia sp., ﬂuorescent, and Inga sp., not ﬂuorescent) and 98.7% for charcoal.


One limitation is that it is not a simple or easily deployable on-site system to use, because it requires a permanent connection to a laptop computer.


Ravindran and Wiedenhoeft [66] compared the performance of XyloTron and MS for species- and genus-level identiﬁcation of 10 species of Meliaceae. The results showed a similar species-level accuracy of the XyloTron and MS models, but higher genus-level accuracy with XyloTron [66].


## 5.5. XyloPhone


To overcome visual aberrations (ﬁeld distortion and spherical aberration), uncontrolled light sources, high prices, and a lack of real ﬁeld applicability, Wiedenhoeft [82] proposed the XyloPhone. Described as an open-source, 3D-printed imaging attachment adaptable to virtually any smartphone for macroscopic image capture, it is a small, closed plastic box that provides a ﬁxed focal distance, exclusion of ambient light, and a choice of visible or UV illumination. It is powered by a rechargeable external battery and a commercially available lens, making it affordable and, according to the author, providing comparable image quality to XyloTron.


To document features such as evenness of illumination, distortion, maximum resolution, and spherical aberration, the author compared the Xylophone + iPhone (XPi), the XyloPhone + Samsung (XPs), the Ollo Clip 14× + iPhone (OCi), and the Xylorix + iPhone, with two distinct conﬁgurations. He reported that XyloPhone’s optical performance, especially when used with more recent smartphones, is clearly superior to the lenses/lighting arrays of other systems [82].


## 5.6. WIDER


WIDER is a battery-charged portable system that uses spectroscopy measurement and machine-learning-based identiﬁcation software. It comprises a database of 15 species and the authors [152] reported accuracy results of 95%. It is part of a larger project that was completed in 2021 and brought into use by USAID PEER Cycle 8 (Development of Wood Identiﬁcation System and Timber Tracking Database to Support Legal Trade). The same project developed the ECVT 4D Dynamic [152] technology for monitoring tree physiological processes.


<!-- Page 20 -->


Forests 2022, 13, 2041 20 of 26


## 5.7. IMAIapp


IMAIapp [153] is a wood identiﬁcation mobile app that uses a lens attached to a smartphone. Its purpose is to use convolutional neural networks (CNN) capable of carrying out timber identiﬁcation through machine learning of macroscopic elements observed in photo enlargements. The difﬁculty of the problem lies in the number of classes that the method is required to recognise automatically, from a total of 400 wood species and a high number of macroscopic images. EfﬁcientNet architecture is enhanced by a novel approach for pre-processing that combines computer vision and data augmentation techniques applied to the original dataset. The use of classiﬁcation models based on deep learning is the leading technique with the best performance at present, and the innovative approach to increase the quality of the training data makes the model integrated in IMAIapp robust to rotation, illumination and zoom invariants. This means the app can be used in the ﬁeld. Using TensorFlow Lite libraries for Apple and Google platforms, the application works standalone, is 100% executable from the mobile device and does not require a connection to the Internet. IMAIapp is therefore a design using an edge-computing method that is intended to avoid computing constraints on the mobile device on which it is installed. The project is under development and the app will be free for Android and iOS.


## 6. Discussion


In the last 100 years, what we now call the traditional wood identiﬁcation method based on anatomical descriptions has followed well deﬁned, standardised features to successfully distinguish and identify the multiple families, genera and species of angiosperm and gymnosperm trees. However, despite the many positive aspects of this method, it is now evident that it is reaching its limit.


The main limitations are the identiﬁcation uncertainty at species level, the timeconsuming methodology, the lack of anatomists with the necessary training for the task, and the associated costs of these professionals, mainly when on-site identiﬁcations are required. These limitations have a notable impact on the type of monitoring that can be carried out, e.g., in the ﬁght against illegal logging. Faster, more accurate and economically scalable methods are urgently needed.


As a valuable response to this need, the results obtained so far by computer visionbased identiﬁcation (CVBI) of wood and, in particular, deep learning approaches, clearly demonstrate that this method has enormous potential for wood identiﬁcation and quantitative wood anatomy.


Despite the many obstacles remaining, this method is steadily adapting to overcome limitations such as inter- and intra-anatomical variability, high anatomical resemblance, non-homogeneous illumination, staining or deformed samples, and limited image databases, among many other issues.


Of all the resources discussed, deep learning appears to be the most signiﬁcant and promising solution in AI developments, and CNN models applied to wood sciences are one of the leading and most rapidly evolving systems. CNNs have exhibited a notably more efﬁcient capacity and accuracy for quantitative wood anatomy and feature recognition, alongside computer cost reduction.


Field-deployable identiﬁcation systems appear to be the most important and impactful option in computer vision-based wood identiﬁcation. This resource, based on advances in communication technologies, will enable more proliﬁc, increasingly accurate and faster screening by authorities without human prejudice, particularly with regard to illegal timber and charcoal trading.


Computer vision-based identiﬁcation technology could become one of the most effective and unavoidable weapons in the ﬁght against the illegal timber and charcoal trade, as it enables individuals who are untrained in traditional identiﬁcation to obtain highly accurate and legally binding identiﬁcations on the spot.


The multiple future contributions of the technologies underpinning CVBI for wood sciences are difﬁcult to fully envision at present. However, it is of utmost importance to


<!-- Page 21 -->


Forests 2022, 13, 2041 21 of 26


overcome or at least mitigate the limitations that are severely hampering the development and implementation of these systems.


Two of the most pressing issues are the limited number of digital databases, which are speciﬁc to geographically restricted areas/species or inaccessible to the global research community, and the lack of extensive ﬁeld testing and veriﬁcation hindering the accuracy quantiﬁcation of the systems.


The most urgent actions required are the construction of a freely accessible global digital wood image database, the availability of this tool in a cloud-based system for access everywhere, by everyone, and priority inclusion of CITES-listed species and their look-a-likes.


Author Contributions: Conceptualisation, writing and original draft preparation J.L.S.; review and editing R.B., J.P., P.d.P. All authors have read and agreed to the published version of the manuscript.


Funding: This research was supported by national funds through Fundação para a Ciência e Tecnologia (FCT), within the scope of the Project UID/EAT/0622/2016 of CITAR—Centro de Investigação da Universidade Católica Escola das Artes, Porto, Portugal. J.L.S. is recipient of a PhD fellowship (UI/BD/151009/2021) with ﬁnancial support from FCT.


Data Availability Statement: Data are contained within the article and are also available from the corresponding author.


Acknowledgments: I would like to acknowledge Yong Haur Tay for his kind clariﬁcations about Xylorix, Pedro Luis Paula Filho for his kind clariﬁcations about The Forest Species Database— Macroscopic, Forest Species Classiﬁer and UTForest—UTFPR Classiﬁcador, Hisashi Abe for his kind clariﬁcations about the Wood database of the Forestry and Forest Products Research Institute, and Dra Cassiana Ferreira for her kind clariﬁcations about the Mader app.


Conﬂicts of Interest: The authors declare no conﬂict of interest.


## References


1. May, C. Transnational Crime and the Developing World; Global Financial Integrity: Washington, DC, USA, 2017. 2. Nellemann, C. Green Carbon, Black Trade: A Rapid Response Assessment on Illegal Logging, Tax Fraud and Laundering in the World’s Tropical Forests. 2012. Available online: https://wedocs.unep.org/20.500.11822/8030 (accessed on 27 April 2022). 3. EU; EC. Forests. Available online: https://ec.europa.eu/environment/forests/illegal_logging.htm (accessed on 27 April 2022). 4. Bösch, M. Institutional quality, economic development and illegal logging: A quantitative cross-national analysis. Eur. J. For. Res. 2021, 140, 1049–1064. [CrossRef] 5. UN. Convention on International Trade in Endangered Species of Wild Fauna and Flora. Available online: https://cites.org/ sites/default/ﬁles/eng/disc/CITES-Convention-EN.pdf (accessed on 27 April 2022). 6. EU. European Union Timber Regulation. Available online: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX% 3A32010R0995 (accessed on 27 April 2022). 7. European Union; Austrian Development Cooperation; The World Bank; IUCN. WWF ENPI EAST FLEG—European Neighborhood and Paternaship Instrument East Countries Forest Law Enforcement and Governance Program. Available online: https://www.enpi-ﬂeg.org/ (accessed on 6 June 2022). 8. FAOUN; UNDP. UNEP UN-REDD Programme. Available online: https://www.un-redd.org/ (accessed on 27 April 2022). 9. UNDER; UNEP. FAOUN Preventing, Halting and Reversing The Degradation Of Ecosystems Worldwide. Available online: https://www.decadeonrestoration.org/ (accessed on 27 April 2022). 10. Schmitz, N.; Beeckman, H.; Blanc-Jolivet, C.; Boeschoten, L.E.; Braga, J.J.W.B.; Cabezas, J.A.; Chaix, G.; Crameri, S.; Degen, B.; Deklerck, V.; et al. Overview of Current Practices in Data Analysis for Wood Identiﬁcation. A Guide for the Different Timber Tracking Methods; GTTN-European Forest Institute: Joensuu, Finland, 2020. 11. Schmitz, N.; Beeckman, H.; Cabezas, J.A.; Cervera, M.T.; Espinoza, E.; Fernandez-Golﬁn, J.; Gasson, P.; Hermanson, J.; Jaime Arteaga, M.; Koch, G.; et al. The Timber Tracking Tool Infogram. Overview of Wood Identiﬁcation Methods’ Capacity; Global Timber Tracking Network, GTTN Secretariat, European Forest Institute and Thünen Institute: Joensuu, Finland, 2019. 12. Dormontt, E.E.; Boner, M.; Braun, B.; Breulmann, G.; Degen, B.; Espinoza, E.; Gardner, S.; Guillery, P.; Hermanson, J.C.; Koch, G.; et al. Forensic timber identiﬁcation: It’s time to integrate disciplines to combat illegal logging. Biol. Conserv. 2015, 191, 790–798. [CrossRef] 13. United Nations. International Consortium on Combating Wildlife Crime. In Best Practice Guide for Forensic Timber Identiﬁcation; United Nations Ofﬁce on Drugs and Crime: New York, NY, USA, 2016. 14. ITTO. Biennial Review and Assessment of the World Timber Situation. Available online: https://www.itto.int/direct/topics/ topics_pdf_download/topics_id=6783&no=1 (accessed on 27 April 2022).


<!-- Page 22 -->


Forests 2022, 13, 2041 22 of 26


15. Interpol Illegal Logging in Latin America and Caribbean Inﬂicting Irreversible Damage-INTERPOL. Available online: https://www.interpol.int/News-and-Events/News/2022/Illegal-logging-in-Latin-America-and-Caribbean-inﬂictingirreversible-damage-INTERPOL (accessed on 27 April 2022). 16. Abe, H.; Watanabe, K.; Ishikawa, A.; Noshiro, S.; Fujii, T.; Iwasa, M.; Kaneko, H.; Wada, H. Simple separation of torreya nucifera and chamaecyparis obtusa wood using portable visible and near-infrared spectrophotometry: Differences in light-conducting properties. J. Wood Sci. 2016, 62, 210–212. [CrossRef] 17. Pace, J.H.C.; Latorraca, J.-V.D.F.; Hein, P.R.G.; de Carvalho, A.M.; Castro, J.P.; da Silva, C.-E.S. Wood species identiﬁcation from Atlantic forest by near infrared spectroscopy. For. Syst. 2019, 28, e015. [CrossRef] 18. Snel, F.A.; Braga, J.W.B.; da Silva, D.; Wiedenhoeft, A.C.; Costa, A.; Soares, R.; Coradin, V.T.R.; Pastore, T.C.M. Potential ﬁeld-deployable NIRS identiﬁcation of seven dalbergia species listed by CITES. Wood Sci. Technol. 2018, 52, 1411–1427. [CrossRef] 19. Akhmetzyanov, L.; Copini, P.; Sass-Klaassen, U.; Schroeder, H.; de Groot, G.A.; Laros, I.; Daly, A. DNA of centuries-old timber can reveal its origin. Sci. Rep. 2020, 10, 20316. [CrossRef] [PubMed] 20. Jiao, L.; Liu, X.; Jiang, X.; Yin, Y. Extraction and ampliﬁcation of DNA from aged and archaeological populus euphratica wood for species identiﬁcation. Holzforschung 2015, 69, 925–931. [CrossRef] 21. Wagner, S.; Lagane, F.; Seguin-Orlando, A.; Schubert, M.; Leroy, T.; Guichoux, E.; Chancerel, E.; Bech-Hebelstrup, I.; Bernard, V.; Billard, C.; et al. High-throughput DNA sequencing of ancient wood. Mol. Ecol. 2018, 27, 1138–1154. [CrossRef] 22. Carmona, R.J.; Wiemann, M.C.; Baas, P.; Barros, C.; Chavarria, G.D.; McClure, P.J.; Espinoza, E.O. Forensic identiﬁcation of CITES appendix I cupressaceae using anatomy and mass spectrometry. IAWA J. 2020, 41, 720–739. [CrossRef] 23. Espinoza, E.O.; Wiemann, M.C.; Barajas-Morales, J.; Chavarria, G.D.; McClure, P.J. Forensic analysis of cites-protected dalbergia timber from the americas. IAWA J. 2015, 36, 311–325. [CrossRef] 24. Zhang, M.; Zhao, G.J.; Liu, B.; He, T.; Guo, J.; Jiang, X.; Yin, Y. Wood discrimination analyses of pterocarpus tinctorius and endangered pterocarpus santalinus using DART-FTICR-MS coupled with multivariate statistics. IAWA J. 2019, 40, 58–74. [CrossRef] 25. Ge, Z.; Chen, L.; Luo, R.; Wang, Y.; Zhou, Y. The detection of structure in wood by X-ray CT imaging technique. BioResources 2018, 13, 3674–3685. [CrossRef] 26. Kobayashi, K.; Hwang, S.-W.; Okochi, T.; Lee, W.-H.; Sugiyama, J. Non-destructive method for wood identiﬁcation using conventional X-ray computed tomography data. J. Cult. Herit. 2019, 38, 88–93. [CrossRef] 27. Tazuru, S.; Sugiyama, J. Wood identiﬁcation of japanese shinto deity statues in matsunoo-taisha shrine in kyoto by synchrotron X-ray microtomography and conventional microscopy methods. J. Wood Sci. 2019, 65, 60. [CrossRef] 28. Wheeler, E.A.; LaPasha, C.A. A microcomputer based system for computer-aided wood identiﬁcation. IAWA Bull. 1987, 8, 347–354. 29. LaPasha, C.A. General unknown entry and search system. A program package for computer-assisted identiﬁcation. Suppl. N. C. Agric. Resour. Serv. 1986, 474, 18. 30. Ilic, J. Computer aided wood identiﬁcation using csiroid. IAWA J. 1993, 14, 333–340. [CrossRef] 31. Dallwitz, M.J. A general system for coding taxonomic descriptions. Taxon 1980, 29, 41–46. [CrossRef] 32. Richter, H.G.; Dallwitz, M.J. Commercial Timbers: Descriptions, Illustrations, Identiﬁcation, and Information Retrieval. Available online: https://www.delta-intkey.com/wood/en/index.htm (accessed on 10 October 2021). 33. Heiss, A.G. Anatomy of European and North American Woods—An Interactive Identiﬁcation Key. Available online: http: //www.holzanatomie.at/ (accessed on 9 February 2022). 34. Forestry & Forest Products Research Institute. Wood Database of the Forestry & Forest Products Research Institute. Available online: https://db.ffpri.go.jp/WoodDB/index-E.html (accessed on 2 May 2022). 35. Wheeler, E.A. InsideWood. Available online: https://insidewood.lib.ncsu.edu/search;jsessionid=hYhHqrsAfkTKM8JGVm0e3 WjZLOdRCfo3_1Y5k6Zq?0 (accessed on 9 January 2022). 36. Schoch, W.; Heller-Kellenberger, I.; Schweingruber, F.; Kienast, F.; Schmatz, D. Wood Anatomy of Central European Species. Available online: http://www.woodanatomy.ch/authors.html (accessed on 3 May 2022). 37. Richter, H.G.; Gembruch, K.; Koch, G. CITESwoodID: Descriptions, Illustrations, Identiﬁcation, and Information Retrieval. Available online: https://www.delta-intkey.com/citeswood/index.htm (accessed on 9 February 2022). 38. Barker, J.A.; Flinders, B.A.H. Key to a Selection of Arid Australian Hardwoods & Softwoods. Available online: https://keys. lucidcentral.org/keys/v3/arid/default_wip.htm (accessed on 4 January 2022). 39. Coradin, V.T.R.; Camargos, J.A.A.; Pastore, T.C.M.; Christo, A.G. Brazilian Commercial Timbers: Interactive Identiﬁcation Key Based on General and Macroscopic Features Madeiras Comerciais do Brasil: Chave Interativa de Identiﬁcação Baseada em Caracteres Gerais e Macroscópicos. Available online: https://keys.lucidcentral.org/keys/v4/madeiras_comerciais_do_brasil/ index_en.html (accessed on 2 May 2022). 40. Sarmiento, C.; Détienne, P.; Heinz, C.; Molino, J.-F.; Grard, P.; Bonnet, P. Pl@ntwood: A computer-assisted identiﬁcation tool for 110 species of amazon trees based on wood anatomical features. IAWA J. 2011, 32, 221–232. [CrossRef] 41. Martins, J.; Oliveira, L.S.; Nisgoski, S.; Sabourin, R. The Forest Species Database—Microscopy. Available online: https://web.inf. ufpr.br/vri/databases/forest-species-database-microscopic/ (accessed on 3 May 2022). 42. UFPR Forest Species Database—Microscopic. Available online: https://web.inf.ufpr.br/vri/databases/forest-species-databasemicroscopic/ (accessed on 21 April 2022).


<!-- Page 23 -->


Forests 2022, 13, 2041 23 of 26


43. Filho, P.L.P.; Oliveira, L.S.; Nisgoski, S.; Britto, A.S. The Forest Species Database—Macroscopic. Available online: https: //web.inf.ufpr.br/vri/databases/forest-species-database-macroscopic/ (accessed on 3 May 2022). 44. UFPR Forest Species Database—Macroscopic. Available online: https://web.inf.ufpr.br/vri/databases/forest-species-databasemacroscopic/ (accessed on 23 April 2021). 45. Richter, H.G.; Oelker, M.; Koch, G. MacroHOLZdata—Computer Aided Macroscopic Wood Identiﬁcation and Information on Properties and Utilization of Trade Timbers. CD-ROM. Available online: http://macroholzdata.appstor.io/ (accessed on 23 April 2021). 46. De Oliveira, W. Forest Species Classiﬁer. Available online: http://reconhecimentoﬂorestal.md.utfpr.edu.br./#/pt/classiﬁcador (accessed on 3 May 2022). 47. Maruyama, T.M.; Oliveira, L.S.; Britto, A.S.; Nisgoski, S. Automatic classiﬁcation of native wood charcoal. Ecol. Inform. 2018, 46, 1–7. [CrossRef] 48. Bodin, S.C.; Scheel-Ybert, R.; Beauchêne, J.; Molino, J.-F.; Bremond, L. CharKey: An electronic identiﬁcation key for wood charcoals of French Guiana. IAWA J. 2019, 40, 75-S20. [CrossRef] 49. EyeWood, S.F.U. Softwood Retrieval System for Coniferous Wood. Available online: http://woodlab.swfu.edu.cn/#/ (accessed on 23 April 2021). 50. Filho, P.L.d.P. UTForest—UTFPR Classiﬁcador. Available online: https://clb.lamia.sh.utfpr.edu.br/classiﬁcation (accessed on 8 June 2022). 51. Ferreira, C.A.; Inga, J.G.; Vidal, O.D.; Goytendia, W.E.; Moya, S.M.; Centeno, T.B.; Vélez, A.; Gamarra, D.; Tomazello-Filho, M. Identiﬁcation of tree species from the peruvian tropical amazon “selva central” forests according to wood anatomy. BioResources 2021, 16, 7161–7179. [CrossRef] 52. Wheeler, E.A.; Baas, P.; Gasson, P.E. IAWA List of microscopic features for hardwood identiﬁcation: With an appendix on non-anatomical information. IAWA Bull. 1989, 10, 219–332. [CrossRef] 53. Schweingruber, F.H. Microscopic Wood Anatomy: Structural Variability of Stems and Twigs in Recent and Subfossil Woods from Central Europe; Swiss Federal Institute for Forest: Birmensdorf, Swiss, 1990; ISBN 3905620022. 54. CITES. Available online: https://cites.org/eng (accessed on 2 May 2022). 55. Menon, L.T.; Laurensi, I.A.; Penna, M.C.; Oliveira, L.E.S.; Britto, A.S. Data augmentation and transfer learning applied to charcoal image classiﬁcation. In Proceedings of the 2019 International Conference on Systems, Signals and Image Processing (IWSSIP), Osijek, Croatia, 5–7 June 2019; pp. 69–74. 56. Détienne, P.; Jacquet, P.; Mariaux, A. Manuel d’identiﬁcation des bois tropicaux. tome 3: Guyane Française. In Manuel D’identiﬁcation des Bois Tropicaux; CIRAD: Montpellier, France, 1982; Volume 3, p. 315. ISBN 139782876145962. 57. Richter, H.G.; Grosser, D.; Heinz, I.; Gasson, P.E. IAWA list of microscopic features for softwood identiﬁcation. IAWA J. 2004, 25, 1–70. [CrossRef] 58. Voulodimos, A.; Doulamis, N.; Doulamis, A.; Protopapadakis, E. Deep learning for computer vision: A brief review. Comput. Intell. Neurosci. 2018, 2018, 7068349. [CrossRef] 59. Li, N.; Shepperd, M.; Guo, Y. A Systematic review of unsupervised learning techniques for software defect prediction. Inf. Softw. Technol. 2020, 122, 106287. [CrossRef] 60. Jordan, M.I.; Mitchell, T.M. Machine learning: Trends, perspectives, and prospects. Science 2015, 349, 255–260. [CrossRef] 61. Khan, A.I.; Al-Habsi, S. Machine learning in computer vision. Procedia Comput. Sci. 2020, 167, 1444–1451. [CrossRef] 62. Hwang, S.-W.; Sugiyama, J. Computer vision-based wood identiﬁcation and its expansion and contribution potentials in wood science: A review. Plant Methods 2021, 17, 47. [CrossRef] [PubMed] 63. Ravindran, P.; Ebanyenle, E.; Ebeheakey, A.A.; Abban, K.B.; Lambog, O.; Soares, R.; Costa, A.; Wiedenhoeft, A.C. Image based identifcation of ghanaian timbers using the xylotron: Opportunities, risks and challenges. In Proceedings of the 33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, BC, Canada, 9–14 December 2019. 64. Ravindran, P.; Thompson, B.J.; Soares, R.K.; Wiedenhoeft, A.C. The xylotron: Flexible, open-source, image-based macroscopic ﬁeld identiﬁcation of wood products. Front. Plant Sci. 2020, 11, 1015. [CrossRef] [PubMed] 65. Tou, J.Y.; Tou, P.; Lau, P.Y.; Tay, Y.H. Computer vision-based wood recognition system. In Proceedings of the International Workshop on Advanced Image Technology; 2007. Available online: https://scholar.google.com/scholar?hl=en&as_sdt=0% 2C5&q=Computer+vision-based+wood+recognition+system.+In+Proceedings+of+International+Workshop+on+Advanced+ Image+Technology%2C+2007&btnG= (accessed on 27 April 2022). 66. Ravindran, P.; Wiedenhoeft, A.C. Comparison of two forensic wood identiﬁcation technologies for ten meliaceae woods: Computer vision versus mass spectrometry. Wood Sci. Technol. 2020, 54, 1139–1150. [CrossRef] 67. Du, M.; Liu, N.; Hu, X. Techniques for interpretable machine learning. Commun. ACM 2019, 63, 68–77. [CrossRef] 68. Martins, A.L.R.; Marcal, A.R.S.; Pissarra, J. Modiﬁed DBSCAN algorithm for microscopic image analysis of wood. In Iberian Conference on Pattern Recognition and Image Analysis; Springer: Cham, Switzerland, 2019; pp. 257–269. 69. Olschofsky, K.; Köhl, M. Rapid ﬁeld identiﬁcation of cites timber species by deep learning. Trees For. People 2020, 2, 100016. [CrossRef] 70. Barmpoutis, P.; Dimitropoulos, K.; Barboutis, I.; Grammalidis, N.; Lefakis, P. Wood species recognition through multidimensional texture analysis. Comput. Electron. Agric. 2018, 144, 241–248. [CrossRef]


<!-- Page 24 -->


Forests 2022, 13, 2041 24 of 26


71. Filho, P.L.P.; Oliveira, L.S.; Nisgoski, S.; Britto, A.S. Forest species recognition using macroscopic images. Mach. Vis. Appl. 2014, 25, 1019–1031. [CrossRef] 72. Fabija´nska, A.; Danek, M.; Barniak, J. Wood species automatic identiﬁcation from wood core images with a residual convolutional neural network. Comput. Electron. Agric. 2021, 181, 105941. [CrossRef] 73. De Andrade, B.G.; Basso, V.M.; de Figueiredo Latorraca, J.V. Machine vision for ﬁeld-level wood identiﬁcation. IAWA J. 2020, 41, 681–698. [CrossRef] 74. Khalid, M.; Lew, E.; Lee, Y.; Yusof, R.; Nadaraj, M. Design of an intelligent wood species recognition system. Int. J. Simul. Syst. Sci. Technol. 2008, 9, 9–19. 75. Wang, H.; Zhang, G.; Qi, H. Wood recognition using image texture features. PLoS ONE 2013, 8, e76101. [CrossRef] 76. Lens, F.; Liang, C.; Guo, Y.; Tang, X.; Jahanbanifard, M.; da Silva, F.S.C.; Ceccantini, G.; Verbeek, F.J. Computer-assisted timber identiﬁcation based on features extracted from microscopic wood sections. IAWA J. 2020, 41, 660–680. [CrossRef] 77. Martins, J.; Oliveira, L.S.; Nisgoski, S.; Sabourin, R. A database for automatic classiﬁcation of forest species. Mach. Vis. Appl. 2013, 24, 567–578. [CrossRef] 78. da Silva, N.R.; De Ridder, M.; Baetens, J.M.; Van den Bulcke, J.; Rousseau, M.; Bruno, O.M.; Beeckman, H.; Van Acker, J.; De Baets, B. Automated classiﬁcation of wood transverse cross-section micro-imagery from 77 commercial central-African timber species. Ann. For. Sci. 2017, 74, 30. [CrossRef] 79. Mallik, A.; Tarrío-Saavedra, J.; Francisco-Fernández, M.; Naya, S. Classiﬁcation of wood micrographs by image segmentation. Chemom. Intell. Lab. Syst. 2011, 107, 351–362. [CrossRef] 80. Kobayashi, K.; Akada, M.; Torigoe, T.; Imazu, S.; Sugiyama, J. Automated recognition of wood used in traditional japanese sculptures by texture analysis of their low-resolution computed tomography data. J. Wood Sci. 2015, 61, 630–640. [CrossRef] 81. Lopes, D.J.V.; Burgreen, G.W.; Entsminger, E.D. North american hardwoods identiﬁcation using machine-learning. Forests 2020, 11, 298. [CrossRef] 82. Wiedenhoeft, A.C. The XyloPhone: Toward democratizing access to high-quality macroscopic imaging for wood and other substrates. IAWA J. 2020, 41, 699–719. [CrossRef] 83. Yu, H.; Cao, J.; Luo, W.; Liu, Y. Image retrieval of wood species by color, texture, and spatial information. In Proceedings of the 2009 International Conference on Information and Automation, Zhuhai/Macau, China, 22–24 June 2009; pp. 1116–1119. 84. Yusof, R.; Khalid, M.; Khairuddin, A.S.M. Application of kernel-genetic algorithm as nonlinear feature selection in tropical wood species recognition system. Comput. Electron. Agric. 2013, 93, 68–77. [CrossRef] 85. Zamri, M.I.P.; Cordova, F.; Khairuddin, A.S.M.; Mokhtar, N.; Yusof, R. Tree species classiﬁcation based on image analysis using improved-basic gray level aura matrix. Comput. Electron. Agric. 2016, 124, 227–233. [CrossRef] 86. Figueroa-Mata, G.; Mata-Montero, E.; Valverde-Otarola, J.C.; Arias-Aguilar, D. Using deep convolutional networks for species identiﬁcation of xylotheque samples. In Proceedings of the 2018 IEEE International Work Conference on Bioinspired Intelligence (IWOBI), San Carlos, Costa Rica, 18–20 July 2018; pp. 1–9. 87. Kobayashi, K.; Kegasa, T.; Hwang, S.S.-W.; Sugiyama, J. Anatomical features of fagaceae wood statistically extracted by computer vision approaches: Some relationships with evolution. PLoS ONE 2019, 14, e0220762. [CrossRef] 88. Souza, D.V.; Santos, J.X.; Vieira, H.C.; Naide, T.L.; Nisgoski, S.; Oliveira, L.E.S. An automatic recognition system of brazilian ﬂora species based on textural features of macroscopic images of wood. Wood Sci. Technol. 2020, 54, 1065–1090. [CrossRef] 89. Tang, X.J.; Tay, Y.H.; Siam, N.A.; Lim, S.C. MyWood-ID. Rapid and robust automated macroscopic wood identiﬁcation system using smartphone with macro-lens. In Proceedings of the 2018 International Conference on Computational Intelligence and Intelligent Systems—CIIS 2018, Phuket, Thailand, 17–19 November 2018; ACM Press: New York, NY, USA, 2018; pp. 37–43. 90. Stanford, V.L.; University, S.; University, P. ImageNet. Available online: https://www.image-net.org/ (accessed on 21 April 2021). 91. Seregin, A.P. Moscow digital herbarium: A consortium since 2019. Taxon 2020, 69, 417–419. [CrossRef] 92. New Your Botanical Garden, N. Index Herbariorum. Available online: http://sweetgum.nybg.org/science/ih/ (accessed on 21 April 2022). 93. Soltis, P.S. Digitization of herbaria enables novel research. Am. J. Bot. 2017, 104, 1281–1284. [CrossRef] 94. Sugiyama, J.; Hwang, S.W.; Kobayashi, K.; Zhai, S.; Kanai, I.; Kanai, K. Database of Cross Sectional Optical Micrograph from KYOw Lauraceae Wood. Available online: https://repository.kulib.kyoto-u.ac.jp/dspace/handle/2433/245888 (accessed on 21 April 2022). 95. Wood-Auth; Barmpoutis, P. WOOD-AUTH Dataset A (Version 0.1). Available online: https://doi.org/10.2018/wood.auth (accessed on 21 April 2022). 96. Nasirzadeh, M.; Khazael, A.A.; bin Khalid, M. Woods recognition system based on local binary pattern. In Proceedings of the Second International Conference on Computational Intelligence, Communication Systems and Networks, CICSyN 2010, Liverpool, UK, 28–30 July 2010; pp. 308–313. 97. Khalid, M.; Yusof, R.; Khairuddin, A.S.M. Improved tropical wood species recognition system based on multi-feature extractor and classiﬁer. Int. J. Electr. Comput. Eng. 2011, 5, 495–501. 98. Damayanti, R.; Prakasa, E.; Krisdianto; Dewi, L.M.; Wardoyo, R.; Sugiarto, B.; Pardede, H.F.; Riyanto, Y.; Astutiputri, V.; Panjaitan, G.R.; et al. LignoIndo: Image database of indonesian commercial timber. IOP Conf. Ser. Earth Environ. Sci. 2019, 374, 12057. [CrossRef]


<!-- Page 25 -->


Forests 2022, 13, 2041 25 of 26


99. Kour, A.; Yv, V.; Maheshwari, V.; Prashar, D. A review on image processing. Int. J. Electron. Commun. Comput. Eng. 2012, 4, 2278–4209. 100. Martins, J.; Oliveira, L.S.; Britto, A.S.; Sabourin, R. Forest species recognition based on dynamic classiﬁer selection and dissimilarity feature vector representation. Mach. Vis. Appl. 2015, 26, 279–293. [CrossRef] 101. Yusof, R.; Khalid, M.; Khairuddin, A.S.M. Fuzzy logic-based pre-classiﬁer for tropical wood species recognition system. Mach. Vis. Appl. 2013, 24, 1589–1604. [CrossRef] 102. Yusof, R.; Rosli, N.R.; Khalid, M. Tropical wood species recognition based on gabor ﬁlter. In Proceedings of the 2009 2nd International Congress on Image and Signal Processing, Tianjin, China, 17–19 October 2009; pp. 1–5. 103. Brunel, G.; Borianne, P.; Subsol, G.; Jaeger, M.; Caraglio, Y. Automatic identiﬁcation and characterization of radial ﬁles in light microscopy images of wood. Ann. Bot. 2014, 114, 829–840. [CrossRef] 104. Kobayashi, K.; Hwang, S.-W.; Lee, W.-H.; Sugiyama, J. Texture analysis of stereograms of diffuse-porous hardwood: Identiﬁcation of wood species used in tripitaka koreana. J. Wood Sci. 2017, 63, 322–330. [CrossRef] 105. Tou, J.Y.; Tay, Y.H.; Lau, P.Y. Rotational invariant wood species recognition through wood species veriﬁcation. In Proceedings of the 2009 First Asian Conference on Intelligent Information and Database Systems, Dong hoi, Vietnam, 1–3 April 2009; pp. 115–120. 106. Cavalin, P.R.; Kapp, M.N.; Martins, J.; Oliveira, L.E.S. A multiple feature vector framework for forest species recognition. In Proceedings of the 28th Annual ACM Symposium on Applied Computing—SAC ’13, Coimbra, Portugal, 18–22 March 2013; ACM Press: New York, NY, USA, 2013; p. 16. 107. Yusof, R.; Khairuddin, U.; Rosli, N.R.; Ghafar, H.A.; Azmi, N.M.A.N.; Ahmad, A.; Khairuddin, A.S.M. A Study of feature extraction and classiﬁer methods for tropical wood recognition system. In Proceedings of the TENCON 2018—2018 IEEE Region 10 Conference, Jeju, Republic of Korea, 28–31 October 2018; pp. 2034–2039. 108. Lewis, N.D. Deep Learning Made Easy with R: A Gentle Introduction for Data Science; Platform, C.I.P., Ed.; CreateSpace Independent Publishing Platform: Scotts Valley, CA, USA, 2016; ISBN 1519514212. 109. Zhuo, L.; Cheng, B.; Zhang, J. A Comparative study of dimensionality reduction methods for large-scale image retrieval. Neurocomputing 2014, 141, 202–210. [CrossRef] 110. Fukushima, K. Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position. Biol. Cybern. 1980, 36, 193–202. [CrossRef] [PubMed] 111. Lu, D.; Weng, Q. A Survey of image classiﬁcation methods and techniques for improving classiﬁcation performance. Int. J. Remote Sens. 2007, 28, 823–870. [CrossRef] 112. Ravindran, P.; Costa, A.; Soares, R.; Wiedenhoeft, A.C. Classiﬁcation of CITES-listed and other neotropical meliaceae wood images using convolutional neural networks. Plant Methods 2018, 14, 25. [CrossRef] [PubMed] 113. Andrade, B.G.D.; Vital, B.R.; Carneiro, A.D.C.O.; Basso, V.M.; Pinto, F.D.A.D.C. Potential of texture analysis for charcoal classiﬁcation. Floresta e Ambient. 2019, 26, e20171241. [CrossRef] 114. LeCun, Y.; Bengio, Y.; Hinton, G. Deep learning. Nature 2015, 521, 436–444. [CrossRef] [PubMed] 115. Goodfellow, I.; Bengio, Y.; Courville, A. Deep Learning; MIT Press: Cambridge, UK, 2016; ISBN 9780262035613. 116. Abiodun, O.I.; Kiru, M.U.; Jantan, A.; Omolara, A.E.; Dada, K.V.; Umar, A.M.; Linus, O.U.; Arshad, H.; Kazaure, A.A.; Gana, U. Comprehensive review of artiﬁcial neural network applications to pattern recognition. IEEE Access 2019, 7, 158820–158846. [CrossRef] 117. Schmidhuber, J. Deep learning in neural networks: An overview. Neural Networks 2015, 61, 85–117. [CrossRef] 118. Yu, Y.; Si, X.; Hu, C.; Zhang, J. A review of recurrent neural networks: LSTM cells and network architectures. Neural Comput. 2019, 31, 1235–1270. [CrossRef] 119. Panzer, M.; Bender, B. Deep reinforcement learning in production systems: A systematic literature review. Int. J. Prod. Res. 2022, 60, 4316–4341. [CrossRef] 120. Gu, J.; Wang, Z.; Kuen, J.; Ma, L.; Shahroudy, A.; Shuai, B.; Liu, T.; Wang, X.; Wang, G.; Cai, J.; et al. Recent advances in convolutional neural networks. Pattern Recognit. 2018, 77, 354–377. [CrossRef] 121. Huang, T.S. Computer vision: Evolution and promise. Comput. Sci. 1996. [CrossRef] 122. Carriquiry, A.; Hofmann, H.; Tai, X.H.; VanderPlas, S. Machine learning in forensic applications. Signiﬁcance 2019, 16, 29–35. [CrossRef] 123. Camps-Valls, G.; Tuia, D.; Zhu, X.X.; Reichstein, M. Deep Learning for the Earth Sciences; Camps-Valls, G., Tuia, D., Zhu, X.X., Reichstein, M., Eds.; Wiley: Hoboken, NJ, USA, 2021; ISBN 9781119646143. 124. Singh, S.P.; Kumar, A.; Darbari, H.; Singh, L.; Rastogi, A.; Jain, S. Machine translation using deep learning: An overview. In Proceedings of the 2017 International Conference on Computer, Communications and Electronics (Comptelix), Jaipur, India, 1–2 July 2017; pp. 162–167. 125. Clanuwat, T.; Bober-Irizar, M.; Kitamoto, A.; Lamb, A.; Yamamoto, K.; Ha, D. Deep learning for classical japanese literature. In Proceedings of the Workshop on Machine Learning for Creativity and Design, Vancouver, BC, Canada, 9 December 2018. 126. Li, Y.; Huang, C.; Ding, L.; Li, Z.; Pan, Y.; Gao, X. Deep learning in bioinformatics: Introduction, application, and perspective in the big data era. Methods 2019, 166, 4–21. [CrossRef] 127. Esteban, L.G.; Fernández, F.G.; de Palacios, P.; Romero, R.M.; Cano, N.N. Artiﬁcial neural networks in wood identiﬁcation: The case of two juniperus species from the canary islands. IAWA J. 2009, 30, 87–94. [CrossRef]


<!-- Page 26 -->


Forests 2022, 13, 2041 26 of 26


128. Turhan, K.; Serdar, B. Support vector machines in wood identiﬁcation: The case of three salix species from Turkey. Turk. J. Agric. For. 2013, 37, 249–256. [CrossRef] 129. Hafemann, L.G.; Oliveira, L.S.; Cavalin, P. Forest species recognition using deep convolutional neural networks. In Proceedings of the 2014 22nd International Conference on Pattern Recognition, Stockholm, Sweden, 24–28 August 2014; pp. 1103–1107. 130. Esteban, L.G.; de Palacios, P.; Conde, M.; Fernández, F.G.; García-Iruela, A.; González-Alonso, M. Application of artiﬁcial neural networks as a predictive method to differentiate the wood of Pinus sylvestris, L. and pinus nigra arn subsp. Salzmannii (dunal) franco. Wood Sci. Technol. 2017, 51, 1249–1258. [CrossRef] 131. Kwon, O.; Lee, H.G.; Lee, M.-R.; Jang, S.; Yang, S.-Y.; Park, S.-Y.; Choi, I.-G.; Yeo, H. Automatic wood species identiﬁcation of korean softwood based on convolutional neural networks. J. Korean Wood Sci. Technol. 2017, 45, 797–808. [CrossRef] 132. De Oliveira, W.; Filho, P.L.d.P.; Martins, J.G. Software for forest species recognition based on digital images of wood. FLORESTA 2018, 49, 543–552. [CrossRef] 133. Kwon, O.; Lee, H.G.; Yang, S.-Y.; Kim, H.; Park, S.-Y.; Choi, I.-G.; Yeo, H. Performance enhancement of automatic wood classiﬁcation of korean softwood by ensembles of convolutional neural networks. J. Korean Wood Sci. Technol. 2019, 47, 265–276. [CrossRef] 134. Kanayama, H.; Ma, T.; Tsuchikawa, S.; Inagaki, T. Cognitive spectroscopy for wood species identiﬁcation: Near infrared hyperspectral imaging combined with convolutional neural networks. Analyst 2019, 144, 6438–6446. [CrossRef] 135. He, T.; Marco, J.; Soares, R.; Yin, Y.; Wiedenhoeft, A. Machine learning models with quantitative wood anatomy data can discriminate between swietenia macrophylla and swietenia mahagoni. Forests 2019, 11, 36. [CrossRef] 136. Deklerck, V.; Mortier, T.; Goeders, N.; Cody, R.B.; Waegeman, W.; Espinoza, E.; Van Acker, J.; Van den Bulcke, J.; Beeckman, H. A protocol for automated timber species identiﬁcation using metabolome proﬁling. Wood Sci. Technol. 2019, 53, 953–965. [CrossRef] 137. De Geus, A.R.; da Silva, S.F.; Gontijo, A.B.; Silva, F.O.; Batista, M.A.; Souza, J.R. An analysis of timber sections and deep learning for wood species classiﬁcation. Multimed. Tools Appl. 2020, 79, 34513–34529. [CrossRef] 138. Wu, F.; Gazo, R.; Haviarova, E.; Benes, B. Wood identiﬁcation based on longitudinal section images by using deep learning. Wood Sci. Technol. 2021, 55, 553–563. [CrossRef] 139. Shugar, A.N.; Drake, B.L.; Kelley, G. rapid identiﬁcation of wood species using XRF and neural network machine learning. Sci. Rep. 2021, 11, 17533. [CrossRef] 140. Da Silva, N.R.; Deklerck, V.; Baetens, J.; Van den Bulcke, J.; De Ridder, M.; Rousseau, M.; Bruno, O.M.; Beeckman, H.; Van den Acker, J.; De Baets, B.; et al. Improved wood species identiﬁcation based on multi-view imagery of the three anatomical planes. Prepr. from Res. Sq. 2022, 18, 79. [CrossRef] 141. Chai, J.; Zeng, H.; Li, A.; Ngai, E.W.T. Deep learning in computer vision: A critical review of emerging techniques and application scenarios. Mach. Learn. with Appl. 2021, 6, 100134. [CrossRef] 142. Goodfellow, I.; Pouget-Abadie, J.; Mirza, M.; Xu, B.; Warde-Farley, D.; Ozair, S.; Courville, A.; Bengio, Y. Generative adversarial nets. In Proceedings of the Advances in Neural Information Processing Systems, Montreal, QC, Canada, 8–13 December 2014. 143. Yi, X.; Walia, E.; Babyn, P. Generative adversarial network in medical imaging: A review. Med. Image Anal. 2019, 58, 101552. [CrossRef] 144. Lopes, D.J.V.; Monti, G.F.; Burgreen, G.W.; Moulin, J.C.; dos, S.; Bobadilha, G.; Entsminger, E.D.; Oliveira, R.F. Creating highresolution microscopic cross-section images of hardwood species using generative adversarial networks. Front. Plant Sci. 2021, 12, 760139. [CrossRef] 145. Hu, K.; Wang, B.; Shen, Y.; Guan, J.; Cai, Y. Defect identiﬁcation method for poplar veneer based on progressive growing generated adversarial network and MASK R-CNN model. BioResources 2020, 15, 3040–3052. [CrossRef] 146. Habite, T.; Abdeljaber, O.; Olsson, A. Automatic detection of annual rings and pith location along norway spruce timber boards using conditional adversarial networks. Wood Sci. Technol. 2021, 55, 461–488. [CrossRef] 147. Shu, D.; Park, S.W.; Kwon, J. 3D Point cloud generative adversarial network based on tree structured graph convolutions. In Proceedings of the 2019 IEEE/CVF International Conference on Computer Vision (ICCV), Seoul, Republic of Korea, 27 October–2 November 2019; pp. 3858–3867. 148. UTAR; FRIM. MyWood-Premium. Available online: https://mywoodid.frim.gov.my/ (accessed on 20 July 2022). 149. Tay, Y.H. XYLORIX: An AI-as-a-service platform for wood identiﬁcation. In Proceedings of the IAWA-IUFRO International Symposium for Updating Wood Identiﬁcation, Beijing, China, 20–22 May 2019. 150. Agritix Xylorix. Available online: https://www.xylorix.com/products/ (accessed on 4 May 2022). 151. XyloTron.org XyloTron. Available online: https://xylotron.org/ (accessed on 4 May 2022). 152. The National Academies of Sciences, Engineering, and Medicine. Available online: https://sites.nationalacademies.org/PGA/ PEER/PEERscience/PGA_195537 (accessed on 4 May 2022). 153. Universidad Politécnica de Madrid, Universidad de Granada, Asociación Española del Comercio e Industria de la Madera. (AEIM) IMAI App.
