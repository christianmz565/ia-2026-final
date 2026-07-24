Automation in Construction 135 (2022) 104138


Available online 13 January 2022
0926-5805/© 2022 Elsevier B.V. All rights reserved.


Bounding-box object augmentation with random transformations for 
automated defect detection in residential building façades 


Kisu Lee a, Sanghyo Lee b,*, Ha Young Kim a,* 


a Graduate School of Information, Yonsei University, 50, Yonsei-ro, Seodaemun-gu, Seoul 03722, Republic of Korea 
b Division of Smart Convergence Engineering, Hanyang University ERICA, 55, Hanyangdaehak-ro, Sangnok-gu, Ansan-si, Gyeonggi-do 15588, Republic of Korea   


A R T I C L E I N F O  


Keywords: 
Data augmentation 
Multi-class defect detection 
Bounding box 
Efficient maintenance strategy 
Residential building façade 
Unmanned aerial vehicles 


A B S T R A C T  


This study proposes a novel bounding-box object augmentation (BoxAug) method to improve the performance of 
deep learning models in detecting defects in residential building façades. The most significant characteristic of 
the method is that it augments objects in images, rather than augmenting images, to solve the data imbalance 
problem. Moreover, it employs the bounding-box form for object detection, instead of the segmentation mask 
form. To evaluate the method, 7635 images obtained using unmanned aerial vehicles were utilized as the original 
training dataset. The faster region-based convolutional neural network model trained with the augmented 
training dataset using the method exhibited better performance than the model trained with the original dataset. 
Particularly, the class with the least objects in the original dataset displayed a markedly improved performance. 
Thus, the method can serve as an auxiliary method for effectively augmenting real-world image datasets with an 
unbalanced number of objects.   


1. Introduction 


Residential building façades mainly serve to protect occupants and 
structural components from natural forces and provide thermal and 
sound insulation [1]. However, due to the permanent exposure to 
adverse environmental conditions during their decades-long service life, 
façades often suffer from more serious degradation than other building 
components [2], which can be aggravated by poor material properties, 
improper design and construction, and inadequate maintenance. The 
neglect of façade defects can negatively affect the aesthetic appearance, 
shorten the service life, and increase the maintenance cost of residential 
buildings [3]. This highlights the need for efficient maintenance stra­
tegies for the early detection of defects in the residential building fa­
çades [4]. 


Façade conditions can be quantitatively evaluated via traditional 
human-based inspection based on the observation of the locations and 
sizes of defects by inspectors [5]. However, defect detection via human- 
based inspection is time consuming, is labor intensive, has high risk, and 
can be inaccurate. Moreover, the skill level and experience of the in­
spectors significantly influence the defect detection accuracy [6,7]. This 
leads to high maintenance costs, low maintenance efficiency, and po­
tential security risks [8]. Therefore, an automatic defect detection 


method is required for the efficiency and objectivity of damage 
assessment. 


Recently, deep convolutional neural networks (DCNNs) have been 
applied for image classification and object detection in computer vision 
[9], and DCNN-based defect detection has been investigated in previous 
studies [4,6–8]. The performance of DCNNs is dependent on the avail­
ability of significant training data [10–12]. 


However, sufficient defect training data for residential building fa­
çades are difficult to obtain. Basically, well-annotated publicly available 
databases for façade defects are lacking, such as ImageNet [13], COCO 
[14], and Open Images [15]. Furthermore, in previous studies on defect 
detection, data were collected and manually labeled to build learning 
datasets [16–18]. These tasks are labor intensive and time consuming 
[19,20]. 


Recently, camera-equipped unmanned aerial vehicles (UAV) are 
being increasingly used for periodical structural inspections [21,22]. 
High-definition image data can be efficiently collected using UAV sys­
tems [23]. Despite these advantages, various problems exist regarding 
the collection of high-quality image data using UAVs. First, the images 
are highly dependent on external conditions, such as the time of the day 
and weather conditions, as residential building façades are exposed to 
the natural environment. Second, the images may be blurred because of 


* Corresponding authors. 
E-mail addresses: mir0903@hanyang.ac.kr (S. Lee), hayoung.kim@yonsei.ac.kr (H.Y. Kim).  


Contents lists available at ScienceDirect 


Automation in Construction 


journal homepage: www.elsevier.com/locate/autcon 


https://doi.org/10.1016/j.autcon.2022.104138 
Received 20 July 2021; Received in revised form 4 December 2021; Accepted 6 January 2022   


Automation in Construction 135 (2022) 104138


2


the UAV vibrations. Third, the same object can exhibit different sizes 
and shapes depending on the altitude and location of the UAV. More­
over, the number of objects in different defect classes is not constant in 
the obtained images. This imbalance in class distribution increases the 
difficulty associated with the effective training of a defect detection 
model. Improvement of the model performance requires a balanced and 
large-sized dataset with a class distribution containing multiple damage 
patterns with label information [19]. Since multi-class objects are 
included in an image, creating a balanced dataset using traditional data 
augmentation is difficult. Owing to the abovementioned limitations, an 
effective object-level data augmentation method is required to over­
come the data imbalance problem. 


Herein, we propose a novel bounding-box object augmentation 
(BoxAug) method to improve the performance of deep learning models 
in detecting various defects in residential building façades. The BoxAug 
method augments the number of defect objects in the images, instead of 
augmenting the images. The method yields a large-size defect training 
dataset and solves the data imbalance problem. To evaluate the BoxAug 
method effectiveness, a dataset comprising UAV-obtained residential 
building façade images was generated for four defect classes: delami­
nation, cracking, peeling, and leakage. The experimental results 
revealed that the BoxAug method improves the performance of a DCNN- 
based defect detection model. 


2. Literature review 


2.1. Importance of the defect detection in residential building façades 


Defects in residential buildings directly affect the quality of life of 
residents, and they also cause disputes between contractors and resi­
dents. Thus, various defects occurring in residential buildings cause the 
wastage of various resources, which are additionally inputted, and 
economic losses. Moreover, these defects cause time, material, and 
mental damage to residents and financial loss and degraded credibility 
to businesses. Numerous countries have recognized the issues stemming 
from the risks of defects in residential buildings, thus facilitating various 
researches for resolving these issues. Chong et al. [24] identified the 
essential design strategies and failure causes that could help prevent 
latent defects stemming from poor design decisions in Singapore. Mill 
et al. [25] discussed the nature of the most important defects and 
investigated the impact of contractor and building types in Australia. 
Forcada et al. [26] examined the nature of defects at the post-handover 
stage for seven major residential developments constructed in Spain by 
identifying their types, elemental characteristics, and the subcontract 
trade. Rotimi et al. [27] investigated a list of common defects and pro­
vided insight into the extent of defects observed by new homeowners 
during handover in New Zealand. Hopkin et al. [28] aimed to better 
understand how housing associations, in practice, learn from past de­
fects to reduce the prevalence of defects in future new homes in the UK. 


