# yang2020-dl-manufacturing


<!-- Page 1 -->


materials


Review Using Deep Learning to Detect Defects in Manufacturing: A Comprehensive Survey and Current Challenges


Jing Yang 1,2 , Shaobo Li 1,2,3,* , Zheng Wang 1 , Hao Dong 1 , Jun Wang 1


and Shihao Tang 3


1 School of Mechanical Engineering, Guizhou University, Guiyang 550025, China; jyang23@gzu.edu.cn (J.Y.); gs.wangz17@gzu.edu.cn (Z.W.); gs.hdong19@gzu.edu.cn (H.D.); gs.wangjun19@gzu.edu.cn (J.W.) 2 Guizhou Provincial Key Laboratory of Public Big Data, Guizhou University, Guiyang 550025, China 3 Key Laboratory of Advanced Manufacturing Technology of Ministry of Education, Guizhou University, Guiyang 550025, China; shtang@gzu.edu.cn * Correspondence: lishaobo@gzu.edu.cn


 


Received: 3 November 2020; Accepted: 7 December 2020; Published: 16 December 2020


Abstract: The detection of product defects is essential in quality control in manufacturing. This study surveys stateoftheart deep-learning methods in defect detection. First, we classify the defects of products, such as electronic components, pipes, welded parts, and textile materials, into categories. Second, recent mainstream techniques and deep-learning methods for defects are reviewed with their characteristics, strengths, and shortcomings described. Third, we summarize and analyze the application of ultrasonic testing, ﬁltering, deep learning, machine vision, and other technologies used for defect detection, by focusing on three aspects, namely method and experimental results. To further understand the difﬁculties in the ﬁeld of defect detection, we investigate the functions and characteristics of existing equipment used for defect detection. The core ideas and codes of studies related to high precision, high positioning, rapid detection, small object, complex background, occluded object detection and object association, are summarized. Lastly, we outline the current achievements and limitations of the existing methods, along with the current research challenges, to assist the research community on defect detection in setting a further agenda for future studies.


Keywords: defect detection; quality control; deep learning; object detection


## 1. Introduction


In the manufacture of mechanical products in complex industrial processes, defects such as internal holes [1], pits [2], abrasions [3], and scratches [4] arise, due to failure in design and machine production equipment as well as unfavorable working conditions. Products may also easily corrode [5] and be prone to fatigue [6] because of daily application. These defects increase the costs incurred by enterprises, shorten the service life of manufactured products, and result in an extensive waste of resources, thereby causing substantial harm to people and their safety [7]. Hence, detecting defects is a core competency that enterprises should possess in order to improve the quality of the manufactured products without affecting production. Automatic defect-detection technology has obvious advantages over manual detection. It not only adapts to an unsuitable environment but also works in the long run with high precision and efﬁciency. Research on defect-detection technology can reduce the production cost, improve production efﬁciency and product quality, as well as lay a solid foundation for the intelligent transformation of the manufacturing industry.


Therefore, many scholars have reviewed defect-detection-related technologies and applications to provide references for the application and research of defect-detection technology. For example, in view


Materials 2020, 13, 5755; doi:10.3390/ma13245755 www.mdpi.com/journal/materials


<!-- Page 2 -->


Materials 2020, 13, 5755 2 of 23


of the defect-detection technology applied by pharmaceutical products, Lalit Mohan Kandpal et al. [8]. summarized the application of hyperspectral [9], vibration spectrum [10], infrared [11], and other spectral technologies. For surface defect detection of manufactured products, Xianghua Xie [12] systematically recent advances in surface detection using computer vision and image processing techniques. By comparing the ﬁndings of past studies, they ﬁnd that surface defect detection based on image processing requires high real-time performance in industrial applications. For fabric defect detection, scholars [13,14] reviewed the application and development of defect-detection methods commonly used in the production of textile fabrics from the perspective of defect-detection development of the textile industry production. Thermal imaging technologies are widely used in many industrial areas. I. Jorge Aldave [15] focused on the comparison of results obtained with commercially available non-experimental IR methods to provide references for the cameras in the ﬁeld of non-destructive defect detection. Defect-detection technology is a hot topic in the industry and academia. However, scholars have yet to categorize product defect types (for example, steel [16] and textile [17]), the main detection techniques, summary of applications of defect-detection technology, existing equipment for defect detection, and other prospects. In addition, the mainline, review, and summary of the research status of relevant technologies locally and abroad have yet to be realized.


This paper ﬁrst classiﬁes the common defects of electronic components, pipes, welding parts, and textile materials, as shown in Figure 1. Then, it summarizes the mainstream deep-learning technology for defect detection and its application status and analyzes the application situation of the main defect-detection equipment, in order to provide reference for defect-detection technology in theory and practical application.


Figure 1. Defects in different areas: (a) metallization peeloff of electronic components [18]. (b) pipeline corrosion [19]. (c) defective with gas pore [20]. (d) defect bigknot of textile materials [21]. (e) shrinkage and porosity defect of Casting [22]. (f) defects in green, yellow, orange bounding box are scratch, cratering, hump, respectively in carbody [23]. (g) Lack defect of gear [24]. (h) light leakage defect on mobile screen [25]. (i) Convexity defect in aluminum foil [26]. (j) Scratch defect of the wheel hub [27]. (k) Branch defect of wood veneer [28]. (l) Bubble defect of tire sidewall [29].


<!-- Page 3 -->


Materials 2020, 13, 5755 3 of 23


## 2. Survey of Defect-Detection Technologies


Product defect-detection technology is mainly to detect the surface and internal defects of products. The defect-detection technology refers to the detection technology of spot, pit, scratch, color differences and defect on the product surface. Internal defect-detection technology mainly includes internal ﬂaw detection, hole detection and crack detection [30]. At present, several methods are used to detect product quality, including deep learning [31], magnetic powder [32], eddy current testing [33], ultrasonic testing [34], and machine vision [35] detection methods.


Wet magnetic particle detection mixes the magnetic powder in water, oil, or other liquid media. Magnetic powder marks the location of defects through liquid pressure and the attraction of the external magnetic ﬁeld [32,36,37]. The moisture detection method has high sensitivity, and the liquid medium is recyclable [38,39]. Dry Magnetic powder testing [40] directly attaches magnetic powder onto the surface of the magnetized workpiece for defect detection. This method is used for the local inspection of defects in large casting, welding parts, and other segments that are unsuitable for wet detection. The continuous magnetic particle detection method detects defects in magnetic suspension or powder under the external magnetic ﬁeld [41]. The method can be used to observe the defects in the external magnetic ﬁeld. Several factors that inﬂuence the precision of Magnetic powder testing include roughness and the proﬁle of the test piece, the geometrical characteristics of defects, the selected magnetization method, and the quality of operators [42]. Meanwhile, the factors that inﬂuence the sensitivity of Osmosis testing are imaging reagent, the performance of osmotic ﬂuid, quality of operators, and the inﬂuence of defects. Factors that inﬂuence the accuracy of the detection of eddy current are the type and parameters of coil and material and the proﬁle of the test piece [43,44].


The ultrasonic testing effect is affected by the angle between the defect surface and the ultrasonic propagation direction [34,45]. If the angle is vertical, then the signal returned is strong, and the defect is easily detected. If the angle is horizontal, then the signal returned is weak, which makes detecting a leak easy. Therefore, selecting the appropriate detection sensitivity and corresponding probe to reduce leakage detection is necessary [46]. The factors that inﬂuence ultrasonic testing include projection direction, probe effectiveness, sound contact quality, and instrument operating frequency [47,48].


Machine vision detection mainly consists of image acquisition and defect detection and classiﬁcation. Because of its fast, accurate, non-destructive and low-cost characteristics, machine vision is widely used. Machine vision identiﬁes objects mainly based on the color, texture and geometric features of objects. The quality of image acquisition determines the difﬁculty of image processing. In turn, the quality of the image processing algorithm directly affects the accuracy and error detection rate of defect detection and classiﬁcation [49–51]. The deep-learning method is also a defect-detection method that is based on image processing, which is widely used to obtain useful features in massive data [52]. Table 1 presents a comparison of commonly used product defect-detection methods.


Clearly, the traditional defect-detection techniques and the popular deep-learning defect-detection techniques have their advantages. The traditional detection methods are highly focused. For instance, Osmosis testing technology [53] is only suitable for detecting defects in highly permeable and non-porous materials and have certain advantages over other general methods. However, most of the traditional detection methods still need to rely on manual assistance to complete, especially when a certain amount of instrument debugging is required before testing, and the equipment development cost is high, which is not highly adaptable and limited by the equipment life and manufacturing accuracy. Innovative defect-detection techniques, particularly machine vision and deep-learning methods [54–56], have become the most popular in recent years and are one of the key technologies for automating defect detection due to their versatility and lack of reliance on human assistance. Compared to traditional defect detection methods, the new technologies offer better inspection results and lower costs, but still rely on large amounts of learned data to drive model updates and improve inspection accuracy.


<!-- Page 4 -->


Materials 2020, 13, 5755 4 of 23


Table 1. Comparison of common defect-detection methods.


Methods Strengths Weaknesses Applicable


Easy to use, strong penetration, high sensitivity, portable equipment, and automatic detection.


Ultrasonic testing [45]


• Unsuitable for complex workpieces. Any material


A wide range of applications, high precision, remains unaffected by the proﬁle of the detection piece, and automatic detection.


Machine vision detection [51]


• Detects surface defects only. Any material


• Application is limited to ferromagnetic materials. • Detection results are affected by the geometric shape of the test pieces. • Realizing automatic detection is difﬁcult.


The position, shape, and size of the defect can be visualized, which is suitable for any size of workpiece detection. It has the characteristics of high precision and low cost.


Magnetic powder testing [57]


Ferromagnetic materials (e.g., cast steel, pipe, calendar, bar, etc.)


• Detecting porous materials is difﬁcult, and the detection speed is slow. • Detection results are greatly affected by the inspectors, and automatic detection is difﬁcult to carry out.


Free from the inﬂuence of material type and shape proﬁle and high sensitivity to pinhole defects.


Osmosis testing [58]


Nonporous materials are tested (e.g., metal casting, ceramic, plastic, glass, etc.)


• The shape and size of the defects cannot be visualized. • The applicable materials are limited. • Difﬁculty in detecting deep defects with low detection accuracy.


Noncontact detection, fast detection speed, high sensitivity, and suitable for high-temperature environments, automatic detection.


