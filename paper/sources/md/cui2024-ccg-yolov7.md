# CCG-YOLOv7: A Wood Defect Detection Model for Small Targets Using Improved YOLOv7


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

Date of publication xxxx 00, 0000, date of current version xxxx 00, 0000.

Digital Object Identifier 10.1109/ACCESS.2022.Doi Number

CCG-YOLOv7: A Wood Defect Detection Model

for Small Targets Using Improved YOLOv7

Wenqi Cui1, Zhenye Li1, Anning Duanmu1, Sheng Xue1, Yiren Guo1, Chao Ni1, Tingting Zhu1

and Yajun Zhang1

1College of Mechanical and Electronic Engineering, Nanjing Forestry University, Nanjing, Jiangsu, 210037, China

Corresponding author: Yajun Zhang (e-mail: zhangyj@njfu.edu.cn).

This work was supported in part by the National Scienc Foundation of China, under Grants 62203223, 62006120 and 31570714.

ABSTRACT The Chinese furniture market has a high demand for wood floors. Manual defect detection in

wood floors is inefficient and lacks stability in accuracy. It is necessary to conduct research on automatic

defect detection in wood floors. To improve the accuracy of detecting small defects in wood floors, this paper

proposed a new network based on YOLOv7. The new network is called the cascade center of gravity

YOLOv7(CCG-YOLOv7). This paper designed cascade efficient layer aggregation networks(C-ELAN),

streamlined the CBS, replaced the ELAN with the C-ELAN, introduced the rapid supervised attention module

to connect the backbone and head layers, and simplified the head layer of the YOLOv7 network. These

methods improved the detection accuracy and speed for detecting small defects on wood floor surfaces. The

improved network can effectively detect small defects on the wooden board surfaces, including knots,

scratches, and mildew. Compared to the original YOLOv7, CCG-YOLOv7 improves precision, recall, and

mean average precision by 2.1%, 1.6%, and 1.2%, respectively.

INDEX TERMS deep learning, small target, wood floor defect detection, YOLOv7

I. INTRODUCTION

II. RELATED WORK

Wood floor is a premium and environmentally-friendly

choice for home decoration. In recent year, the demand for

wood floor in furniture market has been steadily growing. Due

to the characteristics of the raw materials, wood floor

inevitably has defects such as knots, scratches, and mildews

during the production process, as shown in Figure 1. These

defects affect the aesthetic appeal and product quality of wood

floor. For businesses, detecting these defects early can avoid

the production of substandard goods, save production costs,

and enhance competitiveness. For consumers, it can improve

product quality and lifespan, thereby increasing consumer

satisfaction. These defects have small and random shapes, and

they are distributed irregularly on the surface of the wood floor,

without any regular pattern. Therefore, accurate identification

of these defects is crucial in the wood floor production process.

Given the nature of wood floor as a commodity, non-

destructive testing methods are commonly used for defect

detection. Traditional non-destructive testing methods for

wood floor defect detection include manual inspection,

electrical testing [1, 2], laser scanning [3, 4], and ultrasonic testing

[5, 6]. However, traditional non-destructive testing methods are

susceptible to environmental influences, expensive in terms of

equipment, and require well-trained operators [7]. More

importantly, the results of the detection are often insufficient

to meet industrial requirements.

With the development of computer technology, more and

more researchers are applying computer vision and deep

learning methods [8, 9, 10] to wood floor defects detection.

Hashim [11] et al. conducted a visual exploratory analysis on

the defects of lauan wood species, and the results showed that

they could significantly distinguish different defect categories.

He [12] et al. designed a hybrid total convolution neural

network (Mix-FCN) for wood defect recognition and

localization and achieved an overall accuracy of 99.13%. Hu

[13] used the Mask R-CNN algorithm in wood defect detection.

The accuracy of defect identification for knots, dead knots,

and insect holes was 99.05%, 97.05%, and 99.10%,

respectively. Shi [14] combined the Mask R-CNN algorithm

with the Glance network and achieved a 98.70% overall

(a)                    (b)                           (c)

FIGURE 1. Images of solid wood floor defects: (a) scratch, (b) live-knot

and dead-knot, (c) mildew

VOLUME XX, 2017

1

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 2*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

classification accuracy and a 95.31% mean average precision.

Mohammad [15] applied Principal Component Analysis (PCA)

technique in wood defect detection, corresponding modeling

and development process was conducted for the PCA

procedure. Silvén [16] et al. implemented unsupervised

clustering methods to detect and identify wood defects. The

achieved false detection and error escape rates are low. Yang

[17] et al. proposed a method for detecting surface defects of

solid wood panels based on a Sigle Shot MultiBox Detector

algorithm. The average detection accuracy of the defects was

89.7%, and the average detection time was 90 ms. Wu [18] et al.

proposed a defect detection method based on affinity

propagation clustering, effectively improving the clustering

speed with an accuracy of 87.68%. Qi [19] et al. proposed a fast

wood defect detection method based on the BP neural network,

achieving an accuracy of 90%. Tu [20] et al. proposed a surface

defects detection method based on improved YOLOv3 for

sawn lumbers. Urbonas [21] et al. employ a pre-trained

ResNet152 neural network model combined with faster R-

CNN to detect surface defects on wooden boards, achieving

an accuracy of 96.1%. Wei-Han Lim [22] et al. proposed a

lightweight object detection model based on the YOLOv4-

Tiny architecture for the detection of four types of wood

defects. The model led to better accuracy and inference speed.

Yutu Yang [23] et al. combined the deep learning feature

extraction

method

and

extreme

learning

machine

classification method to establish a depth extreme learning

machine model for wood image defect detection. The wood

defect recognition accuracy reached 96.72%.


---
*Page 2*


mildews. A live knot is a knot in which the surrounding wood

structure has intact grain continuity and it has not separated

from the surrounding wood. On the other hand, a dead knot is

a knot where the wood tissue has detached from the

surrounding wood. A scratch is a defect that occurs on the

