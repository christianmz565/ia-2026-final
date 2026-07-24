Leveraging Latent Diffusion Models for
Training-Free In-Distribution Data Augmentation


for Surface Defect Detection


Federico Girella, Ziyue Liu, Franco Fummi, Francesco Setti, Marco Cristani, Luigi Capogrosso


Department of Engineering for Innovation Medicine, University of Verona, Italy


name.surname@univr.it


Abstract—Defect detection is the task of identifying defects
in production samples. Usually, defect detection classifiers are
trained on ground-truth data formed by normal samples (neg-
ative data) and samples with defects (positive data), where
the latter are consistently fewer than normal samples. State-
of-the-art data augmentation procedures add synthetic defect
data by superimposing artifacts to normal samples to mitigate
problems related to unbalanced training data. These techniques
often produce out-of-distribution images, resulting in systems
that learn what is not a normal sample but cannot accurately
identify what a defect looks like. In this work, we introduce
DIAG, a training-free Diffusion-based In-distribution Anomaly
Generation pipeline for data augmentation. Unlike conventional
image generation techniques, we implement a human-in-the-loop
pipeline, where domain experts provide multimodal guidance
to the model through text descriptions and region localization
of the possible anomalies. This strategic shift enhances the
interpretability of results and fosters a more robust human
feedback loop, facilitating iterative improvements of the gener-
ated outputs. Remarkably, our approach operates in a zero-shot
manner, avoiding time-consuming fine-tuning procedures while
achieving superior performance. We demonstrate the efficacy
and versatility of DIAG with respect to state-of-the-art data
augmentation approaches on the challenging KSDD2 dataset,
with an improvement in AP of approximately 18% when positive
samples are available and 28% when they are missing. The source
code is available at https://github.com/intelligolabs/DIAG.


Index Terms—Diffusion Models, Data Augmentation, Surface
Defect Detection.


I. INTRODUCTION


Surface Defect Detection (SDD) is a challenging problem
in industrial scenarios, defined as the task of individuating
samples containing a defect [1], i.e., samples that do not
conform to a prototypical texture. In many real-world appli-
cations, a human expert inspects every product and removes
those defective pieces. Unfortunately, training human experts
can be expensive. Moreover, humans are relatively slow in


This study was carried out within the PNRR research activities of the
consortium iNEST (Interconnected North-Est Innovation Ecosystem) funded
by the European Union Next-GenerationEU (Piano Nazionale di Ripresa e
Resilienza (PNRR) – Missione 4 Componente 2, Investimento 1.5 – D.D.
1058 23/06/2022, ECS 00000043). This manuscript reflects only the Authors’
views and opinions. Neither the European Union nor the European Commis-
sion can be considered responsible for them. Furthermore, this study was also
partially funded by the European Union - NextGenerationEU (Italiadomani,
Piano Nazionale di Ripresa e Resilienza (PNRR) - Missione 4 - Componente
2, Investimento 3.3 - progetto M4C2).


Defect mask


Prompt


Neg. prompt


"A photo of a
scratched surface"


"A photo of a
smooth surface"


Training-free image generation via LDM


Normal samples
 Classification with the


generated samples


Anomalous
Not anomalous


Latent Diffusion


Model


Classification


model


1


2


3


Fig. 1.
The DIAG pipeline. Starting from positive samples, we leverage a
Latent Diffusion Model (LDM) to synthesize novel in-distribution high-quality
images of defective surfaces based on defect localization and textual prompts.
These synthetic images are then used as anomaly samples to train a binary
classifier for anomaly detection.


accomplishing this task, and their performances are subject to
stress and fatigue.


Automated defect detection systems [2], [3] can easily
overcome most of these issues by learning classifiers on
defective and nominal training products. The main drawback is
the data collection process required to train a model effectively.
Indeed, defective items (i.e., positive samples) are relatively
rare compared to nominal items (i.e., negative samples). Thus,
the user may need to collect massive amounts of data to
have enough positive samples. Moreover, with the rise of
the Industry 4.0 paradigm and the transition towards flexible
manufacturing processes, there is an increasing demand for
systems that can quickly adapt to new production setups [4],
i.e., customized products manufactured in small batches. Tra-
ditional automated systems cannot comply with these demands
since data collection could easily involve the whole batch size.


Recent studies on SDD focused on limiting the impact of
the labeling process by formulating the problem under the
unsupervised learning paradigm [5], [6] or training exclusively