Eddy current testing [59]


Non-destructive detection, strong penetration, free from the inﬂuence of material appearance and structure, and easy operation.


X-ray testing [60]


Conductive or non-metallic material (e.g., workpieces, pipes, wires, and graphite)


• Radiation effects for the staff involved in the detection. Any material


## 3. Survey of Deep-Learning Defect-Detection Technologies


Deep-learning technology has developed rapidly and made great success in object detection [61], intelligent robot [62], saliency detection [63], parking garage sound event detection [64], sound event detection for smart city safety [65,66], UAV blade fault diagnosis [67–69] and other ﬁelds [70–72]. Deep learning has a kind of deep neural network structure with multiple convolutions layer. By combining low-level features to form a more abstract high-level representation of attribute categories or features, the data can be better reached in abstract ways such as edge and shape to improve the effectiveness of the deep-learning algorithm [70], Therefore, many researchers try to use deep-learning technology to defect detection of product and improved the product quality [71–74]. Table 2 summarizes the advantages and disadvantages of deep-learning methods commonly used in product defect detection. It mainly includes convolutional neural network (CNN) [75], autoencoder neural network [74,76], deep residual neural network [77], full convolution neural network [78], and recurrent neural network [79,80].


(1) Using the CNN to defect detection of product [75]. CNN is a feedforward neural network. CNN consist of one or more convolutional layers and fully connected layers, as well as associated weights and pooling layers [81]. Literature [82] is a very popular LeNet convolution neural network structure. LeNet network structure can be used to detect defects in two situations: one is to design a complex multi-layer CNN structure, use different network structure to extra image content features, and complete end-to-end training to detect defects in images [56,83]; the other is to combine CNN with CRF model, train CNN with CRF energy function as constraint or optimize network prediction results with CRF. And to achieve the detection of product defects [71].


<!-- Page 5 -->


Materials 2020, 13, 5755 5 of 23


Table 2. Deep-Learning Defect-Detection Methods.


Methods Strengths Weaknesses Applicable


It has a strong learning ability for high-dimensional input data and can learn abstract, essential and high-order features from a small amount of preprocessed and even the most original data.


CNN


It has a good object information representation ability, can extract the foreground region in the complex background, and has good robustness to the environment noise.


Autoencoder neural network


Depth residual neural network


The residual network has lower convergence loss and does not overﬁt, so it has better classiﬁcation performance.


It can extract the feature of any size image, and obtain the high-level semantic prior knowledge matrix, which has a good effect on semantic level object detection.


Full convolution neural network


When there are fewer sample data, we can learn the essential features of the data and reduce the loss of data information in the process of pooling.


Recurrent neural network


The good expression ability and the calculation complex will increase with the increase of network depth.


Unlimited material


The input and output data dimensions of the autoencoder machine must be consistent.


Unlimited material


The network must cooperate with deeper depth to give full play to its structural advantages.


Unlimited material


The feature matrix transformation combined with the underlying features is needed, and the convergence speed of the model is slow.


Unlimited material


With the increase of the number of iterations in the network training process, the recurrent neural network model may appear overﬁtting phenomenon.


Unlimited material


(2) The product defect-detection technology based on the neural network [74,76]. Autoencoder network mainly includes two stages: coding and decoding. In the coding stage, the input signal is converted into a coding signal for feature extraction; in the decoding stage, the feature information is converted into a reconstruction signal, and then the reconstruction error is minimized by adjusting the weight and bias to realize the defect detection [84]. The difference between autoencoder networks and other machine learning algorithms is that the learning goal of the autoencoder network is not for classiﬁcation, but for feature learning [85,86]. It also has a strong ability of autonomous learning and highly nonlinear mapping. It can learn nonlinear metric functions to solve the problem of segmentation of complex background and foreground regions [87].


(3) The product defect-detection technology of deep residual neural network [77]. The deep residual network adds a residual module on the basis of the convolutional neural network. The residual network is characterized by easy optimization and can improve the accuracy by increasing the network depth [88,89]. CNN, Generative Adversarial Networks [90], etc. with the depth of the network increases, the extraction feature increases, but it is easy to cause the activation function not to converge. The purpose of the deep residual network is to optimize the increasing number of network layers with residual while increasing the network structure, so that the output and input element dimensions of the convolution layer in the residual unit are the same, and then through the activation function to reduce the loss.


(4) Full convolution neural network [78]. The fully connected layer is a connection between any two nodes between two adjacent layers. A fully connected neural network uses a fully connected operation, so there will be more weight values, which also means that the network will take up more memory and calculations [91]. During the calculation of the fully connected neural network, the feature map generated by the convolution layer is mapped into a ﬁxed-length feature vector. The full convolution neural network can accept the input image of any size, and use the deconvolution layer to sample the feature map of the last convolution layer, it can recover to the same size of the input image.so that a prediction can be generated for each pixel, while retaining the spatial information in the original input image, and ﬁnally classify the feature map of the upper sampling pixel by pixel.


(5) Recurrent neural network recursively from the evolution direction of sequence data and all cyclic units are connected in a chain manner, and the input is sequence data [79,80]. The CNN model mainly extracts the feature information of input layer test samples through convolution and pooling operations. The recurrent neural network uses the recurrent convolution operation to replace the convolution operation on CNN. The difference is that the recurrent neural network does not perform


<!-- Page 6 -->


Materials 2020, 13, 5755 6 of 23


the pooling layer operation to extract the features after the recurrent operation to extract the input layer features, but uses the recurrent convolution operation to process the features of the samples.


## 4. Survey of Object Detection Technologies Based on Deep Learning


Object detection methods based on neural networks can be divided into a one-stage method based on regression [92–96] and a two-stage method based on candidate box generation and classiﬁcation [97–103]. The one-stage method does not need to generate candidate boxes in advance, but it only needs to complete the three tasks of feature extraction, classiﬁcation, and location regression. By contrast, the two-stage method mainly has four tasks, namely feature extraction, generating candidate boxes, classiﬁcation, and location regression. Table 3 shows a comparative analysis of the two types of object detection methods.


Table 3. Comparative analysis of two kinds of object detection methods.


Methods Onestage Object Detection Twostage Object Detection


Candidate regions are extracted from the input image through selective search and region generation network. Thereafter, convolution, pooling, and other processing is conducted to obtain feature maps.


The input original image is processed directly to obtain the position coordinate value and category probability. The position is corrected thereafter.


Principle


The deep semantic features of the object can be obtained. The detection accuracy of the object is high, whether it is a small object or a scene with considerable density.


In the case of the low input separation rate, the speed and accuracy can be balanced simultaneously, and the detection speed is fast, which can reach above 45 FPS.


Advantage


The algorithm has a large volume, large amount of stored data, complicated calculation process, and slow detection speed.


Insufﬁcient Low accuracy for small objects and prone to miss detection, low positioning accuracy.


Realtime Realtime. Cannot reach real time


Representative one-stage methods include: Joseph Redmon et al. [92,93]. proposed the You Only Look Once(YOLO) method, which inherits OverFeat, and its detection speed reaches 45 pieces per second. The speed advantage makes it an end-to-end leader. Redmon et al. [94]. modiﬁed the network structure of YOLO and proposed the YOLOv2 and YOLO9000 methods, with a 4.00% increase in mAP. YOLOv3 [95] follows the Darknet53 network of YOLOv2 and combines it with the FPN [96] network structure. Thereafter, the prediction results are obtained from the convolutional network. Corresponding improvements enable the accuracy to reach 22.2 milliseconds per piece, and the best effect of mAP@0.5 on the COCO test set reaches 33.00%. However, the overall model becomes considerably complicated, and speed and accuracy serve as checks and balances for each other. To solve the problem of poor positioning accuracy of the YOLO algorithm, Wei Liu et al. [97]. proposed the Single Shot MultiBox Detector(SSD) method that combines YOLO regression ideas with the Faster R-CNN [98] anchor box mechanism, using the Visual Geometry Group Network(VGG) as the feature extraction network. The VGG is a convolutional neural network model proposed by K. Simonyan [99]. To address the issue that the SSD algorithm cannot easily detect small objects, Cheng-Yang Fu et al. [100]. proposed a DSSD method, which replaces the VGG16 of SSD with the ResNet101 network, thereby enhancing the network’s ability to extract features.


The representative two-stage methods are as follows. Girshick et al. [101]. proposed the Rich Feature Convolutional Neural Network (R-CNN) to enrich the features in the training process. That is, the mAP of the PASCAL VOC2007 test set was refreshed to 58.50%. He et al. [102]. proposed the Spatial Pyramid Pooling Network(SPP-Net) algorithm based on R-CNN to solve the problems of repetitive operations and shape distortion of convolutional neural networks. SPP-Net abandons the R-CNN clipping candidate box and image sub-block scaling operations before inputting the neural network, and adds an SPP structure between the convolutional and fully connected layers to increase the generation rate of candidate box and save computational overhead. Given the time cost caused by repeated computation of multiple stages and features during training and the space cost caused by storage of intermediate feature data, Girshick et al. [103]. proposed Fast R-CNN,


<!-- Page 7 -->


Materials 2020, 13, 5755 7 of 23


which combines deep network with SVM classiﬁcation. Accordingly, classiﬁcation and regression are performed simultaneously by the full connectional layer network, thereby forming a multi-task model. This module has numerous calculations, given the problem that SPP-Net and Fast R-CNN have separate candidate area modules. Ren et al. [27] proposed the Faster R-CNN algorithm based on Fast R-CNN. Faster R-CNN adds an RPN network to the backbone network structure and sets multi-scale anchor points on the basis of established rules. To solve the problem that the Faster R-CNN rounds the feature map size when performing ROI pooling and downsampling, Mask R-CNN [104] abandons the rounding operation of the picture size and proposes to replace the ROI Pooling layer with ROI Align and use double Linear interpolation ﬁlls pixels at non-integer positions. Accordingly, no position error occurs when the downstream feature map is mapped upstream.


## 5. Summary Analyses of the Application Status of Defect-Detection Technology


## 5.1. The Traditional Method for Defect-Detection Technology


Non-destructive defect detection of products is widely used in manufacturing, in which analyzing the pros and cons of different algorithms can help to understand and improve the algorithms. Here we focus on the application status using the combination of classical defect detection and other algorithms. Figure 2. shows the different defect-detection methods and their corresponding performance results or summaries for non-destructive defect detection.


Figure 2. Summary and analysis of defect-detection methods.


