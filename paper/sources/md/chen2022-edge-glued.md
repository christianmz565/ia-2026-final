# Edge-glued wooden panel defect detection using deep learning


Wood Science and Technology (2022) 56:477–507

https://doi.org/10.1007/s00226-021-01316-3

ORIGINAL

Edge‑glued wooden panel defect detection using deep

learning

Lun‑Chi Chen, et al. [full author details at the end of the article]

Received: 24 December 2020 / Accepted: 21 June 2021 / Published online: 31 January 2022

© The Author(s) 2022

Abstract

The wood-based furniture manufacturing industries prioritize quality of production to

meet higher market demands. Identifying various types of edge-glued wooden panel

defects are a challenge for a human worker or a camera. Several studies have shown

that the detection of edge-glued defects with low, high, normal, overlong, short is

identified but detection of residue and bluntness is highly challenging. Thus, the pre-

sent model identifies defects of low, high, normal, overlong, short by computer vision

and/or deep learning, whereas defects of residue and bluntness by deep learning based

decide by pass for having better performance. The goal of this paper is to provide an

improved defect detection solution for wood-based furniture manufacturing indus-

tries by process automation. Therefore, a system was designed that takes defect input

images from a camera as raw image and laser-aligned image for defect detection of

the edge-glued wooden panel. The process automation then performs computer vision-

based image features extraction with deep learning for defect detection. The aim of

this paper is to solve edge-glued defect detection problems by using design and imple-

mentation of edge-glued wooden defect detection, that can be stated as edge-glued

wooden panel defect detection using deep learning (WDD-DL) for process automation

by artificial intelligence and Automated Optical Inspection (AOI) consolidation. Possi-

bly there exist several types of defects on the edges while edge-banding on the wooden

panel in furniture manufacturing. Therefore, the scope is to achieve higher accuracy by

raw image and laser-aligned image feature extraction using deep learning algorithms

for final result defect classification in WDD-DL by AOI. The WDD-DL system uses

Gabor, Harris corner, morphology, structured light detection and curvature calculation

for pre-processing and InceptionResnetV2 Convolutional Neural Network algorithm

to attain the best results. The applications of this work can be found in quality control

of the furniture manufacturing industry for an edge, corner, joint defect detection of

the wooden panels. The WDD-DL achieves best results as the precision, recall and F1

score are 0.97, 0.90 and 0.92, respectively. The experiments demonstrate higher accu-

racy achievement as compared to other methods with overkill and escape rate analysis.

Ultimately, the discussion section provides an interesting experience sharing about the

necessary factors for implementing the WDD-DL in real-time industrial operations.

Extended author information available on the last page of the article

Vol.:(0123456789)

1 3

478

Wood Science and Technology (2022) 56:477–507

Introduction

Furniture manufacturing industries usually perform operations in the form of

multiple independent stages. Each stage requires a particular operation that

includes traditional ways of human skills based tasks, i.e., cutting, edge banding,

border smoothing, etc. Process automation will help with quality control (Q.C.)

checking for edge defect problems with better accuracy and less human depend-

ency. The furniture manufacturing process can be detailed as initially import-

ing raw material depending on the type of wood requirements. A wooden panel

is then produced with proper cutting and polishing, thus a defect-free panel is

passed on to the next stage. Selection of wooden panel is based on the respective

furniture parts specification, which is then passed through an edge-glued band-

ing machine. A traditional approach shows the oversized band is cut manually for

border smoothing.


---
*Page 2*


In practise, when the process is completed, the roughness on the edges is still

present which compromises the quality as well as brand value. To improve the

quality control process, WDD-DL provides a solution to identify the edge-glued

defects and to show live defect screening as output. The conventional process

of manufacturing involves only human workers in all the stages, which can be

improved with the help of process automation for better and defect-free produc-

tion. Applications include wood-based chairs, tables, closets, library racks, art-

work, etc. Process automation is evaluated to be a better alternative in both cases

of less infrastructure setup and less human worker dependency. In furniture man-

ufacturing, the quality control requirements are satisfied by the WDD-DL edge

defect detection system. Usually, during the quality control process, the detection

of different types of edge defects is a challenge (Aleksi et al. 2019). The differ-

ent types of edge-glued wooden panel defects can be given as high (the tape is

higher than the surface of the panel), low (the tape is lower than the surface of the

panel), bluntness (the tape is trim or has scrap on the edge), residue (visible glue

marks), short (the tape is shorter than the length of the panel) and overlong (the

tape is longer than the length of the panel). Practically, detecting the edge-glued

wooden defects is different as compared to wooden edge defects (Aleksi et  al.

2019; Wells et al. 2018) having edge knots, wane, split, pith, cracks, decays, etc.

The motivation for WDD-DL is how to achieve high accuracy for edge-glued

wooden defect detection in the furniture industry? Chen et al. (2018) published

a paper on edge detection based on machine vision, which describes the use of

edge filter, canny operator and pixel-wise width calculation, but the results pro-

vided for accuracy were quite inefficient. Therefore, a necessity to design a new

approach was realized that can provide higher accuracy and help in industrial

process automation. The background for WDD-DL can be referenced by various

edge detector, filters and classifiers of visual-based defect detection methods in

manufacturing industries (Czimmermann et al. 2020). The Harris corner is a well-

known computer vision algorithm that calculates differential of the corner score

with respect to direction. It has a high edge and corner distinguishing capability.

The process involved is colour to gray-scale conversion for enhancing processing

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 3*


479

speed, spatial derivative calculation, structure tensor setup, Harris response cal-

culation and non-maximum suppression for picking up optimal values. The Gabor

filter is a linear filter used for texture analysis, that can be described as analyzing

frequency content within an image’s specific region of analysis. In the case of

Local Binary Pattern (LBP), it requires fewer computations and quite an efficient

filter for defect detection. As the surface image has low-rank structure, defects

within them will be quite hard to detect. So, entity sparsity pursuit model is used

to detect such defects and resolve it based on LBP (Wang et  al. 2019). Micro

defects present within OLED panels are detected using modified LBP and SVM

classifier for better performance (Sindagi and Srivastava 2015). Edge features

extraction is used for many defect detection approaches that have a criterion for

edge length, strength and calculating edge neighbours having grey level pixel val-

ues for distribution (Wen and Xia 1999). In case of processing, texture elements

in spatial locations, also known as texture primitives are usually individual pixel

or grey-scale regions. To improve segmentation in the texture based defects for

fabric processing, Cao et al. (2017) implemented subspace segmentation model-

ling using local priori algorithm. Morphological based defects detection used to

avoid fatal defects before steel surface cracks can occur is presented by Yun et al.

(2019). An exhaustive dynamic encoding algorithm is used for searching such

defects by optimizing structural elements. The WDD-DL edge defects detection

process consists of checking defects in the raw image and laser-aligned image-

based features using detail inspection by deep learning. Multi-sensor (Wells et al.

2018) systems have been dominating the industrial detection environment for a

long time. The use of line laser and video camera constitutes a distinct approach,

that is applied to smart manufacturing (Contreras Masse 2019) for process auto-

mation of design and implementation of wooden panel edge defect detection using

deep learning algorithms (WDD-DL). Considering the case of defect detection

approach, segmentation (global) and non-segmentation (local) approaches were

used for defect object detection and non-overlapping rectangular defect regain

parts are used, respectively. The WDD-DL uses a non-segmentation approach,

to evaluate different detection algorithms and provide an efficient result. The

two-stage system uses different detection algorithms consisting of raw image and

laser-aligned image-based features using deep learning. A sequence of operations

is completed by process automation and will help manual workers to watch a live

screening of edge defects on the wooden panel during the manufacturing process.

In short, WDD-DL uses multi-sensor, two-stage system for process automation

by improving the quality of work. Ultimately, a defect-free and parallel manufac-

turing process automation is accomplished. In WDD-DL, the research gap can

be given about the edge-glued defect detection, which has hardly been presented

before. Most of the defect detection process focuses on panel or surface-based

defects, so the present model is exclusively built for improving the edge defect

detection process. The WDD-DL research is rationale because it provides a new

two-stage approach to solve edge-glued defect detection problem. This approach

is practical for the furniture industry in the quality control process. Table 1 shows

a comparison of different defect detection models in detail.

1 3

480

Wood Science and Technology (2022) 56:477–507

Song et al. (2015)

Color camera

Histogram and Eigen vectors

Support Vector Machine (SVM)

Sound Knot, Dry Knot, Black Knot,


---
*Page 4*


K-NN

Cracks, Fungus, Knot, Worm Holes


---
*Page 4*


GradeView Algorithm

N.A.

Wane, Knots, Splits, Wormholes, Rot,


---
*Page 4*


Shake, Iron Stain, Pith, Bark Pockets


---
*Page 4*


Tape is high, low, bluntness, overlong,


---
*Page 4*


(GLCM)

Radial basis function (RBF)

Neural network crack and decay


---
*Page 4*


Crack and Resin Pocket


---
*Page 4*


and Surface Roughness