Copyright © 2024 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future
media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to


servers or lists, or reuse of any copyrighted component of this work in other works.


arXiv:2407.03961v2  [cs.CV]  11 Jul 2024


on nominal samples [7], possibly using few-shot learning
strategies [8]. In both cases, the goal is to generate an accurate
model of the nominal sample distribution and classify every-
thing with a low probability score as anomalies. However,
due to the limited restoration capability of these models, these
approaches tend to generate many false positives, especially
on datasets with complex structures or textures [9].


It is worth noting that, in industrial setups, anomalies are
not generated by Gaussian processes but are the outcome of
specific, often predictable, issues during the production pro-
cess. Consequently, the anomalous samples are not randomly
distributed outside the nominal distribution; they can be mod-
eled as a mixture of Gaussian distributions in the feature space
instead. Expert operators can easily define the main problems
they can expect from the manufacturing process, such as
which kind of defects, in which locations, and how often they
expect them to appear. Thus, generative AI can represent a
powerful tool for SDD, with defect image generation emerging
as a promising approach to enhance detector performance.
Specifically, in recent years, Denoising Diffusion Probabilistic
Models (DDPMs) [10] received significant attention as a
powerful class of generative models.


In this paper, we propose an interactive learning protocol
where a vision language model is used to generate realistic
images starting from textual prompts. Specifically, we promote
using DDPMs to produce fine-grained realistic defect images
that can be used as positive samples to train an anomaly
detection model. We name our approach DIAG, a training-free
Diffusion-based In-distribution Anomaly Generation pipeline
for data augmentation in the SDD task. By leveraging pre-
trained DDPMs with multimodal conditioning, we can exploit
domain experts’ knowledge to generate plausible anomalies
without needing real positive data. When using these aug-
mented images to train an anomaly detection model, we show
a notable increase in the detection performance compared
to previous state-of-the-art augmentation pipelines. Figure 1
outlines our approach, which will be explained in Section III.


The main contributions of our work are as follows:


• We present DIAG, a complete pipeline for training
anomaly detection models based on nominal images and
textual prompts. We showcase the superior outcomes
achieved by utilizing generated defective samples com-
pared to previous state-of-the-art approaches.


• We dive into spatial control approaches to enable the
synthesis of defect samples incorporating regional in-
formation and exhibit enhanced controllability of the
image generation through a human-in-the-loop pipeline,
effectively utilizing domain expertise to generate more
plausible in-distribution anomalies.


II. RELATED WORK


Surface defect detection refers to identifying and catego-
rizing irregularities, flaws, or imperfections on the surface of
materials or objects. These defects include scratches, cracks,
discolorations, and any other anomaly that deviates from the


expected surface quality. Research has been conducted accord-
ing to different setups: unsupervised approaches [11] use a
mixture of unlabelled positive and negative sample images
for training; supervised approaches require labeled samples
in the form of binary masks representing the defects (full
supervision) [12] or simply as a tag for the whole image (weak
supervision) [13]. Supervised methods demonstrated superior
accuracy in the identification of anomalies. Nevertheless, the
effort required to provide good annotations is not always
justified. Collecting positive samples can be time and resource-
consuming due to the low rate of defective products generated
by industrial lines.


Thus, many recent approaches adopt a “clean” setup, where
the training set consists of only nominal samples. Two strate-
gies can be adopted in clean setups: model fitting and image
generation. Model fitting approaches aim at generating an ac-
curate model of the nominal distribution, considering an outlier
every sample with a likelihood lower than –or a distance from
the nominal prototype higher than– a predefined threshold [7],
[14]. On the contrary, data augmentation approaches leverage
generative methods to synthesize images of defects and use
these images as positive samples for training a supervised
model. Specifically, this work focuses on generation-based
data augmentation under clean setups.


The most popular data augmentation pipeline for SDD
consists of a series of random standard transformations of the
input image –such as mirroring, rotations, and color changes–
followed by the super-imposition of noisy patches [15].


In [16], an ablation study focused on the generation of
synthetic anomalies leads to the following findings: i) adding
synthetic noise images is never counterproductive, it just
diminishes the effectiveness in percentage; ii) few generated
anomaly images (in the order of tens) are enough to increase
the performance substantially; iii) textural injection in the
anomalies is essential, or, equivalently, adding uniformly col-
ored patches is ineffective.