surface of a wood floor during production or transportation.

Unlike cracks, scratches are limited to the surface of the wood

floor and do not result in a complete fracture of the board. The

size of these defects ranges from  40 30



to 60 130



pixels. The defects occupy a relatively small proportion

compared to the entire image. The position of defects in the

images appears randomly. The defects exhibit different shapes.

Figure 2 shows examples of dead knots, live knots, scratches,

and mildews. The dataset used in this study consists of 3473

images. Among these, there are 698 images that contain only

the dead-knots defect, 752 images that contain only the live-

knots defect, 623 images that contain only the scratches defect,

and 522 images that contain only the mildews defect, and 694

images do not contain any defects as negative samples.

Additionally, there are 184 images that contain multiple types

of defects.

FIGURE 2. Common defects of wood floor such as dead-knots, live-

knots, scratches and mildews

TABLE I

WOOD DEFECTS DATASETS

Defects

Classes


---
*Page 2*


In this paper, we propose Cascade Center of Gravity

YOLOv7 (CCG-YOLO) based on the latest YOLOv7 model

to improve the accuracy of wood floor defect detection to

address the issue of YOLO networks being less sensitive to

small objects. Building upon the existing YOLO network, we

have streamlined the CBS, the feature extraction module of the

YOLOv7 backbone, leading the network to focus more on

shallow features and smaller targets. We proposed Center

Efficient Layer Aggregation Networks (C-ELAN) to improve

the performance of original ELAN module in the backbone by

introducing an algorithm named Cascade Center of Gravity

Batch Norm (CCG-BN). CCG-BN is designed to normalize

the centroid of features within the same batch.


---
*Page 2*


Multiple

defects

Dead-knots

698

184

Live-knots

752

Scratches

623

Mildews

522

III. METHODOLOGY


---
*Page 2*


Individual

defects

The proposed Cascade Center of Gravity YOLOv7(CCG-

YOLOv7) is presented in Figure 3. The 3-channel color

images of solid wood floor are divided into squares with the

original height as the edge length. These squares are then

proportionally scaled to form images of size 640 640



. It is

important to note that this operation does not result in any

cutting or cropping of edge defects. Then, 3 pairs of MP1 and

C-ELAN modules are sequentially concatenated, forming the

backbone of the proposed model. It should be noted that the

MP1 module has the same structure as in the original YOLOv7

to half the size and double channel counts of feature maps

while extracting information at different depth. The major

difference lies on the design of the C-ELAN module

combining with the Rapid Supervised Attention Module

(RSAM) that transmits features from paths of the backbone at

multiple scales.


---
*Page 2*


The wood floor images used in this study were captured at

Dehua TB New Decoration Material Co., Ltd. The images

were captured using an LT-400CL 3CMOS RGB line scan

industrial camera. Compared to area scan cameras, line scan

cameras are not only cost-effective but also capable of high-

speed image capture for moving objects, making them suitable

for industrial production lines. Based on the different causes

of wood floor defects, we classify the defects into two

categories: growth defects and processing defects. Generally,

growth defects can be further categorized as dead knots and

live knots, while processing defects include scratches and

VOLUME XX, 2017

7

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 3*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

FIGURE 3. The structure of CCG-YOLOv7

We improved and simplified the head module of the

original YOLOv7, replacing it with outputs only containing


---
*Page 3*


A. BACKBONE


---
*Page 3*


40

40



and 80 80



. Therefore, the novel head we

designed is named Mini-Head. Coordinating with features

from RSAM, the succinct structure in Mini-Head focuses on

small object detection including dead-knots, live-knots,

scratches, and mildews. Below, we will provide a detailed

explanation of the modifications made to the backbone and

head layers in YOLOv7 network.


---
*Page 3*


In the original network, with 4 CBS modules stacked at the

beginning of the backbone, the subsequent ELAN and MP1

modules take in deep features that are not suitable for defects

in solid wood flooring, whose background is wood grain with

a relatively simple texture [24]. Besides, many defects on the

solid wood flooring are of small area, such as dead-knots and

live-knots, leading to a poor recall score when extracted by a

large receptive field from the deep layers. So, we simplified

the network architecture of this part and thus the feature paths

to head are moved to a shallower position. This enables the

network to focus more on shallow features and smaller targets,

thereby improving the efficiency of training and the accuracy

of defect detection.


---
*Page 3*


In Figure 3, the Conv denotes the convolution layer, the BN

denotes the batch normalization layer, and Silu denotes the

activation function. The CBS module consists of a Conv layer,

a BN layer, and a Silu layer, identical to the original YOLOv7.

In Figure 3, "CBS 1×1 1" denotes a 1×1 convolution with a

stride of 1. Similarly, "CBS 3×3 2" indicates a 3×3

convolution with a stride of 2. The Rep module is divided into

train and inference modules. The inference module consists of

a 3×3 convolution with a stride of 1.


---
*Page 3*


Figure 4 and Figure 5 display the overall distribution of

defects in the dataset used in this study. The calculation

VOLUME XX, 2017

7

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 4*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

formulas for  y , width ,and height in the Figure 4 are as

follows:


---
*Page 4*


Image Dataset. In contrast, the targets in general datasets like

ImageNet and COCO are typically located at the center of the

image, showing characteristics of a normal distribution.

Secondly, the wooden floor defect dataset used marks targets

like bad spots and scratches, which have fairly fixed shape

characteristics. While, YOLOv7 network uses predefined

anchor boxes to detect objects of different sizes. Statistical

analysis reveals that the aspect ratio of the bounding boxes is

either close to a 1:1 square or a long and narrow shape greater

than 1:5. Therefore, to leverage the YOLOv7 framework

designed for general object detection, it is necessary to

transform the wooden floor defect data, making it possess

adjustable bounding box distribution and shape characteristics.


---
*Page 4*


dx

x

w

=

(1)

dy

y

h

=

(2)

d

width

width

w

=

(3)

d

height

height

h

=

(4)

Where,  w and  h represent the width and height of the image.