Particularly, some previous studies have categorized residential 
buildings defects in detail and have further analyzed the relative 
importance of each defect in terms of frequency and cost. Chong et al. 
[29] examined the differences among the building defects occurring 
during the construction and occupancy stages to explore better ways to 
prevent them. Macarulla et al. [30] presented the development and 
validation of a defect classification system for the Spanish housing 
sector. Forcada et al. [31] classified defects observed by four Spanish 
builders and seven residential developments based on their source and 
origin. Lee et al. [32] constructed a defect classification framework 
based on the defect type, work type, and defect location, and they then 
analyzed the defect risk profile. These results show that various defects 
occur on residential building façades with high frequency. Thus, resi­
dential building façades need to be intensively managed at the main­
tenance stage, depending on the importance of the functional role of the 
residential building façade and the level of occurrence for defects. 


2.2. Deep-learning-based defect detection model 


Deep learning can effectively handle computer vision tasks [7]. 
Hence, several studies have been conducted to detect various types of 
defects in structures using deep learning models with high image 
recognition performances. The quality of the training dataset is critical 
to the performance of a defect detection model. However, most previous 
studies focused on developing architectures for crack detection models 
[7,10,33,34]. This is because cracks are the most typical types of defects 
that indicate a decrease in the structural performance and require 
intensive management. Liu et al. [7] employed a U-Net structure to 
develop a deep learning model for crack detection. Cha et al. [10] 
developed a crack detection model with low influence of noise caused by 
lighting, shadow casting, and blurring to ensure extensive adaptability. 
Zhang et al. [33] proposed an efficient network architecture based on a 
convolutional neural network (CNN) for pavement crack detection on 
three-dimensional (3D) asphalt surfaces and fully considered pixel- 
perfect accuracy. Zhang et al. [34] described a systematic approach to 
training a recurrent neural network (RNN), referred to as CrackNet-R, to 
detect pavement cracks on 3D asphalt surfaces with explicit re­
quirements for pixel-perfect accuracy. 


However, in the abovementioned studies, training datasets were 
developed for only a single class of defects. Owing to the various types of 
structural defects, a multi-class defect detection model is required for 
practical structural monitoring applications. Hence, several studies were 
conducted on the multiple types of defects in images [6,17,35–37]. Li 
et al. [6] proposed a multiple defect detection method for concrete 
structures based on a fully convolutional network to detect multiple 
defects at the pixel level. Cha et al. [17] proposed the faster region-based 
CNN (Faster R-CNN)-based structural visual inspection method for the 
quasi real-time simultaneous detection of multiple types of defects. Li 
et al. [35] presented a unified and purely vision-based method, denoted 
as a defect detection and localization network, to detect and classify 
various types of defects under severe conditions while simultaneously 
geolocating the defects without necessitating external localization sen­
sors. Guo et al. [36] proposed a meta-learning-based CNN model to 
automatically identify façade defects in an imbalanced dataset. Miao 
et al. [37] developed a novel approach based on computer vision tech­
niques for the pixel-level multi-category detection of visible seismic 
defects in resistor–capacitor components. However, they did not provide 
alternative methods to fundamentally solve the problem of an imbal­
anced dataset. Specifically, although image data were manually ob­
tained from the residential building façades or using UAVs; the defects 
were randomly distributed in the images. Particularly, the frequently 
occurring defects, such as cracks, are generally abundantly present in all 
objects; this increases the probability of the generation of an imbalanced 
dataset. If the class distribution in the images is imbalanced, the 
detection performance decreases. This is because the unbalanced dataset 
causes biased training for the model to the majority class data. In pre­
vious studies, general data augmentation methods were applied, but 
they were image augmentation methods. Hence, the size of the dataset 
may increase; however, the data imbalance problem still needs to be 
solved. 


2.3. Data augmentation methods for improving the performance of a 
multi-class defect detection model 


Data augmentation techniques are mainly employed to improve the 
performance of deep learning models when limitations arise during data 
collection, which is necessary for training deep learning models. The 
performance of deep learning models is worse than that of machine 
learning models using hand-crafted features when less data are avail­
able; thus, abundant data are required to train the models. A deep 
learning model can be macroscopically considered as a function con­
taining numerous parameters; moreover, to determine the parameter 
weights, a corresponding amount of data is required. Furthermore, deep 


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


3


learning models are mainly trained on a mini-batch basis, and data with 
various forms are present within one mini-batch is beneficial for 
generalized learning. Hence, data augmentation is used to train deep 
learning models for various tasks. 


Research was conducted on data augmentation techniques to 
improve the performance of object detection models [38–43], which are 
computer vision models that generally perform data augmentation by 
transforming the original image. Montserrat et al. [38] performed data 
augmentation by applying linear and nonlinear transformations to 
original images to afford new images. Huang et al. [20] transformed 
original images by applying marine turbulence—a perspective applica­
tion using affine transformations and uneven illumination—to detect 
marine life in an underwater image dataset. Han et al. [39] performed 
data augmentation via the conditional progressive growing of genera­
tive adversarial networks, which were trained to generate synthetic data 
for a brain MRI dataset. The performance of their detection model was 
improved by using it for brain tumor detection. Zhong et al. [40] con­
ducted data augmentation by removing the pixels of an image or a 
random area above a bounding box in images. Cubak et al. [41] estab­
lished an augmentation policy (i.e., the AutoAugment method) and 
determined the optimal method among various augmentation tech­
niques through policy training. To improve the detection performance 
for small objects in images, Kisantal et al. [42] augmented data by 
copying and pasting segmentation masks for small objects. 


The data augmentation methods applied in most of these studies 
transform the original images. However, as mentioned above, the image 
transformation is limited with respect to the solution of the class dis­
tribution problem of an image. Thus, Ghiasi et al. [43] proposed a 
Copy–Paste augmentation using object-level data augmentation for 
instance segmentation and successfully improved the model perfor­
mance. However, their method did not consider the data imbalance 
problem because objects were randomly selected (not consider the class 
distribution) and augmented. In contrast, Bang et al. [19] attempted to 
solve the class distribution problem by augmenting individual objects in 
images using removing-and-inpainting, cut-and-paste, and image- 
variation. However, their method required the generation of segmen­
tation mask data for each object, which is labor intensive and time 
consuming when compared to the bounding-box data generation. 
Therefore, a new data augmentation method for object detection is 
required to efficiently develop balanced datasets. 


3. Methodology 


This study proposes an effective object-level data augmentation 
method, BoxAug, to improve the performance of deep learning models 
for detecting multi-class defects in images of actual residential building 
façades. Various defects can be revealed in the images, but the frequency 
greatly varies depending on the type of defect. The collected data dis­
tribution is similar to the real data distribution, but it is unsuitable for 
training deep learning models for object detection. Therefore, to solve 
the data imbalance problem, this study focused on augmenting the 
number of objects in the image, instead of augmenting the images. To 
solve this problem, BoxAug conducts object-level data augmentation for 
each image of the original training data. Relatively balanced datasets 
can be generated by augmenting objects in original images using the 
BoxAug method. Here, the object-level data augmentation technique 
can be said to be a simple copy–paste method, but an additional trans­
formation process is included based on the characteristics of the objec­
tive task in the paste process. This process can cope with the limitations 
on bounding boxes while solving data imbalance. The detailed BoxAug 
process and its explanation are presented in Section 3.1. 