---
*Page 4*


and Watermark


---
*Page 4*


residue and short


---
*Page 4*


References

Camera and/or scanner

Computer vision filter

Classifier

Defect type


---
*Page 4*


Tong et al. (2017)

Profile camera

GLCM

SVM, J48, Random Forest (RF) and


---
*Page 4*


ResNet50,DenseNet and Inception-


---
*Page 4*


Convolutional Neural Net-


---
*Page 4*


work (CNN)-MobileNet,


---
*Page 4*


ResNet

WDD-DL

Color camera and line laser

Gabor, Harris corner, morphology,


---
*Page 4*


Mu et al. (2015)

Color camera and X-ray

Gray level co-occurrence matrix


---
*Page 4*


structured light detection and


---
*Page 4*


curvature calculation


---
*Page 4*


Table 1   Comparison of different defect detection models


---
*Page 4*


Wells et al. (2018) Color camera, profile camera,


---
*Page 4*


X-Ray, line laser and grid


---
*Page 4*


laser

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 5*


481

Considering the results presented by most of the automation systems (Aleksi

et al. 2019; Czimmermann et al. 2020), they are inefficient in accurately identify-

ing edge defects on the wooden panel. Efforts are made to increase the quality con-

trol, but lack of high accuracy edge defect detection is the limitation of the litera-

ture work. Therefore, to achieve higher accuracy in the defect detection process,

WDD-DL consists of a two-stage model that performs extraction of image features

from the raw image and laser-aligned image using deep classification-based evalu-

ation. The aim of this study is to solve edge defect detection problems, which can

be stated as edge-glued wooden panel defect detection using deep learning (WDD-

DL) for process automation. The scope is to achieve higher accuracy by image and

laser feature extraction using deep learning algorithms for final result evaluation

in WDD-DL. Table S1 in Electronic Supplementary Material provides a compari-

son of different defect detection models for the industrial quality control.

The WDD-DL objectives are in detail as follows:

–	 Solving the wooden panel edge defect detection using AOI-based process


---
*Page 5*


automation: AOI-based process automation is considered as a crucial fac-

tor in wooden panel edge defect detection. Previously, trained workers were

assigned in every manufacturing stage to identify wooden panel defects and

remove them separately. This manual process was not effective enough as

they have missed many edge defect errors quite frequently. To overcome such

problems, process automation is provided to identify defects in the raw image

and laser-aligned image features by the industrial camera for classification.

Henceforth, various popular CNN models are used here for deep learning-

based classification.

–	 Real-time display of edge defects on the live screen: Most of the machine


---
*Page 5*


learning and deep learning methods require high processing time for clas-

sification that form a bottleneck for live screen display of edge defects. How-

ever, there exist some simplified filters based on a rule-based system to solve

such issues. For efficient processing, the wooden panel edge defects must be

identified in real-time for shorter or long edge defects with both for straight

edge and corner of edge. So, WDD-DL solves the challenge of detecting dif-

ferent edge defect types by multi-sensor and two-stage process in real-time.

The real-time live screening of edge defects is processed by using a raw

image and laser-aligned image features, where deep learning classification is

optional. Different types of edge-glued wooden panel defects can be identi-

fied by raw image and laser-aligned image features using deep classification

model.

–	 Deploying the model in the live manufacturing environment of the furniture


---
*Page 5*


industry: Even though the experiments will demonstrate the accuracy and

performance of the model in various scenarios, a discussion with the manu-

facturing workers will help to share detailed experiences as presented in the

discussion section. Henceforth, a live production environment will help us to

understand the practical aspects of the manufacturing scenario.

1 3

482

Wood Science and Technology (2022) 56:477–507

Literature survey

Recently, process automation within the furniture manufacturing industries was

performed for increasing quality, productivity and decreasing human-related errors.

Even though the traditional process automation was performed involving segmen-

tation (geometrical features) and non-segmentation (tonal and textual features)

approach, they were not found efficient for wooden panel edge/corner defect detec-

tion because of their low defect detection accuracy. Therefore, the present paper

proposes the WDD-DL two-stage approach combining filters and deep learning,

involving morphological and curvature calculation of edges in images with laser

information as a new two-stage approach to achieve higher accuracy for the qual-

ity control process. Some recent studies are shown in Fig. 1. Defect control strat-

egy analysis consists of defect detection in manufacturing, which includes statistics,

machine and deep learning.


---
*Page 6*


Several statistical feature extractions based models for wooden defect detection

including Linear Discriminant Analysis (LDA), Local Binary Patterns (LBP), Gray

Level Dependence Matrix (GLDM), Partial Least Squares (PLS), GradeView algo-

rithm, etc., are given below. The sawn wooden board-based texture used for feature

extraction and defect detection is demonstrated by Aleksi et al. (2019). The mod-

elling is performed using feature selection by statistical feature extraction, texture

defect detection and signal to noise ratio calculation. The automated grading system

for hardwood lumber defect detection is presented by Wells et al. (2018). In nine

different types of hardwood lumber, the defect detection model consists of board

scanning with Microtec Goldeneye 300 multi-sensor-quality scanner, and data were

analyzed with the Purdue GradeView algorithm. The use of local binary pattern var-

iants for wood defect image classification was performed by Rahiddin et al. (2020).

The basic and variants of the LBP feature set are constructed, from a stage of feature

extraction processes with the Basic LBP, Rotation Invariant LBP, Uniform LBP, and

Rotation Invariant Uniform LBP.


---
*Page 6*


The wood defect classes were further evaluated with the use of ANN, KNN

and J48 decision tree classifiers. Classification of wood defects for texture feature

Fig. 1   Defect control strategy analysis

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 7*


483

analysis is demonstrated by Abdullah et al. (2020). The extraction and analysis of

features are based on statistical texture in wood defects images. Feature extrac-

tion using the Grey Level Dependence Matrix (GLDM) and feature analysis were

executed to investigate the appropriate displacement and quantization parameters

that could significantly classify wood defects. Timber defect classification by mul-

tivariate texture descriptor performance evaluation is demonstrated by Hashim et al.

(2016). This paper presents a performance evaluation of texture features based on

orientation independent Grey Level Dependence Matrix (GLDM) for the classifica-

tion of timber defects and clear wood. A series of processes including feature extrac-

tion and feature analysis was implemented to facilitate data understanding in order

to construct a good feature. Wood defects soft measurement by feature fusion of

LDA and the compressed image sensor is presented by Li et al. (2017). Linear Dis-

criminant Analysis (LDA) algorithm was used to integrate these features and reduce

their dimensions. Features after fusion were used to construct a data dictionary and

a compressed sensor was designed to recognize the wood defects types. Appear-

ance lumber-based resin defect detection by 2D NIR spectroscopy is demonstrated

by Thumm and Riddell (2017). Resinous defects found on the finished products of

a barge’s boards and weatherboards, can cause resin bleed and resin show-through,

which is a discoloration of the paint layer above the resin feature. Several efforts

are made to eliminate resinous wood via manual and automated grading systems.

2D histogram-based classification of wood defects using Local Binary Differential

Excitation Pattern and LBP is presented by Li et al. (2019). A classification algo-

rithm based on LBP and local binary differential excitation pattern is presented

for the classification of the crack and the linear mineral line on the surface of the

birch veneer. The local binary differential excitation pattern (LB-DEP) is a texture

description model proposed in this paper, which is generated by the combination of

LBP and Weber’s Law. The 2D histogram is used to classify the defects with Euclid-

ean distance classifier.


---
*Page 7*


In case of defect detection using ultrasonic testing and machine learning model,

they can be further described by ultrasonic, genetic and classification and regression

trees (CART). Wood and wooden products testing by using air-coupled ultrasonic

technologies is presented as a review by Fang et al. (2017). Air coupled ultrasonic

(ACU) testing is a contactless ultrasonic measurement method used for material

characterization. To not contaminate during the testing processes by coupling agents

utilized in conventional ultrasonic testing, correlations between the ACU parameters

(amplitude, velocity, and spectrum) and the wood properties (i.e., density, moisture

content, strength, and stiffness) as well as the wood defects (knots, cracks, decay,

insect damage, and delamination) are inspected. Wood hole defects feature extrac-

tion by wavelet-based ultrasonic testing is presented by Yang and Yu (2017). Wave-

let energy moment can reflect the distribution of energy along the time axis, the

amount of energy in each frequency band and later extract the energy distribution

characteristics of signals in each frequency band. Therefore, wavelet energy moment

can replace the wavelet frequency band energy and constitute wood defect feature

vectors by PCA and feature vectors.


---
*Page 7*


Deep learning methods including CNN, R-CNN, GAN-CNN, BPNN in com-

puter vision are a preferred method for the recent studies, which is given as follows.

1 3

484

Wood Science and Technology (2022) 56:477–507

Wooden defect feature extraction and detection by using deep convolutional neural

networks is demonstrated by He et al. (2020). A laser scanner is used through a

deep convolutional neural network (D-CNN) and TensorFlow to train the network,