---
*Page 4*


• CCG-BN

We proposed Center Efficient Layer Aggregation

Networks (C-ELAN) to improve the performance of original

ELAN module in the backbone by introducing an algorithm

named Cascade Center of Gravity Batch Norm (CCG-BN).

CCG-BN is designed to normalize the centroid of features

within the same batch. The centroid of the grayscale image is

usually defined as follows:


---
*Page 4*


dx represents the coordinate of the defect in the width

direction, while

dy represents the coordinate of the defect in

the height direction.

d

width represents the width of the defect,

and

d

height represents the height of the defect. Figure 4


---
*Page 4*














=


---
*Page 4*


displays the overall spatial distribution of defects in the dataset.

The heat map uses color intensity to represent the density of

defects in different locations. Darker colors indicate a higher

concentration of defects in that area. Figure 5 shows the

distribution of defect sizes. It can be observed from Figure 5

that the defects on the surface of the wooden floor are very

small in size. As can be seen in Figure 4, in the dataset used in

this study, the distribution of wood floor defects is random

across the entire image, and the proportion of defective pixels

in the entire image is relatively small. It should be noted that

the coordinates in the heatmaps of Figure 4 and Figure 5 are

relative coordinates.


---
*Page 4*





---
*Page 4*


in i j

i

j


---
*Page 4*


w

h

=

=


---
*Page 4*


, ,

1

1


---
*Page 4*


i


---
*Page 4*


F

cx


---
*Page 4*





---
*Page 4*


w

h

F


---
*Page 4*


(5)

in i j

i

j


---
*Page 4*


=

=


---
*Page 4*


, ,

1

1













=


---
*Page 4*





---
*Page 4*


in i j

j

i

h

w


---
*Page 4*


h

w

, ,

1

1


---
*Page 4*


j


---
*Page 4*


F

cy


---
*Page 4*


=

=




---
*Page 4*


F


---
*Page 4*


(6)

Where,

, ,

in i j

F

is the grayscale value of the pixel at coordinates


---
*Page 4*


in i j

j

i


---
*Page 4*


=

=


---
*Page 4*


, ,

1

1

(

)

,i j in the image, in which i is the coordinate in the width

1.0


---
*Page 4*


direction, and j is the coordinate in the height.

cx and

cy are

the coordinates of the gravity of center along the axes of width

and height of the image. For color images, we succinctly

define the centroid as a linear combination of the centroid

coordinates in the 3 channels. We vectorize the original

centroid formula for the image to facilitate parallel

acceleration of computations:


---
*Page 4*


0.9

0.8

0.7

0.6

y


---
*Page 4*


0.5

0.4

0.2


---
*Page 4*


0.3

(3 )

3

3

flatten (

)

s

s

s s

flattened

in





=

F

F

(7)


---
*Page 4*


0.1

x

0.1

0.2

0.3

0.4

0.5

0.6


---
*Page 4*


1.0

0.7

0.8

0.9

Rm

Rn

Rm

F

S

Rm


---
*Page 4*




=


























---
*Page 4*


1


---
*Page 4*





---
*Page 4*


s

FIGURE 4. Heatmap of defect location distribution

1.0


---
*Page 4*


2 3

2

(3 )

2,4

1 3

1


---
*Page 4*











---
*Page 4*


s

s

s

flattened

s


---
*Page 4*


2

flatten


---
*Page 4*


1


---
*Page 4*


(8)

0.9

0.8


---
*Page 4*


2 3

3 1

c


---
*Page 4*








=












---
*Page 4*


x


---
*Page 4*


Rn

w

(9)

height


---
*Page 4*


0.7

0.6

Where,

1 3

1

1

1

r

g

b


---
*Page 4*








= 













S

,

2

1 1

1

1

2


---
*Page 4*


y


---
*Page 4*


c







= 







Rm

,


---
*Page 4*


0.5

0.4


---
*Page 4*


s

s


---
*Page 4*


0.3

0.2


---
*Page 4*


1

1

s



Rm

is a row vector consisting of all elements in the first


---
*Page 4*


0.1

width

0.1

0.2

0.3

0.4

0.5

0.6


---
*Page 4*


1.0

0.7

0.8

0.9


---
*Page 4*


row of matrix.

2 s



Rm

and

1

2

s



Rm

is a row vector consisting of

3 1



w

is a

learnable parameter used for linear transformation of the

centroid coordinates in each channel, resulting in the


---
*Page 4*


FIGURE 5. Heatmap of defect size statistics.

The defection distribution of solid wood floor is quite

different from that of objects in public datasets, lettuce pallets


---
*Page 4*


all elements in the second row of matrix

2 s



Rm

.

VOLUME XX, 2017

7

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 5*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

computation of the centroid position of the color image. The

matrix

3

s s

in


---
*Page 5*




F

is a three-channel color image for which the

centroid is to be computed. The function

3

flatten represents

the flattening of the third channel dimension, resulting in a

two-dimensional matrix that contains only the first and second

channels. The function


---
*Page 5*


2,4

flatten

represents the flattening of

the second channel and the fourth channel dimension,

resulting in a two-dimensional matrix where the second

channel is merged into the first channel of the matrix, and the

fourth channel is merged into the third channel. Based on the

above analysis, we have designed a method to shift the

centroid of the image by transforming pixel values. This

method includes learnable parameters that can specify the

position of the image centroid after the shift, allowing the

image features to automatically adjust during the training

process as needed by the network. The algorithm for centroid

shift is as follows:


---
*Page 5*


FIGURE 6. Structure of C-ELAN

The input 3-dimensional feature flows through a

convolutional layer with 3 3 c

 kernel size, which keeps the

size and channels unchanged. Then, it is normalized by CCG-

BN and SiLU activation function. In the C-ELAN module,

R2Us are used to route gradients to 2 different paths: the

forward path and the residual path. Adjusting the gradient

propagation path enhances the effective utilization of network

parameters, and enables different computational units to learn

diverse information, thereby achieving higher parameter

