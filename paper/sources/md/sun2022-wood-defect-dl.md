# sun2022-wood-defect-dl


<!-- Page 1 -->


Hindawi Mathematical Problems in Engineering Volume 2022, Article ID 4878090, 9 pages https://doi.org/10.1155/2022/4878090


Research Article Wood Quality Defect Detection Based on Deep Learning and Multicriteria Framework


Ping’an Sun 1,2


1College of Chemistry and Materials Engineering, Zhejiang A&F University, Linan 311300, China 2School of Mathematics and Computer Science, Wuyi University, Wuyishan 354300, China


Correspondence should be addressed to Ping’an Sun; wyuspa@wuyiu.edu.cn


Received 8 April 2022; Revised 2 May 2022; Accepted 4 May 2022; Published 26 May 2022


Academic Editor: Zaoli Yang


Copyright © 2022 Ping’an Sun. Tis is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


Traditional nondestructive testing technology for wood defects has a series of problems such as low identiﬁcation accuracy, high cost, and cumbersome operation, and traditional testing methods cannot accurately show the speciﬁc location and size of wood internal defects; it is urgent to explore a new nondestructive testing scheme for wood defects. Aiming at this problem, this paper designs and develops an automatic detection method for wood surface defects based on deep learning algorithm and multicriteria framework. By comparing the performance of diﬀerent deep learning detection methods on the data set, the advantages and disadvantages of the detection method in this paper are proved. After a series of works, such as the development and optimization of the experimental algorithm, the algorithm proposed meets the requirements in both the detection accuracy and training time.


## 1. Introduction


As a country occupying huge forest resources, China’s vast land has many rare wood and endless ancient trees worth our protection [1]. In recent years, China’s productivity has developed rapidly, the economy has been improving at a high speed, the demand for all kinds of diﬀerent resources is increasing, the consumption of resources has increased sharply, and the demand for wood resources is growing rapidly. Wood resources play an indispensable role in the development of various ﬁelds in China. Terefore, how to improve the eﬀective utilization rate of wood, ensure the sustainable development of forest resources, and reduce the necessity of felling trees is very important [2].


Wood nondestructive testing technology has become more and more popular because of its important research signiﬁcance and the application potential in the protection of ancient and famous trees and the utilization of wood resources. Compared with the traditional destructive detection technology, its nondeformation advantage breaks through the shackles of the measured wood shape and size, and it can be widely used in ancient buildings, wood detection, ancient and famous tree protection, urban forestry,


wood processing, and other ﬁelds [3]. Tese factors will increase the production cost of wood-processing enterprises; reduce the mechanical properties of wood, appearance quality, and wood utilization rate; and consume a lot of wood resources [4]. However, the above works may be affected by the subjective factors, which will eventually aﬀect the detection eﬀect of defects.


Terefore, in order not to be aﬀected by the subjective factors of workers, machine vision and intelligent recognition technology are used to replace artiﬁcial vision to detect wood defects, and wood intelligent processing equipment is designed to integrate wood defect feature recognition and intelligent sorting and other functions, which can improve the wood production eﬃciency and reduce the production cost of enterprises [5]. Ensuring the maximum yield of wood plays a very positive role. For nearly half a century, wood nondestructive testing technology, as a new technology with high value and wide research, has made a qualitative leap in the 21st century. Wood nondestructive testing technology is usually used to detect wood and the internal defects of wood imaging with the aid of the naked eye, ultrasonic, stress wave, ray, infrared, and computer so that the detection personnel can intuitively understand the


<!-- Page 2 -->


2629, 2022, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2022/4878090 by Cochrane Chile, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 2 Mathematical Problems in Engineering


internal defects of wood. It can be known that there are more than 20,000 ancient and famous trees in Hangzhou alone, among which, 12,000-year-old ginkgo and 1500-year-old osmanthus require nondestructive testing of wood so as to make timely protection and treatment [6]. To sum up, the practical application scenarios of wood nondestructive testing technology are abundant.


