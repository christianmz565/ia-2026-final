Improving Crowded Object Detection via Copy-Paste


Jiangfan Deng, Dewen Fan, Xiaosong Qiu, Feng Zhou


Algorithm Research, Aibee Inc.
jfdeng100@foxmail.com, {dwfan,xsqiu,fzhou}@aibee.com


Abstract


Crowdedness caused by overlapping among similar objects
is a ubiquitous challenge in the ﬁeld of 2D visual object de-
tection. In this paper, we ﬁrst underline two main effects of
the crowdedness issue: 1) IoU-conﬁdence correlation distur-
bances (ICD) and 2) confused de-duplication (CDD). Then
we explore a pathway of cracking these nuts from the per-
spective of data augmentation. Primarily, a particular copy-
paste scheme is proposed towards making crowded scenes.
Based on this operation, we ﬁrst design a “consensus learn-
ing” strategy to further resist the ICD problem and then ﬁnd
out the pasting process naturally reveals a pseudo “depth” of
object in the scene, which can be potentially used for alle-
viating CDD dilemma. Both methods are derived from mag-
ical using of the copy-pasting without extra cost for hand-
labeling. Experiments show that our approach can easily im-
prove the state-of-the-art detector in typical crowded detec-
tion task by more than 2% without any bells and whistles.
Moreover, this work can outperform existing data augmenta-
tion strategies in crowded scenario.


Introduction
The task of object detection has been meticulously studied
for quite a long time. In the deep learning era, in recent
years, many well-designed methods (Liu et al. 2020a) have
been proposed and raised the detection performance to a sur-
prisingly high level. Nevertheless, there still exist many in-
trinsic problems that are not fundamentally solved. One of
them is the “crowdedness issue”, which usually denotes the
phenomenon that objects belonging to the same category are
highly overlapped together. In a geometrical manner, the ba-
sic difﬁculty stems from the semantical ambiguities of the
2D space. As shown in Fig. 1, in our 3D world, each voxel
has its “unique semantics” and lies on a “certain object”.
However, after projecting to 2D plane, one pixel might fall
on several collided objects. After evolving the concept from
a “pixel” to a “box”, the semantical ambiguity in crowded
scenes leads to the notion of overlap.


To probe the effects of this problem, we now dive into the
essence of the detection paradigm. Generally, an object de-
tector reads in an image and outputs a set of bounding-boxes
each associated with a conﬁdence score. For an ideally-
performed detector, the score value should convey how
well the predicted box is overlapped with the ground-truth.
In other words, the Intersection-over-Union (IoU) between


Pixel ambiguity 
in the 2D space


Box ambiguity (overlap) 


in the 2D space


3D
2D


Figure 1: Semantic ambiguities in the 2D space. We ex-
hibit the same scenario in the real 3D world (left) and the
2D space after photographing (right) respectively. The col-
ored boxes represent two distinct objects (pucksters) while
the green points denote a voxel in 3D space and its corre-
sponding pixel in the 2D image. It is clearly illustrated that
the 3D voxel lies on the body of a unique puckster while the
2D pixel lies on both of them. After evolving from a point to
a bounding-box, the ambiguity arises in the form of overlap.


these two boxes should be positively correlated with the con-
ﬁdence score. After visualizing the mean and standard devi-
ation of scores with respect to IoU in Fig. 2, it turns out
that even for the off-the-shelf detectors like (He et al. 2017),
this positive correlation would be gradually disturbed by the
increase of crowdedness degree1. This experimental study
clearly indicates the struggle of current detection algorithms
in facing the super-heavy overlaps. We embody this effect
as IoU-conﬁdence Correlation Disturbances (ICD). On the
other hand, a typical detection pipeline often ends with a de-
duplication module, for example, the widely adopted Non-
Maximum Suppression (NMS). Due to the 2D semantical
ambiguity mentioned previously, these modules are often
confused by heavily overlapped predictions, which leads to
severe missing in a crowd. We cast this type of effect as Con-
fused De-Duplication (CDD).


To overcome these two obstacles, we explore a pathway
from the perspective of data augmentation. Referring to the
preceding works (Ghiasi et al. 2021; Dwibedi, Misra, and
Hebert 2017; Li et al. 2021; Dvornik, Mairal, and Schmid
2018; Fang et al. 2019), a simple copy-paste variant is pro-


1The crowdedness degree is indicated in terms of “occlusion
ratio”, i.e., 1 −sv/sf, where the sv and sf represent size of the
visible box and full box of an object.


arXiv:2211.12110v1  [cs.CV]  22 Nov 2022


Smoother is better
Lower is better


Figure 2: IoU-conﬁdence correlation disturbances (ICD).
We visualize the conﬁdence score w.r.t the IoU between
the predicted box from (He et al. 2017) and ground-truth
in CrowdHuman (Shao et al. 2018). First, the IoU range
of [0, 1] are equally divided into 100 bins (each with the
length of 0.01) as the horizontal axis. Then, average value
(left) or standard deviation (right) of conﬁdence scores are
computed within each bin, generating a corresponding point
in the coordinate plane. Marker shapes of diamond (red),
pentagon (green) and circle (blue) refer to crowdedness de-
grees with the occlusion ratio on three ranges of [0, 0.33],
[0.33, 0.66] and [0.66, 1] respectively. On the left ﬁgure,
the average score curve corresponding to the most crowded
range (blue) are obviously more jittering than the other two
curves; On the right ﬁgure, the heavier the crowdedness is,
the larger the standard deviations are. Both ﬁgures suggest
that the IoU-conﬁdence correlation would become more un-
certain when the crowdedness increases.


posed. Firstly, object segmentation patches are pasted to
the training images following some specialized rules ded-
icated for making crowded scenes. Then, revolved from
copy-pasting, we design a “consensus learning” approach
to align conﬁdence distributions of overlaid objects to their
identical but non-overlaid counterparts, which further re-
strains the ICD problem. Moreover, thanks to the program-
controlled pasting process, we can naturally get the extra or-
der information of which one is in the front and which one is
in the back when two (pasted) objects are overlapped. This
cost-free knowledge provides cues on the additional third
dimension of depth apart from x and y-axis spanning the im-
age plane, which can be deemed as a breakthrough of the
aforementioned 2D restrictions inducing the CDD dilemma.
From this motivation, we propose a concept named “over-
lay depth” and semi-supervisely train the detector to predict
this label. Then, an Overlay Depth-aware NMS (OD-NMS)
is introduced to make use of the depth knowledge during
de-duplication. Experiments show that this strategy can help
distinguish boxes gathered in 2D space and further boost the
detection results.


We evaluate our method from multiple aspects. As a data
augmentation strategy, this work can outperform other coun-
terparts in crowded scenes, no matter hand-craft methods
or automated ones. As an approach of countering crowd-
edness issue, our method can stably improve the state-of-
the-art detector by more than 2% without any bells and
whistles. Moreover, since hand-labeling the crowded data is
resource-consuming, this method provides a way of training
on “sparse data” only and applying to crowded scenes via


