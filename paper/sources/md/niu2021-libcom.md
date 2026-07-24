1


Making Images Real Again: A Comprehensive


Survey on Deep Image Composition


Li Niu*, Wenyan Cong, Liu Liu, Yan Hong, Bo Zhang, Jing Liang, Liqing Zhang


Abstract—As a common image editing operation, image com-
position/compositing, which is also called object/subject inser-
tion/addition/compositing, aims to combine the foreground from
one image and another background image to produce a composite
image. However, there are many issues that could make the
composite images unrealistic. These issues can be summarized as
the inconsistency between foreground and background, which in-
cludes appearance inconsistency (e.g., incompatible illumination),
geometry inconsistency (e.g., unreasonable size), and semantic
inconsistency (e.g., mismatched semantic context). The image
composition task could be decomposed into multiple sub-tasks,
in which each sub-task targets one or more issues. Specifically,
object placement aims to find reasonable scale, location, and
shape for the foreground. Image blending aims to address
the unnatural boundary between foreground and background.
Image harmonization aims to adjust the illumination statistics of
foreground. Shadow (resp., reflection) generation aims to generate
plausible shadow (resp., reflection) for the foreground. These
sub-tasks can be executed sequentially or in parallel to acquire
realistic composite images. To the best of our knowledge, there
is no previous survey on image composition. In this paper, we
conduct a comprehensive survey over the sub-tasks and combined
task of image composition. For each one, we summarize the
existing methods, available datasets, and common evaluation
metrics. Datasets and codes for image composition are summa-
rized at https://github.com/bcmi/Awesome-Image-Composition.
We have also contributed the first image composition tool-
box: libcom https://github.com/bcmi/libcom, which assembles 10+
image-composition-related functions (e.g., image blending, image
harmonization, object placement, shadow/reflection generation,
generative composition). The ultimate goal of this toolbox is
to solve all image composition problems with simple ‘import
libcom’. Based on libcom toolbox, we also develop an online image
composition workbench https://libcom.ustcnewly.com.


I. INTRODUCTION


Image composition/compositing [120, 17, 253, 134], which
is also called object/subject insertion/addition/compositing in
some literature [180, 228, 7, 184], aims to combine the
foreground from one image and another background image to
form a composite image. More generally, image composition
can be used for combining multiple visual elements from
different sources to construct a new image, which is a common
image editing operation. After compositing a new image with
foreground and background, there exist many issues that could
make the composite image unrealistic and thus significantly
degrade its quality. These issues can be summarized as the


Li Niu, Wenyan Cong, Liu Liu, Yan Hong, Bo Zhang, Jing Liang, and
Liqing Zhang are with MOE Key Lab of Artificial Intelligence, Depart-
ment of Computer Science and Engineering Shanghai Jiao Tong University,
Shanghai, China (email: {ustcnewl,plcwyam17320,shirlley,Hy2628982280,
bo-zhang,leungjing, lqzhang}@sjtu.edu.cn).


* means the corresponding author.


Fig. 1.
Image composition aims to combine the foreground object and the
background image to generate a realistic composite image.


inconsistency between foreground and background, which can
be divided into appearance inconsistency, geometric inconsis-
tency, and semantic inconsistency. Each type of inconsistency
involves a number of issues to be solved. Image composition
task could be decomposed into multiple sub-tasks, in which
each sub-task targets at one or more issues. Next, we will
introduce each type of inconsistency one by one.


The appearance inconsistency includes, but is not limited to:
1) unnatural boundary between foreground and background;
2) incompatible illumination statistics between foreground
and background; 3) missing or implausible shadow and re-
flection of foreground; 4) resolution, sharpness, and noise
discrepancy between foreground and background [105]. For
the first issue, the foreground is usually extracted using
image segmentation [143] or matting [238, 47] algorithms.
However, the foregrounds may not be precisely delineated,
especially at the boundaries. When pasting the foreground with
jagged boundaries on the background, there would be obvious
color artifacts along the boundary. To solve this issue, image
blending [230, 262] aims to address the unnatural boundary
between foreground and background, so that the foreground
could be seamlessly blended with the background. For the
second issue, since the foreground and background may be
captured in different conditions (e.g., weather, season, time
of the day, camera setting), the obtained composite image
could lack visual harmony (e.g., foreground captured in the
daytime and background captured at night). To solve this issue,
image harmonization [204, 33, 29] aims to adjust the illu-
mination statistics of foreground to make it more compatible
with the background, so that the resulting composite image
looks more harmonious. For the third issue, when pasting the
foreground on the background, the foreground may also affect
the background with shadow or reflection. To solve this issue,
shadow generation [124, 270, 175] or reflection generation
[139, 228, 198] focus on generating plausible shadow or
reflection for the foreground according to both foreground and
background information. For the fourth issue, the foreground


arXiv:2106.14490v10  [cs.CV]  15 Jun 2026


2


Fig. 2.
The quality of composite image is degraded by the appearance inconsistency, geometric inconsistency, and semantic inconsistency. Each type of
inconsistency involves a number of issues. Each sub-task targets one or more issues.


Fig. 3. Previous works perform multiple sub-tasks (e.g., object placement, image blending, image harmonization, shadow/reflection generation) sequentially
or in parallel to achieve the goal of image composition.


and background may be from two images with different
resolutions, blur degrees, and noise patterns. The resolution
(resp., sharpness, noise) discrepancy between them could be
mitigated by using super-resolution [224], deblurring [260],
denoising [201] techniques.


The geometric inconsistency includes, but is not limited
to: 1) the foreground object is too large or too small; 2)
the foreground object does not have reasonable supporting
force (e.g., hanging in the air); 3) unreasonable occlusion; 4)
inconsistent perspectives between foreground and background.
In summary, the location, size, and shape of the foreground
may be irrational considering the geometric constraints. Ob-
ject placement [4, 37, 86, 202, 261] tends to seek reason-
able location, size, and shape by predicting the foreground
transformation to avoid the abovementioned inconsistencies.
Previous object placement methods [261, 202] mainly predict
simple form of spatial transformation, that is, shifting and
scaling the foreground to achieve reasonable location and size.
Some other methods [86, 120] predict more general form of
spatial transformation (e.g., affine transformation, perspective
transformation, thin plate spline transformation) to warp the
foreground. In terms of more advanced geometric transforma-
tion like view synthesis and pose transfer, we should resort to


generative approaches [242, 184] to change the viewpoint/pose
of the foreground. When placing the object on the background,
unreasonable occlusion may occur. Most previous methods
seek reasonable placement to avoid unreasonable occlusions,
while some methods [4, 254, 191, 114] aim to fix unreasonable
occlusion by removing the occluded regions of foreground
based on the estimated depth information.


The semantic inconsistency includes, but is not limited
to: 1) the foreground appears at a semantically unreasonable
place (e.g., a zebra is placed in the living room); 2) the
foreground has unreasonable interactions with other objects
or people (e.g., a person is riding a motorbike, but the person
and the motorbike are facing towards opposite directions); 3)
the background may have semantic impact on the foreground
appearance. The semantic inconsistency is judged based on
commonsense knowledge, so the cases of semantic inconsis-
tency may be arguable according to subjective judgement.
For example, when a car is placed in the water, it can be
argued that a car is sinking into the water after a car accident.
However, such event has rather low probability compared
with commonly seen cases, so we can claim that the car
appears at an unreasonable place, which belongs to semantic
inconsistency. Partial solution to semantic inconsistency falls


3


TABLE I
THE ISSUES TO BE SOLVED IN IMAGE COMPOSITION TASK AND THE CORRESPONDING DEEP LEARNING METHODS TO SOLVE THESE ISSUE. NOTE THAT


SOME METHODS ONLY FOCUS ON ONE ISSUE WHILE SOME METHODS ATTEMPT TO SOLVE MULTIPLE ISSUES SIMULTANEOUSLY. “BOUNDARY” MEANS


REFINING THE BOUNDARY BETWEEN FOREGROUND AND BACKGROUND. “APPEARANCE” MEANS ADJUSTING THE ILLUMINATION OF FOREGROUND.


“SHADOW” MEANS GENERATING SHADOW FOR THE FOREGROUND. “REFLECTION” MEANS GENERATING REFLECTION FOR THE FOREGROUND.


“GEOMETRY” MEANS SEEKING REASONABLE LOCATION, SIZE, AND SHAPE FOR THE FOREGROUND CONSIDERING GEOMETRIC CONSTRAINTS.
“OCCLUSION” MEANS COPING WITH THE UNREASONABLE OCCLUSION. “SEMANTICS” MEANS FINDING SUITABLE SEMANTIC CONTEXT FOR THE


FOREGROUND.


boundary
appearance
shadow
reflection
geometry
occlusion
semantics
methods
+
[258]
+
[204, 29, 30, 181, 61, 122, 79, 60, 31, 240,
85, 59, 190, 18, 174, 149]
+
+
[230, 262, 235, 213]
+
+
+
[252]
+
+
[253, 5, 280, 250]
+
[124, 270, 69, 196, 128, 275]
+
[276]
+
+
[120, 202, 261, 147, 284, 287, 163, 279]
+
+
+
[4, 254]
+
[191, 113, 114]
+
+
+
+
[17]
+
+
+
[97]
+
+
+
+
[66]
+
+
+
+
+
+
[242, 184, 255, 22, 185, 25, 229, 183]
+
+
+
+
+
+
+
[106]


into the scope of object placement. To be exact, by predicting
suitable spatial transformation for the foreground, we can
relocate the foreground to a reasonable place or adjust the
pose of foreground to make its interactions with environment
more convincing. Additionally, the appearance of foreground
object may be affected by the background semantically [281],
which is different from low-level appearance inconsistency
(illumination, shadow). For example, a car placed on the
snowy ground may be covered by snow. Another example is
that a student inserted into a group of students wearing school
uniforms should wear the same school uniform. Such semantic
appearance editing (included in “Others” in Fig. 2) is very
flexible and challenging, which will not be fully discussed in
this survey.


So far, we have introduced several sub-tasks (e.g., image
blending, image harmonization, shadow generation, object
placement), in which one sub-task targets one or multiple
issues. Previous works usually focus on one sub-task or
perform multiple sub-tasks sequentially (i.e., image blending
followed by image harmonization) as shown in Fig. 3(a). The
reasonable sequential order is as follows. Given a pair of
foreground and background, we first use object placement to
find suitable scale and location for the foreground, and use
image blending to refine the boundary between foreground
and background. Then, we use image harmonization to adjust
the foreground illumination and shadow generation to generate
plausible shadow for the foreground. Recently, as the diffusion
models have demonstrated unprecedented generation ability,
some works [242, 184] utilize diffusion models to perform
multiple sub-tasks (e.g., image blending, image harmonization,
view synthesis) parallelly as shown in Fig. 3(b). Given a


pair of foreground and background with bounding box, they
propose one unified model to directly produce the composite
image, in which the foreground is blended seamlessly and
harmoniously into the background. These methods re-generate
the foreground object instead of making restrained adjustments
for the foreground object, so we refer to them as generative
image composition methods. We summarize all the potential
issues and the corresponding methods to solve them in Table I.


Instead of creating realistic composite images from arbitrary
pairs of foregrounds and backgrounds, another solution is
seeking for suitable foregrounds from a foreground library,
which are compatible with the background in terms of illu-
mination, geometry, and semantics. Finding compatible fore-
grounds can greatly alleviate the burden of creating realistic
composite images, which is complementary with the afore-
mentioned image composition techniques. This task is called
foreground object search [286, 233, 99], which is especially
useful when we have a high-quality foreground library with
wide coverage.


Image composition has a broad spectrum of applications in
the realm of entertainment, virtual reality, artistic creation, e-
commerce [17, 227, 271] and data augmentation [39, 166, 152]
for downstream tasks. For example, people can replace the
backgrounds of self-portraits and make the obtained images
more realistic using image composition techniques [205, 235].
Similar application scenarios include virtual conference room
or virtual card room. Another example is artistic creation,
in which image composition can be used to create fantastic
artworks that originally only exist in the imagination. More-
over, image composition could also be used for automatic
advertising, which helps advertisers with the product insertion


4


in the background scene [271]. When the product is clothes or
furniture, this application scenario is also known as virtual try-
on or virtual home decoration [120]. Similarly, advertisement
logo compositing [110] targets at embedding some specified
logos in target images. The obtained composite images can be
taken as design renderings or blueprint to help the designer
and the client choose their preferable versions. Additionally,
image composition could create synthetic composite images
with close data distribution to real images, to augment the
training data for downstream tasks like object detection and
instance segmentation [39, 166, 152].


In the remainder of this paper, we will elaborate on each
sub-task or the combined task. In particular, we will introduce
object placement in Section II, image blending in Section III,
image harmonization in Section IV, shadow (resp., reflection)
generation in Section V (resp., VI), generative image compo-
sition in Section VII, foreground object search in Section VIII.
In each section, we will introduce the existing methods,
available datasets, and common evaluation metrics. Finally, we
will conclude the whole paper in Section IX. The contributions
of this paper can be summarized as follows,


• To the best of our knowledge, this is the first comprehen-
sive survey on deep image composition (object insertion).


• We summarize the issues in image composition as three
types of inconsistencies. We clarify the relation between
inconsistency, issue, sub-task, and pipeline in Fig. 2. We
also summarize the issues that previous works attempt to
solve in Table I. All the above summaries give rise to a
large picture for deep image composition.


• For each sub-task and the combined task, we survey
the existing methods, available datasets, and common
evaluation metrics. We also show some experimental
results. We believe that this comprehensive survey can
serve as the roadmap for the future research in a broad
community.


II. OBJECT PLACEMENT


Object placement aims to paste the foreground on the back-
ground with suitable location, size, and shape. As shown in
Fig. 4, the cases of unreasonable object placement include but
are not limited to: a) the foreground object has inappropriate
size (e.g., the dog is too large); b) the foreground object
has unreasonable occlusion with background objects (e.g.,
the fences are unreasonably occluded by the giraffe); c) the
foreground object does not have reasonable force condition
(e.g., the suitcase is floating in the air); d) the foreground
object appears at a semantically unreasonable place (e.g., the
boat appears on the land); e) inconsistent perspectives between
foreground and background (e.g., the car and the bus have
inconsistent perspectives). By taking all the above factors into
consideration, object placement is a very challenging task.


A. Traditional Methods


Some object placement methods designed explicit rules to
find reasonable location and scale for the foreground object.
For example, Remez et al. [166] proposed to move the
foreground object of fixed scale along the same horizontal


scanline on the background. They assumed that the locations
along the same horizontal scanline have similar depth, so that
the true scale of foreground object can be well-preserved.
Wang et al. [209] designed the instance-switching strategy
to generate new images through switching different instances
of the same class with similar shape and scale. To better
refine the position where the object is pasted, Fang et al.
[42] explored appearance consistency heatmap to guide the
object placement, based on the intuition that an object could
be moved to another location which has similar visual context
to its original visual context. Specifically, one element in
the appearance consistency heatmap measures the similarity
between the visual context at this point and original visual
context. Georgakis et al. [54] proposed to combine support
surface detection and semantic segmentation to find proper
location for placing the object. With the determined location,
the size of the object is decided in the light of the depth at this
location and the original scale of the object. Zhang et al. [271]
proposed to model the probability distribution of bounding box
information conditioned on background image and foreground
category using Gaussian mixture model.


Although these rules are effective in some cases, they are
incomplete and sometimes inaccurate, which is far below the
requirement to handle the diverse and complicated challenges
in object placement task.


B. Deep Learning Methods


Apart from the above methods which design explicit rules
to infer the reasonable placement for the foreground object,
some methods [252, 4, 254, 191, 217] employ deep learning
techniques to predict the placement and generate the composite
image automatically.


The existing deep learning based object placement methods
can be divided into category-specific object placement and
instance-specific object placement. For category-specific ob-
ject placement, the model aims to predict plausible bounding
boxes given a background image and a foreground category.
This group of methods assume that the predicted bounding
boxes are suitable for all instances belonging to the same
foreground category. Nevertheless, this assumption is too
restrictive, because different instances from the same cate-
gory may have distinct properties (e.g., geometry, fine-grained
semantics) and thus require bounding boxes with different
scales/locations. In contrast, instance-specific object placement
methods aim to predict plausible spatial transformations given
a background image and a specific foreground object. The
difference between category-specific object placement and
instance-specific object placement is shown in Fig. 5. Next,
we will introduce these two groups of works separately.


1) Category-specific Object Placement: Category-specific
object placement methods can be categorized into genera-
tive approach and discriminative approach. The generative
approach targets at predicting one or multiple reasonable
bounding boxes for the foreground category, whereas the
discriminative approach aims to predict the rationality score
of a bounding box for certain foreground category. The dis-
criminative approach can be further divided into sparse dis-
criminative approach and dense discriminative approach. The


5


Fig. 4.
Examples of unreasonable object placements. The inserted foreground objects are marked with red outlines. From left to right: (a) objects with
inappropriate size; (b) unreasonable occlusion; (c) objects hanging in the air; (d) objects appearing at the semantically unreasonable place; (e) inconsistent
perspectives.


Fig. 5.
In the left subfigure, we compare category-specific object placement with instance-specific object placement. In the right subfigure, we show the
taxonomy of existing object placement methods.


Fig. 6. We show three types of methods for category-specific object placement. Generative model: given the foreground category and background image,
the model generates a reasonable bounding box (e.g., location (x,y) and scale (w,h)). Sparse discriminative model: given the foreground category, foreground
bounding box, and background image, the model predicts a rationality score. Dense discriminative model: given the foreground category and background
image, the model uses sliding window on the feature map to get the rationality score for each bounding box.


sparse discriminative approach takes in a background image
with foreground bounding box and predicts a rationality score.
The dense discriminative approach takes in a background and
produces a feature map, based on which sliding window is
used to predict the rationality score of each bounding box. The
comparison between generative model, sparse discriminative
model, and dense discriminative model is illustrated in Fig. 6.


Generative approaches: Tan et al. [189] proposed to
predict the location and scale of inserted object by taking the
background image and object layout as input. Besides, the
bounding box prediction task is converted to a classification
task by discretizing the locations and scales. Lee et al. [96]
investigated on taking a background semantic map instead of
a background image as input. Given a background semantic


