Seesaw Loss for Long-Tailed Instance Segmentation


Jiaqi Wang1
Wenwei Zhang2
Yuhang Zang2
Yuhang Cao1
Jiangmiao Pang5
Tao Gong6


Kai Chen3,4
Ziwei Liu2
Chen Change Loy2
Dahua Lin1


1SenseTime-CUHK Joint Lab, The Chinese University of Hong Kong
2S-Lab, Nanyang Technological University
3 SenseTime Research
4 Shanghai AI Laboratory
5Zhejiang University
6 University of Science and Technology of China


{wj017,cy020,dhlin}@ie.cuhk.edu.hk
{wenwei001,zang0012,ziwei.liu,ccloy}@ntu.edu.sg


{pangjiangmiao,gongtao950513}@gmail.com
chenkai@sensetime.com


Abstract


Instance segmentation has witnessed a remarkable
progress on class-balanced benchmarks. However, they fail
to perform as accurately in real-world scenarios, where
the category distribution of objects naturally comes with
a long tail.
Instances of head classes dominate a long-
tailed dataset and they serve as negative samples of tail
categories. The overwhelming gradients of negative sam-
ples on tail classes lead to a biased learning process for
classiﬁers. Consequently, objects of tail categories are more
likely to be misclassiﬁed as backgrounds or head categories.
To tackle this problem, we propose Seesaw Loss to dynam-
ically re-balance gradients of positive and negative sam-
ples for each category, with two complementary factors,
i.e., mitigation factor and compensation factor. The miti-
gation factor reduces punishments to tail categories w.r.t.
the ratio of cumulative training instances between different
categories. Meanwhile, the compensation factor increases
the penalty of misclassiﬁed instances to avoid false posi-
tives of tail categories. We conduct extensive experiments
on Seesaw Loss with mainstream frameworks and different
data sampling strategies. With a simple end-to-end training
pipeline, Seesaw Loss obtains signiﬁcant gains over Cross-
Entropy Loss, and achieves state-of-the-art performance on
LVIS dataset without bells and whistles. Code is available
at https://github.com/open-mmlab/mmdetection.


1. Introduction


Deep learning-based object detection and instance seg-
mentation approaches have achieved immense success on
datasets with relatively balanced category distribution, e.g.,
COCO dataset [29].
However, the distribution of cate-
gories in the real world is long-tailed [32].
There are a
few head classes containing abundant instances, while most
other classes comprise relatively few instances.


On long-tailed datasets, existing instance segmentation


Cross-Entropy Loss
Seesaw Loss


gradients of negative samples on a tail class


gradients of positive samples on a tail class


Cross-Entropy


Seesaw Loss


Classification Accuracy


Mitigation


Compensation


Sorted Category Index


Cross-Entropy


Seesaw Loss


Sorted Category Index


Instance Segmentation 𝑨𝑷


Figure 1: Seesaw Loss dynamically re-balances the gradients of
positive and negative samples on a tail class with two complemen-
tary factors. It mitigates the overwhelming punishments on the tail
class as well as compensates them to reduce the risk of inducing
false positives. In Mask R-CNN [17], Seesaw Loss achieves re-
markable higher classiﬁcation accuracy of tail classes than Cross-
Entropy Loss on LVIS [14] dataset. As a result, instance segmenta-
tion AP on tail classes is signiﬁcantly improved, leading to better
overall performance.


frameworks [1, 4, 17] fail to perform as accurately as on
the datasets with balanced category distribution, exhibiting
unsatisfactory performance on tail classes. Figure 1 shows
the classiﬁcation accuracy and instance segmentation per-
formance of Mask R-CNN [17] on LVIS [14] dataset. The
classiﬁer in Mask R-CNN trained by Cross-Entropy Loss
tends to misclassify tail categories as backgrounds or other
confusing head classes, which leads to extremely low accu-
racy on tail classes.


1


arXiv:2008.10032v4  [cs.CV]  17 Jun 2021


The primary reason for this undesired phenomenon is
that the instances from head classes are predominant in
a long-tailed dataset. These instances contribute an over-
whelmingly large quantity of negative samples for tail
classes. Thus, the gradients of positive and negative sam-
ples on a tail class are heavily imbalanced, leading to a
biased learning process for the classiﬁer. One can imag-
ine that gradients of positive and negative samples resemble
two objects positioned on each end of a seesaw (see Fig. 1).
To balance them, a viable solution is to shorten the arm of
the heavier end in the seesaw, which is equivalent to scaling
down the overwhelming gradients of negative samples on
the tail class by a factor. Nevertheless, blindly reducing the
gradients of negative samples increases the risk of inducing
false positives of tail classes, since samples of other classes
are less punished when they are misclassiﬁed as tail classes.
Thus, a specialized mechanism is needed to compensate for
the excessively reduced penalties on tail classes.


In this work, we propose Seesaw Loss that dynamically
re-balances positive and negative gradients for each cate-
gory with two complementary factors, i.e., mitigation fac-
tor and compensation factor.
According to the ratio be-
tween categories’ cumulative sample numbers during train-
ing, the mitigation factor reduces the penalty to relatively
rare classes. When a false positive sample of one category is
observed, the compensation factor will increase the penalty
to that category. The synergy of the two above factors en-
ables Seesaw Loss to mitigate the overwhelming punish-
ments to tail classes as well as compensate for the risk of
misclassiﬁcation caused by diminished penalties.


Seesaw Loss has three appealing properties.
1) See-
saw Loss is dynamic.
It explores the ratios of cumula-
tive training sample numbers between different categories
and instance-wise misclassiﬁcation during training. This
differs signiﬁcantly to previous solutions that rely either
on static group split [26] or loss reweighting with con-
stant values [2, 7, 44]. 2) Seesaw Loss is self-calibrated.
The mitigation and the compensation factor synergize to
relieve the overwhelming punishments on tail classes as
well as avoid increasing false positives of tail categories.
On the contrary, previous methods blindly reduce punish-
ments on tail classes [44] or decrease the loss weights
of head categories [7].
3) Seesaw Loss is distribution-
agnostic. It does not rely on pre-computed datasets’ distri-
bution [2, 7, 32, 44], and it can operate well with any data
sampler [14, 19]. By accumulating the number of samples
in each class, Seesaw Loss gradually approximates the real
data distribution during training to achieve more accurate
balancing.


Through extensive experiments, we show consistent im-
provements of Seesaw Loss in different instance segmen-
tation frameworks and data samplers.
On the challeng-
ing LVIS [14] dataset, Seesaw Loss achieves signiﬁcant


improvements of 6.0% AP and 2.1% AP upon Mask R-
CNN [17] with random sampler and repeat factor sam-
pler [14], respectively. Even if switching to the stronger
Cascade Mask R-CNN [1], we still observe an impressive
improvement of 6.4% AP and 2.3% AP with random sam-
pler and repeat factor sampler. To show the versatility of
Seesaw Loss, we integrate it into the long-tailed image clas-
siﬁcation task. Seesaw Loss signiﬁcantly improves the clas-
siﬁcation accuracy by 6% on ImageNet-LT [32] dataset. Be-
sides, we also explore the necessity of the decoupling train-
ing pipeline [23, 26] in Seesaw Loss. Experimental results
demonstrate that Seesaw Loss provides a simpler and more
effective solution to long-tailed instance segmentation with-
out relying on complex training pipelines.


2. Related Work


Object Detection. Recent years have witnessed a remark-
able improvement in object detection [9, 16, 50, 47, 48]. A
leading paradigm in this area is the two-stage pipeline [12,
41], where the ﬁrst stage generates a set of region pro-
posals, and then the second stage classiﬁes and reﬁnes the
proposals.
Unlike the two-stage approaches, the single-
stage pipeline [28, 31, 39, 40] directly predicts bounding
boxes. Classical single-stage approaches [28, 31] require
densely populated anchors as a prior, while anchor-free
methods [24, 25, 45, 51] manage to achieve similar or better
performance without such prior. There are also attempts to
apply cascade architecture [1, 10, 22, 35, 49] to reﬁne the
bounding boxes’ predictions progressively.
Instance Segmentation. Instance segmentation is becom-
ing popular in tandem with a surge in the interest in ob-
ject detection.
Early methods perform segmentation be-
fore object recognition [37, 38]. Via adding a mask pre-
diction branch in the Faster R-CNN [41] architecture, Mask
R-CNN [17] bridges the gap between object detection and
instance segmentation. The idea is also adopted by [1, 4]
in their cascading frameworks. More recent works [6, 54]
introduce an even shorter pipeline by skipping the detec-
tion process and directly predicting mask for each instance.
Seesaw Loss can easily cooperates with object detection
and instance segmentation frameworks for the long-tailed
datasets.
Long-Tailed
Recognition.
Long-tailed
recognition
tasks [32, 14, 15, 55] receive growing attention recently as
the problems are closer to real-world applications. One rep-
resentative solution to the problem is loss re-weighting [2,
7, 20].
Loss re-weighting methods adopt different re-
weighting strategies [2, 7, 20, 28, 44] to adjust the loss of
different classes based on each class’s statistics [2, 7]. Other
common approches [15, 19, 34] re-balance the distribution
of the instance numbers in each class, e.g., repeat factor
sampling [14] and class-balanced sampling [34], both are
based on the sample numbers of classes. Different sampling


