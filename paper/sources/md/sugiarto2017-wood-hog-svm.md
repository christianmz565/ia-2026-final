# sugiarto2017-wood-hog-svm


<!-- Page 1 -->


2017 2nd International Conferences on Information Technology, Information Systems and Electrical Engineering (ICITISEE)


Wood Identification Based on Histogram of Oriented Gradient (HOG) Feature and Support Vector Machine


(SVM) Classifier


Bambang Sugiarto1, Esa Prakasa1, Riyo Wardoyo1, Ratih Damayanti2, Krisdianto2, Listya Mustika Dewi2,


Hilman F. Pardede1, Yan Rianto1


1Research Center for Informatics, Indonesian Institute of Sciences, Bandung, Indonesia 2 Forest  Products  Research  and  Development Center, Bogor Email: bambang@informatika.lipi.go.id


Abstract—Forest areas in Indonesia covered about 2/3 of total land areas which has about 4000 wood species. Wood identification plays a key role in wood utilization not only for determining appropriate use but also for supporting legal timber trade. However, the identification process requires high expertise and complex method which can be done in the laboratory. In order to simplify the identification process, we develop wood identification using computer vision by using Histogram of Oriented Gradient (HOG) to extract the species of wood and Support Vector Machines (SVM) to classify wood species. These methods combination will improve the accuracy of wood identification process. The result showed that the HOG method can extract the texture of woods and SVM classifier can generate the boundary decision after executing the training process. By doing the testing process of SVM classifier, the result showed that the accuracy from the identification is 70.5% for using positive testing image and 77.5% for using negative testing image. This accuracy value can be reached because the texture for each training image has different texture pattern especially the number and location of vessels.


Keywords—Wood identification; computer vision; HOG Feature; SVM classifier;  legal timber


## I.  INTRODUCTION


Wood is one of the main forest products which support human needs so it is important to maintain its sustainability. Indonesia has more than 4,000 wood species grown in its tropical rain forest [1]. Each wood species has their special characteristics which can be differentiated one to another based on their anatomical structures through wood identification. Conventionally, identification process can be done by looking at both macroscopic and microscopic characteristics of wood species to determine the type of fibers, vessels, rays, and other structures. The process is time consuming and require good expertise from wood anatomists. This become an obstacle for frontline field officers who need to check wood species as soon as possible. Therefore, the development of automatic wood identification is highly required. One of methods is by detecting wood image using computer vision extraction which is more rapid and accurate to identify wood species compare to the conventional method.


## 978-1-5386-0658-2/17/$31.00 ©2017 IEEE 337


Recently, there are many researches to identify the species of wood by using computer vision method. In the paper [2], a portable vision system is developed to recognize different wood species based on its pores and concentric curve. By using multichannel Gabor filter as an extract method and Artificial Neural Network (ANN) as a classifier, the wood recognition can be done. Yusof et al. [3] and Khalid et al. [4] proposed a tropical wood species recognition based on multi-feature extractors and classifiers. Yusof et al. [3] using two feature extraction methods which are co-occurrence matrix approached known as grey level co-occurrence matrix (GLCM) and Gabor filter. However, Khalid et al. [4] using basic grey level aura matrix (BGLAM) and statistical properties of pores distribution (SPPD) technique to extract the wood features. Beside the detection of wood features, paper [5][6][7] also detected the wood defect using different method. Yang et al. [5] proposed a method of multi-scale edge detection based on dyadic wavelet transforms in order to solve the contradiction between noise suppression and edge continuity. In paper [6], Ke et al. used the hybrid algorithm of genetic algorithm and particle swarm optimizing algorithm to detect the wood defect. In order to extract the feature of wood defect images, paper [7] proposed an LBP features algorithm and by using BP neural network, the defect identification can be achieved.


The main difficulty in the wood identification is some of the wood species have a similar texture with the others so the extraction is the important process of identification. From paper [2][3][4], the basic extraction of wood identification are Gabor Filter and GLCM features. Gabor filter characterized by frequency and spatial information of the sample images. Furthermore GLCM characterized by calculating how often pairs of pixel with specific values and in a specified spatial relationship occur in an image.