The ultrasonic defect-detection methods are widely used to detect the defects in the internal structure of the sample. Therefore, the results are mainly reﬂected in the performance of the ultrasonic signal [105]. The ﬁndings, as shown in [106], indicates that the ultrasonic defect-detection methods have the advantages of fast detection speed and simple operability. They also have special advantages in detecting defects in the internal material and structure as well as the size of the product. However, this method is unsuitable for workpieces with complicated structures with low detection efﬁciency [106]. Ultrasonic techniques are especially ineffective for detecting defects on the upper surface of the sample since a nonlinear relationship exists between the defect position and the signal receiving the time, which leads to the defect to be closely positioned to the direct pass wave end [107]. The denser the distribution of the real position of the product, the higher the certainty of the “trailing” phenomenon of the direct pass wave signal on the map.


<!-- Page 8 -->


Materials 2020, 13, 5755 8 of 23


The machine vision-based defect-detection methods are suitable for the detection of surface defects in products, which has achieved up to 88.60% accuracy in binary defect-detection problems [108]. The defect-detection accuracy over scratches, holes, scales, pitting, edge cracks, crusting, and inclusions can reach 95.30% [109]. Our survey shows that the machine vision-based image recognition is widely used in manufacturing surface defect detection due to the feature extraction ability from the images made possible by recent deep-learning techniques.


The defect-detection methods are based on ﬁltering has a strong ability to describe the disturbance signal and detection of the tool defect inside the machine.


To the abovementioned main categories of defect-detection methods for mechanical products, several other technologies are also available such as the X-ray image defect-detection technology [110], Pulse magnetoresistance method [111], Acoustic emission technology [106]. These methods [106,110,111] have shown positive detection results and can provide theoretical and practical guidance for real-world applications. In addition, studies show that the majority of the early works studied a single defect-detection problem such as the defects in the material [112,113], shape [114,115], size [116], color [117], and surface of a product [118,119]. At the same time, studies on defects with varying size, crack depth, and other information are scarce, which is also a major limitation of existing defect-detection research [120–122]. The following is an experimental summary of some research methods [108–110,123–132]. The reference [123–126] are the experimental results of ultrasonic detection. The reference [109,127–131] are the experimental results of Filter detection. The reference [108,110,132] are the experimental results of other quality detection technologies.


• The frequency accuracy of the weld defect is over 60.00% when the frequency band is 100–200 kHz.Positive detection results can be obtained at frequencies of 100 to 200 kHz and 300 to 400 kHz [106]. • The total detection rate of the two types of samples in “defects” and “no defects” is 88.60% [108]. • Analysis of the effects of different surface defects and locations on the test results.The average recognition rate under eight types of defects is 95.30% [109]. • Poor detection effect with defect depth less than 2mm [110]. • The peak times of surface and subsurface defect depth of 3 mm are 16.59 and 37.01 ms, respectively [111]. • Realizes the detection and recognition of defects in different texture samples [123]. • Reduces unnecessary interference and extract weak signals from strong background noise [124]. • Effective detection of holes, axial cracks, and circumferential cracks [125]. • Detect cracks less than 3 mm [126]. • Can detect defects exceeding 1 mm2 [127]. • Resolves the quality defect detection with image noise and complex background [128]. • Improved Doppler distortion and multi-bearing source aliasing in bearing signals [129]. • Positive recognition effect on the position, shape, and size of the defect [130]. • It can deﬁne six features based on the characteristics of seam cracks and employed SVM for classiﬁcation. The true positive rate was 94.46%, and the false-negative rate was only 0.29% [131]. • The 8-bit grayscale image recognition rate of an image size of 2500 × 2000 pixels is 94.00% [132].


## 5.2. Machine Learning for Defect-Detection Technology


Another major trend in the literature survey of defect-detection technology is the emerging dominance of the machine learning methods, which are now widely used in all ﬁelds of product defect detection. The defect-detection technology can be divided into two main categories: surface defect detection [133] and internal fault diagnosis [134]. Surface defect detection is similar to ’visual’ detection, that is, learning from the target features in an image with the help of deep-learning image processing technology to classify and locate product defects in the image, whereas internal fault diagnosis is similar to ’Auditory’ detection, that is, the diagnosis of faults in rotating parts such as


<!-- Page 9 -->


Materials 2020, 13, 5755 9 of 23


bearings by means of modal analysis using digital signals in the time or frequency domain. We found that the defect-detection complex functions and enhanced feature extraction [135]. Table 4 Survey of Deep-learning methods in defect methods based on deep learning have achieved the best experimental result thus far. The highest precision of these algorithms can reach 99.00% with a recognition time of 0.12 ms for a single image [136]. The lowest precision level is 86.20% [137].


Table 4. Machine Learning for Defect-Detection Technology.


No. Methods Performance


1 Deep ensemble learning [23] Recall of 93.00% and detection precision of 88.00%.


2 Deep CNN [42] The proposed fast architecture mAP is 96.72%, whereas FPS is 83.00 Training time consumption is 133 min.


3 CNN [136] The overall recognition rate of the six kinds of defect dataset reaches 99.00%. The recognition time of a single image is 1.2 ms.


The CNNs were trained using 12,000 images that were collected from over 200 pipelines. The average testing accuracy, precision, and recall rates were 86.20%, 87.70%, and 90.60%, respectively.


## 4 Deep CNN [137]


## 5 CNN and Naïve Bayes data fusion [138]


The Naïve Bayes decision making discards false positives effectively. The proposed framework achieves a 98.3% hit rate against 0.1 false positives per frame.


The ICA, Gabor ﬁlter, and RF require approximately 0.097, 0.265 and 0.014 s, respectively, to detect defect for a 640 × 480-pixel image with sliding window search. However, CNN takes 0.217s and is slower than ICA and RF.


## 6 Machine learning [139]


Benchmarked on a publicly available dataset of SEM images, outperformed the state of the art by approximately 5% by reaching an area under the curve of approximately 97.00%.


## 7 CNN and self-similarity [140]


8 3D active stereo [141] omnidirectional vision sensor


The highest accuracy to detect defects is 97.00%. The recognition time of a single image is 0.19 s.


This paper obtained a mean IOU of 68.68% over 55.94%. The performance of all three metrics on the validation data reﬂect the superiority of adversarial training.


## 9 Deep neural networks [142]


10 Deep CNN [143] Maximum accuracy of the 32 × 32 pixel-sized image is 94.68% in industrial detection.


## 11 Support vector machine and CNNs [144]


In-wheel defect detection, accuracy is larger than 87.00%. The precision value is larger than 87.00%. The recall rate is larger than 89.00%.


## 12 Deep convolutional autoencoder [145]


Recall 95.70% Precision 91.80% the inspection time for an image of 512 × 512 pixels is only 20 ms.


13 CNN [146] Average accuracy of 93.02 % only 8.07 ms for predicting one image on an ordinary computer. 14 CNN [147] The mean accuracy of 99.38% with the std value of 0.018.


15 Fully Convolutional Neural Network [148] Accuracy 99.14% a batch of 50 images required only 0.368 s.


## 16 Machine learning [149] Accuracy as high as 99.4%.


## 17 Few-shot Learning [150] Accuracy rate can reach 97.25%.


<!-- Page 10 -->


Materials 2020, 13, 5755 10 of 23


## 6. Survey of Defect-Detection Equipment


At present, defect-detection equipment is mainly used in the production and processing stage of products. In the 1960s, due to the demand for the medical examination market, machine vision-based defect-detection robots are developed to detect insoluble foreign bodies in medical injection. Many visual inspection equipment providers were born such as BOSCH(Germany) [151], COMPUR [152], BS [153], CMP (Italy) [154], and Valley Industries (Japan) [155]. Recently, demand for intelligent manufacturing has been increasing as shown in China’s intelligent manufacturing 2025, German industry 4.0 and Britain’s “Modern Industrial Strategy”. Driven by these practical applications, demand for defect-detection equipment has been increasing steadily.


Figure 3. Types of defect-detection equipment: (a) Rhein–Nadel automation (RNA) glass defect-detection system [156] (b) Visual detection system for defects of EvenFit components [157] (c) Rhein–Nadel automated detection system for defects in mechanical parts [158] (d) The visual detection system of the EvenFit capsule [159] (e) KEYENCE product size measuring instrument [160] (f) AVI soldering appearance inspection machine [161] (g) Hardware and workpiece visual measurement equipment [162] (h) ET-F1 engine cylinder bore eddy current detector [163].


Figure 3 presents the defect-detection equipment widely used in the industry. In Table 5, we summarize the advantages and disadvantages of these defect-detection equipment aiming to identify the recurrent and difﬁcult challenges in defect detection. Figure 3a features a defect-detection system for LYNX mechanical parts, which detects missing mechanical parts and external surface damages and assembly of parts. Figure 3b shows the use of machine vision to visually detect component defects. However, it is found that current detection accuracy and detection performance remain incapable of fully meeting the requirements of high-speed production in smart factories. Furthermore, stability and real-time performance should be further improved.


<!-- Page 11 -->


Materials 2020, 13, 5755 11 of 23


Table 5. Existing defect-detection equipment.


Name Performance Packaging defect-detection equipment


color detection, window or insert detection, carton ejection, tilt, double-feed monitoring and glue line detection of mechanical product packaging.


Function


Trait remote control, off-site monitoring, and tracking. ineffective for metal or special transparent packing. LYNX Industrial vision system


Function detect and analyze missing and damaged parts and assembly errors.


System hardware can be controlled by the central terminal, which can adapt to various working environments and cover the detection amount of size and size. It is easy to operate, fully closed, a multi-detection system with data. IRNDT infrared thermal imaging testing


Trait


The defect image is displayed, and the feature is evaluated by heating the tested parts and analyzing the defect position with abnormal internal temperature.


Function


The equipment has the characteristics of the non-contact, large area, fast speed and visual display it has a poor effect on metal parts with a large amount of heat deformation.


Trait


This is used to perform ultrasonic phased array probe, sound beam control, and dynamic focusing technology to realize scanning and imaging detection of composite and metallic materials.


Smart U32 Ultrasonic scanning detector


Function


Coupling stability, automatic measurement, and accurate veriﬁcation. However, it is not good for the detection of large-size parts and non-metal parts.


Trait


This is used to detect parts with diameters ranging from 65 mm to 110 mm, such as sprockets, stators, and rotors. It can also detect breakage, bumps, and cracks.


Parts appearance optical detection equipment


Function