2


strategies can be adopted at different training stages to for-
mulate a multi-stage training procedure [19, 23]. A recent
work [23] proposes a decoupling training pipeline. which
ﬁrst trains a good representation network with natural sam-
pling and then ﬁnetunes the classiﬁer with class-balanced
sampling. There are also attempts to modify the classiﬁer
to improve the performance on tail classes, e.g., using dif-
ferent classiﬁers for different groups of classes [26], or use
two classiﬁers trained with different data samplers [53].


3. Methodology


The classiﬁer trained by the widely applied Cross-
Entropy (CE) Loss (Sec. 3.1) is highly biased on long-
tailed datasets, resulting in much lower accuracy of tail
classes than head classes. The major reason is that gradients
brought by positive samples are overwhelmed by gradients
from negative samples on tail classes. Therefore, we pro-
pose Seesaw Loss to mitigate the overwhelming gradients
of negative samples on tail classes as well as compensate
the gradients of misclassiﬁed samples to avoid false pos-
itives (Sec. 3.2). We also explore some practical compo-
nent designs to adopt Seesaw Loss in instance segmentation
(Sec. 3.3).


3.1. Cross-Entropy Loss


We ﬁrst revisit the most widely adopted Cross-Entropy
(CE) Loss in existing frameworks [4, 17]. The formulation
of CE Loss can be written as


Lce(z) = −


C
X


i=1


yi log(σi),
with σi =
ezi
PC


j=1 ezj , (1)


where z = [z1, z2, . . . , zC] and σ = [σ1, σ2, . . . , σC] are
the predicted logits and probabilities of the classiﬁer, re-
spectively. And yi ∈{0, 1}, 1 ≤i ≤C is the one-hot
ground truth label. Given a training sample of class i, the
gradients on zi and zj are given by


∂Lce(z)


∂zi


= σi −1,
(2)


∂Lce(z)


∂zj


= σj,
(3)


It shows that samples of class i punish the classiﬁer of class
j w.r.t. σj. In the case that the instance number of class i is
enormously greater than that of class j, the classiﬁer of class
j will receive penalties in most samples and attains few pos-
itive signals during training. Thus the predicted probabili-
ties of class j will be heavily suppressed, which results in a
low classiﬁcation accuracy of tail classes, as shown in Fig-
ure 1.


3.2. Seesaw Loss


To alleviate the above mentioned problem, one feasible
solution is to decrease the gradients of negative samples in
Eq. 3 imposed by head classes on a tail class. Therefore, we
propose Seesaw Loss as


Lseesaw(z) = −


C
X


i=1


yi log(bσi),


with bσi =
ezi
PC


j̸=i Sijezj + ezi .


(4)


Then the gradient on zj of negative class j in Eqn 3 becomes


∂Lseesaw(z)


∂zj


= Sij


ezj


ezi bσi.
(5)


Here Sij works as a tunable balancing factor between differ-
ent classes. By a careful design of Sij, Seesaw loss adjusts
the punishments on class j from positive samples of class
i. Seesaw loss determines Sij by a mitigation factor and a
compensation factor, as


Sij = Mij · Cij.
(6)


The mitigation factor Mij decreases the penalty on tail
class j according to a ratio of instance numbers between
tail class j and head class i. The compensation factor Cij
increases the penalty on class j whenever an instance of
class i is misclassiﬁed to class j.
Mitigation Factor.
Seesaw Loss accumulates instance
number Ni for each category i at each iteration in the whole
training process. As shown in Fig. 2, given an instance with
positive label i, for another category j, the mitigation factor
adjusts the penalty for negative label j w.r.t. the ratio Nj


Ni


Mij =


