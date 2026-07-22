# PEER-REVIEW ARTICLE


PEER-REVIEWED ARTICLE

bioresources.com

Accurate and Automated Detection of Surface Knots on

Sawn Timbers Using YOLO-V5 Model

Yiming Fang,a,b,c Xianxin Guo,a Kun Chen,a,* Zhu Zhou,b and Qing Ye c

Knot detection is a challenging problem for the wood industry. Traditional

methodologies depend heavily on the features selected manually and

therefore were not always accurate due to the variety of knot appearances.

This paper proposes an automated framework for addressing the

aforementioned problem by using the state-of-the-art YOLO-v5 (the fifth

version of You Only Look Once) detector. The features of surface knots

were learned and extracted adaptively, and then the knot defects were

identified accurately even though the knots vary in terms of color and

texture. The proposed method was compared with YOLO-v3 SPP and

Faster R-CNN on two datasets. Experimental results demonstrated that

YOLO-v5 model achieved the best performance for detecting surface knot

defects. F-Score on Dataset 1 was 91.7% and that of Dataset 2 was up to

97.7%. Moreover, YOLO-v5 has clear advantages in terms of training

speed and the size of the weight file. These advantages made YOLO-v5

more suitable for the detection of surface knots on sawn timbers and

potential for timber grading.

Keywords: Defect detection; Surface knots; Sawn timber; YOLO-v5

Contact information: a: School of Mechanical & Electrical Engineering, Shaoxing University, Shaoxing

312000, P. R. China; b: School of Information Engineering, Zhejiang A & F University, Hangzhou 311300,

P. R. China; c: Suncha Bamboo & Wood Technology Co. Ltd., Lishui 323899, P. R. China;

* Corresponding author: kchen@usx.edu.cn

INTRODUCTION

Knots are remnants of branches found in sawn timber and have widely been

considered as defects for timber grading (Qu et al. 2019). First, knots cause deviations in

the fiber direction and significantly reduce the mechanical properties, such as Young’s

modulus, shear modulus, etc. (Sarnaghi and Kuilen 2019). Second, the appearance of knots

may bend the wood grain, thus, aesthetically making the wooden product unattractive to

view. Finally, knots are susceptible to splitting during manufacturing, causing an uneven

break in finishing (Wells et al. 2018). Therefore, knot determination and classification are

critically important for either sorting the timber and optimizing it for further processing, or

predicting the mechanical properties (Longuetaud et al. 2012; Hittawe et al. 2015).

Computer vision techniques are a promising tool for knot detection. There are

numerous studies regarding the surface inspection of sawn timbers. Kamal et al. (2017)

and Urbonas et al. (2019) reviewed the related work from the technological standpoint.

The existing methods varied greatly from the different input images, but two common steps

can be highlighted. The first was feature extraction. Knots have a slightly darker color and

torn grain.

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5390

PEER-REVIEWED ARTICLE

bioresources.com

Various techniques, such as gray level cooccurrence matrix (GLCM) (Hu et al.

2011; Hashim et al. 2016), Gabor filter (Pölzleitner 2003; Hittawe et al. 2015), local binary

pattern (LBP) analysis (Silvén et al. 2003; Zhang et al. 2008), etc., have been employed to

extract the color or texture features. Next, classifiers have been utilized to analyze the

extracted characteristics and distinguish the knots from the normal wood tissue. Most

research has employed artificial neural network (ANN) techniques for addressing this

problem (Xie and Wang 2015; Hashim et al. 2016; Kamal et al. 2017; Yu et al. 2019).

Another common classifier used was support vector machine (SVM). As an example, a

tree-structure SVM was proposed to classify four types of wood knots. The authors claimed

that the average accuracy was 96.5% and the false alarm rate was only 2.25% (Gu et al.

2009). Many other methods have also been investigated, such as clustering (Silvén et al.

2003), compressed sensing (Zhang et al. 2016), and convex optimization (Chang et al.

2018).

The main drawback of these methods is that the performance suffers from

variations in the material. The color and texture vary significantly while the tree species,

the surface condition, or the light environment change (He et al. 2019). Finding a method

to efficiently extract color or texture features of timber surface images with a large variety

is formidable. Therefore, automated solutions of detecting surface knots on sawn timbers

remain as a critical need for the wood industry and further exploration is still needed.

Convolutional neural network (CNN) is the leading technique for object detection,

and the most recent papers regarding surface defect inspection rely on it (Dhillon and

Verma 2020). As a universal function approximator, it has a strong ability to extract almost

any high-level features from the input images. Particularly, it was reported to achieve good

performance while applied for defect identification in the wood industry (Rudakov et al.

2019; He et al. 2019; Urbonas et al. 2019; Ding et al. 2020; He et al. 2020; Tu et al. 2021).

Rudakov et al. (2019), to the best of the authors’ knowledge, was a pioneer in using CNN-

based approaches to detect the timber surface defects. AlexNet, GoogLeNet, VGG-16, and

ResNet-50 were compared in terms of the classification accuracy of mechanical damages

