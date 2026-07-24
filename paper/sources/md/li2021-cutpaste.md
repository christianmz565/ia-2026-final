CutPaste: Self-Supervised Learning for Anomaly Detection and Localization


Chun-Liang Li*, Kihyuk Sohn*, Jinsung Yoon, Tomas Pﬁster


Google Cloud AI Research


{chunliang,kihyuks,jinsungyoon,tpfister}@google.com


Abstract


We aim at constructing a high performance model for de-
fect detection that detects unknown anomalous patterns of
an image without anomalous data. To this end, we propose
a two-stage framework for building anomaly detectors us-
ing normal training data only. We ﬁrst learn self-supervised
deep representations and then build a generative one-class
classiﬁer on learned representations. We learn representa-
tions by classifying normal data from the CutPaste, a sim-
ple data augmentation strategy that cuts an image patch and
pastes at a random location of a large image. Our empirical
study on MVTec anomaly detection dataset demonstrates
the proposed algorithm is general to be able to detect vari-
ous types of real-world defects. We bring the improvement
upon previous arts by 3.1 AUCs when learning representa-
tions from scratch. By transfer learning on pretrained rep-
resentations on ImageNet, we achieve a new state-of-the-
art 96.6 AUC. Lastly, we extend the framework to learn and
extract representations from patches to allow localizing de-
fective areas without annotations during training.


1. Introduction


Anomaly detection aims to detect an instance contain-
ing anomalous and defective patterns that are different from
those seen in normal instances. Many problems from dif-
ferent vision applications are anomaly detection, including
manufacturing defect detection [9, 5], medical image anal-
ysis [50, 48], and video surveillance [2, 31, 53]. Unlike
a typical supervised classiﬁcation problem, anomaly detec-
tion faces unique challenges. First, due to the nature of the
problem, it is difﬁcult to obtain a large amount of anoma-
lous data, either labeled or unlabeled. Second, the differ-
ence between normal and anomalous patterns are often ﬁne-
grained as defective areas might be small and subtle in high-
resolution images.


Due to limited access to anomalous data, constructing an
anomaly detector is often conducted under semi-supervised
or one-class classiﬁcation settings using normal data only.


*Equal contributions.


Since the distribution of anomaly patterns is unknown in
advance, we train models to learn patterns of normal in-
stances and determine anomaly if the test example is not
represented well by these models. For example, an autoen-
coder that is trained to reconstruct normal data is used to de-
clare anomalies when the data reconstruction error is high.
Generative models declare anomalies when the probability
density is below a certain threshold. However, the anomaly
score deﬁned as an aggregation of pixel-wise reconstruction
error or probability densities lacks to capture a high-level
semantic information [42, 37].


Alternative methods using high-level learned represen-
tations have shown more effective for anomaly detection.
For example, deep one-class classiﬁer [46] demonstrates
an effective end-to-end trained one-class classiﬁers pa-
rameterized by deep neural networks. It outperforms its
shallow counterparts, such as one-class SVMs [49] and
reconstruction-based approaches such as autoencoders [34].
In self-supervised representation learning, predicting geo-
metric transformations of an image [20, 24, 4], such as ro-
tation or translation, and contrastive learning [54, 52] have
shown to be successful in distinguishing normal data from
outliers. However, most existing works focus on detect-
ing semantic outliers (e.g., visual objects from different
classes) from object-centric natural images. In Section 4.1,
we show these methods do not generalize well in detecting
ﬁne-grained anomalous patterns as in defect detection.


In this work, we tackle a one-class defect detection prob-
lem, a special case of image anomaly detection, where vari-
ous forms of unknown anomalous patterns present locally in
the high-resolution images. We follow the two-stage frame-
work [52], where we ﬁrst learn self-supervised representa-
tions by solving a proxy task, then build a generative one-
class classiﬁer on learned representations to distinguish data
with anomalous patterns from normal ones. Our innova-
tion is at designing a novel proxy task for self-supervised
learning of representations. Speciﬁcally, we formulate a
proxy classiﬁcation task between normal training data and
the ones augmented by the CutPaste, the proposed data aug-
mentation strategy that cuts an image patch and pastes at a
random location of an image. CutPaste augmentation is mo-


1


arXiv:2104.04015v1  [cs.CV]  8 Apr 2021


CNN
GDE


Anomaly score


GradCAM


CNN
GDE


Heatmap
(Upsampled)
Anomaly score
(spatial max-pooling)


Image-level / Patch-level


CutPaste


CNN


CNN


0


1


Shared


(a) Learning Self-Supervised Representation
(b) Anomaly Detection and Localization


Figure 1: An overview of our method for anomaly detection and localization. (a) A deep network (CNN) is trained to
distinguish images from normal (blue) and augmented (green) data distributions by CutPaste (orange dotted box), which cuts
a small rectangular region (yellow dotted box) from normal data and pastes it at random location. Representations are trained
either from the whole image or local patches. (b, top) An image-level representation makes a holistic decision for anomaly
detection and is used to localize defect via GradCAM [51]. (b, bottom) A patch-level representation extracts dense features
from local patches to produce anomaly score map, which is then max-pooled for detection or upsampled for localization [32].


tivated to produce a spatial irregularity to serve as a coarse
approximation of real defects, which we have no access at
training. Rectangular patches of different sizes, aspect ra-
tios, and rotation angles are pasted to generate diverse aug-
mentations. Although CutPaste augmented samples (Fig-
ure 2(e)) are easily distinguishable from real defects and
thus might be a crude approximation of a real anomaly dis-
tribution, we show that representations learned by detecting
irregularity introduced by CutPaste augmentations general-
ize well on detecting real defects.


We evaluate our methods on MVTec anomaly detection
dataset [5], a real-world industrial visual inspection bench-
mark. By learning deep representations from scratch, we
achieve 95.2 AUC on image-level anomaly detection, which
outperforms existing works [25, 61] by at least 3.1 AUC.
Moreover, we report state-of-the-art 96.6 image-level AUC
by transfer learning from an ImageNet pretrained model.
Moreover, we explain how learned representations could
be used to localize the defective areas in high-resolution
images. Without using any anomaly data, a simple patch
model extension can achieve 96.0 pixel-level localization
AUC, which improves upon previous state-of-the-art [61]
(95.7 AUC). We conduct an extensive study using different
types of augmentation and proxy tasks to show the effec-
tiveness of CutPaste augmentations for self-supervised rep-
resentation learning on unknown defect detection.


2. A Framework for Anomaly Detection


In this section, we present our anomaly detection frame-
work for high-resolution image with defects in local re-
gions. Following [54], we adopt a two-stage framework for


building an anomaly detector, where in the ﬁrst stage we
learn deep representations from normal data and then con-
struct an one-class classiﬁer using learned representations.
Subsequently, in Section 2.1, we present a novel method for
learning self-supervised representations by predicting Cut-
Paste augmentation, and extend to learning and extracting
representations from local patches in Section 2.4.


2.1. Self-Supervised Learning with CutPaste


Deﬁning good pretext tasks is essential for self-
supervised representation learning. While popular meth-
ods including rotation prediction [19] and contrastive learn-
ing [60, 12] have been studied in the context of semantic
one-class classiﬁcation [20, 24, 4, 54, 52], our study in Sec-
tion 4.1 shows that naively applying existing methods, such
as rotation prediction or contrastive learning, is sub-optimal
for detecting local defects as we will show in Section 4.1.


