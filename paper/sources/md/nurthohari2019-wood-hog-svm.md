# nurthohari2019-wood-hog-svm


<!-- Page 1 -->


2019 IEEE International Conference on Internet of Things and Intelligence System (IoTaIS)


Wood Quality Classification Based on Texture and


Fiber Pattern Recognition using HOG Feature and


SVM Classifier


Zayyana Nurthohari1,  Muhammad Ary Murti2, Casi Setianingsih3


School of Electrical Engineering


Telkom University Bandung, Indonesia zaynnrth@student.telkomuniversity.ac.id1, arymurti@telkomuniversity.ac.id2, setiacasie@telkomuniversity.ac.id3


Abstract—Wood as a material for household appliance needs to be considered of quality. Quality of wood can be classified according to colours, texture, and wood fibre pattern differences. In general, wood industries have been doing the wood quality classified process using a conventional method with a sense of vision in which the results are subjective in terms of accuracy and time efficiency. Machine Learning is a solution to this problem of predicting and classifying data of wood quality. In this paper, the wood will be recognized using Histogram of Oriented Gradient to know the pattern and texture. Meanwhile, the classification method uses Support Vector Machine which will be compared to find the best accuracy and time computation. This system is given image input with five types of cedar classification such as Class A, Class B, Class C, Class D, and Class E took using Logitech C930e HD which is integrated with Arduino Uno for object detection process and conveyor. The Experiment achieve 90% of accuracy with time computation 1,40 s


Keywords—automatic wood classification, wood fibre pattern, histogram of oriented gradient, support vector machine.


## I. INTRODUCTION


Wood Industry as one of the source to improve the economic sector in Indonesia have a great potential to comply the society needs. Rather unfortunately, the technology for wood classification still traditional. Based on the paper of realtime surface grading of profiled wooden boards, the reproducible of correct classification just 55% by human graders [1]. Nowadays, automated classification machine is used to expedite the process.


The Industry 4.0 era had an impact on the whole aspect, especially in Machine Learning. Machine learning has been shown a good performance to classified wood quality imagebased classification. However, it was rarely applied in the wood industry. Therefore, it must develop technology to classify the wood by species, texture, and fibre pattern.


Various methods already developed by the researchers. For example, B, Sugiarto et al (2018) has identified wood classification using support vector machine (SVM) to classify five wood species based on its texture using the histogram of gradient feature. The performance evaluation has shown that the average is 70,5% for positive testing images and 77.5% using negative testing images. This occurs because the texture for each training images has different texture pattern from number and location of vessles. [2]. Hietaniemi et al (2011) have recognized lumber strength classification using two methods, k-NN and SVM. They were using solely knot


## 978-1-7281-2516-9/19/$31.00 ©2019 IEEE 123


features with performance evaluation are 83% for SVM and 71,73% for k-NN [3]. Turhan et al (2013) proposed a method of support vector machines in wood identification: the case of three Salix species from Turkey. They used three types of Salix species and got 95,2% for accuracy rate. [4]. In paper [5], Khalid et al (2011) proposed for recognition the tropical wood species system based on multi-feature extractors and classifier. The BGLM and SPPD used as a feature extractor with LDA and k-NN classifiers. The performance showed that the LDA classifier is better than k-NN. Hu et al (2019) have developed automated lumber classification using RestNet18. The sorting process classified by defects, species, and texture. The classification accuracy is 99.50% with average time is 0.003s with the high-performance laptop [6].


Hence, this research is proposed to develop an automated wood classification using conveyor based on fibre pattern and texture using HOG [7] and SVM [7] [8] method. The dataset uses five-type different qualities from cedar species. Image dataset acquired with Logitech C930e HD which integrated with Arduino Uno for sensor command.


## II. METHODOLOGY OF WOOD IDENTIFICATION AND


## CLASSIFICATION