data augmentation.


To sum up, the major contributions of this work are two-
fold: (1) We propose a crowdedness-oriented copy-paste
scheme and introduce a consensus learning strategy, which
effectively helps the detector resisting the ICD problem and
bring improvements in crowded scenes. (2) We design a sim-
ple method to utilize the weak depth knowledge produced by
the pasting process, which further optimize the detector.


Related Works


Crowded Object Detection. Detecting objects in crowded
scenes has been a long-standing challenge (Liu et al. 2020a)
and much effort has been spent on this topic. For ex-
ample, (Wang et al. 2018) and (Zhang et al. 2018) pro-
pose speciﬁc loss functions to constrain proposals closer to
the corresponding ground-truth and further away from the
nearby objects, thereby enhancing discrimination between
overlapped individuals. CaSe (Xie et al. 2020) uses a new
branch to count pedestrian number in a region of interest
(RoI) and generates similarity embeddings for each pro-
posal. As a response to the CDD problem mentioned above,
a group of works focuses on alleviating the deﬁciency of
Non-Maximum Suppression (NMS). Adaptive-NMS (Liu,
Huang, and Wang 2019) introduces an adaptation mech-
anism to dynamically adjust the threshold in NMS, lead-
ing to better recall in a crowd. In (G¨ahlert et al. 2020)
and (Huang et al. 2020), NMS leverages the less-occluded
visible boxes to guide the selection of full boxes, whereas
extra labeling (of the visible boxes) is required. Crowd-
Det (Chu et al. 2020) conducts one proposal to make mul-
tiple predictions and uses an artfully designed Set-NMS to
solve heavily-overlapped cases. Some recent works explore
other ways. (Zhang et al. 2021) models the pedestrian detec-
tion task as a variational inference problem. (Zheng et al.
2022) reﬁnes the end-to-end detector Sparse R-CNN (Sun
et al. 2021) to adapt to the crowded detection scenario.


Data Augmentation in Object Detection. In the ﬁeld of
computer vision, data augmentation (Shorten and Khoshgof-
taar 2019) has long been used to optimize the model train-
ing, which originates mainly from the image classiﬁcation
task (He et al. 2016; Tan and Le 2019). Early approaches
usually include strategies such as color shifting (Szegedy
et al. 2014) and random crop (Krizhevsky, Sutskever, and
Hinton 2012; LeCun et al. 1998; Simonyan and Zisser-
man 2015; Szegedy et al. 2014). Naturally, the core ideas
were transferred to the detection domain and some oper-
ations (e.g., image ﬂipping and scale jittering) have been
widely adopted as a standard module (Liu et al. 2016; Red-
mon et al. 2016; Ren et al. 2015). Currently, methods with
more concrete theoretical basis have emerged. These vari-
ants, ranging from hand-crafted Cutout (Devries and Taylor
2017), Mixup (Zhang et al. 2017) and CutMix (Yun et al.)
to learning based AutoAugment (Cubuk et al. 2018), Fast
AutoAugment (Lim et al. 2019) and RandAugment (Cubuk
et al. 2020), perform considerable effects on image clas-
siﬁcation and suggest huge potential in object detection.
Meanwhile, there are also some works focusing on detection
task. Stitcher (Chen et al. 2020) and YOLOv4 (Bochkovskiy,


Wang, and Liao 2020) introduce mosaic inputs containing
rescaled image patches to enhance robustness. (Zoph et al.
2020) and (Chen et al. 2021) re-design the AutoAugment
scheme to adapt to object detection. In (Tang et al. 2021), re-
searchers propose a method searching the policy of data aug-
mentation and loss function jointly. In (Liu et al. 2020b), a
novel APGAN is proposed to transfer pedestrians from other
datasets in making augmentation.


Copy-Paste Augmentation. Copy-paste augmentation is
ﬁrst invented in (Dwibedi, Misra, and Hebert 2017). By cut-
ting object patches from the source image and pasting to
the target one, a combinatorial amount of synthetic train-
ing data can be easily acquired and improve the detec-
tion/segmentation performance signiﬁcantly. This amazing
magic power is then veriﬁed by subsequent works (Remez,
Huang, and Brown 2018; Li et al. 2021; Fang et al. 2019;
Dvornik, Mairal, and Schmid 2018; Ghiasi et al. 2021) and
the method has been further polished by context adapta-
tion (Fang et al. 2019; Remez, Huang, and Brown 2018;
Dvornik, Mairal, and Schmid 2018). In (Ghiasi et al. 2021),
the authors claim that simple copy-paste can bring con-
siderable improvement as long as the training is sufﬁcient
enough. Their experiments further suggest the potential of
this augmentation strategy on instance-level image under-
standing. It should be noted that the initial motivation of
copy-paste is to diversify the sample space, especially for
the rare categories (Ghiasi et al. 2021) or alleviating the
complex mask labeling (Remez, Huang, and Brown 2018).
However, in our work, we utilize this operation to precisely
solve the crowdedness issue. Although there has been sim-
ple practice in previous works (Dwibedi, Misra, and Hebert
2017; Ghiasi et al. 2021), the actual effects of this strategy
on dealing with crowdedness scenario has never been sys-
tematically designed and studied.


Resist the IoU-Conﬁdence Disturbances
This part focuses on solving the Iou-Conﬁdence Distur-
bances (ICD). We explore two consecutive ways in achiev-
ing this aim. First, doing copy-paste to make crowded
scenes. Then, introducing consensus learning between over-
laid objects and their non-overlaid counterparts, which relies
on the copy-pasting.


Crowdedness Oriented Copy-Paste
Based on observations of Fig. 2, an intuitive idea is to make
more crowded cases to dominate the training. To this end,
we carefully re-design the copy-paste strategy. First, the con-
ception of “group” is introduced. An image should include
several groups and each group consists of multiple heav-
ily overlapped objects. Following this logic scheme, we ﬁrst
generate the group centers on an image and then paste ob-
jects around them.


Formally, for every training image to be augmented, we
initialize a set C of “group centers”:


C = {(x1, y1, s1), ..., (x|C|, y|C|, s|C|)},
where each tuple represents the object locating at center of
the corresponding group (xi, yi and si denote the coordi-
nates and normalized object size respectively). We obtain


these group centers by sampling from original objects on
the current image. The group number |C| is randomly cho-
sen from an integral range of [0, N], where N is a hyper pa-
rameter.


The second step is pasting objects around these group cen-
ters. For each ci ∈C, we should generate a set ˆGi of objects
in the group i:


ˆGi = {(ˆxi


1, ˆyi
1, ˆsi
1), ..., (ˆxi
| ˆGi|, ˆyi


| ˆGi|, ˆsi


| ˆGi|)},


similarly, object number | ˆGi| in the group comes from range
[0, M] where M is another hyper parameter. Since the nature
of crowdedness is “overlapping”, every ˆgi