In this paper, we propose a computer vision technique for wood identification by using Histogram of Oriented Gradient (HOG) to extract the species of wood. HOG measures the orientation and the strengths of wood image gradient within an image region. Different from the extraction method above, the HOG features can be achieved by dividing the image region into small region (cells). Each cell arranges a histogram of


<!-- Page 2 -->


2017 2nd International Conferences on Information Technology, Information Systems and Electrical Engineering (ICITISEE)


gradient direction for the pixels within the cell. In HOG method, the local histograms can be normalized by calculating a measure of the intensity across a larger the image region (blocks) to improve accuracy.


Generally, HOG method is used for various object detection. In paper [8], the HOG method was used to determine orientation of vehicle image for autonomous vehicle. Guzman et al. [9] proposed methodology for car detection in outdoor environment using HOG feature and SVM classifier. This detection result determines whether there is a car or not in the captured frame of the camera video. Paper [10] showed that the HOG method can be used for human detection and give more review about the pedestrian detection. Furthermore in the paper [11], the fungus spores in the air is an object detection through an optical sensor system. The detection applied HOG features and SVM for the classification purpose.


For the classifier, we propose Support Vector Machines (SVM) to classify the wood species. SVM is used to classify the extracted wood surface from the HOG feature. SVM is a machine learning which looks for the best decision boundary of classifying the wood species.


## II. METHODOLOGY OF  WOOD IDENTIFICATION


In this paper, the methodology to develop wood identification system by implementing HOG and SVM methods consists of three main steps namely preprocessing of the sample images, feature extraction using HOG method, then classification of the wood species by using SVM. In preprocessing step, some features in wood image data were enhanced for further processing. At the second step, feature extraction from the wood image was conducted by using HOG. The last step was classification process to get the identity of the wood through the learning process of SVM classifier.


Figure 1. Overview of the wood identification process using Histogram of


Oriented Gradient (HOG) and Support Vector Machine (SVM) methods


A. Object Detection


The object of this computer vision for wood identification was macroscopic image of wood cross section. The sample of the wood image of this project was obtained from the Forest Product Research and Development Center (FORDA), the Ministry of Environment and Forestry Republic of Indonesia. The size of images were 2560 x 2048 pixels. Fig. 2 shows some examples of the sample images.


Figure 2. Examples of wood images of some sample


B. Preprocessing of the Sample Images


In the preprocessing step, color normalization was applied to the wood images to enhance the clearness of the texture property. It changed the RGB (Red-Green-Blue) color image to grayscale. The formula of simple popular color image conversion to grayscale [12] is as follow:


B G R I b g r α α α + + = , (1)


where I is a intensity of the image and the non-negative coefficients αr, αg, αb have a condition:


1 = + + b g r α α α (2)


In this research, the conversion color image to grayscale is using formula of the recomendation BT.601:


B G R I 114 .0 587 .0 299 .0 + + = (3) This formula will make the original wood image become a grayscale image. Fig. 3 shows the example of image enhancement using RGB to grayscale conversion.


(a) (b) Figure 3.  (a) Original image  (b) Image enhancement using


RGB to grayscale conversion


338


<!-- Page 3 -->


2017 2nd International Conferences on Information Technology, Information Systems and Electrical Engineering (ICITISEE)


## C. Feature Extraction using HOG Method


HOG features descriptor is that local object appearance and shape within an image can be described by the distribution of density distribution of gradients [13][14]. The implementation of this descriptor can be achieved by dividing the image into small regions called a cell. Each cell compiles a histogram of gradient direction for the pixel within the cell. HOG method has four steps to extract the object [15]. First step is calculating the gradient values by applying 1-D centered to obtain the point of discrete derivative mask in horizontal and vertical direction as follow:


[ ]1 0 1 − = x D (4)








0 1


  


  


y D (5)


=


1


−








If the object image is I, we can obtain x and y derivative using convolution operation:


x x x D I I ∗ = and y y y D I I ∗ = (6)


For calculating the magnitude of gradient, the formula is


2 2 y x I I G + = , (7)


and for gradient orientation is given by


I arctan = θ (8)


y I


x


The second step is spatial orientation binning. This step has a function to give a result of cell histogram by a voting process. Each pixel of the wood image within the casts a weighted vote for orientation in accordance with the closest bin in the range 0 to 180 degrees. In the third step, there is the HOG descriptor to normalize cell and histogram from entire block region to be a vector form. The last step, the block normalization is performed by using the L2 norm as follow:


b b (9)


2 2 ε + =


b


For the implementation this HOG feature in identifying the wood image, these four steps can be seen in Fig.4.


Figure 4.  HOG feature process to identify the wood image After process HOG normalization, the windows descriptor is needed to collect descriptor from all the block and change into vector form. In this research, we use the 64 x 128 pixels detection window. This detection window will be divided into 7 blocks across and 15 blocks vertically then the total of the block is 105 blocks. Each block contains 4 cells with a 9-bin histogram for each cell and the total of value per block is 36 values. Because of this dimension, the final vector size of 7 blocks across x 15 blocks vertically x 4 cells per block x 9 bins per histogram = 3,780 values. In this research, this final vector is accommodated by the xml database for the input in the next step in classifier process.


## D. Support Vector Machine (SVM) Classifier


SVM is a supervised models associated with respect to learning algorithm and mainly used for analyzing the data for regression and classification [16]. SVM works by looking the best decision boundary located between the two classes boundary. The decision boundary is chosen to be the one for which the margin is maximized and the margin is the shortest distance from the decision boundary.


For determine a new sample belongs to a class one or class two after the model was training, the formula can be derived as follow [8]:


N