The construction process of the training dataset that augmented 
objects using the BoxAug method can be described as follows. First, the 
BoxAug method is applied to the original training dataset, wherein the 
data distribution is unbalanced, to generate a balanced training dataset 
by augmenting the objects (Fig. 1(a)). Then, a composition ratio is 
decided to blend the original dataset and balanced training datasets. 
Thereafter, the final training dataset, named BoxAug training dataset, is 
constructed by adding generated training dataset according to the 
selected composition ratio set while preserving the original training 
dataset. The original training dataset is preserved to retain the distri­
bution of real-world data. If only the balanced training dataset gener­
ated by BoxAug is used for model training, the model can be well trained 
for minority class objects. However, the distribution of real-world data 
may be ruined, which will degrade the generalization performance of 
the model. Therefore, the ratio was decided via experiments and the 
BoxAug training dataset constructed in this way is used to train the 
Faster R-CNN model to detect defects in the residential building façade 
images. The BoxAug method proposed, which differs from the tradi­
tional data augmentation method shown in Fig. 1(b), affords the BoxAug 
training dataset during the training process. Thus, as shown in Fig. 1(a), 
object-level data augmentation is performed using the BoxAug method, 
and subsequently, image-level data augmentation is performed via 


(a) Training process applied the BoxAug method.


(b) Training process applied the traditional data augmentation method.


Fig. 1. Comparison of the training processes applied the traditional data augmentation method and the BoxAug method.  


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


4


traditional data augmentation. Data augmentation is typically per­
formed on images whose class distribution is non-uniform, but it is 
performed herein on balanced images. 


3.1. Procedure of the BoxAug method 


Fig. 2 describes the detailed process of applying the BoxAug method 
to an image. To resolve the data imbalance problem, this study estab­
lishes a uniform distribution of the objects in each image of the dataset. 
To obtain a uniform distribution, BoxAug creates an image with a uni­
form distribution by pasting bounding-box images of objects of classes 
that are absent or insufficient in an original image. 


The data imbalance problem interrupts the effective training of an 
object detection model. Moreover, the model is trained by focusing on 
the majority class objects, and the minority class objects are likely to be 
underestimated. Particularly, the imbalance problem becomes more 
severe when the size of a mini-batch, which is a training unit of deep 
learning models, is restricted depending on the hardware performance. 
When the training data are unbalanced and the mini-batch size is small, 
the detection performance of the minority class objects can decrease 


because minority class objects may not be included in the mini-batch. To 
prevent this phenomenon, object-level data augmentation, such as 
BoxAug, is required. 


To apply BoxAug, a dataset of bounding-box images for all objects 
present in the original training dataset primarily needs to be con­
structed. In the process, the bounding-box images of objects in each 
image of the original training dataset are cut and saved. After con­
structing the bounding-box dataset, to identify the number of objects 
subject to augmentation for one image, the distribution of the number of 
objects in that image was examined. When a uniform distribution is 
identified by observation, the BoxAug method is not applied to that 
image. In contrast, if a nonuniform distribution is observed, the number 
of objects that are the most frequent in the image is counted. This 
number is set as the criteria value for augmenting the object. After 
identifying the classes of objects that are less than this criteria value, the 
number of objects of the corresponding class is randomly selected from 
the bounding-box dataset prepared in the previous process using the 
number less than the value. Then, the selected bounding-box image is 
individually transformed. In this case, the number and type of used 
transformation methods are randomly decided. 


Fig. 2. Overview of the development process of the BoxAug method.  


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


5


Here, various transformation methods are applied to the bounding- 
box images due to their characteristics. BoxAug is a method for object 
detection, which differs from other augmentation methods presented in 
previous works [19,44]. Bounding-box annotation is more efficient than 
the segmentation mask annotation for instance segmentation in terms of 
time and cost. However, the bounding-box image contains the back­
ground as well as the object. This means that noise is included in the data 
during the training of a deep learning model for object detection. Due to 
these characteristics, if only a simple transformation method is used, the 
model is more likely to be overfitted to the noise. To overcome this 
shortcoming, BoxAug transforms the bounding box images to be 
attached using various transformation methods. In this study, the 
following transformation methods are employed: “resize,” “random 
crop,” “add random noise,” “horizontal flip,” “vertical flip,” and “add 
morphological transformation mask.” These settings are described in 
detail in Section 3.2. 


The bounding-box image transformed using various transformation 
methods is attached to a random location inside the original image. 
When attaching a transformed bounding-box image, if the image over­
laps with an existing or pasted object, the augmented objects could 
damage the information on other objects. Thus, a “location check” 
process was added to prevent overlapping between bounding-box 
patches. If overlapping occurred with other objects when the trans­
formed bounding-box image was attached to a randomly set position, we 
repeated the process by selecting the bounding-box image from the 
bounding-box dataset. This is because the overlapping is mostly caused 
by the rescaling of the transformation methods. Furthermore, since the 


process of reselection the bounding-box image was randomly per­
formed, there was no difference from the previous selecting process. 
Thus, if the overlapping was perceived from the “location check” pro­
cess, the process of selecting the bounding box image was repeated. 


The above object-level data augmentation process proceeded until 
the number of objects of all classes in an image became equal to the 
previously set criteria value. This enables the creation of an image with 
augmented objects, and the distribution of objects in this image becomes 
uniform. A balanced training dataset is constructed by images generated 
by the BoxAug method. 


The flowchart of the BoxAug method is described step-by-step in 
Fig. 3. Fig. 3 presents the process after the extraction of the bounding- 
box images for objects of every defect class in the original training 
dataset. Fig. 4 shows examples of the images that are generated using the 
BoxAug method.  


(1) STEP 1: Image I of the original training dataset is randomly 


selected, and the number of objects in Image I is recorded for each 
class. Based on this information, the number of objects for each 
class, which is required to achieve a uniform distribution of the 
number of objects by class in Image I, is determined. Particularly, 
the number of objects in Image I is identified for each class, and 
the number of objects of the class with the largest number of 
objects is set as the maximum.  
(2) STEP 2: Then, whether the number of objects for each class in 


Image I is equal to the maximum set in STEP 1 is determined. If 
the condition that the number of objects of each class is equal to 


Fig. 3. Flowchart of the application of the BoxAug method to an image.  


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


6


the maximum is satisfied, the augmentation of the bounding box 
of the corresponding class is not performed. If the condition is not 
satisfied, bounding-box images extracted from the original 
training dataset equal to the number of objects lacking in the 
classes with insufficient objects are randomly selected and 
transformed.  
(3) STEP 3: The location in Image I is randomly selected, and the 


bounding-box image transformed in STEP 2 is pasted to the 
selected location. Here, the transformed bounding-box image 
may overlap with the bounding box of another object. In this 
case, we again proceed from the process of randomly selecting the 
bounding box of STEP 2 so that information is not lost by over­
lapping. Through this process, the bounding-box images of the 
classes with insufficient objects are augmented, and new images 
with uniform class distribution are generated.  
(4) STEP 4: When the objects of each class in Image I have achieved 


uniformity using steps 1–3, they are separately saved as Image I′. 
This process is applied to every image in the original training 
dataset and a new training dataset with augmented bounding 
boxes is generated. 


3.2. Transformation to reduce overfitting 


As mentioned above, to solve the overfitting problem of the model, 
which can be caused by the inclusion of the background in the bounding 
box, the bounding-box image extracted from the original training 
dataset was transformed herein. 