We conjecture that geometric transformations [20, 24, 4],
such as rotations and translations, are effective in learning
representation of semantic concepts (e.g., objectness), but
less of regularity (e.g., continuity, repetition). As shown
in Figure 2(b), anomalous patterns of defect detection typi-
cally include irregularities such as cracks (bottle, wood) or
twists (toothbrush, grid). Our aim is to design an augmenta-
tion strategy creating local irregular patterns. Then we train
the model to identify these local irregularity with the hope
that it can generalize to unseen real defects at test time.


A popular augmentation method that could create a lo-
cal irregularity in image is Cutout [18] (Figure 2(c)), which
wipes out a randomly selected small rectangular area of
an image. Cutout is found to be a useful data augmenta-


2


(a) Normal
(b) Anomaly
(c) Cutout
(d) Scar
(e) CutPaste
(f) CutPaste (Scar)


Figure 2: Visualization of (a, green) normal, (b, red) anomaly, and (c–h, blue) augmented normal samples from bottle,
toothbrush, screw, grid, and wood classes of MVTec anomaly detection dataset [5]. Augmented normal samples are generated
by baseline augmentations including (c) Cutout and (d) Scar, and our proposed (e) CutPaste and (f) CutPaste (Scar). We use
red arrows in (f) to highlight the pasted patch of scar shape, a thin rectangle with rotation.


tion that enforces invariance, leading to improved accuracy
on multi-class classiﬁcation tasks. In contrast, we start by
discriminating Cutout images from the normal ones. At
ﬁrst glance, the task seems easy to solve by well-crafted
low level image ﬁlters. Surprisingly, as we will show in
Section 4, without the hindsight of knowing this, a deep
convolution network does not learn these shortcuts. Using
Cutout in the algorithm design for defect detection can also
be found in [32, 57]. We can make the task harder by ran-
domly choosing colors and the scale as shown in Figure 2(d)
to avoid naive shortcut solutions.


To further prevent learning naive decision rules for dis-
criminating augmented images and encouraging the model
to learn to detect irregularity, we propose the CutPaste aug-
mentation as follows:


1. Cut a small rectangular area of variable sizes and as-
pect ratios from a normal training image.


2. Optionally, we rotate or jitter pixel values in the patch.


3. Paste a patch back to an image at a random location.


We show the CutPaste augmentation process in the orange
dotted box of Figure 1 and more examples in Figure 2(e).
Following the idea of rotation prediction [19], we deﬁne the
training objective of the proposed self-supervised represen-
tation learning as follows:


LCP = Ex∈X





CE(g(x), 0) + CE(g(CP(x)), 1)


	


(1)


where X is the set of normal data, CP(·) is a CutPaste aug-
mentation and g is a binary classiﬁer parameterized by deep


networks. CE(·, ·) refers to a cross-entropy loss. In prac-
tice, data augmentations, such as translation or color jitter,
are applied before feeding x into g or CP.


2.2. CutPaste Variants


CutPaste-Scar.
A special case of Cutout called “scar” us-
ing a long-thin rectangular box of random color, as in Fig-
ure 2(d), is proposed in [16] for defect detection. Simi-
larly, in addition to original CutPaste using a large rectan-
gular patch, we propose a CutPaste-Scar using a scar-like
(long-thin) rectangular box ﬁlled with an image patch (Fig-
ure 2(f)).


Multi-Class Classiﬁcation.
While CutPaste (large patch)
and CutPaste-Scar share a similarity, the shapes of an im-
age patch of two augmentations are very different. Empir-
ically, they have their own advantages on different types of
defects. To leverage the strength of both scales in the train-
ing, we formulate a ﬁner-grained 3-way classiﬁcation task
among normal, CutPaste and CutPaste-Scar by treating Cut-
Paste variants as two separate classes. Detailed study will
be presented in Section 5.2.


Similarity between CutPaste and real defects.
The suc-
cess of CutPaste may be understood from outlier expo-
sure [23], where we generate the pseudo anomalies (Cut-
Paste) during the training. Apart from using natural images
as in [23], CutPaste creates examples preserving more local
structures of the normal examples (i.e., the pasted patch is


3


Normal
Anomaly
Patch
Scar


(a) bottle


Normal
Anomaly
Patch
Scar


(b) toothbrush


Normal
Anomaly
Patch
Scar


(c) screw


Normal
Anomaly
Patch
Scar


(d) grid


Normal
Anomaly
Patch
Scar


(e) wood
Figure 3: t-SNE visualization of representations of models trained with 3-way CutPaste prediction task. We plot embeddings
of normal (blue), anomaly (red), and augmented normal by CutPaste (“Patch”, green) and CutPaste-scar (“Scar”, yellow).


from the same domain), which is more challenging for the
model to learn to ﬁnd this irregularity.


On the other hand, CutPaste does look similar to some
real defects. A natural question is if the success of Cut-
Paste is from a good mimic of real defects. In Figure 3, we
show the t-SNE plots of the representations from the trained
model. Clearly, the CutPaste examples are almost not over-
lapped with real defect examples (anomaly), but the learned
representation is able to distinguish between normal exam-
ple, different CutPaste augmented samples and real defects.
It suggests (1) CutPaste is still not a perfect simulation of
real defects and (2) learning on it to ﬁnd irregularity gener-
alizes well on unseen anomalies.


2.3. Computing Anomaly Score


There exist various ways to compute anomaly scores via
one-class classiﬁers. In this work, we build generative clas-
siﬁers like kernel density estimator [52] or Gaussian den-
sity estimator [43], on representations f. Below, we explain
how to compute anomaly scores and the trade-offs.


Although nonparametric KDE is free from distribution
assumptions, it requires many examples for accurate esti-
mation [58] and could be computationally expensive. With
limited normal training examples for defect detection, we
consider a simple parametric Gaussian density estimator
(GDE) whose log-density is computed as follows:


log pgde(x) ∝





−1


2(f(x) −µ)⊤Σ−1(f(x) −µ)
	


(2)


where µ and Σ are learned from normal training data.1


2.4. Localization with Patch Representation


While we present a method for learning a holistic repre-
sentation of an image, learning a representation of an im-
age patch would be preferred if we want to localize defec-
tive regions [38, 6, 61] in addition to image-level detection.
By learning and extracting representations from an image


1We note that a mixture of Gaussian, which is a middle ground between
KDE and GDE, can also be used for more expressive density modeling. We
do not observe signiﬁcant performance gain empirically.


patch, we can build an anomaly detector that is able to com-
pute the score of an image patch, which then can be used to
localize the defective area.


CutPaste prediction is readily applicable to learn a patch
representation – all we need to do at training is to crop a
patch before applying CutPaste augmentation. Similar to
Equation (1), the training objective can be written as:


Ex∈X





CE(g(c(x)), 0) + CE(g(CP(c(x))), 1)


	


(3)


where c(x) crops a patch at random location of x. At test
time, we extract embeddings from all patches with a given
stride. For each patch, we evaluate its anomaly score and
use a Gaussian smoothing to propagate the score to every
pixel [32]. In Section 4.2, we visualize a heatmap using
patch-level detector for defect localization, along with that
of an image-level detector using visual explanation tech-
niques such as GradCAM [51].


3. Related Work


Anomaly detection under one-class classiﬁcation setting,
where we assume only the normal data is given during the
training, has been widely studied [49, 56, 46, 63, 66, 13, 42,
36, 27]. Recent success of self-supervised learning in com-
puter vision [39, 19, 8, 60, 40, 12, 21] has also been demon-
strated effective for one-class classiﬁcation and anomaly de-
tection. One major family is by predicting geometric trans-
formations [20, 24, 4], such as rotation, translation or ﬂips.
The other family includes variants of contrastive learning
with geometric augmentations [54, 52]. However, the suc-
cess has been limited to semantic anomaly detection bench-
marks, such as CIFAR-10 [28] or ImageNet [17], and as we
show in Section 4.1, methods relying on geometric transfor-
mations perform poorly on defect detection benchmarks.