map, they designed a network consisting of two generative
modules, in which the first module accounts for the bounding
box of inserted object and the second module accounts for
the mask shape of inserted object. Parihar et al. [154] focused
on “person” category and leveraged the prior knowledge of
text-to-image generation model. Specifically, the foreground
mask and foreground image are jointly optimized to fit the
background and text prompt, after which the foreground mask
can be used to indicate the person placement.


Discriminative approaches: The methods in [37, 38] used
a network to predict whether a bounding box is suitable for
certain foreground category, based on the contextual informa-
tion surrounding the bounding box. This approach needs to
pass through the network once for each bounding box, which


6


Fig. 7.
We show three types of methods for instance-specific object placement. Generative model: given the foreground, foreground object mask, and
background, the model generates a reasonable placement (e.g., location (x,y) and scale (w,h)) for the foreground. Sparse discriminative model: given the
composite image and composite foreground mask, the model predicts a rationality score. Dense discriminative model: given the foreground, foreground object
mask, and background, the model predicts a rationality score map containing the rationality scores for all locations.


is very time-consuming. To accelerate this process, Volokitin
et al. [208] employed masked convolutions to aggregate the
contextual information along four directions as context feature
maps, based on which the contextual information excluding
each bounding box can be obtained efficiently to predict the
rationality score for this bounding box.


2) Instance-specific Object Placement:
Instance-specific
object placement methods can also be categorized into gener-
ative approach and discriminative approach. The generative
approach targets at predicting one or multiple reasonable
placements (i.e., spatial transformations) for the foreground
object, whereas the discriminative approach aims to predict
the rationality score of a composite image in terms of the
foreground object placement. The discriminative approach
can be further divided into sparse discriminative approach
and dense discriminative approach. The sparse discriminative
approach takes in a composite image and predicts a rationality
score. The dense discriminative approach takes in a pair of
foreground and background, and predicts a rationality score
map. The comparison between generative model, sparse dis-
criminative model, and dense discriminative model is illus-
trated in Fig. 7.


Generative approaches: Generative approaches [202, 261,
120, 111, 110, 245, 220, 28] predict different types of spatial
transformations (e.g., shifting and scaling, affine transforma-
tion, perspective transformation) for the foreground object,
which is more flexible and powerful than category-specific
object placement methods. For instance, Tripathi et al. [202]
developed a model with generator, discriminator, and target
network. Given a pair of background and foreground, the
generator predicts an affine transformation for the foreground
object to produce a composite image. The produced composite
image is expected to fool the discriminator and fit the target
network corresponding to a downstream task (e.g., object
detection). To produce multiple reasonable placements, Zhang
et al. [261] combined the foreground feature, background
feature, and a random vector to predict the object placement.
Moreover, they ensured the diversity of object placement by


enforcing the pairwise distances between predicted placements
to approach those between corresponding random vectors. To
promote the diversity of generated placements, Zhou et al.
[284] established the bijection between random vector and
positive composite image. Moreover, they reformulated object
placement as a graph completion task. In particular, back-
ground nodes have both content features and placements, while
the inserted foreground node only has content feature, giving
rise to an incomplete graph. Hence, they estimated the missing
placement for the foreground node to complete the graph.
Zhang et al. [268] proposed to make sequential decisions
to produce a reasonable placement by using reinforcement
learning. Qin et al. [163] employed a pre-trained large multi-
modal model to generate a caption containing the placement
information, and then predicted the placement bounding boxes.
Zhou et al. [279] first predicted candidate bounding boxes and
then associated each object query with matched bounding box.


In terms of more advanced geometric transformation like
view synthesis and pose transfer, some methods [4, 120, 256,
57] predicted perspective transformation to adjust the view-
point and some methods [217, 244] predicted human pose in
the scene context. Zhan et al. [252] adopted spatial transformer
network (STN) [77] to predict the warping parameters under
an adversarial learning framework. Azadi et al. [4] employed
STN to warp the foreground and relative appearance flow
network to change the viewpoint of foreground. Additionally,
they investigated on self-consistency constraint, that is, the
generated composite image could be decomposed back to the
foreground and background. ST-GAN [120] proposed to warp
a foreground object into a background image with iterative
spatial transformations predicted by STN. As a follow-up
work, Kikuchi et al. [86] replaced the iterative spatial trans-
formations in [120] with one-shot spatial transformation. Gou
et al. [57] revealed that for perspective transformation, predict-
ing the target locations of four source points is more effective
than predicting the locations for more source points [256] or
predicting the transformation parameters [120]. However, the
view and pose synthesis ability is quite limited, especially


7


Fig. 8.
The visualization results of different object placement methods on OPA [126] dataset. From left to right in each row, we show the foreground,
background, and composite images obtained by TERSE [202], PlaceNet [261], SimOPA (SOPA) [126], FOPA [147].


for drastic viewpoint change (e.g., from front view to side
view) and complicated human-object interaction (e.g., playing
piano). To accomplish drastic viewpoint change and flexible
pose transfer, generative composition methods attempted to
re-generate the foreground object, which will be introduced in
Section VII.


Discriminative approaches: Liu et al. [126] proposed a
discriminative approach named SimOPA to verify whether
a composite image is rational in terms of the foreground
object placement. Particularly, they feed the concatenation of
composite image and foreground mask into a binary classi-
fication network to predict a rationality score. However, this
discriminative approach is very inefficient, because they need
to go through the discriminative network multiple times to
find a reasonable object placement. To address this issue, Niu
et al. [147] dubbed SimOPA as slow object placement as-
sessment (SOPA) model and proposed a fast object placement
assessment (FOPA) model, which can predict the rationality
scores at all locations by going through the model only


once. Precisely, they take in a pair of background and scaled
foreground, and produce a rationality score map, in which
each entry represents the rationality score of the composite
image obtained by pasting the foreground at this location. They
developed several innovations (e.g., background prior transfer,
feature mimicking) to bridge the performance gap between
FOPA and SOPA, reaching the conclusion that FOPA can
achieve comparable performance with SimOPA at significantly
reduced cost. FOPA [147] has also demonstrated stronger
ability to generate realistic composite images than generative
approaches [284, 268]. Similar to FOPA [147], Zhu et al.
[287], Poska et al. [162] also proposed to predict the rationality
scores of all scales and locations, based on the interaction
output between foreground and background. Gao et al. [48]
explored extending object placement task to a broader range
of foreground categories and background scenes.


In the end, we briefly discuss the occlusion issue. Most
of the above methods seek for reasonable placements to
avoid the occurrence of occlusion, i.e., the inserted foreground


8


is not occluded by background objects. Differently, a few
methods [4, 254, 191, 56] attempt to address the unreasonable
occlusion when it occurs. Specifically, they first estimate the
relative depth relation between the foreground object and
the surrounding background objects. Then, they remove the
occluded part of foreground object. In this way, they are
able to generate composite images with reasonable inter-object
occlusions.


C. Datasets and Evaluation Metrics


In some early works [202, 42], object placement is used as
data augmentation strategy to facilitate the downstream tasks
(e.g., object detection, instance segmentation). Therefore, they
make use of existing object detection and instance segmenta-
tion datasets [121, 41, 32, 53]. In particular, the foregrounds
are cropped out based on the annotated segmentation masks.
After removing the foreground objects, the remaining incom-
plete background images are restored to complete background
images by using image inpainting techniques [246, 125, 248].
In this manner, triplets of foregrounds, backgrounds, and
ground-truth composite images can be obtained. Some other
works focus on specific applications like 2D virtual try-
on [120, 86, 111] (e.g., placing glasses/hats on human faces) or
logo composition [110] (e.g., attaching logo to product image),
so they need to collect foregrounds and backgrounds specif-
ically for these applications. More recently, Liu et al. [126]
released a large-scale object placement assessment dataset
named OPA, which consists of 73,470 composite images and
their binary rationality labels. OPA dataset is constructed by
compositing the foregrounds and backgrounds from COCO
dataset [121], followed by manually labelling the rationality
of obtained composite images. A large number of annotated
composite images could greatly facilitate the research on
object placement. Qin et al. [163] established the OPAZ dataset
following the format of OPA.


To evaluate the quality of generated composite images,
previous object placement works usually adopt the following
schemes: 1) Some works measure the similarity between real
images and composite images. For example, Tan et al. [189]
score the correlation between the distributions of predicted
boxes and ground-truth boxes. Zhang et al. [261] calculate
Frechet Inception Distance (FID) [67] between composite
images and real images. However, they cannot evaluate each
individual composite image. 2) Some works [202, 42] utilize
the performance improvement of downstream tasks (e.g., ob-
ject detection) to evaluate the quality of composite images,
where the training sets of the downstream tasks are augmented
with generated composite images. However, the evaluation
cost is quite huge and the improvement in downstream tasks
may not reliably reflect the quality of composite images,
because it has been revealed in [55] that randomly generated
unrealistic composite images could also boost the performance
of downstream tasks. 3) Another common evaluation strategy
is user study, where people are asked to score the rationality of
object placement [96, 189]. User study complies with human
perception and each composite image can be evaluated indi-
vidually. OPA dataset [126] has annotated composite images


and its test set could be used for evaluation. Nevertheless, the
sparse annotations only cover a small proportion of locations
and scales, which limits the universal evaluation of arbitrary
composition results. 4) To support the evaluation of arbitrary
composition results, we can train a binary classifier based on
annotated positive and negative composite images, to predict
the rationality score of an arbitrary composite image.


D. Experiments


In this section, we focus on instance-specific object place-
ment and compare existing object placement methods for
generating a reasonable composite image. For ease of com-
parison, we fix the foreground scale and only predict the
reasonable location for the foreground object. Recall that
instance-specific object placement methods are divided into
generative approaches and discriminative approaches. For gen-
erative approach, we choose TERSE [202] and PlaceNet [261],
which can directly predict one placement. For discriminative
approach, we report the results of SimOPA [126] and FOPA
[147]. We use SimOPA and FOPA to generate rationality score
map, based on which the location with the largest rationality
score is chosen as the optimal placement. We train and evaluate
different methods on OPA dataset [126]. The test results are
shown in Fig. 8, from which it can be seen that discriminative
approaches usually achieve better results than generative ap-
proaches. One possible explanation is that TERSE [202] and
PlaceNet [261] only utilize the annotated composite images to
update the discriminator, without fully using the annotations
to train the generator. Nevertheless, discriminative approaches
also have failure cases when dealing with occlusion and
complex scenes (e.g., unreasonable occlusion between fire
hydrant and fallen branches in row 4).


For practical usage, we recommend dense discriminative
approaches [147, 287], which are more stable, effective, and
flexible than generative approaches and sparse discriminative
approaches. Dense discriminative approaches can efficiently
identify reasonable bounding boxes (i.e., location, scale) for
the inserted foreground object. Then, if necessary, generative
composition methods could be used to further adjust the
viewpoint and pose of foreground object (see Section VII).


III. IMAGE BLENDING


During image composition, the foreground is usually ex-
tracted using image segmentation [143] or matting [238]
methods. However, the segmentation or matting results may
be noisy and the foregrounds are not precisely delineated.
When the foreground with jagged boundaries is pasted on the
background, there will be abrupt intensity change between the
foreground and background. To refine the boundary and reduce
the fuzziness, image blending techniques have been developed.


A. Traditional Methods


Traditional image blending methods aim to smooth the tran-
sition between foreground and background. Alpha blending
[161] proposed to assign alpha values for boundary pixels
indicating what fraction of the colors are from foreground or


9


Fig. 9. The leftmost column is the initial composite image obtained using the alpha matte predicted by LFPNet [127]. The rightmost column is the ground-truth
composite image obtained using ground-truth alpha matte. The middle columns are the refined results obtained by Poisson image blending [158], GP-GAN
[230], Zhang et al. [262], and MLF [258]. The odd rows display the whole image, while the even rows zoom in the red bounding boxes in the odd rows for
better observation.


background, in which the alpha values need to be manually
set. Alpha blending is a simple and fast method, but it blurs
the fine details and brings in ghost effects. Considering multi-
scale information, Laplacian pyramid blending [9] proposed
to build multi-scale Laplacian pyramids for two images and
perform alpha blending at each scale. Then, the final output is
obtained by adding up the blended results of different scales.


Another group of methods attempt to achieve smooth
boundary transition by enforcing gradient domain smoothness
[44, 84, 98, 188]. The earliest work along this research direc-


tion is Poisson image blending [158]. Poisson image blending
[158] proposed to enforce the gradient domain consistency
with respect to the source image containing the foreground,
where the gradient of inserted foreground is computed and
propagated from the boundary pixels in the background. Al-
though Poisson image blending can yield more pleasant results
than simple alpha blending, it is very time-consuming to solve
the Poisson equation. Therefore, there are many follow-up
works [188, 192, 84] to accelerate Poisson image blending
by using different techniques. Based on the observation that


10


the effectiveness of Poisson image blending seriously depends
on the boundary condition, [78] designed a method to optimize
the boundary condition. To avoid the color bleeding and halo
effect brought by Poisson image blending, Tao et al. [194]
developed a two-step algorithm: first processing the gradient
values on the boundary and then employing a weighted inte-
gration scheme to reconstruct the image from its gradient field.
The above methods based on gradient domain smoothness can
smooth the transition between foreground and background to
some extent. However, background colors may seep through
the foreground too much and distort the foreground color,
which would bring significant loss to the foreground content.


B. Deep Learning Methods


Inspired by traditional image blending methods [158, 9],
some recent works [230, 262] explored incorporating the
function of smoothing boundary into deep learning network.
Among them, the works [230, 262, 258] not only enabled
smooth transition over the boundary, but also reduced the
illumination discrepancy between foreground and background,
in which the latter one is the goal of image harmonization
in Section IV. In this section, we only introduce the way
they enable smooth transition over the boundary. These two
works [230, 262] are both inspired by [158]. Specifically, they
added the gradient domain constraint to the objective function
according to Poisson equation, which can produce a smooth
blending boundary with gradient domain consistency. They
both optimized over the input composite image to minimize
the gradient domain loss. Differently, [230] had a close-
form solution, while [262] converted the gradient domain loss
to a differentiable loss function and uses gradient descent
algorithm.


Different from [230, 262] which are inspired by traditional
image blending, recent works [258, 235] proposed learnable
image blending, which produces a seamlessly blended image
by taking in a pair of foreground image and background image.
Specifically, the fusion network in Zhang et al. [258] used two
separate encoders to extract and fuse multi-scale features from
foreground and background. Because the fusion network relies
on ground-truth composite images obtained by using accurate
alpha matte as supervision, the work [258] also proposed an
easy-to-hard data-augmentation scheme to relieve the burden
of annotating ground-truth alpha matte. Similarly, Xing et al.
[235] proposed to concatenate foreground image, background
image, and imperfect mask as input to generate a blended
image. For these methods [258, 235], the trained models
have the ability to refine imperfect masks and deliver more
naturally blended images. Besides the GAN-based generative
models [258, 235], conditional diffusion models [264, 92]
could also generate blended image conditioned on the compos-
ite image, demonstrating stronger generalization ability. For
the above methods, the quality of initial mask has significant
impact on the quality of blended image. If the initial mask is
of very poor quality, these methods can hardly produce high-
quality blended image.


More recently, mask-free image blending has emerged,
which does not require initial masks. ControlCom [255] re-
ceived a foreground image enclosing the foreground object


and a background image with bounding box specifying the
foreground placement, producing a composite image. The
mask-free methods relieve the burden of initial mask predic-
tion, which is not affected by the quality of initial masks. In
[255], the foreground object features are injected into diffusion
model via cross-attention. Such strategy to inject foreground
information may lead to the slight loss or distortion of fore-
ground details. In contrast, the in-context learning strategy
to inject foreground information [183], that is, concatenating
foreground image as one of the inputs, can better preserve the
foreground details.


C. Datasets and Evaluation Metrics


To the best of our knowledge, there are only few deep
learning methods [230, 262, 258] for image blending and there
is no unified benchmark dataset. Zhang et al. [262] do not
mention the source of used images. Wu et al. [230] manually
crop objects from transient attributes database [93] to create
input composite images. Similarly, Zhang et al. [258] take
foreground images from segmentation datasets [70, 173] and
random background images to construct input pairs.


The existing deep image blending works [230, 262, 258]
adopt the following evaluation metrics: 1) Zhang et al. [258]
deem the composite images obtained using ground-truth alpha
matte as ground-truth composite image, and calculate Peak
Signal-to-Noise Ratio (PSNR) between resultant image and
ground-truth composite image. 2) conducting user study by
asking engaged users to select the most realistic images; 3)
calculating realism score using the pretrained model [285]
which reflects the realism of a composite image.


D. Experiments


We evaluate different image blending methods conditioned
on the matting results. First, we create composite images using
the alpha mattes predicted by the state-of-the-art trimap-based
image matting methods [34, 131, 127]. Then, we hope that
image blending methods can refine the obtained composite
images. We sample 500 foreground images from recent im-
age matting datasets [127, 104, 103]. For each foreground
image, we randomly select two background images from
BG20K [105]. The foreground images and background images
form the test set.


By taking LFPNet [127] as an example matting method, we
predict the alpha mattes and obtain the composite images. We
observe that LFPNet can generally achieve satisfactory results
except some challenging cases. We select several of its failure
cases to verify the effectiveness of image blending methods.


We report the results of Poisson image blending [158], GP-
GAN [230], Zhang et al. [262], and MLF [258]. We also report
the ground-truth composite image obtained using ground-truth
alpha matte for comparison. From Fig. 9, it can be seen that
the composite images obtained using predicted alpha mattes
are very close to the ground-truth composite image except
partial boundary regions. We observe that Poisson image
blending [158] smooths the transition boundary to some extent,
but unexpectedly distorts the foreground content by seeping
through the foreground. GP-GAN [230] and Zhang et al. [262]


11


are inspired by Poisson image blending, but use content loss
to preserve the original foreground content. Therefore, they
strike a balance between preserving the foreground content and
smoothing the boundary. However, some smoothed boundary
regions are still not satisfactory. MLF [258] can obtain visually
appealing results in some cases. Nonetheless, it may erase
detailed information (e.g., the small leaves of a pineapple) and
fail in handling transparent foreground objects (e.g., plastic
bag).