In this paper, the methodology to implement automatic wood classification used HOG feature extraction and SVM classification methods consist of three subsystems, namely image acquisition, analysis system device and indicator system. In the image acquisition step, the ultrasonic sensor will detect the wood which passing through the sensor by conveyor. Next, data will be transmitted from the controller to the server use serial communication. The second step, the server will be received data and command camera to capture the object. Data from the image acquisition process will analysis by HOG and SVM. The result of classification will be transmitted to the controller. The last step is the indicator system. The classification result will appear by regretting one of the indicator lights.


A. Image Acquisition


The object will detect the wood on a conveyor belt using HC-SR04 which integrated with Arduino Uno as a controller to send data to the server about the information on wood detected. After that, the server will be capturing the wood using Logitech C930e HD which has resolution 1280 x 720 pixels. Image taken from 15 cm of height box surface which has a light condition that regulated using 72 cm LED strip 3 watts around the box with height 10 cm from the surface. The


Authorized licensed use limited to: University College London. Downloaded on May 24,2020 at 17:37:05 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 2 -->


2019 IEEE International Conference on Internet of Things and Intelligence System (IoTaIS)


box have 14 x 20 x 15 cm size. It already following any test to know the best condition from 5 cm, 10 cm, and 15 cm for height and light intensity using 3-watts led strip (71 lux), 3 watts led lamp (401 lux), and 6-watt lamp (1201 lux). The best accuracy using standard parameter HOG and SVM is 90% with time computation 3.86 s using 15 cm height and 3-watts led strip.


Fig. 1. Wood Identification


Fig. 2. Sample of Cedar wood each class.


Figure 2 shows the type of cedar classification from left is class A,  class B, class C, Class D, and Class E. It was divided depend on texture and fibre pattern of cedarwood. For class A have a tight fibre until class E have not tight fibre.


B. Analysis System


In the analysis system step, image acquisition will be converted to grayscale and resize to 427 x 240 pixels. It takes from several tests using 3 size of images like the original size 1280 x 720 pixels, 640 x 360 pixels, 427 x 240 pixels, and 320 x 180 pixels. The results showed the 427 x 240 pixels get an accuracy 100% and 3.08 s for time computation. After knowing the best size for image acquisition, the images will convert to grayscale. The simple formula for RGB to grayscale conversion [2] [9] is as follow:


  = (	 ∗0.3 +  ∗0.59 +  ∗0.11)


This formula will convert image become grayscale. Fig. 3


## 978-1-7281-2516-9/19/$31.00 ©2019 IEEE 124


Fig. 3. Sample of grayscale conversion image.


The next step is HOG features, this step would calculate the gradient value by applying 1-D centered to obtain point of the discrete derivative mask in the horizontal and vertical direction [2] as follows:


(, ) = (,  + 1) −(,  −1) (2)


(, ) = ( + 1, ) −( −1, ) (3)


For calculating the magnitude of gradient, the formula is:


µ =  ! + ! (4)


and for gradient orientation is given by:


'(


" = #$% &


'() (5)


The second step is the spatial orientation binning. This step has purposed to give a result of the cell histogram by a voting process. Every pixel of the image will be voted for orientation with the closest bin in the range 0 to 180 degrees. Next step, there is the HOG descriptor to normalize cell and histogram to be a vector form. The final step, the block normalization is performed using the L2-Hys norm as follows:


* = +


