# kilic2025-wd-detector


<!-- Page 1 -->


European Journal of Wood and Wood Products (2025) 83:50 https://doi.org/10.1007/s00107-025-02211-5


## ORIGINAL ARTICLE


WD Detector: deep learning-based hybrid sensor design for wood defect detection


Kenan Kılıç1,2 · Kazım Kılıç3,4 · İbrahim Alper Doğru5 · Uğur Özcan6


Received: 2 June 2024 / Accepted: 22 January 2025 / Published online: 4 February 2025 © The Author(s) 2025


Abstract The fast-growing human demands in the world are leading to the expansion of industrialization. As wooden materials are increasingly used in industrial settings, detecting defects in wood has become crucial. Wood defects adversely affect the quality and durability of materials. A wood defect detection method, named WD Detector, is proposed in this study to identify wood defects. There are 18,284 defective wood surface images and 1,992 undefect wood images in a dataset of 20,276 wood images used for wood defect detection. 12 different classical machine learning algorithms are used to clas­ sify wood defects after extracting features from images with various CNNs and transfer learning approaches. In this study, feature extraction is performed by training the Xception CNN model. Once the features are extracted, classical machine learning algorithms are used to classify the wood defects. For the first time, a deep learning-based hybrid sensor design has been implemented on this dataset for wood defect detection. WD Detector achieved 99.32% accuracy in detecting wood surface defects using the new method. The success of this study’s method in detecting wood defects is believed to pave the way for future studies.


Kenan Kılıç


kenan.kilic@bozok.edu.tr


Kazım Kılıç kazim.kilic@bozok.edu.tr


İbrahim Alper Doğru iadogru@gazi.edu.tr


Uğur Özcan uozcan@gazi.edu.tr


1 Department of Wood Products Industrial Engineering, Graduate School of Natural and Applied Sciences, Gazi University, Teknikokullar, Ankara 06560, Turkey


2 Department of Design, Vocational School of Yozgat, Yozgat Bozok University, Yozgat 66100, Turkey


3 Department of Computer Engineering, Graduate School of Natural and Applied Sciences, Gazi University, Teknikokullar, Ankara 06560, Turkey


4 Department of Computer Programming, Vocational School of Yozgat, Yozgat Bozok University, Yozgat 66100, Turkey


5 Department of Computer Engineering, Faculty of Technology, Gazi University, Teknikokullar, Ankara 06560, Turkey


6 Department of Wood Products Industrial Engineering, Faculty of Technology, Gazi University, Teknikokullar, Ankara 06560, Turkey


## 1  Introduction


In woodworking industry and forest industrial engineering, the detection of wood surface defects is critical for qual­ ity control. Early detection of defects enables the quick removal of defective products from the production line, thus increasing production efficiency and quality. Defects can be caused by poor quality raw materials and inappropriate production processes and can reduce the commercial value and mechanical properties of wood products. Woodworking industries require an effective defect detection and identi­ fication system. These processes are carried out by trained personnel.


In the woodworking industry, material utilisation, wast­ age and costs affect the production processes. The heteroge­ neous structure of wood weakens its mechanical properties and leads to various defects, which reduces its aesthetic and commercial value. Major wood defects include cracks, fungal damage, knots and insect damage. Wood quality and price are determined by size, species, defect location and intended use (Broman and Fredrikson 2012; Ding et al. 2020; Çetiner et al. 2014). With Industry 5.0, the demand for automated fault detection in manufacturing industries is growing rapidly. These systems reduce production costs while increasing productivity and enabling further analyses


1 3


<!-- Page 2 -->


## 50 Page 2 of 13


with online data. They also alleviate economic challenges in this area by reducing labour costs (Haoran et al. 2021; Lin and Sanjaya 2021; Zhang et al. 2016a).


The woodworking industry is critical to the economy of many developing countries. As wood is a biological mate­ rial, it is affected by environmental and processing condi­ tions, which leads to the prevalence of defects; these defects can significantly affect the aesthetic and structural integrity of wood (Qayyum et al. 2016). Therefore, producers use trained labour to detect and remove defective wood from the production line (Lim et al. 2022). Although automation is increasing, many industry leaders still rely on trained spe­ cialists for quality control, but these manual processes are time-consuming and error-prone (Gu et al. 2009; Urbonas et al. 2019). In addition, the reliability of manual examinations is generally low and it is difficult to achieve reliability above 70% (Lycken 2016). Automated systems provide more reli­ able results than human inspections, and deep learning tech­ nologies have made great advances in this area (Liu et al. 2018). However, visual detection of wood defects and grad­ ing at the right speed still pose a challenge, which can lead to human errors and potential loss of revenue (Ren 2019; Jabo 2011).


The goal of artificial intelligence in wood defect detec­ tion is to develop intelligent machines close to human intel­ ligence. Machine learning provides an effective method for automatic wood defect detection. The data set obtained from wood surface images is trained, features extracted and clas­ sified by Convolutional Neural Network (CNN) and transfer learning. This is a hybrid approach study used.


In this study, the performance of image processing and artificial intelligence methods for the detection of wood surface defects is analysed. The dataset was adapted for binary classification to detect defective and perfect wood and a hybrid model consisting of Xception and tree-based augmented ensemble classifiers was proposed. The perfor­ mance of the model is optimised by fine-tuning the Xcep­ tion architecture. The bias of the results is reduced by using cross-validation and comparative analysis with twelve dif­ ferent classifiers is presented. This work provides important contributions for the wood industry. The article is divided into five sections. Firstly, Sect. 2 presents the relevant lit­ erature. Secondly, Sect.  3 provides details about the pro­ posed method and information about the dataset. Thirdly, a comparative analysis of the findings is presented in Sect. 4. Fourthly, Chap. 5 includes information about the results of the study. Lastly, future studies are discussed in Chap. 5.


1 3


European Journal of Wood and Wood Products (2025) 83:50


## 2  Literature review


Wood is a commonly used building material across many industries due to its natural properties and environmentally friendly structure. However, the use of defective wood can lead to economic losses and safety risks. Therefore, early detection and classification of defects is important. In recent years, the decline of wood resources has increased the importance of sustainable use. Fast and effective detec­ tion of wood surface defects can improve the utilization efficiency of wood (Pölzleitner and Schwingshakl 1992; Schmoldt et al. 1997; Norlander et al. 2015).