Because of practical applications, such as industrial in-
spection or medical diagnosis, defect detection [9, 5] has
received lots of attention. The initial steps have been taken
with methods including autoencoding [9, 7, 25, 59], gener-
ative adversarial networks [48, 3], using pretrained models
on ImageNet [38, 45, 6, 14, 43, 44], and self-supervised
learning by solving different proxy tasks with augmenta-
tions [61, 47, 57, 15]. The proposed CutPaste prediction


4


task is not only shown to have strong performance on de-
fect detection, but also amenable to combine with existing
methods, such as transfer learning from pretrained models
for better performance or patch-based models for more ac-
curate localization, which we demonstrate in Section 4.


3.1. Relation to Other Augmentations


Although Cutout [18] and RandomErasing [65] are sim-
ilar to CutPaste, they create irregularities by a small rect-
angular region ﬁlled with either zero or uniformly sampled
pixel values instead of a structural image patch as CutPaste.
Moreover, unlike typical use of augmentations for learning
invariant representations, we learn a representation that is
discriminative to these augmentations.


Scar augmentation [16] (Figure 2(d)) is a special case of
Cutout, which uses a long-thin rectangle with random col-
ors. While it demonstrates strong performance, we show
that CutPaste with the same scale (Figure 2(f)), which ﬁlls
a long-thin rectangle by a patch from the same image, im-
proves upon representations trained by predicting Cutout.


CutMix [62], which extracts a rectangular image patch
from an image and pastes at random location of another im-
age, is related to CutPaste in terms of pasting operations.
One main difference is CutMix leverages existing image la-
bels with MixUp [64] in the objective while CutPaste pre-
diction is a self-supervised learning without the need of im-
age labels. The other difference is CutMix studies standard
supervised tasks, while we aim for one-class classiﬁcation.


[11] presents a denoising autoencoder with patch-swap
augmentation as noise process. [26] proposes to learn rep-
resentations by predicting local augmentations using GAN.
Our method is simpler (e.g., no need to train decoder or
GAN) while highly performant, thus more practical.


4. Experiments


We conduct most experiments on MVTec Anomaly De-
tection dataset [5] that contains 10 object and 5 texture cat-
egories for anomaly detection. The dataset is composed of
normal images for training and both normal and anomaly
images with various types of defect for testing. It also pro-
vides pixel-level annotations for defective test images. The
dataset is relatively small scale in number of images, where
the number of training images varies from 60 to 391, posing
a unique challenge for learning deep representations.


We follow one-class classiﬁcation protocol, also known
as semi-supervised anomaly detection [10],2 where we train
a one-class classiﬁer for each category on its respective nor-
mal training examples. Following [52], we learn the rep-
resentations by augmentation prediction from scratch with


2While previous works [5, 6] have used unsupervised to describe their
settings, it could be misleading as training data is curated to include normal
data only.


ResNet-18 [22] plus an MLP projection head on top of aver-
age pooling layer followed by the last linear layer. We con-
struct a Gaussian density estimation (GDE) as Equation (2)
for anomaly detector based on the top pooled features.


We train a model on 256×256 image. We note that the
same training strategy, such as the selection of hyperparam-
eters or data augmentations, is applied to all categories. De-
tailed settings of training can be found in Appendix A.


4.1. Main Results


We report the anomaly detection performance in Table 1.
We run experiments 5 times with different random seeds
and report the mean AUC and standard error for each cat-
egory. We also report the average of mean and standard
errors for texture, object, and all categories.


We test representations trained with different proxy tasks
of self-supervised learning, including baselines such as ro-
tation [20], Cutout or scar predictions, the proposed Cut-
Paste, CutPaste-Scar predictions, and using both with 3-way
classiﬁcation. We also compare with previous works, in-
cluding deep one-class classiﬁer (DOCC) [45], uninformed
student [5], and patch SVDD [61]. We note that some of
these methods use ImageNet pretrained model for transfer
learning, either by ﬁne-tuning (DOCC) or distillation (un-
informed student). The results are in Table 1.


Rotation prediction is demonstrated to be powerful in se-
mantic anomaly detection [52]. However, it results in un-
satisfactory 73.1 AUC in defect detection compared with
the Scar prediction (85.0), a Cutout variant.
Some fail-
ure of rotation prediction is due to the unaligned objects,
such as screw shown in Figure 2. For aligned objects, al-
though it performs well on toothbrush, it is sub-optimal
on capsule. Detailed ablation study of Cutout variants
can be found in Section 5.


CutPaste and CutPaste-Scar, which improve Cutout and
Scar prediction by avoiding potential naive solutions, out-
perform other augmentation predictions with 90.9 and 93.5
AUCs, respectively. With a ﬁner-grained 3-way classiﬁca-
tion to leverage different scale of CutPaste, we achieve the
best 95.2 AUC, which surpasses existing works on learning
from scratch, such as P-SVDD [61] (92.1 AUC). The pro-
posed data-driven approach via CutPaste is also better than
existing works leveraging pretrained networks, including
DOCC [45] (87.9 AUC) with pretrained VGG16 and Unin-
formed Student [6] (92.5 AUC) with pretrained ResNet18.
Last, we further improve the AUC to 96.1 by ensembling
anomaly scores from 5 CutPaste (3-way) models.


4.2. Defect Localization


We conduct anomaly localization experiments using our
representations trained with 3-way classiﬁcation task. One
challenge to accurate localization of defect is that it is difﬁ-
cult to use a heatmap-style approach for localization as our


5


Table 1: Anomaly detection performance on MVTec AD dataset [5]. We report AUCs of representations trained to classify
CutPaste, CutPaste (scar), both (3-way), and baseline augmentations such as rotation, Cutout, or scar. For comparison, we
report those of deep one-class classiﬁer [45], uninformed student [6] and patch-SVDD [61]. We report mean and standard
error tested with 5 random seeds. Lastly, we report the AUC using ensemble of 5 CutPaste (3-way) models. The best
performing model and those within standard error are bold-faced.


Category
DOCC
U-Student
P-SVDD
Rotation
Cutout
Scar
CutPaste
CutPaste
CutPaste
Ensemble
[45]
[6]
[61]
(scar)
(3-way)


texture


carpet
90.6
95.3
92.9
29.7±1.4
35.3±2.3
92.7±0.4
67.9±1.8
94.6±0.6
93.1±1.1
93.9
grid
52.4
98.7
94.6
60.5±7.0
57.5±3.0
74.4±2.5
99.9±0.1
95.5±0.3
99.9±0.1
100.0
leather
78.3
93.4
90.9
55.2±1.4
67.7±1.5
99.9±0.1
99.7±0.1
100.0 ±0.0
100.0 ±0.0
100.0
tile
96.5
95.8
97.8
70.1±1.9
71.8±4.0
96.7±0.9
95.9±1.0
89.4±2.8
93.4±1.0
94.6
wood
91.6
95.5
96.5
95.8±1.1
92.0±0.8
98.9±0.2
94.9±0.5
98.7±0.3
98.6±0.5
99.1


average
81.9
95.7
94.5
62.3±2.6
64.9±2.3
92.5±0.8
91.7±0.7
95.7±0.8
97.0±0.5
97.5