For practical usage, traditional image blending methods are
recommended under very specific circumstances. For example,
when the foreground mask is accurate and there is no high
demand for sharp boundary, alpha blending [161] is applicable.
When the colors of foreground boundaries are expected to be
close to the colors of adjacent background boundaries, Poisson
blending [158] is applicable. Otherwise, conditional diffu-
sion models [92, 183] are recommended. When high-quality
initial mask is available, diffusion model [92] conditioned
on composite image is recommended. When initial mask is
unavailable or only poor-quality initial mask is available,
diffusion model [183] conditioned on background image and
foreground image is recommended.


IV. IMAGE HARMONIZATION


Given a composite image, its foreground and background
are likely to be captured in different conditions (e.g., weather,
season, time of day, camera setting), and thus have distinctive
illumination characteristics, which make them look incom-
patible. Image harmonization aims to adjust the appearance
of composite foreground according to composite background
to make it compatible with the composite background. We
classify the existing methods into rendering based and non-
rendering based methods according to whether using rendering
techniques.


A. Rendering based Methods


Conventional image relighting [153, 179, 223, 263, 200]
aims to adjust the appearance of an image or the object in
an image as lit by novel illumination. With some adaptation,
image relighting can also be used to adjust the foreground
appearance according to the illumination of a new background
[153, 263, 13, 72], which bears some resemblance to image
harmonization. However, they usually achieve this goal by
inferring explicit illumination condition, material properties, or
3D geometry, in which the supervision for these information
is difficult and expensive to acquire. Besides, they generally
have strong assumption about the light source, which may not
generalize well to complicated real-world scenes.


B. Non-rendering based Methods


Early traditional image harmonization methods [241, 187,
94, 182] performed color transformation on the foreground
to match the low-level color statistics between foreground and
background. The difference between different methods mainly
lies in the matching details. For example, Xue et al. [241]
predicted the histogram zone (e.g., low, middle, high) which


can be best matched between foreground and background,
and then adjusted the foreground color to match the selected
zone between foreground and background. [187] explored
decomposing an image into a multi-resolution pyramid with
multiple subbands, and performing histogram matching for
each subband between foreground and background. Lalonde
and Efros [94] proposed to represent foreground and back-
ground with color clusters, followed by matching foreground
and background color clusters. Song et al. [182] proposed
to calculate the color transformation (channel-wise scales)
based on the gray pixels of foreground and background,
because normalized illumination color can be directly derived
from the pixel values of gray pixels. In some works on sky
replacement [288, 193, 203], they attempted to match the
color statistics (e.g., mean, variance) between sky region and
non-sky region. Broadly speaking, traditional color transfer
methods [165, 234, 45, 160, 43, 3] can also be used for color
matching between foreground and background to produce a
harmonized image.


Early deep learning based image harmonization methods
target at making the harmonized images indistinguishable
from real images. For instance, Zhu et al. [285] explored
predicting the realism of an image using a CNN classifier. With
such realism predictor, they learned the color transformation
for the foreground to achieve high realism score, and also
enforced the color variation in different channels to be close.
Similar to [285], the works [253, 17] used adversarial learning
to make the harmonized images indistinguishable from real
images. Bhattad and Forsyth [7] drew inspiration from Retinex
theory [88] that an image can be decomposed into albedo
(reflectance) and shading (illumination). On the premise of
this assumption, an image harmonization model is trained so
that the harmonized result should have consistent albedo and
consistent background shading with input composite image.


With the emergence of image harmonization datasets con-
sisting of paired training data (see Section IV-E), abundant
image harmonization methods [204, 29, 31, 129, 136, 190, 20,
247, 222, 157, 210, 100, 273] using paired supervision have
been developed. Tsai et al. [204] proposed the first end-to-end
CNN network for image harmonization and leveraged auxil-
iary semantic segmentation branch to enhance the basic image
harmonization network. Another work Sofiiuk et al. [181] also
utilized high-level semantic features, which are inserted into
the encoder to provide auxiliary information. Cun and Pun [33]
designed an additional Spatial-Separated Attention Module to
deal with foreground and background feature maps separately.
Hao et al. [65] employed self-attention [218] mechanism
to propagate relevant information from background to fore-
ground. By treating different capture conditions as different
domains, Cong et al. [29] proposed a domain verification
discriminator to pull close the foreground domain and back-
ground domain. Similarly, Cong et al. [30] formulated image
harmonization as background-guided domain translation task,
in which the domain code of background is directly used to
guide the harmonization process. One byproduct of [30] is
predicting the inharmony level of an image by comparing the
domain codes of foreground and background, so that we can
selectively harmonize those inharmonious composite images.


12


Inspired by [30], Valanarasu et al. [205] proposed to extract
style code from part of background.


In
[122],
they
reframed
image
harmonization
as
a
background-to-foreground style transfer problem and intro-
duced region-aware adaptive instance normalization (AdaIn)
to transfer visual style from the background to the fore-
ground. A succeeding work [64] extended [122] by search-
ing foreground-relevant background regions and transferring
foreground-relevant style from background to foreground.
They also extended the triplet loss in [30] to contrastive loss.
Some subsequent works [81, 19] adopted the similar idea of
searching the background regions matching the foreground
region.


Analogous to [7] using Retinex theory, Guo et al. [61] also
developed a model to disentangle a composite image into re-
flectance map and illumination map, in which the illumination
map is harmonized by transferring lighting information from
background to foreground. Another work [60] also adopted
the similar decomposition network and explored integrating
transformer block [207] into the network, which is further
extended to [62]. Following the disentanglement technical
route, Jiang et al. [79] proposed to disentangle an image into
content representation and appearance representation. Then,
the appearance representation of foreground is superseded
by that of background to accomplish the goal of image
harmonization.


Inspired by traditional image harmonization methods [241,
187] which applied color transformation to adjust the fore-
ground appearance, Cong et al. [31] proposed to learn color
transformation using deep learning for image harmonization.
They combined color-to-color transformation and pixel-to-
pixel transformation in a unified framework coherently. Several
other works [240, 118, 168, 85, 59, 212, 142] also proposed to
predict various types of color transformations (e.g., color filter,
rendering curve, linear transformation) for efficient image
harmonization. Beyond different color transformations, some
works [237, 190] explored different color spaces.


Some works [149, 174, 18] concurred that dynamic kernels
applied to feature maps can boost the harmonization perfor-
mance. Furthermore, [149, 174] pointed out the importance
of global information in dynamic kernel prediction. Niu et al.
[148] studied domain adaptive image harmonization by treat-
ing different datasets as different domains. Specifically, an
automatic augmentation network was developed to enrich the
illumination diversity of a target domain with limited data.


Recently, some diffusion-based image harmonization mod-
els [102, 21, 283, 282, 167, 265, 130] have applied con-
ditional diffusion model to image harmonization task. Zhou
et al. [282] proposed to modify VAE decoder to alleviate
the image distortion issue of diffusion model. Ren et al.
[167] proposed to inject background illumination information
into diffusion model. Zhang et al. [265] designed a diffusion
model according to the principle that the linear blending of an
object’s appearances under different illumination conditions
is consistent with its appearance under mixed illumination.
Chadebec et al. [15] proposed latent bridge matching between
source image and target image, achieving superior and stable
performance for image harmonization.


Tao et al. [197] pointed out that when transferring the back-
ground illumination to the foreground, different foreground
reflectances would yield different harmonization results. They
designed a reflectance-guided harmonization network, which
can produce diverse harmonized results considering different
foreground reflectances.


C. Variants of Image Harmonization Task


In this subsection, we discuss two variants of standard image
harmonization task.


Blind image harmonization: Most image harmonization
methods require the foreground mask as input, which means
that the inharmonious region is known in advance. However,
in real-world applications, we may not know the exact in-
harmonious region in advance. Image harmonization without
foreground mask is called blind image harmonization. Cun and
Pun [33] considered the problem of blind image harmoniza-
tion. They proposed to predict the inharmonious region mask
in the attention block, which deals with the foreground and
background separately according to the predicted mask.


Subsequently, some works [116, 117, 232, 231, 269, 178,
23] focused on inharmonious region localization task, which
aims to localize the inharmonious region in an image. Liang
et al. [116] explored aggregating multi-scale contextual infor-
mation and suppressing redundant information. The methods
[117, 232] proposed to magnify the domain discrepancy be-
tween foreground and background using color mapping for
ease of identifying the inharmonious region. Chen et al. [23]
explored multi-view representation including frequency view
and flipped view.


Painterly image harmonization: In standard image harmo-
nization, both foreground and background are from realistic
images. There exist certain application scenarios that the
background is an artistic image while the foreground is from a
realistic image, in which case the standard image harmoniza-
tion models may not work well. To overcome this problem,
painterly image harmonization [138] has been studied to
harmonize the realistic foreground according to the artistic
background to obtain a uniformly stylized composite image.


The relation between painterly image harmonization and
standard image harmonization is like the relation between pho-
torealistic style transfer and artistic style transfer. Painterly im-
age harmonization is more challenging because multiple levels
of styles (i.e., color, simple texture, complex texture) [151]
need to be transferred from background to foreground, while
standard image harmonization only needs to transfer low-level
style (i.e., illumination). Painterly image harmonization is also
referred to as cross-domain image composition [63, 134, 236,
101, 221, 159].
The existing painterly image harmonization methods [138,
156, 12, 132, 219, 151, 150] can be roughly categorized
into optimization-based methods and feed-forward methods.
Optimization-based methods optimize the input image to
minimize the style loss and content loss, which is very
time-consuming. For example, Luan et al. [138] proposed to
optimize the input image with two passes, in which the first
pass aims at robust coarse harmonization and the second pass


13


Fig. 10. In the first (resp., second, third, fourth) row, we show two examples from RealHM [79] (resp., HFlickr in iHarmony4 [11], HVIDIT [61], Hday2night
in iHarmony4 [11]) dataset. From left to right in each example, we show the composite image, the foreground mask, and the ground-truth harmonized image.


targets at high-quality refinement. Li et al. [108] proposed
to optimize the latent features of diffusion model based on
content loss and style loss.


Feed-forward methods send the input image through the
model to output the harmonized result. For example, Peng
et al. [156] applied adaptive instance normalization to match
the means and variances between the feature map of com-
posite image and that of artistic background. Cao et al. [12]
performed painterly image harmonization in both frequency
domain and spatial domain, considering that artistic paintings
often have periodic textures and patterns which appear regu-
larly. Niu et al. [151] divided styles into low-level styles (e.g.,
color, simple pattern) and high-level styles (e.g., complex pat-
tern), and devised a progressive network which can harmonize
a composite image from low-level styles to high-level styles
progressively. Niu et al. [150] proposed style-level supervision
based on pairs of artistic objects and photographic objects,
considering that it is hard to obtain pixel-wise supervision
based on pairs of artistic objects and photographic objects. To
achieve this goal, Niu et al. [150] built an artistic object dataset
containing the artistic objects segmented from artistic images.
Each artistic object is associated with a list of photographic
objects that have similar appearance and semantics to it. For
each artistic object in an artistic image, it can be covered by
a similar photographic object, yielding a composite image.


Then, the harmonized photographic object in the composite
image is expected to have the same style as the artistic object.
Sun and Zhang [186] applied dynamic kernel to painterly
harmonization. Lu et al. [132] is the first work introducing
diffusion model to painterly image harmonization, which can
significantly outperform GAN-based methods when the back-
ground has dense textures or abstract style.


D. Related Research Fields


Image harmonization is closely related to style transfer.
Note that both artistic style transfer [52, 75, 155] and pho-
torealistic style transfer [137, 112] belong to style transfer.
Image harmonization is closer to photorealistic style transfer,
which transfers the style of a reference photo to another input
photo. There are two main differences between image har-
monization and photorealistic style transfer. 1) Firstly, image
harmonization adjusts the foreground appearance according
to the background, which must take the foreground location
into consideration due to the locality property. In contrast,
photorealistic style transfer adjusts the appearance of a whole
input image according to another whole reference image.
2) Secondly, the definition of “style” in photorealistic style
transfer is unclear and coarsely depends on the employed
style loss (e.g., Gram matrix loss [52], AdaIn loss [75]).


14


Differently, the goal of image harmonization is clearly ad-
justing the illumination statistics of foreground, so that the
resultant foreground looks like the same object captured in
the background illumination condition.


E. Datasets and Evaluation Metrics


A large amount of composite images can be easily obtained
by pasting the foreground from one image on another back-
ground image, but it is not easy to obtain the ground-truth
harmonized image for the composite image. Training deep
learning models requires abundant pairs of composite images
and ground-truth harmonized images. Existing works have
designed different schemes to construct image harmonization
dataset. The key lies in how to construct a set of images with
the same content yet different illuminations. We categorize the
existing schemes into four groups: manual editing, color trans-
fer, rendering technique, real shot. We show one representative
dataset from each group in Fig. 10.


Manual editing: HAdobe5k sub-dataset in [29] is con-
structed based on MIT-Adobe FiveK dataset [10], in which
each image is manually edited to five different illumination
conditions. Swapping their foregrounds can yield pairs of
composite images and ground-truth images. Jiang et al. [79]
released a small-scale RealHM dataset with 216 image pairs,
which is constructed based on real composite images obtained
by pasting foregrounds on backgrounds. Human annotators
manually adjust the foreground according to the background
to obtain the ground-truth. Manual editing is time-consuming,
labor-intensive, and unreliable.


Color transfer: Some works [204, 33, 29] adjusted the
foreground of real image to create synthetic composite image.
Specifically, they treat a real image as harmonized image,
segment a foreground region, and adjust this foreground region
to be inconsistent with the background, yielding a synthetic
composite image. HCOCO (resp., HFlickr) sub-dataset in [29]
is built upon COCO [121] (resp., crawled images from Flickr
website), in which the foregrounds in real images are adjusted
using traditional color transfer methods [165, 234, 45, 160].
These color transfer methods require reference object. Given a
foreground object, an object from the same category and with
similar appearance is found as its reference object. Then, color
transfer is performed to change the illumination of foreground
object to match the reference object. It is worth noting that
such color transfer may produce low-quality synthetic compos-
ite images. Thus, Cong et al. [29] manually filter out the low-
quality synthetic composite images. SycoNet [148] learned
a mapping from real images to filtered synthetic composite
images, which can capture the human filtering knowledge and
produce high-quality synthetic composite images.


Another issue is that traditional color transfer methods may
not faithfully reflect the natural illumination variation. To
address this issue, Niu et al. [149] proposed to transit across
different illumination conditions by virtue of color checker,
leading to ccHarmony dataset which can more faithfully
reflect the natural illumination variation. Color checker is a
simple way to record the illumination condition when taking
photos. Given two photos with color checkers, color transfer


parameters can be calculated based on two color checkers to
transit across two illumination conditions.


Rendering technique:
Cao et al. [11] constructed Rd-
Harmony dataset by varying the lighting condition of the
same scene using 3D rendering techniques. Within a set of
images with the same scene yet various lighting conditions,
the composite images could be obtained by exchanging the
foregrounds between two images. Similarly, Guo et al. [61]
constructed HVIDIT dataset based on the rendered dataset
[40]. Another solution is rendering the same 3D foreground
model using different illumination maps [153, 5, 73, 72].
However, the rendered images have a large domain gap with
real images, so the harmonization model trained on rendered
images cannot be directly applied to real test images.


Real shot:
A natural way to build image harmonization
dataset is collecting a set of foreground images captured in
different illumination conditions, followed by replacing one
foreground with another counterpart. For example, Transient
Attributes Database [93] contains 101 sets, in which each
set has well-aligned images for the same scene captured in
different conditions (e.g., weather, time of the day, season).
This dataset has been used to construct pairs in Hday2night
sub-dataset in [29]. However, collecting the dataset like [93]
calls for capturing the same scene with a fixed camera for
a long time, which is hard to be realized in practice. To
obtain the foregrounds in different capture conditions, Song
et al. [182] proposed an interesting way to construct GMS
Dataset. Specifically, they place the same physical model (3D
foreground object) in different lighting conditions to capture
different images and align the foregrounds in different images.
Nevertheless, the collection cost is still very high and the
diversity of foreground is restricted. For indoor scenes, another
solution is using light stage (a large number of individual
lights placed around the scene) to manually control the il-
lumination [144], so that one scene can be quickly switched
to different illumination conditions.


Existing works adopt metrics including Mean Square Error
(MSE), Peak Signal-to-Noise Ratio (PSNR), Structural SIM-
ilarity index (SSIM) [171], Learned Perceptual Image Patch
Similarity (LPIPS) [267] to calculate the distance between
harmonized result and ground-truth. These metrics can also
be calculated only within the foreground region. Besides,
they conduct user study on real composite images by asking
engaged users to select the most realistic images and calculate
the metric (e.g., B-T score [8], ratio).


F. Experiments


We conduct experiments for both standard image harmo-
nization and painterly image harmonization.


For standard image harmonization, we use iHarmony4
[29] dataset (HCOCO, HFlickr, HAdobe5k, and Hday2night),
which is the most commonly used dataset for image har-
monization. All methods are trained on the combination of
training sets from four sub-datasets, and evaluated on the test
set from each sub-dataset. In Fig. 11, we show the harmonized
results of different methods (DoveNet [29], RainNet [122],
iSSAM [181], CDTNet [31], PCTNet [59]). We observe that


15


Fig. 11. The visualization results of different image harmonization methods on iHarmony4 [29] dataset. From left to right in each row, we show the input
composite image, the harmonization results of DoveNet [29], RainNet [122], iSSAM [181], CDTNet [31], PCTNet [59], and the ground-truth harmonized
image.


some competitive methods can generally produce visually
appealing results that are close to the ground-truth images.
However, when the background illumination is very complex
or the composite foreground and background have dramati-
cally divergent illumination statistics, the existing methods are
still struggling to harmonize the foreground to approach the
ground-truth.


For practical usage, in usual lighting conditions, color-to-
color transformation methods like [59] are recommended, be-
cause they can process high-resolution images efficiently and