Traditionally, wood grading has been done manually. Automatic classification machines are currently being employed on a large scale to expedite the process. It is pos­ sible to perform different classification tasks by utilizing the same set of mechanical devices but altering the classification task at hand. Among these tasks, classification is perhaps the most important (Hu et al. 2019). In contrast to traditional methods, the methods used to detect wood surface defects involve computer analysis of images of the wood surface. In this process, a Charge-Coupled Device (CCD) camera is commonly utilized. The processes of detecting surface defects are based on the design of image analysis algo­ rithms. In general, digital image processing techniques are used (Xie 2013). Classification processes usually start with image preprocessing techniques that follow steps such as grayscale conversion, histogram smoothing, and spatial or frequency domain filtering. Wood surface images are then processed to identify defects. In the final stage, a machine learning algorithm is used to classify the images (Chen et al. 2023a).


Machine learning (ML) consists of a set of techniques that use various algorithms to enable computers to improve performance for a given task by learning from the data given to it. ML algorithms can be broadly categorized into three types: unsupervised learning, supervised learning, and rein­ forcement. Commonly used machine learning algorithms include Random Forest Classifier, K Neighbours Classifier, Support Vector Machine, DecisionTreeClassifier, Naive Bayes, Logistic Regression, Gradient Boosting Classifier, XGB Classifier, LightGBM, CatBoost, AdaBoost and MLP Classifier. The preferred methods for detecting and classify­ ing surface defects and knots present in wood combine digi­ tal image processing and machine learning algorithms (Qi et al. 2010; Mu and Qi 2009). The mentioned method is very useful not only for the detection of wood surface defects but also for the quality control of automated production systems in different industries such as ceramics, pharmaceuticals, and textiles (Gao et al. 2021; Liu et al. 2021; Shahrabadi et al. 2022; Zhang et al. 2023).


<!-- Page 3 -->


European Journal of Wood and Wood Products (2025) 83:50


Detection and control of surface defects in industrial products is a very promising area of academic research. For example, fabric defect detection (Raheja et al. 2013; Liu and Zheng 2020; Liu and Le 2021), leather surface defect detec­ tion (Hoang et al. 1997; Chen et al. 2024), pharmaceutical industry defect detection (Galata et al. 2021), surface defect detection for electronic devices (Tsai and Huang 2019; Chen et al. 2023b), defect detection on metal surfaces (Tao et al. 2018), crack detection in concrete (Lei et al. 2024), and mobile phone There are important studies on the detec­ tion of surface defects (Jian et al. 2017).


There are also studies specific to the wood processing industry sector in the literature. Zhang et al. (2015) per­ formed defect detection in wood planks using the principal component analysis (PCA) method. YongHua and Jin-Cong (2015) developed a hybrid wood defect detection method by using Gray Level Commonality Matrix (GLCM) and Tamura texture together for knot defect detection. Li et al. (2017) studied wood defect detection using compressed sen­ sor images with linear discriminant analysis (LDA). Chang et al. (2018) performed wood defect detection with the original image and defective wood images using subtractive


Table 1  Literature summary Reference Data Num­ ber of Image


Page 3 of 13 50


optimization (CO) and Otsu segmentation methods. Li et al. (2019) developed a defect detection algorithm to detect defects in birch plywood with a system in the form of a local binary and differential excitation system.


Urbonas et al. (2019), defect detection and classifica­ tion on plywood surfaces is achieved using a faster regionbased convolutional neural network (faster R-CNN). Shi et al. (2020) created and used an at-a-glance multi-channel max-region convolutional neural network (R-CNN) used to detect defects in wood plywood, an algorithm that emerged for high speed and accuracy in continuous production. Wu et al. (2022) performed wood defect detection by combin­ ing features. Support Vector Machine (SVM) is used in this defect detection method.


In this research conducted with the wood defect detec­ tion method, there is no previous literature on the classical machine learning approach for the data set used. However, a literature summary on general wood defect detection is presented in order to evaluate it together with existing stud­ ies Table 1.


Methodology Techniques Application


Pölzleitner and Schwingshakl (1992)


Surface grading of profiled wooden boards


## 500 Manual wood grading Real-Time/Feature vector Spruce boards


Zhang et al. (2015)


Live knots, dead knots, and cracks


## 50 PCA and compressed sensing


Principal Component Analysis (PCA), Compressed Sensing


Wood plate defect identification YongHua and Jin-Cong (2015)


University of Oulu, Fin­ land (wood knot defects)


## 395 Hybrid method based on texture features


Tamura texture, Grey-Level Co-occurrence Matrix (GLCM)


Detection of dead knots, poles, and living knots Li et al. (2017) Live knots, dead knots, and cracks


## 50 LDA and compressed sensor images


Chang et al. (2018)


Pinhole, crack, live knot and dead knot (X. congestum wood plates)


Linear Discriminant Analysis (LDA), Compressed Sensor Images


Wood defect detection


## 320 Convex optimization and Otsu segmentation


Convex Optimization, Otsu Segmentation


Comprehensive wood surface defect image evaluation Li et al. (2019) Birch Ice Cream Bar Imaging Equipment and Image Data Set


## 443 Local Binary Pattern and Local Binary Dif­ ferential Excitation


Local Binary Pattern, Local Binary Differential Excitation


Classification of cracks and linear mineral lines on birch veneer surface Urbonas et al. (2019)


Wood veneer durface defects 353 Faster R-CNN Region-Based Convolutional Neural Network (Faster R-CNN)


Automatic visual inspection of wood veneer surfaces Shi et al. (2020)


Wood veneer image 2,838 Glance Multi-Channel Mask R-CNN


Glance network, Multi-Chan­ nel Mask R-CNN


Efficient method for wood veneer defect detection Wu et al. (2022)


A large-scale image dataset of wood surface defects for automated vision-based quality control processes


1,440 Feature fusion and Sup­ port Vector Machine


Proposed Study


A large-scale image dataset of wood surface defects for auto­ mated vision-based quality control processes


Support Vector Machine (SVM)


Wood surface defect detection based on feature fusion


20,276 WD Detector Hybrid (CNN feature extrac­ tion and machine learning classification)


Wood defect detection binary classification


1 3


<!-- Page 4 -->


## 50 Page 4 of 13


## 3  Materials and methods


In this section, neither the information about the data set used nor the technical details of the proposed hybrid model are explained. Within the scope of the research, feature extrac­ tion is performed using convolutional neural networks and transfer learning methods. Then, the obtained features are classified with different classical machine learning classifi­ cation algorithms and wood defect detection is performed.


## 3.1  Dataset