which consists of an input layer, four convolutional layers, four max-pooling lay-

ers, three fully-connected layers, a softmax layer, and an output layer. Additional

configurations involve dropout, L2 regularization, and data augmentation to avoid

the overfitting problem. Wood defect feature extraction and classification using BP

neural network, wavelet moment and Hu moment are demonstrated by He et  al.

(2020). Five features of training samples are extracted from the area, roundness and

circumference, which are represented by (x1, x2, x3) to form a three-dimensional

vector, so 150 test samples form a 150*3 matrix. Characteristics of wavelet energy,

the principle and characteristics of Hu moment invariant and extraction of wave-

let moment features are utilized. Wood veneer surface defect identification using

faster region CNN and transfer learning is presented by Urbonas et al. (2019). A

faster region-based convolutional neural network (Faster R-CNN) for the identifica-

tion of defects on wood veneer surface texture is presented. To improve the results,

pre-trained AlexNet, VGG16, BNInception, and ResNet152 neural network models

for transfer learning are used. Lumber tasks classification by using deep learning is

demonstrated by Hu et al. (2019). The four datasets used in this work were manually

marked as lumber defects, wood textures and lumbers by experts with configured

80:20 ratios for training and testing. They investigate variations of deep learning

strategies based on ResNet18 for classification of lumber images. Surface defect

inspection by using weakly supervised learning from deep convolutional networks

is presented by Chen et al. (2020). A novel end-to-end CNN architecture integrat-

ing the robust classifier and spatial attention module is proposed to enhance defect

feature representation ability for classification accuracy. Spatial attention class acti-

vation map (SA-CAM) is added to improve segmentation adaptability by generating

more accurate heat map. Defect recognition by using deep learning for multi-level

fusion of information is demonstrated by Gao et al. (2019). A three-level Gauss-

ian pyramid is introduced to generate the multi-level information of the defect, for

model training. Three VGG16 networks are built to learn the information, and the

outputs are fused for the final recognition result. Wood defect identification and

location by using convolutional neural networks is presented by He et al. (2019a).

In Mix-FCN, filter weights were initialized during training from the trained VGG16

model, whereas weights of VGG16 were learned from the dataset 1 and their sys-

tem model was trained, validated and tested on dataset 2. Overall classification

accuracy (OCA), pixel accuracy (PA), mean intersection over union, detection rate,

missing alarm, false alarm rate, and precision were evaluation indicators. Surface

defect classification using image segmentation by convex optimization is presented

by Chang et al. (2018). The convex optimization (CO) with different weights is used

as a pretreatment method for smoothing and the Otsu segmentation method to obtain

the target defect area images. Structural similarity (SSIM) results between the orig-

inal image and defect image were calculated to evaluate the performance of seg-

mentation with different convex optimization weights. The geometric and intensity

features of defects were extracted before constructing a classification and regression

tree (CART) classifier.

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 9*


485

Ultimately, the following achievements of WDD-DL are summarized as com-

pared to the limitations observed in the above literature survey:

1.	 WDD-DL uses both segmentation and non-segmentation approach, to decide

which approach suits better with different types of edge-glued wooden panel

defects as verified by the experiments.

2.	 The use of hybrid approach provides a better accuracy, which was rarely utilized

for implementation. Moreover, it performs better than the statistical and computer

vision filters to detect various types of defects in the industrial process.

3.	 The use of multi-sensor, two-stage design approaches yields better performance.

4.	 The algorithms are defined properly in pseudo-code and are quite practical to

implement.

Methodology

In the methodology section, the workflow process pre-requirements are presented

that enable the workflow in the furniture manufacturing industry. The WDD-DL

operational process is described as a workflow model given below:

–	 Resource Requirement: The manufacturing process must plan for detailed


---
*Page 9*


resource requirements. The resources include input raw material, types of mate-

rial, processing machinery, human workers, etc. In addition, all the resources

must be available, so as to be ready before the manufacturing process. An appro-

priate schedule plan ensures smooth initialization and completion of the work-

flow.

–	 Process Planning: Planning specifies the synchronization of process steps that are


---
*Page 9*


required to be implemented. A proper plan will ensure fixed operations with opti-

mal steps. Details of the machine usage, resource availability, human worker task

assignment, etc., are crucial factors of process planning. Each task performed

with the respective resources will be specified with a timing diagram/chart for

efficient operations.

–	 Quality Control: The grading of resources, evaluation, outcome is the measure


---
*Page 9*


of quality control. Therefore, the wooden panel types, defect types, wastage in

production, accuracy in production, and evaluation by the international quality

standard are performed. For manual workers, their skill training, past experience,

performance are also considered. In short, the quality control process helps to

reduce time, wastage and schedule resources for better performance.

The approached system WDD-DL, as shown in Fig. 2, is presented in four major

categories: The input provided to the system, AOI-based process automation that

automates the manufacturing system, filtering and classification using deep learning

and real-time defect detection for the manufacturing process.


---
*Page 9*


(Note: Raw image is input to the computer vision algorithm, whereas laser-

aligned image is input for CNN.)

1 3

486

Wood Science and Technology (2022) 56:477–507

Fig. 2   System model

WDD‑DL system model

1.	 Input to the System: The input provided to the system consists of a specific type of

wooden panel, to detect the edge-glued defects on it. In addition, the wood panel

exact size, positioning and placement on the conveyor should be determined.

2.	 AOI-based Process Automation: After the input is given to the system in the

form of a wooden panel, the defect detection process is known to be initialized.

The AOI-based process automation consists of controlling all of the hardware

and software within the WDD-DL. At first, when the input is provided in the

form of a wooden panel on the conveyor, the edge banding on the wooden panel

is performed by the edge banding machine, as shown in Fig. 2. The WDD-DL is

evaluated for detecting the accuracy of band placement on the edge-glued wooden

panel for the defect types identification. The identification of the defect will be

based on raw image, line laser-based image processing for computer vision with

the help of industrial camera having set the focal length and field of view (FOV),

which is processed by a local Nuvo-8108GC computer. Evaluating the results is

based on the environment having a camera, line laser, a combination of lenses and

its holder. Ultimately, the objective is to achieve real time live defect detection on

the wooden panel at the end of the conveyor as output.

3.	 Computer Vision-based Filtering and Deep Learning based Classification: The

filtering is performed on the raw image and on line laser image by using computer

vision algorithms so that the defects can be identified on the edge-glued wooden

panel after the edge banding process. Figures 3 and 4 are used to describe the

wooden defect detection system with the flowchart and its functions, respectively.

The WDD-DL process automation inspects the raw image and laser image-based

region-of-interest (ROI) for filtering and classification. In the beginning, the

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 11*


487

Fig. 3   Flowchart for the system model

Fig. 4   Functional model

image is captured for a wooden panel which needs to be inspected and is given

as input to the system. The system then checks whether the line laser mark is pre-

sent within the image, if not present then the system is required to recapture the

image. The absence of a line laser in the captured image may be due to weather

1 3

488

Wood Science and Technology (2022) 56:477–507

conditions, camera blurring, noise or other technical problems. The defect fea-

tures are then extracted from the raw image using k-means with contours, com-

paring pixel distribution, evaluating pixel after applying the threshold, means

denoising, Harris corner, local binary patterns (LBP), a histogram of oriented

gradients (HOG), wavelet-based contourlet transform, Gabor /convert scale edge

detection based on using Canny, Sobel, Prewitt, Roberts and Laplace. Ultimately,

WDD-DL has better defect detection achieved by Harris corner and Gabor filter

based on the results demonstrated in the experiment section. Whereas, the types

of edge-glued wooden defects present within WDD-DL are high, low, bluntness,

residue, short and overlong. For the line laser image, the features are extracted

using morphological processing and curvature calculation. After the above two

steps of defect feature extraction, if the present defect is detected by the camera,

then the defect ROI raw image is further passed for classification using deep

learning. If no defect is detected, then the camera continues to take new images

from the other parts of the edge-glued wooden panel based on the speed motion

of the conveyor. The deep learning classification models used are ResNet50,

MobileNetV2, DenseNet201 and InceptionResNetV2. If the defect is classified by

the deep learning model, then the defect area is highlighted on the real-time live

output screen, so that the human worker can notice it and can place that particular

wooden panel separately as an exception. The defect types are given as low (L),

high (H), normal (N), overlong (O) and short (S), which if detected by computer

vision then the results are declared even if unclassified by deep learning. In case,

the defect is not classified by the deep learning classifier, even after confirmed by

the computer vision algorithm, then it has to be confirmed by pass. For the case

of defect type residue (R) and bluntness (B) from captured image input with line

laser, when the control is in decide by pass function and if detected by computer

vision but not classified by deep learning, then it will use the result by deep

learning instead. If deep learning detects the defect, then it will output the defect

type without decide by pass. The functional model as shown in Fig. 4. presents

functions used within different stages of WDD-DL system.

4.	 Real-Time Defect Detection: The live screen is used to display the wooden panel

passing on the conveyer for quality inspection. The WDD-DL system helps to