In MemSeg [15], the pipeline for the generation of the
abnormal synthetic examples is divided into three steps: i)
a Region of Interest (ROI) indicating where the defect will
be located is generated using Perlin noise and the target
foreground; ii) the ROI is applied to a noise image to generate
a noise foreground ROI; iii) the noise foreground ROI is
super-imposed on the original image to obtain the simulated
anomalous image. However, all these approaches are based
on generating out-of-distribution patterns that do not faithfully
represent the target-domain anomalies.


In [17], the authors introduced the concept of “extended
anomalies”, where the specific abnormal regions of the seen
anomalies are placed at any possible position within the
normal sample after applying random spatial transformations.
Unfortunately, this requires an accurate segmentation of the
training images, an operation we may want to avoid.


More recently, the first work that draws attention to in-
distribution defect data is In&Out [18], in which the authors
empirically show that diffusion models provide more realistic
in-distribution defects.


In this paper, we significantly improve the generation of in-
distribution anomalous samples incorporating domain knowl-
edge provided by an expert user through textual prompts and
localization of salient regions. We will use state-of-the-art
MemSeg [15] and In&Out [18] methods as competitors for
our augmentation pipeline. With DIAG, we can produce a
distribution of defective images closer to the real one, resulting
in a more precise identification of the decision boundaries in
the classification step.


III. METHODOLOGY
In this section, we provide detailed explanations of DIAG.
In particular, Section III-A covers techniques for diffusion-
based image generation, Section III-B showcases the anoma-
lous image generation pipeline, and Section III-C outlines the
anomaly detection model training procedure.


A. Multimodal diffusion-based image generation


DDPMs [10], [19] are a class of deep latent variable models
that work by modeling the joint distribution of the data
over a Markovian inference process. This process consists
of small perturbations of the data with a variance-preserving
property [20], such that the limit distribution after the dif-
fusion process is approximately identical to a known prior
distribution. Starting with samples from the prior, a reverse
diffusion process is learned by gradually denoising the sample
to resemble the initial data by the end of the procedure.


Formally, the data distribution q(x0) is modelled through a
latent variable model pθ(x0):


pθ(x0) =


Z


pθ(x0:T )dx1:T ,
(1)


pθ(x0:T ) := pθ(xT )


T
Y


t=1


p(t)


θ (xt−1|xt) ,
(2)


where x1, . . . , xT are latent variables of the same dimension-
ality as x0.


The parameters θ are learned by maximizing an ELBO of
the log evidence, i.e.:


max


θ
Eq(x0)[log pθ(x0)] ≤


max


θ
Eq(x0,x1,...,xT ) [log pθ(x0:T ) −log q(x1:T |x0)] ,
(3)


where q(x1:T |x0) represents a fixed inference process defined
as the following as a Markov chain:


q(x1:T |x0) :=


T
Y


t=1


q(xt|xt−1) ,
(4)


q(xt|xt−1) := N


r αt


αt−1


xt−1,





1 −
αt
αt−1





I





,
(5)


where α1:T ∈(0, 1]T is a predefined variance schedule, and
the covariance matrix is ensured to have positive terms on its
diagonal. Specifically, this parametrization has the property:


q(xt|x0) =


Z


q(x1:t|x0)dx1:(t−1) =


N(xt; √αtx0, (1 −αt)I) ,
(6)


therefore we can write xt as a linear combination of x0 and
a noise variable ϵ.


When we set αT sufficiently close to 0, q(xT |x0) con-
verges to a standard Gaussian for all x0, so it is natural
to set pθ(xT ) := N(0, I). Given that all the conditionals
are modeled as Gaussians with fixed variance, the objective
in Equation (3) can be greatly simplified. In particular, [10]
shows that the following (further simplified) lower bound
provides optimal generative performance:


L(ϵθ) :=


T
X


t=1


Ex0,ϵt


h


∥ϵ(t)


θ (√αtx0 +


√


1 −αtϵt) −ϵt∥2
2
i


,


(7)


where x0 ∼q(x0), ϵt ∼N(0, I), ϵθ = {ϵ(t)


θ }T


t=1 is a set of T
functions, with each ϵ(t)


θ
: X →X having trainable parameters
θ(t).


In practice, these functions are approximated by a neural
network conditioned on the diffusion time t. After the model
is trained, we can generate new samples by first sampling xT
from the known prior pθ(xT ), and then iteratively reversing
the diffusion process, thereby sampling {xT −1 . . . x0}.