of sawn timber. The experimental results showed that VGG-16 was the best approach and

achieved over 92% accuracy (Rudakov et al. 2019). In Hu’s work, a pre-trained ResNet18

network, combined with transfer learning strategies, was utilized for the problems of wood

defect, wood texture, and wood species classification (Hu et al. 2019). Some recently

proposed CNN-based models, such as Mix-FCN (He et al. 2019; He et al. 2020), Faster R-

CNN (Urbonas et al. 2019), Mask R-CNN (Hu et al. 2020; Shi et al. 2020), etc., have also

found very successful application in this field.

This paper proposes an idea for applying the current state-of-the-art YOLO (You

Only Look Once) in the automated detection of surface knots on sawn timbers. YOLO,

originally designed by Joseph Redmon (Redmon et al. 2016), is an attractive CNN-based

algorithm for object detection, classification, and localization in images and videos (Desai

et al. 2020). During the past years, YOLO kept improving with some new algorithms to

optimize the computing speed and achieve better performance. The fifth version of YOLO

(YOLO-v5) was introduced by Glenn Jocher in June 2020 (Jocher et al. 2021). This model

significantly reduced the model size (YOLO-v4 on Darknet had 244MB size whereas

YOLO-v5 smallest model is 27MB). YOLO-v5 also claimed a higher accuracy and more

frames per second than all previous versions.

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5391

PEER-REVIEWED ARTICLE

bioresources.com

EXPERIMENTAL

Materials

Dataset 1

Some sawn timbers with sanded surfaces were purchased from a local sawmill.

Parts of them were Metasequoia glyptostroboides, and the other parts were Pinus

koraiensis. The number and the ratio were random. 305 images were collected from those

sawn timbers and utilized as Dataset 1.  The raw images were first processed with Adobe

Photoshop software (San Jose, CA) to ensure that each image contained at least one knot.

The image size ranged from 70 kB to 3354 kB. Figure 1 demonstrates some typical images

in the dataset. All images were labeled by experienced workers, using the open-source