object


bottle
99.6
96.7
98.6
95.0±0.7
88.7±0.8
98.5±0.2
99.2±0.2
98.0±0.5
98.3±0.5
98.2
cable
90.9
82.3
90.3
85.3±0.8
80.2±1.4
78.3±1.7
87.1±0.8
78.8±2.9
80.6±0.5
81.2
capsule
91.0
92.8
76.7
71.8±1.4
69.5±1.1
82.9±0.7
87.9±0.7
95.3±0.8
96.2±0.5
98.2
hazelnut
95.0
91.4
92.0
83.6±0.8
69.7±1.3
98.9±0.2
91.3±0.6
96.7±0.4
97.3±0.3
98.3
metal nut
85.2
94.0
94.0
72.7±0.5
84.6±0.7
86.9±1.5
96.8±0.5
97.9±0.2
99.3±0.2
99.9
pill
80.4
86.7
86.1
79.2±1.4
78.7±0.7
82.2±1.4
93.4±0.9
85.8±1.3
92.4±1.3
94.9
screw
86.9
87.4
81.3
35.8±2.9
17.6±4.4
11.3±2.2
54.4±1.7
83.7±0.7
86.3±1.0
88.7
toothbrush
96.4
98.6
100.0
99.1±0.2
98.1±0.6
94.8±1.0
99.2±0.2
96.7±0.4
98.3±0.9
99.4
transistor
90.8
83.6
91.5
88.9±0.4
82.5±1.2
92.0±0.7
96.4±0.7
91.1±0.6
95.5±0.5
96.1
zipper
92.4
95.8
97.9
74.3±1.6
75.7±1.0
86.8±0.9
99.4±0.1
99.5±0.1
99.4±0.2
99.9


average
90.9
90.9
90.8
78.6±1.1
74.5±1.3
81.3±1.1
90.5±0.6
92.4±0.8
94.3±0.6
95.5


average
87.9
92.5
92.1
73.1±1.6
71.3±1.6
85.0±1.0
90.9±0.7
93.5±0.8
95.2±0.6
96.1


Input


GT 
Mask


Grad
CAM


Patch 
Heatmap


Figure 4: Defect localization on bottle, hazelnut, metal nut, screw, wood and grid classes of MVTec datasets. From top to
bottom, input images, those with ground-truth localization mask in red, GradCAM results using image-level detector, and
heatmaps using patch-level detector. We provide more examples in Appendix B.


model learns a holistic representation of an image. Instead,
we use visual explanation techniques, GradCAM [51], to
highlight the area affecting the decision of anomaly detec-
tor. We show qualitative results in the second row of Fig-
ure 4, which are visually pleasing. We further evaluate the
pixel-wise localization AUC, achieving 88.3.


Instead, we learn a representation of an image patch us-
ing CutPaste prediction, as in Section 2.4. We train mod-
els of 64×64 patches from 256×256 image. At test time,
we densely extract anomaly scores with a stride of 4 and
propagate the anomaly scores via receptive ﬁeld upsam-
pling with Gaussian smoothing [32]. We report a localiza-
tion AUC in Table 2. Our patch-based model achieves 96.0


AUC. Speciﬁcally, our model shows strong performance on
texture categories over previous state-of-the-art (96.3 AUC
compared to 93.7). We also outperforms the DistAug con-
trastive learning [52], which only results in 90.4 localiza-
tion AUC. Finally, we visualize representative samples for
localization in Figure 4, showing accurate localization even
when defects are tiny. More comprehensive results on de-
fect localization are given in Appendix B.


4.3. Transfer Learning with Pretrained Models


In Section 4.1, we have shown the proposed data-driven
approach is better than leveraging pretrained networks, such
as DOCC [45] and Uninformed Student [6]. It is consistent


6


Table 2: Pixel-wise localization AUC on MVTec dataset.
The best and models within standard error are bold-faced.


Category
FCDD [32]
P-SVDD [61]
CutPaste (3-way)


texture


carpet
96
92.6
98.3±0.0
grid
91
96.2
97.5±0.1
leather
98
97.4
99.5±0.0
tile
91
91.4
90.5±0.2
wood
88
90.8
95.5±0.1


average
93
93.7
96.3±0.1


object


bottle
97
98.1
97.6±0.1
cable
90
96.8
90.0±0.2
capsule
93
95.8
97.4±0.1
hazelnut
95
97.5
97.3±0.1
metal nut
94
98.0
93.1±0.4
pill
81
95.1
95.7±0.1
screw
86
95.7
96.7±0.1
toothbrush
94
98.1
98.1±0.0
transistor
88
97.0
93.0±0.2
zipper
92
95.1
99.3±0.0


average
91
96.7
95.8±0.1


average
92
95.7
96.0±0.1


Table 3: Detection performance on MVTec dataset using
representations of EfﬁcientNet (B4) [55] pretrained on Im-
ageNet [17] and ﬁne-tuned by the CutPaste (3-way). The
number is bold when it is better than its pretrained or ﬁne-
tuned counterpart under the same feature (pool v.s. level-7).


Category
Pool
Level-7


Pretrain
Finetune
Pretrain
Finetune


texture


carpet
98.3
100.0±0.0
97.6
100.0±0.0
grid
96.4
98.8±0.1
98.2
99.1±0.0
leather
100.0
100.0±0.0
100.0
100.0±0.0
tile
99.9
98.9±0.2
99.9
99.8±0.2
wood
99.7
99.8±0.0
99.6
99.8±0.0


average
98.9
99.5±0.0
99
99.7±0.0


object


bottle
99.8
100.0±0.0
100.0
100.0±0.0
cable
91.2
93.9±0.1
96.5
96.2±0.3
capsule
93
94.3±0.3
94.7
95.4±0.1
hazelnut
96.6
99.7±0.0
100.0
99.9±0.0
metalnut
94.3
98.7±0.1
97.7
98.6±0.0
pill
81.9
91.3±0.2
91
93.3±0.2
screw
86.3
86±0.1
92.0
86.6±0.2
toothbrush
89.3
92.8±0.2
90.3
90.7±0.1
transistor
94.6
95.6±0.2
97.5
97.5±0.2
zipper
95.6
99.9±0.0
97
99.9±0.1


average
92.3
95.2±0.1
95.7
95.8±0.1


average
94.5
96.6±0.1
96.8
97.1±0.0


with the prior study on semantic anomaly detection [52].
On the other hand, pretrained EfﬁcientNet [55] is found use-
ful for defect detection [43]. As shown in Table 3, without
ﬁne-tuning, the representation from the pretrained Efﬁcient-
Net (B4) results in 94.5 AUC, which is competitive with the
proposed CutPaste prediction (95.2 from Table 1).


Here we demonstrate that the proposed self-supervised
learning via CutPaste is versatile, which can also be used to
improve the pretrained networks to better adapt to the data.
We use pretrained EfﬁcientNet (B4) as a backbone, and fol-
low the standard ﬁne-tuning steps to train with the same


Table 4: Detection AUCs of representations trained to pre-
dict Cutout, with mean pixel value, with random color, Con-
fetti noise [32], or the proposed CutPaste.


Category
Cutout
Cutout
Cutout
Confetti
CutPaste
(Mean)
(Color)


texture
64.9±2.3
65.5±1.8
70.5±2.2
80.1±2.3
91.7±0.7
object
74.5±1.3
78.1±1.1
78.9±1.0
76.7±0.3
90.5±0.6


all
71.3±1.7
73.9±1.3
76.1±1.4
77.8±1.5
90.9±0.7