j ∈ˆGi is enforced
to be overlapped with the group center object ci. We ma-
nipulate the overlapping from three aspects of the x, y and s
conditioning in a probabilistic sense.


First, objects in a group usually have similar sizes. Let
p(ˆsi


j|si, I) be the probability density function of ˆsi


j on con-
ditions of the center object size si in the image I. We choose
p(·) to be a Gaussian as:


p(ˆsi


j|si, I) =
1
√


2πσ exp(−(ˆsi
j −si)2


2σ2
),
(1)


where σ is the standard deviation which a constant value 0.2
is used in this paper. To guarantee overlapping, we adopt
two independent uniform distributions in modeling the co-
ordinate values ˆxi


j and ˆyi


j:


ˆxi


j ∼U(xi −dw


τ , xi + dw


τ ),
(2)


ˆyi


j ∼U(yi −dh


ϵ , yi + dh


ϵ ),
(3)


where dw and dh are the maximum distances of ˆgi


j shifting
from group center ci with overlap. Coefﬁcients τ > 1 and
ϵ > 1 are used to adjust the crowdedness degree.


During training, for every image loaded, the set C and ˆGi-
s are generated obeying rules above. Then object segmenta-
tion patches would be sampled, re-scaled and pasted to the
image accordingly.


Consensus Learning
With the toolkit of copy-pasting, we augment detector train-
ing with a dedicated strategy for resisting the ICD issue.
Given the observation shown in Fig. 2 that the instability of
predicted scores derives from crowdedness, an emerging ﬁx
is to align the score of an object in crowded circumstances
(overlaid by other objects) to that when it is not overlaid.
Thanks to the copy-paste method, we can easily generate
this type of object pairs in which two identical objects lie in
different surroundings. Fig. 3 illustrates our idea. Following
the previous data augmentation, we pick out a set Bovl of
objects which are overlaid by others. Then, the same object
patches with those in Bovl are re-pasted to the image without
been overlaid, constructing another set B∗


ovl. During train-
ing, we enforce the predicted score distributions of each ob-
ject bi ∈Bovl in an alignment with its counterpart b∗


i ∈B∗


ovl.
We term this process as consensus learning by drawing an
analogy of “reaching consensus” within each pair. Speciﬁ-
cally, let Pi be the set of proposals matched to bi and P∗


i


𝒑𝒊𝟐


𝒑𝒊𝟑


𝒑𝒊𝟏


∗


𝒑𝒊𝟐


∗


𝒑𝒊𝟑


∗
score distr.
score distr.


Consensus 


Learning


𝒑𝒊𝟏


(𝜇!, 𝜎! )
(𝜇!


∗, 𝜎!


∗)
Eq.(6)


Figure 3: Consensus Learning. Learn to reach consensus
between the overlaid object (the man in red on the left) and
its identical but non-overlaid counterpart (right).


be the set of proposals matched to b∗


i . We ﬁrst compute the
mean µ and standard deviation σ of scores for each object:


µi = 1


m


X


pij∈Pi


c(pij),
σi =


v
u
u
t 1


m


X


pij∈Pi


(c(pij) −µi)2, (4)


µ∗


i =
1
m∗


X


p∗


ij∈P∗


i


c(p∗


ij), σ∗


i =


v
u
u
t 1


m∗


X


p∗


ij∈P∗


ij


(c(p∗


i ) −µ∗


i )2,


(5)
where m and m∗are the sizes of Pi and P∗


i respectively and
c(·) denotes the predicted conﬁdence score of a proposal.
Then we pursue a pair of {µi, σi} approaching {µ∗


i , σ∗


i }
through the mean squared error (MSE) loss:


Lcl =
1
|Bovl|


X


bi∈Bovl


(µi −µ∗


i )2 + (σi −σ∗


i )2.
(6)


It is worth to point that only the overlaid half {µi, σi} con-
tributes to the gradient back-propagation while the non-
overlaid half (marked by ∗) is treated as target.


Analyze the IoU-Conﬁdence Disturbances
Now we analyze the effectiveness of our method on miti-
gating the aforementioned ICD issue. To revisit the origi-
nal motivation raised from the right of Fig. 2, we plot the
standard deviation (STD) of scores in Fig. 4. First, it is
clearly demonstrated that score STDs of the model trained
with our Crowdedness-oriented Copy-Paste (CCP) are obvi-
ously lower than those of the baseline model (BL) and the
gap becomes larger by improving the crowdedness degree
(from Fig. 4-(a) to (d)). Second, although the curves of CCP
and CCP+CL seems with no clear distinction, after comput-
ing their average STDs (the four histograms in Fig. 4), we
ﬁnd the value of the latter is actually lower than that of the
former. Moreover, we plot another model augmented with
random copy-paste (RCP) without specially taking crowd-
edness into consideration. It is obvious that the decline of
score STDs is with a much smaller margin. These observa-
tions convince that our method can signiﬁcantly improve the
detector’s robustness in crowded scenes and therefore alle-
viate the ICD problem.


Alleviate the Confused De-Duplications
Our augmentation strategy has a natural by-product: for
these overlapped objects pasted, the relative “order of depth”


standard deviation of scores


(a)
(b)


(c)
(d)


IoU between dets and gts


occ: [0, 0.25]
occ: [0.25, 0.5]


occ: [0.5, 0.75]
occ: [0.75, 1]


0.1970.192
0.184
0.177


0.256
0.246
0.234
0.227


0.281
0.271
0.251
0.245


0.289
0.273
0.253
0.249


Figure 4: Effects of our method on the ICD issue, lower
is better. We plot only the standard deviation of conﬁdence
scores w.r.t the IoU value on CrowdHuman. The crowded-
ness (occlusion ratio) gradually increases from (a) to (d).


is known a priori. In other words, we are aware of which one
is in the front and which one is in the back. Now let us re-
turn to the semantical ambiguity described in Sec.. Basically,
ambiguities in 2D space are caused by the absence of one
dimension in the real (3D) world. From this point of view,
the depth order can be viewed as some weak knowledge of
the additional third dimension, which shed light on mitigat-
ing the vagueness. As a feasible practice, in this work, we
utilize the depth order information to resolve the confused
de-duplication (CDD) problem.


First, we introduce a variable named “overlay depth”
(OD) that depicts the extent of how an object is visually
overlaid by others. Fig. 5 demonstrates the process of cal-
culating OD. We start by assuming that the overlay depth of
an object equals to 1.0 if there are no other objects covering
it. Let ovl(b1, b2) be the region of object b1 overlaid by ob-
ject b2 and S(·) denote the size of a region. For any object
bi in the image, there exists a set Oi of objects overlying bi:


Oi = {bj ∈B|bj̸ = bi, S(ovl(bi, bj)) > 0},
(7)


where B is the set of all objects in current image. Then, the
OD value of bi can be clearly deﬁned:


odi = 1.0 +
1
S(bi)


X


bj∈Oi


S(ovl(bi, bj)).
(8)