Based on the above analysis, at present, the detection and classiﬁcation of wood defects in China mainly rely on manual selection [7]. (is method is susceptible to subjective factors, so it is diﬃcult to meet the needs of high-precision defect detection in the actual generation process. In addition, the human cost is getting higher and higher, resulting in higher cost of wood processing the standard cannot be uniﬁed, the actual detection classiﬁcation is diﬃcult to ensure enough accuracy, and it is urgent to take more ideal solutions to overcome the current problems. (erefore, in order to improve the eﬃciency of wood defect detection, machine vision and deep learning technology are used to replace artiﬁcial vision for wood defect detection. Based on high-tech support, it can not only improve the eﬃciency of wood processing but also help enterprises save production costs and reduce the input of human resources. (rough this research, the purpose is to put forward a fast detection speed, high detection accuracy of solid wood panel defect detection algorithm, reduce the cost of wood-processing enterprises, improve the eﬃciency of wood defect detection, and improve the degree of automation of wood-processing enterprises [8].


On the other hand, due to the development of computer hardware technology in recent years, especially the upgrade of GPU, the eﬃciency of computing and image processing has been greatly improved. Among the advanced methods, the convolutional neural network (CNN) represents deep learning. Practical application scenarios are image recognition, natural language processing, and speech recognition. (e traditional manual detection is limited to the subjective cognitive of people. When diﬀerent people detect the same piece of wood and identify the defects of wood, the size and location of the defects will be determined, resulting in diﬀerent results [3]. And manual detection requires a long time, the detection of manpower and material resources are too large, and this detection method has been slowly eliminated with the development of the era. Image recognition using deep learning does not need to carry out the complex process of manual feature extraction but can completely carry out feature extraction and recognition from the input image end to end, which greatly liberates manpower. Moreover, the feature of autonomous learning is no less than that of manual feature extraction by experience, and the recognition eﬀect is better [9].


## 2. Related Work


2.1. Research Status of Wood Nondestructive Testing Technology. Wood nondestructive testing technology can detect wood defects without destroying the original state of wood, and quickly and correctly identify the required wood defect target information, which can be used as the


theoretical basis for intelligent detection of wood defects. Nondestructive testing of wood defects can automatically classify wood raw materials, improve the intelligence and automation of the whole production line of wood-processing enterprises, and bring economic beneﬁts to woodprocessing enterprises [10].


Jayne was the ﬁrst to hypothesize the feasibility of nondestructive testing in wood [11]. (e wood industry technology of some developed countries such as Europe and the United States developed rapidly in the 1950s and beneﬁted from the social environment at that time. When some technology can reduce the loss of wood resources and improve production eﬃciency, it will be paid great attention to by relevant practitioners, and nondestructive testing technology can be used with wood from this. (e authors of [12] used a stress wave timer to accurately calculate the propagation speed of stress waves between healthy and decayed trees during the experiment. (e calculation results showed that the propagation speed of stress waves between healthy and decayed trees would be greatly reduced if there were certain cavities or decayed trees in the sample. (e authors of [13] dissected the propagation path of stress waves over wood faults and found that stress wave technology has very high research signiﬁcance in the ﬁeld of wood detection. In response to this discovery, stress wave imaging technology was discussed in 2000. (e authors of [14] and other experts focused on analyzing the inﬂuence of diﬀerent number of sensors and diﬀerent distribution of sensors on experimental samples on stress wave monitoring of wood internal defects.


(e authors of [15] used principal component analysis to reduce the dimension of wood spectral data and established a backpropagation (BP) neural network model processing data and classiﬁcation and identiﬁcation of wood species. (e more the tree species, the higher the identiﬁcation accuracy. (e authors of [16] designed Gabor ﬁlter and extracted Gabor feature parameters of wood defect image segmentation based on multidirection ﬁltering results. (e segmentation accuracy rate was 98.29%, which was better than the segmentation method based on the gray level cooccurrence matrix. (e authors of [17] combined the Gabor ﬁlter method with wavelet transform to identify the grayscale images of wood defects and introduced the multichannel Gabor ﬁlter, which could identify wood defects under the interference of complex background. (e authors of [18] used principal component analysis to reduce the dimension of extracted features which can eﬀectively identify and locate defects of complex inner holes. (e authors of [19] input ﬁve features including the ﬁrst three features of local binary mode and Tamura texture together with the entropy feature of gray co-occurrence matrix into the classiﬁer of the support vector machine, and the recognition accuracy is 91.67%, which is better than that of BP neural network classiﬁer, and the recognition accuracy of BP neural network is 82.75%. (e authors of [20] used the improved Grab Cuts algorithm for optimization to solve the problems of the image under segmentation and easy interference by regional texture in the traditional algorithm. (e authors of [21] proposed a method to detect wood


<!-- Page 3 -->


2629, 2022, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2022/4878090 by Cochrane Chile, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


Mathematical Problems in Engineering 3


defects based on the gray histogram. (e identiﬁcation of wood defects relies on color mutation, and defect images can be eﬀectively diﬀerentiated, but the speciﬁc type of wood defects cannot be determined. To solve this problem, the authors of [22] divided the image into subgraphs of the same size. (e accuracy of segmentation is 95%. (e BP neural network has good convergence, but the training time is slow, the defect recognition rate is low, and the sample demand is large. In terms of training time and recognition rate, SVM is superior to the BP network, and when the number of selected samples is not large, SVM can also achieve high accuracy in defect classiﬁcation. (e authors of [23] used wavelet transform to extract multidimensional feature vectors of wood defect images as vector input of BP and SVM neural network and carried out classiﬁcation and recognition through these two kinds of classiﬁers. Because of the high feature dimension of samples, the support vector machine is more advantageous. (e accuracy rate reached 93.3%. (e authors of [24] proposed an Otsu method, which used the weighted variance threshold method to detect wood surface defects.


Reference [25] used principal component analysis to detect wood defects, and the results showed that this method was applicable and reliable to identify wood defects. Ondrejka et al. [26] developed an algorithm framework based on deep learning, established a convolutional neural network composed of eight layers of networks for feature extraction, and extracted wood surface defect features from a deep learning network model, thus improving the detection eﬃciency and classiﬁcation accuracy of wood defects. Reference [27] used histogram threshold method to segment images, extracted wood defect characteristic values by principal component analysis, and improved classiﬁer by extreme learning machine algorithm combined with AdaBoost algorithm to improve the detection accuracy of wood defects and eﬀectively classify wood defects. (e authors of [28] were the ﬁrst to put forward the theoretical formula of log axial stress wave propagation, namely, displacement, velocity, stress, and strain equations. It was found that the stress wave propagation time and velocity were positively correlated with the wood elasticity, modulus, and length. Reference [29] used Arbotom stress wave detection system to detect the internal decay of wood logs of tree species in the northeast forest region, developed a stress wave nondestructive testing device based on a digital signal processor, and carried out practical testing on wood disks. Reference [30] used a method based on stress wave to reconstruct the structure of internal defects of wood, which could analyze the internal mechanism connections of wood and judge the types of internal defects by using the gray model. Reference [31] proposed an image reconstruction method based on the segmental propagation lines of the stress wave. (e method uses sensors to capture stress wave velocity data by hanging uniformly around the wood. (us, the defect images inside the wood can be reconstructed according to the visualization method. (e algorithm is based on precisely dividing light to facilitate spatial interpolation. (en, the image simulation and experimental data of


reconstructed wood internal defects are used to evaluate the method [32]. Meanwhile, the comparison of the area and shape of the image results shows that the proposed method can produce high-quality reconstruction with clear edges and high precision.


2.2. Research Status of Deep Learning and Multicriteria Framework. As a branch of machine learning, deep learning is gradually transitioning from shallow learning to deep learning. Deep learning is the nature of some deep web by means of nonlinear information processing mechanism, the training mode of combining to implement feature extraction and feature conversion of sample information, and ﬁnally with the help of the distributed feature representation to complex data relationship between ﬁtting samples [33]. Deep learning can realize the ﬁtting of observed samples and the continuous approximation of complex functions so as to learn the essential characteristics of conceptualization in data. Its advantages over the shallow learning model lie in its strong generalization performance and eﬀective representation of complex functions when dealing with complex classiﬁcation problems [34]. However, deep learning is not a new concept. Deep learning theory is the product of neural network development to a certain extent. Since the 1960s and 1970s, researchers in some developed countries have begun to try to use computers to help people understand the world they see and have achieved abundant scientiﬁc research results. (erefore, the neural network did not ﬂourish and experienced a cold winter period until the arrival of the 1990s, when LeCun applied the BP algorithm to the neural network, greatly improving the training speed of the traditional neural network. At the same time, the Lenet-5 network structure for handwritten digit recognition proposed by LeCun brought convolutional network into practical application for the ﬁrst time [35]. Nevertheless, the shallow layer was still the mainstream of neural network at that time.


Based on the above discussions, the contributions of this paper are given as below:


(1) (is paper is the ﬁrst to integrate multiframe criteria


into deep learning for defect detection of wood quality (2) In this paper, deep learning is used to better extract


wood features so as to improve the quality defect detection accuracy of the model.


## 3. The Proposed Wood Quality Defect Detection Method


Due to the shallow network layer and the use of linear activation units, the early artiﬁcial neural network models are often unable to solve complex problems. So, in recent years, the convolutional neural network model is often used to solve complex image recognition problems. On the basis of the traditional fullconnection layer neural network, the convolutional neural network adds a convolution layer and pooling layer, and its core ideas mainly include local connection weight sharing and


<!-- Page 4 -->


2629, 2022, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2022/4878090 by Cochrane Chile, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 4 Mathematical Problems in Engineering


Input and Convolution Pooling Pooling Fully connected Convolution


Figure 1: Schematic diagram of convolutional neural network.


pooling. (e model structure of the convolutional neural network is shown in Figure 1, which consists of input layer, convolutional layer, pooling layer, fully connected layer, and output layer. In addition, the depth of the network layer can be increased by increasing the number of convolutional layer, pooling layer, or full connection layer. In general, the convolutional layer and pooling layer can be designed alternately.


(e function of the convolution layer lies in the extraction of image features. (e essence of the convolution kernel is a ﬁlter matrix, which can produce many diﬀerent eﬀects on the original image. (e calculation process of convolution is shown below:


xi  act xi−1 ⊗ki + bi   􏼁. (1)


(en, the mathematical expression of sigmoid function is


f(x)  1 1 + e−x. (2)


(e mathematical expression of tanh function is


f(x)  ex −e−x


ex + e−x. (3)


(e mathematical expression of ReLu function is


f(x)  max(0, x). (4)


In addition to the above activation functions, another common activation (LeakyReLu) function is as follows:


x, x ≥0,


f(x) 


αx, x < 0. 􏼨 (5)


(e pooling layer is the lower sampling layer. After the pooling layer is pooled, the size of the original feature graph will be reduced and too much original feature graph information will not be lost. (erefore, the eﬃciency of the entire network operation can be improved to a certain extent. In addition, the pooling operation can maintain translation invariance within a certain range. Assuming that the original region size is 2 ∗2, the pooling operation is to calculate a value of the four values in the region according to certain rules.


(e output layer adopts softmax function to normalize, and the probability value in the corresponding category is shown in the following formula:


p yi  1 | xi; w, b   􏼁


ew1xi+b1


⎤⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦


⎡⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣


⎤⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦


⎡⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣


p yi  2 | xi; w, b   􏼁


ew2xi+b2


 1


ew3xi+b3


.


hw,b xi   􏼁


p yi  3 | xi; w, b   􏼁


j1 ewjxi+bj


􏽐n


· · ·


· · ·


ewnxi+bn


p yi  n | xi; w, b   􏼁


(6)


In classiﬁcation tasks, it is a common method to use cross-entropy loss function to evaluate the gap between the predicted value and true value. (e cross-entropy formula is as follows:


m


n


loss  −1


yjilog 􏽢yji 􏼐 􏼑. (7)


􏽘


m 􏽘


j1


i1


(e error calculated from the cross-entropy function needs to be calculated by backpropagation so as to realize the newer backpropagation of model parameters. (e original form of the gradient descent method is shown in the following formula:


θ ≔θ −α z


zθ J(θ). (8)


In the experiments of the following chapters, this paper also veriﬁes that the use of Adam has faster convergence than SGD. (e mathematical expression of a common Adam optimizer is as follows:


mt  β1mt−1 + 1 −β1   􏼁gt, (9)


vt  β2vt−1 + 1 −β2   􏼁g2


t. (10)


(erefore, the updating rule of gradient descent is as follows:


θt+1  θt − α  vt + ε √ mt. (11)


Based on equations (1)–(11), Figure 2 gives wood quality defect detection based on the deep learning and the multicriteria framework proposed in this paper.


<!-- Page 5 -->


2629, 2022, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2022/4878090 by Cochrane Chile, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


Mathematical Problems in Engineering 5


FC Output


CNN Feature mapping layer


Figure 2: Schematic diagram of CNN model based on multicriteria framework.


Figure 3: Simulation program running eﬀect.


## 4. Experimental Results and Analysis


4.1. Introduction to Experimental Data Set. To ensure the accuracy and eﬀectiveness of the research conclusions, all the experimental wood of this project is strictly selected by the workers of a company, and the ﬁr wood picture with a size of 1000 ∗100 ∗10 mm is used. (e size of images collected by the image acquisition system is 18000 ∗2048 ∗3 mm (width, height, and the number of channels), including wood photos and scanning background. In order to improve the quality of the data set and ensure the credibility of the experimental results, the number of images in the wood data set was expanded by rotating and magnifying the images as well as water and vertical mirror processing.


As shown in the ﬁgure, 2838 solid wood images were ﬁnally obtained, among which 612 were wood images without defects and the rest 2226. Each image contains one or more defects. Among these defect images, 846 are live nodule images, 760 are dead nodule images, and 620 are crack images. LabelMe software is used to annotate the defective wood pictures in the data set. LabelMe is written in Python language and uses Qt as the image annotation tool of its graphical interface. In practical application, LabelMe can perform polygon annotation and output data sets in COCO format, and its segmentation function is helpful to obtain defect masks in data set images from images.


4.2.ExperimentalResultsAnalysis. When selecting the void, the two points input by the user are embodied as the points on the center of the defect circle and the circumference of the defect so as to determine the position and size of the defect on the coordinate axis, and the white circle is represented in the painting area so as to distinguish it from the gray background. At the same time, the right display area shows the ﬁnal feature matrix diagram and can be saved to a preset path to select similar cracks and defects ﬂow.


(e function menu in the upper left corner of the program has the function of clearing and saving (Figure 3). Among them, the clear function is mainly used to clean the painting area and the display area of the image, restore the initial state, in order to facilitate the user to work again, and avoid the trouble of repeatedly opening the program. In the save function, the feature matrix image of the display area is saved in PNG format to a preset path by the system. Meanwhile, each feature matrix image is annotated in XML format in the directory.


(e detection model in this paper has a certain relationship between the cross ratio of internal defects of wood and the classiﬁcation of internal defects of wood. (e cross ratio of cracks (Figure 4(a)) and decay (Figure 4(b)) is lower than that of voids (Figure 4(c)), which conforms to the classiﬁcation rules of the classiﬁcation model. In conclusion, the detection eﬀect of the location and size of internal


<!-- Page 6 -->


2629, 2022, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2022/4878090 by Cochrane Chile, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 6 Mathematical Problems in Engineering


(a)


(b)


(c)


Figure 4: Test results of diﬀerent wood defect test data.


Figure 5: Location results of diﬀerent wood defects.


defects in wood is also good. (e ability of the generated recognition model to judge whether there are internal defects in wood is 99.8% on the test data set, the average IOU obtained by the model detection is 74.3%, and the


maximum center oﬀset is less than 1%, which has certain application value.


CNN model is used to ﬁne-tune the full connection layer of the model, retain the parameters of the


<!-- Page 7 -->


2629, 2022, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2022/4878090 by Cochrane Chile, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


Mathematical Problems in Engineering 7


(a) (b)


Figure 6: Solid wood panel defect detection. (a) Original; (b) detection result.


Figure 7: Defect detection eﬀect drawing based on multicriteria CNN.


convolution layer, and then conduct training and testing. As the number of iterations of the model gradually increases, the total loss value presents a downward trend on the whole and converges after a certain number of iterations.


In this paper, 100 images of live node, dead node, and worm eye were used for the gravity center positioning test. (e speciﬁc results of the test are shown in Figure 5. It can be seen from Figure 5 that the algorithm in this paper can accurately locate all kinds of defect types of wood, and the results can meet the actual needs. (e average error between the ﬁnal center of


gravity positioning and the manually measured center of gravity extraction is between (−1.10cm, 0.92cm).


(e ﬁrst to use the network on a sliding window in ﬁgure sliding, feature extraction network using Zeiler and Fergus Net (ZF-Net), the sliding window after the characteristics of each location on the map into a 256-dimensional feature vector, and then each feature vector into two full connection layer, a fully connected output layer contains the possibility and does not include the objectives. After obtaining the coordinates of each sliding window, the reference rectangular box is modiﬁed through coordinates, and each


<!-- Page 8 -->


2629, 2022, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2022/4878090 by Cochrane Chile, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## 8 Mathematical Problems in Engineering


Feature 1 Feature 2 Feature 3 Feature 4 Feature 5


Feature 6 Feature 7 Feature 8 Feature 9 Feature 10


Figure 8: Defect feature map.


reference rectangular box corresponds to 4 coordinates, respectively. Finally, 9 candidate regions are obtained for each sliding window position, and the scoring of candidate regions is represented by the 18 scores mentioned above, and 2 scores correspond to one candidate region. (e ﬁnal test results of solid wood panel passing CNN are shown in Figure 6. It can be seen from the original picture and the comparison picture that the method proposed in this paper has a good detection eﬀect of wood quality defects.


Based on the above illustrations, Figure 7 shows the types and locations of defects. It also shows the possibility of defect categories, which is called conﬁdence in the picture. In the ﬁrst column of the picture, the conﬁdence of live joints is 86.3% and that of dead joints is 96.2%. In the rest of the images, the conﬁdence of dead joints, live joints, and cracks was 99.8%, 99.2%, and 99.7%, respectively. Based on these results, we conclude that the detection performance of the proposed method is satisfactory.


As shown in Figure 8, these feature maps are extracted by Glance Network and are to be input into CNN’s wood features. By comparison, it is found that some ﬁlters extract features from the background, such as feature 1, some ﬁlters focus on the details of the input image, such as feature 5, and some ﬁlters focus on defects, such as features 4 and 8. Some features are similar, such as features 2 and 3 and features 9 and 10. (erefore, it is a waste of computing resources to input the features of all channels into CNN because the input of many similar features into the subsequent network will not greatly improve the experimental results but may lead to slower detection speed and thus take more time.


## 5. Conclusion


(e shortages of wood resources in our country have hindered the sustainable development of the wood-processing industry, with uneven quality of wood and limitations of artiﬁcial ingredients.


In view of the current wood nondestructive testing technique and traditional artiﬁcial detection technology for the defects in the related research, based on the CNN, generating wood internal defects recognition and detection models, and exploring the types of wood internal defects and model recognition rate, results show the generated model


has an eﬀect on wood internal defects recognition and classiﬁcation is better, which has veriﬁed the practicability of this method.


Data Availability


(e data used to support the ﬁndings of this study are available from the corresponding author upon request.


Conflicts of Interest


(e author declares no known competing ﬁnancial interests or personal relationships that could have appeared to inﬂuence the work reported in this paper.


## References


[1] S. Ge, S. Zuo, M. Zhang et al., “Utilization of decayed wood for


polyvinyl chloride/wood ﬂour composites,” Journal of Materials Research and Technology, vol. 12, pp. 862–869, 2021. [2] X. Yang, Z. You, Q. Dai, and J. Mills-Beale, “Mechanical


performance of asphalt mixtures modiﬁed by bio-oils derived from waste wood resources,” Construction and Building Materials, vol. 51, pp. 424–431, 2014. [3] M. Gao, D. Qi, H. Mu, and J. Chen, “A transfer residual neural


network based on ResNet-34 for detection of wood knot defects,” Forests, vol. 12, no. 2, p. 212, 2021. [4] M. Deluzet, T. Erudel, X. Briottet, D. Sheeren, and S. Fabre,


“Individual tree crown delineation method based on multicriteria graph using geometric and spectral information: application to several temperate forest sites,” Remote Sensing, vol. 14, no. 5, Article ID 1083, 2022. [5] Y. Hu, J. Li, M. Hong et al., “Short term electric load fore


casting model and its veriﬁcation for process industrial enterprises based on hybrid GA-PSO-BPNN algorithm-A case study of papermaking process,” Energy, vol.170, pp.1215–1227, 2019. [6] R. Espinosa, J. Palma, F. Jim´enez, J. Kami´nska, G. Sciavicco,


and E. Lucena-S´anchez, “A time series forecasting based multi-criteria methodology for air quality prediction,” Applied Soft Computing, vol. 113, Article ID 107850, 2021. [7] P. Huang, F. Zhao, Z. Zhu, Y. Zhang, X. Li, and Z. Wu,


“Application of variant transfer learning in wood recognition,” Bioresources, vol. 16, no. 2, pp. 2557–2569, 2021. [8] D. ˇSulyov´a and G. Koman, “(e signiﬁcance of IoTtechnology


in improving logistical processes and enhancing


<!-- Page 9 -->


2629, 2022, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2022/4878090 by Cochrane Chile, Wiley Online Library on [03/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


Mathematical Problems in Engineering 9


competitiveness: a case study on the world’s and Slovakia’s wood-processing enterprises,” Sustainability, vol. 12, no. 18, Article ID 7804, 2020. [9] S. Sharma and A. Kaul, “Hybrid fuzzy multi-criteria decision


making based multi cluster head dolphin swarm optimized IDS for VANET,” Vehicular Communications, vol. 12, pp. 23–38, 2018. [10] M. Sedliaˇcikov´a, Z. Strokov´a, and J. Dr´abek, “Controlling


implementation: what are the beneﬁts and barries for employees of wood processing enterprises?” Acta Facultatis Xylologiae Zvolen res Publica Slovaca, vol. 61, no. 2, pp. 163–173, 2019. [11] Z. He, K. P. Tran, and S. (omassey, “A deep reinforcement


learning based multi-criteria decision support system for textile manufacturing process optimization,” 2020, https:// arxiv.org/abs/2012.14794. [12] X. Du, J. Li, H. Feng, and S. Chen, “Image reconstruction of


internal defects in wood based on segmented propagation rays of stress waves,” Applied Sciences, vol. 8, no. 10, Article ID 1778, 2018. [13] U. Dackermann, K. Crews, B. Kasal et al., “In situ assessment


of structural timber using stress-wave measurements,” Materials and Structures, vol. 47, no. 5, pp. 787–803, 2014. [14] X. Du, S. Li, G. Li, H. Feng, and S. Chen, “Stress wave to


mography of wood internal defects using ellipse-based spatial interpolation and velocity compensation,” Bioresources, vol. 10, no. 3, pp. 3948–3962, 2015. [15] C. H. Lee, T. L. Wu, and Y. L. Chen, “Characteristics and


discrimination of ﬁve types of wood-plastic composites by FTIR spectroscopy combined with principal component analysis,” Holzforschung, vol. 64, pp. 17–29, 2010. [16] J. L. Raheja, S. Kumar, and A. Chaudhary, “Fabric defect


detection based on GLCM and Gabor ﬁlter: a comparison,” Optik, vol. 124, no. 23, pp. 6469–6474, 2013. [17] W. Hu, T. Wang, Y. Wang, Z. Chen, and G. Huang, “LE


MSFE-DDNet: a defect detection network based on low-light enhancement and multi-scale feature extraction,” >e Visual Computer, vol. 17, pp. 1–15, 2021. [18] C. Ding, Z. Feng, D. Wang, D. Cui, and W. Li, “Acoustic


vibration technology: toward a promising fruit quality detection method,” Comprehensive Reviews in Food Science and Food Safety, vol. 20, no. 2, pp. 1655–1680, 2021. [19] J. B. Amodei, J. Latorraca, G. Santos, and B. C. Martins,


“Wood quality of young teak in diﬀerent planting spaces,” Floresta e Ambiente, vol. 28, no. 4, pp. 11–23, 2021. [20] H. Zhang, H. Jing, and T. Chen, “Partial application of defect


detection in industry,” International Core Journal of Engineering, vol. 7, no. 7, pp. 144–147, 2021. [21] B. Wang, C. Yang, Y. Ding, and G. Qin, “Detection of wood


surface defects based on improved YOLOv3 algorithm,” Bioresources, vol. 16, no. 4, pp. 6766–6780, 2021. [22] M. Gao, F. Wang, P. Song, J. Liu, and D. Qi, “BLNN: mul


tiscale feature fusion-based bilinear ﬁne-grained convolutional neural network for image classiﬁcation of wood knot defects,” Journal of Sensors, vol. 2021, Article ID 8109496, 18 pages, 2021. [23] M. Mousavi and A. H. Gandomi, “Wood hole-damage de


tection and classiﬁcation via contact ultrasonic testing,” Construction and Building Materials, vol. 307, Article ID 124999, 2021. [24] X. Cao and G. Li, “An eﬀective method of wood crack trace


and quantity detection based on digital image processing technology,” in Proceedings of the 2021 13th International


Conference on Machine Learning and Computing, pp. 304– 309, Shenzhen, China, February 2021. [25] M. Radwan, D. V. (iel, and H. G. Espinosa, “Single-sided


microwave near-ﬁeld scanning of pine wood lumber for defect detection,” Forests, vol. 12, no. 11, p. 1486, 2021. [26] V. Ondrejka, T. Gergeˇl, T. Bucha, and M. P´astor, “Innovative


methods of non-destructive evaluation of log quality,” Central European Forestry Journal, vol. 67, no. 1, pp. 3–13, 2021. [27] E. A. B. Ibrahim, U. R. a. Hashim, L. Salahuddin et al.,


“Evaluation of texture feature based on basic local binary pattern for wood defect classiﬁcation,” International Journal of Advances in Intelligent Informatics, vol. 7, no. 1, pp. 26–36, 2021. [28] D. Riana, S. Rahayu, and M. Hasan, “Comparison of seg


mentation and identiﬁcation of swietenia mahagoni wood defects with augmentation images,” Heliyon, vol. 7, no. 6, Article ID e07417, 2021. [29] W. Du, Y. Xi, K. Harada, Y. Zhang, K. Nagashima, and


Z. Qiao, “Improved hough transform and total variation algorithms for features extraction of wood,” Forests, vol. 12, no. 4, pp. 466–482, 2021. [30] F. Delconte, P. Ngo, I. Debled-Rennesson, B. Kerautret,


V.-T. Nguyen, and T. Constant, “Tree defect segmentation using geometric features and CNN,” Reproducible Research in Pattern Recognition, vol. 5, pp. 80–100, 2021. [31] H. I. Lin and S. D. Sanjaya, “Wood polish classiﬁcation for


automated quality inspection based on AI vision,” in Proceedings of the 2021 21st International Conference on Control, Automation and Systems (ICCAS), pp. 1974–1977, IEEE, Jeju, Korea, October 2021. [32] L. Pan, R. Rogulin, and S. Kondrashev, “Artiﬁcial neural


network for defect detection in CT images of wood,” Computers and Electronics in Agriculture, vol. 187, Article ID 106312, 2021. [33] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature,


vol. 521, no. 7553, pp. 436–444, 2015. [34] Y. Li, F. Gimeno, and P. Kohli, “Strong generalization and


eﬃciency in neural programs,” 2020, https://arxiv.org/abs/ 2007.03629. [35] K. Cai, H. Chen, W. Ai, X. Miao, Q. Lin, and Q. Feng,


“Feedback convolutional network for intelligent data fusion based on near-infrared collaborative IoT technology,” IEEE Transactions on Industrial Informatics, vol. 18, no. 2, pp. 1200–1209, 2022.