In the transformation process, six transformation methods were 
employed: “resize,” “random crop,” “add random noise,” “horizontal 
flip,” “vertical flip,” and “add morphological transformation.” Among 
them, “resize” is a fundamental method used for the bounding boxes of 
every selected object. The other five transformation methods were 
randomly selected. For more diverse transformation combinations, the 
number of methods employed was randomly selected, and the selection 


of the methods, according to the set number of methods, was randomly 
determined. Fig. 5 presents a flowchart of the transformation process. As 
shown in Fig. 5, the transformation method receives one bounding-box 
image as the input. First, as mentioned above, the image is resized, and 
then, the number of methods applied among the other five trans­
formation methods is randomly set (a value of 0–5). Thereafter, trans­
formation methods equal to the number of methods set in the previous 
step are randomly selected in the candidate set. Each selected method is 
applied to the bounding-box image. The box image to which various 
transformations are applied is outputted. This transformed bounding- 
box image is copied to the target image of the augmentation. 


3.2.1. Transformation method: Resize, random crop, and horizontal and 
vertical flip 


Note that “resize,” “random crop,” and “flips” in the candidate set of 
transformation methods are representative image data augmentation 
methods in computer vision. “Resize” is an augmentation method for 
representing objects of various sizes, and the detection models can be 
trained to detect objects of various sizes. Herein, constant size thresholds 
(for the width and height) are set, and the “resize” method is employed 
based on the threshold. The threshold was set as 25% of the width and 
height of the full image size. If the width and height of the selected 
bounding box were smaller than the thresholds, the upscale method was 
applied to the bounding box; otherwise, the downscaling method was 
applied. To prevent the elimination of all the information in the 
bounding box, the upscale ratio was randomly set between 0 and 1 and 
the downscale ratio was randomly set between 0 and 1/2. 


“Horizontal and vertical flip” is a simple method to horizontally and 
vertically reverse the bounding-box image. This method can be applied 
using a simple function in the OpenCV package, and the box image 
transformed by these methods can be represented in various directions. 
Therefore, in computer vision tasks, this method is utilized to enable the 
extraction of various features from images using CNN-based models. 


The “random crop” method is used to crop the bounding boxes of 


Fig. 4. Examples of the images generated using the BoxAug method.  


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


7


objects, and the cropping rule for the method varies. The cropping rule 
used herein comprises the cropping of the bounding box using a 
randomly preset “cropping point” within a given range. Subsequently, 
horizontal and vertical lines were superimposed onto the box image 
based on the set “cropping point,” and the image was cropped based on 
the lines. This newly generated bounding box was not restored to its 
original size owing to the size diversity. Herein, the “given range” was 
set to the upper left corner of the bounding box, within 10% of the 
width, and with the height of the original bounding box. Moreover, 10% 
range is a hyperparameter that can be adjusted in the experiment. 
Herein, 10% is employed to prevent a significant information loss within 
the bounding box. Fig. 6 describes the procedure for applying a random 
crop transformation to the bounding box of an object. 


3.2.2. Transformation methods: add random noise 
Adding noise to data is a data augmentation method that is mainly 
employed in image-related tasks using a deep learning model. Moreover, 


“add random noise” is used to increase the generalization performance 
of a model and the data required for model training. Herein, noise was 
added to the bounding box extracted from original images to perform 
tasks for the bounding boxes of objects in the images. Moreover, four 
types of noises were set (Gaussian, Poisson, Salt and Pepper (S&P), and 
Speckle) as candidates. One of these types was randomly selected and 
applied to the original bounding-box. Only one type was randomly 
selected because the selection of multiple types of noises excessively 
increases the severity of the resulting noise, which consequently in­
creases the probability of eliminating information from the original 
image. Fig. 7 presents examples of the original objects and the result of 
adding each noise. 


Fig. 5. Flowchart of the application of the transformation function to a 
bounding-box image of the object. 


Fig. 6. Process of the random crop method (the red box is the predefined 
range). (For interpretation of the references to colour in this figure legend, the 
reader is referred to the web version of this article.) 


Fig. 7. Image with different noises added (top: an original bounding- 
box image). 


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


8


3.2.3. Transformation methods: add morphological transformation 
Fig. 8 presents the overall process of generating a new object image 
using the “add morphological transformation” method, which is a new 
transformation method proposed herein. In this method, a trans­
formation is applied by calculating the weighted average of the original 
image after generating a mask image that highlights the edge through 
the morphological transformation of the original box image. The mask 
that highlights the edge was fabricated using the morphological trans­
formation equation from the OpenCV package in Python. This trans­
formation result was merged with the original image to emphasize the 
defect edge in the original box image. Additional information on the 
defect can be obtained by emphasizing the defect edge, and a more 
generalized shape of the defect can be learned through transformation. 
Several alternative methods exist for morphological transformation that 
highlight the edge of an object in an image (e.g., using the Sobel and 
Canny edge detectors). The novel transformation method was employed 
herein as it afforded the largest amount of information compared to the 
other methods while highlighting the object edges. 


To generate a mask image that emphasizes the edge using the 
morphological transformation method, various detailed items need to be 
determined, such as the thresholding method, selected kernel, and 
detailed method to use in the transformation (“Dilation,” “Erosion,” 
“Opening,” and “Closing”). No general method exists for the optimal 
selection of these items. Therefore, herein, examples of masks were 
identified, a mask that most effectively highlighted the edge of the ob­
ject in the box was selected, and a hyperparameter that indicated this 
mask was determined. Subsequently, the mask was generated, and the 
weight average of the original image was calculated for each pixel and a 
new object image was generated. The weighted average ratio was 
determined as a random ratio, and to preserve the information about the 
defects inside the original box image, the weight of the original box 
image was set to be larger than that of the generated mask image. 
Furthermore, the bounding boxes of other objects were transformed 
using the hyperparameter that generated the optimal mask. 


4. Results 


4.1. Dataset 


The image dataset of an actual residential building façade is used 
here. Each image comprised a minimum of one defect, and the infor­
mation comprised the vertex coordinates of the bounding box and defect 
type. This dataset was collected using an imaging device mounted on a 
UAV, and the resolution of the images was 4,032 × 1,960. The 
computation cost of images of this size is significantly large, which will 
increase the number of training data and the inference time of the 


model. Thus, in this study, the training data were resized to a resolution 
of 800 × 600. Totally, 10,907 images were used in the experiment, and 
the types and numbers of defects inside the images are listed in Table 1. 
Four types of defects were selected for detection in the residential 
building façades: delamination, crack, peeling, and leakage. Addition­
ally, for generalized training, the entire dataset was divided into 
training, validation, and test datasets. The training dataset was used to 
train the model, the validation dataset was used to determine the 
generalized learning performance of the model, and the test dataset was 
used to evaluate the performance of the trained model. 


4.2. Detection model for validating the BoxAug method: faster R-CNN 


Faster R-CNN [44] is mainly used in object detection tasks. It is a 
typical two-stage structure model that demonstrates excellent detection 
speed and performance after its initial release. To verify the BoxAug 
method, Faster R-CNN was used. 


The architecture of Faster R-CNN is shown in Fig. 9. First, the feature 
map of an image was extracted using a backbone network comprising a 
DCNN. The extracted feature map of the image was inputted into a re­
gion proposal network (RPN), which is a core network of Faster R-CNN. 
The RPN extracted the region of interest (RoI). The extracted RoI was 
aligned with the previously extracted feature map and then passed 
through a region convolutional network, followed by the box regression 
layer and box classification layer, which are sibling layers, to detect 
objects within the image. Finally, the entire model was trained and the 
loss was calculated using these two sibling layers. 