There are 20,276 wood images in the data set. Of these images, 1,992 are undefect of any surface defects, while 18,284 had wood surface defects. Overall, 10 types of com­ mon wood surface defects are covered. The dataset contains 20,276 wood surface images containing ten common types of wood defects, including knots, cracks, blue stains, resin, and heartwood (Kodytek et al. 2021). Figure 1 shows exam­ ples of wood defects within the dataset.


1,992 of these images have undefect wood surface images. A total of 18,284 images contained wood images containing one or more surface defects. On average, each image has 2.2 defects. 6.7% of images have more than 3 defects. The most defects in a single image are 16.


In the wood industry’s quality control processes, it’s more crucial to identify if the wood is defective than to determine the type of defect it has. Therefore, this study focuses solely on identifying the presence of defects in the wood, without considering the specific types of defects.


## 3.2  Data augmentation and data preprocessing


The initial 1,992 images of undefect wood are increased by data augmentation to 18,284 to balance the number of defect wood. Since the data set contains significantly more defect samples compared to undefect samples, it is impor­ tant to balance the data set. Data augmentation is a process of adding data to increase and stabilize the number of data to be processed (Purnama et al. 2019). High-rate sampling and


European Journal of Wood and Wood Products (2025) 83:50


subsampling methods are commonly used in imbalanced datasets. Studies show that data augmentation increases the success of classification problems with deep learning network architectures (Lopez et al. 2017; Ayan and Ünver 2018). Data augmentation is performed with the Augmen­ tor library to prevent defect and defective class imbalance in the dataset and to improve the performance of the deep learning architecture. The features used in this library are as follows: vertical and horizontal rotation, rotation up to a maximum angle of 355 degrees, zoom values ranging from 1.1 to 1.5, and random brightness and contrast enhance­ ment with a maximum value of 0.2. As a result, a total of 36,568 samples are generated. To improve the effectiveness of the proposed approach, the BMP images with an original resolution of 2800 × 1024 pixels are resized to obtain jpeg images with a resolution of 300 × 300 pixels. The data pre­ processing data augmentation stage is shown in Fig. 2.


## 3.3  Deep learning


Deep learning is fundamentally based on artificial neu­ ral networks. These structures can process large amounts of data by learning from their representatives. As a result, deep neural networks have more hidden layers compared to conventional neural networks. Within deep neural net­ works, labeled input values are passed to non-linear acti­ vation functions to produce a specific output with specific weights (Schmidhuber 2015). The goal of training a deep neural network is to minimize the error value by optimizing these weights (Ergün and Kılıç 2021).


## 3.3.1  Convolutional neural network


Convolutional Neural Networks (CNN) are a trainable mul­ tilayer architecture consisting of numerous feature extrac­ tion stages. Three layers make up each stage. These layers are the convolutional layer, nonlinear layer, and pooling layer, respectively (Zhang et al. 2016). Computer vision applications often use CNN, which is a crucial part of deep learning. CNN detects visual patterns in pixel images with


Fig. 1  Wood defects within the dataset. A live knot, B dead knot, C quartzity, D knot with crack, E knot missing, F crack, G overgrowth, H resin, I marrow, and J blue stain (Kodytek et al. 2021)


1 3


<!-- Page 5 -->


European Journal of Wood and Wood Products (2025) 83:50


Fig. 2  The data augmentation phase of data preprocessing


Fig. 3  Schematic representation of the general structure of a typical CNN


minimal pre-processing. This has led to its widespread use in image-based perception research (Ishengoma et al. 2022). CNN has achieved significant success and is widely used in various applications. Instead of traditional classification techniques, CNNs are one of the most commonly used clas­ sification methods in image classification processes (Ben­ brahim and Behloul 2021).


CNNs consist of three basic components: convolution layers, pooling layers, and fully connected layers. Convo­ lution layers work by using filters to extract patterns and features from the input image. Pooling layers reduce infor­ mation density by decreasing the size of maps and the num­ ber of weights of map objects. This process is also called subsampling. The feature matrix obtained from convolu­ tion and pooling layers is usually multidimensional, so it is smoothed to a one-dimensional vector before moving to the fully connected layer. The fully connected layer uses this one-dimensional feature vector to train the deep neural network and perform classification tasks (Ergün and Kılıç 2021). Figure 3 shows the general schematic structure of a CNN architecture.


3.3.1.1  Convolutional layer  The convolution layer is a critical part of a CNN and plays an important role in image processing. Because images are often localized, patterns in one region can be thought of as occurring elsewhere. By taking a small section of a large image and moving it across the entire image (input), we can transform each point into a single location (output). The small sections that move over this large image are called filters or kernels. Filters are cre­


Page 5 of 13 50


ated using the backpropagation technique (LeCun and Ben­ gio 1995).


3.3.1.2  Subsampling or pooling layer  Pooling in CNNs refers to the process of subsampling an image. It involves selecting a portion of the output to obtain a single output value. There are different pooling techniques such as maxi­ mum pooling, average pooling and mean pooling. Pooling reduces the computational burden by reducing the number of parameters while at the same time giving the network the ability to handle changes in shape, size, and scale (Atacak et al. 2022).


3.3.1.3  Fully connected layer  A fully connected layer con­ sists of a one-dimensional matrix connected to all neurons of the previous layer. These layers are usually used towards the end of the CNN architecture and to optimize class scores. In addition, the number of these layers may increase or decrease in deep learning-based architectures (Sultana et al. 2018).


## 3.3.2  Xception


Xception is a type of CNN designed and developed by François Chollet. Xception architecture is very effective on large and complex data sets, especially when used in image classification, object detection, and other imagebased tasks. It has been trained on over one million images


1 3


<!-- Page 6 -->


## 50 Page 6 of 13


from the ImageNet database and works with image input of 224 × 224-pixel dimensions. By not compressing the input data and reducing it into smaller pieces, it maps geometric correlations separately for all output channels and creates a 1 × 1 depth convolution to reach a correlation in the chan­ nels (Chollet 2017). The general outline and details of the Xception architecture are shown in Fig. 4.


## 3.4  Transfer learning


The transfer learning approach is a deep learning tool based on using a model that has been previously trained with a large and comprehensive set for a problem. Instead of train­ ing the CNN model from scratch, it is much faster and easier to fine-tune the model using transfer learning techniques (Weiss et al. 2016; Fırıldak and Talu 2019).


## 3.5  Experimental installation


The materials used in this research, wood and undefect wood surface images, are divided into two categories. Due to the limited number of undefect wood images, the num­ ber of images in the training set is increased to increase the consistency of the method reduce its bias, and increase the performance of the network. With this increase, the number of undefect wood images equals the number of defective wood images. However, the data augmentation is only per­ formed on the training set. In total, the dataset consists of