identify edge defects in real-time and displays the defects on the edge-glued

wooden panel with the banding errors by highlighting the prone area. Therefore,

an alert is raised for helping the machine operator to notice the defect with the

beep sound, as passing the quality control checkpoint in that stage. Real-time

processing eases the manual work of missing the defect detection and ensures

high-quality checking and separating out the defective items.

Mathematical model

For the effective corner detection of better invariance including scale, rotation,

image noise and illumination variance, Harris corner detector is utilized (Derpanis

2004). In this case, signals use the local function of auto-correlation which identifies

local changes by a measure for shifting patches in various directions. In Eq. (1), the

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 13*


489

auto-correlation function can be given with the points (x, y) and the shift ( 훥 x, 훥 y)

as,

(1)

c(x, y) = ∑


---
*Page 13*


w[I(xi, yi) −I(xi + 훥x, yi + 훥y)]2

In Equation (1), I(. , .) is image function and (xi, yi) is centered (x,y) points of the W

(Gaussian) window. The Taylor expansion approximation for the shifted image can

be given in first-order term as:

(2)

I(xi + 훥x, yi + 훥y) ≈

I(xi, yi) + [Ix(xi, yi)Iy(xi, yi)][ 훥x


---
*Page 13*


훥y]

In Eq. (2), Ix(., .) and Iy(., .) is used to denote (x,y) partial derivatives, respectively.

(3)

c(x, y) = [훥x훥y]C(x, y)[ 훥x


---
*Page 13*


훥y]

Equation (3) is obtained by substituting Eq. (2) into (1). Here, c(x,y) is used to

denote capturing of local neighbourhood intensity structure. Let the matrix c(x,y)

have eigenvalues 휆1, 휆2 forming the description for rotational invariant. When both

휆1, 휆2 are low, high and opposite then it represents constant intensity, corner and


---
*Page 13*


edge, respectively. Another corner detection algorithm, Gabor function given in

Eq. (4) is used by Gaussian function as complex exponentially modulated operation

(Kumar and Pang 2002a). A non-orthogonal basis set is formed by complete Gabor

function and in 2-D plane, its impulse response can be given as:

(4)

g(x, y) = (

1

2휋휎x휎y )exp[−1

2( x2


---
*Page 13*


휎2


---
*Page 13*


x + y2


---
*Page 13*


휎2


---
*Page 13*


y ) + 2휋jwx]

The Gabor function’s radial frequency is denoted by uo . The (x, y) axis with Gauss-

ian envelope can be given as 휎x , 휎y space constants. Gabor functions behave as a

bandpass filter in the frequency domain and f(x, y) Fourier transform is given as:

(5)

G(u, v) = exp−1


---
*Page 13*


2[ (u−W)2


---
*Page 13*


u

−v2


---
*Page 13*


v ]


---
*Page 13*


휎2


---
*Page 13*


휎2

In Eq. (5), 휎u = 1


---
*Page 13*


2휋휎x and 휎v = 1

2휋휎y . The learning for deep residuals can be given

as a subset of stacked layer mapping as H(x), where prior layers’ input is x. Assum-

ing asymptotic approximations of several nonlinear layers of complicated functions

then it is also equivalent to residual function, i.e., H(x) - x, having the same dimen-

sions for input and output. So, F(x): = H(x) - x can be given as distinct for different

functions. The training error for deep models (He et al. 2016) is equivalent to shal-

low models when identity mapping is constructed from added layers. The difficulties

given by solvers for mapping identity to deep nonlinear layers are found to suffer

degradation. For the optimal identity mappings with the reformulation of residual

learning, the solver makes the weight tune to zero for identity mappings of the deep

nonlinear layers. Reformulation helps in the case of precondition problems having

less optimal identity mapping in reality. It is considered to be efficient for searching

permutations referring to identity mapping, when the closeness of identity mapping

1 3

490

Wood Science and Technology (2022) 56:477–507

is to optimal function instead of new function learning. Every subset of stacked lay-

ers adapts to residual learning. The building block is given as

(6)

y = F(x, {Wi}) + x

Here, we consider the input and output as x and y layers, respectively. In Eq. (6),

the learning for residual mapping can be given by F(x, {Wi}) function. For two lay-

ers, F = W2휎(W1x) where ReLU is given as 휎 and notation simplifying by omitting

biases. The element-wise addition and shortcut connection are F +x operation, 휎(y)

is second nonlinearity adapted after addition. The shortcut connections use Ws as a

linear projection for dimension matching, when x and F dimensions are not equal.

(7)

y = F(x, {Wi}) + Wsx

Ws square matrix can be used in Eq. (7). Here, F is flexible as a residual function.


---
*Page 14*


The notations given above can be applied to both fully connected layer and convo-

lutional layer, where deep convolution layer can be given by y = F(x, {Wi}) . The

feature map uses channel by channel element-wise addition. For training high defini-

tion mini-batch SGD (Akiba et al. 2017), the SGD and RMSprop are used to repre-

sent a simplified combination of momentum as an update rule.


---
*Page 14*


In Inception Resnet (Zhang and Davison 2019), the extracted features have

detailed information, achieving higher accuracy by the classifier. The features are

trained for the robust classifier to account quantitatively for the conditional and mar-

ginal distribution having relative importance with the function, as distribution align-

ment is dynamic. Manifold learning is used to present learned feature alignment

given by Manifold Embedded Distribution Alignment (MEDA). The process can

be given as: (a) manifold-based feature learning, (b) the conditional and marginal

distribution of data is aligned-based on dynamic distribution and (c) the estimated

parameters are used for classified labels updating.


---
*Page 14*


In modified distribution alignment, original features are preferred over the use of

GFK model features. It can be justified as: (a) the GFK model undetermined dimen-

sionality is avoided by the original features information and (b) the classification

problem can obtain required detailed information from the Inception Resnet (IR)

feature extraction.

Algorithms

This section presents algorithms with detail description used to carry out two-stage

operation process of WDD-DLA that includes computer vision-based defect detec-

tion, neural network-based defect detection and hybrid algorithm for final results

using computer vision and neural network-based defect detection.


---
*Page 14*


The Algorithm 1. AOI for computer vision-based defect detection is given in the

form of pseudo-code. In step 1, the input is given to the algorithm using a cam-

era. The input image consists of both raw image and laser-aligned image. The raw

image does not consider the presence of line laser, whereas the laser-aligned image

requires line laser mark for its processing. In step 2, the output of the algorithm is

given as candidateSet 1, which consists of computer vision-based filtered defects

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 15*


491

given as C. In step 3, the candidateSet 1 is initialized to NULL. In step 4, the If

condition checks whether the input image given to the algorithm is able to detect the

Region of Interest (ROI) in both the raw and laser-aligned image. In step 5, if the

previous condition is true, then morphological ROI feature (fm) is calculated from

the laser-aligned image to enhance laser features. In step 6, a new loop is started for

each laser feature taken from the 3D matrix of laser image to calculate pixel depth

difference having range 1 to k, where k is given as all of the non-segmented defects

detected from the laser image. In step 7, the depth curvature ( DepthCur ) is calculated

for each laser feature. In step 8, the depth local ( DepthLocal ) stores the successive 3D

matrix difference from 1 to k given as adjacency difference. In step 9, a new if con-

dition checks whether the depth locally calculated is greater than the tolerance limit

and depth curvature is within the curvature threshold limit. In step 10, if the above

condition is true then candidateSet 1 stores the classified defects that can either hold

one of the values from high, low and overlong.

In step 11, the blur kernel ( fb ) stores the calculated blur sharp boundary. In step

12, the Gabor filter ( fg ) stores the edge texture analysis features calculated from the

raw image. In step 13, the Harris-corner filter ( fh ) is used to store blunt boundary

features from the enhanced edge banding featured image. In step 14, inherited for

loop checks defect features for each pixel of normalized fh. In step 15, if condition

checks whether the defect features within that pixel are higher than the tolerance

limit. In step 16, if the above condition is true then candidateSet 1 stores the classi-

fied defects as bluntness, residue and short. In step 17, finally after processing all the

pixels within the target image, the defect features computed by computer vision are

returned as candidateSet 1.


---
*Page 15*


The Algorithm 2 pseudo-code given above is AOI for neural network-based defect

calculation in the pseudo-code form. In step 1, the input (Image) to the algorithm is

given by a camera for defect detection. In step 2, the output is given as candidateSet

2, which contains the defects detected by the neural network on the input image.

In step 3, the neural network confidence ( NNConf ) is given by the model predicted

1 3

492

Wood Science and Technology (2022) 56:477–507

confidence. In step 4, the candidate set 2 is initialized by setting it to NULL. In step

5, the input image captured by the camera may have different dimensions depend-

ing on the camera picture resolution, so the image is resized to the standard neural

network input image dimensions. In step 6, after providing the resize image as input

to the neural network, the output is provided in the form of classified defects type

( ClassifyDefect ) and neural network confidence ( NNConf ) about that classification. In

step 7, candidateSet 2 is added with the output of the neural network having Clas-