preserve the image details well. In unusual lighting conditions
(e.g., neon light, high-contrast shadow caused by non-uniform
lighting), diffusion-based methods may perform better. It is
worth noting that among the diffusion-based methods, the
methods (e.g., [15]) adopting latent bridge matching between
source image and target image generate remarkably stable
results.


For painterly image harmonization, we use COCO [121]
and WikiArt [146]. COCO [121] contains instance segmen-
tation annotations for 80 object categories, while WikiArt


16


Fig. 12. The visualization results of different painterly image harmonization methods. From left to right in each row, we show the input composite image,
the composite mask, the harmonization results of SDEdit [140], CDC [63], DIB [262], DPH [138], PHDNet [12], and PHDiffusion [132].


[146] contains digital artistic paintings from different styles.
We create composite images based on these two datasets,
with the photographic objects from COCO and the painterly
backgrounds from WikiArt. In Fig. 12, we show the harmo-
nized results of different methods (SDEdit [140], CDC [63],
DIB [262], DPH [138], PHDNet [12], PHDiffusion [132]).
We split COCO and WikiArt into training set and test set,
based on which all methods are trained and evaluated. It
can be seen that the methods (DPH, PHDNet, PHDiffusion)
specifically designed for painterly image harmonization signif-


icantly outperform the other methods. In the challenging cases,
where the background has dense textures or abstract styles,
PHDiffusion achieves remarkable performance, probably due
to the generative ability of diffusion model and the rich prior
knowledge in foundation model.


For practical usage, in most cases, feed-forward GAN-
based methods like [12] can achieve satisfactory results. In
the challenging cases such as dense textures or abstract style,
feed-forward diffusion-based methods like [132] are able to
demonstrate their strengths.


17


V. SHADOW GENERATION


In the previous section, image harmonization methods could
adjust the foreground appearance to make it compatible with
the background, but they ignore the fact that the inserted
object may also have impact on the background. For example,
if background objects cast shadows on the ground but the
inserted object does not have shadow, the composite image
would look unrealistic. To address this issue, shadow genera-
tion task aims to generate plausible shadow for the foreground
object according to background illumination information to
make the composite image more realistic. Similar to Sec-
tion IV, we divide the existing methods into rendering based
methods and non-rendering based methods.


A. Rendering based Methods


The traditional methods [82, 83, 123, 119] usually use
rendering techniques to generate shadow for the inserted
foreground object, which need to collect or estimate the scene
geometry, foreground object geometry, and scene illumination.
For example, [82] proposed to collect the rough geometry
information and lighting information from users, based on
which rendering techniques could be employed. However, it
is very tedious and sometimes impossible to collect all the
required information. In [83, 123, 119], they attempted to es-
timate the missing information (e.g., scene geometry, lighting
information) automatically. With the recovered information,
the local region to place the inserted 3D object is rendered with
and without the inserted foreground object. The difference
between these two rendered images reveals the impact of fore-
ground object on the background, which is added to the input
composite image to produce the target image with foreground
shadow. Geometry estimation and lighting estimation based
on a single image have been long studied, and many different
technical approaches have been developed [123, 89]. More
recently, some methods [119, 50, 259, 51, 68, 226] endeavored
to estimate illumination condition and scene geometry based
on a single image using deep learning models, which could
achieve better performance than traditional estimation models.
Some works [176, 177] proposed to forecast essential geome-
try information (e.g., pixel height) which cooperates with user-
specified illumination to render realistic shadows.


Despite the remarkable progress they have achieved, it is
still very challenging to accurately estimate the geometry and
lighting information in complex real-world scenes. Erroneous
estimation may mislead the rendering process and produce
terrible results [270].


B. Non-rendering based Methods


Recently, some works treat shadow generation as an image-
to-image translation task, and develop deep networks which
translate input composite image without foreground shadow
to the target image with foreground shadow. For instance,
Zhan et al. [253] used an auto-encoder to predict the shadow
mask with a pretrained illumination model [49, 27] to provide
illumination information. The generated images are pushed to-
wards real images with foreground shadows using adversarial
learning.


Other methods [270, 76, 124, 69, 46] utilized paired training
data (paired images with and without foreground shadow) to
generate better shadow images. ShadowGAN [270] employed
standard conditional GAN with reconstruction loss, local ad-
versarial loss, and global adversarial loss to generate shadow
for the inserted 3D foreground objects. Inoue et al. [76] devel-
oped a multi-task framework with two decoders accounting for
depth map prediction and ambient occlusion map prediction
respectively. ARShadowGAN [124] proposed an attention-
guided residual network. The network predicts two atten-
tion maps for background shadow and occluder respectively,
which are concatenated with composite image and foreground
object mask to produce a residual shadow image. SGRNet
[69] designed a two-stage shadow generation network. In the
first stage, foreground features and background features are
interacted using cross-attention to predict a shadow mask. In
the second stage, they predict shadow parameters which are
used to darken the input composite image. Then, the darkened
image is combined with the input composite image with
shadow matte. Meng et al. [141] adopted a similar two-stage
pipeline and proposed to generate the shadow region by fusing
multiple underexposure images. DMASNet [196] decomposed
shadow mask prediction into box prediction and shape predic-
tion, followed by attending relevant background shadow pixels
to fill in the predicted shadow region. The method in [46]
proposed a 3D-aware shadow generation model by embedding
tri-plane feature representations into a pixel-aligned volume
rendering pipeline. Some other shadow generation methods
are not designed for our task, i.e., generating shadow for
the foreground object in a composite image, but they can
be somehow adapted to our task. Mask-ShadowGAN [71]
explored conducting shadow removal and shadow generation
with unpaired data at the same time, which satisfies cyclic
consistency. The shadow generation branch can be directly
extended to generate foreground shadow. Sheng et al. [175]
designed a shadow generation network to generate soft shadow
for foreground object with user control. They first predict
ambient occlusion map, which is jointly used with user-
provided light map to produce soft shadow mask. When
adapted to our task, an environment light map needs to be
inferred from background before using their network.


SGDiffusion [128] is the first work on shadow generation
using diffusion model, which is built upon ControlNet [264]
with extra intensity module to refine the shadow intensity.
[228, 198, 216, 2] also trained conditional diffusion model for
shadow generation. [280, 250] first predicted coarse shadow
mask and then fed the shadow mask to diffusion model. Zhao
et al. [275] injected geometry prior, i.e., shadow location and
shape, into diffusion model to enhance the quality of generated
shadows with complex shapes. The diffusion-based methods
can generate reasonable shadows for foreground objects in
the composite images with simple scene and illumination
condition, but often fail to generate reasonable shadows for
the composite images with complex scene and illumination
condition. Moreover, the generated shadows have roughly
correct locations and shapes, but lack realistic contours and
details matching the foreground objects.


18


Fig. 13. In the first row, we show two examples from Shadow-AR [124] dataset, which is constructed based on rendered images. In the second row, we show
two examples from DESOBA [69] dataset , which is constructed based on real images. From left to right in each example, we show the composite image
without foreground shadow, the foreground mask, and the ground-truth image with foreground shadow.


C. Datasets and Evaluation Metrics


Similar to image harmonization in Section IV, composite
images without foreground shadows can be easily obtained.
Nonetheless, it is very difficult to obtain paired data, i.e., a
composite image without foreground shadow and a ground-
truth image with foreground shadow, which are required
by supervised deep learning methods on shadow genera-
tion [270, 124, 69]. Some works [270, 124] construct rendered
datasets with paired data by inserting a virtual object into
3D scene and generating shadow for this object with ren-
dering technique. ARShadowGAN [124] released a rendered
dataset named Shadow-AR by inserting a foreground object
into real background image and generating its corresponding
shadow with rendering technique. Shadow-AR dataset contains
3, 000 quintuples, in which each quintuple consists of a
composite image without foreground shadow, its correspond-
ing ground-truth image with foreground shadow, foreground
object mask, background object mask, and background shadow
mask. Shadow-AR dataset only uses 13 foreground objects
from ShapeNet [16] and Stanford 3D scanning repository, so
the diversity of dataset is very limited. Some examples in
Shadow-AR dataset are exhibited in the first row in Fig. 13,
in which we show the composite image without foreground
shadow, foreground object mask, and ground-truth image with
foreground shadow. Similar to ARShadowGAN [124], Shad-
owGAN [270] also adopted rendering technique to construct
a rendered dataset, which uses 9, 265 foreground objects from
ShapeNet [16] and 110 background textures (e.g., woolen,
stone, tablecloth) collected from Internet. Tao et al. [196]
contributed a large-scale rendering dataset called RdSOBA,
which has 788 3D foreground objects and nearly 280,000
object-shadow pairs. In particular, they place a group of 3D
objects in the 3D scene, and get the images without or with
object shadows using rendering techniques.


Although it is feasible to generate paired data using ren-
dering technique, the rendered images have large domain
gap with real images. When applying the model trained on


rendered images to real images, the performances are usually
significantly degraded. To overcome this drawback, Hong
et al. [69] constructed paired data by manually removing
the foreground shadows from real shadow images in SOBA
dataset [214] to produce synthetic composite images without
foreground shadows, leading to DESOBA dataset. This strategy
to create synthetic composite images is similar to the backward
adjustment for constructing image harmonization dataset (see
Section IV). In particular, Hong et al. [69] first remove all
shadows from a shadow image to create a shadow-free image.
Then, one foreground shadow region in the shadow image
is overlaid by the counterpart in its corresponding shadow-
free image, yielding a synthetic composite image with one
missing foreground shadow. DESOBA dataset contains 839
training images with totally 2,995 object-shadow pairs and
160 test images with totally 624 object-shadow pairs. Some
examples in DESOBA dataset are exhibited in the second row
in Fig. 13, in which we show the composite image without
foreground shadow, foreground object mask, and ground-truth
image with foreground shadow. As mentioned in [69], manual
shadow removal is extremely expensive.


To alleviate the burden of manually annotating masks and
removing shadows, [128] design an automatic pipeline to con-
struct shadow generation dataset and contributed a larger-scale
dataset DESOBAv2. Specifically, [128] employ the pretrained
object-shadow detection model [215] to predict object-shadow
masks and employ the off-the-shelf inpainting model [169] to
inpaint the shadow regions. DESOBAv2 has 21,575 images
with 28,573 valid object-shadow pairs.


Instead of constructing synthetic datasets [69, 128] by re-
moving the shadows, [228, 87] constructed real-world dataset
by taking photos with object (factual image) or without object
(counterfactual image). However, this approach to construct
dataset is very costly and labor-intensive.


To evaluate the quality of generated composite images with
foreground shadows, 1) existing shadow generation works
[253] without paired data adopt Frechet Inception Distance


19


Fig. 14.
The visualization results of different shadow generation methods on DESOBA [69] dataset. From left to right in each row, we show the input
composite image, the composite foreground mask, the generated results of ShadowGAN [270], MaskShadowGAN [71], ARShadowGAN [124], SGRNet [69],
SGDiffusion [128], and the ground-truth shadow image.


(FID) [67] and Manipulation Score (MS) [17] to measure
the realism of generated shadow images. 2) For the works
[124, 69] with paired data, they adopt Structural SIMilarity in-
dex (SSIM) [171] and Root Mean Square Error (RMSE) [6] to
measure the difference between generated image and ground-
truth image. SSIM and RMSE can also be calculated only
within the ground-truth foreground shadow region. Liu et al.
[124] also use Balanced Error Rate (BER) [145] to evaluate
the quality of predicted shadow mask based on ground-truth
shadow mask. 3) User study is also called for to ensure that
generated shadows comply with human perception. Partici-
pants are asked to select the most realistic images, based on
which some metrics (e.g., B-T score [8], ratio) are calculated.


D. Experiments


We compare existing shadow generation methods Shadow-
GAN [270], MaskShadowGAN [71], ARShadowGAN [124],
SGRNet [69], and SGDiffusion [128]. All methods are trained
on the training set of DESOBA [69] and DESOBAv2 [128],
and evaluated on the test set of DESOBA. We show the shadow
images generated by different methods in Fig. 14.


It can be seen that most methods [270, 71, 124] are strug-
gling to produce reasonable shadow for the foreground object,
or even produce no shadow at all, which implies that shadow
generation for the inserted foreground object is a very tough
task. SGRNet [69] achieves relatively compelling results, but
the shapes of generated shadows are often unrealistic. Besides,


20


we observe that SGRNet tends to overfit the artifacts caused
by manual shadow removal in DESOBA training set, leading
to the results perfectly matching the ground-truth (e.g., row
6, 7). SGDiffusion [128] obtains the most competitive results
by resorting to the foundation diffusion model, even for the
foreground objects (e.g., row 1, 4) with complicated shapes,
and demonstrates remarkable generalization ability.


For practical usage, foundation diffusion model (e.g.,
SD [169], FLUX [1]) is imperative to generate realistic shad-
ows. More advanced foundation models usually lead to better
performance, especially in the challenging cases.


VI. REFLECTION GENERATION


Besides shadow, reflection is another impact that the fore-
ground object may cast on the background, especially when
the foreground object is above the water or on the desktop with
reflective material. To address this issue, reflection generation
task aims to generate plausible reflection for the foreground
object to make the composite image more realistic. Similar
to Section V, we divide the existing methods into rendering
based methods and non-rendering based methods. ’


A. Rendering based Methods


Ma et al. [139] first estimated the lighting information and
then employed a renderer to generate coarse reflection, which
is further refined using neural network.


B. Non-rendering based Methods


Some works treat reflection generation as image-to-image
translation task without estimating lighting/geometry informa-
tion or employing renderer. For example, the works [228, 198]
employed conditional diffusion model to synthesize reflec-
tion for the inserted foreground object. The works [35, 36]
adopted similar approaches but focused on mirror reflection.
RGDiffusion [276] extended ControlNet [264] considering
the property of reflection generation task. Specifically, they
inject the cropped foreground into denoising UNet via cross-
attention, considering that reflections are usually the horizontal
or vertical mirror images of foreground objects.


C. Datasets and Evaluation Metrics


Training conditional diffusion model for reflection synthesis
requires paired training data, i.e., a composite image without
foreground reflection and a ground-truth image with fore-
ground reflection.


Some works [35, 36] constructed rendered datasets with
paired data by inserting a virtual object into 3D scene and
generating reflection in the mirror with rendering technique.
For example, Dhiman et al. [35] released SynMirror dataset
with 66,068 objects and 198,204 rendered images.


Different from rendering pipeline and similar to the pipeline
of constructing shadow generation dataset DESOBAv2 [128],
DEROBA [276] manually annotated object-reflection masks
and employed the off-the-shelf inpainting model to inpaint the
reflection regions, resulting in synthesized composite images.
Some examples in DEROBA dataset are exhibited in Fig. 15,


in which we show the composite image without foreground
reflection, foreground object mask, and ground-truth image
with foreground reflection.


Instead of constructing synthetic datasets [35, 36], some
other works [228, 87] constructed real-world dataset by taking
photos with object (factual image) or without object (counter-
factual image). However, this approach to construct dataset is
very costly and labor-intensive.


To evaluate the quality of generated composite images
with foreground reflections, Mean Squared Error (MSE), Peak
Signal-to-Noise Ratio (PSNR), Structural SIMilarity index
(SSIM) [171], Learned Perceptual Image Patch Similarity
(LPIPS) [267] can be adopted to measure the difference
between generated image and ground-truth image. User study
is also necessary to ensure that generated reflections conform
to human perception. Participants are asked to select the most
realistic images, based on which some metrics (e.g., B-T score
[8], ratio) are calculated.


D. Experiments


We compare different methods [264, 276] on DER-
OBA [276] dataset. As shown in Fig. 16, RGDiffusion [276]
produces more accurate shapes and clearer details compared
with ControlNet [264].


For practical usage, the methods built upon foundation dif-
fusion model (e.g., SD [169], FLUX [1]) can usually produce
satisfactory results.


VII. GENERATIVE COMPOSITION


As the diffusion models [169] pretrained on large-scale
dataset [172] become popular in various image generation and
editing tasks, generative image composition (object composit-
ing) has attracted growing research interest. In contrast with
previous methods which perform one or multiple sub-tasks
sequentially, generative image composition is a combinatorial
task which performs multiple sub-tasks (e.g., image blending,
image harmonization, shadow generation) in parallel through
one unified model. Given a foreground, a background, and a
bounding box indicating the foreground placement, generative
image composition aims to directly produce a realistic com-
posite image with the foreground naturally and harmoniously
merged into the background.


Generative image composition has certain overlap with
object-guided image inpainting [242] and image customization
[251]. Their differences are claimed as follows. 1) Object-
guided image inpainting needs a mask to indicate the inpainted
region, where the mask shape usually implies the target
shape of inserted object. When the inpainted region is a
bounding box free of shape information, object-guided image
inpainting is closer to generative image composition. However,
strictly speaking, generative image composition expects to
preserve the non-foreground pixels in the bounding box, which
is different from object-guided image inpainting. Moreover,
generative image composition aims to generate shadow and
reflection for the foreground object without box or shape
constraint, which is also different from object-guided image
inpainting. 2) Image customization is a very broad concept,


21


Fig. 15.
We show four examples from DEROBA [276] dataset. From left to right in each example, we show the composite image without foreground
reflection, the foreground mask, and the ground-truth image with foreground reflection.


Fig. 16. The visualization results of different reflection generation methods on DEROBA [276] dataset. From left to right in each group, we show the input
composite image, the composite foreground mask, the generated results of ControlNet [264], RGDiffusion [276], and the ground-truth reflection image.


which includes changing attributes and adding background
for a specific object. Generative image composition can be
deemed as a special case of image customization.


A. Deep Learning Methods


The existing generative image composition methods can be
divided into two groups: training-free methods and training-
based methods.


1) Training-free Methods:
The first group of methods
[63, 134, 221, 107, 239, 135] utilizes off-the-shelf foundation
generation model, which does not require training or finetun-
ing. They aim to generate high-quality composite images by
manipulating the foreground and background elements (e.g.,
feature, attention) through the denoising process.