In addition, we leveraged the natural ability of DDPMs to
incorporate multimodal conditioning in the generation process,
taking inspiration from [21]–[24]. Specifically, we will use
prompts, i.e., textual descriptions of the anomaly, and negative
prompts, i.e., prompts that guide the image generation “away”
from its concepts. This results in high-quality images that
comply with the given descriptions [25]–[27].


In particular, we opt to utilize an inpainting model, as
demonstrated in [19], [22]. Given an image with a masked re-
gion, inpainting seamlessly fills it with content that harmonizes
with the surrounding image. Although typically employed to
eliminate undesired artifacts, the inpainting process ensures
that the masked area incorporates the provided prompt, effec-
tively merging textual and visual content.


B. The DIAG pipeline


To generate an anomalous image ia, the process starts by
sampling a random negative image, an anomaly description,
and a mask, forming the triplet (in, da, ma). Instead of directly
operating on the image pixels using DDPM, we use a Latent
Diffusion Model (LDM) to work in a lower-dimensional latent
space [22]. Thus, the above information will be fed to a text-
conditioned LDM to perform inpainting on image in using the
mask ma.


The anomaly description da guides the generation, filling
the masked region of in with an anomaly that complies with
the prompt. To generate images resembling real anomalous
samples, domain knowledge from industrial experts is ex-
ploited, providing textual descriptions of the potential anoma-
lies’ type, shape, and spatial information.


The LDM is then conditioned on this information to in-
paint plausible anomalies on defect-free samples. Formally,
given pictures of defect-free (negative) samples In, domain
experts will provide textual descriptions Da of what different


anomalies may look like. At the same time, regions where
these anomalies may appear on the defect-free samples will
be designated. We define this set of regions as a set of binary
masks Ma of possible anomalies, shapes, and locations. The
result of this operation is ia, an anomalous version of in,
where an anomaly has been inpainted in the masked region
ma. Due to the stochastic nature of LDMs, this process can
be repeated multiple times to generate an augmented set of
anomalous sample images Ia. Finally, the set Ia can be used
as data augmentation for training anomaly detection models,
as presented in the following section.


C. Anomaly detection task


We approach the anomaly detection problem as a bi-
nary classification problem, where the objective is to predict
whether a sample belongs to one of two classes. Specifically,
we utilized a ResNet-50 [28] backbone trained with a binary
cross-entropy loss function denoted as LBCE. The binary cross-
entropy loss measures the dissimilarity between the predicted
probability distribution and the actual distribution of the labels.
Mathematically, it is defined as:


LBCE(y, ˆy) = −1


N


N
X


i=1


[yi log(ˆyi) + (1 −yi) log(1 −ˆyi)] ,


(8)
where, y represents the ground truth labels, ˆy represents the
predicted probabilities, and N is the number of samples. In
detail, yi denotes the true label for sample i, which can be
either 0 or 1, while ˆyi signifies the predicted probability that
sample i belongs to class 1.


IV. EXPERIMENTS


In this section, we show the efficacy of our data augmen-
tation approach for defect detection from a quantitative and
qualitative point of view.


A. Experiment setup


Datasets: We use the Kolektor Surface-Defect Dataset
2 (KSDD2) [13], one of the most recent, complex, and real-
world surface defect detection datasets. This dataset comprises
246 positive and 2085 negative images in the training set
and 110 positive and 894 negative images in the testing
set. Positive images are images with visible defects, such as
scratches, spots, and surface imperfections.


Since the images have different dimensions, we standardize
the dataset resolution, resizing all the images to 224 × 632
pixels while keeping the number of normal and anomalous
samples unchanged.


Evaluation metrics: The anomaly detection performance
was evaluated based on Average Precision (AP), Precision, and
Recall, following the evaluation protocol defined in [18].


Additionally, to evaluate the visual similarity between gen-
erated images and the original dataset images, we employ the
Fr´echet Inception Distance (FID) [29], a popular metric in the
image generation field which computes the distance between
the distribution of two sets of images. More specifically, the