TPros: non-destructive testing, multi-angle identiﬁcation, fast detection speed, high precision, stable performance, and accurate data statistics function. Turbine detection system


Trait


The defect of the shallow surface of metal parts is detected through the analysis and treatment of the eddy current. It is suitable for defect detection of conductive materials.


Function


Eddy current testing is only applicable to conductive materials. It can only detect defects on the surface or near the surface layer. It is not conducive for use in components with complicated shapes.


Trait


It collects and analyzes the images of the seal ring directly above, sides, and bottom and extracts the surface scratches and bubble defects of the seal ring.


Sealing detection equipment


Function


The equipment can set the number of test stations, adjust the test sequence and methods at will, and support the detection of all product models. The detection speed is slow, which reduces the production tempo along the pipeline. 3D Visual measuring equipment


Trait


It has the functions of edge extraction, contour degree and other 2D and 3D form tolerance calculation, 3D digital model comparison, and heat map display.


Function


The device can only detect non-transparent products, and the measuring effect is insufﬁcient when the running speed is over 400 mm/s.


Trait


<!-- Page 12 -->


Materials 2020, 13, 5755 12 of 23


Table 5. Cont.


Name Performance


Inkjet detector Function It can detect defects in mechanical parts without and incomplete


codes, indented characters, and offset position of the code.


The device consists of a code detection unit, man-machine interface, and stripper. However, it is ineffective in detecting parts with greasy surfaces.


Trait


## 7. Challenge


7.1. 3D Object Detection


In modern computer vision systems, people are satisﬁed with 2D object detection. With the advent of 2.5D depth sensor, building 3D models has become increasingly important, and 3D geometric shapes have been considered an important clue in object recognition. One of the most important challenges of 3D is that given a depth map of an object from an angle, the 3D structure of an object can be inferred. We are convinced that one of the important trends in visual recognition is to identify defects on the surface of an object and infer its corresponding 3D model to determine the shape defects in the 3D layer. This situation is akin to that when we observe one side of a table, i.e., we naturally visualize a 3D model of the entire table. To determine the table based on the surface defects and in the 3D shape of the defects, various methods can be used to reconstruct and synthesize shapes, although such techniques are based on assembly. They are the same class or type of 3D shape completion. The completion of 3D models of different types of objects in complex environments should be studied further. At present, similar studies have been conducted. For example, the linear relationship between the 3D defect size of transparent parts and image gray level is found under certain circumstances [164]. On this basis, a set of vision-based transparent micro-defect measurement systems is developed. Iglesias [165] developed an automated inspection system to examine SLATE based on the use of 3D color cameras to capture data and using computer vision algorithms developed speciﬁcally for the purpose of studying SLATE characteristics. In a previous study [166], a potato virtual reality model reconstruction algorithm based on 3D shape and color images is proposed for sample quality tracking and review. The model redisplays potato color and 3D shape data in multiple views and supports 360-degree rotation in horizontal and vertical directions to simulate a handheld exam experience. This depth image processing is a potentially effective method for future non-destructive post-harvest grading, particularly for products in which size, shape, and surface conditions are important factors. In a previous study [167], a detection method combining grayscale image and 3D depth information is proposed.


## 7.2. High Precision, High Positioning, Fast Detection, Small Object


Through investigation, it is found that high precision [96,98], high positioning [94,96,98], fast detection [94], small object, complex background [94,96,98,168], occluded object detection [94,168], and object detection based on the association between objects [96,98] are the main challenges of the current deep-learning algorithm in the application of quality detection. In order to further assist researchers and enterprise engineers to apply the deep-learning method to product defect detection, Table 6 are from high precision [96,98], high positioning [94,96,98], fast detection [94], small object [96,100], complex background [94,96,98,168], occluded object detection [168,169], object association [170], and other aspects are summarized in the relevant papers published in ICCV and CVPR and other well-known international conferences in recent years, and the core idea and source code of these better papers are summarized to assist R & D personnel in knowledge reuse and innovative design.


<!-- Page 13 -->


Materials 2020, 13, 5755 13 of 23


Table 6. Summary of object detection methods with high precision, high positioning, fast detection, small object, complex background, occluded object detection.


Position Ability Fast Small Object


Train Strategy


Ref. High Precision


Irregular Object Imbalance Data


Complex Background


Occluded Objects


Objects Relationship Published


## [94] ✓ ✓ ✓ ✓ ✓ CVPR2017


## [96] ✓ ✓ ✓ ✓ CVPR2017


## [98] ✓ ✓ ✓ ✓ ✓ CVPR2017


[100] ✓ ✓ ✓ ✓ ✓ arXiv


## [104] ✓ ✓ ✓ ✓ ICCV2017


## [168] ✓ ✓ ICCV2017


## [169] ✓ ✓ ICCV2017


## [170] ✓ ✓ CVPR2018


## [171] ✓ ✓ ✓ CVPR2017


## [172] ✓ ✓ ICCV2017


## [173] ✓ ✓ ICCV2017


## [174] ✓ ✓ ICCV2017


<!-- Page 14 -->


Materials 2020, 13, 5755 14 of 23


## 8. Development Trend


Our survey found that most of the existing defect-detection studies focused on defect detection of speciﬁc products. But the identiﬁcation accuracy of current online defect-detection techniques remains to be improved. The following aspects of defect detection need special attention:


• Combined with the actual requirements of the factory, online defect detection of manufacturing products on the conveyor belt should be realized. • As intelligent manufacturing enterprises attach importance to defect-detection technology, embedded sensor equipment to conduct online real-time detection of defects in manufactured products can be designed and used. Then, various non-destructive defect-detection methods should be integrated to realize multi-modal defect detection of manufacturing products, which can have broad application prospects in the ﬁeld of defect detection. • The main objects of 2D image surface defect-detection technology are surface scratches and abrasions. Obtaining in-depth information about the defects is limited. However, in the actual production process, the defect information of the product is not only displayed on the surface of the manufactured product but also requires the use of 3D defect-detection methods to detect the 3D surface characteristics of the test sample. • With the rapid development of artiﬁcial intelligence and big data technology, useful information that can be extracted is abundant. Applying the rich information accurately to the manufacture of product defect feedback technology, defect control, and fault diagnosis warrants further research. • Aiming at the multi-fault diagnosis of intelligent equipment with defect-detection technology in complex industrial processes, one of the important research directions to undertake should be effective fault prediction and diagnosis for intelligent equipment when multiple faults simultaneously occur. • High-precision identiﬁcation technology. In the process of image acquisition, the apparent characteristics of the object can considerably change with different lighting conditions and shooting angles and distance. Many noise interference and partial occlusion of the detected sample can also have a great impact on the detection results due to the different backgrounds of the detection object. The abovementioned factors are commonly used in industrial applications, which can lead to substantial difﬁculties in detecting defects in manufactured products. Therefore, such a problem should be further solved to improve the feature extraction capability of the current online non-destructive defect-detection technology and improve the accuracy of non-destructive defect detection. • How to optimize the quality of image acquisition, improve the accuracy of the candidate box, extract features more comprehensively and accurately for learning, and extract features of small-size targets are the future research directions; • Presently, a large number of neural networks (including neural networks improved for a certain problem) have their own advantages and disadvantages. These networks are implemented based on a large amount of data. How to use fewer picture samples to train the recognition model with excellent performance is a big difﬁculty; • With more and more product derivatives, it remains to be studied how to transfer a trained model to another similar product and ensure its accuracy and detection efﬁciency; • After the defect is detected and the type of defect is clear, it is very important to deal with the information of the object, and it is also very necessary to separate the defective product from the non-defective product. The defect-detection system can be combined with the early warning system to give timely warning after detecting the defective products, and the staff can timely eliminate the defective products. Or with the sorting system, the manipulator to eliminate the defective products, in addition, can also establish traceability system to check the production process will make the product defects steps, and timely optimization of the production process, so as to reduce the production cost;


<!-- Page 15 -->


Materials 2020, 13, 5755 15 of 23


• Future studies can also design defect information feedback technology that is based on defect-detection technology. Many feedback methods and objects remain undiscussed and are difﬁcult points for future research. Once product information is processed and analyzed, and after determining the cause of the product defect or fault information, the defect or fault information can be fed back to the mother-machine system to realize online production and self-correction of the product. Doing so can help improve product quality and reduce manpower, material resources, and production costs. Finally, we hope to compare the performance of the mainstream deep-learning detection model, which can provide a reference for researchers in deep-learning surface defect detection. See Table 7 for details.


Table 7. Performance comparison of deep-learning object detection model.


Model Network Structure Real-Time Performance Analysis mAP Published VOC2007 COCO


Faster R-CNN [27] ResNet101 Poor realtime performance 73.20% 37.40% NIPS’15 YOLO [92] VGG16 Good real-time performance 66.40% 23.70% CVPR’16 OverFeat [93] −− Poor real-time performance −− −− ICLR’14 YOLO V2 [94] Darknet19 Good real-time performance 78.60% 21.60% CVPR’17 YOLOv3 [95] Darknet53 Good real-time performance −− 57.90% Arxiv’18 FPN [96] ResNet Good real-time performance −− 36.20% CVPR’17 SSD [97] VGG16 Good real-time performance 76.80% 31.20% ECCV’16 DSSD [100] ResNet101 Good real-time performance 81.50% 33.20% Arxiv’17 R-CNN [101] AlexNet Poor realtime performance 58.50% −− CVPR’14 SPP-Net [102] ZF-Net Poor realtime performance 59.20% −− ECCV’14 Fast R-CNN [103] VGG16 Poor realtime performance 70.00% 19.70% ICCV’15 Mask R-CNN [104] ResNet101 Poor real-time performance −− 39.80% ICCV’17 R-FCN [171] ResNet101 Poor realtime performance 79.5% 29.90% NIPS’16 MegDet [175] ReseNet Good real-time performance −− 52.50% CVPR’18


## 9. Summary


Industrial product quality is an important part of product production, and the research on defect-detection technology has great practical signiﬁcance to ensure product quality. This article provides a comprehensive overview of the research status of product defect-detection technology in complex industrial processes. We have compared and analyzed traditional defect-detection methods and deep-learning defect-detection techniques, and comprehensively summarized the experimental results of defect-detection techniques. Meanwhile, combined with the actual application requirements and the development of artiﬁcial intelligence technology, the defect-detection equipment was investigated and analyzed. Through investigation, we found that 3D object detection, high precision, high positioning, rapid detection, small targets, complex backgrounds, detection of occluded objects, and object associations are the hotspots of academic and industrial research. We also pointed out that embedded sensor equipment, online product defect detection, 3D defect detection, etc. are the development trends in the ﬁeld of industrial product defect detection. We believe that the investigation will help industrial enterprises and researchers understand the research progress of product defect-detection technology in the ﬁeld of deep learning and traditional defect detection.