Therefore, the severer an object is occluded by others (ob-
jects of the same category), the higher OD value it would be
assigned (such as objects b1 and b2 in Fig. 5). Starting from
this property, application of the overlay depth is based on a
plausible observation: two heavily overlapped objects usu-
ally lie in different depth, or more speciﬁcally, hold distinct
OD values. So by taking extra knowledge from the axis of
depth, the OD value can be adopted during de-duplication in
a confused 2D plane.


Now we enable the detector to predict the OD values.
Generally, a detection model takes a branch to regress the
coordinates of the bounding-box. Following this design, we
add an extra predictor to the branch in taking responsibility


1
1+1


1+1+1


1


1+1


1


𝑜𝑑! = 1.25


𝑜𝑑" = 1.66


𝑜𝑑# = 1.0


𝑜𝑣𝑙𝑏", 𝑏#


𝑜𝑣𝑙𝑏!, 𝑏"


𝑜𝑣𝑙𝑏!, 𝑏#


𝑏!


𝑏"


𝑏#


Figure 5: Deﬁnition of overlay depth (OD). Calculation
process of the OD value as deﬁned in Eq.(11). Boxes of b1,
b2 and b3 are three overlapped objects (skaters), in which b2
is overlaid by b3 only while b1 is overlaid by both b2 and b3.


for the OD regression. This modiﬁcation incurs neglectable
computing burden and can be easily implemented in both
one-stage and two-stage structures (refer to the Appendix
for details). During training, a common L2 loss is adopted.
It should be emphasized that only the OD of pasted objects
can be acquired due to the semi-supervised knowledge of the
overlay depth. So we activate the OD regression loss only
when the ground-truth is available. Formally, the whole loss
can be written as below:


Ldet =


α · Lcls reg + γ · Lcl + η · Lod
if od available
α · Lcls reg + γ · Lcl
elsewise,


(9)
where Lcls reg is the conventional detection loss, Lcl is the
consensus learning loss and Lod is OD regression loss re-
spectively. We use α = γ = 1 and η = 0.1 in this paper.


Algorithm 1: Overlay Depth-aware NMS


Input: B = {b1, ..., bN}: All boxes; S = {s1, ..., sN}:
Scores; thiou: IoU threshold.
D ←∅
while B̸ = ∅do


m ←argmax{S}
M ←bm; D ←D S M; B ←B −M
for bi in B do


thod = δ · eψ·IoU(M,bi)
if IoU(M, bi) ⩾thiou and |odi −odm| ⩽thod
then


B ←B −bi; S ←S −si
end if
end for
end while


During inference, we invent a novel de-duplication strat-
egy named Overlay Depth-aware NMS (OD-NMS). In the
original NMS pipeline, boxes are recursively compared with
each other and one of them would be suppressed in each step
if the IoU exceeds a threshold thiou. Following this scheme,
objects might be de-duplicated by mistake in a crowded sce-
nario. In our OD-NMS, for difﬁcult scenario where IoU is
higher than thiou, we integrate the predicted OD value into


a more comprehensive decision. If the two objects are in dif-
ferent depth, i.e., the absolute difference of the two OD val-
ues is higher than a predeﬁned threshold thod, we can cancel
the suppression in the current step. Empirically, ambiguous
cases often raise in the range of large IoU: when two boxes
are more heavily overlapped, we need stricter OD threshold
to judge if they are distinct objects. So we design a dynamic
threshold of OD with respect to the IoU value:


thod = δ · eψ·IoU,
(10)


where δ and ψ are constant coefﬁcients.


Algorithm 1 summarizes the whole process. In this way,
objects in a crowded scenario can be effectively recalled in-
stead of being inappropriately de-duplicated. This strategy
can be viewed as an evolvement of the original NMS with
comparable time complexity.


Experiment


Datasets. Pedestrian detection is the most typical task bur-
dened by the crowdedness problem, so our experiments
are conducted mainly on two datasets: CrowdHuman (Shao
et al. 2018) and CityPersons (Zhang, Benenson, and Schiele
2017). Annotations in these datasets consist of a full box and
a visible box for each person, in which we only adopt the
full ones to make the data crowded enough. Since both the
training and validation data hold the same level of crowded-
ness, we prepare another “sparse training set” by re-labeling
full body box of persons in COCO (Lin et al. 2014) to fur-
ther evaluate the potential of our method. We name this train
set as COCO-fullperson (we will release this dataset). More-
over, we use the category of “car” in KITTI (Geiger, Lenz,
and Urtasun 2012) to further estimate the generality of our
work in other types of objects.


Augmentation Details. For pasting instance generation, we
choose the open source Mask R-CNN (He et al. 2017) model
adopting ResNet-50 (He et al. 2016) as backbone. We run
this model on the train set and select 1000 instances with
only three rough criteria: high conﬁdence, relatively large
size and not been occluded. A group of ﬁxed hyper param-
eters are used in our experiments, where sample numbers
N = 3 and M = 5, shifting coefﬁcients τ = 4, ϵ = 2 and
OD-NMS coefﬁcient δ = 0.001, ψ = 10. Copy-paste aug-
mentation strategies are processed online within each train-
ing step, along with the generation of the semi-supervised
OD ground-truths according to Eq.(11). We start consensus
learning at the 10-th epoch during training.


Experimental Settings. We conduct experiments on both
two-stage and one-stage detection frameworks. For two-
stage structure, we use the standard Faster R-CNN (Ren
et al. 2015) with FPN (Lin et al. 2017a). For one-stage struc-
ture, we choose RetinaNet (Lin et al. 2017b) as a represen-
tative. All those detectors use ResNet-50 as backbone. We
train the networks on 8 Nvidia V100 GPUs with 2 images on
each GPU. We also apply our method to the state-of-the-art
pedestrian detectors CrowdDet (Chu et al. 2020) and ProgS-
RCNN (Zheng et al. 2022). Other training details will be
reported in the following subsections.


MR−2
AP@0.5
AP@0.5:0.95
JI
Aug Method
on Faster R-CNN
Baseline
50.42
84.95
-
-
Baseline+
42.46
87.07
52.70
79.77
Mosaic
43.71
85.21
52.66
78.35
RandAug
42.17
87.48
53.19
80.40
SAutoAug
42.13
87.64
53.35
80.39
SimCP
41.88
87.36
53.36
79.53
CrowdAug (Ours)
40.21
88.61
54.88
81.41
Aug Method
on RetinaNet
Baseline
63.33
80.83
-
-
Baseline+
50.65
83.80
49.63
76.40
Mosaic
52.53
82.95
48.87
75.60
RandAug
50.25
83.94
49.77
76.58
SAutoAug
50.21
84.02
49.85
76.80
SimCP
50.01
84.12
50.05
77.02
CrowdAug (Ours)
47.35
85.29
51.84
77.79
on SOTA pedestrian detectors
CrowdDet
41.35
90.06
55.02
82.07
ProgS-RCNN
41.45
92.15
58.17
83.13
CrowdDet + AutoPedestrian
40.58
-
-
-
CrowdDet + Ours
38.98
91.50
57.65
83.89
ProgS-RCNN + Ours
40.12
92.31
58.20
83.35