Fig. 4  Xception architecture schematic representation (Chollet 2017)


1 3


European Journal of Wood and Wood Products (2025) 83:50


20,276 images, 1,992 undefect wood images, and 18,284 defect wood images. The undefect wood images are aug­ mented with the Augmentor library to reach 18,284. In total, experiments are performed on 36,568 wood surface images.


Six different well-known CNN architectures (VGGNet, ResNet50, MobileNet, DenseNet121, Xception, and Incep­ tionV3) are trained with images for wood defect detection. Each is trained with the same hyperparameters. Instead of starting the training from scratch, a transfer learning method is preferred. This method aims to avoid overfitting, save time, and increase accuracy. ImageNet weights are used for the weights. Well-known transfer learning architectures include feature extraction layers and an additional classifier softmax layer. In addition, the “Adam” activation function is used for activation within the network. In the experiments, a batch normalization layer, a fully connected layer, and a dropout layer with a dropout rate of 0.25 are added before the softmax layer of these architectures. This aims to pre­ vent over-fitting of the network and to perform fine-tuning.


In the experiments, different optimization algorithms such as Adam, RMSprop, Adadelta, Adagrad, and SGD are used for comparative analysis. At the same time, for the most successful optimizer, 256, 512, 1024, and 2048 neu­ rons are added to each architecture, and their performances are measured separately.


In the experiments, learning rates of 0.0001 are set as a standard at the beginning of the training of the networks. In each training cycle, the validation loss is checked and if


<!-- Page 7 -->


European Journal of Wood and Wood Products (2025) 83:50


Fig. 5  WD Detector: Schematic representation of the deep learn­ ing-based hybrid detector design for wood defect detection


Table 2  Performance of classical machine learning classification algorithms for feature extraction via Xception


Page 7 of 13 50


Algorithms AUC Precision Recall F1-Score Accuracy Xception + RandomForestClassifier 0.9974 0.9931 0.9931 0.9931 0.9931 Xception + KNeighborsClassifier 0.9885 0.9893 0.9894 0.9894 0.9894 Xception + Support Vector Machine 0.9987 0.9926 0.9927 0.9926 0.9927 Xception + DecisionTreeClassifier 0.9881 0.9886 0.9886 0.9886 0.9886 Xception + Naive Bayes 0.9941 0.9923 0.9923 0.9923 0.9923 Xception + LogisticRegression 0.9991 0.9925 0.9925 0.9925 0.9925 Xception + GradientBoostingClassifier 0.9991 0.9931 0.9931 0.9931 0.9931 Xception + XGBClassifier 0.9990 0.9928 0.9928 0.9928 0.9928 Xception + LightGBM 0.9990 0.9928 0.9928 0.9928 0.9928 Xception + CatBoost 0.9991 0.9932 0.9932 0.9932 0.9932* Xception + AdaBoost 0.9946 0.9921 0.9922 0.9922 0.9922 Xception + MLPClassifier 0.9981 0.9919 0.9919 0.9919 0.9919


the loss does not decrease for 5 epochs, the learning rate is reduced by 50%. Thus, the aim is to use a dynamic learning rate. Since the study involves a large number of experiments and comparative analysis, the number of epochs is set to 20, taking into account the training times. The batch size is set to 64 considering the RAM and graphics card capacity and data size.


As a result of the analysis, the most successful Xcep­ tion architecture is determined as the feature extractor in the hybrid architecture proposed in this study. The features extracted by the Xception architecture are classified with different classical machine learning techniques. For the validity of the results, the cross-validation technique is used in the classification phase.


The experiments are carried out in the Kaggle kernels cloud environment at Google running on the Nvidia Tesla P100 graphics card. Python programming language is used for the software. Figure 5 shows a schematic representation of the WD Detector.


## 4  Results and discussion


With the hybrid approach, the Xception CNN architecture RMSprop optimization algorithm used in deep learning is optimized and the highest accuracy is found with 512 neu­ rons. As a result of investigating whether the 97.57% accu­ racy rate obtained here can be brought to higher levels, the features extracted by the CNN architecture are classified with classical machine learning classification algorithms, and hybrid approach wood surface defect detection experi­ ments are carried out. It should be taken into account that the features extracted with CNN are used by optimizing instead of the normal CNN architecture and are extracted by training the model with a transfer learning approach. Classification is performed with classification algorithms without feature selection of 2048 features consisting of a batch normalization layer added at the end of the optimized Xception architecture. The performance of the classifica­ tion algorithms with the WD detector (hybrid approach) is given in Table 2. The performances of the classification algorithms are evaluated using the same hyperparameters for comparison.


1 3


<!-- Page 8 -->


## 50 Page 8 of 13


The classification algorithms with the hybrid approach have high AUC values between 98.81% and 99.91%. This indicates that the classification ability of the models is gen­ erally high. Precision values are generally high, around 99% for most algorithms, indicating that the algorithms’ positive predictions are generally accurate. Precision val­ ues are also generally high and around 99%, indicating that the true positive predictions of the algorithms are highly accurate. The F1-Score shows the trade-off between preci­ sion and accuracy All classification algorithms used in the hybrid approach have high F1-Scores ranging from 99.19 to 99.32%. Accuracy values are generally high, between 98.86% and 99.32%, indicating the overall accurate clas­ sification capabilities of the algorithms.


When Table 2 is examined, it is seen that the fine-tuned Xception feature extraction model extracts effective fea­ tures for the ability to distinguish between two classes. Boosting tree-based ensemble classifiers perform success­ fully on these features. The classification performance of SVM, Naïve Bayes and Logistic regression algorithms is similar to boosted tree-based algorithms. KNN and Deci­ sion tree algorithms are relatively unsuccessful compared to other algorithms, but the results obtained by these algo­ rithms are observed to be quite successful when the liter­ ature is examined. Since the data set used in the study is balanced using data augmentation techniques, the Precision and Recall values are close to each other. At the same time, these values ​are similar to the accuracy values. This situa­ tion shows that the proposed method has a similar ability to distinguish between both classes.The classification accu­ racy performance of the WD detector hybrid approach is given in Fig. 6.


According to this table, the accuracy metric is quite high in classification processes using the Xception architecture.


Fig. 6  Classification accuracy performance of the WD detector hybrid approach


1 3


European Journal of Wood and Wood Products (2025) 83:50