software labelImg (https://github.com/tzutalin/labelImg). The red rectangular box in Fig. 1

illustrated the annotation results. Annotations were saved as XML files in PASCAL VOC

format and then were transferred to YOLO format with a Python program.

Fig. 1. Some typical images in Dataset 1

Dataset 2

Dataset 2 was downloaded from the website of the University of Oulu, Finland

(Silvén et al. 2003). It contains 839 images of spruce wood. They were RBG color images

with 8 bits per channel and the size was 488 by 512 pixels. Figure 2(a) shows one typical

image of the dataset.

Originally, each image was divided into rectangular regions. One rectangle

corresponds to about 2.5 * 2.5 cm2 area of wood surface which has been manually labeled,

as illustrated in Fig. 2(b). In total, there were 5,952 defect rectangles in the dataset. Table

1 lists the different types and quantities of defects.

Figure 2(b) shows that one whole knot was often split into two or more batches

because the rectangles were arranged in a fixed position and the size was fixed. The

geometric feature of the knot was then destroyed in each batch, which was not beneficial

for the knot detection. Another drawback of this annotation method was that the feature of

a small knot was easily submerged by the large area of normal wood tissues, like the small

knot showed in Fig. 2(b). Therefore, all images were labeled manually in the same way as

Dataset 1. Figure 2(c) shows the annotation results in this work. The dry knot and the small

knot were labeled with one rectangle, respectively. The size and position of the rectangle

were no longer fixed and completely depended on the knots.

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5392

PEER-REVIEWED ARTICLE

bioresources.com

Fig. 2. A typical image of Dataset 2 and its annotations: (a) The original image; (b) The original

annotations; (c) The annotations in this work

Table 1. Summary of Dataset 2

Class of Defects

Numbers of Defect


---
*Page 4*


Class of Defects

Numbers of Defect

Rectangles

Dry_Knot

474

Resin

60

Resin_Pocket

139

Sound_Knot

553

Encased_Knot

142

Edge_Knot

155

Moustache_Knot

30

Leaf_Knot

126

Core_Stripe

340

Horn_Knot

145

Small_Knot

369

Split

750

Wane

2126

Knot_Hole

53

Unknown

137

Bark_Pocket

55

Mold

261

Decayed_Knot

37

This work focused on the detection method of knot defects, and all knot types were

grouped into one category. Otherwise, the detection performance would not be adequate if

the samples were split by knot classes. It should be worth noting that a part of the samples

in Dataset 2 had a sanded surface, whereas the surface of the other part of the samples was

unsurfaced, as shown in Fig. 3.


---
*Page 4*


Rectangles

Fig. 3. Illustration of the surface condition of some samples in Dataset 2

To the authors’ knowledge, it is more in line with industrial practice. The common

need for knot identification is in unsurfaced or "rough" boards, even though most of the

existing research were conducted on the sanded samples.

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5393

PEER-REVIEWED ARTICLE

bioresources.com

Architecture of YOLO-v5 Model

Architecturally, the YOLO-v5 model is similar to YOLO-v4. As shown in Fig. 4,

it consists of three main parts: Backbone, Neck, and Head (Zhu et al. 2020; Xu et al. 2021).

The first part, Backbone, extracts crucial features from the given input image. In

YOLO-v5, CSPNet s (Cross Stage Partial Networks) are incorporated into Darknet,

creating CSPDarknet as its backbone. Compared to the Darknet53 used by YOLO-v3,

CSPDarknet has achieved considerable improvement in processing speed with equivalent

or even superior detection accuracy (Wang et al. 2020).

The second part, Neck, is primarily employed to generate feature pyramids, which

benefit YOLO-v5 in generalizing the object scaling for identifying the same object with

different sizes and scales. In YOLO-v5, Neck employs Path Aggregation Network (PANet)

as a parametric polymerization mechanism for different bone and detector levels. The

feature grid is connected to all the feature layers by the adaptive feature pools provided by

PANet. Consequently, the useful information obtained from each feature layer can be

transmitted directly to the proposed subnetwork (Liu et al. 2018; Cheng and Zhang 2020).

The final detection is performed in the part of Head, which is the same as the

previous YOLO-v3 and v4 versions. Head generates anchor boxes for feature maps and

outputs final output vectors with class probabilities and bounding boxes of detected knots.

Backbone:CSPDarknet

Neck:PANet

Head:Yolo Layer

Focus

CSP

(1*Bottleneck)

Concat


---
*Page 5*


Conv


---
*Page 5*


Conv2d

Conv

CSP

(1*Bottleneck)


---
*Page 5*


Upsample

Conv


---
*Page 5*


Conv


---
*Page 5*


Concat

CSP

(3*Bottleneck)


---
*Page 5*


CSP

(1*Bottleneck)


---
*Page 5*


CSP

(1*Bottleneck)


---
*Page 5*


Conv2d

Conv


---
*Page 5*


Concat


---
*Page 5*


Conv

CSP

(3*Bottleneck)


---
*Page 5*


Upsample


---
*Page 5*


Concat

Conv

Conv


---
*Page 5*


CSP

(1*Bottleneck)


---
*Page 5*


Conv2d

CSP

(1*Bottleneck)


---
*Page 5*


SPP

Fig. 4. The architecture of YOLO-v5 model

Experimental Configuration

The experiments were conducted in the environment represented in Table 2. The

implementation of YOLO-v5 was downloaded from the website, https://github.com/

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5394

PEER-REVIEWED ARTICLE

bioresources.com

ultralytics/yolov5. The release of YOLO-v5 includes four models of different sizes:

YOLO-v5s (smallest), YOLO-v5m, YOLO-v5l, YOLO-v5x (largest). YOLO-v5m model

was selected in this work due to the compromise of its modest size and outstanding

performance. The network was pre-trained with Coco dataset and it was fine-tuned using

Dataset 1 or Dataset 2 mentioned above.

Table 2. Configuration of Experimental Environment

Name

Parameter

CPU

Intel I5-7500 3.4GHz Quad-core

System

Windows 10

Operating memory

16 GB

Graphics card

NVIDIA GeForce RTX 2060 6GB

cuDNN 7.6.5

Evaluation Metrics


---
*Page 6*


Environment configuration

Python 3.7.6 + Pytorch 1.5.1 + VS 2017 + CUDA 10.2 +

The output of the detectors was compared with the manual annotations to evaluate

the performance quantitatively. Precision, Recall Rate, and overall accuracy F-Score were

calculated according to Eqs. 1 through 3 (Goutte and Gaussier 2005),

𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 (%) =


---
*Page 6*


𝑇𝑃

𝑇𝑃 + 𝐹𝑃  × 100

(1)


---
*Page 6*


𝑅𝑒𝑐𝑎𝑙𝑙 𝑅𝑎𝑡𝑒 (%) =


---
*Page 6*


𝑇𝑃

𝑇𝑃 + 𝐹𝑁  × 100

(2)


---
*Page 6*


𝐹−𝑆𝑐𝑜𝑟𝑒 (%) = 2 ×


---
*Page 6*


(𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 × 𝑅𝑒𝑐𝑎𝑙𝑙)


---
*Page 6*


(𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙)  × 100

(3)

where TP (true positive) referred to the number of the correctly detected knots, FP (false

positive) indicated the number of the extra knots that did not exist on the timber surface

(commission error), and FN (false negative) denoted the number of knots that were not

detected (omission error). Obviously, Precision indicated the ratio of correctly detected

knots out of all detected knots. Recall Rate  was an indication of the detector’s sensitivity.

F-Score  provided a way to combine both Precision and Recall Rate  into a single measure

that captured both properties. A higher F-Score indicated a more accurate model.

RESULTS AND DISCUSSION

Experiments on Dataset 1

Data augmentation

The data loader of YOLO-v5 makes three kinds of augmentations automatically:

scaling, color space adjustments, and mosaic augmentation. Mosaic is a novel and effective

data augmentation technique, which combines 4 training images into one in certain ratios,

as demonstrated in Fig. 5. It is beneficial to optimize the performance of the detector and

avoid overfitting by enriching the training dataset.

Training

The dataset was randomly split as follows: 80% for training, 10% for validation,

and 10% for testing. The total numbers of knots contained in the three subsets were 305,

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5395

PEER-REVIEWED ARTICLE

bioresources.com

37, and 36, respectively. GIOU_Loss was used as the loss of the bounding box (Jiang et al.

2021) and the threshold for non-maximum suppression (NMS) of the bounding box was

0.45. Table 3 lists the main training parameters.

Fig. 5. Illustration of the mosaic data augmentation

Table 3. Main Training Parameter

Name

Parameter

Name

Parameter

Batch size

8

Learning epochs

1000

Learning rate

0.001

NMS threshold

0.45

Loss function

GIOU_Loss

Optimizer

Adam

In the training process, each iteration can be divided into two steps. First, the data

in the training set was applied to the model, and the model automatically adjusted the

weight according to the loss value. Then, the data in the validation set was applied to the

model. Consequently, the loss value was calculated using the weight just updated. The loss

value obtained using the data in the validation set was used as an important index to

evaluate the performance of the model.

0.15

0.12

0.09

Loss

0.06

0.03

0

0

100

200

300

400

500

600

700

800

900

1000

Fig. 6. The loss for the YOLO-v5 in training


---
*Page 7*


Epoch

The training finished after 1000 iterations, and a weight file with a size of 43.3 MB

was obtained. The training work took 7.23 h. The loss for validation dataset during training

is shown in Fig. 6.

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5396

PEER-REVIEWED ARTICLE

bioresources.com

After the first 20 iterations, the loss dropped rapidly from 0.144 to 0.052. Then, a

steady decline can be observed from the curve of the loss even though an oscillation

appeared. After 800 iterations, the loss tended to be stable and gradually approached 0.009.

The loss curve showed that YOLO-v5 has a strong learning ability and can converge

quickly.

Detection performance

The trained YOLO-v5 model was utilized to detect the images of the testing set.

The object confidence threshold was 0.25. Figure 7 shows the results of six typical samples.

Rectangles were employed to mark the knots detected. The confidence coefficients were

also represented on the top of the rectangles.

Fig. 7. The detection results of some typical samples: (a) dark knot; (b) decayed knot; (c) sound

knot; (d) pin knot; (e) edge knot; (f) irregular knot

The trained YOLO-v5 accurately detected the knot defects. The knots in Fig. 5(a)

and (b) featured a different grain pattern and a distinctly different color. Figure 5(c) shows

a sound knot whose color was very close to the surrounding tissues. The image shown in

Fig. 5(d) contained some pin knots, which often have an actual size that is less than one-

fourth of an inch in diameter. Note that some researchers argued that YOLO-v5, like other

existing methods, is still deficient in detecting small targets, especially those near large

targets (Wang et al. 2021). The detecting results in this work showed that YOLO-v5 is

enough for the application of pin knot detection. An edge knot is shown in Fig. 5(e). The

whole knot was split into two different pieces. As a result, the geometric shape and the

grain changed significantly. The knot in Fig. 5(f) has an irregular shape. Generally, it was

challenging for the traditional methods to identify all these types of knots. However, the

detection results demonstrated that YOLO-v5 model can detect them with high confidence

coefficients (most of the confidence coefficients are bigger than 0.90).

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5397

PEER-REVIEWED ARTICLE

bioresources.com

Table 4 lists the detailed results on the training set, the validating set, and the testing

set. YOLO-v5 achieved the best performance on the training set. All 305 knots were

identified accurately, and only one extra knot that did not exist was marked. Recall rate

was 100% and Precision was 99.7%. The F-Score was 99.8%, which was very close to

100%. This is a high performance in the field of target detection. On the validating set,

YOLO-v5 could find 36 out of 37 knots and made two commission errors. Precision, Recall

Rate, and F-Score were 94.7%, 97.3%, and 96.0%, respectively. The detection performance

was still very high on the testing set, even though it was slightly lower than that of the

training set and the validating set. Totally, 33 out of 36 knots were identified and F-score

was 91.7%. All the results demonstrated that YOLO-v5 can effectively learn enough

information from the training set, and then correctly identify the knot defects from the

background.

Table 4. Detailed Results on the Training Set, Validating Set, and Testing Set

Dataset

TP

FP

FN

Training set

305

1

0

99.7%

100%

99.8%

Validating set

36

2

1

94.7%

97.3%

96.0%

Testing set

33

3

3

91.7%

91.7%

91.7%

Comparison YOLO-v5 with other methods

To further evaluate the performance, the YOLO-v5 model was compared with

YOLO-v3 SPP (Liu et al. 2020 ) and Faster R-CNN (Ren et al. 2017). The implementation

of these two models was also downloaded from the website, https://github.com/. The

backbone of Faster R-CNN was Restnet50. Due to the limitation of GPU, the batch size of

training for these two models was set as 4. The training iterations was 1000. Table 5 lists

the training time and the size of the weight file of these two models.

Table 5. Training Time and the Size of the Weight File of YOLO-v3 SPP Model

and Faster R-CNN

Model

YOLO-v3 SPP

Faster RCNN

Time for training

8.515 h

11.25h

Size of the weight file

244.8 MB

110.718 MB

The training time of these two models was longer than that of the YOLO-v5 model.

Especially, the training time of Faster R-CNN was almost 155% of that of YOLO-v5

model. The weight file size of these two models was also significantly larger than that of

YOLO-v5 model. The weight file size of YOLO-v3 SPP was almost 6 times that of the

YOLO-v5 model, and the Faster R-CNN was almost 3 times that of the YOLO-v5 model.

Figure 8 shows the output of the image from Fig. 7(d) using these two detectors.

The performance of these two models was worse than that of the YOLO-v5 model. Many

small knots were omitted to be detected. Moreover, some of the confidence coefficients

obtained by YOLO-v3 SPP were quite low. Table 6 listed the quantitative results of these

two models. By comparing values in Tables 4 and 6, it can be easily observed that YOLO-

v5 model had the best detection results regardless of the Precision, Recall Rate, or F-Score.

YOLO-v3 SPP achieved almost the same results, and Faster R-CNN was the worst one.

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5398

PEER-REVIEWED ARTICLE

bioresources.com

Fig. 8. The detection result of the image showed in Figure 5(d) obtained from: (a) YOLO-v3 SPP;

(b) Faster R-CNN

Table 6. Quantitative Results of YOLO-v3 SPP and Faster R-CNN

Model

Data Set

Precision

Recall Rate

F-Score

Yolo v3-SPP

Training set

99.0%

99.3%

99.2%

Validating set

92.3%

94.7%

93.5%

Testing set

91.7%

89.2%

90.4%

Faster R-CNN

Training set

93.4%

99.3%

96.3%

Validating set

95.5%

89.4%

92.3%

Testing set

90.9%

90.9%

90.9%

While checking all the output images of Faster R-CNN, it was found that Faster R-

CNN could accurately detect most of the knot defects. However, it sometimes marked the

area of torn grain as a knot. One typical example was shown in Fig. 9(a). Another reason

of the decrease in Precision was that the detector labeled an actual knot two or more times,

as shown in Fig. 9(b) and 9(c). For comparison, Fig. 9(d)-(f) showed the detection results

of the same sample using YOLO-v5. Obviously, YOLO-v5 avoids these problems.

Fig. 9. The comparison of detection results of two methods using some typical samples. (a)-(c)

The output of Faster R-CNN. (d)-(f) The output of YOLO-v5

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5399

PEER-REVIEWED ARTICLE

bioresources.com

Experimental Results on Dataset 2

The same tests were conducted on Dataset 2. At the first stage, 80% of the images

were used for training. Half of the remaining images were employed to validate the models

and the other half part were utilized to evaluate the knot detection. Figures 10 to 12 depicted

the results of three typical images.

According to the original annotation, there were two small knots and two dry knots

on the image of the sample st1184, which is shown in Fig. 10(a). Figure 10(b) illustrates

the detection results of the YOLO-v5 model. Undoubtedly, the YOLO-v5 model identified

all the knot defects correctly. Figure 10(c-d) shows that the four knots could also be

recognized by YOLO-v3 SPP and Faster R-CNN. However, the confidence coefficients

obtained by YOLO-v3 SPP were quite low, whereas Faster R-CNN labeled one actual knot

two or three times. These two problems can also be found from the previous experimental

results on Dataset 1.

Fig. 10.  Detection results of the sample st1184: (a) Original annotation; (b) Result of YOLO-v5;

(c) Result of YOLO-v3 SPP; (d) Result of Faster RCNN

Similar results are shown in Fig. 11. While inspecting the image of sample st1188,

the YOLO-v5 model could identify the dry knot with a confidence coefficient of 0.96,

whereas the coefficient obtained by YOLO-v3 SPP was only 0.68. For the same input

image, Faster R-CNN made a commission error besides marking the dry knots repeatedly.

The image of the sample st1407 depicted in Fig. 12(a) was quite complicated. It

included an encased knot, three small knots, and an edge knot. Particularly, the encased

knot had an irregular shape and the edge knot was incomplete and very small. All the

detectors omitted the encased knot except the YOLO-v5 model. Similar to previous results,

YOLO-v3 SPP detected the small knots with low confidence coefficients and overlapping

rectangles could be found in the result of Faster R-CNN.

At the next stage, the impact of the size of the training set on the detection accuracy

was investigated. The detectors were trained with train sets included 80%, 70%, 60%, and

50% images of Dataset 2, respectively. Similarly, the remaining images were divided into

two halves. One half was used as the validating set, and the other half was used for testing.

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5400

PEER-REVIEWED ARTICLE

bioresources.com

Fig. 11.  Detection results of the sample st1188: (a) Original annotation; (b) Result of YOLO-v5

model; (c) Result of YOLO-v3 SPP; (d) Result of Faster R-CNN

Fig. 12.  Detection results of sample st1407: (a) Original annotation; (b) Result of YOLO-v5; (c)

Result of YOLO-v3 SPP; (d) Result of Faster R-CNN

Figure 13 demonstrated the detection performance of the three types of detectors.

Overall, YOLO-v5, among the three methods, always achieved the best identification

performance and Faster R-CNN was the worst one. While 80% of images were used for

training, F-Score values obtained from the three detectors were 97.7%, 93.4%, and 77.2%,

respectively. The same tendency could also be observed when the detectors were trained

with 60% of all the images. The three F-Score were 93.6%, 91.9, and 72.3%.

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5401

PEER-REVIEWED ARTICLE

bioresources.com

Fig. 13. The detection performance with different size of training sets: (a) 80% images for

training; (b) 70% images for training; (c) 60% images for training; (d) 50% images for training

The accuracy decreased slowly when the number of training data diminished. The

F-Score of YOLO-v5 on the training set included 70% images was 91.0%. That was

significantly lower than F-Score, while 80% of images were used for training. The F-Score

values of YOLO-v3 on the two different training sets were 93.4% and 91.4%. Generally,

the more data that was used for training, the more feature information the network could

learn. Accordingly, a high detection accuracy could be achieved. Many CNN-based works

reported a similar tendency (Hu et al. 2019; He et al. 2020).

CONCLUSIONS

1. A YOLO-based approach was proposed to accurately and automatedly detect surface

knot defects of sawn timber using the YOLO-v5 model. Two datasets were employed

to test the method, and the experimental results obtained from the experiments suggest

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5402

PEER-REVIEWED ARTICLE

bioresources.com

that it could be a very effective choice for wood industries. F-score on Dataset 1 was

91.7% and that of Dataset 2 was up to 97.7%.

2. In comparison with YOLO-v3 SPP and Faster R-CNN, the YOLO-v5 model achieved

best performance for detecting surface knot defects. The comparison also showed that

YOLO-v5 has clear advantages in terms of training speed and the size of the weight

file. The training time of Faster R-CNN was almost 155% of that of YOLO-v5 model.

The weight file size of YOLO-v3 SPP was almost 6 times that of the YOLO-v5 model.

These advantages made YOLO-v5 more suitable for wood defect detection.

3. Like many other CNN-based models, the accuracy improves as the size of the training

set increases. The detection accuracy when 80% of all the images of Dataset 2 were

utilized for training was significantly higher than that of the training set included only

70% images.

4. YOLO models detect knot defects and achieves the classification of knots. However,

the latter point was not conducted in this work because the performance of YOLO

models depends on the size of the training set while the number of some types of knot

defects was quite low in the two datasets, especially encase knot, horn knot, etc. In the

future, more samples would be collected to train the YOLO better and carry on more

studies.

ACKNOWLEDGMENTS

The research work presented in this paper was supported by the China Postdoctoral

Science Foundation, Grant No. 2019M662112 and the Scientific Research Foundation of

Shaoxing University, Grant No. 20195024. The authors gratefully acknowledge the

anonymous reviewers for their valuable comments.

REFERENCES CITED

Chang, Z., Cao, J., and Zhang, Y. (2018). "A novel image segmentation approach for

wood plate surface defect classification through convex optimization," Journal of

Forestry Research  29(6), 1789-1795. DOI: 10.1007/s11676-017-0572-7

Cheng, Z., and Zhang, F. (2020). "Flower end-to-end detection based on YOLOv4 using

a mobile device," Wireless Communications and Mobile Computing  2020, article no.

8870649. DOI: 10.1155/2020/8870649

Desai, K., Parikh, S., Patel, K., Bide, P., and Ghane, S. (2020). "Survey of object

detection algorithms and techniques," in: Cybernetics, Cognition and Machine

Learning Applications. Algorithms for Intelligent Systems, V. Gunjan, P. Suganthan,

J. Haase, A. Kumar, B. Raman (eds.). Springer, Singapore. DOI: 10.1007/978-981-

15-1632-0_23

Dhillon, A., and Verma, G. K. (2020). "Convolutional neural network: A review of

models, methodologies and applications to object detection," Progress in Artificial

Intelligence  9, 85-112. DOI: 10.1007/s13748-019-00203-0

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5403

PEER-REVIEWED ARTICLE

bioresources.com

Ding, F., Zhuang, Z., Liu, Y., Jiang, D., Yan, X., and Wang, Z. (2020). "Detecting

defects on solid wood panels based on an improved SSD algorithm," Sensors  20(18),

5315. DOI: 10.3390/s20185315

Goutte, C., and Gaussier, E. (2005). "A probabilistic interpretation of Precision, Recall,

and F-score, with implication for evaluation," in: Advances in Information Retrieval.

ECIR 2005. Lecture Notes in Computer Science, D. E. Losada, J. M. Fernández-Luna

(eds.), vol 3408, Springer, Berlin, Heidelberg, pp. 345-359. DOI: 10.1007/978-3-540-

31865-1_25

Gu, I. Y. H., Andersson, H., and Vicen, R. (2009). "Wood defect classification based on

image analysis and support vector machines," Wood Science and Technology  44(4),

693-704. DOI: 10.1007/s00226-009-0287-9

Hashim, U. R., Hashim, S. Z. M., and Muda, A. K. (2016). "Performance evaluation of

multivariate texture descriptor for classification of timber defect," Optik  127(15),

6071-6080. DOI: 10.1016/j.ijleo.2016.04.005

He, T., Liu, Y., Xu, C., Zhou, X., Hu, Z., and Fan, J. (2019). "A fully convolutional

neural network for wood defect location and identification," IEEE Access  7, 123453-

123462. DOI: 10.1109/ACCESS.2019.2937461

He, T., Liu, Y., Yu, Y., Zhao, Q., and Hu, Z. (2020). "Application of deep convolutional

neural network on feature extraction and detection of wood defects," Measurement

152, article no. 107357. DOI: 10.1016/j.measurement.2019.107357

Hittawe, M. M., Sidibé, D., and Mériaudeau, F. (2015). "A machine vision based

approach for timber knots detection," in: Proceedings of the 12th International

Conference on Quality Control by Artificial Vision, 95340L. DOI:

10.1117/12.2182770

Hu, C., Min, X., Yun, H., Wang, T., and Zhang, S. (2011). "Automatic detection of sound

knots and loose knots on sugi using gray level co-occurrence matrix parameters,"

Annals of Forest Science  68, 1077-1083. DOI: 10.1007/s13595-011-0123-x

Hu, J., Song, W., Zhang, W., Zhao, Y., and Yilmaz, A. (2019). "Deep learning for use in

lumber classification tasks," Wood Science and Technology  53, 505-517. DOI:

10.1007/s00226-019-01086-z

Hu, K., Wang, B., Shen, Y., Guan, J., and Cai, Y. (2020). "Defect identification method

for poplar veneer based on progressive growing generated adversarial network and

MASK R-CNN model," BioResources  15(2), 3041-3052. DOI:

10.15376/biores.15.2.3041-3052

Jiang, K., Itoh, H., Oda, M., Okumura, T., Mori, Y., Misawa, M. Hayashi, T., Kudo, S.

E., and Mori, K. (2021). " Dense-layer-based YOLO-v3 for detection and localization

of colon perforations," in: Proceedings of Medical Imaging 2021: Computer-Aided

Diagnosis, Birmingham, UK, DOI: 10.1117/12.2582300.

Jocher, G., Stoken, A., Borovec, J., NanoCode012, ChristopherSTAN, Changyu, L.,

Laughing, tkianai, yxNONG, Hogan, A., et al. (2021). "Ultralytics/yolov5: v4.0 -

nn.SiLU() activations, weights & biases logging, PyTorch hub integration," DOI:

10.5281/zenodo.4418161

Kamal, K., Qayyum, R., Mathavan, S., and Zafar, T. (2017). "Wood defects classification

using laws texture energy measures and supervised learning approach," Advanced

Engineering Informatics  34, 125-135. DOI: 10.1016/j.aei.2017.09.007

Liu, S., Qi, L., Qin, H., Shi, J., and Jia, J. (2018). "Path aggregation network for instance

segmentation," in: Proceedings of IEEE conference on computer vision and pattern

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5404

PEER-REVIEWED ARTICLE

bioresources.com

recognition, Salt Lake City, UT, USA, pp. 8759-8768. DOI:

10.1109/CVPR.2018.00913

Liu, Y., Hou, M., Li, A., Dong, Y., Xie, L., and Ji, Y. (2020). "Automatic detection of

timber-cracks in wooden architectural heritage using YOLOv3 algorithm," in:

Proceedings of The International Archives of the Photogrammetry, Remote Sensing

and Spatial Information Sciences, 1471-1476. DOI:10.5194/isprs-archives-XLIII-B2-

2020-1471-2020

Longuetaud, F., Mothe, F., Kerautret, B., Krähenbühl, A., Hory, L., Leban, J. M., and

Debled-Rennesson, I. (2012). "Automatic knot detection and measurements from X-

ray CT images of wood: a review and validation of an improved algorithm on

softwood samples," Computers and Electronics in Agriculture  85, 77-89. DOI:

10.1016/j.compag.2012.03.013

Pölzleitner, W. (2003). "Quality classification of wooden surfaces using Gabor filters and

genetic feature optimisation," in: Machine Vision for the Inspection of Natural

Products, M. Graves, B. Batchelor (eds.), Springer, London, pp. 259-277. DOI:

10.1007/1-85233-853-9_9

Qu, H., Chen, M., Hu, Y., and Lyu, J. (2019). "Effect of trees knot defects on wood

quality: A review," in: Proceedings of International Conference on Energy, Chemical

and Materials Science-IOP Conference Series: Materials Science and Engineering,

Malacca, Malaysia, article no. 012027. DOI: 10.1088/1757-899X/738/1/012027

Redmon, J., Divvala, S., Girshick, R., and Farhadi, A. (2016). "You only look once:

Unified, real-time object detection," in: Proceedings of IEEE Conference on

Computer Vision and Pattern Recognition, Las Vegas, NV, USA, 779-788. DOI:

10.1109/CVPR.2016.91

Ren, S., He, K., Girshick, R., and Sun, J. (2017). "Faster R-CNN: Towards real-time

object detection with region proposal networks," IEEE Transactions on Pattern

Analysis and Machine Intelligence  39(6), 1137-1149. DOI:

10.1109/TPAMI.2016.2577031

Rudakov, N., Eerola, T., Lensu, L., Kälviäinen, H., and Haario, H. (2019). "Detection of

mechanical damages in sawn timber using convolutional neural networks," in:

Proceedings of German Conference on Pattern Recognition, Stuttgart, Germany, 115-

126. DOI: 10.1007/978-3-030-12939-2_9

Sarnaghi, A. K., and Kuilen, J. W. G. v. d. (2019). "An advanced virtual grading method

for wood based on surface information of knots," Wood Science and Technology 53,

535-557. DOI: 10.1007/s00226-019-01089-w

Shi, J., Li, Z., Zhu, T., Wang, D., and Ni, C. (2020). "Defect detection of industry wood

veneer based on NAS and multi-channel mask R-CNN," Sensors 20(16), Article

Number 4398. DOI: 10.3390/s20164398

Silvén, O., Niskanen, M., and Kauppinen, H. (2003). "Wood inspection with non-

supervised clustering," Machine Vision and Applications  13, 275-285. DOI:

10.1007/s00138-002-0084-z

Tu, Y., Ling, Z., Guo, S., and Wen, H. (2021). "An accurate and real-time surface defects

detection method for sawn lumber," IEEE Transactions on Instrumentation and

Measurement 70, article no. 2501911. 10.1109/TIM.2020.3024431

Urbonas, A., Raudonis, V., Maskeliunas, R., and Damaševičius, R. (2019). "Automated

identification of wood veneer surface defects using faster region-based convolutional

neural network with data augmentation and transfer learning," Applied Sciences  9,

article no. 4898. DOI: 10.3390/app9224898

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5405

PEER-REVIEWED ARTICLE

bioresources.com

Wang, C. Y., Liao, H. Y. M., Wu, Y. H., Chen, P. Y., Hsieh, J. W., and Yeh, I. H. (2020).

"CSPNet: A new backbone that can enhance learning capability of CNN," in:

Proceedings of IEEE/CVF Conference on Computer Vision and Pattern Recognition

Workshops, Seattle, WA, USA, 390-391. DOI: 10.1109/CVPRW50498.2020.00203

Wang, Z. J., Wu, Y. M., Yang, L. C., Thirunavukarasu, A., Evison, C., and Zhao, Y. F.

(2021). "Fast personal protective equipment detection for real construction sites using

deep learning approaches," Sensors 21, article no. 3478. DOI: 10.3390/s211034 78

Wells, L., Gazo, R., Del Re, R., Krs, V., and Benes, B. (2018). "Defect detection

performance of automated hardwood lumber grading system," Computers and

Electronics in Agriculture 155, 487-495. DOI: 10.1016/j.compag.2018.09.025

Xie, Y. H., and Wang, J. C. (2015). "Study on the identification of the wood surface

defects based on texture features," Optik-International Journal for Light and Electron

Optics 126, 2231-2235. DOI: 10.1016/j.ijleo.2015.05.101

Xu, R., Lin, H., Lu, K., Cao, L., and Liu, Y. (2021). "A forest fire detection system based

on ensemble learning," Forests 12, article no. 217. DOI: 10.3390/f12020217

Yu, H., Liang, Y., Liang, H., and Zhang, Y. (2019). "Recognition of wood surface

defects with near infrared spectroscopy and machine vision," Journal of Forestry

Research  30, 2379–2386. DOI: 10.1007/s11676-018-00874-w

Zhang, Y., Liu, S., Cao, J., Li, C., and Yu, H. (2016). "Wood board image processing

based on dual-tree complex wavelet feature selection and compressed sensing," Wood

Science and Technology  50, 297-311. DOI: 10.1007/s00226-015-0776-y

Zhang, Z., Ye, N., Wu, D., and Ye, Q. (2008). "Locating the wood defects with typical

features and SVM," in: Proceedings of the 11th Joint International Conference on

Information Sciences, 1-7, Shenzhen, China. DOI: 10.2991/jcis.2008.54

Zhu, Q., Zheng, H., Wang, Y., Cao, Y., and Guo, S. (2020). "Study on the evaluation

method of sound phase cloud maps based on an improved YOLOv4 algorithm,"

Sensors  20(15), Article Number 4314. DOI: 10.3390/s20154314

Article submitted: February 22, 2021; Peer review completed: April 25, 2021; Revised

version received: June 4, 2021; Accepted: June 6, 2021; Published: June 10, 2021.

DOI: 10.15376/biores.16.3.5390-5406

Fang et al. (2021). “Surface knots on sawn timber,” BioResources 16(3), 5390-5406.

5406