utilization efficiency. Then, the feature map is fed to an

identical structure, and the new output is aggregated with the

residual output of the previous R2U module to form a residual

feature with twice the number of channels.


---
*Page 5*


(

)

, ,

1

1

,

, ,

1

2


---
*Page 5*


F

F

F

(10)


---
*Page 5*


c

c

in i j

i

j

out i

in i j


---
*Page 5*


=

=



−

=

+


---
*Page 5*


x

x


---
*Page 5*


w

h

hwx

h


---
*Page 5*


−

F

F

F

(11)


---
*Page 5*


(

)

, ,

1

1

,

, ,

1

2


---
*Page 5*


c

w

h

c

c

in i j

i

j

out j

in i j


---
*Page 5*


=

=



−

=

+


---
*Page 5*


y

y


---
*Page 5*


Simultaneously, another 2 convolution layers with kernel

size of

(

)

3 3

/ 2

c



and paddings of 1 perform channel


---
*Page 5*


hwy

w


---
*Page 5*


c


---
*Page 5*


−


---
*Page 5*


compression on the input feature. This operation generates 2

independent outputs with a half channel number. The presence

of the above-mentioned strategy ensures that the learning

capability of C-ELAN is stable enough to avoid degradation

during training. The reason is that the gradient directly

determines and propagates information to update the weights

in each branch. Finally, the features from the 3 branches and

the residual-aggregated features from each R2U module are

stacked together to form a feature map with four times the

number of channels. Then, a 3 3



convolutional layer with a

stride of 2 is applied to obtain an output with a reduced spatial

size compared to the input features, while doubling the

number of channels.


---
*Page 5*


,

,

out

out i

out j

=

+

F

F

F

(12)

Where,

,

out i

F

represents

the

feature

after

centroid

normalization in the width direction,

,

out j

F

is the feature after

centroid normalization in the height direction, and

out

F

is the

output of the module.

cx  and

cy  are learnable parameter

vectors, each containing scalars equal to the number of input

feature channels.


---
*Page 5*


• C-ELAN

In the YOLOv7 network, the Enhanced Local Attention

(ELAN) layer is a special attention mechanism used to

w   ’              f         g    . The ELAN

layer adjusts the weights of feature maps adaptively,

increasing the focus on regions of interest and improving the

accuracy of object detection. To improve the detection

accuracy of small target defects in the YOLO network, it is

necessary to enhance the depth of the ELAN layer. Therefore,

we propose the Center Efficient Layer Aggregation Networks

(C-ELAN) layer.


---
*Page 5*


Concatenation and Bottleneck Structure (CBS) layer plays

a role in feature fusion and dimension adaptation between the

backbone and head layers. The CBS layer first concatenates

the feature maps from the backbone layer and the head layer

along the channel dimension to achieve feature fusion across

different scales. Then, it reduces the number of channels in the

feature maps using a bottleneck structure, which helps to

reduce the computational complexity. To improve the

detection speed of YOLOv7 network for small target defects,

it is necessary to introduce channel attention mechanism to

adaptively adjust the weights of feature map channels.

Therefore, we replaced the CBS module with the Rapid

Supervised Attention Module (RSAM) to achieve this.


---
*Page 5*


B. HEAD

The C-ELAN is designed as a feature exactor that bring the

output to larger receptive field and deeper-level features. The

C-ELAN module is presented in Figure 6. As shown in Figure

6, the C-ELAN module consists of 13 convolutional layers, 2

SiLU activation layers, 2 ReLU activation layers, 2 CCG-BN

layers, and 2 stacking computation along the axis of the

channels. The number of feature channels is doubled when it

flows to the output layer.


---
*Page 5*


Rapid Supervised Attention Module is designed to transfer

features from the backbone layer to the mini-head layer at

multiple scales. Rapid Supervised Attention Module (RSAM)

VOLUME XX, 2017

7

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 6*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

improves upon the Multi-Stage Progressive Image Restoration

(MRPNet), proposed by Zamir [25] et al. The Supervised

Attention Module (SAM) used in MRPNet to pass features to

the next stage includes the Locally Supervised Predictions

(LSP) structure for generating attention maps, appropriately

suppressing features with smaller amounts of information in

the current stage. The SAM structure is shown in Figure 7 The

input is the image input feature


---
*Page 6*


g

h w c



F

from the previous stage,

where h and w are its height and width, and c is the number

of channels. At the same time, SAM takes a low-quality

(Degraded) image input

3

h w

degarded


---
*Page 6*


,

SAM in

FIGURE 8. Structure of RSAM



F

, which, when added to the


---
*Page 6*


In the YOLOv7 network, the role of the head layer is to

process the feature maps extracted from the backbone layer

and output the final detection results. The head layer consists

of a series of convolutional layers and fully connected layers,

responsible for transforming the feature maps into predicted

bounding boxes, class probabilities, and confidences. To make

it focus more on shallow-level features and smaller objects, we

need to decrease the depth of the head layer.


---
*Page 6*


convoluted


---
*Page 6*


h w c



F

, computes the repaired image and

calculates the loss function. To introduce features into the next

stage, a 1 1

 pointwise 2D convolution is used to transform

the repaired image, and an image attention map is calculated

using the Sigmoid function. This is then multiplied by


---
*Page 6*


,

SAM in

h w c



F


---
*Page 6*


,

SAM in


---
*Page 6*


We simplified the head layer to the mini-head layer,

allowing it to focus more on shallow features and smaller

targets, thereby improving the efficiency of training and the

accuracy of defect detection. As shown in Figure 9, the grid of


---
*Page 6*


to apply the attention map, and finally, the residual structure

of


---
*Page 6*


h w c



F

is adopted to form the LSP structure, outputting the

image output feature

,

h w c

SAM out


---
*Page 6*


,

SAM in



F

required for the next stage. The


---
*Page 6*


20

20



is deleted from the original head, making it less

complex and more effective. The output of the head is

refactored to 2 different features with size of 80 80 9 3