2) Training-based Methods: The second group of methods
[242, 184, 272, 255, 22, 251, 25, 109, 133, 195, 274, 228, 266,


243, 115] require training or finetuning. They can be further di-
vided into two subgroups, according to whether object-specific
finetuning is indispensable. The first subgroup of methods
[242, 184, 272, 255, 251, 25, 206] train a diffusion model on
abundant pairs of foregrounds and backgrounds, so that it can
be directly applied to a new pair of foreground and background
at test time. These models need to take one or more reference
images of the inserted foreground object as input. In the testing
period, if a few images containing the foreground object are
available, we can optionally finetune the pretrained model
on these images and may achieve better performance. The
second subgroup of methods [26, 133, 109, 170] do not train
the model on large-scale dataset. Most of them associate the
target object with one rare token, so object-specific finetuning
(training on a few images of the same foreground object) is
indispensable for these methods. Because the first subgroup


22


Fig. 17.
The visualization results of different generative composition methods on MureCom [133] dataset. From left to right in each row, we show
the background with foreground bounding box, five reference images of the same foreground object, the generated results of ObjectStitch [184],
InsertAnything [183], OSInsert [80], Banana pro [199], and Seedream 5.0.


is dominant, we will mainly introduce the first subgroup of
methods.


Among the first subgroup of training-based methods, the
pioneering works like PbE [242] and ObjectStitch [184] con-
struct massive training triplets of foregrounds, backgrounds,
and ground-truth real images based on large-scale image
datasets [91], in which the foregrounds are cropped from
real images followed by color and geometry perturbation.
Then, they adapt conditional diffusion model to this task. In
particular, the background image, bounding box mask, and
noisy image are concatenated as input, while the foreground
is injected into the network via cross-attention. Kulal et al. [90]
adopted a similar approach, but focused on human generation.
Some subsequent methods focus on enhancing the ability of


detail preservation. For example, Zhang et al. [255] proposed
global-and-local fusion, in which shallow foreground features
are used to enhance the details. Chen et al. [25] extracted
high-frequency information for better detail preservation. Yu
et al. [249] designed a cycle formed by adding object and
removing object, which is expected to facilitate each other.
Recently, inspired by in-context learning, several recent works
[211, 183, 74] explored image composition task under the
framework of in-context learning. Specifically, noisy latent,
background, foreground are equally fed into diffusion model
and interact with each other. Different types of input are added
with different levels of noise. In-context learning methods
demonstrate clear advantage in preserving the subtle fore-
ground details, but they exhibit noticeable copy-and-paste


23


effect and lag in viewpoint/pose adjustment. [80] is a com-
bination of [184] and [183], that is, using [184] to generate
foreground mask and [183] to fill in the foreground mask.
Therefore, [80] can accomplish both detail preservation and
viewpoint/pose adjustment.


Different works [255, 251] also attempted to control image
composition from different perspectives. For example, [251]
provided the target camera viewpoint of foreground object.
[255] can selectively adjust the illumination and pose of
foreground object to match the background. Some methods
[66, 106, 278] aimed to insert the object into any reasonable
place in the background image without the provided bounding
box. Some methods [278, 229] explored generating plausible
shadow and reflection for the inserted foreground without the
spatial constraint of bounding box.


B. Datasets and Evaluation Metrics


Training diffusion model requires massive training triplets
of foregrounds, backgrounds, and ground-truth real images.
Previous works [242, 184] proposed to crop the foregrounds
from real images and perturb the foregrounds (e.g., color trans-
fer, geometric transformation), so that we can have perturbed
foreground, masked background, and ground-truth real image.
The multi-view datasets and video datasets can also be used
to simulate more diverse and realistic geometry perturbation.
In particular, they replace the perturbed foreground with the
foreground image from another viewpoint or another video
frame.


Another way to construct image composition dataset is
capturing two images with or without the foreground object
for the same scene [229, 87]. Specifically, they first capture an
image for the background scene. Then, they place a foreground
object and capture an image with the same camera viewpoint
again. However, the scale of such datasets is limited by the
high cost of image collection.


In real-world application scenarios, there exist no ground-
truth images for a pair of foreground and background, so we
cannot calculate the distance between generated image and
ground-truth image. Therefore, previous works [242, 184, 272]
used FID [67] to measure the distribution discrepancy between
generated images and real images. Quality metrics [58, 225]
are used to evaluate the authenticity of each image. CLIP score
[164] or DINO score [14] are used to measure the similarity
between generated foreground and reference foreground. User
study should also be conducted to evaluate different aspects
for the generated images.


C. Experiments


We evaluate different methods ObjectStitch [184], Inser-
tAnything [183], OSInsert [80], Banana pro [199], and See-
dream 5.0 on MureCom [133] dataset. The visualization results
are shown in Fig. 17.


From Fig. 17, we can see that [184] can generate foreground
object with reasonable viewpoint/pose but fails to preserve
the appearance details. [183] can preserve the appearance
details, but weak in adjusting the foreground viewpoint/pose to
match the background when the viewpoint/pose of foreground


Fig. 18. Illustration of foreground object search. Given a background image
with query bounding box (yellow), foreground object search aims to find
compatible foreground objects of a specified category from a library, which
is combined with the background to produce a realistic composite image.


reference image is not compatible with the background. [80]
combines the advantages of [184] and [183], accomplishing
both detail preservation and viewpoint/pose adjustment.


Banana pro and Seedream 5.0 are very competitive com-
mercial models with plausible foreground viewpoint/pose and
faithful foreground details, but they have two practical flaws.
On the one hand, the generated foregrounds are not well
aligned with the provided bounding boxes. Specifically, the
inserted objects are often slightly offset, scaled improperly, or
partially out of the designated bounding box region. On the
other hand, the original background’s color tone and luminance
present slight yet discernible alterations in the generated
composite images, which disrupts the visual consistency and
integrity of the background scene.


VIII. FOREGROUND OBJECT SEARCH


The goal of foreground object search (FOS) is to retrieve
suitable foreground objects from a foreground library, which
are compatible with the background in terms of illumination,
geometry, and semantics. The FOS task is illustrated in Fig. 18.
Finding compatible foreground objects can significantly re-
duce the effort required to create realistic composite images,
complementing other image composition techniques. FOS task
can be divided into constrained or unconstrained depending on
whether the foreground category is specified.


A. Traditional Methods


Early works [95, 24] attempted to match each foreground
with the background using hand-crafted features, but their
performance is limited by the expressiveness of hand-crafted
features. Specifically, Lalonde et al. [95] estimated the object
information (e.g., size, orientation, lighting condition) and
designed matching criteria to rank all the objects in the library.
Chen et al. [24] exploited the contour consistency and content
consistency between foreground and background based on
hand-crafted features.


24


Fig. 19.
The visualization results of different foreground object search methods CFO [277], UFO [278], GALA [286], FFR [233], DiscoFOS [257] on
S-FOSD [257] (top) and R-FOSD [257] (bottom) datasets. On R-FOSD test set, green (resp., red) box is used to indicate the foreground with compatible
(resp., incompatible) label.


B. Deep Learning Methods


Recent work used deep learning features for foreground
retrieval. For example, Tan et al. [189] utilized deep features
to capture local context particularly for person compositing.
Zhu et al. [285] trained a composite image discriminator
to predict the realism of composites by compositing each
foreground with the background. This method is effective
in using the realism of composite images to measure the
foreground-background compatibility, but computing the re-
alism of all composite images is very expensive. More recent
methods [277, 278, 286, 233, 99, 257] typically trained two
encoders to extract foreground feature and background feature.
Then, the foreground-background compatibility is measured
by calculating the distance between foreground feature and
background feature. They share a similar framework, despite
the difference in data preparation, network structure, and
loss design. Zhang et al. [257] observed that a composite
image discriminator [285] can perform much better than two
encoders, so they developed a teacher-student network which
distills composite image feature from the discriminator to
the interaction output of foreground feature and background
feature.


As introduced in Section I, the foreground and background
in a composite image have multiple types of inconsistencies.
The existing FOS works considered different sets of inconsis-
tencies between background and foreground. For example, the
methods [277, 278] considered the semantic consistency. The
methods [99, 257] considered the geometric consistency and


semantic consistency. Besides the geometric and semantic con-
sistency, some other methods [233, 286] additionally consid-
ered style consistency [233] or illumination consistency [286].


C. Datasets and Evaluation Metrics


Early FOS studies [277, 278, 233, 286] did not release
their datasets. Zhang et al. [257] contributed two datasets:
S-FOSD and R-FOSD, which contain synthetic composite
images and real composite images respectively. In S-FOSD
dataset, Zhang et al. [257] segment one foreground object
from a real image and fill its bounding box with image mean
values to get the background. For each background image, the
foreground object from the same image is deemed as ground-
truth. In R-FOSD dataset, Zhang et al. [257] collect images
from Internet as background images and draw a bounding box
at the expected foreground location as query bounding box. R-
FOSD dataset uses the same foregrounds with the test set of
S-FOSD dataset. Zhang et al. [257] employ human annotators
to label the compatibility of each pair of background and
foreground. In comparison, S-FOSD dataset is low-cost and
highly scalable, but does not contain complete background
images or ground-truth negative samples. R-FOSD dataset has
complete background image with accurately annotated positive
and negative foregrounds, but is unscalable due to the high
annotation cost.


On the synthetic composite image dataset, Recall@k (R@k)
is adopted as an evaluation metric [277, 286, 257], which rep-
resents the percentage of background queries whose ground-


25


truth foreground appears in top k retrievals. On the real
composite image dataset, mean Average Precision (mAP),
mAP@20, and Precision@k (P@k) are adopted as an eval-
uation metrics [278, 286, 257].


D. Experiments


We evaluate different methods on S-FOSD dataset and R-
FOSD dataset [257]. Specifically, we train on S-FOSD training
set, while testing on S-FOSD and R-FOSD test sets. The
retrieval results of CFO [277], UFO [278], GALA [286],
FFR [233], and DiscoFOS [257] are shown in Fig. 19. In each
example, we show the background image with query bounding
box (gray square or yellow box) on the left side and top five
retrieved results of different methods on the right side. The
results show that DiscoFOS can retrieve more foregrounds
that are compatible with the background geometrically and
semantically.


IX. CONCLUSION


In this paper, we have conducted a comprehensive survey on
image composition, which involves a variety of techniques to
produce a realistic composite image. We have introduced ob-
ject placement, image blending, image harmonization, shadow
generation, generative image composition, and foreground
object search. In the future, we will extend this survey to
broader composition tasks in related fields, such as video
composition and 3D/4D composition.


REFERENCES


[1] Black forest labs. flux. https://github.com/ black-forest-


labs/flux, 2024.
[2] Waqas Ahmed, Dean Diepeveen, and Ferdous Sohel.


Coshadow: Multi-object shadow generation for im-
age compositing via diffusion model.
arXiv preprint
arXiv:2603.02743, 2026.
[3] Evline J Alappatt and Vince Paul. A survey on color


transfer methods.
International Journal of Science,
Engineering and Computer Technology, 6(1):70, 2016.
[4] Samaneh Azadi, Deepak Pathak, Sayna Ebrahimi, and


Trevor Darrell. Compositional GAN: Learning image-
conditional binary composition. International Journal
of Computer Vision, 128(10):2570–2585, 2020.
[5] Zhongyun Bao, Chengjiang Long, Gang Fu, Daquan


Liu, Yuanzhen Li, Jiaming Wu, and Chunxia Xiao.
Deep image-based illumination harmonization.
In
CVPR, 2022.
[6] Jonathan T Barron and Jitendra Malik. Shape, illumina-


tion, and reflectance from shading. IEEE Transactions
on Pattern Analysis and Machine Intelligence, 37(8):
1670–1687, 2014.
[7] Anand Bhattad and David A Forsyth.
Cut-and-paste
object insertion by enabling deep image prior for re-
shading. In 3DV, 2022.
[8] Ralph Allan Bradley and Milton E Terry. Rank analysis


of incomplete block designs: I. the method of paired
comparisons. Biometrika, 39(3/4):324–345, 1952.


[9] Peter J Burt and Edward H Adelson. A multiresolu-


tion spline with application to image mosaics.
ACM
Transactions on Graphics, 2(4):217–236, 1983.
[10] Vladimir Bychkovsky, Sylvain Paris, Eric Chan, and


Fr´edo Durand.
Learning photographic global tonal
adjustment with a database of input / output image pairs.
In CVPR, 2011.
[11] Junyan Cao, Wenyan Cong, Li Niu, Jianfu Zhang, and


Liqing Zhang. Deep image harmonization by bridging
the reality gap. In BMVC, 2022.
[12] Junyan Cao, Yan Hong, and Li Niu. Painterly image


harmonization in dual domains. In AAAI, 2023.
[13] Chris Careaga, S Mahdi H Miangoleh, and Ya˘gız Ak-


soy.
Intrinsic harmonization for illumination-aware
compositing. In ACM SIGGRAPH Asia, 2023.
[14] Mathilde Caron, Hugo Touvron, Ishan Misra, Herv´e


J´egou, Julien Mairal, Piotr Bojanowski, and Armand
Joulin.
Emerging properties in self-supervised vision
transformers. In ICCV, 2021.
[15] Cl´ement Chadebec, Onur Tasar, Sanjeev Sreetharan, and


Benjamin Aubin. Lbm: Latent bridge matching for fast
image-to-image translation. In ICCV, 2025.
[16] Angel X Chang, Thomas Funkhouser, Leonidas Guibas,


Pat Hanrahan, Qixing Huang, Zimo Li, Silvio Savarese,
Manolis Savva, Shuran Song, Hao Su, et al. ShapeNet:
An information-rich 3D model repository.
arXiv
preprint arXiv: 1512.03012, 2015.
[17] Bor-Chun Chen and Andrew Kae.
Toward realistic
image compositing with adversarial learning. In CVPR,
2019.
[18] Haoxing Chen, Zhangxuan Gu, Yaohui Li, Jun Lan,


Changhua Meng, Weiqiang Wang, and Huaxiong Li.
Hierarchical dynamic image harmonization.
In ACM
MM, 2023.
[19] Haoxing Chen, Yaohui Li, Zhangxuan Gu, Zhuoer Xu,


Jun Lan, and Huaxiong Li. Segment anything model
meets image harmonization. In ICASSP, 2024.
[20] Jianqi Chen, Yilan Zhang, Zhengxia Zou, Keyan Chen,


and Zhenwei Shi. Dense pixel-to-pixel harmonization
via continuous image representation. IEEE Transactions
on Circuits and Systems for Video Technology, 34(5):
3876–3890, 2023.
[21] Jianqi Chen, Yilan Zhang, Zhengxia Zou, Keyan Chen,


and Zhenwei Shi.
Zero-shot image harmonization
with generative model prior.
IEEE Transactions on
Multimedia, 2025.
[22] Jiaxuan Chen, Bo Zhang, Qingdong He, Jinlong Peng,


and Li Niu. Generative image composition with cali-
brated reference features. In AAAI, 2026.
[23] Shenghao Chen, Chunjie Ma, Yibo Zhao, Meng Liu,


Yanbing Xue, and Zan Gao.
A novel multi-view
perception and shrinkage aggregation network for in-
harmonious region localization. IEEE Transactions on
Circuits and Systems for Video Technology, 2025.
[24] Tao Chen, Ming-Ming Cheng, Ping Tan, Ariel Shamir,


and Shimin Hu. Sketch2Photo: internet image montage.
In ACM SIGGRAPH Asia, 2009.
[25] Xi Chen, Lianghua Huang, Yu Liu, Yujun Shen, Deli


26


Zhao, and Hengshuang Zhao.
Anydoor: Zero-shot
object-level image customization. In CVPR, 2024.
[26] Zhekai Chen, Wen Wang, Zhen Yang, Zeqing Yuan, Hao


Chen, and Chunhua Shen. Freecompose: Generic zero-
shot image composition with diffusion prior. In ECCV,
2024.
[27] Dachuan Cheng, Jian Shi, Yanyun Chen, Xiaoming


Deng, and Xiaopeng Zhang.
Learning scene illumi-
nation by pairwise photos from rear and front mobile
cameras.
Computer Graphics Forum, 37(7):213–221,
2018.
[28] Xianhe Cheng, Peng Zhai, Dingkang Yang, Xiangrui


Meng, Yang Xia, and Lihua Zhang.
Diverse object
placement with dual interaction. Neurocomputing, page
131161, 2025.
[29] Wenyan Cong, Jianfu Zhang, Li Niu, Liu Liu, Zhixin


Ling, Weiyuan Li, and Liqing Zhang. DoveNet: Deep
image harmonization via domain verification. In CVPR,
2020.
[30] Wenyan Cong, Li Niu, Jianfu Zhang, Jing Liang, and


Liqing Zhang. BargainNet: Background-guided domain
translation for image harmonization. In ICME, 2021.
[31] Wenyan Cong, Xinhao Tao, Li Niu, Jing Liang,


Xuesong Gao, Qihao Sun, and Liqing Zhang.
High-
resolution image harmonization via collaborative dual
transformations. In CVPR, 2022.
[32] Marius Cordts, Mohamed Omran, Sebastian Ramos


an Timo Rehfeld, Markus Enzweiler, Rodrigo Benen-
son, Uwe Franke, Stefan Roth, and Bernt Schiele. The
cityscapes dataset for semantic urban scene understand-
ing. In CVPR, 2016.
[33] Xiaodong Cun and Chi-Man Pun. Improving the har-


mony of the composite image by spatial-separated atten-
tion module. IEEE Transactions on Image Processing,
29:4759–4771, 2020.
[34] Yutong Dai, Brian Price, He Zhang, and Chunhua Shen.


Boosting robustness of image matting with context
assembling and strong data augmentation.
In CVPR,
2022.
[35] Ankit Dhiman, Manan Shah, Rishubh Parihar, Yash


Bhalgat, Lokesh R Boregowda, and R Venkatesh Babu.
Reflecting reality: Enabling diffusion models to produce
faithful mirror reflections. In 3DV, 2024.
[36] Ankit Dhiman, Manan Shah, and R Venkatesh Babu.


Mirrorverse: Pushing diffusion models to realistically
reflect the world. In CVPR, 2025.
[37] Nikita Dvornik, Julien Mairal, and Cordelia Schmid.