While the lowest accuracy value is 98.86%, the highest accuracy value is 99.32%. These results show that combin­ ing the Xception architecture with various classification algorithms generally results in high accuracy. In particular, algorithms such as CatBoost and Gradient Boosting Classi­ fier achieved slightly higher accuracy than the others. This table shows that the different classification algorithms used in combination with the Xception architecture are success­ ful and provide overall high accuracy.


In feature extraction with CNN, all classification algo­ rithms are found to classify 99% of the features. The com­ plexity matrix of all classification algorithms of the WD Detector approach is given in Fig. 7 and the ROC curves of the classification algorithms are given in Fig. 8.


When Fig. 7 is examined, it is seen that the classifiers used in the proposed method have similar numbers of TP and TN values ​in the defect and undefect classes. The FN and FP values are low and the error rates of the classifiers in the defect and undefect classes are balanced. Figure 8 pres­ ents the ROC curves showing the ability of the classifiers to distinguish two classes.


In this study, Xception architecture, which has been finetuned for feature extraction in defect and undefect wood images, was used. The extracted features were classified with different machine learning methods. When the findings of the study were examined, it was observed that boosting tree-based classifiers performed better on the extracted fea­ tures. Transfer learning architecture is successful in feature extraction for the detection of defective woods. However, well-known CNN architectures are dependent on the graph­ ics card and contain a high number of parameters. At the same time, they consume more resources and are disad­ vantageous in terms of speed. Traditional image processing methods are more advantageous in terms of computational


<!-- Page 9 -->


European Journal of Wood and Wood Products (2025) 83:50


Fig. 7  (a) Random Forest Classifier, (b) K Neighbor Classifier, (c) Support Vector Machine. (d) Decision Tree Classifier, (e) Naive Bayes, (f) Logistic Regression, (g) Gradient Boosting Classifier, (h)


Page 9 of 13 50


XGB Classifier, (i) Light GBM, (j) CatBoost, (k) AdaBoost, (l) MLP Classifier WD Detector confusion matrix


1 3


<!-- Page 10 -->


## 50 Page 10 of 13


Fig. 8  Average ROC curve values of the WD detector classification algorithms


European Journal of Wood and Wood Products (2025) 83:50


Table 3  Comparison with similar studies Reference Techniques Application Metrics Zhang et al. (2015) Principal Component Analysis (PCA), Compressed Sensing Wood plate defect identification 92% Accuracy YongHua and Jin-Cong (2015)


Tamura texture, Grey-Level Co-occurrence Matrix (GLCM) Detection of dead knots, poles, and living knots


91.83% Accuracy Li et al. (2017) Linear Discriminant Analysis (LDA), Compressed Sensor Images


Wood defect detection 94% Accuracy Chang et al. (2018) Convex Optimization, Otsu Segmentation Comprehensive wood surface defect image evaluation


94.1% Accuracy Li et al. (2019) Local Binary Pattern, Local Binary Differential Excitation Classification of cracks and linear mineral lines on birch veneer surface


93% Recall Wu et al. (2022) Support Vector Machine (SVM) Wood surface defect detection based on feature fusion


91.26% Accuracy Proposed Method (WD Detector)


Hybrid (CNN feature extraction and machine learning classification)


complexity compared to deep learning methods, but the detection performance is low compared to deep learning methods. In the proposed method, fine-tuning of the Xcep­ tion architecture and classification of the extracted features require expert knowledge. However, the performance of the proposed method is tremendous for defective wood detec­ tion when compared to the literature. There are studies in the literature on the detection of defective woods and their defects. These studies are based on classical machine learn­ ing and classical image processing techniques and their detection performance is low. Table 3 presents the perfor­ mance of similar studies.


Zhang et al. (2015) extracted geometry and regional fea­ tures to detect and classify defects from wood panel images. They applied PCA dimensionality reduction method to these features and achieved 92% accuracy using SOM neural net­ work. YongHua and Jin-Cong (2015) achieved 91.8% detec­ tion accuracy using Artificial Neural Network and GLCM


1 3


Wood defect detection binary classification 99.32%


Accuracy


methods on wood image. These methods require expert knowledge and the selection of relevant features directly affects the classification success. In the method proposed in this study, deep learning based extracted features are more successful in detecting defects. Lie et al. (2017) performed defect detection from compressed sensor images using LDA and neural networks. In the study where feature selection was performed with Fisher method, 94% detection success was achieved. Chang et al. (2019) performed defect detec­ tion from wood panel images using convex optimization and otsu methods. These studies include different optimization, dimensionality reduction, feature selection and segmenta­ tion and classification processes. Our method automates these processes and enables testing with the trained model without requiring expert knowledge. In addition, our trained model can be integrated into the product or application to achieve high detection success.


<!-- Page 11 -->


European Journal of Wood and Wood Products (2025) 83:50


Li et al. (2019) extracted features using LBP and local binary differential excitation pattern method to classify defects on birch veneer surface. The researchers classi­ fied these features using Euclidean similarity and achieved 93% accuracy. Wu et al. (2022) combined HOG feature and GLCM features to detect wood defects. They classi­ fied the features they applied KPCA method with SVM and achieved 91.26% accuracy.


When the studies conducted for the detection of wood defects in the literature are examined, the classification suc­ cess of the proposed method is higher than similar studies. At the same time, similar studies use classical image pro­ cessing techniques. In order for the extracted features to be meaningful, methods such as feature selection and dimen­ sion reduction are needed. In the method proposed in this study, these processes are easier and automated.


As a result, it is seen that the deep learning based transfer learning architecture is more effective than classical meth­ ods in extracting features from wood images and the pro­ posed model is more successful compared to similar studies.


## 5  Conclusion


In wood defect detection, the proposed hybrid approach is used for feature extraction with CNN and classification with classical machine learning algorithms. This new approach is called WD Detector. Optimized CNN architecture Xcpe­ tion architecture RMSprop optimization algorithm is trained with 512 neurons and features are extracted and classified with 12 different classical classification algorithms. All algorithms can detect 99% of wood defects. In this context, the hybrid approach of WD Detector provides high accu­ racy for wood defect detection. Other evaluation metrics also show that wood defect detection is performed with high success. The WD Detector has been trained using the Xception transfer learning approach, and features have been extracted. The following accuracies are obtained for the given machine learning models: Random Forest (99.31%), KNN (98.94%), SVM (99.27%), Decision Tree (98.86%), Naive Bayes (99.23%), Logistic Regression (99.25%), Gradient Boosting (99.31%), XGB (99.28%), LightGBM (99.28%), CatBoost (99.32%), Adaboost (99.22%), and MLP (99.19%). The accuracy rate of the WD detector sys­ tem indicates that it operates successfully. The use of this method in wood defect detection systems for automation, quality control, and production lines will yield positive results. Therefore, it is recommended to employ the WD detector approach that utilizes deep learning and machine learning together for this study.