sifyDefects and NNConf as the format. In step 8, the output is returned by the algo-

rithm as candidateSet 2 for the defect features computed by neural network.

The Algorithm 3 given is a computer vision and neural network hybrid algo-

rithm for the final defect result detection presented in the pseudo-code form. In

step 1, the input given to the algorithm is the captured image from the camera.

In step 2, candidateSet 1 is used which stores the AOI-based computer vision

detected defects. In step 3, candidateSet 2 is used which stores the AOI-based

neural network detected defects. In step 4, the NNConf is used to store a prediction,

specifically neural network model confidence about the detected defect. In step 5,

the output candidateFinal determines whether the output type will be predicted by

computer vision defect or neural network defect or by combining both  hybrid. In

step 6, the result candidateFinal is initialized to NULL. In step 7, the if condition

checks that whether candidateSet 1 is a subset of either having a defect in D1 set

defect type low, high, normal, overlong and short. In step 8, if the previous con-

dition is true then a new inherited If condition checks whether NNConf is greater

than or equal to 80% and none of the candidateSet 1 values match with the can-

didateSet 2 values. In step 9, when the previous two conditions are true then the

result candidateFinal is assigned the values by adding candidateSet 1 and candi-

dateSet 2. In step 10, if step 8 is not true then the result candidateFinal in step 11 is

assigned only the values from candidateSet 1. Step 12 checks if the candidateSet

1 is a subset of value from D2 set having defect type as residue or bluntness. Step

13 verifies if the previous condition is true and NNConf is greater than or equal to

80%. In step 14, when the previous two conditions are true then candidateFinal is

assigned the values from candidateSet 2 as the neural network defect. In step 15,

the else condition represents if the NNConf is not greater than or equal to 80%. In

step 16, candidateFinal is assigned the values from candidateSet 1 as the computer

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 17*


493

vision defect. In step 17, finally the hybrid algorithm returns the candidateFinal as

the final result of the WDD-DL system.

Experiments

For the experiments section, the workstation configuration used is presented in

Table 2. All the experiments performed in this section are used to support pro-

posed methodology demonstration of this paper. The results are evaluated using

a large set of defect category and multiple defect category dataset using deep fea-

ture extraction. The system configuration consists of Solid State Drive (SSD) and

Graphics Processing Unit (GPU) card for edge-glued wooden panel defect detec-

tion using deep feature extraction.

Dataset

The dataset given in Tables  3 and 4 presents the defect category and multiple

defect category with their corresponding frames, respectively.


---
*Page 17*


These two datasets are used for both training and testing with different ratios

of CNN models for deep feature extraction. Various CNN models are used for

checking the accuracy of the test dataset for selecting the high accuracy model

and achieving best performance. The training data consist of various types of

independent or combined edge-glued wooden defects, which is used to train a

CNN model. A test data will then be used to check for the accuracy given by the

various CNN models. All the data used for training and testing are taken from a

single source Sakura furniture industry in Taichung, Taiwan. The high definition

industrial camera is used for capturing different defect images to generate a data-

set, which will be utilized by filters of computer vision (Kumar and Pang 2002b)

1 3

494

Wood Science and Technology (2022) 56:477–507

Table 2   System configuration

Processor

Intel Core i7-7700 @ 3.60 GHz

Memory

16 GB

SSD card

Plextor PX-256S2C

Graphics card (GPU)

1060 Nvidia GeForce GTX, 6GB

Python library

Numpy, Sklearn, OpenCV, Keras,


---
*Page 18*


Tensorflow, Matplotlib and

Seaborn

Table 3   Dataset for defect

category and frames

Defect category

Normal

Bluntness

Residue

High

Low

Frames

1722

2343

1269

106

2655

Table 4   Dataset for multiple defect category and frames

Defect category

Bluntness + Low

Residue + High

Residue + Low

Frames

525

1815

3

and classification by CNN for evaluating the results. In Fig. 5a, the different cat-

egory sample types are presented, which are used for this experimentation.

Evaluations

The configuration for CNN functional parameters is shown in Table  5, which

presents the input parameters that are used for configuring the CNN model. The

input shape denotes the height, width and depth (color channel) of the image used

for processing. The batch size is used to indicate the data fitting in the batch of 10

to the network. A single epoch presents the dataset accessed in the set of batches

within the neural network by a forward and backward pass at once, which is com-

pleted in iterations. The weights here are referred from “Imagenet” visual object

recognition project (Russakovsky et  al. 2015), which are learnable parameters

used for controlling the signal within the network. The train and test ratio defines

the distribution for the images into experiments for validation. Figure  5b pre-

sents the output generated after processing images from Gabor filter. Four images

are shown, which have bluntness defect type, given as input for the Gabor filter

operation. The purpose of Gabor filter is to extract features of edge and perform

the operation of convert scale, suitable for pattern identification. The result of

two algorithms is similar, but the convert scale function has better identification

evaluation.


---
*Page 18*


In Fig.  6a, K-means, an unsupervised machine learning algorithm is used to

find new pixel-based patterns by clustering, for image segmentation purpose.

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 19*


495

Fig. 5   Different categories of defects and edge-glued defect evaluation

Table 5   Convolutional neural network (CNN) parameters

Input shape

Batch size

Epoch

Initial weights

Train and test ratio

(224, 224, 3)

10

20

Imagenet

66:33

Fig. 6   Evaluation by basic image processing algorithms

Successively, Find contours function is used for defect detection within the input

image for normal and bluntness types. Even though the output in processed image

shows defect detection by red mark, it is still not evaluated to be effective for achiev-

ing high accuracy. In Fig. 6b, the pixel distribution comparison algorithm is used to

capture and fetch the defect features and their positions, respectively. The high and

low defect gap is used to represent the unnecessary gap between the tape and panel

in the images.

1 3

496

Wood Science and Technology (2022) 56:477–507

Fig. 7   Processing by denoising, threshold and edges

Therefore, the purpose of this algorithm is to extract the region, segments from

the images with respect to foreground and background. It is still ineffective as per

the expected results and demonstrated by the fluctuating graph.


---
*Page 20*


In Fig. 7a, Means denoising and threshold otsu is used to present the algorithm

for filtering out non-defect and fetch the defect regions after eliminating the noise.

Henceforth, by a careful inspection, it was found to be suffering from similar accu-

racy issues as discussed previously for k-means. Figure  7b shows various edge

detection filtering algorithms such as Canny, Sobel, Prewitt, Roberts and Laplace,

which are used to extract edge features from the input image. Each filter has its own

way of edge feature extraction, which takes input of bluntness wood pattern type

image.


---
*Page 20*


Usually, applying computer vision-based filters are considered to be a basic

process in edge defect detection. In Fig. 8, hybrid algorithms are used to present

experiments by combining different algorithms. At first, the bluntness wooden

pattern is taken as input. Here, applying smoothing and threshold algorithm

before edge detection algorithm has achieved better detection results. The first

Fig. 8   Hybrid algorithm

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 21*


497

Fig. 9   Harris corner evaluations for different defect samples: a Normal, b High, c Low + Bluntness and

d Bluntness

Table 6   Comparison of different defect classification models based on F1 score

Models/defects

Bluntness

Residue

High

Low

Normal

Evalua-

tion time

(s)

MobileNetV2

0.873

0.892

0.993

0.979

0.924

0.003


---
*Page 21*


ResNet50V2

0.625

0.844

0.995

0.667

0.83

0.005


---
*Page 21*


ResNet50

0.818

0.973

0.997

0.979

0.886

0.007


---
*Page 21*


DenseNet169

0.95

0.982

0.997

0.984

0.952

0.007


---
*Page 21*


InceptionResNetV2

0.904

0.986

0.997

0.991

0.93

0.008


---
*Page 21*


ResNet101V2

0.795

0.935

0.991

0.957

0.648

0.008

ResNet101

0.736

0.735

0.86

0.761

0.61

0.009


---
*Page 21*


DenseNet201

0.703

0.974

0.997

0.984

0.903

0.009

result is obtained after combining it with original image and canny. The second

result is obtained by combining original and Gaussian blur. Similarly, third result

is obtained by combining threshold with Canny. Figure 9 presents Harris corner

evaluations for normal, high, low with bluntness and bluntness defect types. The

process achieved by means denoising, Harris corner function and Harris corner

map presents high accuracy evaluation of defects. Therefore, from Figs. 5b, 6, 7,

8, 9, Gabor function and Harris corner are only found to achieve high accuracy.

Table 6 shows the F1 score calculated as a part of performance measure for the

WDD-DL F1 score (also F-score or F-measure) as a measure of a test’s accuracy.

The column shows the various deep neural network models used within this paper

for performing experiments, whereas the row for every model represents 5 types

of defects detected from the wooden panel image by the respective neural net-

work model. The values present the F1 score, which is given as a weighted aver-

age of precision and recall.

1 3

498

Wood Science and Technology (2022) 56:477–507

(8)

F1Score = 2 × Precision × Recall


---
*Page 22*