and 40 40 9 3





, to speed up the inference speed of the

model. Each of the features consists of information of the

detected defects, including the grid shape, 3 bounding boxes

(height, width, and center coordinates), defect type, and

confidence score. With the elimination of the 20

20



output

and its associated output structure from the original YOLOv7,

the parameter count in the head is reduced by 72% compared

to its original value. This optimization has significantly

improved the efficiency of our modified YOLOv7 network for

the task of defect detection in solid wood floor.


---
*Page 6*


structure of RSAM is shown in Figure 8. Compared to SAM,

RSAM replaces the image feature


---
*Page 6*


h w c



F

, therefore, it


---
*Page 6*


,

,1

RSAM in

directly adds the input feature matrix


---
*Page 6*


h w



F

to reduce one


---
*Page 6*


RSAM in


---
*Page 6*


,

,2

3

convolution that reduces the number of channels. The size of

the convolution kernel on the path from


---
*Page 6*


h w



F

to

,

h w c

SAM out


---
*Page 6*


3


---
*Page 6*




F

is

1, with both stride and padding set to 1, so the size and channel

count of the output from this convolution layer are consistent

with the input. Another convolution layer on the lower path in

the figure has the same parameters as the aforementioned

convolution, and the size of its output feature also satisfies


---
*Page 6*


RSAM in


---
*Page 6*


,

3

h

w



. Since the input feature


---
*Page 6*


h w



F

undergoes one less


---
*Page 6*


RSAM in


---
*Page 6*


,


---
*Page 6*


3

convolution, if the output features

3

,

h w

RSAM out


---
*Page 6*




F

is output directly

after the first sum, there would be no learnable parameters in

the RSAM structure. Hence,


---
*Page 6*




F

is used directly as the


---
*Page 6*


3

,

h w

RSAM out

output features. The parameter count of RSAM is

approximately 2.5% of the SAM with an 80-channel input

using the same convolution kernel size, which is why it is

called the Rapid Supervised Attention Module.

g


---
*Page 6*


FIGURE 9. Structure of mini-head

IV. RESULT & DISCUSSION

A. TRAINING STRATEGIES

FIGURE 7. Structure of SAM


---
*Page 6*


During the training process of the CCG-YOLOv7 network,

we utilized the data augmentation technique of copy-pasting a

small object into various positions in an image to create new

annotated samples, which helps improve the model's ability to

detect small defects and does not result in an increase in the

number of training samples. The pasted small object can

undergo scaling, flipping, rotation, and other random

VOLUME XX, 2017

7

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 7*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

transformations. This method increases the contribution of

small objects to the loss calculation during training by

increasing the number of small objects in each image and

matching anchor boxes. To enhance the robustness and

generalization ability of the model, we adopt this data

augmentation technique during the model training process.

The training hyperparameters in the experiment are shown in

Table2.

TABLE2

THE TRAINING HYPERPARAMETERS IN THE EXPERIMENT

Hyperparameters

Value

Epoch

300

Initial learning rate

0.01

Batch size

8

Momentum

0.913

Wight decay

0.0005

Loss function

BCE, CIoU


---
*Page 7*


(a)


---
*Page 7*


(b)

(d)


---
*Page 7*


(c)


---
*Page 7*


B. EXPERIMENT of SOME METHODS AppLYING to

YOLOv7

To build and test the proposed defect detection model, the

collected dataset of 3473 wood floor images were divided into

three parts: training set, testing set, and validation set, in a ratio

of 3:1:1. The training set is used to train the constructed

network, the testing set is used to evaluate the network, and

the validation set is used for final assessment. The training

platform specifications are presented in Table 3.


---
*Page 7*


FIGURE 10.

The training process of the different methods

introduced into YOLOv7(a) YOLO-RSAM result, (b) YOLO-C-ELAN

result, (c) YOLO-NC result, (d) YOLO-mini-head.

In Figure. 10, YOLO-RSAM represents the independent

integration of the RSAM module into the YOLO network.

YOLO-C-ELAN indicates the replacement of all ELAN

modules in the original YOLO network with C-ELAN

modules. YOLO-NC signifies the simplification of the

backbone layer by removing four CBS modules. YOLO-mini-

head denotes the replacement of the head layer in the original

YOLO network with the mini-head. Also, Precision(P),

Recall(R), and mean average precision (mAP) are selected as

the main evaluation indexes which are defined as follows:


---
*Page 7*


TABLE 3

HARDWARE AND SOFTWARE PARAMETERS OF THE EXPERIMENTAL

ENVIRONMENT.

Name

Parameter

Memory

32.00 GB

CPU

Intel Core i7-8700 CPU


---
*Page 7*


TP

Precision

TP

FP

=

+


---
*Page 7*


@3.2GHz

Graphics card

NVIDLA GeForce RTX


---
*Page 7*


(13)

3080 Ti

System

Windows 10

Environment

Configuration


---
*Page 7*


Re

TP

call

TP

FN

=

+


---
*Page 7*


(14)

1.14.0, Pytorch


---
*Page 7*


Python3.6, TensorFlow-GPU


---
*Page 7*


1


---
*Page 7*


N


---
*Page 7*


i

i

mean Average Precision

AP

N

=

=



(15)


---
*Page 7*


In order to improve the detection performance of the

YOLOv7 model, several methods that may affect the detection

performance were employed. A comparison was made

between these methods and the original YOLOv7 model to

observe whether these methods had a positive effect on

enhancing the detection performance of YOLOv7. Figure 10

displays the variation curves of the network training loss and

validation loss after training and testing under the same

conditions.


---
*Page 7*


Where, TP refers to the number of samples where positive

samples are correctly classified; FP means the number of

negative samples which are correctly classified as negative,

and FN indicates the number of positive samples which are

incorrectly classified as negative. AP is the area abounded

by the

Re

Precision

call

−

curve which represents the

detection accuracy of one kind of wood floor defects.


---
*Page 7*


1

mean Average Precision (mAP) refers to the overall