4.3. Performance metric: average precision 


The average precision (AP) metric used herein measured the detec­
tion performance for the MS COCO dataset [14], which is the repre­
sentative dataset of the object detection task. To calculate AP, the 
intersection over union (IoU) of the bounding box predicted by the 


Fig. 8. Process of applying the “add morphological transformation” method to a bounding box of an object.  


Table 1 
Distribution of the datasets.  


Category 
Training 
Validation 
Test 


Images  
7635 
1091 
2181 
Class 
Delamination 
5108 
639 
1395 
Crack 
5620 
833 
1714 
Peeling 
1207 
165 
343 
Leakage 
181 
38 
47 
Total 
12,116 
1675 
3499  


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


9


model and the ground-truth box needs to be determined. The IoU was 
calculated by dividing the intersection area of the two boxes by the area 
of union of the two boxes. 


AP is dependent on the IoU threshold because the status of the image 
predictions is determined by the IoU threshold. Owing to this charac­
teristic in the object detection task, AP can be calculated according to 
the IoU threshold and class of prediction. We set AP50 as a metric, which 
uses 50% of the IoU threshold. 


4.4. Evaluation of the BoxAug method 


In this study, various training datasets were configured using the 
BoxAug method, and the BoxAug method was evaluated by analyzing 
the performance of the Faster R-CNN model trained using this training 
dataset. The learning rate and mini-batch size, which are hyper­
parameters used in the training process of Faster R-CNN, were set as 
0.001 and 8, respectively. 
Before verifying the performance improvement of the BoxAug 
method, the ratio of the original training dataset to the balanced training 
dataset was determined to construct the BoxAug training dataset. The 
amount of data that can be newly generated by the BoxAug method is 
infinite. However, if transformed data are excessively used in model 
training instead of original data, the generalization performance of the 
original data could deteriorate. Thus, the balanced training dataset 
created using the BoxAug method should be properly blended with the 
original training dataset. 


To determine the composition ratio between the original and 
balanced training datasets, experiments were conducted on the BoxAug 
training datasets configured at ratios of 1:1, 2:1, 3:1, 4:1, and 5:1 


between the original and balanced training datasets. Fig. 10 presents 
AP50 for the validation dataset of the Faster R-CNN model trained using 
the BoxAug training datasets at each ratio as well as the original training 
dataset. The validation dataset was used to verify the model perfor­
mance because it determines the hyperparameters required for the 
BoxAug method before the verification of the learning performance of 
the final model. Furthermore, since the background of the image whose 
objects have been augmented using BoxAug matches that of the original 
image, the BoxAug method exhibits various limitations in augmenting 
image samples compared to the traditional data augmentation method. 
When a deep learning model is trained using a small volume of data, the 
overfitting of the model on the corresponding data degrades its gener­
alization performance. Therefore, traditional data augmentation 
methods that can sufficiently augment data should be concurrently 
utilized with BoxAug to prevent model overfitting and achieve the 
intended performance. Thus, the model was trained using both 
augmentation methods in all subsequent experiments, including the 
experiment shown in Fig. 10. 


Fig. 10 shows that the performance of the model trained using the 
BoxAug training dataset was higher than that of the model trained using 
the original training dataset. Especially, the AP50 metric of the model 
trained using the BoxAug training dataset composed at a ratio of 3:1 
exhibited the highest performance at 61.01%. Therefore, the composi­
tion ratio of the training dataset is an important parameter that in­
fluences the model performance as the model trained using the dataset 
composed at a ratio of 3:1 exhibited better performance than that 
trained using the dataset composed at a ratio of 1:1. 


Table 2 shows the distribution of the BoxAug training dataset 
composed at a ratio of 3:1. Compared to that of the original training 


Fig. 9. Architecture of the Faster R-CNN.  


Fig. 10. AP50 for the validation dataset according to the training dataset composition ratio.  


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


10


dataset, the data balance of the dataset composed at a ratio of 3:1 
obviously improved. 


Thereafter, the performance of the Faster R-CNN model was evalu­
ated according to the number of techniques applied for transformation. 
Three candidate sets were defined: {resize}, {resize, horizontal flip, and 
vertical flip}, and {resize, horizontal flip, vertical flip, random crop, add 
random noise, and add morphology}. Fig. 11 presents a comparison of 
the performances of the Faster R-CNN model trained using the different 
BoxAug training datasets. The Faster R-CNN model trained with the 
BoxAug training dataset generated using each candidate set in the 
BoxAug method is named as BoxAug-1, BoxAug-2, and BoxAug-3, 
respectively. As shown in Fig. 11, the AP50 metric of the model was 
optimal at 61.01% with BoxAug-3. This suggests that the model per­
formance considerably improves when various transformation methods 
are applied. 


Table 3 presents the performance evaluation results of the Faster R- 
CNN model trained using the BoxAug training dataset with the optimal 
composition ratio and transformation set based on the experimental 
results. It describes the comparisons of the data distribution and per­
formance of the models with and without BoxAug. As shown in the table, 
when the models trained with and without BoxAug were applied to the 
test dataset, the mean AP50 values of all the classes were 60.83% and 
63.53%, respectively. Thus, the results of the performance of the 


detection model for each class show that the overall detection perfor­
mance improved. The AP50 for delamination (Class 1), crack (Class 2), 
and peeling (Class 3) increased from 52.84% to 53.83%, 73.8% to 
74.75%, and 54.57% to 55.8%, respectively. Especially, the AP50 for 
leakage (Class 4) considerably increased from 62.1% to 69.73%. In 
addition, the BoxAug training data distribution indicated less data 
imbalance than the original training data distribution. Consequently, 
the minority classes (classes 3 and 4) exhibit relatively more improved 
detection performances than other classes. Despite the lowest ratio 
included in the original training dataset at 1.5%, leakage (Class 4) was 
significantly augmented in the BoxAug training dataset, accounting for 
13.8% of the entirety. This suggests that data imbalance can be reduced 
using BoxAug and the model performance can be subsequently 
improved. 


5. Discussion 


This study proposed a new data augmentation method to formulate 
an efficient well-balanced dataset targeting multiple defects that are 
present on residential building façades. 


When the training dataset constructed with the proposed BoxAug is 
utilized, the model performance for all classes improves (Fig. 12). 
Particularly, class 4, which is a minority class, exhibited the highest 
performance improvement, suggesting the possibility of BoxAug as a 
technical solution for resolving the imbalanced dataset problem. Addi­
tionally, as suggested in previous studies, the simultaneous detection of 
various types of defects in residential building façades is crucial for 
defect management from two viewpoints. First, the various defects 
appearing on residential building façades are in a complex relationship 
with each other. Thus, since the minority classes also have a close 
relationship with the durability performance of the structure and the 
living environment of residents, they need to be detected [36]. Second, 
the criterion that distinguishes majority and minority classes is the 
frequency of detected defects. Thus, from the perspective of defect 


Table 2 
Comparison of the data distributions.  


Category 
Original training 
dataset 


BoxAug training 
dataset 