Table 1: Results on CrowdHuman val set. The Baseline+ de-
notes newly trained strong baselines. Results are in percentage (%).


Results on CrowdHuman


Four metrics are used to evaluate results on CrowdHuman:
the log-average miss rate on False Positive Per Image (FPPI)
in the range of [10−2, 100] (shortened as MR−2, lower is
better), the Average Precisions (AP@0.5 and AP@0.5:0.95,
higher is better) and the Jaccard Index (JI, higher is better),
among which the MR−2 is the main indicator. To make our
experiments convincing enough, we use very strong base-
lines (the Baseline+s in Table 1), which are 8%-12% supe-
rior than those in the CrowdHuman paper (Shao et al. 2018).
During training, the short side of each image is resized to
800 and the long side is limited within 1400. Models are
trained for 60k iterations starting from an initial learning rate
of 0.02 (Faster R-CNN) or 0.01 (RetinaNet) and is reduced
by 0.1 on 30k and 40k iters respectively. Table 1 compares
results of our method (CrowdAug) with other approaches.
First, the widely used Mosaic augmentation (Bochkovskiy,
Wang, and Liao 2020) leads to a decline. This phenomenon
is mainly attributed to the fact that in CrowdHuman, many
boxes extend across image boundary. After the mosaic op-
eration, these near-boundary boxes are truncated at the
joints of image patches, losing original characteristics. We
also make trials of two automated strategies: the Random-
Augmentation (RandAug) (Cubuk et al. 2020) and the Scale-
Aware Auto-Augmentation (SAutoAug) (Chen et al. 2021).
It needs to be noted that in these works, the search space
does not include policies in dealing with crowded scene,
which we hypothesize is the main reason of their marginal
effects. The Simple Copy-Paste (Ghiasi et al. 2021) (SimCP
in Table 1)improves the detector by nearly 0.6%. Instead,
our CrowdAug can consistently improve the detection re-
sults by 2.2% and 3.3% for Faster R-CNN and RetinaNet re-
spectively from the strong baselines. Moreover, the proposed
method has exceptional performance on the state-of-the-art
(SOTA) pedestrian detectors CrowdDet (Chu et al. 2020)
and ProgS-RCNN (Zheng et al. 2022). As shown in the last


MR−2
AP@0.5
AP@0.5:0.95
JI
Faster R-CNN
53.51
85.30
46.33
77.21
Faster R-CNN + Ours
50.12
86.40
48.52
78.50
RetinaNet
59.45
80.86
41.71
74.22
RetinaNet + Ours
56.80
81.42
43.41
75.30


Table 2: Results of model trained on COCO-fullperson and evalu-
ated on CrowdHuman val set. We list results on Faster R-CNN and
RetinaNet respectively.


MR−2
AP@0.5
MR−2
AP@0.5
CCP
CL
OD
on Faster R-CNN
on RetinaNet
42.46
87.07
50.65
83.80
(RCP)
42.01
87.10
49.75
84.02
√
41.11
87.75
48.81
84.73
√
√
40.80
88.02
47.93
84.85
√
√
√
40.21
88.61
47.35
85.29


Table 3: Ablation results on CrowdHuman val set. Experiments
are conducted on Faster R-CNN and RetinaNet respectively.


two lines of Table 1. On CrowdDet, our method can achieve
an improvement of 2.37% and reach a new SOTA of 38.98%
in MR−2. On ProgS-RCNN (only the CCP is applied since
the CL and OD-NMS is not needed for end-to-end detector),
our method can bring an enhancement of 1.33%. The pro-
posed CrowdAug can also outperform the previously SOTA
augmentation strategy AutoPedestrian (Tang et al. 2021) by
1.6% in MR−2. These experiments conﬁrm that the Crow-
dAug can effectively optimize the crowded detection even
on a supremely high base.


We also train the detector on the “sparse” dataset COCO-
fullperson and report results on the “crowded” CrowdHu-
man val set in Table 2. Since training samples are generally
not crowded, the CrowdAug can bring signiﬁcant improve-
ment (more than 3% in MR−2). These results suggest that
our method can largely help the detector to handle crowded
scenes when there is limited or even no crowded data avail-
able for training.


Ablation Study
Crowdedness-oriented Design. The third line of Table 3
shows the contribution of our augmentation strategy (CCP).
Take the Faster R-CNN as an example. The CCP can im-
prove the detection result by nearly 1.3%. For comparison,
we try the random copy-paste (RCP) mentioned in Sec.. In
this strategy, average number and size distribution of past-
ing objects are kept the same with those in our CCP while
the positions to paste are randomly allocated rather than
specially making crowded scenes. The 2nd line of Table 3
shows that the RCP improves the baseline by 0.45%, which
is inferior to our CCP. These results demonstrate that oper-
ations in boosting the crowdedness are necessary and effec-
tive. As discussed in Sec., we think the improvement comes
mainly from resisting the ICD issue.


Consensus Learning. As shown in the 4-th line of Table 3,
the proposed consensus learning (CL) strategy can further
enhance the the Faster R-CNN by 0.3% from CCP baseline.
This improvement becomes much larger (0.88%) when ap-
plying the CL to RetinaNet. Additionally, with qualitative
analysis in Sec., we can make a conclusion that this module


Figure 6: Visualization of the OD prediction. The value
of predicted overlay depth (OD) is marked at the top left
corner of each box. The red boxes denote the persons who
are wrongly deleted by the original NMS while recalled by
our OD-NMS.


Pasting Object Numbers
MR−2
AP@0.5
AP@0.5:0.95
JI
1000 (default)
40.21
88.61
54.88
81.41
3000
40.25
88.53
54.85
81.39
500
40.23
88.57
54.88
81.40
1000 sel
40.20
88.60
54.90
81.32
1000 sel+mask gt
40.21
88.62
54.86
81.42


Table 4: Robustness to Pasting Objects. The “sel” denotes man-
ually selected high-quality objects and the “mask gt” means using
segmentation annotations instead of those predicted by the Mask
R-CNN model.


makes a step further in alleviating the ICD problem.


Overlay Depth. Comparing the last two lines of Table 3
can ﬁnd out contribution of the overlay depth (OD). As a
breakthrough of the 2D constraint, this weak depth knowl-
edge brings a stable enhancement.We make visualizations of
the OD prediction in Fig. 6. It can be seen that although the
training process is semi-supervised, overlay depths learned
by the detector are quite discriminative and can recall miss-
ing pedestrians (red dotted boxes in Fig. 6) of the baseline
model. In the structure design, the simplicity of our OD pre-
dictor guarantees the ease of use during application.