Fr´echet distance calculates distance d(., .) between a Gaussian
with mean (m, C) obtained from p(.) and a Gaussian with
mean (mw, Cw) obtained by pw(.), where pw(.) represents
real world data and p(.) represents generated data. In practice,
these distributions are two sets of data: the “world” data (i.e.,
the images in a dataset) and the “generated” data (i.e., the
generated images). These sets are then fed to an Inception
model pre-trained on ImageNet to extract deep features from
each sample of the distributions. The resulting two sets of
features represent the Gaussians with mean (mw, Cw) and
(m, C) for the “world” and “generated” data, respectively.
Specifically, [29] shows that a lower FID score matches a
human’s higher perceived visual similarity (a lower perceptual
distance), meaning that similar sets of images will have a lower
FID than dissimilar sets. Formally, the FID score is:


d((m, C), (mw, Cw)) = ||m−mw||2


2+T(C+Cw−2(CCw)
1
2 )
(9)
where T refers to the trace linear algebra operation.


B. Implementation details


In this section, we specify all the implementation details for
reproducibility. All training and inferences were conducted on
an NVIDIA RTX 3090 GPU.


Inpainting via DIAG: We use the pre-trained imple-
mentation of SDXL [27] from Diffusers [30] as our text-
conditioned LDM. In particular, SDXL shows drastically
improved performance compared to the previous versions
of Stable Diffusion [22] and achieves results comparable to
commercial state-of-the-art image generators.


Following the procedure outlined in Section III-B, we
use the negative images of KSDD2 as the set In. As the
set of anomaly descriptions Da, we used the prompts
“white marks on the wall” and “copper metal
scratches”.
Instead,
“smooth, plain, black,
dark, shadow” were used as a negative prompt to
improve
the
performance
further.
These
prompts
were
selected through a human-in-the-loop iterative pipeline, until
the resulting images resembled plausible anomalies. We used
the segmentation masks of positive samples in the KSDD2
dataset to simulate the domain experts’ definition of plausible
anomalous regions.


Then, these data are fed to the pre-trained SDXL model to
perform inpainting on the negative images in a training-free
process, generating the set of augmented anomalous images
Ia as described in Section III-B.


Finally, the generated images Ia are added to the training
set, which will be used to train the anomaly detection model.


ResNet-50 training and testing: For a fair comparison
with [18], we use the same PyTorch implementation of the
ResNet-50 [28] as our anomaly detection model, in which
we substitute the fully connected layers after the backbone
to make it a binary classifier. The network is trained for 50
epochs with Adam [31] as an optimizer, a learning rate of
0.0001, and a batch size of 32.
To maintain consistency with the training and evaluation
procedures of KSDD2, our setup is the same as presented


TABLE I
RESULTS BETWEEN MEMSEG, IN&OUT AND DIAG WHEN no
ANOMALOUS SAMPLES ARE AVAILABLE. IN BOLD, THE BEST RESULTS.


UNDERLINED, THE SECOND BEST.


Model
Naug
AP ↑
Precision ↑
Recall ↑


MemSeg [15]
80
.514
.733
.436
MemSeg [15]
100
.388
.633
.432
MemSeg [15]
120
.511
.683
.470


In&Out [18]
80
.556
.530
.655
In&Out [18]
100
.626
.742
.568
In&Out [18]
120
.536
.699
.534


DIAG (ours)
80
.769
.851
.673
DIAG (ours)
100
.801
.924
.664
DIAG (ours)
120
.739
.944
.609


in [13], [18], where only the images and ground truth labels are
used to train the model. For our comparison, we use the official
code of In&Out [18] to fine-tune a DDPM in the full-shot
scenario (on all the positive images of the KSDD2 dataset)
and generate their augmented images. Likewise, we follow
the procedure of MemSeg [15] to generate the “per-region”
augmented images. Finally, we generate DIAG augmented
images, following the inpainting methodology outlined in
Section III. The set of images used for training changes
depending on the experiment and the pipelines being tested,
but in general, it can be seen as a combination of the original
negative images In, an optional set Ip of original positive
images, and the set of generated positive images Ia.


C. Quantitative results


Zero-shot data augmentation: Here, we emulate the
situation where no original positive samples are available in
the training set. This scenario makes generating augmented
positive samples necessary and restricts the users to augmen-
tation procedures that do not rely on positive images. To do
this, we build the set of augmented anomalous images Ia by
generating Naug augmented positive samples with different
pipelines, i.e., MemSeg [15], In&Out [18] and DIAG. Then,
we train a ResNet-50 on a dataset that includes the original
negative samples In and the augmented positive samples Ia.
Finally, we evaluate the model on the original test set.