Author Contributions: Methodology, J.Y., Z.W., J.W., and H.D.; investigation, J.Y., S.L, J.W., and S.T.; resources, J.Y. and S.L.; writing–original draft preparation, J.Y., Z.W. and H.D.; writing–review and editing, J.Y., S.L., H.D., S.T. and J.W.; visualization, J.Y. and Z.W.; supervision, J.Y. and S.L.; project administration, S.L. and J.Y.; funding acquisition, S.L. All authors have read and agreed to the published version of the manuscript.


Funding: This work was supported by the National Natural Science Foundation of China under Grant Nos.91746116, 61863005.The Science and Technology Foundation of Guizhou Province under grant [2020]009, [2016]5013, [2019]3003, [2020]005, and The Guizhou Province Internet + Collaborative Intelligent Manufacturing Key Laboratory Open Fund[2016]5103.


Conﬂicts of Interest: The authors declare no conﬂict of interest.


<!-- Page 16 -->


Materials 2020, 13, 5755 16 of 23


## References


1. Peng, Y.; Liu, G.; Quan, Y.; Zeng, Q. The depth measurement of internal defect based on laser speckle shearing interference. Opt. Laser Technol. 2017, 92, 69–73. [CrossRef] 2. Xiao, X.; Yu, L.; Dong, Z.; Mbelek, R.; Xu, K.; Lei, C.; Zhong, W.; Lu, F.; Xing, M. Adipose stem cell-laden injectable thermosensitive hydrogel reconstructing depressed defects in rats: Filler and scaffold. J. Mater. Chem. B 2015, 27, 5635–5644. [CrossRef] [PubMed] 3. Hui, K.; Jian, Y.; Chen, Z. Accurate and Efﬁcient Inspection of Speckle and Scratch Defects on Surfaces of Planar Products. IEEE Trans. Ind. Inform. 2017, 4, 1855–1865. [CrossRef] 4. Chen, J.; Li, C. Prediction and Control of Thermal Scratch Defect on Surface of Strip in Tandem Cold Rolling. J. Iron Steel Res. Int. 2015, 22, 106–114. [CrossRef] 5. Rodionova, I.G.; Zaitsev, A.I.; Baklanova, O.N.; Kazankov, A.Y.; Naumenko, V.V.; Semernin, G.V. Effect of carbon steel structural inhomogeneity on corrosion resistance in chlorine-containing media. Metallurgist 2016, 59, 774–783. [CrossRef] 6. Amaya, J.; Lelah, A.; Zwolinski, P. Design for intensiﬁed use in product–service systems using life-cycle analysis. J. Eng. Des. 2014, 25, 280–302. [CrossRef] 7. Wang, T.; Chen, Y.; Qiao, M.; Snoussi, H. A fast and robust convolutional neural network-based defect detection model in product quality control. Int. J. Adv. Manuf. Technol. 2018, 94, 3465–3471. [CrossRef] 8. Kandpal, L.M.; Park, E.; Tewari, J.; Cho, B. Spectroscopic Techniques for Nondestructive Quality Inspection of Pharmaceutical Products. J. Biosyst. Eng. 2015, 40, 394–408. [CrossRef] 9. Li, B.; Cobo-Medina, M.; Lecourt, J.; Harrison, N.; Harrison, R.J.; Cross, J.V. Application of hyperspectral imaging for nondestructive measurement of plum quality attributes. Postharvest Biol. Technol. 2018, 141, 8–15. [CrossRef] 10. Amar, M.; Gondal, I.; Wilson, C. Vibration spectrum imaging: A novel bearing fault classiﬁcation approach. IEEE Trans. Ind. Electron. 2014, 62, 494–502. [CrossRef] 11. Li, P.; Dolado, I.; Alfaro-Mozaz, F.J.; Casanova, F.; Hueso, L.E.; Liu, S.; Edgar, J.H.; Nikitin, A.Y.; Vélez, S.; Hillenbrand, R. Infrared hyperbolic meta surface based on nanostructured van der Waals materials. Science 2018, 359, 892–896. [CrossRef] [PubMed] 12. Xie, X. A review of recent advances in surface defect detection using texture analysis techniques. ELCVIA Electron. Lett. Comput. Vis. Image Anal. 2008, 7, 1–22. [CrossRef] 13. Ngan, H.Y.; Pang, G.K.; Yung, N.H. Automated fabric defect detection—A review. Image Vis. Comput. 2011, 29, 442–458. [CrossRef] 14. Mahajan, P.M.; Kolhe, S.R.; Patil, P.M. A review of automatic fabric defect detection techniques. Adv. Comput. Res. 2009, 1, 18–29. 15. Aldave, I.J.; Bosom, P.V.; González, L.V.; De Santiago, I.L.; Vollheim, B.; Krausz, L.; Georges, M. Review of thermal imaging systems in composite defect detection. Infrared. Phys. Technol. 2013, 61, 167–175. [CrossRef] 16. Pernkopf, F. Detection of surface defects on raw steel blocks using Bayesian network classiﬁers. Pattern Anal. Appl. 2004, 7, 333–342. [CrossRef] 17. Zhang, W.; Ye, C.; Zheng, K.; Zhong, J.; Tang, Y.; Fan, Y.; Buehler, M.J.; Ling, S.; Kaplan, D.L. Tensan silk-inspired hierarchical ﬁbers for smart textile applications. ACS Nano 2018, 12, 6968–6977. [CrossRef] 18. Shankar, N.G.; Zhong, Z.W. Defect detection on semiconductor wafer surfaces. Microelectron. Eng. 2005, 77, 337–346. [CrossRef] 19. Mao, B.; Lu, Y.; Wu, P.; Mao, B.; Li, P. Signal processing and defect analysis of pipeline inspection applying magnetic ﬂux leakage methods. Intell. Serv. Robot. 2014, 7, 203–209. [CrossRef] 20. Liu, J.; Xu, G.; Ren, L.; Qian, Z.; Ren, L. Defect intelligent identiﬁcation in resistance spot welding ultrasonic detection based on wavelet packet and neural network. Int. J. Adv. Manuf. Technol. 2017, 90, 2581–2588. [CrossRef] 21. Kumar, A.; Pang, G.K. Defect detection in textured materials using Gabor ﬁlters. IEEE Trans. Ind. Appl. 2002, 38, 425–440. [CrossRef] 22. Lin, J.; Yao, Y.; Ma, L.; Wang, Y. Detection of a casting defect tracked by deep convolution neural network. Int. J. Adv. Manuf. Technol. 2018, 97, 573–581. [CrossRef] 23. Chang, F.; Liu, M.; Dong, M.; Duan, Y.A. Mobile vision inspection system for tiny defect detection of smooth car-body surface based on deep ensemble learning. Meas. Sci. Technol. 2019, 30, 125905. [CrossRef]


<!-- Page 17 -->


Materials 2020, 13, 5755 17 of 23


24. Yu, L.; Wang, Z.; Duan, Z. Detecting Gear Surface Defects Using Background-Weakening Method and Convolutional Neural Network. J. Sens. 2019, 2019, 125905. [CrossRef] 25. Li, C.; Zhang, X.; Huang, Y.; Tang, C.; Fatikow, S. A novel algorithm for defect extraction and classiﬁcation of mobile phone screen based on machine vision. Comput. Ind. Eng. 2020, 146, 106530. [CrossRef] 26. Zhai, M.; Fu, S.; Gu, S.; Xie, Z.; Luo, X. Defect detection in aluminum foil by measurement-residual-based chi-square detector. Int. J. Adv. Manuf. Technol. 2011, 53, 661–667. [CrossRef] 27. Sun, X.; Gu, J.; Huang, R.; Zou, R.; Giron Palomares, B. Surface Defects Recognition of Wheel Hub Based on Improved Faster R-CNN. Electronics 2019, 8, 481. [CrossRef] 28. Urbonas, A.; Raudonis, V.; Maskeli¯unas, R.; Damaševiˇcius, R. Automated Identiﬁcation of Wood Veneer Surface Defects Using Faster Region-Based Convolutional Neural Network with Data Augmentation and Transfer Learning. Appl. Sci. 2019, 9, 4898. [CrossRef] 29. Wang, R.; Guo, Q.; Lu, S.; Zhang, C. Tire Defect Detection Using Fully Convolutional Network. IEEE Access 2019, 7, 43502–43510. [CrossRef] 30. Moulin, E.; Chehami, L.; Assaad, J.; De Rosny, J.; Prada, C.; Chatelet, E.; Lacerra, G.; Gryllias, K.; Massi, F. Passive defect detection in plate from nonlinear conversion of low-frequency vibrational noise. Microelectron. Eng. 2005, 77, 337–346. [CrossRef] 31. Li, Y.; Zhao, W.; Pan, J. Deformable patterned fabric defect detection with ﬁsher criterion-based deep learning. IEEE Trans. Autom. Sci. Eng. 2016, 14, 1256–1264. [CrossRef] 32. Elrefai, A.L.; Sasada, I. Magnetic particle detection system using ﬂuxgate gradiometer on a permalloy shielding disk. IEEE Magn. Lett. 2016, 7, 1–4. [CrossRef] 33. Angelo, G.D.; Laracca, M.; Rampone, S.; Betta, G. Fast eddy current testing defect classiﬁcation using lissajous ﬁgures. IEEE Trans. Instrum. Meas. 2018, 67, 821–830. [CrossRef] 34. Kusano, M.; Hatano, H.; Watanabe, M.; Takekawa, S.; Yamawaki, H.; Oguchi, K.; Enoki, M. Mid-infrared pulsed laser ultrasonic testing for carbon ﬁber reinforced plastics. Ultrasonics 2018, 84, 310–318. [CrossRef] 35. Yang, J.; Li, S.; Gao, Z.; Wang, Z.; Liu, W. Real-Time Recognition Method for 0.8 cm Darning Needles and KR22 Bearings Based on Convolution Neural Networks and Data Increase. Appl. Sci. 2018, 8, 1857. [CrossRef] 36. Chen, Y.; Kolhatkar, A.; Zenasni, O.; Xu, S.; Lee, T. Biosensing Using Magnetic Particle Detection Techniques. Sensors 2017, 17, 2300. [CrossRef] 37. Li, J.; Wang, G.; Xu, Z. Environmentally-friendly oxygen-free roastingwet magnetic separation technology for in situ recycling cobalt, Lithium Carbonate Graph. Spent LiCoO2/graphite Lithium Batteries. J. Hazard. Mater. 2016, 302, 97–104. [CrossRef] 38. Rymarczyk, T.; Szumowski, K.; Adamkiewicz, P.P.T.; Jan, S. Moisture Wall Inspection Using Electrical Tomography Measurements. Przegl ˛ad Elektrotechniczny 2018, 94, 97–100. [CrossRef] 39. Seo, J.; Duque, L.; Wacker, J. Drone-enabled bridge inspection methodology and application. Autom. Constr. 2018, 94, 112–126. [CrossRef] 40. Shelikhov, G.S.; Glazkov, Y.A. On the improvement of examination questions during the nondestructive testing of magnetic powder. Russ. J. Nondestruct. Test. 2011, 47, 112–117. [CrossRef] 41. García-Arribas, A.; Martínez, F.; Fernández, E. GMI detection of magnetic-particle concentration in continuous ﬂow. Sens. Actuators Phys. 2011, 172, 103–108. [CrossRef] 42. Chen, J.; Liu, Z.; Wang, H.; Núñez, A.; Han, Z. Automatic defect detection of fasteners on the catenary support device using deep convolutional neural network. IEEE Trans. Instrum. Meas. 2017, 67, 257–269. [CrossRef] 43. Tsuboi, H.; Seshima, N.; Sebestyén, I.; Pávó, J.; Gyimóthy, S.; Gasparics, A. Transient eddy current analysis of pulsed eddy current testing by ﬁnite element method. IEEE Trans. Magn. 2004, 40, 1330–1333. [CrossRef] 44. Tian, G.Y.; Sophian, A. Defect classiﬁcation using a new feature for pulsed eddy current sensors. NDT-E Int. 2005, 38, 77–82. [CrossRef] 45. Yang, H.; Yu, L. Feature extraction of wood-hole defects using wavelet-based ultrasonic testing. J. For. Res. 2017, 28, 395–402. [CrossRef] 46. Gholizadeh, S. A review of non-destructive testing methods of composite materials. Procedia Struct. Integr. 2016, 1, 50–57. [CrossRef] 47. Fang, Y.; Lin, L.; Feng, H.; Lu, Z.; Emms, G.W. Review of the use of air-coupled ultrasonic technologies for nondestructive testing of wood and wood products. Comput. Electron. Agric. 2017, 137, 79–87. [CrossRef]