The objective of this study is to assess the effectiveness of employing image processing and artificial intelligence


Page 11 of 13 50


methods to detect surface defects on wood. The findings obtained from this research will aid in the discovery of techniques and algorithms that can significantly enhance the utilization of wooden materials in industrial processes by enabling early detection of defects. In the future, fur­ ther research can expand the potential of providing more efficient and reliable solutions for industrial applications by keeping up with technological advancements in this area.


Acknowledgements  This research represents a part of Kenan Kılıç’s PhD thesis titled “A Computer Vision-Based Machine Learning Approach for Wood Defect Detection” prepared at Gazi University, Institute of Science, Department of Wood Products Industrial Engi­ neering, Ankara, TÜRKİYE.


Author contributions  KK; He carried out the topic idea, code writing, literature and article writing. KK; provided code and algorithm sup­ port. IAD; He wrote the review and supervised it. UO; carried out the article plan, writing and checking processes.


Funding  Open access funding provided by the Scientific and Techno­ logical Research Council of Türkiye (TÜBİTAK).


Data availability  No datasets were generated or analysed during the current study.


Declarations


Competing interests  The authors declare no competing interests.


Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​n​s​.​o​ r​g​/​l​i​c​e​n​s​e​s​/​b​y​/​4​.​0​/.


## References


Atacak İ, Kılıç K, Doğru İA (2022) Android malware detection using


hybrid ANFIS architecture with low computational cost convolu­ tional layers. PeerJ Comput Sci 8:e1092. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​7​7​1​7​ /​p​e​e​r​j​-​c​s​.​1​0​9​2 Ayan E, Ünver HM (2018) Data augmentation importance for clas­


sification of skin lesions via deep learning. In 2018 Electric Elec­ tronics, Computer Science, Biomedical Engineerings' Meeting (EBBT) (pp. 1–4). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​E​B​B​T​.​2​0​1​8​.​8​3​ 9​1​4​6​9 Benbrahim H, Behloul A (2021) Fine-tuned Xception for image clas­


sification on tiny Imagenet. In 2021 International Conference on Artificial Intelligence for Cyber Security Systems and Privacy (AI-CSP) (pp. 1–4). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​A​I​-​C​S​P​5​2​9​6​ 8​.​2​0​2​1​.​9​6​7​1​1​5​0


1 3


<!-- Page 12 -->


## 50 Page 12 of 13


Broman O, Fredriksson M (2012) Wood material features and techni­


cal defects that affect yield in a finger joint production process. Wood Mater Sci Eng 7(4):167–175. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​8​0​/​1​7​4​ 8​0​2​7​2​.​2​0​1​2​.​6​9​9​4​6​1 Çetiner İ, Var AA, Çetiner H (2014) Wood surface analysis with image


processing techniques. In 2014 22nd Signal Processing and Communications Applications Conference (SIU) (pp. 393–396). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​S​I​U​.​2​0​1​4​.​6​8​3​0​2​4​8 Chang Z, Cao J, Zhang Y (2018) A novel image segmentation approach


for wood plate surface defect classification through convex opti­ mization. J Forestry Res 29(6):1789–1795. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​ 7​/​s​1​1​6​7​6​-​0​1​7​-​0​5​7​2​-​7 Chen Y, Sun C, Ren Z, Na B (2023a) Review of the current state of


application of Wood Defect Recognition Technology. BioRe­ sources 18(1). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​5​3​7​6​/​b​i​o​r​e​s​.​1​8​.​1​.​C​h​e​n Chen Z, Xu D, Deng J, Chen Y, Li C (2023b) Comparative study on


deep-learning-based leather surface defect identification. Meas Sci Technol 35(1):015402. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​8​8​/​1​3​6​1​-​6​5​0​1​/​a​ c​f​b​9​f Chen Z, Zhu Q, Zhou X, Deng J, Song W (2024) Experimental Study


on YOLO-Based Leather Surface Defect Detection. IEEE Access. ​ h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​A​C​C​E​S​S​.​2​0​2​4​.​3​3​6​9​7​0​5 Chollet F (2017) Xception: Deep learning with depthwise separable


convolutions. In Proceedings of the IEEE conference on com­ puter vision and pattern recognition (pp. 1251–1258). ​h​t​t​p​s​:​/​/​d​o​i​.​ o​r​g​/​1​0​.​1​1​0​9​/​C​V​P​R​.​2​0​1​7​.​1​9​5 Ding F, Zhuang Z, Liu Y, Jiang D, Yan X, Wang Z (2020) Detecting


defects on solid wood panels based on an improved SSD algo­ rithm. Sensors 20(18):5315. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​s​2​0​1​8​5​3​1​5 Ergün E, Kılıç K (2021) Derin öğrenme ile artırılmış görüntü seti üzer­


inden cilt kanseri tespiti. Black Sea J Eng Sci 4(4):192–200. ​h​t​t​p​ s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​4​2​4​8​/​b​s​e​n​g​i​n​e​e​r​i​n​g​.​9​3​8​5​2​0 Fırıldak K, Talu MF (2019) Evrişimsel sinir ağlarında kullanılan trans­


fer öğrenme yaklaşımlarının incelenmesi. Comput Sci 4(2):88– 95. ​h​t​t​p​s​:​/​/​d​e​r​g​i​p​a​r​k​.​o​r​g​.​t​r​/​t​r​/​p​u​b​/​b​b​d​/​i​s​s​u​e​/​4​9​5​4​6​/​5​2​7​8​6​3 Galata DL, Meszaros LA, Kallai-Szabo N, Szabo E, Pataki H, Marosi


G, Nagy ZK (2021) Applications of machine vision in pharma­ ceutical technology: a review. Eur J Pharm Sci 159:105717. ​h​t​t​p​s​ :​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​e​j​p​s​.​2​0​2​1​.​1​0​5​7​1​7 Gao M, Qi D, Mu H, Chen J (2021) A transfer residual neural network


based on ResNet-34 for detection of wood knot defects. Forests 12(2):212. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​f​1​2​0​2​0​2​1​2 Gu IY, Andersson H, Vicen R (2009) Automatic classification of


wood defects using support vector machines. In Computer Vision and Graphics: International Conference, ICCVG 2008 Warsaw, Poland, November 10-12, 2008 Revised Papers (pp. 356–367). Springer Berlin Heidelberg. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​6​4​2​-​0​ 2​3​4​5​-​3​_​3​5 Haoran Z, Yuzeng W, Enkai B (2021) Smart Classification System of