Table I reports the comparison between the models trained
with MemSeg, In&Out, and DIAG augmented data at different
values of Naug. As we can see, our proposed method achieves
the highest AP (.801), recorded at 100 augmented images,
while also resulting in a consistently higher AP when com-
pared to the MemSeg and In&Out pipelines. These impressive
results highlight how, through domain expertise in the form of
anomaly descriptions and segmentation masks, it is possible
to generate in-distribution images able to meaningfully guide
an anomaly detection network, even in a complicated scenario
where no real anomalous data is available.


Surprisingly, the DIAG performance with Naug = 120
augmented images is lower than using a smaller number of
augmented images. We hypothesize this is due to the stochastic
nature of the LDMs image generation. While it allows the


TABLE II
RESULTS BETWEEN MEMSEG, IN&OUT AND DIAG WHEN all THE
ANOMALOUS SAMPLES ARE AVAILABLE. IN BOLD, THE BEST RESULTS.


UNDERLINED, THE SECOND BEST.


Model
Naug
AP ↑
Precision ↑
Recall ↑


MemSeg [15]
80
.744
.851
.691
MemSeg [15]
100
.774
.814
.752
MemSeg [15]
120
.734
.772
.707


In&Out [18]
80
.747
.764
.734
In&Out [18]
100
.775
.868
.720
In&Out [18]
120
.782
.906
.689


DIAG (ours)
80
.869
.912
.755
DIAG (ours)
100
.911
.978
.800
DIAG (ours)
120
.924
.896
.864


generation of various images given the same guidance, it can
also lower, in some cases, the predictability of the quality of
the generated samples, which sometimes may not faithfully
comply with the prompt. Future works will focus on studying
quality consistency in the image generation pipeline.


Full-shot data augmentation: To showcase DIAG as
a general data augmentation technique, we also explore the
scenario where real positive samples are available in the
training set. To this aim, we include all the 246 real positive
samples Ip in the training set, together with the real negative
images In and the Naug augmented positive images Ia.


As we can see from Table II, DIAG achieves the highest
average AP yet (.924), surpassing the .782 set by the previous
state-of-the-art data augmentation pipeline [18]. When com-
paring these results to the ones obtained in the “zero-shot data
augmentation” scenario, it is clear how more in-distribution
images improve model performance during training. This is
highlighted by the improvement in performance of all the
models when adding the real positive images Ip to the training
set. At the same time, the inclusion of DIAG augmented
images allows the model to explore the anomaly distribution
further, resulting in the difference in performance between the
different data augmentation pipelines.


D. Qualitative results


The main goal of our data augmentation pipeline is to
generate in-distribution synthetic positive images, meaning
images that closely resemble the real ones. Figure 2 shows
qualitative results. It’s evident that the images produced by
DIAG are markedly more realistic compared to those gener-
ated by MemSeg [15] and In&Out [18].


In addition, we provide a numeric evaluation of the sim-
ilarity between the generated images and the real ones by
employing FID [29]. It is worth noting that due to the limited
number of anomalous images in the original dataset, we are
forced to calculate FID on a different network layer, precisely
the second max pooling layer. This is a common procedure in
cases where the number of images is low, as the calculation
requires the number of samples (images) to be higher than the
number of features. Note that this only changes the magnitude
of the values obtained, not the metric’s general behavior. In


Fig. 2. First row displays some negative samples from the KSDD2 dataset. Instead, the second row shows some images of positive samples from the same
dataset. In the third row, we show the MemSeg-generated defect samples. The fourth row shows In&Out generated defect samples. Lastly, the final row
showcases images generated with DIAG. Notably, the defect images that DIAG generated are more realistic and in-distribution.


TABLE III
FID SCORES BETWEEN THE REAL POSITIVE IMAGES OF KSDD2 AND THE


IMAGES GENERATED BY MEMSEG, IN&OUT AND DIAG. THE SCORES
ARE CALCULATED USING THE FIRST AND SECOND MAX POOLING LAYERS


OF THE INCEPTION NETWORK, HAVING 64 AND 192 FEATURES,


RESPECTIVELY. IN BOLD, THE BEST RESULTS.


Augmentation procedure
FID 64 ↓
FID 192 ↓


MemSeg [15]
0.834
4.376
DDPM [18]
0.334
1.520
DIAG (ours)
0.096
0.411