(a) Cutout
(Standard)


(b) Cutout


(Mean)


(c) Cutout
(Random Color)
(d) Confetti
(e) CutPaste


Figure 5: Visual comparison between the proposed Cut-
Paste and Cutout variants, including ﬁlling with grey color,
mean pixel values, random colors and Confetti noise [32].


CutPaste prediction (3-way) task. Detailed settings can be
found in Appendix A. We show the results in Table 3. After
ﬁne-tuning via CutPaste, we achieve the new state-of-the-
art 96.6 AUC. Furthermore, CutPaste prediction is a gen-
eral and useful strategy to adapt to the data for most of the
situations. For example, CutPaste improves by a large mar-
gin on class pill (81.9 →91.3). For many nearly perfect
situations, such as bottle, CutPaste is still able to im-
prove by a small margin. Last, as suggested by [30, 43], we
investigate the performance of various deep features. We
ﬁnd that level-7 feature shows the best performance, and
we further improve the level-7 feature of EfﬁcientNet from
96.8 (pretrained) to 97.1±0.0 with CutPaste.


5. Ablation Study


We conduct various additional studies to provide deeper
insights of the proposed CutPaste. We ﬁrst compare Cut-
Paste with different Cutout variants in addition to the stan-
dard ones reported in Section 4.1. Second, we showcase the
representation learned via predicting CutPaste generalizes
well to more crafted unseen defects. Last, we compare with
the semantic anomaly detection.


5.1. From Cutout to CutPaste


We evaluate the performance of representations trained
to predict variants of Cutout augmentations whose areas are
ﬁlled by grey color (standard), mean pixel values, random
color, or image patch from different location, i.e., CutPaste.
We also test Confetti noise [32] that jitters a color of a local
patch. We show samples from considered augmentations in
Figure 5 and report the detection AUCs in Table 4. While


7


Table 5: Detection AUCs of representations trained with
binary classiﬁcation between normal and the union of Cut-
Paste and CutPaste-Scar examples and 3-way classiﬁcation
among normal, CutPaste and CutPaste-scar examples.


Category
CutPaste
CutPaste (scar)
Binary (Union)
3-Way


texture
91.7±0.7
95.7±0.8
97.3±0.3
97.0±0.5
object
90.5±0.6
92.4±0.8
92.8±0.5
94.3±0.6


all
90.9±0.7
93.5±0.8
94.3±0.5
95.2±0.6


achieving 71.3 AUC that already is signiﬁcantly better than
random guessing, predicting a standard Cutout augmenta-
tion is still a simple task and the network may have learned
a naive solution from easy proxy task, as discussed in Sec-
tion 2. By gradually increasing the difﬁculty of proxy task
to avoid known trivial solutions with random color to the
patch, or with structures similar to local patterns of the nor-
mal data (Confetti noise, CutPaste), the network learns to
ﬁnd irregularity and generalizes better to detect real defects.


5.2. Binary v.s. Finer-Grained Classiﬁcation


In Table 1, although CutPaste-scar shows better perfor-
mance on average than CutPaste, there is no clear winner
that works the best for all. As there are diverse types of
defect in practice, we leverage the strength of both augmen-
tations for representation learning. In Section 2.2, we train
a model by solving a 3-way classiﬁcation task between nor-
mal, CutPaste and CutPaste-scar. Alternatively, we train to
solve a binary classiﬁcation task by discriminating normal
examples and the union of two augmentations.


The results, along with those of representations trained
with CutPaste and CutPaste-scar, are in Table 5. It is clear
that using both augmentations improve the performance.
Between binary with union of augmentations and 3-way,
we observe better detection performance with representa-
tions trained by 3-way classiﬁcation task. A plausible hy-
pothesis on the superiority of 3-way formulation in our case
is that it is more natural to model CutPaste and CutPaste-
scar augmentations separately than together as there exists
a systematic difference between them in the size, shape, and
rotation angle of patches.


5.3. CutPaste on Synthetic Anomaly Detection


We further study the generalization of our models to un-
seen anomalies. Speciﬁcally, we test on synthetic anomaly
datasets created by patching diverse shape masks to normal
data, such as digits [29], square, ellipse, or heart [35], ﬁlled
with random color or natural images. Samples of synthetic
anomalies are shown in Figure 6 and detection results are in
Table 6. We ﬁrst note that these datasets are not trivial – a
model trained by predicting Cutout augmentations achieves
only 81.5. Our proposed CutPaste (3-way) model performs
well on synthetic dataset, achieving 98.3 AUC on average.
We highlight that some shapes (e.g., ellipse, heart) or color


Figure 6: Synthetic defects on pill class. From left to right,
we use MNIST [29], square, ellipse, heart [35] with random
color, and those ﬁlled with natural image patches.


Table 6: Detection AUCs on synthetic data. Various shapes,
such as digit, square, ellipse, or heart, are patched to normal
images with random color or natural images (†).


Dataset
MNIST
Square
Ellipse
Heart
Square†
Ellipse†
Heart†
Avg


Cutout
52.3
90.6
89.3
87.5
86.4
84.0
80.7
81.5
CutPaste
96.1
98.4
98.2
97.9
99.3
99.2
99.0
98.3


statistics inside the patch (e.g., constant color, natural im-
ages) are not seen at training, but we can still generalize to
these unseen cases.


5.4. Application to Semantic Outlier Detection


We also conduct the semantic anomaly detection experi-
ment on CIFAR-10 [28] following the protocol in [20, 52],
where a single class is treated as normal and remaining 9
classes are anomalies. We make a comparison of Cutout,
CutPaste and rotation prediction [52]. Cutout results in 60.2
AUC, and CutPaste achieves 69.4 AUC, which signiﬁcantly
improves upon Cutout (60.2). However, these are still far
behind that of rotation prediction (91.3 AUC) on CIFAR-10
semantic anomaly detection. On the other hand, in Sec-
tion 4.1, we have discussed the reversed situation that rota-
tion prediction is much worse than 3-way CutPaste predic-
tion. The results suggest the difference between semantic
anomaly detection and defect detection, which needs differ-
ent algorithm and augmentation designs.


6. Conclusion


We propose a data-driven approach for defect detection
and localization. The key to our success is self-supervised
learning of representations with CutPaste, a simple yet ef-
fective augmentation that encourages the model to ﬁnd local
irregularities. We show superior image-level anomaly de-
tection performance on the real-world dataset. Furthermore,
by learning and extracting patch-level representations, we
demonstrate state-of-the-art pixel-wise anomaly localiza-
tion performance. We envision the CutPaste augmentation
could be a cornerstone for building a powerful model for
semi-supervised and unsupervised defect detection.


Acknowledgment.
We thank Yang Feng for sharing the
implementation of uninformed student and Sercan Arik for
the proofread of our manuscript.


8


References


[1] Mart´ın Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen,


Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghe-
mawat, Geoffrey Irving, Michael Isard, et al. Tensorﬂow:
A system for large-scale machine learning. In {USENIX},
2016. 12
[2] Amit Adam, Ehud Rivlin, Ilan Shimshoni, and Daviv


Reinitz. Robust real-time unusual event detection using mul-
tiple ﬁxed-location monitors. IEEE transactions on pattern
analysis and machine intelligence, 2008. 1
[3] Samet Akcay, Amir Atapour-Abarghouei, and Toby P