Robustness to Pasting Objects. Our method is robust to
the quantity and quality of pasting objects. First, we experi-
ment the CrowdAug on a variety of pasting objects numbers.
Then, we manually select 1000 high-quality object patches
and train a comparing model (the 4th line in Table 4). Fi-
nally, we replace the mask of the object patches above with
the segmentation annotations in COCO (Lin et al. 2014) to
get more precise masks and make another experiment (the
5th line in Table 4). Results show that variations of either
quantity or quality of pasting objects will not essentially ef-
fect the ﬁnal performance, which suggest that our method
does not have strict requirement of the training data and with
huge potential of application.


Method


MR−2


AP@0.5
Reasonable
Partial
Bare
Heavy
Faster R-CNN
11.20
11.55
6.62
52.05
82.95
Faster R-CNN + Mosaic
11.05
11.42
6.77
51.62
83.01
Faster R-CNN + RandAug
10.84
11.20
6.31
51.27
82.97
Faster R-CNN + APGAN
11.9
11.9
6.8
49.6
-
Faster R-CNN + AutoPedestrian
10.3
-
-
49.4
-
Faster R-CNN + Ours
10.02
10.48
5.79
48.50
83.78
RetinaNet
13.60
14.32
7.22
55.61
79.31
RetinaNet + Mosaic
13.20
14.58
7.50
54.90
79.31
RetinaNet + RandAug
13.23
13.96
7.02
54.61
79.77
RetinaNet + Ours
12.38
13.07
6.49
52.96
80.86


Table 5: Results on CityPersons val set. We list the MR−2 on
four crowdedness levels: reasonable, partial, bare and heavy. The
metric of AP@0.5 is also reported.


Easy
Moderate
Hard
Easy
Moderate
Hard
on Faster R-CNN
on RetinaNet
Baseline
97.24
89.77
79.44
93.72
87.33
76.76
CrowdAug
98.30
91.07
81.69
94.81
88.59
78.63


Table 6: Results on KITTI val set. We use the category of “cars”
in KITTI (Geiger, Lenz, and Urtasun 2012) dataset. AP@0.7 (%)
of easy, moderate and hard objects are listed respectively.


Results on CityPersons


On CityPersons, images are trained and evaluated with in-
put scale of ×1.3. During training, we use an initial learning
rate of 0.02 (Faster R-CNN) or 0.01 (RetinaNet) for the ﬁrst
5k iterations and reduce it by 0.1 continuously on the next
two groups of 2k iterations. Table 5 compares our Crow-
dAug with other methods. The results show that the Crow-
dAug can stably optimize the detector and once the crowd-
edness becomes heavier, the improvement becomes larger.
Meanwhile, the proposed method can also outperform other
counterparts.


Results on KITTI


To estimate the generalization of our method to other
crowded objects, we make experiments on the category of
“cars” in KITTI (Geiger, Lenz, and Urtasun 2012). Table 6
shows the results. After applying the CrowdAug, Average
Precision of cars get improvement if 1.05%, 1.20% and
2.25% for the objects of easy, moderate and hard respec-
tively for the Faster R-CNN structure, which demonstrate
the similar trend of its performance on pedestrian detection.


Conclusion


In this paper, we point out two main effects of crowded-
ness issue in the visual object detection task and propose
a solution from the perspective of data augmentation. First,
we invent a novel copy-paste strategy to improve crowded-
ness and design a consensus learning method. Then, we rea-
sonably use the weak information of depth produced by the
pasting process. Both contributions can help alleviating the
ambiguities of crowded 2D object detection. We think this
is a new pathway of solving the crowdedness issue with the
advantages of signiﬁcant effect and resource conservation.


References
Bochkovskiy, A.; Wang, C.; and Liao, H. M. 2020.
YOLOv4: Optimal Speed and Accuracy of Object Detec-
tion. CoRR, abs/2004.10934.
Chen, Y.; Li, Y.; Kong, T.; Qi, L.; Chu, R.; Li, L.; and Jia, J.
2021. Scale-aware automatic augmentation for object detec-
tion. In Proceedings of the IEEE/CVF Conference on Com-
puter Vision and Pattern Recognition, 9563–9572.
Chen, Y.; Zhang, P.; Li, Z.; Li, Y.; Zhang, X.; Meng, G.; Xi-
ang, S.; Sun, J.; and Jia, J. 2020. Stitcher: Feedback-driven
Data Provider for Object Detection. CoRR, abs/2004.12432.
Chu, X.; Zheng, A.; Zhang, X.; and Sun, J. 2020. Detec-
tion in crowded scenes: One proposal, multiple predictions.
In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, 12214–12223.
Cubuk, E.; Zoph, B.; Mane, D.; Vasudevan, V.; and Le, Q. V.
2018. AutoAugment: Learning Augmentation Policies from
Data.
Cubuk, E. D.; Zoph, B.; Shlens, J.; and Le, Q. 2020. Ran-
dAugment: Practical Automated Data Augmentation with a
Reduced Search Space. In Advances in Neural Information
Processing Systems 33: Annual Conference on Neural Infor-
mation Processing Systems 2020, NeurIPS 2020, December
6-12, 2020, virtual.
Devries, T.; and Taylor, G. W. 2017. Improved Regulariza-
tion of Convolutional Neural Networks with Cutout. CoRR,
abs/1708.04552.
Dvornik, N.; Mairal, J.; and Schmid, C. 2018. Modeling vi-
sual context is key to augmenting object detection datasets.
In Proceedings of the European Conference on Computer
Vision (ECCV), 364–380.
Dwibedi, D.; Misra, I.; and Hebert, M. 2017.
Cut, Paste
and Learn: Surprisingly Easy Synthesis for Instance Detec-
tion. In IEEE International Conference on Computer Vision,
ICCV 2017, Venice, Italy, October 22-29, 2017, 1310–1319.
IEEE Computer Society.
Fang, H.; Sun, J.; Wang, R.; Gou, M.; Li, Y.; and Lu, C.
2019. InstaBoost: Boosting Instance Segmentation via Prob-
ability Map Guided Copy-Pasting. In 2019 IEEE/CVF In-
ternational Conference on Computer Vision, ICCV 2019,
Seoul, Korea (South), October 27 - November 2, 2019, 682–
691. IEEE.
G¨ahlert, N.; Hanselmann, N.; Franke, U.; and Denzler, J.
2020. Visibility guided nms: Efﬁcient boosting of amodal
object detection in crowded trafﬁc scenes. arXiv preprint
arXiv:2006.08547.
Geiger, A.; Lenz, P.; and Urtasun, R. 2012. Are we ready for
Autonomous Driving? The KITTI Vision Benchmark Suite.
In Conference on Computer Vision and Pattern Recognition
(CVPR).
Ghiasi, G.; Cui, Y.; Srinivas, A.; Qian, R.; Lin, T.; Cubuk,
E. D.; Le, Q. V.; and Zoph, B. 2021. Simple Copy-Paste Is
a Strong Data Augmentation Method for Instance Segmen-
tation. In IEEE Conference on Computer Vision and Pattern
Recognition, CVPR 2021, virtual, June 19-25, 2021, 2918–
2928. Computer Vision Foundation / IEEE.