the specific case of KSDD2, we choose the first and second
max-pooling layers with 64 and 192 features, respectively.
Specifically, we compare the images generated with MemSeg,
In&Out, and DIAG with the ones available in the KSDD2
dataset and compute the FID scores between the positive
images of the KSDD2 and the previously mentioned sets of
augmented images.


The results, reported in Table III, highlight how DIAG can
generate images that are very similar to the ones originally
present in the dataset, resulting in the lowest FID out of all
the other methodologies.


Another interesting observation is how both the generative-
model-based procedures (DDPM and DIAG) result in images
that are more in-distribution (lower FID) than the “per-region”


augmentation techniques such as MemSeg, which records the
highest FID out of all the tested methodologies.


V. CONCLUSIONS
This work presents DIAG, a novel data augmentation
pipeline that leverages language-conditioned Latent Diffusion
Models to produce training-free positive images for enhancing
the performance of a surface defect detection model. We
introduced domain experts in the generation pipeline, asking
them to describe with textual prompts how a defect should
look and where it can be localized. Then, we adopt a pre-
trained LDM to generate defective images and train a binary
classifier for isolating the anomalous images. We focus our
experiments on the KSDD2 dataset and establish ourselves as
the new state-of-the-art data augmentation pipeline, surpassing
previous approaches in both the zero-shot and full-shot data
augmentation scenarios with an AP of .801 and .924, respec-
tively. These results highlight the potential of in-distribution
data augmentation in the anomaly detection field, where
training-free generative model pipelines such as DIAG can
provide meaningful data for downstream classification, making
them appealing solutions in scenarios where real anomalous
data is difficult to collect or unavailable. These promising
results promote further exploration across various datasets,
particularly investigating how robust the image generation is
compared to noisy textual prompts.


REFERENCES


[1] T. Wang, Y. Chen, M. Qiao, and H. Snoussi, “A fast and robust


convolutional neural network-based defect detection model in product
quality control,” The International Journal of Advanced Manufacturing
Technology, vol. 94, pp. 3465–3471, 2018.
[2] C. S. Tsang, H. Y. Ngan, and G. K. Pang, “Fabric inspection based on


the elo rating method,” Pattern Recognition, vol. 51, pp. 378–394, 2016.
[3] S. H. Hanzaei, A. Afshar, and F. Barazandeh, “Automatic detection and


classification of the ceramic tiles’ surface defects,” Pattern Recognition,
vol. 66, pp. 174–189, 2017.
[4] L. Capogrosso, F. Cunico, D. S. Cheng, F. Fummi, and M. Cristani,


“A machine learning-oriented survey on tiny machine learning,” IEEE
Access, 2024.
[5] H. Deng and X. Li, “Anomaly detection via reverse distillation from


one-class embedding,” in IEEE/CVF Conference on Computer Vision
and Pattern Recognition (CVPR), 2022.
[6] K. Roth, L. Pemula, J. Zepeda, B. Sch¨olkopf, T. Brox, and P. Gehler,


“Towards total recall in industrial anomaly detection,” in IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR), 2022,
pp. 14 318–14 328.
[7] M. Rudolph, B. Wandt, and B. Rosenhahn, “Same same but differnet:


Semi-supervised defect detection with normalizing flows,” in Winter
Conference on Applications of Computer Vision (WACV), 2021.
[8] Y. Song, T. Wang, P. Cai, S. K. Mondal, and J. P. Sahoo, “A compre-


hensive survey of few-shot learning: Evolution, applications, challenges,
and opportunities,” ACM Computing Surveys, vol. 55, no. 13s, pp. 1–40,
2023.
[9] Y. Chen, Y. Ding, F. Zhao, E. Zhang, Z. Wu, and L. Shao, “Surface


defect detection methods for industrial products: A review,” Applied
Sciences, vol. 11, no. 16, p. 7657, 2021.
[10] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,”


Advances in Neural Information Processing Systems (NeurIPS), vol. 33,
pp. 6840–6851, 2020.
[11] X. Tao, D. Zhang, W. Ma, Z. Hou, Z. Lu, and C. Adak, “Unsupervised


anomaly detection for surface defects with dual-siamese network,” IEEE
Transactions on Industrial Informatics, vol. 18, no. 11, pp. 7707–7717,
2022.
[12] C. Luan, R. Cui, L. Sun, and Z. Lin, “A siamese network utilizing image