Precision + Recall

It is also known as an indicator to mark precision and recall together as given

in Eq. (8). Here, the red colour highlighted values shows the highest score for a

particular defect. In this case, the InceptionResNet v2 is the choice for this paper,

as it shows the highest F1 score values evaluated among most of the defects in

comparison. The defect detection time given by the InceptionResNet v2 is 0.008

sec, which is quite practical to present the results in the real time environment.

The computer vision evaluation time for detecting a defect is given as 0.013,

which is quite higher as compared to any of the deep neural network models

listed above.


---
*Page 22*


Figure 10 presents the performance measure of WDD-DL by precision, recall,

F1 score and evaluation time for the different neural network models for the average

of various types of defects. In Fig. 10a, the precision is used to present the actual

“accuracy”, when predicting the positive results. It can also be said as correctly pre-

dicted positive observations to the total predicted positive observations. The preci-

sion formula is given in Equation (9) as

(9)

Precision =

TruePositive(TP)

TruePositive(TP) + FalsePositive(FP)

The highest precision in all deep neural network models is demonstrated by

DenseNet 169 and InceptionResnet v2. Figure 10b presents the recall performance

measure calculation for the actual positive output to “How much can be recalled”,

Fig. 10   Deep neural network performance measure comparison: a Precision, b Recall, c F1 Score and d

Prediction Time

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 23*


499

when the actual situation is positive. Recall can be given as the ratio of correctly

predicted positive observations over all observations in the actual class. The recall

formula can be given as Eq. (10),

(10)

Recall =

TruePositive(TP)

TruePositive(TP) + FalseNegative(FN)

The F1 score as presented before, is given in Fig. 10c where DenseNet 169 and

InceptionResnet v2 are found to be leading in comparison to other deep neural net-

work models. Figure 10d presents an evaluation time taken by each model for mak-

ing a defect prediction. It can be observed that even though the fastest evaluation is

performed by MobileNet v2, it does not provide higher F1 score for most of the dif-

ferent types of defect detection.


---
*Page 23*


The benchmark results show the comparison between the ANN (DN) + Find

contours method, LBP + SVM method, HOG+SVM method and WDD-DL sys-

tem. Table 7 shows that the defects F1-score comparison is presented independently,

recall is effective in the defect detection process, the precision for the alarm and

evaluation time for the processing. Overall the WDD-DL system performs best in

all the experiment cases for the performance and evaluation time to the recent refer-

ences. The output processed image results and the detail benchmark results for the

confusion matrix are given in Figure S1 and Figure S2 to S4 in Electronic Supple-

mentary Material, respectively.


---
*Page 23*


The highest recall is recorded by the DenseNet 196, DenseNet 201 and Inception-

Resnet v2 in all of the deep neural network models. The neural network model time

is given by processing of 1 frame per second as prediction time. Even though the

running time for half of the models shown in the table is less, the performance meas-

ure is taken as the priority. The performance measure given by accuracy is more

instinctively accurate and can be given as the ratio of correctly predicted observa-

tions to the total observations.


---
*Page 23*


Figure S5(a) in Electronic Supplementary Material, which shows Neural Net-

work model training epoch vs. accuracy presents the increase in accuracy over more

epochs until achieving stable accuracy rate, whereas Figure S5(b) in Electronic

Table 7   Benchmark comparison results for the defect classification

Reference/algorithm

Bluntness Residue High

low

Normal Recall Precision Evaluation


---
*Page 23*


time (sec.)

ANN (DN) + Find


---
*Page 23*


Contours (Wenshu et al.

2015)


---
*Page 23*


nan

0.005

0.005 nan

nan

0.001

0.325

0.051

LBP + SVM (Kuang


---
*Page 23*


0.275

0.707

0.909 0.655 0.455

0.489

0.908

108.5


---
*Page 23*


et al. 2018)

HOG + SVM (Sugiarto


---
*Page 23*


et al. 2020)


---
*Page 23*


0.693

0.902

0.97

0.909 0.835

0.819

0.916

106.4

WDD-DL

0.904

0.986

0.997 0.991 0.93

0.90

0.97

0.008

1 3

500

Wood Science and Technology (2022) 56:477–507

Supplementary Material shows Neural Network model training epochs vs. loss pre-

sents the decrease in loss over more epochs until achieving stable loss rate.

Overkill and escape analysis

As the industrial measurement and inspection error are unavoidable, there are some

issues faced that include defect-free cases, which are rejected (overkill) and defective

cases are accepted (Escape) (Fu et al. 2011). Overkill and escape lead to high produc-

tion cost and dissatisfaction of the customer, respectively. These overkill and escape

analysis is used in industrial system for analysis and process improvement. The input

parameters for obtaining the model in Figure S6 analysis of error distribution graph

in Electronic Supplementary Material, is shown by Table 8 parameters set for overkill

and escape analysis. The upper specification, the lower specification limit and average

value are taken from the defect types low and high range. The total sigma is the pro-

cess standard deviation, which is assumed to be normal distribution. The Gage R &

R (GRR) sigma is a measurement variation, which is narrowed as possible and taken

between 10% ∼ 30% as a marginal rate. Less than 10% are acceptable and less than 5%

is good but will incur high cost and hard to achieve. It can also be given as in Eq. (11),

Table 8   Parameters set for

overkill and escape analysis

USL

LSL

Average

Total sigma

GRR sigma

Bias

0.2

− 0.3

− 0.1

0.1

0.01

− 0.01

Table 9   Parameters for GRR

AND CPK

GRR (Percent of total variance)

10%

GRR (Percent tolerance with 5.15 distribution width)

10%

Cpk Observed

0.67

Cpk Actual

0.64

Fig. 11   The analysis of test cases

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 25*


501

(11)

GageR&R = 5.15 × 휎m


---
*Page 25*


USL −LSL × 100%

Here, the measurement system variation is 휎m , the upper specification limit is USL

and the lower specification limit is LSL. The bias is the difference between observed

mean and the reference value measurement, which can be positive or negative. As

shown in Table 9, Cpk is the part of process capability index, which specifies pre-

determined specification limits for producing items that can be given as in Eq. (12),

(12)

Cpk = min(USL −휇, 휇−LSL)

Here, the process mean is 휇 and the process standard deviation is 휎 . Figure S6 in

Electronic Supplementary Material, presents the analysis of error distribution,

which shows the error range for USL and LSL. Variance and percentage of error

is given as standard distribution, with low overkill rate and escape rate as tolerable

values in process automation.


---
*Page 25*


3휎

Figure 11 presents the analysis of test cases, which can be stated as:

1.	 A good part is evaluated to be good.

2.	 A bad part is evaluated to be bad.

3.	 (Type I error) Overkill: A good part is evaluated to be bad.

4.	 (Type II error) Escape: A bad part is evaluated as good.

The observations from the measurement system for fault rate analysis is when we

increase sigma gradually, the overkill rate and escape rate are found to be increas-

ing. In case of increasing GRR sigma, the overkill rate is increasing, but the escape

rate is found to be fluctuating highly, whereas for increasing the bias, the overkill

rate and escape rate are increasing too. Higher accuracy in defect detection can be

achieved, which will require hyper-parameter setting in deep neural network and

will take high processing power for evaluation.

Discussion

Analysis of CNN model and evaluation

Convolutional Neural Network (CNN) serves the purpose of feature extraction and

classification. During the baseline CNN evaluation, several challenges are faced

with different angles (rotation, translation and scaling), different background and

illumination. In such case, high training images of the defect are required, which is

quite a challenge for identifying different shapes and sizes of defect. To overcome

these challenges, we have used geometric filters to capture different category of

defect features as for two-stage classification. The illumination problem was solved

using batch normalization and rectified linear unit (ReLU). CNN is usually stuck in

local minima because of high redundancy in training feature. To avoid this problem,

1 3

502

Wood Science and Technology (2022) 56:477–507

feature selection used within the algorithm helps to resolve such issue. Still, eval-

uation metrics in CNN was average for accuracy, precision, recall and F1-score

because of over-fitting. Therefore, optimization was needed to achieve best predic-

tion without over-fitting. The over-fitting problem is resolved by using dropout layer

and ReLU as a part of regularization. Also applying minimal CNN and some well

known CNN models was not enough. To achieve better performance, more experi-

ments and high-end GPU for processing were used. InceptionResnet v2 performed

better than other CNN models by having high accuracy and recall with better evalu-

ation time for different defect detection models.


---
*Page 26*


For baseline CNN, the training time is high, whereas classification is average,

there is a need of proper data pre-processing, CNN layer configuration and feature

extraction. The CNN performed with high accuracy in capturing different defect

shapes and sizes with geometric filters. Feature extraction was also simplified by

categorizing different types of defects distinctly. Even though geometric filters

were applied, most of the CNN models suffered in accuracy because of high false

alarm rate. Loss incurred is higher too, while performing convolution operation. A

proper setting for CNN configuration is one of the crucial tasks for achieving bet-

ter performance with minimal values as shown in Table 5 (CNN parameters). In