Modeling visual context is key to augmenting object
detection datasets. In ECCV, 2018.
[38] Nikita Dvornik, Julien Mairal, and Cordelia Schmid. On


the importance of visual context for data augmentation
in scene understanding. IEEE Transactions on Pattern
Analysis and Machine Intelligence, 43(6):2014–2028,
2019.
[39] Debidatta Dwibedi, Ishan Misra, and Martial Hebert.


Cut, paste and learn: Surprisingly easy synthesis for
instance detection. In ICCV, 2017.
[40] Majed El Helou, Ruofan Zhou, Johan Barthas, and


Sabine S¨usstrunk.
VIDIT: Virtual image dataset for
illumination transfer. arXiv preprint arXiv:2005.05460,
2020.
[41] Mark Everingham, Luc Van Gool, Christopher K. I.


Williams, John M. Winn, and Andrew Zisserman. The
pascal visual object classes (VOC) challenge.
Inter-
national Journal of Computer Vision, 88(2):303–338,
2010.
[42] Haoshu Fang, Jianhua Sun, Runzhong Wang, Minghao


Gou, Yonglu Li, and Cewu Lu. InstaBoost: Boosting
instance segmentation via probability map guided copy-
pasting. In ICCV, 2019.
[43] Hasan Sheikh Faridul, Tania Pouli, Christel Chamaret,


J¨urgen Stauder, Alain Tr´emeau, Erik Reinhard, et al.
A survey of color mapping and its applications. Euro-
graphics (State of the Art Reports), 3(2):1, 2014.
[44] Raanan Fattal, Dani Lischinski, and Michael Werman.


Gradient domain high dynamic range compression. In
ACM Siggraph Computer Graphics, 2002.
[45] Ulrich Fecker, Marcus Barkowsky, and Andr´e Kaup.


Histogram-based prefiltering for luminance and chromi-
nance compensation of multiview video. IEEE Trans-
actions on Circuits and Systems for Video Technology,
18(9):1258–1267, 2008.
[46] Yanping Fu, Jiazheng Tao, Chenpei Li, Shaojie Zhang,


Dengdi Sun, and Haifeng Zhao.
3d-aware shadow
generation for composite image. In ICASSP, 2026.
[47] Yu Fu and Yuezhen Hu. A survey on image matting


methods based on deep learning.
Frontiers in Eco-
nomics and Management, 3(3):497–502, 2022.
[48] Bingjie Gao, Bo Zhang, and Li Niu. Object placement


for anything. In ICME, 2025.
[49] Marc-Andr´e Gardner, Kalyan Sunkavalli, Ersin Yumer,


Xiaohui Shen, Emiliano Gambaretto, Christian Gagn´e,
and Jean-Franc¸ois Lalonde. Learning to predict indoor
illumination from a single image. ACM Transactions
on Graphics, 36(6):1–14, 2017.
[50] Marc-Andr´e Gardner, Yannick Hold-Geoffroy, Kalyan


Sunkavalli,
Christian
Gagn´e,
and
Jean-Francois
Lalonde. Deep parametric indoor lighting estimation.
In ICCV, 2019.
[51] Mathieu
Garon,
Kalyan
Sunkavalli,
Sunil
Hadap,
Nathan Carr, and Jean-Franc¸ois Lalonde. Fast spatially-
varying indoor lighting estimation. In CVPR, 2019.
[52] Leon A Gatys, Alexander S Ecker, and Matthias Bethge.


A neural algorithm of artistic style.
arXiv preprint
arXiv:1508.06576, 2015.
[53] Georgios
Georgakis,
Md.
Alimoor
Reza,
Arsalan
Mousavian, Phi-Hung Le, and Jana Kosecka. Multiview
RGB-D dataset for object instance detection. In 3DV,
2016.
[54] Georgios Georgakis, Arsalan Mousavian, Alexander C.


Berg, and Jana Kosecka. Synthesizing training data for
object detection in indoor scenes. In RSS XIII, 2017.
[55] Golnaz Ghiasi, Yin Cui, Aravind Srinivas, Rui Qian,


Tsung-Yi Lin, Ekin D. Cubuk, Quoc V. Le, and Barret
Zoph. Simple copy-paste is a strong data augmentation
method for instance segmentation. In CVPR, 2021.


27


[56] Amr Ghoneim, Jiju Poovvancheri, Yasushi Akiyama,


and Dong Chen. Depgan: Leveraging depth maps for
handling occlusions and transparency in image compo-
sition. arXiv preprint arXiv:2407.11890, 2024.
[57] Junhong Gou, Bo Zhang, Li Niu, Jianfu Zhang, Jianlou


Si, Chen Qian, and Liqing Zhang.
Virtual acces-
sory try-on via keypoint hallucination. arXiv preprint
arXiv:2310.17131, 2023.
[58] Shuyang Gu, Jianmin Bao, Dong Chen, and Fang Wen.


GIQA: Generated image quality assessment. In ECCV,
2020.
[59] Julian Jorge Andrade Guerreiro, Mitsuru Nakazawa,


and Bj¨orn Stenger.
PCT-Net: Full resolution image
harmonization using pixel-wise color transformations.
In CVPR, 2023.
[60] Zonghui
Guo,
Dongsheng
Guo,
Haiyong
Zheng,
Zhaorui Gu, Bing Zheng, and Junyu Dong.
Image
harmonization with transformer. In ICCV, 2021.
[61] Zonghui Guo, Haiyong Zheng, Yufeng Jiang, Zhaorui


Gu, and Bing Zheng. Intrinsic image harmonization. In
CVPR, 2021.
[62] Zonghui Guo, Zhaorui Gu, Bing Zheng, Junyu Dong,


and Haiyong Zheng. Transformer for image harmoniza-
tion and beyond. IEEE Transactions on Pattern Analysis
and Machine Intelligence, 2022.
[63] Roy Hachnochi, Mingrui Zhao, Nadav Orzech, Ri-


non Gal, Ali Mahdavi-Amiri, Daniel Cohen-Or, and
Amit Haim Bermano.
Cross-domain compositing
with pretrained diffusion models.
arXiv preprint
arXiv:2302.10167, 2023.
[64] Yucheng Hang, Bin Xia, Wenming Yang, and Qingmin


Liao. SCS-Co: Self-consistent style contrastive learning
for image harmonization. In CVPR, 2022.
[65] Guoqing Hao, Satoshi Iizuka, and Kazuhiro Fukui.


Image harmonization with attention-based deep feature
modulation. In BMVC, 2020.
[66] Jixuan He, Wanhua Li, Ye Liu, Junsik Kim, Donglai


Wei, and Hanspeter Pfister.
Affordance-aware object
insertion via mask-aware dual diffusion. arXiv preprint
arXiv:2412.14462, 2024.
[67] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner,


Bernhard Nessler, and Sepp Hochreiter. GANs trained
by a two time-scale update rule converge to a local nash
equilibrium. In NeurIPS, 2017.
[68] Yannick Hold-Geoffroy, Akshaya Athawale, and Jean-


Franc¸ois Lalonde. Deep sky modeling for single image
outdoor lighting estimation. In CVPR, 2019.
[69] Yan Hong, Li Niu, Jianfu Zhang, and Liqing Zhang.


Shadow generation for composite image in real-world
scenes. In AAAI, 2022.
[70] Qibin Hou, Ming-Ming Cheng, Xiaowei Hu, Ali Borji,


Zhuowen Tu, and Philip HS Torr. Deeply supervised
salient object detection with short connections.
In
CVPR, 2017.
[71] Xiaowei Hu, Yitong Jiang, Chi-Wing Fu, and Pheng-


Ann Heng.
Mask-ShadowGAN: Learning to remove
shadows from unpaired data. In ICCV, 2019.
[72] Zhongyun Hu, Jiahao Li, Xue Wang, and Qing Wang.


Spatially-varying illumination-aware indoor harmoniza-
tion. International Journal of Computer Vision, pages
1–20, 2024.
[73] Zhongyun Hu, Ntumba Elie Nsampi, Xue Wang, and


Qing Wang.
SIDNet: Learning shading-aware illu-
mination descriptor for image harmonization.
IEEE
Transactions on Emerging Topics in Computational
Intelligence, 2024.
[74] Junjia Huang, Pengxiang Yan, Jiyang Liu, Jie Wu,


Zhao Wang, Yitong Wang, Liang Lin, and Guanbin
Li. Dreamfuse: Adaptive image fusion with diffusion
transformer. In ICCV, 2025.
[75] Xun Huang and Serge Belongie. Arbitrary style transfer


in real-time with adaptive instance normalization.
In
ICCV, 2017.
[76] Naoto Inoue, Daichi Ito, Yannick Hold-Geoffroy, Long


Mai, Brian Price, and Toshihiko Yamasaki. RGB2ao:
Ambient occlusion generation from RGB images. Com-
puter Graphics Forum, 39(2):451–462, 2020.
[77] Max Jaderberg, Karen Simonyan, Andrew Zisserman,


and Koray Kavukcuoglu. Spatial transformer networks.
In NeurIPS, 2015.
[78] Jiaya Jia, Jian Sun, Chi-Keung Tang, and Heung-Yeung


Shum. Drag-and-drop pasting. ACM Transactions on
graphics, 25(3):631–637, 2006.
[79] Yifan Jiang, He Zhang, Jianming Zhang, Yilin Wang,


Zhe Lin, Kalyan Sunkavalli, Simon Chen, Sohrab
Amirghodsi, Sarah Kong, and Zhangyang Wang. SSH:
A self-supervised framework for image harmonization.
In ICCV, 2021.
[80] Li Niu Jingyuan Wang. Osinsert. https://github.com/


bcmi/OSInsert-Image-Composition, 2026.
[81] Liuxue Ju, Chengdao Pu, Fang Gao, and Jun Yu.


Adaptive fine-grained region matching for image har-
monization. In ICIG, 2023.
[82] Kevin Karsch, Varsha Hedau, David Forsyth, and Derek


Hoiem. Rendering synthetic objects into legacy pho-
tographs. ACM Transactions on Graphics, 30(6):1–12,
2011.
[83] Kevin Karsch, Kalyan Sunkavalli, Sunil Hadap, Nathan


Carr, Hailin Jin, Rafael Fonte, Michael Sittig, and David
Forsyth.
Automatic scene inference for 3d object
compositing.
ACM Transactions on Graphics, 33(3):
1–15, 2014.
[84] Michael Kazhdan and Hugues Hoppe. Streaming multi-


grid for gradient-domain operations on large images.
ACM Transactions on graphics, 27(3):1–10, 2008.
[85] Zhanghan Ke, Chunyi Sun, Lei Zhu, Ke Xu, and Ryn-


son W.H. Lau. Harmonizer: Learning to perform white-
box image and video harmonization. In ECCV, 2022.
[86] Kotaro Kikuchi, Kota Yamaguchi, Edgar Simo-Serra,


and Tetsunori Kobayashi. Regularized adversarial train-
ing for single-shot virtual try-on. In ICCV Workshop,
2019.
[87] Jinwoo Kim, Sangmin Han, Jinho Jeong, Jiwoo Choi,


Dongyeoung Kim, and Seon Joo Kim. ORIDa: Object-
centric real-world image composition dataset. In CVPR,
2025.


28


[88] Ron Kimmel, Michael Elad, Doron Shaked, Renato


Keshet, and Irwin Sobel. A variational framework for
retinex. International Journal of Computer Vision, 52
(1):7–23, 2003.
[89] Joel Kronander, Francesco Banterle, Andrew Gardner,


Ehsan Miandji, and Jonas Unger. Photorealistic render-
ing of mixed reality scenes. Computer Graphics Forum,
34(2):643–665, 2015.
[90] Sumith Kulal, Tim Brooks, Alex Aiken, Jiajun Wu,


Jimei Yang, Jingwan Lu, Alexei A. Efros, and Kr-
ishna Kumar Singh.
Putting people in their place:
Affordance-aware human insertion into scenes.
In
CVPR, 2023.
[91] Alina Kuznetsova, Hassan Rom, Neil Gordon Alldrin,


Jasper R. R. Uijlings, Ivan Krasin, Jordi Pont-Tuset,
Shahab Kamali, Stefan Popov, Matteo Malloci, Alexan-
der Kolesnikov, Tom Duerig, and Vittorio Ferrari. The
open images dataset v4.
International Journal of
Computer Vision, 128:1956–1981, 2020.
[92] Black Forest Labs, Stephen Batifol, Andreas Blattmann,


Frederic Boesel, Saksham Consul, Cyril Diagne, Tim
Dockhorn, Jack English, Zion English, Patrick Esser,
et al.
Flux. 1 kontext: Flow matching for in-context
image generation and editing in latent space.
arXiv
preprint arXiv:2506.15742, 2025.
[93] Pierre-Yves Laffont, Zhile Ren, Xiaofeng Tao, Chao


Qian, and James Hays. Transient attributes for high-
level understanding and editing of outdoor scenes. ACM
Transactions on graphics, 33(4):1–11, 2014.
[94] Jean-Franc¸ois Lalonde and Alexei A. Efros. Using color


compatibility for assessing image realism.
In ICCV,
2007.
[95] Jean-Franc¸ois Lalonde, Derek Hoiem, Alexei A. Efros,


Carsten Rother, John M. Winn, and Antonio Criminisi.
Photo clip art. In ACM SIGGRAPH, 2007.
[96] Donghoon Lee, Sifei Liu, Jinwei Gu, Ming-Yu Liu,


Ming-Hsuan Yang, and Jan Kautz. Context-aware syn-
thesis and placement of object instances. In NeurIPS,
2018.
[97] Jonghyun
Lee,
Hansam
Cho,
Youngjoon
Yoo,
Seoung Bum Kim, and Yonghyun Jeong. Compose and
conquer: Diffusion-based 3d depth aware composable
image synthesis. In ICLR, 2024.
[98] Anat Levin, Assaf Zomet, Shmuel Peleg, and Yair


Weiss. Seamless image stitching in the gradient domain.
In ECCV, 2004.
[99] Boren Li, Po-Yu Zhuang, Jian Gu, Mingyang Li, and


Ping Tan.
Interpretable foreground object search as
knowledge distillation. In ECCV, 2020.
[100] Guanlin Li, Bin Zhao, and Xuelong Li.
Image har-
monization in complex degradation scenes.
Pattern
Recognition, page 112227, 2025.
[101] Haowen Li, Zhenfeng Fan, Zhang Wen, Zhengzhou


Zhu, and Yunjin Li. Aicomposer: Any style and content
image composition via feature integration.
In ICCV,
2025.
[102] Jiajie Li, Jian Wang, Chen Wang, and Jinjun Xiong.


Image harmonization with diffusion model.
arXiv


preprint arXiv:2306.10441, 2023.
[103] Jizhizi Li, Sihan Ma, Jing Zhang, and Dacheng Tao.


Privacy-preserving portrait matting. In ACM MM, 2021.
[104] Jizhizi Li, Jing Zhang, and Dacheng Tao. Deep auto-


matic natural image matting. In IJCAI, 2021.
[105] Jizhizi Li, Jing Zhang, Stephen J Maybank, and


Dacheng Tao.
Bridging composite and real: towards
end-to-end deep image matting. International Journal
of Computer Vision, 130(2):246–266, 2022.
[106] Lingxiao Li, Kaixiong Gong, Weihong Li, Xili Dai, Tao


Chen, Xiaojun Yuan, and Xiangyu Yue. BIFROST: 3d-
aware image compositing with language instructions. In
NeurIPS, 2024.
[107] Pengzhi Li, Qiang Nie, Ying Chen, Xi Jiang, Kai Wu,


Yuhuan Lin, Yong Liu, Jinlong Peng, Chengjie Wang,
and Feng Zheng. Tuning-free image customization with
image and text guidance. In ECCV, 2024.
[108] Ruibin Li, Jingcai Guo, Song Guo, Qihua Zhou, and


Jie Zhang.
FreePIH: Training-free painterly image
harmonization with diffusion model.
In ACM MM,
2024.
[109] Tianle Li, Max Ku, Cong Wei, and Wenhu Chen.


Dreamedit: Subject-driven image editing. arXiv preprint
arXiv: 2306.12624, 2023.
[110] Xiang Li, Guowei Teng, Ping An, Haiyan Yao, and Yilei


Chen. Advertisement logo compositing via adversarial
geometric consistency pursuit. In VCIP, 2019.
[111] Xiang Li, Guowei Teng, Ping An, and Hai-Yan Yao.


Image synthesis via adversarial geometric consistency
pursuit. Signal Processing: Image Communication, 99:
116489, 2021.
[112] Yijun Li, Ming-Yu Liu, Xueting Li, Ming-Hsuan Yang,


and Jan Kautz. A closed-form solution to photorealistic
image stylization. In ECCV, 2018.
[113] Zan Li, Wencheng Wang, and Fei Hou. Image compo-


sition with depth registration. In IJCAI, 2023.
[114] Zan Li, Bingnan Wang, Wencheng Wang, and Fei


Hou. Place anywhere: Learning spatial reasoning for
occlusion-aware image composition. In ICASSP, 2026.
[115] Dong Liang, Jinyuan Jia, Yuhao Liu, and Rynson WH


Lau. Hocomp: Interaction-aware human-object compo-
sition. In NeurIPS, 2025.
[116] Jing Liang, Li Niu, and Liqing Zhang. Inharmonious


region localization. In ICME, 2021.
[117] Jing Liang, Li Niu, Penghao Wu, Fengjun Guo, and


Teng Long. Inharmonious region localization by mag-
nifying domain discrepancy. In AAAI, 2022.
[118] Jingtang Liang, Xiaodong Cun, and Chi-Man Pun.


Spatial-separated curve rendering network for efficient
and high-resolution image harmonization.
In ECCV,
2022.
[119] Bin Liao, Yao Zhu, Chao Liang, Fei Luo, and Chunxia


Xiao.
Illumination animating and editing in a single
picture using scene structure estimation. Computers &
Graphics, 82:53–64, 2019.
[120] Chen-Hsuan Lin, Ersin Yumer, Oliver Wang, Eli Shecht-