<!-- Page 18 -->


Materials 2020, 13, 5755 18 of 23


48. Bernasconi, A.; Carboni, M.; Comolli, L.; Galeazzi, R.; Gianneo, A.; Kharshiduzzaman, M. Fatigue crack growth monitoring in composite bonded lap joints by a distributed ﬁbre optic sensing system and comparison with ultrasonic testing. J. Adhes. 2016, 92, 739–757. [CrossRef] 49. Aytekin, Ç.; Rezaeitabar, Y.; Dogru, S.; Ulusoy, I. Railway fastener inspection by real-time machine vision. IEEE Trans. Syst. Man Cybern. Syst. 2015, 45, 1101–1107. [CrossRef] 50. Lin, H.; Chen, H. Automated visual fault inspection of optical elements using machine vision technologies. J. Appl. Eng. Sci. 2018, 16, 447–453. [CrossRef] 51. Shanmugamani, R.; Sadique, M.; Ramamoorthy, B. Detection and classiﬁcation of surface defects of gun barrels using computer vision and machine learning. Measurement 2015, 60, 222–230. [CrossRef] 52. Jia, F.; Lei, Y.; Lin, J.; Zhou, X.; Lu, N. Deep neural networks: A promising tool for fault characteristic mining and intelligent diagnosis of rotating machinery with massive data. Mech. Syst. Signal Process. 2016, 72, 303–315. [CrossRef] 53. Habib, M.A.; Kim, C.H.; Kim, J. A Crack Characterization Method for Reinforced Concrete Beams Using an Acoustic Emission Technique. Appl. Sci. 2020, 10, 7918. [CrossRef] 54. Yang, Y.; Pan, L.; Ma, J.; Yang, R.; Zhu, Y.; Yang, Y.; Zhang, L. A High-Performance Deep Learning Algorithm for the Automated Optical Inspection of Laser Welding. Appl. Sci. 2020, 10, 933. [CrossRef] 55. Zhong, J.; Liu, Z.; Han, Z.; Han, Y.; Zhang, W. A CNN-Based Defect Inspection Method for Catenary Split Pins in High-Speed Railway. IEEE Trans. Instrum. Meas. 2019, 68, 2849–2860. [CrossRef] 56. He, Y.; Song, K.; Meng, Q.; Yan, Y. An end-to-end steel surface defect detection approach via fusing multiple hierarchical features. IEEE Trans. Instrum. Meas. 2020, 69, 1493–1504. [CrossRef] 57. Pashagin, A.I.; Shcherbinin, V.E.; Zhang, C. Indication of magnetic ﬁelds with the use of galvanic currents in magnetic-powder nondestructive testing. Russ. J. Nondestruct. 2012, 48, 528–531. [CrossRef] 58. Gholizadeh, S.; Leman, Z.; Baharudin, B. A review of the application of acoustic emission technique in engineering. Struct. Eng. Mech. 2015, 51, 1075–1095. [CrossRef] 59. Rocha, T.J.; Ramos, H.G.; Ribeiro, A.L.; Pasadas, D.J. Magnetic sensors assessment in velocity induced eddy current testing. Sens. Actuators A Phys. 2015, 28, 55–61. [CrossRef] 60. Du Plessis, A.; le Roux, S.G. Standardized X-ray tomography testing of additively manufactured parts: A round robin test. Addit. Manuf. 2018, 24, 125–136. [CrossRef] 61. Khan, F.; Salahuddin, S.; Javidnia, H. Deep Learning-Based Monocular Depth Estimation Methods—A State-of-the-Art Review. Sensors 2020, 20, 2272. [CrossRef] [PubMed] 62. Yang, G.; Yang, J.; Sheng, W.; Fernandes, F.E., Jr.; Li, S. Convolutional Neural Network-Based Embarrassing Situation Detection under Camera for Social Robot in Smart Homes. Sensors 2018, 18, 1530. [CrossRef] [PubMed] 63. Borji, A.; Cheng, M.; Jiang, H.; Li, J. Salient object detection: A benchmark. IEEE Trans. Image Process 2015, 24, 5706–5722. [CrossRef] [PubMed] 64. Ciaburro, G. Sound event detection in underground parking garage using convolutional neural network. Big Data Cogn. Comput. 2020, 4, 20. [CrossRef] 65. Ciaburro, G.; Iannace, G. Improving Smart Cities Safety Using Sound Events Detection Based on Deep Neural Network Algorithms. Informatics 2020, 7, 23. [CrossRef] 66. Costa, D.G.; Vasques, F.; Portugal, P.; Ana, A. A distributed multi-tier emergency alerting system exploiting sensors-based event detection to support smart city applications. Sensors 2020, 20, 170. [CrossRef] 67. Iannace, G.; Ciaburro, G.; Trematerra, A. Fault diagnosis for UAV blades using artiﬁcial neural network. Robotics 2019, 8, 59. [CrossRef] 68. Peng, L.; Liu, J. Detection and analysis of large-scale WT blade surface cracks based on UAV-taken images. IET Image Processing 2018, 12, 2059–2064. [CrossRef] 69. Saied, M.; Lussier, B.; Fantoni, I.; Shraim, H.; Francis, C. Fault Diagnosis and Fault-Tolerant Control of an Octorotor UAV using motors speeds measurements. IFAC-PapersOnLine 2017, 50, 5263–5268. [CrossRef] 70. Deng, L.; Yu, D. Deep learning: Methods and applications. Found. Trends Signal Process. 2014, 7, 197–387. [CrossRef] 71. Tao, X.; Wang, Z.; Zhang, Z.; Zhang, D.; Xu, D.; Gong, X.; Zhang, L. Wire Defect Recognition of Spring-Wire Socket Using Multitask Convolutional Neural Networks. IEEE Trans. Compon. Packag. Manuf. Technol. 2018, 8, 689–698. [CrossRef]


<!-- Page 19 -->


Materials 2020, 13, 5755 19 of 23