Images  
7635 
10019 
Objects 
Delamination (Class 
1) 
5108 
8899 


Crack (Class 2) 
5620 
9278 
Peeling (Class 3) 
1207 
4565 
Leakage (Class 4) 
181 
3652 
Total 
12116 
26394  


Fig. 11. Performance comparison of the original training dataset and different BoxAug training datasets.  


Table 3 
Comparisons of the data distribution and performance of the models with and without BoxAug. (The model without BoxAug indicates the model with the basic training 
framework.)  


Category 
Original 
dataset 
Distribution (%) 


BoxAug  
dataset 
Distribution (%) 


Model w/o  
BoxAug (AP50) 


Model w/ 
BoxAug (AP50) 


Performance Improvement (points) 
Performance Improvement (%) 


Class 1 
42.2% 
33.7% 
52.84 
53.83 
0.99 
1.87 
Class 2 
46.4% 
35.2% 
73.80 
74.75 
0.95 
1.29 
Class 3 
10.0% 
17.3% 
54.57 
55.80 
1.23 
2.25 
Class 4 
1.5% 
13.8% 
62.10 
69.73 
7.63 
12.29 
Mean   
60.83 
63.53 
2.70 
4.44  


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


11


management, the criteria for the priority of defects include severity as 
well as frequency [32]. Thus, if defects corresponding to minority 
classes are ignored, various problems may occur from the perspective of 
defect management. Hence, since the imbalanced dataset problem 
regarding the residential building façades must be resolved, data 
augmentation methods, such as BoxAug, are vital. 


Table 4 shows the comparison results between the proposed BoxAug 
method and the Copy–Paste method. First, the proposed BoxAug is a 
method for object detection, whereas Copy–Paste augmentation is a 
method for instance segmentation. These target task differences cause 
differences in the annotation types in both methods. Thus, BoxAug re­
quires only bounding-box annotation, but Copy-Paste augmentation 
demands segmentation mask annotation. Although segmentation has a 
technical advantage, it is labor intensive and time consuming. 
Furthermore, defects have various shapes with several vague bound­
aries between the object and background. Owing to the unique char­
acteristics of the defects, it is difficult to create segmentation masks for 
instance segmentation. Second, due to differences in annotation types, 
we applied more various transformations to augmented objects using 
BoxAug. This is because both the background and the objects are 
included in the bounding-box images. If a few transformation methods, 
such as Copy–Paste augmentation, are utilized to apply BoxAug, various 
transformation methods are required as the model is highly likely to be 
overfitted to the background in the bounding box. Third, in contrast to 
the random augmentation of objects in the Copy–Paste augmentation, 
BoxAug mainly augments objects of minority classes to resolve the data 
imbalance problem. 


As aforementioned, the performance of the detection model for the 
minority class greatly improved when the data imbalance was reduced 
using BoxAug. In contrast, the performance of the detection model for 
the majority class slightly increased. Nevertheless, these results have 
valuable implications. This is because increasing AP50 by 1% or more 
by developing an algorithm-level method is considerably challenging. 
In fact, although the performance evaluation of various object detection 
models is being conducted by targeting the MS COCO dataset, the dif­
ference in AP50 between ranks is insignificant. Therefore, an AP50 in­
crease of approximately 2.7% using a data-level method like the 
proposed BoxAug method is highly meaningful. 


Especially, the defects in the residential building façade were more 
diverse than those in the infrastructure, and several defects exhibited 
similar shapes or were difficult to distinguish. Consequently, the 
development of a well-distributed training dataset with respect to the 
defect class is difficult for implementing a multi-class defect detection 
model. Moreover, using an image dataset with a uniform class distri­
bution can guarantee the high performance of a DCNN model; however, 
it is difficult to develop such an image dataset. The BoxAug method is an 
alternative method that can overcome these practical barriers and 
effectively augment the real-world image dataset. 


However, the model performance was generally low. A typical 
method for solving this problem is to optimize the detection model or 
obtain a large original image dataset. Moreover, the proposed BoxAug 
method requires improvement. The problem associated with the 
method that sets the location of the bounding box pasted in the new 
image is as follows. Herein, the location of a newly pasted bounding box 
was randomly determined. Consequently, the bounding boxes of 
various classes could be pasted at nonexistent locations. For example, 
the bounding box of a crack could be located in the trees and roads 
included in the original image. Although the BoxAug dataset underwent 
the transformation process, it was insufficient to overcome the over­
fitting problem because of the difference in the completely heteroge­
neous background. Furthermore, the dataset used herein did not reflect 
the patterns of all variables (e.g., time of day, weather, shadows, and 
distance). Therefore, the effectiveness of BoxAug can be improved by 
including additional original image datasets reflecting different 
parameters. 


Table 4 


Differences between the BoxAug and Copy–Paste methods.  


Category 
Method 


BoxAug 
Copy–Paste 


Objective Task 
Object Detection 
Instance Segmentation 


The form of the object that copy and paste 
Bounding box 
Segmentation mask 


The number of applied transformation 


methods for objects 
6 
2 


Considering data imbalance 
O 
X 


Pros. 
Since it can be applied with bounding-box annotation alone, the time and costs for 


constructing a dataset can be reduced. 
The augmented object does not contain a background, so there is less noise in the augmented images. 


Cons. 
A bounding-box image includes both a background and an object, which may interfere 


with model learning. 
To apply this method, it takes a considerable amount of time and money to construct the dataset because 


segmentation mask annotation is required.  


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


12


6. Conclusions 


This study proposes a novel augmentation method (BoxAug) to 
improve the performance of a multi-class defect detection model for 
residential building façade images obtained using a UAV. The BoxAug 
method yields a new image by pasting the bounding boxes of objects 
with insufficient classes on another specific image in the training dataset 
when the number of bounding boxes of objects in a specific image is not 
uniform for each class. 


The validity of the BoxAug method was verified by comparing it with 
the Faster R-CNN method, which is typically used as an object detection 
model. In this study, 10,907 original images obtained using UAVs were 
randomly classified into training, validation, and test datasets at a ratio 
of 7:1:2. The number of objects observed by class in the training dataset 
was 5108 for delamination, 5620 for cracking, 1207 for peeling, and 181 
for leakage. 10,019 training images were augmented by applying the 
composition ratio of 3:1 between the original dataset and BoxAug 
dataset, which was derived by applying the candidate transformation 
set. The number of objects by class was 8899 for delamination, 9278 for 
cracking, 4565 for peeling, and 3652 for leakage. The performance 
evaluation of the Faster R-CNN model trained using the generated 
training dataset demonstrated that the model trained using the BoxAug 
method exhibits better performance than the model trained using the 
original dataset. Especially, the class that obtained the smallest number 
of objects in the original dataset demonstrated a significant improve­
ment in the learning performance. 


The proposed BoxAug method can contribute to the realization of a 
practical alternative method that can effectively augment an original 
image dataset with an uneven class distribution. BoxAug can be utilized 
to construct a well-balanced large-sized dataset by overcoming realistic 
barriers, such as the resident privacy issues of residential buildings, 
difficulty in recognizing defects, and imbalanced dataset. Moreover, the 
proposed BoxAug method exhibits good practical applicability as it 
utilizes bounding-box rather than segmentation, which requires signif­
icant time and manpower. Accordingly, the proposed method can serve 
as a benchmark for real-world image data augmentation research on 
various defects present on residential building façades. 