(
1,
if Ni ≤Nj



Nj
Ni


p


,
if Ni > Nj
(7)


When category i is more frequent than category j, See-
saw Loss will reduce the penalty on category j, which is


imposed by samples of category i, by a factor of





Nj
Ni


p


.
Otherwise, Seesaw Loss will keep the penalty on negative
classes to reduce misclassiﬁcation.
The exponent p is a
hyper-parameter that adapts the magnitude of mitigation.


Note that Seesaw Loss accumulates the instance num-
bers during training, rather than get the statistics from the
whole dataset ahead of time. This strategy brings two ben-
eﬁts. First, it can be applied when the distribution of the
whole training set is unavailable, e.g., training examples
are obtained from a stream. Second, the training samples
of each category can be affected by the adopted data sam-
pler [14], and the online accumulation is robust to sampling


3


Compensation Factor ( 𝓒𝒊𝒋=


𝝈𝒋
𝝈𝒊


𝒒


)


Head


Tail


𝑁𝑖


Mitigation Factor ( 𝓜𝒊𝒋 =


𝑵𝒋
𝑵𝒊


𝒑


)


𝑁𝑗


𝑁𝑖


𝑁𝑗


...
...


𝜎𝑗
𝜎𝑖


= 


𝑁𝑗
𝑁𝑖


𝜎𝑗


𝜎𝑖


...


Classifier


104


102


101


100
0
1200
600


0


1


103


A Sample of Class 𝑖


0.6


0.3


0.6


0.3


Figure 2: Seesaw Loss adjusts the punishments on tail classes
with the mitigation factor Mij and the compensation factor Cij.
The mitigation factor decreases the punishments w.r.t. the ratio of
instance numbers between different categories. The compensation
factor increases the penalty of misclassiﬁed instances w.r.t. the ra-
tio of classiﬁcation probabilities between the false positive and the
ground-truth category.


methods. During training, the mitigation factor is uniformly
initialized and smoothly updated to approximate the real
data distribution.
Compensation Factor. The mitigation factor effectively
balances the gradients of head and tail classes. Neverthe-
less, it may cause more false positives for tail classes due to
less penalty. Moreover, the false positives cannot be elim-
inated by simply adjusting p in Mij, since it is applied to
the whole category. We propose a compensation factor that
focuses on misclassiﬁed samples instead of adjusting the
whole category. As shown in Fig. 2, this factor compensates
the diminished gradient when there is misclassiﬁcation, i.e.,
the predicted probability σj of negative label j is greater
than σi. The compensation factor Cij is calculated as


Cij =


(
1,
if σj ≤σi



σj
σi


q


,
if σj > σi
(8)


For a training sample with positive label i, if the predicted
probability of any negative class j is greater than class i,
i.e., σj > σi, the compensation factor increases the punish-


ment on class j by a factor of





σj
σi


q


, where q is a hyper-
parameter to control the scale. Otherwise, Cij = 1 and only
the mitigation factor Mij is applied.
Normalized Linear Activation. The classiﬁer in an object
detector [41] usually predicts classiﬁcation logits as z =
WT x + b on the dataset with balanced category distribu-
tion [29], where W and b are the weights and bias of the lin-
ear layer and x is the input features. On long-tailed datasets,
previous works [23, 26] ﬁnd that the weight norm of Wi is


highly related to the number of training instances in the cor-
responding category i. The more training samples of cate-
gory i there are, the larger ∥Wi∥will be. This phenomenon
is also observed in the feature norm ∥x∥. Therefore, we
adopt a normalized linear activation (which [11, 32, 46]
are related) to re-balance the scale of ∥Wi∥and ∥x∥as
z = τ f
WT ex + b, where f
Wi =
Wi
∥Wi∥2 , i ∈C, ex =
x
∥x∥2 , and
τ is a temperature factor. The normalized linear activation
normalizes the weights W and features x by their L2 norm
to reduce their scale variance for different categories. Thus,
it effectively balances the distribution of predicted probabil-
ities of different categories and improves the performance
on a long-tailed dataset.


3.3. Model Design for Instance Segmentation


Objectness Branch. In contrast to image classiﬁcation, the
classiﬁer in an object detector has two functionalities. It
ﬁrst determines if a bounding box is a foreground object
then distinguishes which category the foreground instance
belongs to. Previous practices [1, 17, 41] usually regard
the background as an auxiliary category in the classiﬁer.
Given a dataset with C categories, the classiﬁer in most de-
tectors [17, 41] predicts logits of C + 1 classes. Although
widely adopted, this design brings difﬁculty when adopt-
ing Seesaw Loss to balance long-tailed distribution. In gen-
eral, most object candidates in a detector are backgrounds.
Thus, all foreground categories are much rarer categories
compared to the background category. Consequently, See-
saw Loss will signiﬁcantly reduce punishments on all fore-
ground categories. As a result, the classiﬁer tends to mis-
classify more backgrounds as foregrounds and harms the
performance.


To tackle this problem, we decouple the two function-
alities of the classiﬁer in an object detecter. Speciﬁcally,
apart from the classiﬁer with C classes, we adopt an ex-
tra objectness branch to distinguish the foregrounds and
backgrounds.
The objectness branch adopts the normal-
ized linear activation to predict logits of two classes, i.e.,
foreground and background, and is trained by cross-entropy
loss. During inference, both the classiﬁcation logit zclass


i
of
category i ∈C and logit of objectness zobj are activated
with a softmax function.
The ﬁnal detection probability
σdet


i
for a bounding box of category i is σdet


i
= σclass


i
·σobj.
Normalized Mask Predication. Inspired by normalized
linear activation, we further present a normalized mask pre-
diction to alleviate the biased training process in mask head.
In Mask R-CNN [17], a 1x1 convolution layer is applied in
the end of the mask head, and the predicted logits are acti-
vated by a sigmoid function. We normalize the weights W
of the 1x1 convolution layer and the input features X with
L2 normalization. Note that the spatial size of X is H ×W,
we denote the feature at (y, x) as Xy,x. The formula of
normalized mask prediction is z = τ f
W ∗e
X + b, where


4


f
Wi =
Wi
∥Wi∥2 , i ∈C, e
Xy,x =
Xy,x
∥Xy,x∥2 , y ∈H, x ∈W and τ
is a temperature factor.


4. Experiments


4.1. Experimental Settings


Datasets. We perform experiments on the challenging LVIS
v1 dataset [14]. LVIS is a large vocabulary instance seg-
mentation dataset containing 1203 categories with high-
quality instance mask annotations. LVIS v1 provides a train
split with 100k images, a val split with 19.8k images and a
test-dev split with 19.8k images. According to the numbers
of images that each category appears in the train split, the
categories are divided into three groups: rare (1-10 images),
common (11-100 images) and frequent (>100 images).
Evaluation metrics. The results of instance segmentation
are evaluated with AP of mask prediction, which is aver-
aged at different IoU thresholds (from 0.5 to 0.95) across
categories. The AP for rare, common and frequent cate-
gories are denoted as APr, APc and APf. The AP for de-
tection boxes is denoted as APbox.
Implementation Details. We implement our method with
mmdetection [5] and train Mask R-CNN [17], Cascade
Mask R-CNN [1] using the 2x training schedule [5, 13].
The model is trained with batch size of 16 for 24 epochs.
The learning rate is 0.02, and it will decrease by 0.1 after 16
and 22 epochs, respectively. ResNet-50 [18] with FPN [27]
backbone is adopted if not further speciﬁed. Following the
practice in mmdetection [5], we adopt multi-scale with hor-
izontally ﬂip augmentation during training. Speciﬁcally, we
randomly resize the shorter edge of the image within {640,
672, 704, 736, 768, 800} pixels and keep the longer edge
smaller than 1333 pixels without changing the aspect ratio.
In inference, we adopt single-scale testing with image size
of 1333 × 800 pixels and score thresholds of 10−3 without
bells and whistles.


Apart from the standard random sampler that samples
images in train split randomly, the repeat factor sampler
(RFS) [14, 34] is also evaluated in experiments. RFS over-
samples categories that appear in less than 0.1% of the total
images and is effective to improve the overall AP. The ab-
lation study is conducted with RFS if not further speciﬁed.
We adopt Seesaw Loss in the box classiﬁcation branch of
Mask R-CNN [17] with hyper-parameter p = 0.8, q = 2,
and τ = 20. In Cascade Mask R-CNN [1], Seesaw Loss
is adopted in box classiﬁcation branches of all three stages
with the same hyper-parameters as that in Mask R-CNN.
We further evaluate the proposed Normalized Mask Predic-
tion and integrate it into the mask head of Mask R-CNN and
all the mask heads in Cascade Mask R-CNN. For simplicity,
Normalized Mask Prediction adopts the same temperature,
i.e. τ = 20. We use the train split for training and report
the performance on val split for ablation study. The perfor-


mance of our method is also reported on test-dev split.


4.2. Benchmark Results


To show the effectiveness of Seesaw Loss, we per-
form extensive experiments with different data samplers
and instance segmentation frameworks. We adopt Mask R-
CNN [17] with ResNet-101 [18] backbone with FPN [27]
and train the models with the random sampler or the repeat
factor sampler (RFS) by 2x schedule.


As shown in Table 1, Seesaw Loss signiﬁcantly outper-
forms Cross-Entropy (CE) loss by 6.0% AP with random
sampler and 2.1% AP on the stronger baseline with RFS.
The improvements on APr, APc, and APf with both sam-
plers reveals the effectiveness of Seesaw Loss on categories
with different frequency. We further integrate the proposed
Normalized Mask Prediction (Norm Mask) into Mask R-
CNN [17] with Seesaw Loss. Without extra cost, the overall
AP is improved from 26.6% to 27.1 % and 27.6% to 28.1%
with random sampler and RFS, respectively.


Apart from the CE loss baseline, we further compare
Seesaw Loss with recent designs for long-tailed instance
segmentation, i.e., Equalization Loss (EQL) [44] and Bal-
anced Group Softmax (BAGS) [26], in Table 1. Seesaw
Loss outperforms EQL by 3.9% AP and 1.4% AP, and out-
performs BAGS by 1.0% AP and 1.8% AP with random
sampler and RFS, respectively. Seesaw Loss also achieves
higher APr, APc and APf than the two methods consis-
tently. Notably, EQL and BAGS achieve lower APf than the
CE baseline while Seesaw Loss does not. This phenomenon
indicates that these two methods improve the performance
of rare and common categories while sacriﬁcing frequent
categories.


We further compare Seesaw Loss with previous meth-
ods [26, 44] with both random sampler and RFS on Cas-
cade Mask R-CNN [1]. It’s a representative framework of
cascade methods [4, 1] that outperforms Mask R-CNN [17].
As shown in Table 1, Seesaw Loss performs much supe-
rior to previous works [26, 44] on Cascade Mask R-CNN.
Speciﬁcally, Seesaw Loss improves the baseline by 6.4%
AP and 2.3% AP with random sampler and RFS, respec-
tively. With Normalized Mask Prediction, Cascade Mask-
RCNN with Seesaw Loss ﬁnally achieves 29.6% AP and
30.1% AP with the two samplers, respectively. Moreover,
Seesaw Loss is also evaluated on test-dev split and consis-
tently obtains signiﬁcant gains over the CE baseline.


4.3. Ablation study


We conduct a comprehensive ablation study to verify the
effectiveness of each design choice in the proposed method.
Components in Seesaw Loss. There are three components
in Seesaw Loss: mitigation factor, compensation factor, and
normalized linear activation. We evaluated each compo-
nent on Mask R-CNN with RFS (Table 2). The mitigation


5


Table 1: Performance comparison of Mask R-CNN [17] and Cascade Mask R-CNN [1] with Cross-Entropy (CE) Loss, Equalization Loss
(EQL) [44], Balanced Group Softmax (BAGS) [26], and Seesaw Loss on LVIS v1 dataset [14]. The ResNet-101 [18] w/ FPN [27] is
adopted as backbone. All models are trained with random sampler or repeat factor sampler (RFS) [14] by 2x schedule in an end-to-end
pipeline. Norm Mask indicates the proposed Normalized Mask Prediction in Sec. 3.3.


Framework
Sampler
Loss
Split
AP
APr
APc
APf
AP box


Mask R-CNN [17]
Random


Cross-Entropy (CE)


val


20.6
0.8
19.3
30.7
21.7
Equalization Loss (EQL) [44]
22.7
3.7
23.3
30.4
24.0
Balanced Group Softmax (BAGS) [26]
25.6
17.3
25.0
30.1
26.4
Seesaw Loss
26.6
18.1
25.8
31.2
27.4
Seesaw Loss + Norm Mask
27.1
18.7
26.3
31.7
27.4


Mask R-CNN [17]
RFS [14]


Cross-Entropy (CE)


val


25.5
16.6
24.5
30.6
26.6
Equalization Loss (EQL) [44]
26.2
17.0
26.2
30.2
27.6
Balanced Group Softmax (BAGS) [26]
25.8
16.5
25.7
30.1
26.5
Seesaw Loss (Ours)
27.6
20.6
27.3
31.1
28.9
Seesaw Loss + Norm Mask (Ours)
28.1
20.0
28.0
31.8
28.9


Cascade Mask R-CNN [1]
Random


Cross-Entropy (CE)


val


22.6
2.4
22
32.2
25.5
Equalization Loss (EQL) [44]
24.3
5.1
25.3
31.7
27.3
Balanced Group Softmax (BAGS) [26]
27.9
19.6
27.7
31.6
31.5
Seesaw Loss (Ours)
29.0
21.1
28.6
33.0
32.8
Seesaw Loss + Norm Mask (Ours)
29.6
20.3
29.3
34.0
32.7


Cascade Mask R-CNN [1]
RFS [14]


Cross-Entropy (CE)


val


27.0
16.6
26.7
32.0
30.3
Equalization Loss (EQL) [44]
27.1
17.0
27.2
31.4
30.4
Balanced Group Softmax (BAGS) [26]
27.0
16.9
26.9
31.7
30.2
Seesaw Loss (Ours)
29.3
21.7
29.2
32.8
32.8
Seesaw Loss + Norm Mask (Ours)
30.1
21.4
30.0
33.9
32.8


Mask R-CNN [17]
RFS [14]
Cross-Entropy (CE)
test-dev
25.1
13.0
24.8
30.8
-
Seesaw Loss + Norm Mask (Ours)
27.9
20.3
27.1
32.2
-


Cascade Mask R-CNN [1]
RFS [14]
Cross-Entropy (CE)
test-dev
26.4
15.5
25.5
32.3
-
Seesaw Loss + Norm Mask (Ours)
30.0
23.0
29.3
34.1
-


Table 2: Ablation study of each design in Seesaw Loss with Mask
R-CNN w/ R-50 FPN backbone and repeat factor sampler. MF,
CF, NLA indicate mitigation factor, compensation factor, and nor-
malized linear activation, respectively.


MF CF NLA AP
APr APc APf AP box


23.7 13.5 22.8 29.3
24.7
✓
25.1 16.7 24.5 29.4
26.2
✓
24.1 13.2 23.5 29.5
25.1
✓
✓
25.7 19.1 25.0 29.4
26.8
✓
24.7 15.0 24.1 29.6
25.6
✓
✓
✓
26.4 19.6 26.1 29.8
27.4


factor that mitigates the overwhelming punishments on rare
classes leads to a signiﬁcant improvement from 23.7% AP
to 25.1% AP. Notably, it improves the APr of rare classes
by 2.8% AP. The compensation factor increases the pun-
ishments of a class when it observes false positives on that
class to reduce misclassiﬁcation. It improves the baseline
by 0.4% AP. The combination of the mitigation and the
compensation factors achieves 25.7% AP, outperforming
the performance of mitigation factor by 0.6% AP. It reveals
the effectiveness of instance-wise compensation to avoid
misclassiﬁcation. The normalized linear activation is an-
other important component in Seesaw Loss, which reduces
the scale invariance of weights and features across differ-


Table 3: The effectiveness of the normalized linear activation in
different methods. EQL and BAGS indicates Equalization Loss
and Balanced Group Softmax Loss, respectively.


Method NLA AP
APr APc APf AP box


EQL
25.1 17.4 24.8 28.8
26.1
EQL
✓
25.4 17.8 25.2 29.1
26.5
BAGS
24.7 15.6 24.4 28.9
25.2
BAGS
✓
25.5 19.2 25.0 28.9
25.8
Seesaw
25.7 19.1 25.0 29.4
26.8
Seesaw
✓
26.4 19.6 26.1 29.8
27.4


ent categories. It improves the baseline performance from
23.7% to 24.7% AP. Seesaw Loss combining all these three
components achieves 26.4% AP.
Normalized linear activation. We empirically ﬁnd that
normalized linear activation (NLA) helps to improve the
performance of both CE Loss and Seesaw Loss. Therefore,
we further integrate NLA with equalization loss (EQL) and
balanced group softmax (BAGS) for fair comparisons. Re-
sults in Table 3 show that NLA improves the performance
of EQL and BAGS by 0.3% and 0.8% AP, respectively. It is
noteworthy that Seesaw Loss outperforms EQL and BAGS
no matter whether NLA is adopted.
Cumulative Sample Numbers. Different from previous
works [2, 44, 26] that rely on the pre-computed frequency


6


Table 4: Comparison of different approaches to obtain sample
numbers of different categories in Seesaw Loss. From dataset in-
dicates to obtain the distribution of instance numbers directly from
the train split. Pre-Record indicates to load the cumulative sample
numbers from a model trained with Seesaw Loss. Online indicates
to accumulate the sample numbers during training.


Source
AP
APr APc APf AP box


From dataset 26.1 19.7 25.6 29.5
27.2
Pre-Record
26.3 19.6 25.8 29.8
27.4
Online
26.4 19.6 26.1 29.8
27.4


Table 5: Ablation study of the hyper-parameter p in





Nj
Ni


p


of
mitigation factor. The normalized linear activation is not adopted
in this table. p = 0.8 is the default setting in other experiments.


p
AP
APr APc APf AP box


0.2 24.4 14.7 23.6 29.4
25.4
0.4 24.9 15.2 24.6 29.6
26.0
0.6 25.4 17.9 24.6 29.5
26.5
0.8 25.7 19.1 25.0 29.4
26.8
1.0 25.5 17.6 25.2 29.2
26.4
1.2 25.3 18.1 24.7 29.0
26.5


Table 6:
Ablation study of the hyper-parameter q in





σj
σi


q


of compensation factor. The normalized linear activation is not
adopted in this table. q = 2.0 is the default setting.


q
AP
APr APc APf AP box


0.5 25.4 17.6 25.0 29.4
26.3
1.0 25.5 17.5 25.1 29.4
26.6
1.5 25.5 17.8 25.1 29.3
26.8
2.0 25.7 19.1 25.0 29.4
26.8
2.5 25.6 17.7 25.2 29.4
26.5
3.0 25.4 17.3 24.9 29.5
26.4


distribution of categories in the dataset, Seesaw Loss accu-
mulates the sample numbers of each category during train-
ing. We compare different approaches to obtain the sample
numbers of categories for Seesaw Loss (Table 4). Directly
using the statistics of train split decreases the performance
of Seesaw Loss by 0.3% AP. The reason lies in that the data
sampler, e.g., repeat factor sampler, changes the frequency
distribution of categories during training. We also explore
loading the pre-recorded distribution of training samples
from a model trained with Seesaw Loss. It achieves a simi-
lar performance with accumulating the training samples on-
line (26.3% AP vs. 26.4% AP). These results verify the
effectiveness and simplicity of online accumulating.
Hyper-parameters. We study the hyper-parameters, i.e., p,
q, τ, adopted in different components of Seesaw Loss. The
normalized linear activation is not applied when studying
the mitigation and compensation factors (25.7% AP with


this setting). In Table 5, we explore p in





Nj
Ni


p


of mitiga-
tion factor. p controls the magnitude to mitigate the pun-
ishments on rare classes. A higher value of p will reduce
punishments more, as well as increase the risk of inducing


Table 7: Ablation study of the temperature term τ in Normalized
Linear Activation. τ = 20 is the default setting.


τ
AP
APr
APc
APf
AP box


10
24.7
16.7
24.1
28.8
25.7
15
26.0
19.0
25.5
29.6
27.0
20
26.4
19.6
26.1
29.8
27.4
25
26.2
19.2
25.7
29.9
27.4
30
25.9
16.4
26.2
29.8
27.0


Table 8: Ablation study of the objectness branch in CE loss
baseline and Seesaw Loss. OBJ indicates whether the objectness
branch is adopted.


Method OBJ AP
APr APc APf AP box


CE
24.0 14.0 23.4 29.0
24.9
CE
✓
23.7 13.5 22.8 29.3
24.7
Seesaw
25.3 16.0 25.1 29.4
26.5
Seesaw
✓
26.4 19.6 26.1 29.8
27.4


false positives of tail classes. Therefore, it is critical to ﬁnd
a suitable p. Results show that p = 0.8 achieves the best
performance. In Table 6, we explore q in





σj
σi


q


of the com-
pensation factor. q controls the magnitude to compensate
the reduced punishments on tail classes when false positives
are observed. We study the effectiveness of different q and
ﬁnd q = 2.0 achieves the best performance. Notably, q is
robust across different values as the best value is only 0.3%
AP better than the worst value. In Table 7, we study the
temperature τ in normalized linear activation (NLA). τ de-
termines the variance of the classiﬁer’s predicted logit z. If
τ is too small, the variance of z is insufﬁcient to distinguish
positive and negative samples. However, if τ is too big,
the target of balancing the variance in weights and features
between different categories will be sacriﬁced. We choose
τ = 20 in the NLA as it achieves the best performance.
Objectness Branch. In a common practice of object detec-
tion, the classiﬁer predicts C + 1 scores for C foregrounds
categories and one background category. Due to the ex-
tremely imbalanced distribution between foregrounds and
backgrounds, Seesaw Loss will tend to misclassify more
backgrounds as foregrounds with this design.
Thus, we
adopt an extra objectness branch as described in Sec. 3.3.
The results in Table 8 shows that the objectness branch does
not improve the Coss-Entropy loss baseline but is critical
to Seesaw Loss. The objectness branch helps to avoid re-
ducing the backgrounds’ punishments on C foreground cat-
egories. As a result, the objectness branch brings gains on
Seesaw Loss across categories with different frequency, and
improves the overall AP from 25.3% to 26.4%.
Training Pipeline.
Apart from the end-to-end training
pipeline, we further explore the popular decoupling train-
ing pipeline [23, 26] on Mask R-CNN. Speciﬁcally, we pre-
train the Mask R-CNN with Cross-Entropy loss using ei-
ther random sampler or repeat factor sampler for 2x sched-


7


Table 9: Explorations of decouple training pipelines [23, 26] for
instance segmentation. Mask R-CNN with different classiﬁcation
loss is ﬁnetuned for 1x schedule with RFS sampler. We adopt
pre-trained models with random (P-Rand) or repeat factor sampler
(P-RFS) for 2x schedule. ‘DE-’ indicates the model is trained with
decoupling training pipelines.


Loss
P-Rand P-RFS AP APr APc APf AP box


EQL
25.1 17.4 24.8 28.8
26.1
BAGS
24.7 15.6 24.4 28.9
25.2
Seesaw
26.4 19.6 26.1 29.8
27.4
DE-EQL
✓
23.9 12.9 23.7 28.9
25.4
DE-EQL
✓
25.2 15.9 25.5 28.9
26.5
DE-BAGS
✓
25.4 16.3 25.1 29.7
26.3
DE-BAGS
✓
25.6 17.0 25.3 29.8
26.6
DE-Seesaw
✓
25.1 16.6 24.6 29.5
26.2
DE-Seesaw
✓
25.8 18.7 25.3 29.6
26.9


ule. Then we ﬁnetune the ﬁnal fully-connected layer of the
classiﬁer with all other components ﬁxed. The 1x sched-
ule and repeat factor sampler is adopted during ﬁnetuning.
As shown in Table 9, Seesaw Loss with the pre-trained
model on repeat factor sampler (P-RFS) achieves 25.8%
AP, outperforming other methods with decoupling training
pipeline. Notably, Seesaw Loss performs better with the
end-to-end training pipeline than with the decoupling train-
ing pipeline. It indicates Seesaw Loss provides a simpler
and more effective solution to long-tailed instance segmen-
tation without relying on complex training pipelines.


4.4. Long-Tailed Image Classiﬁcation


To show the versatility of Seesaw Loss, we apply it for
long-tailed image classiﬁcation task on ImageNet-LT [32]
dataset. ImageNet-LT [32] is generated from the ImageNet-
2012 [42] dataset with long-tailed distributed categories in
training set. There are 115.8k images of 1000 categories
with a maximum number of 1280 images and a minimum
number of 5 images. The performance is evaluated with
top-1 accuracy on all categories and the accuracies for Many
Shot (> 100 images), Medium Shot (20∼100 images) and
Few Shot (< 20 images) categories are also reported.


We adopt two training pipelines: end-to-end training and
decoupling training[23]. We use ResNeXt-50 [56] back-
bone and SGD optimizer with momentum of 0.9, initial
learning rate of 0.2, batch size of 512, and cosine learn-
ing rate [33] following [23]. For the end-to-end training
pipeline, the model is trained for 90 epochs. For decouple
training pipeline [23], we load the pre-trained ResNeXt-
50 [56] with Cross-Entropy Loss (CE), and ﬁnetune the
classiﬁer with class-balanced sampler while ﬁxing all other
layers for 10 epochs. Seesaw Loss in image classiﬁcation
mostly follows the hyper-parameters on the instance seg-
mentation task except for q in the compensation factor. We
adopt q = 1 for ImageNet-LT dataset. The study of q for
ImageNet-LT dataset is shown in Table 11.


Table 10: Comparison of different methods on ImageNet-LT [32]
test set. ResNeXt-50 [56] backbone is adopted in experiments.
Decouple means using decouple training pipeline [23].


Method
Decouple Overall Many Medium Few
CE
44.4
65.9
37.5
7.7
Focal Loss [28]
43.3
64.5
36.3
7.8
CB-Focal [7]
45.3
60.4
40.6
19.2
EQL [7]
46.0
61.7
42.5
13.8
NCM [23]
✓
47.3
56.6
45.3
28.1
cRT [23]
✓
49.6
61.8
46.2
27.4
τ-norm [23]
✓
49.4
59.1
46.9
30.7
LWS [23]
✓
49.9
60.2
47.2
30.3
Seesaw
✓
49.7
60.7
46.8
28.9
Seesaw
50.4
67.1
45.2
21.4


Table 11: Comparison of hyper-parameter q in the compensation
factor





σj
σi


q


on ImageNet-LT [32].


q
Overal Many Medium Few
0.5
49.6
66.2
44.4
20.9
1.0
50.4
67.1
45.2
21.4
1.5
49.6
66.4
44.3
20.7
2.0
49.4
66.5
44.0
20.3
2.5
48.4
65.8
42.9
18.7


We report the performance of Seesaw Loss in Table 10.
Seesaw Loss improves top-1 accuracies of CE from 44.4%
to 49.7% and 50.4% with the decoupling training and the
end-to-end training pipeline, respectively. Similar to our
observations on the instance segmentation task, Seesaw
Loss performs better with the end-to-end training pipeline
on image classiﬁcation. The performance achieved by See-
saw Loss with the end-to-end pipeline is competitive among
previous methods on ImageNet-LT [32].


5. Conclusion


In this paper, we propose Seesaw Loss for long-tailed in-
stance segmentation. Seesaw Loss dynamically re-balances
gradients of positive and negative samples for each category
with two complementary factors. The mitigation factor re-
duces punishments to tail categories w.r.t. the ratio of cu-
mulative training instances between categories. Meanwhile,
the compensation factor increases the penalty of misclassi-
ﬁed instances to avoid false positives. Experimental results
demonstrate that Seesaw Loss provides a simpler and more
effective solution to long-tailed instance segmentation with-
out relying on complex training pipelines.
Acknowledgements. This research was conducted in col-
laboration with SenseTime. This work is supported by GRF
14203518, ITS/431/18FX, CUHK Agreement TS1712093,
NTU NAP, A*STAR through the Industry Alignment Fund
- Industry Collaboration Projects Grant, Shanghai Com-
mittee of Science and Technology, China (Grant No.
20DZ1100800).


8


Cross-Entropy Loss


Seesaw Loss


Sorted Category Index


Ratio of cumulative gradients between


positive samples and negative samples


for each category


Figure 3: The distribution of the ratio of cumulative gradients be-
tween positive and negative samples for each category with Cross-
Entropy Loss and Seesaw Loss, respectively. The categories are
sorted in descending order with respect to their instance num-
bers. In contrast to Cross-Entropy Loss, Seesaw Loss effectively
re-balances the gradients of positive and negative samples.
Appendix A. Analysis of Sij in Seesaw Loss


In this work, we propose Seesaw Loss to dynamically
re-balance gradients of positive and negative samples for
each category. Speciﬁcally, Seesaw Loss mitigates the over-
whelming gradients of negative samples imposed by a head
class i on a tail class j via decreasing the value of Sij in the
following formula,


∂Lseesaw(z)


∂zj


= Sij


ezj


ezi bσi,


with bσi =
ezi
PC


j̸=i Sijezj + ezi .


(9)


To further analyze the effects of adjusting the value of Sij,
we calculate the partial derivative of Eqn 9 with respect to
Sij as


∂(Sij ezj


ezi bσi)
∂Sij


=


ezj(PC


k̸=i,j Sikezk + ezi)


(PC


j̸=i Sijezj + ezi)2
> 0.
(10)


The value of the partial derivative in Eqn 10 is always pos-
itive. This indicates that the gradients of negative samples
imposed by class i on class j will be reduced as the value of
Sij decreases.


Appendix B. How Seesaw Loss works


Via re-balancing gradients of positive and negative sam-
ples, Mask R-CNN [17] w/ Seesaw Loss signiﬁcantly out-
performs Mask R-CNN [17] w/ Cross-Entropy Loss on


LVIS [14] dataset. Here, we conduct a quantitative analysis
of the effectiveness of Seesaw Loss on re-balancing the gra-
dients of positive and negative samples for each category.
Speciﬁcally, we adopt Mask R-CNN [17] with ResNet-
101 [18] backbone and FPN [27] as instance segmentation
framework. The Cross-Entropy Loss and Seesaw Loss are
integrated into the framework and trained with random sam-
pler by 2x schedule. We accumulate the gradients of posi-
tive and negative samples on predicted logit zi of each cat-
egory i during the whole training procedure.


Figure 3 shows the distribution of the ratio of cumulative
gradients between positive and negative samples for each
category in Mask R-CNN [17] with Cross-Entropy Loss
and Seesaw Loss, respectively. With Cross-Entropy Loss,
tail classes obtain heavily imbalanced gradients of positive
and negative samples during training. The overwhelming
gradients of negative samples lead to a biased learning pro-
cess for the classiﬁer, which results in the low classiﬁcation
accuracy on tail classes. On the contrary, Seesaw Loss ef-
fectively re-balances the gradients of positive and negative
samples across different categories. Consequently, Mask R-
CNN with Seesaw Loss achieves signiﬁcant improvements
on instance segmentation performance as shown in Figure
1 and Table 1 in the main text.


Appendix C. Per-category Performance Com-


parison


In addition to the performance reported in Table 1 of the
main text, we further show the per-category performance
(AP) to verify the superiority of Seesaw Loss compared to
other loss functions. As shown in Figure 4, compared to
other loss functions (i.e., Cross-Entropy Loss, Equalization
Loss [44], and Balanced Group Softmax [26]), Seesaw Loss
consistently achieves strong performance across categories
with different frequency on different frameworks (i.e. Mask
R-CNN [17], Cascade Mask R-CNN [1]) and samplers (i.e.,
random sampler, repeat factor sampler [14]).


Appendix D. LVIS Challenge 2020


Here we present the approach used in the entry of team
MMDet in the LVIS Challenge 2020. In our entry, we adopt
Seesaw Loss for long-tailed instance segmentation as de-
scribed in the main text. Seesaw Loss improves the strong
baseline by 6.9% AP on LVIS v1 val split. Furthermore, we
propose HTC-Lite, a light-weight version of Hybrid Task
Cascade (HTC) [4] which replaces the semantic segmen-
tation branch with a global context encoder. With a sin-
gle model and without using external data and annotations
except for standard ImageNet-1k classiﬁcation dataset for
backbone pre-training, our entry achieves 38.92% AP on
the test-dev split of the LVIS v1 benchmark.


9


Cross-Entropy Loss (20.6%) 


Seesaw Loss (26.6%)


Equalization Loss (22.7%)


Balanced Group Softmax (25.6%)


Mask R-CNN w/ Random Sampler
Mask R-CNN w/  Repeat Factor Sampler


Cascade Mask R-CNN w/ Random Sampler


Cross-Entropy Loss (27.0%)


Seesaw Loss (29.3%)


Equalization Loss (27.1%)


Balanced Group Softmax (27.0%)


Cascade Mask R-CNN w/  Repeat Factor Sampler


Cross-Entropy Loss (25.5%) 


Seesaw Loss (27.6%)


Equalization Loss (26.2%)


Balanced Group Softmax (25.8%)


Cross-Entropy Loss (22.6%) 


Seesaw Loss (29.0%)


Equalization Loss (24.3%)


Balanced Group Softmax (27.9%)


Sorted Category Index
Sorted Category Index


Sorted Category Index
Sorted Category Index


Figure 4: Per-category performance (AP) comparison between different methods in Table 1 of the main text. Norm Mask is
not adopted for a fair comparison.


F


Pool
Pool
Pool


B1


M1


B2


M2


B3


M3


Pool


Semantic
Segmentatin


Pool


F


Pool
Pool
Pool


B1
B2
B3


M


Pool


Context
Encoding


Pool


HTC
HTC-Lite
Figure 5: The comparison of HTC and HTC-Lite.


D.1. HTC-Lite


We propose HTC-Lite, a light-weight version of Hy-
brid Task Cascade (HTC) [4], to accelerate the training


and inference speed while maintaining good performance.
As shown in Figure 5, the modiﬁcations are in two folds:
replacing the semantic segmentation branch with a global
context encoding branch and reducing mask heads.


10


Table 12: Step by step results of our entry on LVIS v1 [14] val split.
Modiﬁcation
Schedule
AP
APr
APc
APf
AP box


Mask R-CNN
2x
18.7
1.0
16.1
29.4
20.1
+ SyncBN
2x
18.9 (+0.2)
0.7
16.0
30.3
20.2 (+0.1)
+ CARAFE Upsample
2x
19.4 (+0.5)
0.7
16.5
30.9
20.4 (+0.2)
+ HTC-Lite
2x
21.9 (+2.5)
1.1
19.8
33.5
23.6 (+3.2)
+ TSD
2x
23.5 (+1.6)
2.3
22.3
34.0
25.5 (+1.9)
+ Mask scoring
2x
23.9 (+0.4)
2.8
22.4
35.0
25.6 (+0.1)
+ Training-time augmentaion
45e
26.5 (+2.6)
3.6
25.7
37.4
28.1 (+2.5)
+ Stronger neck
45e
27.0 (+0.5)
3.5
25.8
38.6
29.1 (+1.0)
+ Stronger backbone
45e
29.9 (+2.9)
4.2
29.4
41.8
32.1 (+3.0)
+ Seesaw Loss
45e
36.8 (+6.9)
25.5
35.6
42.9
39.8 (+7.7)
+ Dual Head Classiﬁcation
1x
37.3 (+0.5)
26.4
36.3
43.1
40.6 (+0.8)
+ Test-time augmentation
-
38.8 (+1.5)
26.4
38.3
44.9
41.5 (+0.9)


Table 13: Comparison of different cascading instance segmenta-
tion frameworks on LVIS v1 [14] dataset with repeat factor sam-
pler and 1x training schedule. HTC w/o semantic indicates HTC
without adopting the semantic segmentation branch since semantic
segmentation annotations are not available on LVIS v1 dataset.


Method
AP APr APc APf AP box fps
Cascade Mask R-CNN [1] 24.3 13.7 23.8 29.6
27.2 0.1
HTC w/o semantic [4]
24.8 14.5 24.1 30.2
27.0 0.1
HTC-Lite
25.5 15.0 25.4 30.3
28.0 2.8


Context Encoding Branch. Since semantic segmentation
annotations are not available for LVIS [14] dataset, we re-
place the semantic segmentation branch with a global con-
text encoder [57] which works as a multi-label classiﬁca-
tion branch trained by a binary cross-entropy loss. The con-
text encoder applies convolution layers and a global average
pooling on the input feature map to obtain a feature vec-
tor. And an auxiliary fully connected (fc) layer is applied
on the feature vector to predict the categories existing in
the current image. By this approach, this feature vector en-
codes the global context information of the image. Then it
is added to the RoI features used by box heads and mask
heads to enrich their semantic information.
Reduced Mask Heads. To further reduce the cost of in-
stance segmentation, HTC-Lite only keeps the mask head
in the last stage, which also spares the original interleaved
information passing.


In Table 13, we compare the performance and inference
speed on LVIS v1 [14] dataset of HTC-Lite with two main-
stream cascading instance segmentation frameworks, i.e.,
Cascade Mask R-CNN and HTC. The ResNet-50 with FPN
backbone, repeat factor sampler and 1x training schedule
are adopted in these methods. The semantic segmentation
branch in HTC [4] is removed since semantic segmentation
annotations are not available on LVIS v1 [14] dataset. We
evaluate the inference speed for each framework with a sin-
gle Tesla V100 GPU. The experimental results show that
HTC-Lite is not only much more efﬁcient than its counter-


parts but also outperforms them.


D.2. Step by Step Results


We report the step-by-step results of our entry in LVIS
Challenge 2020 as shown in Table 12.
Baseline. The baseline model is Mask R-CNN [17] using
ResNet-50-FPN [27], trained with multi-scale training and
random data sampler by 2x schedule [5].
SyncBN. We use SyncBN [30, 36] in the backbone and
heads.
CARAFE Upsample. CARAFE [47] is used for upsam-
pling in the mask head.
HTC-Lite.
We use HTC-Lite as described in Ap-
pendix D.1.
TSD. TSD [43] is used to replace the box heads in all three
stages in HTC-Lite.
Mask Scoring. We further use the mask IoU head [21] to
improve mask results.
Training Time Augmentation. We train the model with
stronger augmentations with 45 epochs. The learning rate is
decreased by 0.1 at 30 and 40 epochs. We randomly resize
the image with its longer edge in a range of 768 to 1792
pixels. And then, we randomly crop the image to the size of
1280 × 1280 after adopting instaboost augmentation [8].
Stronger Neck.
We replace the neck architecture with
an enhanced version of Feature Pyramid Grids (FPG) [3].
The enhanced FPG uses deformable convolution v2
(DCNv2) [59] after feature upsampling, and a downsampler
version of CARAFE [47, 48] for feature downsampling.
Stronger Backbone.
We use ResNeSt-200 [58] with
DCNv2 [59] as the backbone.
Seesaw Loss. We apply the proposed Seesaw Loss to clas-
siﬁcation branches of the TSD box head, in all cascading
stages. Furthermore, we remove the original progressive
constraint (PC) loss on classiﬁcation branches in TSD.
Dual Head Classiﬁcation. Inspired by [53, 52], we adopt
a dual-head classiﬁcation policy to further boost the perfor-
mance. Speciﬁcally, after obtaining the model with Seesaw


11


Loss trained by a random sampler, we freeze all components
in the original model. Then we ﬁnetune a new classiﬁcation
branch for each cascading stage on the ﬁxed model using re-
peat factor sampler [14] by 1x schedule. During inference,
the classiﬁcation scores of original classiﬁcation branches
and the scores of new classiﬁcation branches are averaged
to get the ﬁnal scores.
Test Time Augmentation. We adopt multi-scale testing
with horizontal ﬂipping.
Speciﬁcally, image scales are
1200, 1400, 1600, 1800, and 2000 pixels.
Final Performance on Test-dev. After adding the above-
mentioned components step by step, we ﬁnally achieve
38.8% AP on the val split and 38.92% AP on the test-dev
split.


References


[1] Zhaowei Cai and Nuno Vasconcelos. Cascade r-cnn: High


quality object detection and instance segmentation. arXiv
preprint arXiv:1906.09756, 2019. 1, 2, 4, 5, 6, 9, 11
[2] Kaidi Cao, Colin Wei, Adrien Gaidon, Nikos Arechiga,


and Tengyu Ma. Learning imbalanced datasets with label-
distribution-aware margin loss. In NeurIPS, 2019. 2, 6
[3] Kai Chen, Yuhang Cao, Chen Change Loy, Dahua Lin, and


Christoph Feichtenhofer. Feature pyramid grids. 2020. 11
[4] Kai Chen, Jiangmiao Pang, Jiaqi Wang, Yu Xiong, Xiaoxiao


Li, Shuyang Sun, Wansen Feng, Ziwei Liu, Jianping Shi,
Wanli Ouyang, Chen Change Loy, and Dahua Lin. Hybrid
task cascade for instance segmentation. In CVPR, 2019. 1,
2, 3, 5, 9, 10, 11
[5] Kai Chen, Jiaqi Wang, Jiangmiao Pang, Yuhang Cao, Yu


Xiong, Xiaoxiao Li, Shuyang Sun, Wansen Feng, Ziwei Liu,
Jiarui Xu, Zheng Zhang, Dazhi Cheng, Chenchen Zhu, Tian-
heng Cheng, Qijie Zhao, Buyu Li, Xin Lu, Rui Zhu, Yue Wu,
Jifeng Dai, Jingdong Wang, Jianping Shi, Wanli Ouyang,
Chen Change Loy, and Dahua Lin.
MMDetection: Open
mmlab detection toolbox and benchmark.
arXiv preprint
arXiv:1906.07155, 2019. 5, 11
[6] Xinlei Chen, Ross B. Girshick, Kaiming He, and Piotr


Doll´ar. TensorMask: A foundation for dense object segmen-
tation. In ICCV, 2019. 2
[7] Yin Cui, Menglin Jia, Tsung-Yi Lin, Yang Song, and Serge


Belongie. Class-balanced loss based on effective number of
samples. CVPR, 2019. 2, 8
[8] Hao-Shu Fang, Jianhua Sun, Runzhong Wang, Minghao


Gou, Yong-Lu Li, and Cewu Lu.
Instaboost: Boosting
instance segmentation via probability map guided copy-
pasting. In ICCV, 2019. 11
[9] Golnaz Ghiasi, Tsung-Yi Lin, Ruoming Pang, and Quoc V.


Le. NAS-FPN: Learning scalable feature pyramid architec-
ture for object detection. CoRR, abs/1904.07392, 2019. 2
[10] Spyros Gidaris and Nikos Komodakis. LocNet: Improving


localization accuracy for object detection. In CVPR, 2016. 2
[11] Spyros Gidaris and Nikos Komodakis. Dynamic few-shot


visual learning without forgetting. In CVPR, 2018. 4
[12] Ross Girshick. Fast R-CNN. In ICCV, 2015. 2


[13] Ross Girshick, Ilija Radosavovic, Georgia Gkioxari, Piotr


Doll´ar, and Kaiming He. Detectron. https://github.
com/facebookresearch/detectron, 2018. 5
[14] Agrim Gupta, Piotr Dollar, and Ross Girshick.
LVIS: A
dataset for large vocabulary instance segmentation. In CVPR,
2019. 1, 2, 3, 5, 6, 9, 11, 12
[15] Haibo He and Edwardo A. Garcia. Learning from imbal-


anced data. IEEE TKDE, 2009. 2
[16] Kaiming He, Ross Girshick, and Piotr Dollar. Rethinking


ImageNet pre-training. In ICCV, 2019. 2
[17] Kaiming He, Georgia Gkioxari, Piotr Dollar, and Ross Gir-


shick. Mask R-CNN. ICCV, 2017. 1, 2, 3, 4, 5, 6, 9, 11
[18] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.


Deep residual learning for image recognition.
In CVPR,
2016. 5, 6, 9
[19] Xinting Hu, Yi Jiang, Kaihua Tang, Jingyuan Chen, Chunyan


Miao, and Hanwang Zhang. Learning to segment the tail. In
CVPR, 2020. 2, 3
[20] Chen Huang, Yining Li, Chen Change Loy, and Xiaoou


Tang. Deep imbalanced learning for face recognition and
attribute prediction. IEEE TPAMI, 2020. 2
[21] Zhaojin Huang, Lichao Huang, Yongchao Gong, Chang


Huang, and Xinggang Wang.
Mask Scoring R-CNN.
In
CVPR, 2019. 11
[22] Borui Jiang, Ruixuan Luo, Jiayuan Mao, Tete Xiao, and Yun-


ing Jiang. Acquisition of localization conﬁdence for accurate
object detection. In ECCV, 2018. 2
[23] Bingyi Kang, Saining Xie, Marcus Rohrbach, Zhicheng Yan,


Albert Gordo, Jiashi Feng, and Yannis Kalantidis. Decou-
pling representation and classiﬁer for long-tailed recogni-
tion. In ICLR, 2020. 2, 3, 4, 7, 8
[24] Tao Kong, Fuchun Sun, Huaping Liu, Yuning Jiang, and


Jianbo Shi. FoveaBox: Beyond anchor-based object detector.
CoRR, abs/1904.03797, 2019. 2
[25] Hei Law and Jia Deng.
CornerNet: Detecting objects as
paired keypoints. In ECCV, 2018. 2
[26] Yu Li, Tao Wang, Bingyi Kang, Sheng Tang, Chunfeng


Wang, Jintao Li, and Jiashi Feng. Overcoming classiﬁer im-
balance for long-tail object detection with balanced group
softmax. In CVPR, 2020. 2, 3, 4, 5, 6, 7, 8, 9
[27] Tsung-Yi Lin, Piotr Doll´ar, Ross B. Girshick, Kaiming He,


Bharath Hariharan, and Serge J. Belongie. Feature pyramid
networks for object detection. In CVPR, 2017. 5, 6, 9, 11
[28] Tsung-Yi Lin, Priya Goyal, Ross B. Girshick, Kaiming He,


and Piotr Doll´ar. Focal loss for dense object detection. In
ICCV, 2017. 2, 8
[29] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,


Pietro Perona, Deva Ramanan, Piotr Doll´ar, and C Lawrence
Zitnick. Microsoft COCO: Common objects in context. In
ECCV, 2014. 1, 4
[30] Shu Liu, Lu Qi, Haifang Qin, Jianping Shi, and Jiaya Jia.


Path aggregation network for instance segmentation.
In
CVPR, 2018. 11
[31] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian


Szegedy, Scott E. Reed, Cheng-Yang Fu, and Alexander C.
Berg. SSD: single shot multibox detector. In ECCV, 2016. 2


12


[32] Ziwei Liu, Zhongqi Miao, Xiaohang Zhan, Jiayun Wang,


Boqing Gong, and Stella X. Yu.
Large-scale long-tailed
recognition in an open world. In CVPR, 2019. 1, 2, 4, 8
[33] Ilya Loshchilov and Frank Hutter. SGDR: stochastic gradient


descent with warm restarts. In ICLR, 2017. 8
[34] Dhruv Mahajan, Ross B. Girshick, Vignesh Ramanathan,


Kaiming He, Manohar Paluri, Yixuan Li, Ashwin Bharambe,
and Laurens van der Maaten. Exploring the limits of weakly
supervised pretraining. In ECCV, 2018. 2, 5
[35] Mahyar Najibi, Mohammad Rastegari, and Larry S Davis. G-


cnn: an iterative grid based object detector. In CVPR, 2016.
2
[36] Chao Peng, Tete Xiao, Zeming Li, Yuning Jiang, Xiangyu


Zhang, Kai Jia, Gang Yu, and Jian Sun. MegDet: A large
mini-batch object detector. CVPR, 2018. 11
[37] Pedro H. O. Pinheiro, Ronan Collobert, and Piotr Doll´ar.


Learning to segment object candidates. In NeurIPS, 2015.
2
[38] Pedro Oliveira Pinheiro, Tsung-Yi Lin, Ronan Collobert, and


Piotr Doll´ar. Learning to reﬁne object segments. In ECCV,
2016. 2
[39] Joseph Redmon, Santosh Kumar Divvala, Ross B. Girshick,


and Ali Farhadi. You only look once: Uniﬁed, real-time ob-
ject detection. In CVPR, 2016. 2
[40] Joseph Redmon and Ali Farhadi. YOLO9000: Better, faster,


stronger. In CVPR, 2017. 2
[41] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.


Faster R-CNN: Towards real-time object detection with re-
gion proposal networks. In NeurIPS, 2015. 2, 4
[42] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, San-


jeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy,
Aditya Khosla, Michael Bernstein, Alexander C. Berg, and
Li Fei-Fei. ImageNet Large Scale Visual Recognition Chal-
lenge. IJCV, 2015. 8
[43] Guanglu Song, Yu Liu, and Xiaogang Wang. Revisiting the


sibling head in object detector. CVPR, 2020. 11
[44] Jingru Tan, Changbao Wang, Buyu Li, Quanquan Li, Wanli


Ouyang, Changqing Yin, and Junjie Yan. Equalization loss
for long-tailed object recognition. In CVPR, 2020. 2, 5, 6, 9
[45] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS:


Fully convolutional one-stage object detection.
CoRR,
abs/1904.01355, 2019. 2
[46] Hao Wang, Yitong Wang, Zheng Zhou, Xing Ji, Dihong


Gong, Jingchao Zhou, Zhifeng Li, and Wei Liu. CosFace:
Large margin cosine loss for deep face recognition. CVPR,
2018. 4
[47] Jiaqi Wang, Kai Chen, Rui Xu, Ziwei Liu, Chen Change Loy,


and Dahua Lin. CARAFE: Content-Aware ReAssembly of
FEatures. In ICCV, 2019. 2, 11
[48] Jiaqi Wang, Kai Chen, Rui Xu, Ziwei Liu, Chen Change Loy,


and Dahua Lin. Carafe++: Uniﬁed content-aware reassem-
bly of features, 2020. 2, 11
[49] Jiaqi Wang, Kai Chen, Shuo Yang, Chen Change Loy, and


Dahua Lin. Region proposal by guided anchoring. In CVPR,
2019. 2
[50] Jiaqi Wang, Wenwei Zhang, Yuhang Cao, Kai Chen, Jiang-


miao Pang, Tao Gong, Jianping Shi, Chen Change Loy, and


Dahua Lin. Side-aware boundary localization for more pre-
cise object detection. In ECCV, 2020. 2
[51] Ning Wang, Yang Gao, Hao Chen, Peng Wang, Zhi Tian, and


Chunhua Shen. NAS-FCOS: Fast neural architecture search
for object detection. CoRR, abs/1906.04423, 2019. 2
[52] Tao Wang, Yu Li, Bingyi Kang, Junnan Li, Jun Hao Liew,


Sheng Tang, Steven Hoi, and Jiashi Feng. Classiﬁcation cal-
ibration for long-tail instance segmentation. arXiv preprint
arXiv:1910.13081, 2019. 11
[53] Tao Wang, Yu Li, Bingyi Kang, Junnan Li, Jun Hao Liew,


Sheng Tang, Steven C. H. Hoi, and Jiashi Feng. The devil is
in classiﬁcation: A simple framework for long-tail instance
segmentation. In ECCV, 2020. 3, 11
[54] Xinlong Wang, Tao Kong, Chunhua Shen, Yuning Jiang, and


Lei Li.
SOLO: Segmenting objects by locations.
CoRR,
abs/1912.04488, 2019. 2
[55] Tong Wu, Qingqiu Huang, Ziwei Liu, Yu Wang, and Dahua


Lin. Distribution-balanced loss for multi-label classiﬁcation
in long-tailed datasets. In ECCV, 2020. 2
[56] Saining Xie, Ross Girshick, Piotr Dollar, Zhuowen Tu, and


Kaiming He. Aggregated residual transformations for deep
neural networks. In CVPR, 2017. 8
[57] Hang Zhang, Kristin Dana, Jianping Shi, Zhongyue Zhang,


Xiaogang Wang, Ambrish Tyagi, and Amit Agrawal. Con-
text encoding for semantic segmentation. In CVPR, 2018.
11
[58] Hang Zhang, Chongruo Wu, Zhongyue Zhang, Yi Zhu, Zhi


Zhang, Haibin Lin, Yue Sun, Tong He, Jonas Muller, R.
Manmatha, Mu Li, and Alexander Smola. ResNeSt: Split-
attention networks. arXiv preprint arXiv:2004.08955, 2020.
11
[59] Xizhou Zhu, Han Hu, Stephen Lin, and Jifeng Dai.
De-
formable ConvNets V2: More deformable, better results. In
CVPR, 2019. 11


13