detection accuracy of all defects categories. As shown in

Figure 8, during the training of 200 epochs, the loss curves of

all the aforementioned models on the validation set and

training set become relatively flat, indicating that the model

training has converged.

VOLUME XX, 2017

7

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 8*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

TABLE 4

THE COMPARISON OF CLASSICAL ALGORITHMS.

Methods

𝑃(%)

𝑅(%)

𝑚𝐴𝑃(%)

SSD

75.6

76.4

77.5

Faster R-


---
*Page 8*


compared to other classical algorithms, the YOLOv7

demonstrates superior performance in wood floor defect

detection.

CNN


---
*Page 8*


87.6

87.7

87.9


---
*Page 8*


C. ABLATION EXPERIMENT

We conducted an ablation experiment to investigate

whether the fusion of these modules could further enhance the

performance of the YOLOv7 network. Using the original

YOLOv7 network as the baseline, we introduced RSAM,

mini-head, and C-ELAN in separate experiments. The results

of this experiment are presented in Table 5.


---
*Page 8*


YOLOv5

89.3

90.7

90.9

YOLOv6

89.7

91.4

91.5

YOLOv7

90.6

93.2

93.6

We conducted comparative experiments with some classic

detection networks. From Table 4, it can be observed that

TABLE 5

ABLATION EXPERIMENT OF RSAM, MINI-HEAD, NC AND C-ELAN

RSAM

C-ELAN

mini-head

NC

𝑃(%)

𝑅(%)

𝑚𝐴𝑃(%)

T(ms)

90.6

93.2

93.6

38

√

91.8

93.4

93.9

37

√

90.7

93.5

93.7

25

√

91.5

93.7

94.2

41

√

90.7

93.3

93.8

23

√

√

90.5

89.9

91.2

25

√

√

89.3

91.7

92.4

29

√

√

√

90.8

93.7

94.1

29

√

√

√

√

92.7

94.8

94.8

19

In the table 5, T represents the average detection time for

100 images, measured in milliseconds. From the table, it can

be observed that the detection accuracy improves when NC

and C-ELAN modules are individually integrated into the

network. Additionally, the detection speed significantly

increases when the RSAM module is integrated with the mini-

head into the network. However, the introduction of mini-head

and NC results in a decrease of 0.1% in P, 3.3% in R, and 1.4%

in mAP. The introduction of mini-head and C-ELAN results

in a decrease of 1.3% in P, 1.5% in R, and 1.2% in mAP. The

mini-head is composed of a series of convolutional and fully

connected layers, responsible for transforming the feature map

into predicted bounding boxes, class probabilities, and

confidence scores. In comparison to the original head layer,

the mini-head layer eliminates the 20

20



grid, which

includes detected defect information. Therefore, when the

backbone focuses too much on either shallow or deep image

features, the network's detection accuracy decreases. With the

integration of C-ELAN, NC, and the mini-head into the

network, both the detection accuracy and speed have been

improved.

Further

introducing

RSAM

resulted

an

improvement of 2.1% in P, 1.6% in R, and 1.2% in mAP. And

detection speed of the network improves to 19ms. This is

because the RSAM module adaptively adjusts the weights of

the feature map channels, connecting the feature maps

between the backbone and the mini-head layer, achieving

feature fusion across different scales. Therefore, we choose to

apply RSAM, C-ELAN, mini-head, and NC to the YOLO

network based on these results. The figure 11 shows the curves

of YOLOv6, YOLOv7 and CCG-YOLOv7.


---
*Page 8*


FIGURE 11.

curve diagram of the evaluation index

D. EXPERIMENT UNDER DIFFERENT LIGHT CONDITION

In industrial production processes, continuous and

prolonged operation can cause a decrease in the intensity of

the light source. We defined the illuminance range of 4600 lux

- 6100 lux as strong lighting, 4400 lux - 4600 lux as moderate

lighting, and 3300 lux - 4400 lux as weak lighting. The

numbers of images captured under strong, weak, and moderate

lighting conditions were 98, 103, and 112, respectively. These

images were utilized to evaluate the detection performance of

the CCG-YOLOv7 network under diverse lighting conditions.

These images, taken under different light intensities, feature

defects like knots, scratches, and mildews, with only a few

defects presented in each image. The experiments were

conducted using the images under different lighting conditions.

The experimental results are presented in Table 7. Figure 11

showcases partial visual results of wood floor defect detection

under different lighting conditions using the CCG-YOLOv7

model.

VOLUME XX, 2017

7

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 9*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

TABLE 6

THE DETECTION RESULTS OF CCG-YOLOV7 AND FASTER R-CNN UNDER


---
*Page 9*


The numbers of images captured under small, big, and normal

tilt angle conditions were 63, 87, and 78, respectively. These

images were utilized to evaluate the detection performance of

the CCG-YOLO network under different tilt angle conditions.

These images, taken under different tilt angle, feature defects

like knots, scratches, and mildews, with only a few defects

presented in each image. Table 7 presents the experimental

results for detecting skewed images.


---
*Page 9*


DIFFERENT TILT ANGLE CONDITIONS.

Base

Model


---
*Page 9*


Light

Condition


---
*Page 9*


𝑃(%)

𝑅(%)

𝑚𝐴𝑃(%)

CCG-

YOLOv7


---
*Page 9*


Weak

92.0

94.3

94.4

Normal

92.1

94.3

94.5

Strong

92.1

94.2

94.5

Faster

R-CNN


---
*Page 9*


Weak

86.9

86.9

87.1

Normal

87.6

87.7

87.9

Strong

87.1

87.3

87.4

As shown in Table 6, when using images captured under

strong lighting conditions for detection, the CCG-YOLOv7

model exhibited no decrease in P and mAP, with a slight

decrease of 0.1% in R. However, when using images captured

under weak lighting conditions for detection, the CCG-

YOLOv7 model showed a decrease of 0.1% in P and mAP,

with no decrease in R. From the results in Table 8, it can be