Solid Wood Board Based on Convolutional Neural Networks. In 2021 International Conference on Intelligent Computing, Auto­ mation and Systems (ICICAS) (pp. 302–307). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​ r​g​/​1​0​.​1​1​0​9​/​I​C​I​C​A​S​5​3​9​7​7​.​2​0​2​1​.​0​0​0​6​9 He K, Zhang X, Ren S, Sun J (2016) Deep residual learning for image


recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770–778). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​ 1​0​9​/​C​V​P​R​.​2​0​1​6​.​9​0 Hoang K, Wen W, Nachimuthu A, Jiang XL (1997) We are achieving


automation in leather surface inspection. Comput Ind 34(1):43– 54. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​S​0​1​6​6​-​3​6​1​5​(​9​7​)​0​0​0​1​9​-​5 Hu J, Song W, Zhang W, Zhao Y, Yilmaz A (2019) Deep learning for


use in lumber classification tasks. Wood Sci Technol 53:505–517. ​ h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​0​0​2​2​6​-​0​1​9​-​0​1​0​8​6​-​z Ishengoma FS, Rai IA, Ngoga SR (2022) Hybrid convolution neu­


ral network model for a quicker detection of infested maize


1 3


European Journal of Wood and Wood Products (2025) 83:50


plants with fall armyworms using UAV-based images. Ecol Inf 67:101502. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​e​c​o​i​n​f​.​2​0​2​1​.​1​0​1​5​0​2 Jabo S (2011) Machine vision for wood defect detection and


classification. Jian C, Gao J, Ao Y (2017) Automatic surface defect detection for


mobile phone screen glass based on machine vision. Applied Soft Computing 52:348–358. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​a​s​o​c​.​2​0​1​6​.​1​0​.​0​ 3​0 Kodytek P, Bodzas A, Bilik P (2021) A large-scale image dataset of


wood surface defects for automated vision-based quality control processes. F1000Research 10. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​2​6​8​8​%​2​F​f​1​0​0​ 0​r​e​s​e​a​r​c​h​.​5​2​9​0​3​.​2 LeCun Y, Bengio Y (1995) Convolutional networks for images,


speech, and time series. Handb Brain Theory Neural Networks 336110:1995 Lei MF, Zhang YB, Deng E, Ni YQ, Xiao YZ, Zhang Y, Zhang JJ.


(2024). Intelligent recognition of joints and fissures in tun­ nel faces using an improved mask region‐based convolutional neural network algorithm. Comput‐Aided Civ Infrastruct Eng 39(8):1123–1142. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​1​1​/​m​i​c​e​.​1​3​0​9​7 Li C, Zhang Y, Tu W, Jun C, Liang H, Yu H (2017) Soft measurement


of wood defects based on LDA feature fusion and compressed sensor images. J Forestry Res 28(6):1285–1292. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​ 0​.​1​0​0​7​/​s​1​1​6​7​6​-​0​1​7​-​0​3​9​5​-​6 Li S, Li D, Yuan W (2019) Wood defect classification is based on a


two-dimensional histogram constituted by LBP and local binary differential excitation pattern. IEEE Access 7:145829–145842. ​h​t​ t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​A​C​C​E​S​S​.​2​0​1​9​.​2​9​4​5​3​5​5 Lim WH, Bonab MB, Chua KH (2022) An optimized lightweight


model for real-time wood defects detection based on yolov4-tiny. In 2022 IEEE International Conference on Automatic Control and Intelligent Systems (I2CACIS) (pp. 186–191). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​ r​g​/​1​0​.​1​1​0​9​/​I​2​C​A​C​I​S​5​4​6​7​9​.​2​0​2​2​.​9​8​1​5​2​7​4 Lin HI, Sanjaya SD (2021) Wood polish classification for automated


quality inspection based on AI vision. In 2021 21st International Conference on Control, Automation and Systems (ICCAS) (pp. 1974–1977). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​2​3​9​1​9​/​I​C​C​A​S​5​2​7​4​5​.​2​0​2​1​ .​9​6​4​9​9​1​0 Liu G, Li F (2021) Fabric defect detection based on low-rank decom­


position with structural constraints. Visual Comput 38:639–653. ​ h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​0​0​3​7​1​-​0​2​0​-​0​2​0​4​0​-​y Liu G, Zheng X (2020) Fabric defect detection based on information


entropy and frequency domain saliency. Visual Comput 37:515– 528. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​0​0​3​7​1​-​0​2​0​-​0​1​8​2​0​-​w Liu Z, Peng C, Work T, Candau JN, DesRochers A, Kneeshaw D


(2018) Application of machine-learning methods in forest ecol­ ogy: recent progress and future challenges. Environ Reviews 26(4):339–350. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​3​9​/​e​r​-​2​0​1​8​-​0​0​3​4 Liu X, Song L, Liu S, Zhang Y (2021) A review of deep-learning-based


medical image segmentation methods. Sustainability 13:1224. ​h​t​ t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​s​u​1​3​0​3​1​2​2​4 Lopez AR, Giro-i-Nieto X, Burdick J, Marques O (2017) Skin lesion


classification from dermoscopic images using deep learning tech­ niques. In 2017 13th IASTED international conference on bio­ medical engineering (BioMed) (pp. 49–54). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​ /​1​0​.​2​3​1​6​/​P​.​2​0​1​7​.​8​5​2​-​0​5​3 Lycken A (2006) Comparison between automatic and manual quality


grading of sawn softwood. For Prod J 56(4):13–18. Mu H, Qi D (2009) Pattern recognition of wood defects types based


on Hu invariant moments. In 2009 2nd international congress on image and signal processing (pp. 1–5). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​ 1​0​9​/​C​I​S​P​.​2​0​0​9​.​5​3​0​3​8​6​6 Norlander R, Grahn J, Maki A (2015) Wooden knot detection using


convNet transfer learning. In: Paulsen R, Pedersen K (eds) Image analysis. SCIA 2015. Lecture Notes in Computer Science, 9127


<!-- Page 13 -->


European Journal of Wood and Wood Products (2025) 83:50


edn. Springer, Cham. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​3​1​9​-​1​9​6​6​5​-​7​ _​2​2 Pölzleitner W, Schwingshakl G (1992) Real-time surface grading of