He, K.; Gkioxari, G.; Doll´ar, P.; and Girshick, R. 2017. Mask
r-cnn. In Proceedings of the IEEE international conference
on computer vision, 2961–2969.
He, K.; Zhang, X.; Ren, S.; and Sun, J. 2016. Deep resid-
ual learning for image recognition. In Proceedings of the
IEEE conference on computer vision and pattern recogni-
tion, 770–778.
Huang, Z.; Yue, K.; Deng, J.; and Zhou, F. 2020. Visible
Feature Guidance for Crowd Pedestrian Detection. arXiv
preprint arXiv:2008.09993.
Krizhevsky, A.; Sutskever, I.; and Hinton, G. E. 2012. Im-
ageNet Classiﬁcation with Deep Convolutional Neural Net-
works. In Advances in Neural Information Processing Sys-
tems 25: 26th Annual Conference on Neural Information
Processing Systems 2012. Proceedings of a meeting held
December 3-6, 2012, Lake Tahoe, Nevada, United States,
1106–1114.
LeCun, Y.; Bottou, L.; Bengio, Y.; and Haffner, P. 1998.
Gradient-based learning applied to document recognition.
Proc. IEEE, 86(11): 2278–2324.
Li, C.; Sohn, K.; Yoon, J.; and Pﬁster, T. 2021. CutPaste:
Self-Supervised Learning for Anomaly Detection and Lo-
calization.
In IEEE Conference on Computer Vision and
Pattern Recognition, CVPR 2021, virtual, June 19-25, 2021,
9664–9674. Computer Vision Foundation / IEEE.
Lim, S.; Kim, I.; Kim, T.; Kim, C.; and Kim, S. 2019. Fast
AutoAugment. In Advances in Neural Information Process-
ing Systems 32: Annual Conference on Neural Information
Processing Systems 2019, NeurIPS 2019, December 8-14,
2019, Vancouver, BC, Canada, 6662–6672.
Lin, T.-Y.; Doll´ar, P.; Girshick, R.; He, K.; Hariharan, B.;
and Belongie, S. 2017a. Feature pyramid networks for ob-
ject detection. In Proceedings of the IEEE conference on
computer vision and pattern recognition, 2117–2125.
Lin, T. Y.; Goyal, P.; Girshick, R.; He, K.; and Dollar, P.
2017b. Focal loss for dense object detection. IEEE Transac-
tions on Pattern Analysis & Machine Intelligence, PP(99):
2999–3007.
Lin, T. Y.; Maire, M.; Belongie, S.; Hays, J.; Perona, P.; Ra-
manan, D.; Doll´ar, P.; and Zitnick, C. L. 2014. Microsoft
COCO: Common Objects in Context. 8693: 740–755.
Liu, L.; Ouyang, W.; Wang, X.; Fieguth, P. W.; Chen, J.; Liu,
X.; and Pietik¨ainen, M. 2020a. Deep Learning for Generic
Object Detection: A Survey. Int. J. Comput. Vis., 128(2):
261–318.
Liu, S.; Guo, H.; Hu, J.-G.; Zhao, X.; Zhao, C.; Wang,
T.; Zhu, Y.; Wang, J.; and Tang, M. 2020b. A novel data
augmentation scheme for pedestrian detection with attribute
preserving GAN. Neurocomputing, 401: 123–132.
Liu, S.; Huang, D.; and Wang, Y. 2019. Adaptive nms: Re-
ﬁning pedestrian detection in a crowd. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, 6459–6468.
Liu, W.; Anguelov, D.; Erhan, D.; Szegedy, C.; Reed, S.;
Fu, C.-Y.; and Berg, A. C. 2016. Ssd: Single shot multibox
detector. In European conference on computer vision, 21–
37. Springer.


Redmon, J.; Divvala, S.; Girshick, R.; and Farhadi, A. 2016.
You only look once: Uniﬁed, real-time object detection. In
Proceedings of the IEEE conference on computer vision and
pattern recognition, 779–788.
Remez, T.; Huang, J.; and Brown, M. 2018. Learning to
Segment via Cut-and-Paste.
In Ferrari, V.; Hebert, M.;
Sminchisescu, C.; and Weiss, Y., eds., Computer Vision -
ECCV 2018 - 15th European Conference, Munich, Germany,
September 8-14, 2018, Proceedings, Part VII, volume 11211
of Lecture Notes in Computer Science, 39–54. Springer.
Ren, S.; He, K.; Girshick, R.; and Sun, J. 2015. Faster R-
CNN: towards real-time object detection with region pro-
posal networks. In International Conference on Neural In-
formation Processing Systems, 91–99.
Shao, S.; Zhao, Z.; Li, B.; Xiao, T.; Yu, G.; Zhang, X.; and
Sun, J. 2018. CrowdHuman: A Benchmark for Detecting
Human in a Crowd. arXiv preprint arXiv:1805.00123.
Shorten, C.; and Khoshgoftaar, T. M. 2019. A survey on
Image Data Augmentation for Deep Learning. J. Big Data,
6: 60.
Simonyan, K.; and Zisserman, A. 2015. Very Deep Convo-
lutional Networks for Large-Scale Image Recognition. In
3rd International Conference on Learning Representations,
ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Confer-
ence Track Proceedings.
Sun, P.; Zhang, R.; Jiang, Y.; Kong, T.; Xu, C.; Zhan, W.;
Tomizuka, M.; Li, L.; Yuan, Z.; Wang, C.; et al. 2021. Sparse
r-cnn: End-to-end object detection with learnable proposals.
In Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition, 14454–14463.
Szegedy, C.; Liu, W.; Jia, Y.; Sermanet, P.; and Rabinovich,
A. 2014. Going Deeper with Convolutions. IEEE Computer
Society.
Tan, M.; and Le, Q. 2019. Efﬁcientnet: Rethinking model
scaling for convolutional neural networks. In International
conference on machine learning, 6105–6114. PMLR.
Tang, Y.; Li, B.; Liu, M.; Chen, B.; Wang, Y.; and Ouyang,
W. 2021. Autopedestrian: an automatic data augmentation
and loss function search scheme for pedestrian detection.
IEEE transactions on image processing, 30: 8483–8496.
Wang, X.; Xiao, T.; Jiang, Y.; Shao, S.; Sun, J.; and Shen,
C. 2018. Repulsion loss: Detecting pedestrians in a crowd.
In Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition, 7774–7783.
Xie, J.; Cholakkal, H.; Anwer, R. M.; Khan, F. S.; Pang, Y.;
Shao, L.; and Shah, M. 2020. Count-and similarity-aware
r-cnn for pedestrian detection. In European Conference on
Computer Vision, 88–104. Springer.
Yun, S.; Han, D.; Chun, S.; Oh, S. J.; Yoo, Y.; and Choe, J.
???? CutMix: Regularization Strategy to Train Strong Clas-
siﬁers With Localizable Features. In International Confer-
ence on Computer Vision.
Zhang, H.; Cisse, M.; Dauphin, Y. N.; and Lopez-Paz, D.
2017. mixup: Beyond Empirical Risk Minimization.
Zhang, S.; Benenson, R.; and Schiele, B. 2017. Citypersons:
A diverse dataset for pedestrian detection. In Proceedings