observed that the proposed CCG-YOLOv7 model achieves

high detection accuracy under different lighting conditions.

Compared with the Faster R-CNN, the CCG-YOLOv7 model

possesses sufficient robustness to detect wood floor defects

under varying lighting conditions, enabling prolonged

industrial production.


---
*Page 9*


TABLE 7

THE DETECTION RESULTS OF CCG-YOLOV7 UNDER DIFFERENT TILT

ANGLE CONDITIONS.

Base

Model


---
*Page 9*


Tilt

Angle


---
*Page 9*


𝑃(%)

𝑅(%)

𝑚𝐴𝑃(%)

Small

92.1

94.3

94.4

Normal

92.1

94.3

94.5

Big

92.0

94.1

94.2

As shown in Table 7, when using images with smaller tilt

angles for detection, the CCG-YOLOv7 model exhibited no

decrease in precision and recall, with a slight decrease of 0.1%

in mAP. However, when using images with larger tilt angles,

the RDEYOLOv7 model showed a decrease in precision,

recall, and mAP by 0.1%, 0.2%, and 0.3% respectively. The

experimental results indicate that the impact of image tilt angle

on the CCG-YOLOv7 model is negligible and can be

disregarded.


---
*Page 9*


CCG-

YOLOv7

(a)


---
*Page 9*


(a)

(b)


---
*Page 9*


(b)

(c)


---
*Page 9*


(c)

FIGURE 12.

The visualization results of detecting wood floor

defects under different light conditions by using the CCG-YOLOv7

model:(a) weak light, (b) normal light, (c) strong light


---
*Page 9*


FIGURE 13.

The detection results of images with different tilt

angle by using the CCG-YOLOv7. Conditions: (a)big tilt angle, (b)small

tilt angle, (c) normal tilt angle.

E. EXPEIMENT UNDER DIFFERENT TILT ANGLE

To validate the tolerance of CCG-YOLO to skewed

images during the wood floor sorting process, we selected

images with different tilt angles from the test set for testing.


---
*Page 9*


V. CONCLUSION

This study proposes a wood floor defect detection method

called CCG-YOLOv7, which can accurately detect small

defects on the surface of wood floors. YOLOv7 introduces

8

VOLUME XX, 2017

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 10*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

RSAM, mini-head, and C-ELAN to replace the CBS

modules connecting the backbone and head layers, as well as

the head layer and ELAN, resulting in improved detection

performance. It has been demonstrated that CCG-YOLOv7

can increase P, R, and mAP by 2.1%, 1.6%, and 1.2%,

respectively. CCG-YOLOv7 is constructed by incorporating

C-ELAN, RSAM, mini-head, and removing certain CBS

modules in YOLOv7. Through the analysis of experimental

results, the following findings are obtained: Compared to the

original YOLOv7, CCG-YOLOv7 improves P, R, and mAP

by 2.1%, 1.6%, and 1.2%, respectively. CCG-YOLOv7 also

demonstrates good performance in detecting wood floor

surface defects under different lighting conditions, which is

of

significant

importance

in

industrial

production.

Furthermore, CCG-YOLOv7 is capable of detecting surface

defects on inclined images. The experiments confirm that the

proposed CCG-YOLOv7 method is effective for wood floor

defect detection.


---
*Page 10*


[14] Shi, Jiahao, et al. "Defect detection of industry wood veneer based on

NAS and multi-channel mask R-CNN." Sensors 20.16 (2020): 4398.

[15] Tafarroj, Mohammad Mahdi, et al. "An application of principal

component analysis method in wood defects identification." Journal

of the Indian Academy of Wood Science 11 (2014): 33-38.

[16] Silvén, Olli, Matti Niskanen, and Hannu Kauppinen. "Wood

inspection with non-supervised clustering." Machine Vision and

Applications 13 (2003): 275-285.

[17] Yang, Yutu, et al. "Surface detection of solid wood defects based on

SSD improved with ResNet." Forests 12.10 (2021): 1419.

[18] Wu, Dong-yang, and Ning Ye. "Wood defect recognition based on

affinity propagation clustering." 2010 Chinese Conference on Pattern

Recognition (CCPR). IEEE, 2010.

[19] Qi, Dawei, Peng Zhang, and Lei Yu. "Study on wood defect detection

based on artificial neural network." 2008 IEEE Conference on

Cybernetics and Intelligent Systems. IEEE, 2008.

[20] Tu, Yaxin, et al. "An accurate and real-time surface defects detection

method for sawn lumber." IEEE Transactions on Instrumentation and

Measurement 70 (2020): 1-11.

[21] Urbonas, Augustas, et al. "Automated identification of wood veneer

surface defects using faster region-based convolutional neural network

with data augmentation and transfer learning." Applied Sciences 9.22

(2019): 4898.

[22] Lim, Wei-Han, Mohammad Babrdel Bonab, and Kein Huat Chua.

"An optimized lightweight model for real-time wood defects

detection based on yolov4-tiny." 2022

IEEE

International

Conference on Automatic Control and Intelligent Systems

(I2CACIS). IEEE, 2022.

[23] Yang, Yutu, et al. "Wood defect detection based on depth extreme


---
*Page 10*


ACKNOWLEDGMENT

This research was supported by the National Natural

Science Foundation of China, under Grants 62203223,

62006120 and 31570714.


---
*Page 10*


learning machine." Applied Sciences 10.21 (2020): 7488.

[24] Wang, Chien-Yao, Alexey Bochkovskiy, and Hong-Yuan Mark Liao.

REFERENCES

[1] Mohammadabadi, Ali, and Roberto Dugnani. "Detection of wood


---
*Page 10*


"YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-

time object detectors." Proceedings of the IEEE/CVF Conference on

Computer Vision and Pattern Recognition. 2023.

[25] Zamir, Syed Waqas, et al. "Multi-stage progressive image


---
*Page 10*


defects

using

low

acoustic

impedance-based

PZT

transducers." Journal of the Indian Academy of Wood Science 17.2