profiled wooden boards. Industrial Metrol 2(3–4):283–298. ​h​t​t​p​s​ :​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​0​9​2​1​-​5​9​5​6​(​9​2​)​8​0​0​0​8​-​H Purnama IKE, Hernanda AK, Ratna AAP, Nurtanio I, Hidayati AN,


Purnomo MH, Nugroho SMS, Rachmadi RF (2019) Disease clas­ sification based on dermoscopic skin images using convolutional neural network in teledermatology system. In 2019 international conference on computer engineering, network, and intelligent multimedia (CENIM) (pp. 1–5). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​C​ E​N​I​M​4​8​3​6​8​.​2​0​1​9​.​8​9​7​3​3​0​3 Qayyum R, Kamal K, Zafar T, Mathavan S (2016) Wood defects clas­


sification using GLCM based features and PSO trained neural network. In 2016 22nd International Conference on Automation and Computing (ICAC) (pp. 273–277). IEEE. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​ 1​0​9​/​I​C​o​n​A​C​.​2​0​1​6​.​7​6​0​4​9​3​1 Qi D, Zhang P, Jin X, Zhang X (2010) Study on wood image edge


detection based on Hopfield neural network. 2010 IEEE Int Conf Inform Autom ICIA 2010. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​I​C​I​N​F​A​.​2​0​1​0​ .​5​5​1​2​0​1​4 Raheja JL, Kumar S, Chaudhary A (2013) Fabric defect detection based


on GLCM and Gabor filter: a comparison. Optik 124(23):6469– 6474. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​i​j​l​e​o​.​2​0​1​3​.​0​5​.​0​0​4 Ren YY (2019) Wood Defect Detection and Classification Using Deep


Learning (Master’s thesis, University of Malaya (Malaysia)). Schmidhuber J (2015) Deep learning in neural networks: an overview.


Neural Netw 61:85–117. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​n​e​u​n​e​t​.​2​0​1​4​.​0​ 9​.​0​0​3 Schmoldt DL, Li P, Abbott AL (1997) Machine vision using artificial


neural networks with local 3D neighborhoods. Comput Electron Agric 16(3):255–271. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​S​0​1​6​8​-​1​6​9​9​(​9​7​)​0​0​ 0​0​2​-​1 Shahrabadi S, Castilla Y, Guevara M, Magalhães LG, Gonzalez D,


Adão T (2022) Defect detection in the textile industry using image-based machine learning methods: a brief review. In Journal of Physics: Conference Series 2224(1):012010. IOP Publishing. ​h​ t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​8​8​/​1​7​4​2​-​6​5​9​6​/​2​2​2​4​/​1​/​0​1​2​0​1​0 Shi J, Li Z, Zhu T, Wang D, Ni C (2020) Defect detection of industry


wood veneer based on NAS and multichannel mask R-CNN. Sen­ sors 20(16):4398. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​s​2​0​1​6​4​3​9​8 Sultana F, Sufian A, Dutta P (2018) Advancements in image classifica­


tion using convolutional neural network. In 2018 Fourth Interna­ tional Conference on Research in Computational Intelligence and Communication Networks (ICRCICN) (pp. 122–129). IEEE. ​h​t​t​p​ s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​I​C​R​C​I​C​N​.​2​0​1​8​.​8​7​1​8​7​1​8


Page 13 of 13 50


Tao X, Zhang D, Ma Wp, Liu X, Xu D (2018) Automatic metallic


surface defect detection and recognition with convolutional neu­ ral networks. Appl Sci 8(9):1575. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​a​p​p​8​0​ 9​1​5​7​5 Tsai DM, Huang CK (2019) Defect detection in electronic surfaces


using template-based Fourier image reconstruction. IEEE Trans Compon Packag Manuf Technol 9(1):163–172. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​ .​1​1​0​9​/​T​C​P​M​T​.​2​0​1​8​.​2​8​7​3​7​4​4 Urbonas A, Raudonis V, Maskeliūnas R, Damaševičius R (2019) Auto­


mated identification of wood veneer surface defects using faster region-based convolutional neural network with data augmenta­ tion and transfer learning. Appl Sci 9(22):4898. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​ 0​.​3​3​9​0​/​a​p​p​9​2​2​4​8​9​8 Weiss K, Khoshgoftaar TM, Wang D (2016) A survey of transfer learn­


ing. J Big Data 3:1–40. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​8​6​/​s​4​0​5​3​7​-​0​1​6​-​0​0​4​ 3​-​6 Wu C, Zou X, Yu Z (2022) A detection method for wood surface defect


based on feature fusion. 2022 4th Int Conf Front Technol Inform Comput (ICFTIC) 876–880. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​I​C​F​T​I​C​5​7​6​9​ 6​.​2​0​2​2​.​1​0​0​7​5​1​5​8. Qingdao, China Xie DY (2013) Analysis to situation and countermeasure of wood


manufacture industry of our country. Invest Des 3:85–92. ​h​t​t​p​s​:​/​/​ d​o​i​.​o​r​g​/​1​0​.​3​9​6​9​/​j​.​i​s​s​n​.​1​6​7​3​-​4​5​0​5​.​2​0​1​3​.​0​3​.​0​3​8 YongHua X, Jin-Cong W (2015) Study on the identification of the


wood surface defects based on texture features. Optik-Interna­ tional J Light Electron Opt 126(19):2231–2235. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​ 1​0​.​1​0​1​6​/​j​.​i​j​l​e​o​.​2​0​1​5​.​0​5​.​1​0​1 Zhang Y, Xu C, Li C, Yu H, Cao J (2015) Wood defect detection method


with PCA feature fusion and compressed sensing. J Forestry Res 26:745–751. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​1​6​7​6​-​0​1​5​-​0​0​6​6​-​4 Zhang H, Guan C, Wen J (2016a) Applications and research develop­


ment of nondestructive testing of wood based materials. J For­ estry Eng 1(6):1–9 Zhang L, Zhang L, Du B (2016b) Deep learning for remote sensing


data: a technical tutorial on the state of the art. IEEE Geoscience Remote Sens Magazine 4(2):22–40. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​M​G​ R​S​.​2​0​1​6​.​2​5​4​0​7​9​8 Zhang T, Wang Z, Li F, Zhong H, Hu X, Zhang W, Zhang D, Liu X


(2023) Automatic detection of surface defects based on deep ran­ dom chains. Expert Systems with Applications 229:120472. ​h​t​t​p​s​ :​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​e​s​w​a​.​2​0​2​3​.​1​2​0​4​7​2


Publisher’s note  Springer Nature remains neutral with regard to juris­ dictional claims in published maps and institutional affiliations.


1 3