The BoxAug method not only improved the detection performance of 
the model in every class but also significantly improved the detection 
performance of classes with insufficient training datasets. However, the 
overall detection performance is not sufficiently reliable for practical 
applications. This is because of the heterogeneity of the background 
generated by the nonexistent location of the bounding box. Thus, a study 
that reflects the background of the original image in the background of 
the bounding box needs to be conducted using the recently developed 
generative adversarial network. Furthermore, since various parameters 
such as weather, shadow, and distance influence the detection perfor­
mance, an original image dataset that reflects these parameters needs to 
be considered. 


Declaration of Competing Interest 


The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 


Acknowledgments 


This research was supported by a grant (21CTAP-C163951-01) from 
Technology Advancement Research Program (TARP) funded by the 
Ministry of Land, Infrastructure and Transport of Korean government. 


References 


[1] I. Flores-Colen, J. de Brito, Discussion of proactive maintenance strategies in 


façades’ coatings of social housing, J. Build. Apprais. 5 (2010) 223–240, https:// 
doi.org/10.1057/jba.2009.2. 
[2] J.S. Lee, Value engineering for defect prevention on building façade, J. Constr. Eng. 


Manag. 144 (8) (2018) 4018069, https://doi.org/10.1061/(ASCE)CO.1943- 
7862.0001500. 
[3] H. Perez, J.H.M. Tah, A. Mosavi, Deep learning for detecting building defects using 


convolutional neural networks, Sensors. 19 (16) (2019) 3556, https://doi.org/ 
10.3390/s19163556. 
[4] C.V. Dung, L.D. Anh, Autonomous concrete crack detection using deep fully 


convolutional neural network, Autom. Constr. 99 (2019) 52–58, https://doi.org/ 
10.1016/j.autcon.2018.11.028. 
[5] B.A. Graybeal, B.M. Phares, D.D. Rolander, M. Moore, G. Washer, Visual inspection 


of highway bridge, J. Nondestruct. Eval. 21 (3) (2002) 67–83, https://doi.org/ 
10.1023/A:1022508121821. 
[6] S. Li, X. Zhao, G. Zhou, Automatic pixel-level multiple damage detection of 


concrete structure using fully convolutional network, Computer-Aided Civil and 
Infrastruct. Eng. 34 (7) (2019) 616–634, https://doi.org/10.1111/mice.12433. 
[7] Z. Liu, Y. Cao, Y. Wang, W. Wang, Computer vision-based concrete crack detection 


using U-net fully convolutional networks, Autom. Constr. 104 (2019) 129–139, 
https://doi.org/10.1016/j.autcon.2019.04.005. 
[8] Q. Yang, W. Shi, J. Chen, W. Lin, Deep convolution neural network-based transfer 


learning method for civil infrastructure crack detection, Autom. Constr. 116 
(2020), 103199, https://doi.org/10.1016/j.autcon.2020.103199. 
[9] W. Rawat, Z. Wang, Deep convolutional neural networks for image classification: a 


comprehensive review, Neural Comput. 29 (9) (2017) 2352–2449, https://doi.org/ 
10.1162/neco_a_00990. 
[10] Y.J. Cha, W. Choi, O. Buyukozturk, Deep learning-based crack damage detection 


using convolutional neural networks, Computer-Aided Civil and Infrastruct. Eng. 
32 (5) (2017) 361–378, https://doi.org/10.1111/mice.12263. 
[11] Y.Z. Lin, Z.H. Nie, H.W. Ma, Structural damage detection with automatic feature- 


extraction through deep learning, Computer-Aided Civil and Infrastruct. Eng. 32 
(12) (2017) 1025–1046, https://doi.org/10.1111/mice.12313. 
[12] S.I. Hassan, L.M. Dang, I. Mehmood, S. Im, C. Choi, J. Kang, Y.S. Park, H. Moon, 


Underground sewer pipe condition assessment based on convolutional neural 
networks, Autom. Constr. 106 (2019), 102849, https://doi.org/10.1016/j. 
autcon.2019.102849. 
[13] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh, S. Ma, Z. Huang, 


A. Karpathy, A. Khosia, M. Bernstein, A.C. Berg, L. Fei-Fei, ImageNet large scale 
visual recognition challenge, Int. J. Comput. Vis. 115 (3) (2015) 211–252, https:// 
doi.org/10.1007/s11263-015-0816-y. 
[14] T.Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Doll´ar, C. 


L. Zitnick, C.O.C.O. Microsoft, Common objects in context, in: Proceedings of the 
2014 European Conference on Computer Vision (ECCV), Zurich, CH, 2014, 
pp. 740–755, https://doi.org/10.1007/978-3-319-10602-1_48. 
[15] A. Kuznetsova, H. Rom, N. Alldrin, J. Uijings, I. Krasin, J. Pont-Tuset, S. Kamali, 


S. Popov, M. Malloci, A. Kolesnikov, T. Duerig, V. Ferrari, The Open Images Dataset 
V4: Unified image classification, object detection, and visual relationship detection 
at scale, arXiv preprint (2018), https://doi.org/10.1007/s11263-020-01316-z 
arXiv:1811.00982. 
[16] X. Yang, H. Li, Y. Yu, X. Luo, T. Huang, X. Yang, Automatic pixel-level crack 


detection and measurement using fully convolutional network, Computer-Aided 
Civil and Infrastruct. Eng. 33 (12) (2018) 1090–1109, https://doi.org/10.1111/ 
mice.12412. 
[17] Y.J. Cha, W. Choi, G. Suh, S. Mahmoudkhani, O. Buyukozturk, Autonomous 


structural visual inspection using region-based deep learning for detecting multiple 
damage types, Computer-Aided Civil and Infrastruct. Eng. 33 (9) (2018) 731–747, 
https://doi.org/10.1111/mice.12334. 
[18] Y. Gao, K.M. Mosalam, Deep transfer learning for image-based structural damage 


recognition, Computer-Aided Civil and Infrastruct. Eng. 33 (9) (2018) 748–768, 
https://doi.org/10.1111/mice.12363. 
[19] S. Bang, F. Baek, S. Park, W. Kim, H. Kim, Image augmentation to improve 


construction resource detection using generative adversarial networks, cut-and- 
paste, and image transformation techniques, Autom. Constr. 115 (2020), 103198, 
https://doi.org/10.1016/j.autcon.2020.103198. 
[20] H. Huang, H. Zhou, X. Yang, L. Zhang, L. Qi, A.Y. Zang, Faster R-CNN for marine 


organisms detection and recognition using data augmentation, Neurocomputing. 
337 (2019) 372–384, https://doi.org/10.1016/j.neucom.2019.01.084. 
[21] C. Eschmann, C.-M. Kuo, C.-H. Kuo, C. Boller, Unmanned aircraft systems for 


remote building inspection and monitoring, in: Proceedings of the 6th European 
Workshop Structure Health Monitoring 36, 2012, p. 13. http://www.ecphm2012. 
com/Portals/98/BB/th2b1.pdf (accessed October 3, 2017). 
[22] D. Roca, S. Laguela, L. Díaz-Vilarino, J. Armesto, P. Arias, Low-cost aerial unit for 