(2020): 107-113.

[2] Radwan, Mohamed, et al. "In-Line Wood Defect Detection Using


---
*Page 10*


restoration." Proceedings of the IEEE/CVF conference on computer

vision and pattern recognition. 2021.


---
*Page 10*


Simple Scalar Network Analyzer." Sensors 22.23 (2022): 9495.

[3] Ai, Zhijie, et al. "Wood Broken Defect Detection With 3D Laser


---
*Page 10*


Wenqi Cui received the B.S. degrees in

College

of

Mechanical

and

Electronic

Engineering, Nanjing Forestry University,

Nanjing, China in 2020, where he is currently

pursuing the M.S. degree. His research

interests include the application of intelligent

algorithms in industry, image data processing,

and time series prediction.


---
*Page 10*


Scanning." 2022 China Automation Congress (CAC). IEEE, 2022.

[4] Yang, Yutu, et al. "Detection system for U-shaped bellows

convolution pitches based on a laser line scanner." Sensors 20.4

(2020): 1057.

[5] Hilbers, Ulrich, et al. "Observation of interference effects in air-

coupled ultrasonic inspection of wood-based panels." Wood science

and technology 46 (2012): 979-990.

[6] Tiitta, M., et al. "Air-coupled ultrasound detection of natural defects

in wood using ferroelectret and piezoelectric sensors." Wood Science

and Technology 54 (2020): 1051-1064.

[7] Fang, Yiming, et al. "Review of the use of air-coupled ultrasonic


---
*Page 10*


Zhenye LI was born in Yangzhou, Jiangsu, China

in 1997. He graduated from Nanjing Forestry

University in 2019 and obtained a bachelor's degree

in engineering. He is currently pursuing a master's

degree at Nanjing Forestry University. His research

interests include the application of intelligent

algorithms in industry, image data processing and

hyperspectral analysis.


---
*Page 10*


technologies for nondestructive testing of wood and wood

products." Computers and electronics in agriculture 137 (2017): 79-

87.

[8] Quan, Yu, et al. "Object Detection Model Based on Deep Dilated

Convolutional Networks by Fusing Transfer Learning." IEEE

Access 7 (2019): 178699-178709.

[9] Li, Wei, et al. "Causal-ViT: Robust Vision Transformer by causal

intervention." Engineering Applications of Artificial Intelligence 126

(2023): 107123.

[10] Chen, Shengjia, Zhixin Li, and Zhenjun Tang. "Relation r-cnn: A


---
*Page 10*


Dr. Author was a recipient of the International

Association of Geomagnetism and Aeronomy

Young Scientist Award for Excellence in 2008, and

the IEEE Electromagnetic Compatibility Society Best Symposium Paper

Award in 2011.


---
*Page 10*


graph based relation-aware network for object detection." IEEE Signal

Processing Letters 27 (2020): 1680-1684.

[11]       ,          ’  ,      . "                                     f

texture features on images of timber defect." Advanced Science

Letters 24.2 (2018): 1104-1108.

[12] He, Ting, et al. "Application of deep convolutional neural network on

feature extraction and detection of wood defects." Measurement 152

(2020): 107357.

[13] Hu, Kai, et al. "Defect identification method for poplar veneer based

on progressive growing generated adversarial network and MASK R-

CNN Model." BioResources 15.2 (2020): 3041-3052.

8

VOLUME XX, 2017

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
*Page 11*


This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and

content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3352445

Duanmu Anning holds a Bachelor's degree in

Mechanical and Electronic Engineering from

Nanjing Forestry University and is currently

pursuing a Master's degree in Control Science and

Engineering at Nanjing Forestry University. His

research interests include computer vision, deep

learning, and image processing. In this study, he

was responsible for proofreading the manuscript.


---
*Page 11*


Yajun Zhang is a Lecturer of School of

Mechanical and Electronic Engineering, Nanjing

Forestry University, Nanjing, China. He received

his Ph.D. and M.S., degrees in Control Science

and Engineering

from Southeast University in 2021 and Donghua

University in 2017, respectively, and the B.S.

degree in Electrical Engineering from Shanghai

Institute of Technology in 2014. His research

areas include production systems control, supply

chain management, and deep Learning.


---
*Page 11*


Sheng XUE was born in Huaian, Jiangsu, China, in

000.                         ’    g

engineering from Nanjing Forestry University, in

0  , w                            g           ’

degree. His research interests include the application

of intelligent algorithms in industry and image data

processing.

Yiren Guo received the B.S. degrees in College of

Mechanical and Electronic Engineering, Nanjing

Forestry University, Nanjing, China in 2020, where

he is currently pursuing the M.S. degree. His

research interests include the application of

intelligent algorithms in industry, image data

processing, and time series prediction.


---
*Page 11*


Chao Ni was born in Nanjing, Jiangsu, China in

1979. He received the B.S. degree in automation

from

Nanjing

University

of

Science

and

Technology, Nanjing, in 2001 and the Ph.D.

degree in control theory and control engineering

from Southeast University, Nanjing, China, in

2008. He is currently an Associate Professor with

Automation

Department,

Nanjing

Forestry

University, China. From Oct. 2017 to Nov. 2018,

he was a visiting scholar to University of Maryland,

College Park, USA. His research interests include

artificial intelligence in industrial application, data processing, and

spectroscopy analysis.

Tingting Zhu is working in College of Mechanical

and Electronic Engineering, Nanjing Forestry

University, China. Her Ph.D. degree is in pattern

g               ﬁ            g     f            f

Automation, Southeast University, in 2019. She

achieved a fellowship jointly awarded by the Fonds

de Recherche du Quebec—Nature et Technologies

(FRQNT) and the China Scholarship Council and

studied as a visiting student at department of

Atmospheric and Oceanic Sciences, in McGill

University, Canada, from 2017 to 2018. Her current

research interests include machine learning, data processing and modeling,

renewable energy generation forecast, climate feedback.

8

VOLUME XX, 2017

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4