1 , ) ( ) ( ,                                 (10)


m n n n b x x k t a x y


+ =


n


=


where the conditions are:


0 ≥ n a (11)


0 1 ) ( ≥ − n n x y a (12) { } 0 1 ) ( = − n n n x y t a (13)


The value of an = 0 is not into the sum and can be discarded. Other points are known as supports vectors and this sample located at the nearest to decision boundary. These samples are used to make the classification considering these vectors enough to build the separating hyper plane. In wood identification, SVM is used to classify the species of wood through the testing process by resulting value of 1 from the correct data and value of -1 for the incorrect data.


339


<!-- Page 4 -->


2017 2nd International Conferences on Information Technology, Information Systems and Electrical Engineering (ICITISEE)


SVM must be trained prior to testing process. Data training are obtained from wood images within various wood species. This training data consist of positive and negative training data. The positive and negative training data consist of various wood image taken from the sample wood images. The positive training image is the image only contain the object of interest. In this case we use positive training image that corresponds to the appropriate wood species. The negative training image is the image provided for the training process without the object of interest. This means the image is not an appropriate wood species.


## III. EXPERIMENTAL  RESULT AND ANALYSIS


We have performed some wood identification experiments using the HOG feature and SVM classifier. Fig. 5 shows the testing procedure to obtain the result of classification.


Figure 5.  The testing procedure of identification the wood image


In our experiments, 5 species of wood image were used. There are durian burung (Durio carinatus Masters), eboni bergaris (Diospyros celebica Bakh.), jati (Tectona grandis L.f.), patin (Mussaendopsis beccariana Baill) and pelawan (Tristania ferruginea (C.T.White) P.G.W.). To collect training and testing image, the 2560 x 2048 pixel samples image are divided into two regions. The top region of this samples image are prepared for the training image and the bottom region for the testing image. Each region divided into eight sub image with size of a 640 x 512 pixel of training or testing images. Each species has a total of 40 training images and 40 testing image. Overall, a total of 200 images were used for training while another 200 images were used for testing.


The algorithms of HOG feature extraction and SVM classifier are implemented by using C++ and OpenCV libraries. OpenCV is an open source computer vision and machine learning software library. Through the C ++ language, the OpenCV library can be used in implementing some of the procedures in the HOG feature and SVM classifier. For


compilation and computation process, we use Grid LIPI, a public cluster for open collaboration and located at Cibinong– Bogor, Indonesia. This High Performance Computer (HPC) will help to provide a computation problem solution for researcher in their research process.


For the first experiment, we trained 40 positive training images and 40 negative training images for each wood species for SVM classifier. This training process has a function to generate a decision boundary of a support vector form. This support vector will use for determining the class of testing process. In this research, the support vectors saved into xml database for each woods species. The next experiment was a testing process using testing images. According to Fig. 5, the testing image will also be extracted with HOG feature for determining a final vector in the end of the extraction process. For this experiment, we also used 40 positive training images and 40 negative training images for each wood species.


Table I shows the result of the experiment using 40 positive testing images of each woods species. Table I shows that the result of the testing process for each wood species represents a various accuracy. The lowest accuracy value is durian burung. This is caused by the texture of this wood species has many vessels and the dimension of this vessel is bigger than the others. So after through the extraction process, the vessels position seems very clear. When the testing process, SVM classifier will compare this wood species in accordance with the decision boundary. The highest accuracy value is eboni bergaris because the texture for each training image has a small texture pattern. From the Table I, the average accuracy from all wood species using positive image is 70.5%.


## TABLE I.  THE TESTING RESULT OF THE POSITIVE IMAGES


Positive Image Accuracy


Wood Species


(%) Correct


Incorrect


(1)


(-1)


Durian Burung 19 21 47.5


Eboni Bergaris 40 0 100


Jati 33 7 82.5


Patin 23 17 57.5


Pelawan 26 14 65.0


## TABLE II.  THE TESTING RESULT OF THE NEGATIVE  IMAGES


Negative Image Accuracy


Wood species


(%) Correct


Incorrect


(-1)


(1)


Durian Burung 28 12 70.0


Eboni Bergaris 35 5 87.5


Jati 27 13 67.5


Patin 30 10 75.0


Pelawan 35 5 87.5


From the Table II above, the experiment using negative images has different accuracy value in each wood species due to the different in detail textures. This testing process using negative image in several wood species obtained accuracy


340


<!-- Page 5 -->


2017 2nd International Conferences on Information Technology, Information Systems and Electrical Engineering (ICITISEE)


values that does not reach a value of 100% and the average accuracy from all woods species is 77.5%. This is because of textures on negative testing images in this experiment something similar to the texture of the positive training image particularly of the visible vessels.


## IV. CONCLUSION


In this work, a methodology for identification wood was evaluated. Classification results showed HOG feature as a descriptor and give various accuracy for wood species depend on the texture of each species. The result showed that the accuracy from the identification is 70.5% for using positive testing image and 77.5% for using negative testing image. In the experiment using positive testing image, the lowest accuracy value is durian burung. This is caused by the texture of this wood species has many vessels and the dimension of this vessel is bigger than the others. This condition is different from eboni bergaris species within has a small texture pattern. In the experiment using negative testing image, the accuracy does not reach a value of 100% because the textures of negative testing images in this experiment something similar to the texture of the positive training image particularly of the visible vessels. The SVM classifier in this research was useful and efficient for a classifier in determining the species of wood for either a positive image or a negative image of the testing process.


## ACKNOWLEDGMENT


This research is a collaborative work between Research Center for Informatics, Indonesian Institute of Sciences (LIPI) and Forest Products Research and Development Center (FORDA). The work is funded by Ministry of Research, Technology and Higher Education under Research Grant INSINAS 2017.


## REFERENCES


[1] Forest Product Research and Development Center, the Ministry of


Forestry Republic of Indonesia, “4000 Jenis Pohon di Indonesia dan Index 4000 Jenis Kayu Indonesia”, Jakarta, 1992. [2] E. Yuliastuti, Suprijanto, and S, Retno S., “Compact Computer Vision


for Tropical Wood Species Recognition Based On Pores and Concentric Curve,” International Conference on Instrumentation Control and Automation (ICA), 28-30 August 2013, pp. 198-202, Bali, 2013. [3] R. Yusof, N. Ruthfalydia R., and M. Khalid, “Using Gabor Filters as


Image Multiplier for Tropical Wood Species Recognition System”, International Conference on Computer Modelling and Simulation, 24-26 March 2010, pp. 289-294, Cambridge, 2010. [4] M. Khalid, R. Yusof and M. Khairuddin, “Tropical Wood Species


Recognition System based on Multi-Feature Extractors and Classifier”, International Conference on Instrumentation Control and Automation (ICA), 15-17 November 2011, pp. 6-11, Bandung, 2011. [5] X.Yang, D. Qi and X. Li, “Multi-scale Edge Detection of Wood Defect


Images Based on the Dyadic Wavelet Transform”, International Conference on Machine Vision and Human-Machine Interface (MVHA), 24-25 April 2010, pp. 120-123, Kaifeng, 2010. [6] Z. Ke, Q. Zhao, C. Huang, P. Ai and J. Yi, “Detection of Wood Surface


Defects Based om Particle Swarm Genetic Hybrid Algorithm”,


International Conference on Audio, Language and Image Processing (ICALIP), 11-12 July 2016, pp. 375-379, Shanghai, 2016. [7] Z. Xiang, Z. Qin, L. Ying, J. Quan and C. Wei, “Identification of Wood


Defect Based on LBP Features”, The Chinese Control Conference, 2729 July 2016, pp. 4202-4205, Chengdu, 2016. [8] P.E. Rybski, D. Huber, D.D. Morris and R. Hoffman, “Visual


classification of coarse vehicle orientation using Histogram of Oriented Gradients Features”, The IEEE Intelligent Vehicle Symposium (IV), 2124 June 2010, pp. 1-8, San Diego, 2010. [9] S. Guzman, A. Gomez, G. Diez, D.S. Fernadez, “Car detection


methodology in outdoor environment based on histogram of oriented gradient (HOG) and support vector machine (SVM)”, The 6th LatinAmerica Conference on Networked and Electronic Media (LACNEM 2015), 23-25 September 2015, pp. 1-4, Medellin, 2015. [10] C.Q. Lai and S.S. Teoh, “A review on pedestrian detection techniques


based on Histogram of Oriented Gradient feature”, The IEEE Student Conference on Research and Development (SCOReD), 16-17 December 2015, pp. 1-6, Batu Ferringhi, 2015. [11] M.W. Tahir, N.A Zaidi, R. Blank, P.P Vinayaka, M.J. Vellekoop and W.


Lang, “Detection of fungus through an optical sensor system using the histogram of oriented gradients”, The IEEE Sensors 2016, 30 October-2 November 2016, pp. 1-3, Orlando, 2016. [12] Y. Wan and Q. Xie, “A Novel Framework for Optimal RGB to


Grayscale Image Conversion”, The International Conference on Intelligent Human-Machine System and Cybernetics (IHMSC), 27-28 August 2016. pp. 345-348, Hangzhou, 2016. [13] H. Ren and A. Li, “Object detection using edge histogram of oriented


gradient”, IEEE International Conference on Image Processing (ICIP), 27-30 October 2014, pp. 4057-4061, Paris, 2014. [14] J. Zhang, L. Liu, D. Huang, X. Fu and Q. Huang, “Clothing Co


Segmentation Based on HOG Feature and E-SVM Classifier”, International Conference on Digital Home (ICDH)”, 2-4 December 2016, pp. 16-19, Guangzhou, 2016. [15] M.M. Isaac and m. Wilscy, “A key point based copy-move forgery


detection using HOG features”, International Conference on Circuit, Power and Computing Technologies (ICCPCT), 18-19 March 2016, pp. 1-6, Nagercoil, 2016. [16] K. Srunitha and S. Padmavathi, “Performance of SVM classifier for


image based soil classification”, The International Conference on Signal Processing, communication, Power and Embedded System (SCOPES), 3-5 October 2017, pp. 411-415, Paralakhemundi, 2017.


341