outdoor inspection of building façades, Autom. Constr. 36 (2013) 128–135, 
https://doi.org/10.1016/j.autcon.2013.08.020. 
[23] D. Mader, R. Blaskow, P. Westfeld, C. Weller, Potential of UAV-based laser scanner 


and multispectral camera data in building inspection, the international archives of 
the photogrammetry, Remote Sens. Spat. Inf. Sci. 41 (2016) 1135–1142, https:// 
doi.org/10.5194/isprs-archives-XLI-B1-1135-2016. 
[24] W.K. Chong, S.P. Low, Latent building defects: causes and design strategies to 


prevent them, J. Perform. Constr. Facil. 20 (3) (2006) 213–221, https://doi.org/ 
10.1061/(ASCE)0887-3828(2006)20:3(213). 


K. Lee et al.                                                                                                                                                                                                                                      


Automation in Construction 135 (2022) 104138


13


[25] A. Mills, P.E.D. Love, P. Williams, Defect costs in residential construction, J. Constr. 


Eng. Manag. 135 (1) (2009) 12–16, https://doi.org/10.1061/(ASCE)0733-9364 
(2009)135:1(12). 
[26] N. Forcada, M. Macarulla, P.E.D. Love, Assessment of residential defects at post- 


handover, J. Constr. Eng. Manag. 139 (4) (2013) 372–378, https://doi.org/ 
10.1061/(ASCE)CO.1943-7862.0000603. 
[27] F.E. Rotimi, J. Tookey, J.O. Rotimi, Evaluating defect reporting in new residential 


buildings in New Zealand, Buildings. 5 (1) (2015) 39–55, https://doi.org/10.3390/ 
buildings5010039. 
[28] T. Hopkin, S.L. Lu, P. Rogers, M. Sexton, Detecting defects in the UK new-build 


housing sector: a learning perspective, Constr. Manag. Econ. 34 (1) (2016) 35–45, 
https://doi.org/10.1080/01446193.2016.1162316. 
[29] W.K. Chong, S.P. Low, Assessment of defects at construction and occupancy stages, 


J. Perform. Constr. Facil. 19 (4) (2005) 283–289, https://doi.org/10.1061/(ASCE) 
0887-3828(2005)19:4(283). 
[30] M. Macarulla, N. Forcada, M. Casals, M. Gangolells, A. Fuertes, X. Roca, 


Standardizing housing defects: classification, validation, and benefits, J. Constr. 
Eng. Manag. 139 (8) (2013) 968–976, https://doi.org/10.1061/(ASCE)CO.1943- 
7862.0000669. 
[31] N. Forcada, M. Macarulla, M. Gangolells, M. Casals, A. Fuertes, X. Roca, 


Posthandover housing defects: sources and origins, J. Perform. Constr. Facil. 27 (6) 
(2013) 756–762, https://doi.org/10.1061/(ASCE)CF.1943-5509.0000368. 
[32] J. Lee, Y. Ahn, S. Lee, Post-handover defect risk profile of residential buildings 


using loss distribution approach, J. Manag. Eng. 36 (4) (2020) 04020021, https:// 
doi.org/10.1061/(ASCE)ME.1943-5479.0000785. 
[33] A. Zhang, K.C.P. Wang, B. Li, E. Yang, X. Dai, Y. Peng, Y. Fei, Y. Liu, J.Q. Li, 


C. Chen, Automated pixel-level pavement crack detection on 3D asphalt surfaces 
using a deep-learning network, Computer-Aided Civil and Infrastruct. Eng. 32 (10) 
(2017) 805–819, https://doi.org/10.1111/mice.12297. 
[34] A. Zhang, K.C.P. Wang, Y. Fei, Y. Liu, C. Chen, G. Yang, J.Q. Li, E. Yang, Automated 


pixel-level pavement crack detection on 3D asphalt surfaces with a recurrent 
neural network, Computer-Aided Civil and Infrastruct. Eng. 34 (3) (2019) 
213–229, https://doi.org/10.1111/mice.12409. 
[35] R. Li, Y. Yuan, W. Zhang, Y. Yuan, Unified vision-based methodology for 


simultaneous concrete defect detection and Geolocalization, Computer-Aided Civil 


and Infrastruct. Eng. 33 (7) (2018) 527–544, https://doi.org/10.1111/ 
mice.12351. 
[36] J. Guo, Q. Wang, Y. Li, P. Liu, Façade defects classification from imbalanced 


dataset using meta learning-based convolutional neural network, Computer-Aided 
Civil and Infrastruct. Eng. 35 (12) (2020) 1403–1418, https://doi.org/10.1111/ 
mice.12578. 
[37] Z. Miao, X. Ji, T. Okazaki, N. Takahashi, Pixel-level multicategory detection of 


visible seismic damage of reinforced concrete components, Computer-Aided Civil 
and Infrastruct. Eng. 36 (5) (2021) 620–637, https://doi.org/10.1111/ 
mice.12667. 
[38] D.M. Montserrat, Q. Lin, J. Allebach, E.J. Delp, Training object detection and 


recognition CNN models using data augmentation, Electronic Imaging. 2017 (10) 
(2017) 27–36, https://doi.org/10.2352/ISSN.2470-1173.2017.10.IMAWM-163. 
[39] C. Han, K. Murao, T. Noguchi, Y. Kawata, F. Uchiyama, L. Rundo, H. Nakayama, 


S. Satoh, Learning more with less: Conditional PGGAN-based data augmentation 
for brain metastases detection using highly-rough annotation on MR images, in: 
Proceedings of the 28th ACM International Conference on Information and 
Knowledge Management, Beijing, China, 2019, pp. 119–127, https://doi.org/ 
10.1145/3357384.3357890. 
[40] Z. Zhong, L. Zheng, G. Kang, S. Li, Y. Yang, Random erasing data augmentation, in: 


Proceedings of the AAAI Conference on Artificial Intelligence, NY, USA, 2020, 
pp. 13001–13008, https://doi.org/10.1609/aaai.v34i07.7000. 
[41] E.D. Cubuk, B. Zoph, D. Mane, V. Vasudevan, Q.V. Le, Autoaugment: learning 


augmentation strategies from data, in: Proceedings of the IEEE/CVF Conference on 
Computer Vision and Pattern Recognition, IEEE, 2019, pp. 113–123. 
[42] M. Kisantal, Z. Wojna, J. Murawski, J. Naruniec, K. Cho, Augmentation for small 


object detection, in: Proceedings of the CS & IT Conference, Sydney, Australia, 
2019, pp. 119–133, https://doi.org/10.5121/csit.2019.91713. 
[43] G. Ghiasi, Y. Cui, A. Srinivas, R. Qian, T.Y. Lin, E.D. Cubuk, Q.V. Le, B. Zoph, 


Simple copy-paste is a strong data augmentation method for instance 
segmentation, in: Proceedings of the IEEE/CVF Conference on Computer Vision 
and Pattern Recognition, Vancouver, 2021, pp. 2918–2928. 
[44] S. Ren, K. He, R. Girshick, J. Sun, Faster R-CNN: Towards real-time object detection 


with region proposal networks, IEEE Transact. Pattern Anal. Mach. Intell. 39 (6) 
(2015) 1137–1149. 


K. Lee et al.                                                                                                                                                                                                                                      