72. Jiang, J.; Chen, Z.; He, K. A feature-based method of rapidly detecting global exact symmetries in CAD models. Comput. Aided. Des. 2013, 45, 1081–1094. [CrossRef] 73. Cheng, J.C.P.; Wang, M. Automated detection of sewer pipe defects in closed-circuit television images using deep learning techniques. Autom. Constr. 2018, 95, 155–171. [CrossRef] 74. Bergmann, P.; Löwe, S.; Fauser, M.; Sattlegger, D.; Steger, C. Improving Unsupervised Defect Segmentation by Applying Structural Similarity to Autoencoders. arXiv 2018, arXiv:1807.02011. 75. Yang, J.; Yang, G. Modiﬁed Convolutional Neural Network Based on Dropout and the Stochastic Gradient Descent Optimizer. Algorithms 2018, 11, 28. [CrossRef] 76. Sun, K.; Zhang, J.; Zhang, C.; Hu, J. Generalized extreme learning machine autoencoder and a new deep neural network. Neurocomputing 2017, 230, 374–381. [CrossRef] 77. Yu, L.; Chen, H.; Dou, Q.; Qin, J.; Heng, P.A. Automated melanoma recognition in dermoscopy images via very deep residual networks. IEEE Trans. Med. Imaging 2016, 36, 994–1004. [CrossRef] 78. Xue, Y.; Li, Y. A Fast Detection Method via Region-Based Fully Convolutional Neural Networks for Shield Tunnel Lining Defects. Comput. Civ. Infrastruct. Eng. 2018, 33, 638–654. [CrossRef] 79. Lei, J.; Gao, X.; Feng, Z.; Qiu, H.; Song, M. Scale insensitive and focus driven mobile screen defect detection in industry. Neurocomputing 2018, 294, 72–81. [CrossRef] 80. Lukoševiˇcius, M.; Jaeger, H. Reservoir computing approaches to recurrent neural network training. Comput. Sci. Rev. 2009, 3, 127–149. [CrossRef] 81. Krizhevsky, A.; Sutskever, I.; Hinton, G.E. Imagenet classiﬁcation with deep convolutional neural networks. Commun. ACM 2017, 60, 84–90. [CrossRef] 82. LeCun, Y.; Bottou, L.; Bengio, Y.; Haffner, P. Gradient-based learning applied to document recognition. Proc. IEEE 1998, 86, 2278–2324. [CrossRef] 83. Li, J.; Su, Z.; Geng, J.; Yixin, Y. Real-time detection of steel strip surface defects based on improved yolo detection network. IFAC-PapersOnLine 2018, 51, 76–81. [CrossRef] 84. Ozkan, S.; Kaya, B.; Akar, G.B. Endnet Sparse autoencoder network for endmember extraction and hyperspectral unmixing. IEEE Trans. Geosci. Remote Sens. 2018, 57, 482–496. [CrossRef] 85. Mei, S.; Wang, Y.; Wen, G. Automatic fabric defect detection with a multi-scale convolutional denoising autoencoder network model. Sensors 2018, 18, 1064. [CrossRef] 86. To˘gaçar, M.; Ergen, B.; Cömert, Z. Waste classiﬁcation using AutoEncoder network with integrated feature selection method in convolutional neural network models. Measurement 2020, 153, 107459. [CrossRef] 87. Long, J.; Sun, Z.; Li, C.; Ying, H.; Yun, B.; Zhang, S. A novel sparse echo autoencoder network for data-driven fault diagnosis of delta 3-D printers. IEEE Trans. Instrum. Meas. 2019, 69, 683–692. [CrossRef] 88. Chen, K.; Chen, K.; Wang, Q.; Ziyu, H.; Jun, H.; Jinliang, H. Short-term load forecasting with deep residual networks. IEEE Trans. Smart Grid 2018, 10, 3943–3952. [CrossRef] 89. He, K.; Zhang, X.; Ren, S.; Sun, J. Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2016, Las Vegas, NV, USA, 27–30 June 2016; pp. 770–778. [CrossRef] 90. Creswell, A.; White, T.; Dumoulin, V.; Arulkumaran, K.; Sengupta, B.; Bharath, A.A. Generative adversarial networks: An overview. IEEE Signal Proc. Mag. 2018, 35, 53–65. [CrossRef] 91. Long, J.; Shelhamer, E.; Darrell, T. Fully convolutional networks for semantic segmentation. IEEE Trans. Pattern Anal. Mach. Intell. 2017, 39, 640–651. [CrossRef] 92. Redmon, J.; Divvala, S.; Girshick, R.; Farhadi, A. You only look once: Uniﬁed, real-time object detection. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2016, Las Vegas, NV, USA, 27–30 June 2016; pp. 779–788. [CrossRef] 93. Sermanet, P.; Eigen, D.; Zhang, X.; Mathieu, M.; Fergus, R.; LeCun, Y. Overfeat: Integrated recognition, localization and detection using convolutional networks. arXiv 2013, arXiv:1312.6229. 94. Redmon, J.; Farhadi, A. YOLO9000: Better, faster, stronger. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2017, Honolulu, HI, USA, 21–26 July 2017; pp. 7263–7271. [CrossRef] 95. Redmon, J.; Farhadi, A. Yolov3: An incremental improvement. arXiv 2018, arXiv:1804.02767. 96. Lin, T.; Dollár, P.; Girshick, R.; He, K.; Hariharan, B.; Belongie, S. Feature pyramid networks for object detection. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2017, Honolulu, HI, USA, 21–26 July 2017; pp. 2117–2125. [CrossRef]


<!-- Page 20 -->


Materials 2020, 13, 5755 20 of 23


97. Liu, W.; Anguelov, D.; Erhan, D.; Szegedy, C.; Reed, S.; Fu, C.; Berg, A.C. Ssd: Single shot multibox detector. In Proceedings of the European Conference on Computer Vision (ECCV), Amsterdam, The Netherlands, 8–16 October 2016; pp. 21–37. [CrossRef] 98. Ren, S.; He, K.; Girshick, R.; Sun, J. Faster r-cnn: Towards real-time object detection with region proposal networks. IEEE Trans. Pattern Anal. Mach. Intell. 2017, 39, 1137–1149. [CrossRef] [PubMed] 99. Simonyan, K.; Zisserman, A. Very deep convolutional networks for large-scale image recognition. arXiv 2014, arXiv:1409.1556. 100. Fu, C.; Liu, W.; Ranga, A.; Tyagi, A.; Berg, A.C. Dssd: Deconvolutional single shot detector. arXiv 2017, arXiv:1701.06659. 101. Girshick, R.; Donahue, J.; Darrell, T.; Malik, J. Rich feature hierarchies for accurate object detection and semantic segmentation. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2014, Columbus, OH, USA, 24–27 June 2014; pp. 580–587. [CrossRef] 102. He, K.; Zhang, X.; Ren, S.; Sun, J. Spatial pyramid pooling in deep convolutional networks for visual recognition. IEEE Trans. Pattern Anal. 2015, 37, 1904–1916. [CrossRef] 103. Girshick, R. Fast r-cnn. In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2015, Santiago, Chile, 7–13 December 2015; pp. 1440–1448. [CrossRef] 104. He, K.; Gkioxari, G.; Dollár, P.; Girshick, R. Mask r-cnn. In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2017, Venice, Italy, 22–29 October 2017; pp. 2961–2969. [CrossRef] 105. Meng, M.; Chua, Y.J.; Wouterson, E.; Chin, P. Ultrasonic signal classiﬁcation and imaging system for composite materials via deep convolutional neural networks. Neurocomputing 2017, 257, 128–135. [CrossRef] 106. Droubi, M.G.; Faisal, N.H.; Orr, F.; Steel, J.A.; El-Shaib, M. Acoustic emission method for defect detection and identiﬁcation in carbon steel welded joints. J. Constr. Steel Res. 2017, 134, 28–37. [CrossRef] 107. Alobaidi, W.M.; Alkuam, E.A.; Al-Rizz, H.M.; Eric, S. Applications of ultrasonic techniques in oil and gas pipeline industries: A review. Am. J. Oper. Res. 2015, 5, 274. [CrossRef] 108. Boaretto, N.; Centeno, T.M. Automated detection of welding defects in pipelines from radiographic images DWDI. NDT-E Int. 2009, 86, 7–13. [CrossRef] 109. Masserey, B.; Fromme, P. Surface defect detection in stiffened plate structures using Rayleigh-like waves. NDT-E Int. 2017, 42, 564–572. [CrossRef] 110. Kazantsev, I.G.; Lemahieu, I.; Salov, G.I.; Denys, R. Statistical detection of defects in radiographic images in nondestructive testing. Signal Process 2002, 82, 791–801. [CrossRef] 111. Wilson, J.W.; Tian, G.Y. Pulsed electromagnetic methods for defect detection and characterisation. NDT-E Int. 2007, 40, 275–283. [CrossRef] 112. Arora, V.; Siddiqui, J.A.; Mulaveesala, R. Hilbert transform-based pulse compression approach to infrared thermal wave imaging for sub-surface defect detection in steel material. Insight-Non Test. Cond. Monit. 2014, 56, 550–552. [CrossRef] 113. Lascoup, B.; Perez, L.; Autrique, L.; Antoine, C. On the feasibility of defect detection in composite material based on thermal periodic excitation. Compos. Part B Eng. 2013, 45, 1023–1030. [CrossRef] 114. Moon, H.; Chellappa, R.; Rosenfeld, A. Optimal edge-based shape detection. IEEE Trans. Image Process. 2002, 11, 1209–1227. [CrossRef] 115. Amit, Y.; Geman, D.; Fan, X. A coarse-to-ﬁne strategy for multiclass shape detection. IEEE Trans. Pattern Anal. Mach. Intell. 2004, 26, 1606–1621. [CrossRef] 116. Atherton, T.J.; Kerbyson, D.J. Size invariant circle detection. Image Vision Comput. 1999, 17, 795–803. [CrossRef] 117. Zhou, X.; Zifer, T.; Wong, B.M.; Krafcik, F.L. Color detection using chromophore-nanotube hybrid devices. Nano Lett. 2009, 9, 1028–1033. [CrossRef] 118. Karimi, M.H.; Asemani, D. Surface defect detection in tiling Industries using digital image processing methods: Analysis and evaluation. ISA Trans. 2014, 53, 834–844. [CrossRef] 119. Tsai, D.M.; Chiang, I.Y.; Tsai, Y.H. A shift-tolerant dissimilarity measure for surface defect detection. IEEE Trans. Ind. Inform. 2011, 8, 128–137. [CrossRef] 120. Bernieri, A.; Betta, G.; Ferrigno, L. Crack depth estimation by using a multi-frequency ECT method. IEEE Trans. Instrum. Meas. 2013, 62, 544–552. [CrossRef] 121. Komura, I.; Hirasawa, T.; Nagai, S. Crack detection and sizing technique by ultrasonic and electromagnetic methods. Nucl. Eng. Des. 2001, 206, 351–362. [CrossRef]


<!-- Page 21 -->


Materials 2020, 13, 5755 21 of 23