addition, the CNN with appropriate filters and multiple planned experiments con-

stitutes a finely executed approach for implementing effective and efficient research.

CNN is incomplete without the support of high-end GPU hardware to accelerate the

implementation.

Structural light detection for the depth edges

The purpose of using structured light detection is to perform depth edges detec-

tion accurately and avoid scattering of the inner texture edges. Usually, the depth

discontinuities based distortion depends upon the distance from the camera (Park

et al. 2008). The depth edge detection is crucial in the defect detection process as it

represents object contours. The limitations of the traditional computer vision-based

edge detection method are no differentiation present within depth edges and texture

edges. Moreover, detecting depth edges is possible by eliminating the need of recon-

struction of dense 3D image scenes. The process of detecting depth edge map con-

sists of consecutively projecting white and structured light of the target object. The

pattern image is obtained by differentiating the white and structured light images

with robust threshold criteria. The final depth edge map is achieved by capturing

candidate locations from the Gabor filter by identifying depth edge and distortions

of the light patterns.

Experience sharing for development and deployment

Wooden furniture has several applications in the market including homes, offices,

shops, restaurants, etc. Several manufacturing industries are completely depend-

ent on the human workers for identification of various types of defects. In such

cases, the wood material is first cut into a wooden panel, which is then sent for the

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 27*


503

edge-glued banding process. During the edge-glued banding process, several defects

can arise that include tape can be high, low, bluntness, residue, short and overlong.

Traditionally, a quality check (Q.C.) sticker was put on the wooden panel after the

human worker inspection. There are high chances that the human identification of

such defects can be missed. In addition, the human worker needs extra time other

than the edge banding process to identify the defects because missing an error may

affect the brand image and quality of the furniture product. Due to inefficiency of

this process, WDD-DL was designed to overcome this problem and provide real-

time identification of edge-glued banding defects. At the start of WDD-DL, some

basic image filters were used to identify such defects but due to their inaccuracy

only Gabor and Harris corner were used with a deep feature extraction as a two

stage model to achieve higher accuracy.


---
*Page 27*


Comparing the literature (Hao et al. 2020) and this paper’s experiments, most of

the systems use the same group of edge feature detection filters. WDD-DL experi-

ments have been performed on various filters including the hybrid ones but dem-

onstrate better results with the use of red line laser with filtering and different per-

formance evaluation with accuracy and loss. Various defect/data feature collections

were performed with infrared, ccd cameras but was decided to use line laser as to

represent the highlight of the model. The edge-glued based defect detection can be

performed on wooden panels of different shapes and sizes. The image quality is con-

trolled by adjusting the angle of the red line laser (laser-aligned), frequency of tak-

ing images is maintained to 75 frames/sec by the use of practical industrial camera

in the experimentation environment. The pre-processing of the image taken to get

the necessary features includes specifying the image resize and several defect label-

ling to the training images with the help of manual operations too. The speed of the

conveyor is not an issue as the 75 frames/sec are taken by the camera to process

the frame. Documentation of the production operation can be done by generating

a report that includes day-wise, weekly or monthly production with average errors

encountered per day, per week or per month respectively. The WDD-DL system

shows very few false alarm detected as the accuracy presented by the CNN models

is quite high. The threshold set by the CNN model is 80% for identifying a defect

type based on the training defect images. Ultimately, the human operators sort out

the defective wooden panels after edge banding based on the error alert as shown

by the WDD-DL display screen. The WDD-DL system performs comparison with

different edge defect detection algorithms, CNN models and evaluates them based

on F1 score, precision, recall, accuracy and loss. Henceforth, the overall benefit of

the system can be represented as high accuracy, real-time defect detection, while the

wooden panel is on the conveyor after the edge banding process.

Applying AOI in the industrial environment

AOI approach is being applied to solve many industrial challenges (He et al. 2019b;

Block et al. 2020). It is focused on reducing human dependency, improve speed and

achieve high accuracy. The use of AOI has helped the quality control process to be

transformed and implement process automation to identify, notify, alert and display

1 3

504

Wood Science and Technology (2022) 56:477–507

the affected region. The purpose of using AOI is to provide high accuracy defect

detection for quality inspection and higher production with less maintenance cost.

The performance modelling can be done by accuracy, precision, F1-score and recall

from the confusion matrix calculations.


---
*Page 28*


The deep learning algorithms are well known to provide only classification,

which is insufficient to locate exact defect position on the edge-glued wooden panel.

Therefore, a two-stage approach consists of high level pre-processing by computer

vision that captures laser based non-segmented defects for size of defect and type

stored in candidate set 1, whereas the other defect patterns detected by better classi-

fication are stored in candidate set 2. Later, both candidate set 1 and candidate set 2

are combined to represent as a complete final result. “The computer vision based fil-

tering consists of a rule-based system for achieving good accuracy results, whereas

the deep learning based classification provides the enhancement for the best accu-

racy.” Ultimately, the innovation statement can be stated as the various wood-based

edge-glued defect detection in the WDD-DL having structured light detection and

line laser (multi-sensors) by using the computer vision-based pre-processing, filter-

ing and convolutional neural networks for re-evaluation, to achieving high accuracy

results. The goal of this paper is to perform hardware and software based integration

using AOI and to share practical industrial implementation experience for achieving

high accuracy results.

Limitations of the WDD‑DL

Limitation of this work can be given that the experiments are performed only on 21

different wood types, and fewer defect training images were available for overlong

and short edge banding. However, the improvements are not a big challenge to be

implemented as only some additional training is required for the CNN model. The

approach presented by the WDD-DL paper is multi-disciplinary research. This paper

is the successor for the edge based defect detection process in the furniture indus-

try. In the future, WDD-DL can be included as a part of the ERP system operating

within the respective industrial environment to have better track of Quality Control

(Q.C.) process and records for reporting.

Conclusion

WDD-DL provides automation for the development of the production line, by eas-

ing defect detection work load on the human machine operators. Integration of

WDD-DL and production line helps to complete the workflow automation process.

Edge-glued wooden defect detection has high demand in the furniture industry, hav-

ing products for homes, offices, shops, institutions, organizations, etc. Therefore,

advancing the real-time defect detection process, which is the part of quality con-

trol in the industrial environment by using various computer vision and CNN algo-

rithms for achieving higher accuracy. The use of two-stage model utilizing computer

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 29*


505

vision-based filtering and deep learning-based classification by using Inception-

ResnetV2 is found to be yielding best performance with the highest recall of 0.90

in comparison with other popular CNN models, which is effective for the defect

detection process. Moreover, the evaluation time is quite reasonable to be shown on

the live screen at 0.008 seconds. The outcome of this paper can be given as achiev-

ing high accuracy quality control in the furniture industry using multi-sensor, two-

stage approach for real-time monitoring of defects. The paper also provides detailed

overkill and escape rate analysis. The discussion section containing interaction with

industrial employees after implementing the WDD-DL provides various insights

into the practical working scenario. In the future work, a new interpretable AI model

is planned to be demonstrated, which can detect different kinds of defects includ-

ing the wooden panel surface defects for overall industrial product defect inspection.

Ultimately, the paper achieves better performance for the quality control process by

WDD-DL with higher F1 score.

Supplementary Information  The online version contains supplementary material available at https://​doi.​

org/​10.​1007/​s00226-​021-​01316-3.

Acknowledgements  This research is funded by the DDS-THU AI Center of Tunghai University, Taiwan

and Taiwan Sakura Corporation with the project code: 108670. Also a special thanks to the funding from

ministry of science and technology (MOST), Taiwan with the project code: “MOST 109-2622-E-029-

013-”, reviewers and editors of the WSAT journal.

Declarations

Conflict of interest  The authors declare that they have no conflict of interest.

Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License,

which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as

you give appropriate credit to the original author(s) and the source, provide a link to the Creative Com-

mons licence, and indicate if changes were made. The images or other third party material in this article

are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the

material. If material is not included in the article’s Creative Commons licence and your intended use is

not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission

directly from the copyright holder. To view a copy of this licence, visit http://​creat​iveco​mmons.​org/​licen​

ses/​by/4.​0/.

References

Abdullah ND, Hashim UR, Ahmad S, Salahuddin L (2020) Analysis of texture features for wood defect clas-


---
*Page 29*


sification. Bul Electr Eng Inf 9(1):121–128

Akiba T, Suzuki S, Fukuda K (2017) Extremely large minibatch sgd: training resnet-50 on imagenet in 15


---
*Page 29*


minutes. arXiv preprint arXiv:​1711.​04325

Aleksi I, Sušac F, Matić T (2019) Features extraction and texture defect detection of sawn wooden board


---
*Page 29*


images. In: 2019 27th Telecommunications Forum (TELFOR), IEEE, pp 1–4

Block SB, da Silva RDD, Dorini L, Minetto R (2020) Inspection of imprint defects in stamped metal surfaces


---
*Page 29*


using deep learning and tracking. IEEE Trans Ind Electron. https://​doi.​org/​10.​1109/​TIE.​2020.​29844​53