Breckon.
Ganomaly: Semi-supervised anomaly detection
via adversarial training. In ACCV, 2018. 4
[4] Liron Bergman and Yedid Hoshen.
Classiﬁcation-based
anomaly detection for general data. In ICLR, 2020. 1, 2,
4
[5] Paul Bergmann, Michael Fauser, David Sattlegger, and


Carsten Steger.
Mvtec ad–a comprehensive real-world
dataset for unsupervised anomaly detection. In CVPR, 2019.
1, 2, 3, 4, 5, 6
[6] Paul Bergmann, Michael Fauser, David Sattlegger, and


Carsten Steger.
Uninformed students:
Student-teacher
anomaly detection with discriminative latent embeddings. In
CVPR, 2020. 4, 5, 6
[7] Paul Bergmann, Sindy L¨owe, Michael Fauser, David Sattleg-


ger, and Carsten Steger. Improving unsupervised defect seg-
mentation by applying structural similarity to autoencoders.
arXiv preprint arXiv:1807.02011, 2018. 4
[8] Mathilde Caron, Piotr Bojanowski, Armand Joulin, and


Matthijs Douze. Deep clustering for unsupervised learning
of visual features. In ECCV, 2018. 4
[9] Diego Carrera, Giacomo Boracchi, Alessandro Foi, and


Brendt Wohlberg. Detecting anomalous structures by con-
volutional sparse models. In IJCNN, 2015. 1, 4
[10] Varun Chandola, Arindam Banerjee, and Vipin Kumar.


Anomaly detection: A survey.
ACM computing surveys
(CSUR), 2009. 5
[11] Liang Chen, Paul Bentley, Kensaku Mori, Kazunari Misawa,


Michitaka Fujiwara, and Daniel Rueckert. Self-supervised
learning for medical image analysis using image context
restoration. Medical image analysis, 2019. 5
[12] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Ge-


offrey Hinton. A simple framework for contrastive learning
of visual representations. arXiv preprint arXiv:2002.05709,
2020. 2, 4
[13] Hyunsun Choi, Eric Jang, and Alexander A Alemi. Waic, but


why? generative ensembles for robust anomaly detection.
arXiv preprint arXiv:1810.01392, 2018. 4
[14] Niv Cohen and Yedid Hoshen. Sub-image anomaly detec-


tion with deep pyramid correspondences.
arXiv preprint
arXiv:2005.02357, 2020. 4
[15] Anne-Sophie Collin and Christophe De Vleeschouwer. Im-


proved anomaly detection by training an autoencoder with
skip connections on images corrupted with stain-shaped
noise. arXiv preprint arXiv:2008.12977, 2020. 4
[16] daisukelab.
Spotting
defects!
—
deep
met-
ric
learning
solution
for
mvtec
anomaly
detection


dataset.
https : / / medium . com / analytics -
vidhya / spotting - defects - deep - metric -
learning - solution - for - mvtec - anomaly -
detection- dataset- c77691beb1eb.
Accessed:
2020-11-12. 3, 5
[17] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,


and Li Fei-Fei. ImageNet: A large-scale hierarchical image
database. In CVPR, 2009. 4, 7
[18] Terrance DeVries and Graham W Taylor. Improved regular-


ization of convolutional neural networks with cutout. arXiv
preprint arXiv:1708.04552, 2017. 2, 5
[19] Spyros Gidaris, Praveer Singh, and Nikos Komodakis. Un-


supervised representation learning by predicting image rota-
tions. In ICLR, 2018. 2, 3, 4
[20] Izhak Golan and Ran El-Yaniv. Deep anomaly detection us-


ing geometric transformations. In NIPS, 2018. 1, 2, 4, 5,
8
[21] Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, and Ross


Girshick. Momentum contrast for unsupervised visual rep-
resentation learning. In CVPR, 2020. 4
[22] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.


Deep residual learning for image recognition.
In CVPR,
pages 770–778, 2016. 5
[23] Dan Hendrycks, Mantas Mazeika, and Thomas Dietterich.


Deep anomaly detection with outlier exposure.
arXiv
preprint arXiv:1812.04606, 2018. 3
[24] Dan Hendrycks, Mantas Mazeika, Saurav Kadavath, and


Dawn Song.
Using self-supervised learning can improve
model robustness and uncertainty. In NIPS, 2019. 1, 2, 4
[25] Chaoqing Huang, Jinkun Cao, Fei Ye, Maosen Li, Ya Zhang,


and Cewu Lu. Inverse-transform autoencoder for anomaly
detection. arXiv preprint arXiv:1911.10676, 2019. 2, 4
[26] Simon Jenni, Hailin Jin, and Paolo Favaro. Steering self-


supervised feature learning beyond local pixel statistics. In
CVPR, 2020. 5
[27] Polina Kirichenko, Pavel Izmailov, and Andrew Gordon Wil-


son. Why normalizing ﬂows fail to detect out-of-distribution
data. arXiv preprint arXiv:2006.08545, 2020. 4
[28] Alex Krizhevsky. Learning multiple layers of features from


tiny images. Technical report, University of Toronto, 2009.
4, 8
[29] Yann LeCun, L´eon Bottou, Yoshua Bengio, and Patrick


Haffner. Gradient-based learning applied to document recog-
nition. Proceedings of the IEEE, 1998. 8
[30] Kimin Lee, Kibok Lee, Honglak Lee, and Jinwoo Shin. A


simple uniﬁed framework for detecting out-of-distribution
samples and adversarial attacks. In NIPS, 2018. 7
[31] Yusha Liu, Chun-Liang Li, and Barnab´as P´oczos. Classiﬁer


two sample test for video anomaly detections. In BMVC,
2018. 1
[32] Philipp Liznerski, Lukas Ruff, Robert A Vandermeulen,


Billy Joe Franks, Marius Kloft, and Klaus-Robert M¨uller.
Explainable deep one-class classiﬁcation.
arXiv preprint
arXiv:2007.01760, 2020. 2, 3, 4, 6, 7, 13
[33] Ilya Loshchilov and Frank Hutter. SGDR: Stochastic gradi-


ent descent with warm restarts. In ICLR, 2017. 12


9


[34] Jonathan Masci, Ueli Meier, Dan Cires¸an, and J¨urgen


Schmidhuber. Stacked convolutional auto-encoders for hi-
erarchical feature extraction. In ICANN, 2011. 1
[35] Loic Matthey, Irina Higgins, Demis Hassabis, and Alexan-


der Lerchner.
dsprites:
Disentanglement testing sprites
dataset.
URL
https://github.
com/deepmind/dsprites-
dataset/.[Accessed on: 2018-05-08], 2017. 8
[36] Warren R Morningstar, Cusuh Ham, Andrew G Gallagher,


Balaji Lakshminarayanan, Alexander A Alemi, and Joshua V
Dillon. Density of states estimation for out-of-distribution
detection. arXiv preprint arXiv:2006.09273, 2020. 4
[37] Eric Nalisnick, Akihiro Matsukawa, Yee Whye Teh, and Bal-


aji Lakshminarayanan. Detecting out-of-distribution inputs
to deep generative models using a test for typicality. arXiv
preprint arXiv:1906.02994, 2019. 1
[38] Paolo Napoletano, Flavio Piccoli, and Raimondo Schettini.


Anomaly detection in nanoﬁbrous materials by cnn-based
self-similarity. Sensors, 2018. 4
[39] Mehdi Noroozi and Paolo Favaro. Unsupervised learning of


visual representations by solving jigsaw puzzles. In ECCV,
2016. 4
[40] Aaron van den Oord, Yazhe Li, and Oriol Vinyals. Repre-