man, and Simon Lucey. ST-GAN: spatial transformer
generative adversarial networks for image compositing.


29


In CVPR, 2018.
[121] Tsung-Yi Lin, Michael Maire, Serge J. Belongie, James


Hays, Pietro Perona, Deva Ramanan, Piotr Doll´ar, and
C. Lawrence Zitnick. Microsoft COCO: common ob-
jects in context. In ECCV, 2014.
[122] Jun Ling, Han Xue, Li Song, Rong Xie, and Xiao Gu.


Region-aware adaptive instance normalization for image
harmonization. In CVPR, 2021.
[123] Bin Liu, Kun Xu, and Ralph R Martin. Static scene


illumination estimation from videos with applications.
Journal of Computer Science and Technology, 32(3):
430–442, 2017.
[124] Daquan Liu, Chengjiang Long, Hongpan Zhang, Han-


ning Yu, Xinzhi Dong, and Chunxia Xiao.
ARshad-
owGAN: Shadow generative adversarial network for
augmented reality in single light scenes. In CVPR, 2020.
[125] Guilin Liu, Fitsum A Reda, Kevin J Shih, Ting-Chun


Wang, Andrew Tao, and Bryan Catanzaro.
Image
inpainting for irregular holes using partial convolutions.
In ECCV, 2018.
[126] Liu Liu, Bo Zhang, Jiangtong Li, Li Niu, Qingyang Liu,


and Liqing Zhang. OPA: Object placement assessment
dataset. arXiv preprint arXiv:2107.01889, 2021.
[127] Qinglin Liu, Haozhe Xie, Shengping Zhang, Bineng


Zhong, and Rongrong Ji.
Long-range feature propa-
gating for natural image matting. In ACM MM, 2021.
[128] Qingyang Liu, Junqi You, Jianting Wang, Xinhao Tao,


Bo Zhang Zhang, and Li Niu. Shadow generation for
composite image using diffusion model.
In CVPR,
2024.
[129] Sheng Liu, Cong Phuoc Huynh, Cong Chen, Maxim


Arap, and Raffay Hamid.
LEMaRT: Label-efficient
masked region transform for image harmonization. In
CVPR, 2023.
[130] Yong Liu, Wenpeng Xiao, Qianqian Wang, Junlin Chen,


Shiyin Wang, Yitong Wang, Xinglong Wu, and Yansong
Tang. Dreamlight: Towards harmonious and consistent
image relighting.
arXiv preprint arXiv:2506.14549,
2025.
[131] Yuhao Liu, Jiake Xie, Xiao Shi, Yu Qiao, Yujie Huang,


Yong Tang, and Xin Yang.
Tripartite information
mining and integration for image matting.
In ICCV,
2021.
[132] Lingxiao Lu, Jiangtong Li, Junyan Cao, Li Niu, and


Liqing Zhang.
Painterly image harmonization using
diffusion model. In ACM MM, 2023.
[133] Lingxiao Lu, Bo Zhang, and Li Niu.
Dreamcom:
Finetuning text-guided inpainting model for image com-
position. arXiv preprint arXiv:2309.15508, 2023.
[134] Shilin Lu, Yanzhu Liu, and Adams Wai-Kin Kong.


TF-ICON: Diffusion-based training-free cross-domain
image composition. In ICCV, 2023.
[135] Shilin Lu, Zhuming Lian, Zihan Zhou, Shaocong


Zhang, Chen Zhao, and Adams Wai-Kin Kong. Does
flux already know how to perform physically plausible
image composition? In ICLR, 2026.
[136] Xin Lu, Zhe Lin, Hailin Jin, Jianchao Yang, and


James Z Wang. A structure-preserving and illumination-


consistent cycle framework for image harmonization.
IEEE Transactions on Multimedia, 2022.
[137] Fujun Luan, Sylvain Paris, Eli Shechtman, and Kavita


Bala. Deep photo style transfer. In CVPR, 2017.
[138] Fujun Luan, Sylvain Paris, Eli Shechtman, and Kavita


Bala. Deep painterly harmonization. Computer Graph-
ics Forum, 37(4):95–106, 2018.
[139] Shengjie Ma, Qian Shen, Qiming Hou, Zhong Ren,


and Kun Zhou.
Neural compositing for real-time
augmented reality rendering in low-frequency lighting
environments. Science China Information Sciences, 64
(2):1–15, 2021.
[140] Chenlin Meng, Yutong He, Yang Song, Jiaming Song,


Jiajun Wu, Jun-Yan Zhu, and Stefano Ermon. SDEdit:
Guided image synthesis and editing with stochastic
differential equations. In ICLR, 2021.
[141] Quanling
Meng,
Shengping
Zhang,
Zonglin
Li,
Chenyang
Wang,
Weigang
Zhang,
and
Qingming
Huang.
Automatic shadow generation via exposure
fusion. IEEE Transactions on Multimedia, 2023.
[142] Quanling Meng, Qinglin Liu, Zonglin Li, Xiangyuan


Lan, Shengping Zhang, and Liqiang Nie.
High-
resolution image harmonization with adaptive-interval
color transformation. In NeurIPS, 2024.
[143] Shervin Minaee, Yuri Y Boykov, Fatih Porikli, Anto-


nio J Plaza, Nasser Kehtarnavaz, and Demetri Terzopou-
los. Image segmentation using deep learning: A survey.
IEEE Transactions on Pattern Analysis and Machine
Intelligence, 2021.
[144] Lukas Murmann, Michael Gharbi, Miika Aittala, and


Fredo Durand. A dataset of multi-illumination images
in the wild. In ICCV, 2019.
[145] Vu Nguyen, Tomas F Yago Vicente, Maozheng Zhao,


Minh Hoai, and Dimitris Samaras. Shadow detection
with conditional generative adversarial networks.
In
ICCV, 2017.
[146] Kiri Nichol. Painter by numbers. https://www.kaggle.


com/competitions/painter-by-numbers/data, 2016.
[147] Li Niu, Qingyang Liu, Zhenchen Liu, and Jiangtong


Li. Fast object placement assessment. arXiv preprint
arXiv:2205.14280, 2022.
[148] Li Niu, Junyan Cao, Wenyan Cong, and Liqing Zhang.


Deep image harmonization with learnable augmenta-
tion. In ICCV, 2023.
[149] Li Niu, Linfeng Tan, Xinhao Tao, Junyan Cao, Fengjun


Guo, Teng Long, and Liqing Zhang. Deep image har-
monization with globally guided feature transformation
and relation distillation. In ICCV, 2023.
[150] Li Niu, Junyan Cao, Yan Hong, and Liqing Zhang.


Painterly
image
harmonization
by
learning
from
painterly objects. In AAAI, 2024.
[151] Li Niu, Yan Hong, Junyan Cao, and Liqing Zhang.


Progressive painterly image harmonization from low-
level styles to high-level styles. In AAAI, 2024.
[152] Xi Ouyang, Yu Cheng, Yifan Jiang, Chun-Liang Li,


and Pan Zhou. Pedestrian-synthesis-GAN: Generating
pedestrian data in real scene and beyond. arXiv preprint
arXiv:1804.02047, 2018.


30


[153] Rohit Kumar Pandey, Sergio Orts Escolano, Chloe


LeGendre, Christian Haene, Sofien Bouaziz, Christoph
Rhemann, Paul Debevec, and Sean Fanello.
Total
relighting: Learning to relight portraits for background
replacement. In SIGGRAPH, 2021.
[154] Rishubh Parihar, Harsh Gupta, Sachidanand VS, and


R Venkatesh Babu. Text2place: Affordance-aware text
guided human placement. In ECCV, 2024.
[155] Dae Young Park and Kwang Hee Lee. Arbitrary style


transfer with style-attentional networks. In CVPR, 2019.
[156] Hwai-Jin Peng, Chia-Ming Wang, and Yu-Chiang Frank


Wang. Element-embedded style transfer networks for
style harmonization. In BMVC, 2019.
[157] Jinlong Peng, Zekun Luo, Liang Liu, and Boshen


Zhang.
FRIH: Fine-grained region-aware image har-
monization. In AAAI, 2024.
[158] Patrick P´erez, Michel Gangnet, and Andrew Blake.


Poisson image editing. In ACM SIGGRAPH, 2003.
[159] Kien T Pham, Jingye Chen, and Qifeng Chen. Tale:


Training-free
cross-domain
image
composition
via
adaptive latent manipulation and energy-guided opti-
mization. In ACM MM, 2024.
[160] Franc¸ois Piti´e, Anil C Kokaram, and Rozenn Dahyot.


Automated colour grading using colour distribution
transfer. Computer Vision and Image Understanding,
107(1-2):123–137, 2007.
[161] Thomas Porter and Tom Duff.
Compositing digital
images. In ACM Siggraph Computer Graphics, 1984.
[162] Matthew Poska, Sharon X Huang, and Bin Hwang.


Hopnet: Harmonizing object placement network for
realistic image generation via object composition. In
CVPR, 2025.
[163] Yaxuan Qin, Jiayu Xu, Ruiping Wang, and Xilin Chen.


Think before placement: Common sense enhanced
transformer for object placement. In ECCV, 2025.
[164] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya


Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen
Krueger, and Ilya Sutskever.
Learning transferable
visual models from natural language supervision.
In
ICML, 2021.
[165] Erik Reinhard, Michael Ashikhmin, Bruce Gooch, and


Peter Shirley.
Color transfer between images.
IEEE
Computer Graphics and Applications, 21(5):34–41,
2001.
[166] Tal Remez, Jonathan Huang, and Matthew Brown.


Learning to segment via cut-and-paste. In ECCV, 2018.
[167] Mengwei Ren, Wei Xiong, Jae Shin Yoon, Zhixin Shu,


Jianming Zhang, HyunJoon Jung, Guido Gerig, and
He Zhang.
Relightful harmonization: Lighting-aware
portrait background replacement. In CVPR, 2024.
[168] Xuqian Ren and Yifan Liu.
Semantic-guided multi-
mask image harmonization. In ECCV, 2022.
[169] Robin Rombach, Andreas Blattmann, Dominik Lorenz,


Patrick Esser, and Bj¨orn Ommer. High-resolution image
synthesis with latent diffusion models. In CVPR, 2022.
[170] Nataniel Ruiz, Yuanzhen Li, Neal Wadhwa, Yael Pritch,


Michael Rubinstein, David E Jacobs, and Shlomi


Fruchter. Magic insert: Style-aware drag-and-drop. In
ICCV, 2025.
[171] Tiago A Schieber, Laura Carpi, Albert D´ıaz-Guilera,


Panos M Pardalos, Cristina Masoller, and Mart´ın G
Ravetti. Quantification of network structural dissimi-
larities. Nature Communications, 8(1):1–10, 2017.
[172] Christoph Schuhmann, Richard Vencu, Romain Beau-


mont, Robert Kaczmarczyk, Clayton Mullis, Aarush
Katta, Theo Coombes, Jenia Jitsev, and Aran Komat-
suzaki.
LAION-400M: Open dataset of clip-filtered
400 million image-text pairs.
arXiv preprint arXiv:
2111.02114, 2021.
[173] Xiaoyong Shen, Aaron Hertzmann, Jiaya Jia, Sylvain


Paris, Brian Price, Eli Shechtman, and Ian Sachs.
Automatic portrait segmentation for image stylization.
Computer Graphics Forum, 35(2):93–102, 2016.
[174] Xintian Shen, Jiangning Zhang, Jun Chen, Shipeng Bai,


Yue Han, Yabiao Wang, Chengjie Wang, and Yong Liu.
Learning global-aware kernel for image harmonization.
In ICCV, 2023.
[175] Yichen Sheng, Jianming Zhang, and Bedrich Benes.


SSN: Soft shadow network for image compositing. In
CVPR, 2021.
[176] Yichen Sheng, Yifan Liu, Jianming Zhang, Wei Yin,


A. Cengiz Oztireli, He Zhang, Zhe Lin, Eli Shechtman,
and Bedrich Benes.
Controllable shadow generation
using pixel height maps. In ECCV, 2022.
[177] Yichen Sheng, Jianming Zhang, Julie Philip, Yannick


Hold-Geoffroy, Xin Sun, He Zhang, Lu Ling, and
Bedrich Benes.
PixHt-Lab: Pixel height based light
effect generation for image compositing.
In CVPR,
2023.
[178] Philip Wootaek Shin, Jack Sampson, Vijaykrishnan


Narayanan, Andres Marquez, and Mahantesh Halap-
panavar. Disharmony: Forensics using reverse lighting
harmonization. In WACV, 2025.
[179] Zhixin Shu, Sunil Hadap, Eli Shechtman, Kalyan


Sunkavalli, Sylvain Paris, and Dimitris Samaras. Por-
trait lighting transfer using a mass transport approach.
ACM Transactions on Graphics, 36(4):1, 2017.
[180] Jaskirat Singh, Jianming Zhang, Qing Liu, Cameron


Smith, Zhe Lin, and Liang Zheng. Smartmask: Context
aware high-fidelity mask generation for fine-grained
object insertion and layout control. In CVPR, 2024.
[181] Konstantin
Sofiiuk,
Polina
Popenova,
and
Anton
Konushin. Foreground-aware semantic representations
for image harmonization. In WACV, 2021.
[182] Shuangbing Song, Fan Zhong, Xueying Qin, and


Changhe Tu.
Illumination harmonization with gray
mean scale. In Computer Graphics International Con-
ference, 2020.
[183] Wensong Song, Hong Jiang, Zongxing Yang, Ruijie


Quan, and Yi Yang. Insert anything: Image insertion
via in-context editing in dit. In AAAI, 2026.
[184] Yizhi Song, Zhifei Zhang, Zhe Lin, Scott Cohen, Brian


Price, Jianming Zhang, Soo Ye Kim, and Daniel Aliaga.
Objectstitch: Generative object compositing. In CVPR,
2023.


31


[185] Yizhi Song, Zhifei Zhang, Zhe Lin, Scott Cohen, Brian


Price, Jianming Zhang, Soo Ye Kim, He Zhang, Wei
Xiong, and Daniel Aliaga. Imprint: Generative object
compositing by learning identity-preserving representa-
tion. In CVPR, 2024.
[186] Zhangliang Sun and Hui Zhang. Painterly image har-


monization via bi-transformation with dynamic kernels.
In BMVC, 2024.
[187] Kalyan Sunkavalli, Micah K. Johnson, Wojciech Ma-


tusik, and Hanspeter Pfister. Multi-scale image harmo-
nization. ACM Transactions on Graphics, 29(4):125:1–
125:10, 2010.
[188] Richard Szeliski, Matthew Uyttendaele, and Drew


Steedly. Fast poisson blending using multi-splines. In
ICCP, 2011.
[189] Fuwen Tan, Crispin Bernier, Benjamin Cohen, Vicente


Ordonez, and Connelly Barnes. Where and who? au-
tomatic semantic-aware person composition. In WACV,
2018.
[190] Linfeng Tan, Jiangtong Li, Li Niu, and Liqing Zhang.


Deep image harmonization in dual color spaces.
In
ACM MM, 2023.
[191] Xuehan Tan, Panpan Xu, Shihui Guo, and Wencheng


Wang. Image composition of partially occluded objects.
Computer Graphics Forum, 38(7):641–650, 2019.
[192] Masayuki Tanaka, Ryo Kamio, and Masatoshi Okutomi.


Seamless image cloning by a closed form solution of a
modified poisson problem. In SIGGRAPH Asia, 2012.
[193] Litian Tao, Lu Yuan, and Jian Sun. Skyfinder: attribute-


based sky image search. ACM Transactions on Graph-
ics, 28(3):1–5, 2009.
[194] Michael W Tao, Micah K Johnson, and Sylvain Paris.


Error-tolerant image compositing. In ECCV, 2010.
[195] Weijing Tao, Xiaofeng Yang, Miaomiao Cui, and Gu-


osheng Lin. Motioncom: Automatic and motion-aware
image composition with llm and video diffusion prior.
arXiv preprint arXiv:2409.10090, 2024.
[196] Xinhao Tao, Junyan Cao, Yan Hong, and Li Niu.


Shadow generation with decomposed mask prediction
and attentive shadow filling. In AAAI, 2024.
[197] Xinhao Tao, Tianyuan Qiu, Junyan Cao, and Li Niu.


Diverse
image
harmonization.
arXiv
preprint
arXiv:2407.15481, 2024.
[198] Gemma Canet Tarr´es, Zhe Lin, Zhifei Zhang, Jianming


Zhang, Yizhi Song, Dan Ruta, Andrew Gilbert, John
Collomosse, and Soo Ye Kim.
Thinking outside the
bbox: Unconstrained generative object compositing. In
ECCV, 2024.
[199] Gemini Team, R Anil, S Borgeaud, Y Wu, JB Alayrac,


J Yu, R Soricut, J Schalkwyk, AM Dai, A Hauth, et al.
Gemini: A family of highly capable multimodal models,
2024. arXiv preprint arXiv:2312.11805, 2024.
[200] Ayush Tewari, Tae-Hyun Oh, Tim Weyrich, Bernd


Bickel, Hans-Peter Seidel, Hanspeter Pfister, Wojciech
Matusik, Mohamed Elgharib, Christian Theobalt, et al.
Monocular reconstruction of neural face reflectance
fields. In CVPR, 2021.
[201] Chunwei Tian, Lunke Fei, Wenxian Zheng, Yong Xu,


Wangmeng Zuo, and Chia-Wen Lin. Deep learning on
image denoising: An overview. Neural Networks, 131:
251–275, 2020.
[202] Shashank Tripathi, Siddhartha Chandra, Amit Agrawal,


Ambrish Tyagi, James M. Rehg, and Visesh Chari.
Learning to generate synthetic data via compositing. In
CVPR, 2019.
[203] Yi-Hsuan
Tsai,
Xiaohui
Shen,
Zhe
Lin,
Kalyan
Sunkavalli, and Ming-Hsuan Yang. Sky is not the limit:
semantic-aware sky replacement. ACM Trans. Graph.,
35(4):149–1, 2016.
[204] Yi-Hsuan
Tsai,
Xiaohui
Shen,
Zhe
Lin,
Kalyan
Sunkavalli, Xin Lu, and Ming-Hsuan Yang. Deep image
harmonization. In CVPR, 2017.
[205] Jeya Maria Jose Valanarasu, He Zhang, Jianming