Cao J, Zhang J, Wen Z, Wang N, Liu X (2017) Fabric defect inspection using prior knowledge guided least


---
*Page 29*


squares regression. Multimed Tools Appl 76(3):4141–4157

Chang Z, Cao J, Zhang Y (2018) A novel image segmentation approach for wood plate surface defect clas-


---
*Page 29*


sification through convex optimization. J For Res 29(6):1789–1795

1 3

506

Wood Science and Technology (2022) 56:477–507

Chen H, Hu Q, Zhai B, Chen H, Liu K (2020) A robust weakly supervised learning of deep conv-nets for


---
*Page 30*


surface defect inspection. Neural Comput Appl 32:11229–11244

Chen N, Men X, Han X, Wang X, Sun J, Chen H (2018) Edge detection based on machine vision applying


---
*Page 30*


to laminated wood edge cutting process. In: 2018 13th IEEE conference on industrial electronics and

applications (ICIEA), IEEE, pp 449–454

Contreras Masse R (2019) Application of iot with haptics interface in the smart manufacturing industry.


---
*Page 30*


Instituto de Ingenierıa y Tecnologıa

Czimmermann T, Ciuti G, Milazzo M, Chiurazzi M, Roccella S, Oddo CM, Dario P (2020) Visualbased


---
*Page 30*


defect detection and classification approaches for industrial applications-a survey. Sensors 20(5):1459

Derpanis KG (2004) The harris corner detector. York University, 2

Fang Y, Lin L, Feng H, Lu Z, Emms GW (2017) Review of the use of air-coupled ultrasonic technologies for


---
*Page 30*


nondestructive testing of wood and wood products. Comput Electron Agric 137:79–87

Fu S, Kauppila O, Mottonen M (2011) Measurement system escape and overkill rate analysis. Int J Adv


---
*Page 30*


Manuf Technol 57(9–12):1079

Gao Y, Gao L, Li X, Wang XV (2019) A multilevel information fusion-based deep learning method for


---
*Page 30*


vision-based defect recognition. IEEE Trans Instrum Meas 69(7):3980–3991

Hao R, Lu B, Cheng Y, Li X, Huang B (2020) A steel surface defect inspection approach towards smart


---
*Page 30*


industrial monitoring. J Intell Manuf 32:1833–1843

Hashim UR, Hashim SZM, Muda AK (2016) Performance evaluation of multivariate texture descriptor for


---
*Page 30*


classification of timber defect. Optik 127(15):6071–6080

He K, Zhang X, Ren S, Sun J (2016) Deep residual learning for image recognition. In: Proceedings of the


---
*Page 30*


IEEE conference on computer vision and pattern recognition, pp 770–778

He T, Liu Y, Xu C, Zhou X, Hu Z, Fan J (2019) A fully convolutional neural network for wood defect loca-


---
*Page 30*


tion and identification. IEEE Access 7:123453–123462

He T, Liu Y, Yu Y, Zhao Q, Hu Z (2020) Application of deep convolutional neural network on feature extrac-


---
*Page 30*


tion and detection of wood defects. Measurement 152:107357

He Y, Song K, Meng Q, Yan Y (2019) An end-to-end steel surface defect detection approach via fusing mul-


---
*Page 30*


tiple hierarchical features. IEEE Trans Instrum Meas 69(4):1493–1504

Hu J, Song W, Zhang W, Zhao Y, Yilmaz A (2019) Deep learning for use in lumber classification tasks.


---
*Page 30*


Wood Sci Technol 53(2):505–517

Kuang H, Ding Y, Li R, Liu X (2018) Defect detection of bamboo strips based on lbp and glcm features by


---
*Page 30*


using svm classifier. In: 2018 Chinese control and decision conference (CCDC), IEEE, pp 3341–3345

Kumar A, Pang GK (2002a) Defect detection in textured materials using gabor filters. IEEE Trans Ind Appl


---
*Page 30*


38(2):425–440

Kumar A, Pang GK (2002b) Defect detection in textured materials using optimized filters. IEEE Trans Syst


---
*Page 30*


Man Cybern Part B (Cybernetics) 32(5):553–570

Li C, Zhang Y, Tu W, Jun C, Liang H, Yu H (2017) Soft measurement of wood defects based on lda feature


---
*Page 30*


fusion and compressed sensor images. J For Res 28(6):1285–1292

Li S, Li D, Yuan W (2019) Wood defect classification based on two-dimensional histogram constituted by


---
*Page 30*


lbp and local binary differential excitation pattern. IEEE Access 7:145829–145842

Mu H, Zhang M, Qi D, Ni H (2015) The application of rbf neural network in the wood defect detection. Int J


---
*Page 30*


Hybrid Inf Technol 8(2):41–50

Park J, Kim C, Na J, Yi J, Turk M (2008) Using structured light for efficient depth edge detection. Image


---
*Page 30*


Vision Comput 26(11):1449–1465

Rahiddin RNN, Hashim UR, Ismail NH, Salahuddin L, Choon NH, Zabri SN (2020) Classification of wood


---
*Page 30*


defect images using local binary pattern variants. Int J Adv Intell Inform 6(1):36–45

Russakovsky O, Deng J, Su H, Krause J, Satheesh S, Ma S, Bernstein M et al (2015) Imagenet large scale


---
*Page 30*


visual recognition challenge. Int J Comput Vis 115(3):211–252

Sindagi VA, Srivastava S (2015) Oled panel defect detection using local inlier-outlier ratios and modified


---
*Page 30*


lbp. In: 2015 14th IAPR international conference on machine vision applications (MVA), IEEE, pp

214–217

Song W, Chen T, Gu Z, Gai W, Huang W, Wang B (2015) Wood materials defects detection using image


---
*Page 30*


block percentile color histogram and eigenvector texture feature. In: First international conference on

information sciences, machinery, materials and energy, Atlantis Press, pp 779–783

Sugiarto B, Arifin MR, Laluma RH, Prakasa E, Azwar AG et al (2020) An improved wood identification


---
*Page 30*


accuracy using gaussian pyramid and laplacian edge detection based on android smartphone. In: 2020

14th international conference on telecommunication systems, services, and applications (TSSA), IEEE,

pp 1–5

1 3

Wood Science and Technology (2022) 56:477–507


---
*Page 31*


507

Thumm A, Riddell M (2017) Resin defect detection in appearance lumber using 2d nir spectroscopy. Eur J


---
*Page 31*


Wood Wood Prod 75(6):995–1002

Tong H, Ng H, Yap T, Ahmad W, Fauzi M (2017) Evaluation of feature extraction and selection techniques


---
*Page 31*


for the classification of wood defect images. J Eng Appl Sci 12(3):602–608

Urbonas A, Raudonis V, Maskeliūnas R, Damaševičius R (2019) Automated identification of wood veneer


---
*Page 31*


surface defects using faster region-based convolutional neural network with data augmentation and

transfer learning. Appl Sci 9(22):4898

Wang J, Li Q, Gan J, Yu H, Yang X (2019) Surface defect detection via entity sparsity pursuit with intrinsic


---
*Page 31*


priors. IEEE Trans Ind Inform 16(1):141–150

Wells L, Gazo R, Del Re R, Krs V, Benes B (2018) Defect detection performance of automated hardwood


---
*Page 31*


lumber grading system. Comput Electron Agric 155:487–495

Wen W, Xia A (1999) Verifying edges for visual inspection purposes. Pattern Recognit Lett 20(3):315–328

Wenshu L, Lijun S, Jinzhuo W (2015) Study on wood board defect detection based on artificial neural net-


---
*Page 31*


work. Open Autom Control Syst J. https://​doi.​org/​10.​2174/​18744​44301​50701​0290

Yang H, Yu L (2017) Feature extraction of wood-hole defects using wavelet-based ultrasonic testing. J For


---
*Page 31*


Res 28(2):395–402

Yun JP, Lee SJ, Koo G, Shin C, Park C (2019) Automatic defect inspection system for steel products with


---
*Page 31*


exhaustive dynamic encoding algorithm for searches. Opt Eng 58(2):023107

Zhang Y, Davison BD (2019) Modified distribution alignment for domain adaptation with pre-trained incep-


---
*Page 31*


tion resnet. arXiv preprint arXiv:​1904.​02322

Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published

maps and institutional affiliations.

Authors and Affiliations

Lun‑Chi Chen1 · Mayuresh Sunil Pardeshi2 · Win‑Tsung Lo1,2 · Ruey‑Kai Sheu1   ·

Kai‑Chih Pai1 · Chia‑Yu Chen1 · Pei‑Yu Tsai1 · Yueh‑Tiann Tsai3

*	 Ruey‑Kai Sheu

rickysheu@thu.edu.tw

1

Department of Computer Science, Tunghai University, Taichung City, Taiwan (R.O.C.)

2

DDS-THU AI Center, Tunghai University, Taichung City, Taiwan (R.O.C.)

3

Taiwan Sakura Corporation, Taichung City, Taiwan (R.O.C.)

1 3