sentation learning with contrastive predictive coding. arXiv
preprint arXiv:1807.03748, 2018. 4
[41] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B.


Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss,
V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M.
Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine
learning in Python. Journal of Machine Learning Research,
2011. 12
[42] Jie Ren, Peter J Liu, Emily Fertig, Jasper Snoek, Ryan


Poplin, Mark Depristo, Joshua Dillon, and Balaji Lakshmi-
narayanan. Likelihood ratios for out-of-distribution detec-
tion. In NIPS, 2019. 1, 4
[43] Oliver Rippel, Patrick Mertens, and Dorit Merhof. Modeling


the distribution of normal data in pre-trained deep features
for anomaly detection.
arXiv preprint arXiv:2005.14140,
2020. 4, 7
[44] Marco Rudolph, Bastian Wandt, and Bodo Rosenhahn. Same


same but differnet: Semi-supervised defect detection with
normalizing ﬂows. arXiv preprint arXiv:2008.12577, 2020.
4
[45] Lukas Ruff,
Jacob R Kauffmann,
Robert A Vander-
meulen, Gr´egoire Montavon, Wojciech Samek, Marius
Kloft, Thomas G Dietterich, and Klaus-Robert M¨uller. A
unifying review of deep and shallow anomaly detection.
arXiv preprint arXiv:2009.11732, 2020. 4, 5, 6
[46] Lukas Ruff, Robert Vandermeulen, Nico Goernitz, Lucas


Deecke, Shoaib Ahmed Siddiqui, Alexander Binder, Em-
manuel M¨uller, and Marius Kloft. Deep one-class classiﬁ-
cation. In ICML, 2018. 1, 4
[47] Mohammadreza Salehi, Ainaz Eftekhar, Niousha Sadjadi,


Mohammad Hossein Rohban, and Hamid R Rabiee. Puzzle-
ae: Novelty detection in images through solving puzzles.
arXiv preprint arXiv:2008.12959, 2020. 4
[48] Thomas Schlegl, Philipp Seeb¨ock, Sebastian M Waldstein,


Ursula Schmidt-Erfurth, and Georg Langs.
Unsupervised


anomaly detection with generative adversarial networks to
guide marker discovery. In IPMI, 2017. 1, 4
[49] Bernhard Sch¨olkopf, Robert C Williamson, Alex J Smola,


John Shawe-Taylor, and John C Platt. Support vector method
for novelty detection. In NIPS, 2000. 1, 4
[50] Philipp Seeb¨ock, Sebastian Waldstein, Sophie Klimscha,


Bianca S Gerendas, Ren´e Donner, Thomas Schlegl, Ursula
Schmidt-Erfurth, and Georg Langs.
Identifying and cate-
gorizing anomalies in retinal imaging data. arXiv preprint
arXiv:1612.00686, 2016. 1
[51] Ramprasaath R Selvaraju, Michael Cogswell, Abhishek Das,


Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra.
Grad-cam:
Visual explanations from deep networks via
gradient-based localization. In ICCV, 2017. 2, 4, 6
[52] Kihyuk Sohn, Chun-Liang Li, Jinsung Yoon, Minho Jin, and


Tomas Pﬁster. Learning and evaluating representations for
deep one-class classiﬁcation. In ICLR, 2021. 1, 2, 4, 5, 6, 7,
8
[53] Waqas Sultani, Chen Chen, and Mubarak Shah. Real-world


anomaly detection in surveillance videos. In CVPR, 2018. 1
[54] Jihoon Tack, Sangwoo Mo, Jongheon Jeong, and Jin-


woo Shin.
Csi: Novelty detection via contrastive learn-
ing on distributionally shifted instances.
arXiv preprint
arXiv:2007.08176, 2020. 1, 2, 4
[55] Mingxing Tan and Quoc Le. Efﬁcientnet: Rethinking model


scaling for convolutional neural networks. In ICML, 2019. 7
[56] David MJ Tax and Robert PW Duin. Support vector data


description. Machine learning, 2004. 4
[57] Tareq Tayeh, Sulaiman Aburakhia, Ryan Myers, and Ab-


dallah Shami.
Distance-based anomaly detection for in-
dustrial surfaces using triplet networks.
arXiv preprint
arXiv:2011.04121, 2020. 3, 4
[58] Alexandre B Tsybakov. Introduction to nonparametric esti-


mation. Springer Science & Business Media, 2008. 4
[59] Shashanka
Venkataramanan,
Kuan-Chuan
Peng,
Ra-
jat Vikram Singh, and Abhijit Mahalanobis.
Attention
guided anomaly localization in images.
arXiv preprint
arXiv:1911.08616, 2019. 4
[60] Mang Ye, Xu Zhang, Pong C Yuen, and Shih-Fu Chang. Un-


supervised embedding learning via invariant and spreading
instance feature. In CVPR, 2019. 2, 4
[61] Jihun Yi and Sungroh Yoon. Patch svdd: Patch-level svdd


for anomaly detection and segmentation.
arXiv preprint
arXiv:2006.16067, 2020. 2, 4, 5, 6, 7
[62] Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk


Chun, Junsuk Choe, and Youngjoon Yoo. Cutmix: Regu-
larization strategy to train strong classiﬁers with localizable
features. In ICCV, 2019. 5
[63] Shuangfei Zhai, Yu Cheng, Weining Lu, and Zhongfei


Zhang. Deep structured energy based models for anomaly
detection. arXiv preprint arXiv:1605.07717, 2016. 4
[64] Hongyi Zhang, Moustapha Cisse, Yann N. Dauphin, and


David Lopez-Paz. MixUp: Beyond empirical risk minimiza-
tion. arXiv preprint arXiv:1710.09412, 2017. 5
[65] Zhun Zhong, Liang Zheng, Guoliang Kang, Shaozi Li, and


Yi Yang. Random erasing data augmentation. In AAAI, 2020.
5, 12


10


[66] Bo Zong, Qi Song, Martin Renqiang Min, Wei Cheng, Cris-


tian Lumezanu, Daeki Cho, and Haifeng Chen. Deep autoen-
coding gaussian mixture model for unsupervised anomaly
detection. In ICLR, 2018. 4


11


A. Details on Experiments


A.1. Experiment with ResNet-18


We train a model on 256×256 image. Model parameters are updated for 65k steps using momentum SGD with the
learning rate of 0.03, momentum of 0.9, and the batch size of 64 (or 96 for 3-way). A single cycle of cosine learning rate
decay schedule [33] and L2 weight regularization with a coefﬁcient of 0.00003 are used. We apply random translation and
color jitters for data augmentation to enhance invariance of representations. We note that the same training strategy, such as
the selection of hyperparameters or data augmentations, is applied to different categories. Full range of hyperparameters we
studied are provided in below. We use Tensorﬂow [1], and scikit-learn [41] for GDE implementation.


A.2. Implementation details on CutPaste


Our implementation of the CutPaste augmentation closely follows that of RandomErasing3 [65]. First, we determine the
size of the patch by sampling the area ratio between the patch and the full image from (0.02, 0.15). We then determine
the aspect ratio by sampling from (0.3, 1) ∪(1, 3.3). The locations of the patch where we cut from and paste to are ran-
domly selected in a way that the entire patch appears in the full image. To construct CutPaste-Scar, we directly sample
the width between [2, 16] and the length between [10, 25] in terms of number of pixels. CutPaste-Scar is randomly rotated
between (−45, 45) degrees. Before pasting, we apply color jitter,4 which applies brightness, contrast, saturation, and hue
transformations in sequence with random order, with the maximum intensity of 0.1.