Zhang, Yilin Wang, Zhe Lin, Jose Echevarria, Yinglan
Ma, Zijun Wei, Kalyan Sunkavalli, and Vishal M. Patel.
Interactive portrait harmonization. In ICLR, 2023.
[206] Raghu Vamsi Chittersu, Yuvraj Singh Rathore, Pranav


Adlinge, and Kunal Swami. Insert in style: A zero-shot
generative framework for harmonious cross-domain ob-
ject composition.
arXiv preprint arXiv:2511.15197,
2025.
[207] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob


Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser,
and Illia Polosukhin. Attention is all you need. In NIPS,
2017.
[208] Anna
Volokitin,
Igor
Susmelj,
Eirikur
Agustsson,
Luc Van Gool, and Radu Timofte. Efficiently detecting
plausible locations for object placement using masked
convolutions. In ECCV workshop, 2020.
[209] Hao Wang, Qilong Wang, Fan Yang, Weiqi Zhang, and


Wangmeng Zuo. Data augmentation for object detection
via progressive and selective instance-switching. arXiv
preprint arXiv:1906.00358, 2019.
[210] Haolin Wang, Ming Liu, Zifei Yan, Chao Zhou, Longan


Xiao, and Wangmeng Zuo.
Retrieval-augmented im-
age harmonization. Pattern Recognition, page 112556,
2025.
[211] Haoxuan Wang, Jinlong Peng, Qingdong He, Hao Yang,


Ying Jin, Jiafu Wu, Xiaobin Hu, Yanjie Pan, Zhenye
Gan, Mingmin Chi, et al. Unicombine: Unified multi-
conditional combination with diffusion transformer. In
ICCV, 2025.
[212] Ke Wang, Micha¨el Gharbi, He Zhang, Zhihao Xia, and


Eli Shechtman. Semi-supervised parametric real-world
image harmonization. In CVPR, 2023.
[213] Shuo Wang, Weijie Lv, Xinyuan Zhao, Xinyu Zhang,


Junyu Su, and Long Zeng. Refined-mask guided multi-
stream blending network. Multimedia Tools and Appli-
cations, 83(19):56445–56462, 2024.
[214] Tianyu Wang, Xiaowei Hu, Qiong Wang, Pheng-Ann


Heng, and Chi-Wing Fu. Instance shadow detection. In
CVPR, 2020.
[215] Tianyu Wang, Xiaowei Hu, Pheng-Ann Heng, and Chi-


Wing Fu. Instance shadow detection with a single-stage
detector. IEEE Transactions on Pattern Analysis and
Machine Intelligence, 45(3):3259–3273, 2022.


32


[216] Tianyu Wang, Jianming Zhang, Haitian Zheng, Zhihong


Ding, Scott Cohen, Zhe Lin, Wei Xiong, Chi-Wing Fu,
Luis Figueroa, and Soo Ye Kim. Metashadow: Object-
centered shadow detection, removal, and synthesis. In
CVPR, 2025.
[217] Xiaolong Wang, Rohit Girdhar, and Abhinav Gupta.


Binge watching: Scaling affordance learning from sit-
coms. In CVPR, 2017.
[218] Xiaolong Wang, Ross Girshick, Abhinav Gupta, and


Kaiming He.
Non-local neural networks.
In CVPR,
2018.
[219] Xudong Wang, Li Niu, Junyan Cao, Yan Hong, and


Liqing Zhang. Painterly image harmonization via ad-
versarial residual learning. In WACV, 2024.
[220] Yibin Wang, Yuchao Feng, and Jianwei Zheng. Learn-


ing object placement via convolution scoring attention.
In BMVC, 2024.
[221] Yibin Wang, Weizhong Zhang, Jianwei Zheng, and


Cheng Jin. Primecomposer: Faster progressively com-
bined diffusion for image composition with attention
steering. In ACM MM, 2024.
[222] Yijiang Wang, Yuqi Li, Chong Wang, and Xulun Ye.


Harmonized portrait-background image composition.
Computer Graphics Forum, 42(6):e14921, 2023.
[223] Zhibo Wang, Xin Yu, Ming Lu, Quan Wang, Chen


Qian, and Feng Xu.
Single image portrait relighting
via explicit multiple reflectance channel modeling. ACM
Transactions on Graphics, 39(6):1–13, 2020.
[224] Zhihao Wang, Jian Chen, and Steven CH Hoi. Deep


learning for image super-resolution: A survey.
IEEE
Transactions on Pattern Analysis and Machine Intelli-
gence, 43(10):3365–3387, 2020.
[225] Zhou Wang, Alan C Bovik, Hamid R Sheikh, and


Eero P Simoncelli. Image quality assessment: from er-
ror visibility to structural similarity. IEEE Transactions
on Image Processing, 13(4):600–612, 2004.
[226] Henrique Weber, Donald Pr´evost, and Jean-Franc¸ois


Lalonde. Learning to estimate indoor lighting from 3d
objects. In 3DV, 2018.
[227] Shuchen Weng, Wenbo Li, Dawei Li, Hongxia Jin,


and Boxin Shi.
Misc: Multi-condition injection and
spatially-adaptive compositing for conditional person
image synthesis. In CVPR, 2020.
[228] Daniel Winter, Matan Cohen, Shlomi Fruchter, Yael


Pritch, Alex Rav-Acha, and Yedid Hoshen. Objectdrop:
Bootstrapping counterfactuals for photorealistic object
removal and insertion. In ECCV, 2024.
[229] Daniel Winter, Asaf Shul, Matan Cohen, Dana Berman,


Yael Pritch, Alex Rav-Acha, and Yedid Hoshen. Ob-
jectmate: A recurrence prior for object insertion and
subject-driven generation. In ICCV, 2025.
[230] Huikai Wu, Shuai Zheng, Junge Zhang, and Kaiqi


Huang.
GP-GAN: Towards realistic high-resolution
image blending. In ACM MM, 2019.
[231] Penghao Wu, Li Niu, Jing Liang, and Liqing Zhang.


Inharmonious region localization via recurrent self-
reasoning. In BMVC, 2022.
[232] Penghao Wu, Li Niu, and Liqing Zhang. Inharmonious


region localization with auxiliary style feature.
In
BMVC, 2022.
[233] Zongze Wu, Dani Lischinski, and Eli Shechtman. Fine-


grained foreground retrieval via teacher-student learn-
ing. In WACV, 2021.
[234] Xuezhong Xiao and Lizhuang Ma.
Color transfer in
correlated color space. In ACM International Confer-
ence on Virtual Reality Continuum and Its Applications,
2006.
[235] Yazhou Xing, Yu Li, Xintao Wang, Ye Zhu, and Qifeng


Chen. Composite photograph harmonization with com-
plete background cues. In ACM MM, 2022.
[236] Dejia Xu, Xingqian Xu, Wenyan Cong, Humphrey


Shi, and Zhangyang Wang. Reference-based painterly
inpainting via diffusion: Crossing the wild reference
domain gap. arXiv preprint arXiv: 2307.10584, 2023.
[237] Ke Xu, Gerhard Petrus Hancke, and Rynson WH Lau.


Learning image harmonization in the linear color space.
In ICCV, 2023.
[238] Ning Xu, Brian Price, Scott Cohen, and Thomas Huang.


Deep image matting. In CVPR, 2017.
[239] Yu Xu, Fan Tang, You Wu, Lin Gao, Oliver Deussen,


Hongbin Yan, Jintao Li, Juan Cao, and Tong-Yee Lee.
In-context brush: Zero-shot customized subject inser-
tion with context-aware latent space manipulation. In
SIGGRAPH Asia, 2025.
[240] Ben Xue, Shenghui Ran, Quan Chen, Rongfei Jia,


Binqiang Zhao, and Binqiang Zhao. DCCF: Deep com-
prehensible color filter learning framework for high-
resolution image harmonization. In ECCV, 2022.
[241] Su Xue, Aseem Agarwala, Julie Dorsey, and Holly E.


Rushmeier. Understanding and improving the realism
of image composites. ACM Transactions on Graphics,
31(4):84:1–84:10, 2012.
[242] Binxin Yang, Shuyang Gu, Bo Zhang, Ting Zhang,


Xuejin Chen, Xiaoyan Sun, Dong Chen, and Fang Wen.
Paint by example: Exemplar-based image editing with
diffusion models. In CVPR, 2023.
[243] Lu Yang, Yuanhao Wang, Yicheng Liu, Enze Wang,


Ziyang Zhao, Yanqi He, Zexian Song, and Hao Lu. Uni-
com: Unified, foreground-aware, and context-realistic
deep image composition with diffusion model.
Neu-
rocomputing, page 131129, 2025.
[244] Jieteng Yao, Junjie Chen, Li Niu, and Bin Sheng. Scene-


aware human pose generation using transformer.
In
ACM MM, 2023.
[245] Guosheng Ye, Jianming Wang, and Zizhong Yang.


Efficient object placement via ftopnet. Electronics, 12
(19):4106, 2023.
[246] Raymond A Yeh, Chen Chen, Teck Yian Lim, Alexan-


der G Schwing, Mark Hasegawa-Johnson, and Minh N
Do. Semantic image inpainting with deep generative
models. In CVPR, 2017.
[247] Huayan Yu, Hai Huang, Yueyan Zhu, and Aoran Chen.


Semantic-aware visual consistency network for fused
image harmonisation.
IET Signal Processing, 17(6):
e12219, 2023.
[248] Jiahui Yu, Zhe Lin, Jimei Yang, Xiaohui Shen, Xin Lu,


33


and Thomas S Huang. Free-form image inpainting with
gated convolution. In ICCV, 2019.
[249] Yongsheng Yu, Ziyun Zeng, Haitian Zheng, and Jiebo


Luo. Omnipaint: Mastering object-oriented editing via
disentangled insertion-removal inpainting.
In ICCV,
2025.
[250] Ziqi Yu, Jing Zhou, Zhongyun Bao, Gang Fu, Weilei


He, Chao Liang, and Chunxia Xiao. Cfdiffusion: Con-
trollable foreground relighting in image compositing via
diffusion model. In ACM MM, 2024.
[251] Ziyang Yuan, Mingdeng Cao, Xintao Wang, Zhon-


gang Qi, Chun Yuan, and Ying Shan.
Customnet:
Zero-shot object customization with variable-viewpoints
in text-to-image diffusion models.
arXiv preprint
arXiv:2310.19784, 2023.
[252] Fangneng Zhan, Hongyuan Zhu, and Shijian Lu. Spatial


fusion GAN for image synthesis. In CVPR, 2019.
[253] Fangneng Zhan, Shijian Lu, Changgong Zhang, Feiying


Ma, and Xuansong Xie. Adversarial image composition
with auxiliary illumination. In ACCV, 2020.
[254] Fangneng Zhan, Jiaxing Huang, and Shijian Lu. Hierar-


chy composition GAN for high-fidelity image synthesis.
IEEE Transactions on cybernetics, 2021.
[255] Bo Zhang, Yuxuan Duan, Jun Lan, Yan Hong, Huijia


Zhu, Weiqiang Wang, and Li Niu. Controlcom: Control-
lable image composition using diffusion model. arXiv
preprint arXiv:2308.10040, 2023.
[256] Bo Zhang, Yue Liu, Kaixin Lu, Li Niu, and Liqing


Zhang.
Spatial transformation for image compo-
sition via correspondence learning.
arXiv preprint
arXiv:2207.02398, 2023.
[257] Bo Zhang, Jiacheng Sui, and Li Niu. Foreground object


search by distilling composite image feature. In ICCV,
2023.
[258] He Zhang, Jianming Zhang, Federico Perazzi, Zhe Lin,


and Vishal M Patel. Deep image compositing. In WACV,
2021.
[259] Jinsong Zhang, Kalyan Sunkavalli, Yannick Hold-


Geoffroy, Sunil Hadap, Jonathan Eisenman, and Jean-
Franc¸ois Lalonde.
All-weather deep outdoor lighting
estimation. In CVPR, 2019.
[260] Kaihao Zhang, Wenqi Ren, Wenhan Luo, Wei-Sheng


Lai, Bj¨orn Stenger, Ming-Hsuan Yang, and Hongdong
Li.
Deep image deblurring: A survey.
International
Journal of Computer Vision, 130(9):2103–2130, 2022.
[261] Lingzhi Zhang, Tarmily Wen, Jie Min, Jiancong Wang,


David Han, and Jianbo Shi. Learning object placement
by inpainting for compositional data augmentation. In
ECCV, 2020.
[262] Lingzhi Zhang, Tarmily Wen, and Jianbo Shi.
Deep
image blending. In WACV, 2020.
[263] Longwen Zhang, Qixuan Zhang, Minye Wu, Jingyi Yu,


and Lan Xu. Neural video portrait relighting in real-
time via consistency modeling. In ICCV, 2021.
[264] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala.


Adding conditional control to text-to-image diffusion
models. In ICCV, 2023.
[265] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Scal-


ing in-the-wild training for diffusion-based illumination
harmonization and editing by imposing consistent light
transport. In ICLR, 2025.
[266] Qi Zhang, Guanyu Xing, Mengting Luo, Jianwei Zhang,


and Yanli Liu. Inserting objects into any background
images via implicit parametric representation.
IEEE
Transactions on Visualization and Computer Graphics,
2024.
[267] Richard Zhang, Phillip Isola, Alexei A Efros, Eli


Shechtman, and Oliver Wang.
The unreasonable ef-
fectiveness of deep features as a perceptual metric. In
CVPR, 2018.
[268] Shengping
Zhang,
Quanling
Meng,
Qinglin
Liu,
Liqiang Nie, Bineng Zhong, Xiaopeng Fan, and Ron-
grong Ji. Interactive object placement with reinforce-
ment learning. In ICML, 2023.
[269] Shu Zhang, Hai Huang, and Yueyan Zhu. Multi-scale


context aggregation network for inharmonious region
localization. In ICAIT, 2023.
[270] Shuyang Zhang, Runze Liang, and Miao Wang. Shad-


owGAN: Shadow synthesis for virtual objects with
conditional adversarial networks. Computational Visual
Media, 5(1):105–115, 2019.
[271] Song-Hai Zhang, Zhengping Zhou, Bin Liu, Xi Dong,


and Peter Hall.
What and where: A context-based
recommendation system for object insertion. Compu-
tational Visual Media, 6(1):79–93, 2020.
[272] Xin Zhang, Jiaxian Guo, Paul Yoo, Yutaka Matsuo,


and Yusuke Iwasawa.
Subject-driven image editing
with pre-trained diffusion model. arXiv preprint arXiv:
2306.07596, 2023.
[273] Zhiqiu Zhang, Dongqi Fan, Mingjie Wang, Qiang Tang,


Jian Yang, and Zili Yi.
Region-to-region: Enhancing
generative image harmonization with adaptive regional
injection. arXiv preprint arXiv:2508.09746, 2025.
[274] Zitian Zhang, Fr´ed´eric Fortier-Chouinard, Mathieu


Garon, Anand Bhattad, and Jean-Franc¸ois Lalonde.
Zerocomp: Zero-shot object compositing from image
intrinsics via diffusion. In WACV, 2025.
[275] Haonan Zhao, Qingyang Liu, Xinhao Tao, Li Niu, and


Guangtao Zhai.
Shadow generation using diffusion
model with geometry prior. In CVPR, 2025.
[276] Haonan Zhao, Qingyang Liu, Jiaxuan Chen, and Li Niu.


Reflection generation for composite image using diffu-
sion model. In ICME, 2026.
[277] Hengshuang Zhao, Xiaohui Shen, Zhe L. Lin, Kalyan


Sunkavalli, Brian L. Price, and Jiaya Jia. Compositing-
aware image search. In ECCV, 2018.
[278] Yinan Zhao, Brian L. Price, Scott D. Cohen, and Danna


Gurari.
Unconstrained foreground object search.
In
ICCV, 2019.
[279] Hang Zhou, Xinxin Zuo, Rui Ma, and Li Cheng. Boot-


place: Bootstrapped object placement with detection
transformers. In CVPR, 2025.
[280] Jing Zhou, Ziqi Yu, Zhongyun Bao, Gang Fu, Weilei


He, Chao Liang, and Chunxia Xiao. Foreground harmo-
nization and shadow generation for composite image. In
ACM MM, 2024.


34


[281] Jinghao Zhou, Tomas Jakab, Philip Torr, and Christian


Rupprecht. Scene-conditional 3d object stylization and
composition. In ECCV, 2024.
[282] Pengfei Zhou, Fangxiang Feng, Guang Liu, Ruifan Li,


and Xiaojie Wang. Diffharmony++: Enhancing image
harmonization with harmony-vae and inverse harmo-
nization model. In ACM MM, 2024.
[283] Pengfei Zhou, Fangxiang Feng, and Xiaojie Wang.


Diffharmony: Latent diffusion model meets image har-
monization. In ICMR, 2024.
[284] Siyuan Zhou, Liu Liu, Li Niu, and Liqing Zhang. Learn-


ing object placement via dual-path graph completion. In
ECCV, 2022.
[285] Jun-Yan Zhu, Philipp Krahenbuhl, Eli Shechtman, and


Alexei A Efros. Learning a discriminative model for the
perception of realism in composite images. In ICCV,
2015.
[286] Sijie Zhu, Zhe Lin, Scott D. Cohen, Jason Kuen, Zhifei


Zhang, and Chen Chen. GALA: Toward geometry-and-
lighting-aware object search for compositing. In ECCV,
2022.
[287] Sijie Zhu, Zhe Lin, Scott Cohen, Jason Kuen, Zhifei


Zhang, and Chen Chen.
TopNet: Transformer-based
object placement network for image compositing. In
CVPR, 2023.
[288] Zhengxia Zou, Rui Zhao, Tianyang Shi, Shuang Qiu,


and Zhenwei Shi.
Castle in the sky: Dynamic sky
replacement and harmonization in videos. IEEE Trans-
actions on Image Processing, 31:5067–5078, 2022.