structural differences for cross-category defect detection,” in 2020 IEEE
International Conference on Image Processing (ICIP).
IEEE, 2020.
[13] J. Boˇziˇc, D. Tabernik, and D. Skoˇcaj, “Mixed supervision for surface-


defect detection: From weakly to fully supervised learning,” Computers
in Industry, vol. 129, p. 103459, 2021.
[14] T. Defard, A. Setkov, A. Loesch, and R. Audigier, “Padim: a patch dis-


tribution modeling framework for anomaly detection and localization,”
in International Conference on Pattern Recognition (ICPR), 2021.
[15] M. Yang, P. Wu, and H. Feng, “Memseg: A semi-supervised method for


image surface defect detection using differences and commonalities,”
Engineering Applications of Artificial Intelligence, vol. 119, p. 105835,
2023.
[16] V. Zavrtanik, M. Kristan, and D. Skoˇcaj, “Draem-a discriminatively


trained reconstruction embedding for surface anomaly detection,” in
IEEE/CVF International Conference on Computer Vision (ICCV), 2021.
[17] H. Zhang, Z. Wu, Z. Wang, Z. Chen, and Y.-G. Jiang, “Prototypical


residual networks for anomaly detection and localization,” in IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR), 2023.
[18] L. Capogrosso, F. Girella, F. Taioli, M. D. Chiara, M. Aqeel, F. Fummi,


F. Setti, and M. Cristani, “Diffusion-based image generation for in-
distribution data augmentation in surface defect detection,” arXiv
preprint arXiv:2406.00501, 2024.
[19] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli,


“Deep unsupervised learning using nonequilibrium thermodynamics,”
in International Conference on Machine Learning (ICML), 2015.
[20] Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and


B. Poole, “Score-based generative modeling through stochastic differen-
tial equations,” in International Conference on Learning Representations
(ICLR), 2020.
[21] J. Ho and T. Salimans, “Classifier-free diffusion guidance,” arXiv


preprint arXiv:2207.12598, 2022.
[22] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, “High-


resolution image synthesis with latent diffusion models,” in IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR), 2022.


[23] L. Zhang, A. Rao, and M. Agrawala, “Adding conditional control to


text-to-image diffusion models,” in IEEE/CVF International Conference
on Computer Vision (ICCV), 2023, pp. 3836–3847.
[24] L. Capogrosso, A. Mascolini, F. Girella, G. Skenderi, S. Gaiardelli,


N. Dall’Ora, F. Ponzio, E. Fraccaroli, S. Di Cataldo, S. Vinco et al.,
“Neuro-symbolic empowered denoising diffusion probabilistic models
for real-time anomaly detection in industry 4.0: Wild-and-crazy-idea
paper,” in 2023 Forum on Specification & Design Languages (FDL).
IEEE, 2023, pp. 1–4.
[25] C. Saharia, W. Chan, S. Saxena, L. Li, J. Whang, E. L. Denton,


K. Ghasemipour, R. Gontijo Lopes, B. Karagol Ayan, T. Salimans
et al., “Photorealistic text-to-image diffusion models with deep language
understanding,” Advances in Neural Information Processing Systems
(NeurIPS), vol. 35, pp. 36 479–36 494, 2022.
[26] A. Ramesh, P. Dhariwal, A. Nichol, C. Chu, and M. Chen, “Hierarchical


text-conditional image generation with clip latents. arxiv 2022,” arXiv
preprint arXiv:2204.06125, 2022.
[27] D. Podell, Z. English, K. Lacey, A. Blattmann, T. Dockhorn, J. M¨uller,


J. Penna, and R. Rombach, “Sdxl: Improving latent diffusion models
for high-resolution image synthesis,” arXiv preprint arXiv:2307.01952,
2023.
[28] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image


recognition,” in IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), 2016.
[29] M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter,


“GANs trained by a two time-scale update rule converge to a local
nash equilibrium,” Advances in Neural Information Processing Systems
(NeurIPS), vol. 30, 2017.
[30] P. von Platen, S. Patil, A. Lozhkov, P. Cuenca, N. Lambert, K. Rasul,


M. Davaadorj, and T. Wolf, “Diffusers: State-of-the-art diffusion mod-
els,” https://github.com/huggingface/diffusers, 2022.
[31] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,”


arXiv preprint arXiv:1412.6980, 2014.