of the IEEE Conference on Computer Vision and Pattern
Recognition, 3213–3221.
Zhang, S.; Wen, L.; Bian, X.; Lei, Z.; and Li, S. Z. 2018.
Occlusion-aware R-CNN: detecting pedestrians in a crowd.
In Proceedings of the European Conference on Computer
Vision (ECCV), 637–653.
Zhang, Y.; He, H.; Li, J.; Li, Y.; See, J.; and Lin, W.
2021. Variational pedestrian detection. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, 11622–11631.
Zheng, A.; Zhang, Y.; Zhang, X.; Qi, X.; and Sun, J.
2022. Progressive End-to-End Object Detection in Crowded
Scenes.
In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, 857–866.
Zoph, B.; Cubuk, E. D.; Ghiasi, G.; Lin, T.; Shlens, J.; and
Le, Q. V. 2020. Learning Data Augmentation Strategies for
Object Detection. In Computer Vision - ECCV 2020 - 16th
European Conference, Glasgow, UK, August 23-28, 2020,
Proceedings, Part XXVII, 566–583. Springer.


classification


box regression 
𝑓𝑐!


RoI


𝐿!"#


𝑳𝒐𝒅


training


𝑓𝑐"


×4


×4


classification


box regression


𝐿!"#


𝐿&'(


𝑳𝒐𝒅


training


Two-stage


One-stage


1024d
1024d


H × W × 256
H × W × 256
H × W × 256


𝐿&'(


overlay depth


H × W × 256
H × W × 256
H × W × 256


overlay depth


Figure A 7: Structure of the OD predictor. The OD pre-
dictor (plotted with green) on typical two-stage (top) and
one-stage (bottom) detection frameworks.


Structure of the OD Predictor


Fig.A7 illustrates the details of our overlay depth (OD) pre-
dictor. On two-stage framework, this module is in parallel
with the predictor for classiﬁcation and bounding-box re-
gression, sharing the same head following RoI-Pooling. On
one-stage framework, the OD predictor is derived from the
regression branch. It is obvious that the newly added module
is ultra light-weighted.


Implementation Details on CrowdDet


The CrowdDet (Chu et al. 2020) adopts a multi-instance pre-
diction (MIP) mechanism to solve the cases in which mul-
tiple objects fall into one proposal. During training, apart
from the classiﬁcation and bounding-box regression, we add
cost functions of consensus learning (Lcl) and OD predic-
tion (Lod) to the EMD loss proposed in CrowdDet:


L(bi) = min


π∈Π


K
X


k=1


[α · (Lcls(c(k)


i
, gπk) + Lreg(I(k)


i
, gπk))


+γ · Lcl(c(k)


i
, gπk) + η · Lod(od(k)


i
, gπk)],


(11)


where α, γ and η are coefﬁcients of Eq.(9) in our paper.
Please refer to Eq.(3) in (Chu et al. 2020) for other details of
the equation above. During inference, we simply append the
OD check to the original Set-NMS to decide if a box should
be suppressed when it is highly overlapped with anothor pre-
diction derived from a different proposal.


More discussions of the Consensus Learning


In the main body of our paper, we ignore a small issue about
the consensus learning (CL): does the improvement come
from additionally pasted objects in B∗


ovl ? To study this prob-
lem, we conduct ablation experiments in Table A 7. During
training, we follow the same re-pasting process in the con-
sensus learning pipeline but cancel the loss Lcl for pair-wise
score alignment. As shown by results in the third line, the ex-
tra pasting objects alone cannot improve the detector’s per-
formance, which futher veriﬁes the necessity of our design.


MR−2
AP@0.5
MR−2
AP@0.5
on Faster R-CNN
on RetinaNet
CCP
41.11
87.75
48.81
84.73
CCP+CL
40.80
88.02
47.93
84.85
CCP+CL w/o Lcl
41.15
87.78
48.88
84.71


Table A 7: Futher discussions of the CL. Experiments are
conducted on Faster R-CNN and RetinaNet respectively. Re-
sults are reported on CrowdHuman val set.


on KITTI
Easy
Moderate
Hard


Faster R-CNN
ped
97.30
89.80
79.41
car
87.85
76.31
70.23


Faster R-CNN + ours
ped
98.51
91.26
81.70
car
88.61
77.70
72.11


Table A 8: Experiments for the multi-category setting.
We use the categories of “pedestrian” and “car” in KITTI.
AP@0.7 (%) of easy, moderate and hard objects are listed
respectively.


Multi-Category Setting
Since a typical crowded object detection task (and its corre-
sponding open dataset) often includes only one category, we
make experiments on the pedestrians and cars respectively
in the paper. To further explore the effect of our method on
the more general multi-category setting, we train a Faster R-
CNN on KITTI for “pedestrian” and “car” jointly, applying
our CrowdAug. As shown in Table A 8, improvements of
detection performance are acquired on both categories.


Additional Visualizations of OD
We make more comprehensive visualizations of the overlay
depth (OD) in Fig. A8. In our method, learning of OD is in
a semi-supervised manner. During training, only the pasting
objects (synthetic data) have OD ground-truths (the ﬁrst four
lines of Fig. A8) while in inference, we expect the OD pre-
dictors perform well on natural data (the last four lines of
Fig. A8). These visualizations suggest that our method can
effectively learn the overlay depth and alleviate miss recall
during de-duplication (red dotted boxes in Fig. A8).


Visualize the Detection Results
We visually compare the detection results of the baseline de-
tector (Faster R-CNN) and our CrowdAug in Fig. A9. Qual-
itatively, we ﬁnd two kinds of typical improvements. First,
CrowdAug effectively avoids intermediate false boxes be-
tween objects (like (a), (b), (c), etc.), which we think is due
to the better correlated conﬁdence score with the IoU value.
Second, CrowdAug can reduce the miss recalls (like (d), (g),
(h), etc.), which mainly comes from the more discriminative
OD-NMS.


OD ground-truths in training set


OD predictions in validation set


Figure A 8: Additional visualizations of OD. The value of overlay depth (OD) is marked at the top left corner of each box. The
ﬁrst four lines: OD ground truths generated by copy-paste process in training data (only objects pasted have the OD ground-
truths). The last four lines: OD predictions of Faster R-CNN structure on the CrowdHuman val set. The red dotted boxes denote
the persons who are wrongly deleted by the original NMS while recalled by our OD-NMS.


（a）
（b）
（c）
（d）


（e）
（f）
（g）
（h）


（i）
（j）
（k）
（l）


（m）
（n）
（o）
（p）


Figure A 9: Visualize the detection results. We visualize the detection results of the Faster R-CNN baseline (the top image for
each pair) and those of our CrowdAug (the bottom image for each pair) on CrowdHuman val set. Conﬁdence score is marked
at the top left corner of each box.