122. Schlichting, J.; Maierhofer, C.; Kreutzbruck, M. Crack sizing by laser excited thermography. NDT-E Int. 2012, 45, 133–140. [CrossRef] 123. Hu, G. Automated defect detection in textured surfaces using optimal elliptical Gabor ﬁlters. J. Constr. Steel Rest. 2017, 134, 28–37. [CrossRef] 124. Liang, B.; Iwnicki, S.; Ball, A.; Young, A.E. Adaptive noise cancelling and time–frequency techniques for rail surface defect detection. Mech. Syst. Signal Process. 2015, 54, 41–51. [CrossRef] 125. Ge, J.; Li, W.; Chen, G.; Yin, X.; Yuan, X.; Yang, W.; Liu, J.; Chen, Y. Multiple type defect detection in pipe by Helmholtz electromagnetic array probe. NDT-E Int. 2017, 91, 97–107. [CrossRef] 126. Koike, R.; Kakinuma, Y.; Aoyama, T. Drill fracture detection by integrating disturbance observer and rotational digital ﬁlter. CIRP J. Manuf. Sci. Technol. 2014, 7, 177–184. [CrossRef] 127. Trottier, C.; Shahjahan, S.; Schumm, A.; Aubry, A.; Derode, A. Multiple Scattering Filter: Application to the Plane Defect Detection in a Nickel Alloy. Phys. Procedia 2015, 70, 795–798. [CrossRef] 128. Zou, Y.; Du, D.; Chang, B.; Ji, L.; Pan, J. Automatic weld defect detection method based on Kalman ﬁltering for real-time radiographic inspection of spiral pipe. NDT-E Int. 2015, 72, 1–9. [CrossRef] 129. Zhang, S.; He, Q.; Ouyang, K.; Xiong, W. Multi-bearing weak defect detection for wayside acoustic diagnosis based on a time-varying spatial ﬁltering rearrangement. Mech. Syst. Signal Process. 2018, 100, 224–241. [CrossRef] 130. Mak, K.; Peng, P.; Yiu, K.F.C. Fabric defect detection using morphological ﬁlters. Image Vis. Comput 2009, 27, 1585–1592. [CrossRef] 131. Choi, D.; Jeon, Y.; Lee, S.J.; Yun, J.P.; Kim, S.W. Algorithm for detecting seam cracks in steel plates using a Gabor ﬁlter combination method. Appl. Opt. 2014, 53, 4865–4872. [CrossRef] [PubMed] 132. Jian, C.; Gao, J.; Ao, Y. Automatic surface defect detection for mobile phone screen glass based on machine vision. Appl. Soft. Comput. 2017, 52, 348–358. [CrossRef] 133. Czimmermann, T.; Ciuti, G.; Milazzo, M. Visual-Based Defect Detection and Classiﬁcation Approaches for Industrial Applications-A SURVEY. Sensors 2020, 20, 1459. [CrossRef] 134. Hoang, D.; Kang, H. A survey on Deep Learning based bearing fault diagnosis. Neurocomputing 2019, 335, 327–335. [CrossRef] 135. Wei, X.; Yang, Z.; Liu, Y.; Wei, D.; Jia, L.; Li, Y. Railway track fastener defect detection based on image processing and deep learning techniques: A comparative study. Eng. Appl. Artif. Intell. 2019, 80, 66–81. [CrossRef] 136. Yi, L.; Li, G.; Jiang, M. An End-to-End Steel Strip Surface Defects Recognition System Based on Convolutional Neural Networks. Steel Res. Int. 2017, 88, 1600068. [CrossRef] 137. Kumar, S.S.; Abraham, D.M.; Jahanshahi, M.R.; Iseley, T.; Starr, J. Automated defect classiﬁcation in sewer closed circuit television inspections using deep convolutional neural networks. Autom. Constr. 2018, 91, 273–283. [CrossRef] 138. Chen, F.; Jahanshahi, M.R. NB-CNN: Deep learning-based crack detection using convolutional neural network and Naïve Bayes data fusion. IEEE Trans. Ind. Electron. 2017, 65, 4392–4400. [CrossRef] 139. Park, J.; Kwon, B.; Park, J.; Kang, D. Machine learning-based imaging system for surface defect inspection. Int. J. Proc. Eng. Manuf. Green Technol. 2016, 3, 303–310. [CrossRef] 140. Napoletano, P.; Piccoli, F.; Schettini, R. Anomaly detection in nanoﬁbrous materials by CNN-based self-similarity. Sensors 2018, 18, 209. [CrossRef] [PubMed] 141. Yang, Z.; Lu, S.; Wu, T.; Yuan, G.; Tang, Y. Detection of morphology defects in pipeline based on 3D active stereo omnidirectional vision sensor. IET Image Process 2017, 12, 588–595. [CrossRef] 142. Yuan, Z.; Zhang, Z.; Su, H.; Zhang, L.; Shen, F.; Zhang, F. Vision-based defect detection for mobile phone cover glass using deep neural networks. Int. J. Precis Eng. Manuf. 2018, 19, 801–810. [CrossRef] 143. Liu, R.; Gu, Q.; Wang, X.; Yao, M. Region-convolutional neural network for detecting capsule surface defects. Boletín Técnico 2017, 55, 92–100. 144. Krummenacher, G.; Ong, C.S.; Koller, S.; Kobayashi, S.; Buhmann, J.M. Wheel defect detection with machine learning. IEEE Trans. Intell. Transp. 2017, 19, 1176–1187. [CrossRef] 145. Lv, C.; Zhang, Z.; Shen, F.; Zhang, F.; Su, H. A Fast Surface Defect Detection Method Based on Background Reconstruction. Int. J. Precis. Eng. Manuf. 2019, 21, 363–375. [CrossRef]


<!-- Page 22 -->


Materials 2020, 13, 5755 22 of 23


146. Akram, M.W.; Li, G.; Jin, Y.; Chen, X.; Zhu, C.; Zhao, X.; Khaliq, A.; Faheem, M.; Ahmad, A. CNN based automatic detection of photovoltaic cell defects in electroluminescence images. Energy 2019, 189, 116319. [CrossRef] 147. Zhang, Z.; Wen, G.; Chen, S. Weld image deep learning-based on-line defects detection using convolutional neural networks for Al alloy in robotic arc welding. J. Manuf. Process 2019, 45, 208–216. [CrossRef] 148. He, T.; Liu, Y.; Xu, C.; Zhou, X.; Hu, Z.; Fan, J. A Fully Convolutional Neural Network for Wood Defect Location and Identiﬁcation. IEEE Access 2019, 7, 123453–123462. [CrossRef] 149. Caggiano, A.; Zhang, J.; Alﬁeri, V.; Caiazzo, F.; Gao, R.; Teti, R. Machine learning-based image processing for on-line defect recognition in additive manufacturing. CIRP Ann. 2019, 68, 451–454. [CrossRef] 150. Lv, Q.; Song, Y. Few-shot Learning Combine Attention Mechanism-Based Defect Detection in Bar Surface. ISIJ Int. 2019, 59, 1089–1097. [CrossRef] 151. BOSCH (Germany). Available online: https://www.bosch.com/company/ (accessed on 30 December 2019). 152. COMPUR Company. Available online: https://skgrimes.com/products/ (accessed on 16 December 2019). 153. BS Company. Available online: https://www.bs-company.com/en/index.html (accessed on 20 December 2019). 154. CMP Company. Available online: https://www.c-m-p.com/company-info/ (accessed on 6 July 2020). 155. Valley Industries Company. Available online: https://www.valleyind.com/ (accessed on 1 September 2020). 156. Rhein–Nadel Automation (RNA) Glass Defect Detection System. Available online: https://www. rnaautomation.com/products (accessed on 30 September 2018). 157. Visual Inspection System for Parts Defect. Available online: http://www.evenﬁt.com.cn/showal75.html (accessed on 26 December 2018). 158. Quality Control Checks System. Available online: https://www.rnaautomation.com/ (accessed on 21 January 2019). 159. EvenFit, Capsule Visual Inspection System. Available online: http://www.evenﬁt.com.cn/showpro25.html (accessed on 9 June 2019). 160. KEYENCE Product Size Measuring Instrument. Available online: https://www.keyence.com.cn (accessed on 8 June 2020). 161. AVI Soldering Appearance Inspection Machine. Available online: http://www.geeyoo.net/products.html (accessed on 13 July 2019). 162. Hardware and Workpiece Visual Measurement Equipment. Available online: https://yuyaonaide.1688. com/?spm=a261y.8881078.0.0.656d1321mIPSHy (accessed on 3 July 2018). 163. ET-F1 Engine Cylinder Bore Eddy Current Detector. Available online: http://www.bknzdh.com/product. html (accessed on 30 November 2020) 164. Deng, Y.; Pan, X.; Wang, X.; Zhong, X. Vison-Based 3D Shape Measurement System for Transparent Microdefect Characterization. IEEE Access 2019, 7, 105721–105733. [CrossRef] 165. Iglesias, C.; Martínez, J.; Taboada, J. Automated vision system for quality inspection of slate slabs. Comput. Ind. 2018, 99, 119–129. [CrossRef] 166. Su, Q.; Kondo, N.; Li, M.; Sun, H.; Al Riza, D.F.; Habaragamuwa, H. Potato quality grading based on machine vision and 3D shape analysis. Comput. Electron. Agric. 2018, 152, 261–268. [CrossRef] 167. Wen, X.; Song, K.; Huang, L.; Niu, M.; Yan, Y. Complex surface ROI detection for steel plate fusing the gray image and 3D depth information. Optik 2019, 198, 163313. [CrossRef] 168. Ouyang, W.; Wang, K.; Zhu, X.; Wang, X. Chained cascade network for object detection. In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2017, Venice, Italy, 22–29 October 2017; pp. 1956–1964. [CrossRef] 169. Bodla, N.; Singh, B.; Chellappa, R.; Davis, L.S. Soft-nms—improving object detection with one line of code. In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2017, Venice, Italy, 22–29 October 2017; pp. 2380–7504. [CrossRef] 170. Hu, H.; Gu, J.; Zhang, Z.; Dai, J.; Wei, Y. Relation networks for object detection. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2018, Salt Lake City, UT, USA, 18–22 June 2018; pp. 2380–7504. [CrossRef] 171. Dai, J.; Li, Y.; He, K.; Sun, J. R-fcn: Object detection via region-based fully convolutional networks. Adv. Neural Inf. Process. Syst. 2016, 198, 379–387.


<!-- Page 23 -->


Materials 2020, 13, 5755 23 of 23


172. Shen, Z.; Liu, Z.; Li, J.; Jiang, Y.; Chen, Y.; Xue, X. Dsod: Learning deeply supervised object detectors from scratch. In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2017, Venice, Italy, 22–29 October 2017; pp. 1919–1927. [CrossRef] 173. Dai, J.; Qi, H.; Xiong, Y.; Li, Y.; Zhang, G.; Hu, H.; Wei, Y. Deformable convolutional networks. In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2017, Venice, Italy, 22–29 October 2017; pp. 764–773. [CrossRef] 174. Lin, T.; Goyal, P.; Girshick, R.; He, K.; Dollár, P. Focal loss for dense object detection. IEEE Trans. Pattern Anal. Mach. Intell. 2020, 42, 318–327. [CrossRef] 175. Peng, C.; Xiao, T.; Li, Z.; Jiang, Y.; Zhang, X.; Jia, K.; Yu, G.; Sun, J. Megdet: A large mini-batch object detector. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition(CVPR) 2018, Salt Lake City, UT, USA, 18–22 June 2018; pp. 6181–6189. [CrossRef]


Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional afﬁliations.


c⃝2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).