|+|(-.( (6)


With maximum of b is 0.2 than renormalizing. For the implementation of this HOG Feature could be seen in fig 4.


Fig. 4. HOG Feature Process to Identify the Wood Image


In this research, the 427 x 240 pixels detection window will be divided into 42 blocks across and 23 blocks vertically, for a total of 966 blocks. Each block contains 4 cells with a 9-bin histogram for each cell, for a total of 36 values per block. This brings the final vector size to 42 blocks across x 15 blocks vertically x 4 cells per block x 9-bins per histogram


Authorized licensed use limited to: University College London. Downloaded on May 24,2020 at 17:37:05 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 3 -->


2019 IEEE International Conference on Internet of Things and Intelligence System (IoTaIS)


= 22,680 values. This final vector is accommodated by the *.csv database for the input in the next step process.


The last step is the Support Vector Machine. This step has purposed to determine the class type for each image. Besides that, SVM work based on hyperplane or discriminatory boundaries that are used to improve the image of each class. The best hyperplane or discriminatory boundaries determined based on the margin at the maximum hyperplane point [10]. The linear classification hyperplane is denoted as follow:


/012( ) = ∑4 ∈6 778( 7, ) + * (7)


99 = : 1,


/012( ) ≥0


<#ℎ9 (8)


−1,


## C. Indicator System


Fig. 5. Indicator System.


The identified result will be sent to Arduino Uno with “K.x” code. x symbols representative of classification types such as A, B, C, D, or E. The code received will be processed by Arduino Uno to shift one of plate relay. The LED light will light up according to their respective class.


## III. EXPERIMENTAL RESULT AND ANALYSIS


The algorithms on HOG features and SVM classifiers are implemented by using python and OpenCV libraries. The material available for this research consisted of 110 cedar boards with dimensions of 196 x 65 x 5 mm. These materials are limited which got from Wood Industry at Purwakarta, West Java, Indonesia. The material was divided into five classes based on the texture and fibre pattern which every class has 22 samples. Fig 6 is the hardware appearance of this system. It has 3 subsystems which had mentioned in section II.


Fig. 6. Hardware Design.


For knowing the system performance, there are 4 experiments such as partition data test, the angle of the camera position test, the parameter on the HOG test, and the parameter of the SVM test. The first experiment purposed to collect training and testing images. For the parameter in HOG and SVM used default parameters. There were conducted on the randomly selected data set and the result is given in table 1.


## 978-1-7281-2516-9/19/$31.00 ©2019 IEEE 125


## TABLE I. RESULT OF ANGLE CAMERA


50% Train


60% Train


70% Train


80% Train


90% Train


% 50


% 40


% 30


% 20


% 10


Test


Test


Test


Test


Test


Accuracy (%) 69 80 60 75 90


Time (s) 0.52 0.65 0.82 0.99 1.21


The model’s performance from table 1, 90% train 10% test is the best accuracy. This relates to training data is bigger than testing data. Somehow, time computation was the longest of all. In this case, identification will be better when the training dataset was bigger than testing data. It will make a system know the characteristic of texture and fibre pattern each class. More data could mean more possibilities of extracting and revealing useful underlying knowledge. Albeit SVMs have proved extremely effective in solving a variety of pattern recognition tasks, their main drawback lies in huge time and memory complexities, depending on the training set size cardinality[13]. So, 90% train 10% test used as the parameter for the next test which each class has a total of 20 training images and 2 testing images.


Next experiment is changing the angle of the camera position test. This experiment purposed to know the best angle of the camera position for this system. The surface of the camera will be set with 5 angle positions such as +5° right side, +10° right side, 0°, +5° left side, and +10° left side. So, the results are given in Table 2.


## TABLE II. RESULT OF ANGLE CAMERA


0֠ +5֠ Left


+10֠ Right


+5֠ Right


+10֠ Left


Side


Side


Side


Side


Accuracy (%) 0 30 90 40 10


Time (s) 1.61 1.45 1.58 1.61 1.61


Based on table 2, the best accuracy got by 0° angle camera position with 90% performance rate. Meanwhile, for time computation have a similar value, but isn’t being a problem with little range every scenario. In this case, training dataset using wood fibre with the surface of the conveyor. It will be impacted by the system to detect the objects. Based on Sahki et al [11], from his paper about HOG based Fast human detection used a training database from the "INRIA pedestrian database" which contains two folders. Both folders have two kinds of images "post" and "neg". The post contains the normal positive training or test images centred on the person with their left-right reflections, and for neg contains the original negative training or test images without the humanlike a park, ocean, city environment, etc. These conditions could have an easier system to recognize the object in another position in the picture. It could take a conclusion, that 0° will be used for this experiment.


The third step is a HOG parameters test. In this section purposed to know the best parameter such as orientation, block norm, pixel per pixel, block per pixel. In figure 7 and figure 8 the results are given.


Figure 7 and figure 8 shows the result of the experiment using changing each indicator of HOG. There are various accuracy and time computation. The best parameter for this test is 100% with 2 s time computation using orientation 9, block norm L2-Hys, pixel per cell 10x10, and cell block 2x2. In this case, cells per block indicator show that each 2x2 is


Authorized licensed use limited to: University College London. Downloaded on May 24,2020 at 17:37:05 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 4 -->


2019 IEEE International Conference on Internet of Things and Intelligence System (IoTaIS)


bigger than a 4x4. It means 2x2 is more suitable for this system than 4x4. Besides that for pixel per pixel indicator, 10x10 is higher than 20x20 it means the gradient result in more detail and specificity. Besides that, Block value has a function to avoid the images from brightness and contrast intensity. This system suitable to control it using cell per block 2x2 and pixel per pixel is 10 x 10. Next, block norm indicator has variations value, it’s not have affected yet. Block normalization has a function to reduce the brightness and contrast changes in the image based on neighbour gradient cell. It has a purpose to keep the image feature from varying brightness and contrast changes by dividing each vector element with its vector length[7][14]. Last is orientations, the 9 value of orientation have an average accuracy of 66%. It means that the accuracy is lower than the 12 value of orientations. The 12 value of orientation has performance average is 70%. So, if the system using higher orientation value it will affect toward getting the best analysis for the detail of images and gradient value[7][15]. It could take a conclusion, that using orientation 9, block norm L2-Hys, pixel per cell 10x10, and cell block 2x2 is suitable for this system and get the best performance rate.


Fig. 7. The Performance Rate of HOG (Accuracy (%))


Fig. 8. The Performance Rate of HOG (Time (s))


## 978-1-7281-2516-9/19/$31.00 ©2019 IEEE 126


Authorized licensed use limited to: University College London. Downloaded on May 24,2020 at 17:37:05 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 5 -->


2019 IEEE International Conference on Internet of Things and Intelligence System (IoTaIS)


The last step is an SVM parameters test. In this section purposed to know the best parameter such as kernel type, c value, gamma and multiclass type.


Fig. 9. The Performance Rate of SVM (Accuracy (%))


## 978-1-7281-2516-9/19/$31.00 ©2019 IEEE 127


Fig. 10. The Performance Rate of SVM (Time (s))


Based on figure 9 and figure 10, the best performance rate was obtained when the linear kernel with one-versus-rest multiclass was 90% with 1.40 s. The smallest accuracy was a


Authorized licensed use limited to: University College London. Downloaded on May 24,2020 at 17:37:05 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 6 -->


2019 IEEE International Conference on Internet of Things and Intelligence System (IoTaIS)


radial basis function kernel with one-versus-one. The kernel type used to produce for getting the best accuracy in this system is the Linear kernel. Because of the process when the database builds, the array of the image will flatten. That’s mean, the image array data from each column-major moved to one row or be flattened into a 1-D iterator over the array. This database has been modified into text data with column 1 is the type of classification and 2 until the end is the code of images. C or gamma is the parameter for the soft margin cost function, which controls the influence of each individual support vector; this process involves trading error penalty for stability. A linear kernel is one of the kernels suitable for text classification. Besides that, Radial Basis Function is nonlinearly mapped samples into a higher dimensional space so it, unlike the linear kernel, can handle the case when the relation between class labels and attributes is nonlinear [12]. A polynomial kernel is one of the non-linear kernels with have less time consuming and provides more accuracy than the RBF or linear kernels. It could take a conclusion, that linear kernel is possible to use in this scenario and the best performance rate is 90% and 1.40 second for the condition C = 1 with multiclass OVR and linear kernel.


## IV. CONCLUSION


This paper explores a methodology for implementing automated wood classification based on texture and fibre pattern using the histogram of oriented gradient feature and support vector machine classifier. Classification result showed that the performance rate of this system is 90% with time computation 1.40 using HOG and SVM. The scenario using the difference of the data set is 90% of training data and 10% testing test. Besides that the angular position of the camera is 0°. The SVM classifier in this research was useful during the use of linear kernel and one-versus-rest multiclass. This condition efficient for classifying and recognize the cedar texture and fibre pattern.


## 978-1-7281-2516-9/19/$31.00 ©2019 IEEE 128


## REFERENCES


[1] P. W and S. G, "Real-time Surface Grading of Profiled Wooden


Boards," Joanneum Reaserch, vol. II, pp. 283-298, 1992.


[2] B. Sugiarto, E. Prakasa, R. Wardoyo, R. Damayanti, K. L. M. Dewi, H.


F. Pardede and Y. Rianto, "Wood Identification Based on Histogram of Oriented Gradient (HOG) Feature and Support Vector Machine (SVM) Classifier," in 2017 2nd International conferences on Information Technology, Information Systems and Electrical Engineering (ICITISEE), Yogyakarta, 2017. [3] R. Hietaniemi, J. Hannuksela and O. Silv´en, "Camera Based Lumber


Strength Classification System," in MVA2011 IAPR Conference on Machine Vision Applications, Nara, 2011.


[4] K. Turhan and B. Serdar, "Support Vector Machines in Wood


Identification: The Case of Three Salix species from Turkey," Turkish Journal of Agriculture and Forestry, vol. 37, pp. 249-256, 2013.


[5] M. Khalid, R. Yusof and A. S. M. Khairuddin, "Tropical wood species


recognition system based on multi-feature extractors and classifiers," in 2011 2nd International Conference on Instrumentation Control and Automation, Bandung, 2011. [6] J. Hu, W. Song, W. Zhang, Y. Zhao and A. Yilmaz, "Deep Learning


for use in lumber classification task," Wood Science and Technology, vol. 53, pp. 505-517, 2019. [7] N. Dalal and B. Triggs, "Histograms of Oriented Gradients for Human


Detection," in IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR'05), San Diego, 2005. [8] I. Y. Gu, H. Anderson and R. Vicen, "Automatic Classification of


Wood Defects Using Support Vector Machine," in International Conference on Computer Vision and Graphics, Berlin, 2008. [9] R. Yusof, M. Khalid and A. S. M. Khairuddin, "Fuzzy data


management on pores arrangement for tropical wood species recognition system," in 2013 Science and Information Conference, London, 2013. [10] J. S. Prakash, K. A. Vignesh, C. Ashok and R. Adithyan, "Multi class


Support Vector Machines classifier for machine vision application," in 2012 International Conference on Machine Vision and Image Processing (MVIP), Taipei, 2012. [11] M. K. S. Sahki dan M. L. N. Ouadah, “HOG Based fast Human


Detection,” dalam 24th International Conference on Microelectonics (ICM), Algiers, 2012. [12] C. W. Hsu, C. C. Chang dan C. J. Lin, “A Practical Guide to Support


Vector Classification,” Department of Computer Science, National Taiwan University, Taipei, 2003. [13] J. Nalepa dan M. Kawulok, “Selecting training sets for support vector


machines: a review,” Springer Netherlands, vol. 52, no. 2, pp. 857-900, 2018.


[14] R.D.Atmaja,  M.A. Murti, J. Halomoan, F. Y. Suratman, "An


image processing method to convert RGB image into binary", Indonesian Journal of Electrical Engineering and Computer Science, vol. 3(2), pp.377-382,  2016.


[15] R. D. Atmaja, E. Susanto, J. Halomoan, G. K. Indraloka,  M. A. Murti.


"The detection of straight and slant wood fiber through slop angle fiber feature." TELKOMNIKA Indonesian Journal of Electrical Engineering, vol. 14, pp. 318-322, 2015.


Authorized licensed use limited to: University College London. Downloaded on May 24,2020 at 17:37:05 UTC from IEEE Xplore.  Restrictions apply.