A.3. Ablation Study on Hyperparameters


We study the impact of different values for optimization hyperparameters. Furthermore, we study the impact of CutPaste
hyperparameters, such as jitter intensity or the size of the patch. All experiments are done on CutPaste 3-way setting. Below,
we enumerate the ranges for hyperparameters we studied. The bold-faced items are default values used for experiments in
the main text as well as in this section.


1. Learning rates ∈{0.1, 0.03, 0.01, 0.003}.


2. Number of training epochs ∈{128, 192, 256, 320, 384}.5


3. Maximum jitter intensity on patch ∈{0, 0.1, 0.2, 0.3}.


4. Maximum size of patch ∈{0.1, 0.15, 0.2, 0.3}.


We report the mean and standard error of detection AUCs in Table 7 and 8. We observe that our method is fairly robust
across different learning rates and number of epochs. When the learning rate becomes too small (≤0.003) we observe
slow convergence, so it suggests to train longer. The number of training epochs is also an important hyperparameter for
semi-supervised anomaly detection as early stopping is particularly difﬁcult. We observe that our method provides a reliable
solution when trained for different number of epochs.


For jitter intensity on patch of the CutPaste augmentation, we ﬁnd it more important for texture categories. Part of the
reasons is that the CutPaste augmentation, when applied without jitter augmentation, makes it too difﬁcult to distinguish from
the original images, as texture categories contain repetitive patterns. By adding jitter on the patch, the contrast between pasted
patch and the surrounding area becomes more apparent and this makes the CutPaste prediction task a bit easier. Similarly, the
size of the patch mostly affects the performance on texture categories and we observe the method prefers generally smaller
patch sizes.


A.4. Experiment with EfﬁcientNet


We follow the Keras guide6 of ﬁne-tuning EfﬁcientNet. We use EfﬁcientNet B4 with batch size 24, which is the limit we
tried to ﬁt into single GPU training. We ﬁrst train only the MLP head for 10 epochs with learning rate of 0.03 while freezing
the pretrained backbone. We then ﬁne-tune all layers for 64 epochs with learning rate of 0.0001. We note that the batchnorm
layers are kept frozen as suggested by the Keras guide. The other unstated hyperparameters are the same as in Section A.1.


3https://pytorch.org/docs/stable/_modules/torchvision/transforms/transforms.html#RandomErasing
4https://pytorch.org/docs/stable/_modules/torchvision/transforms/transforms.html#ColorJitter
5Note that, unlike conventional deﬁnition for an epoch, we deﬁne 256 parameter update steps as one epoch.
6https://keras.io/examples/vision/image_classification_efficientnet_fine_tuning/


12


Table 7: Detection AUCs using (1) different learning rates and (2) the number of epochs. We report the mean and standard
error of AUCs for 5 runs with different random seeds.


Category
Learning rates
Number of epochs


0.1
0.03
0.01
0.003
128
192
256
320
384


texture
97.1±0.3
97.0±0.5
97.2±0.3
96.1±0.7
96.6±0.4
96.1±0.7
97.0±0.5
97.0±0.4
96.3±0.4
object
94.4±0.6
94.3±0.6
94.2±0.6
93.9±0.5
94.9±0.6
94.5±0.4
94.3±0.6
94.7±0.5
94.0±0.6


all
95.3±0.5
95.2±0.6
95.2±0.5
94.6±0.6
95.4±0.5
95.0±0.5
95.2±0.6
95.5±0.4
94.8±0.5


Table 8: Detection AUCs using (1) different jitter intensity and (2) the size of patch of the CutPaste augmentation. We report
the mean and standard error of AUCs for 5 runs with different random seeds.


Category
Jitter intensity
Size of patch


0.0
0.1
0.2
0.3
0.1
0.15
0.2
0.3


texture
96.2±0.6
97.0±0.5
97.4±0.3
97.5±0.2
97.1±0.4
97.0±0.5
95.8±0.9
96.6±0.4
object
94.3±0.6
94.3±0.6
94.5±0.5
94.5±0.5
94.5±0.5
94.3±0.6
94.4±0.5
94.5±0.5


all
94.9±0.6
95.2±0.6
95.5±0.4
95.5±0.4
95.3±0.5
95.2±0.6
94.8±0.6
95.2±0.5


A.5. Details on Localization with Patch-based model


The training procedure of patch-based model with CutPaste should be straightforward from Section 2.4. Once patch-based
models are trained, we densely extract representations of 32×32 patches with the stride of 4, which results in ( 256−32


4
+
1)×( 256−32
4
+ 1)×512 = 57×57×512 dimensional tensor of embedding vectors. Then we compute the anomaly score of
512 dimensional embedding vector at each location to obtain 57×57 anomaly score map. Finally, to obtain an anomaly
score map of full resolution (256×256), we apply receptive ﬁeld upsampling via Gaussian smoothing following [32], which
essentially applies the transposed convolution with the stride of 4, the same stride that we used for dense feature extraction,
using a single convolution kernel of size 32×32 whose weights are determined by a Gaussian distribution.


Depending on the category, we ﬁnd different strategies for computing score improves the performance. For those cat-
egories with “aligned objects” (bottle, cable, capsule, metal nut, pill, toothbrush, transistor, zipper), we ﬁnd it useful to
construct one-class classiﬁers at each location separately. This is particularly useful for detecting missing or dislocated com-
ponents (e.g., examples in the second row of Figure 15) as global context is captured by classiﬁers at each location. For
some object categories, such as hazelnut or screw whose objects are randomly rotated, and texture categories, we use a single
one-class classiﬁer applied to all locations.


B. More Localization Visualizations


From Figure 7 to Figure 21, we show localization visualizations of 24 examples for each of 10 object and 5 texture
categories via GradCAM for image-level CutPaste models and patch heatmap for patch-based models. We not only show
successful cases, but also some failure cases.


B.1. Failure Case Analysis


Here we enumerate some failure cases. Note that this is not the comprehensive list of all failure cases, but a few represen-
tative failure cases we ﬁnd via visually inspecting localization visualizations.


• Cable (Figure 8): Missing components (row 2 column 6–8).


• Metal Nut (Figure 11): Flipped components (row 1 column 1–2).


• Screw (Figure 13): Speckle noise in the background (row 3 column 1, 6).


• Transistor (Figure 15): Dislocated or missing components (row 2).


• Tile (Figure 20): dyed tiles (row 2 column 7–8, row 3 column 1–2).


13


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 7: Defect localization on bottle class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


14


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 8: Defect localization on cable class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


15


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 9: Defect localization on capsule class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


16


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 10: Defect localization on hazelnut class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


17


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 11: Defect localization on metal nut class of MVTec dataset. From top to bottom, input images, those with ground-
truth localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


18


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 12: Defect localization on pill class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


19


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 13: Defect localization on screw class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


20


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 14: Defect localization on toothbrush class of MVTec dataset. From top to bottom, input images, those with ground-
truth localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


21


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 15: Defect localization on transistor class of MVTec dataset. From top to bottom, input images, those with ground-
truth localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


22


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 16: Defect localization on zipper class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


23


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 17: Defect localization on carpet class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


24


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 18: Defect localization on grid class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


25


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 19: Defect localization on leather class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


26


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 20: Defect localization on tile class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


27


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Input


GT
mask


Grad
CAM


Patch
Heatmap


Figure 21: Defect localization on wood class of MVTec dataset. From top to bottom, input images, those with ground-truth
localization mask in red, GradCAM results using image-level detector, and heatmaps using patch-level detector.


28
