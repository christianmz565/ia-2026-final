LBM: Latent Bridge Matching for Fast Image-to-Image Translation


Cl´ement Chadebec


Jasper Research


Onur Tasar
Jasper Research


Sanjeev Sreetharan


Jasper Research


Benjamin Aubin
Jasper Research


Original


Figure 1. Relighted images using Latent Bridge Matching (LBM) and 1 neural function evaluation (NFE).


Abstract


In this paper, we introduce Latent Bridge Matching (LBM),
a new, versatile and scalable method that relies on Bridge
Matching in a latent space to achieve fast image-to-image
translation. We show that the method can reach state-of-
the-art results for various image-to-image tasks using only
a single inference step. In addition to its efficiency, we also
demonstrate the versatility of the method across different
image translation tasks such as object removal, normal and
depth estimation, and object relighting. We also derive a
conditional framework of LBM and demonstrate its effec-
tiveness by tackling the tasks of controllable image relight-
ing and shadow generation. We provide an implementation
at https://github.com/gojasper/LBM.


1. Introduction


Image translation is a task that consists of mapping an im-
age from a source domain to a target domain. It can be for-


mulated as a transport problem where the goal is to find a
mapping that translates samples from the source domain to
the target domain [63]. This field contains a wide range of
tasks such as object removal [88], semantic image synthesis
[64], style transfer [21, 120], image harmonization [9, 112]
or image segmentation [40, 118].


Diffusion models (DM) [28, 83, 84] are a type of gen-
erative model that learns a denoising mechanism that can
be used to generate new samples from a Gaussian noise.
These models appear very well suited for image synthesis
[14, 61, 67, 73] and can be conditioned with respect to var-
ious types of inputs such as text [14, 16, 29, 61, 66, 67, 73]
where they demonstrate remarkable performance. In the
particular context of image-to-image translation, the con-
ditional setting allows to build a diffusion model condi-
tioned with source images such as low-resolution images
[73], depth maps, normal maps or edges [59, 111] and gen-
erate images belonging to the target domain. While they
demonstrate strong results, their intrinsic iterative genera-
tion process hinders their usability for real-time applica-


1


arXiv:2503.07535v2  [cs.CV]  22 Aug 2025


tions. Recently, several works have been proposed to ac-
celerate the sampling process of DM through more efficient
solvers [53, 54, 113, 116] or via distillation [31, 46, 51, 56,
57, 71, 76–78, 85, 97, 102]. However, despite revealing
promising results, most of these methods are limited to text-
to-image or struggle to achieve satisfactory one-step gener-
ation.


Drawing inspiration from diffusion models, bridge
matching and flow models have been proposed and aim
to find transport maps between two distributions using
Stochastic Differential Equations (SDEs) or Ordinary Dif-
ferential Equations (ODEs). The key difference from diffu-
sion models is that they do not involve any noising mech-
anism and can be applied to any pair of distributions. The
main idea behind flow matching [1, 47, 49] (resp. bridge
matching [65, 81]) is to define deterministic (resp. stochas-
tic) interpolants between pairs of samples from the source
and target distributions and estimate the drift of the associ-
ated ODE (resp. SDE) using a denoiser model [2]. While
there exist some works applying flow matching to image-to-
image translation [17, 24, 58], the usability, scalability, and
efficiency of their stochastic variant remain an open ques-
tion. It’s worth noting that [48] previously applied bridge
matching to super-resolution and inpainting tasks, though
their approach was limited to low-resolution images.


In this paper, we aim to bridge this gap by introduc-
ing Latent Bridge Matching (LBM), a novel and scalable
method based on bridge matching able to achieve 1 step in-
ference for various image translation tasks. The main con-
tributions of this paper are as follows:
• We propose LBM, a novel, versatile and scalable method
based on bridge matching that shows to be very effective
for various image-to-image tasks even for high resolution
images.
• We show that our method can either compete or achieve
state-of-the-art performance for object-removal, depth
and surface estimation as well as object relighting. In
particular, it outperforms both diffusion-based methods
requiring multiple sampling steps as well as flow match-
ing models.
• We also derive a conditional framework of the method
and apply it to controllable object relighting and shadow
generation.
• Finally, we conduct an extensive ablation study to un-
derstand the impact of the different components of our
method.


2. Related works


Diffusion models are generative models that consist in ar-
tificially adding noise to samples drawn from a given dis-
tribution according to a pre-defined noising mechanism
[28, 83, 84]. This process is such that the final data distri-
bution is roughly equivalent to Gaussian noise. A denoiser


model is then trained to denoise the corrupted samples such
that at inference time, the model can be used to iteratively
generate samples from pure Gaussian noise. These models
can also be conditioned with respect to various modalities
such as text [14, 16, 29, 61, 66, 67, 73], images [73], depth
maps, edges or poses [59, 111] to further guide the genera-
tion process. Despite their success, these models are limited
by their intrinsic iterative generation process that requires
multiple evaluations of a potentially very computationally
expensive neural network.


Various methods were then proposed in the literature to
accelerate the sampling process of diffusion models by re-
ducing the number of denoising steps required to generate
new samples at inference time. The research has evolved
along two main paths. First, more effective solvers were
proposed [53, 54, 113, 116] but these methods still require
quite a few steps to generate satisfying samples. Second,
many works explored distillation methods [27], training stu-
dent networks to approximate the teacher denoiser’s gener-
ation in fewer steps [31, 43, 51, 55–57, 76, 102, 117]. These
approaches were further enriched with adversarial training
[46, 71, 77, 78, 97, 97], distribution matching [102] or both
[8, 103]. While these approaches show very promising re-
sults for text-to-image, they remain specifically tailored to
this task or fail to achieve single-step generation.


Driven by the impressive performance of flow-based
models for text-to-image [16], several works have started
to extend the applicability of flow matching to other tasks.
These models were for instance adapted to the context of
super-resolution [17, 58], depth estimation [24], video gen-
eration [12], audio generation [44], image editing [33] as
well as model distillation [51]. However, its stochastic vari-
ant (bridge matching) has seen far less traction and has
mainly been used in [48] for image restoration and image
inpainting on low resolution images. Hence, it remains un-
clear if such an approach would scale to high resolution im-
ages or transfer efficiently to other tasks since it bridges dis-
tributions in the pixel space.


3. Proposed method


In this section, we detail Latent Bridge Matching (LBM),
the proposed method that is based on the bridge matching
framework.


3.1. Bridge matching


Let π0 and π1 be a pair of distributions such that we have ac-
cess to samples from both distributions (x0, x1) ∼π0 × π1.
The main idea behind bridge matching is to find a trans-
port map from π0 to π1 [2, 50, 65, 81] so one may ul-
timately sample from π1 using samples from π0. To do
so, given (x0, x1) ∼π0 × π1, we build a stochastic inter-
polant xt such that the conditional distribution of xt given
(x0, x1) (π(xt|x0, x1)) is essentially a Brownian motion


2


(also known as Brownian bridge).


xt = (1 −t)x0 + tx1 + σ


p


t(1 −t)ϵ ,
(1)


where ϵ ∼N(0, I), σ ≥0 and t ∈[0, 1]. Notably, if
one further sets σ = 0, one may retrieve the flow match-
ing formulation [2, 47, 49] which can be considered as the
zero-noise limit of bridge matching. Hence, the evolution in
time of xt is given by the following Stochastic Differential
Equation (SDE):


dxt = (x1 −xt)


1 −t
dt + σdBt ,
(2)


where v(xt, t) = (x1 −xt)/(1 −t) is called the drift of the
SDE. In order to use Eq. (2) to sample from π1 using π0, one
needs to ensure that the distribution of xt (πt) is Markov
and so does not depend on x1. In practice, a Markovian
projection is performed and typically consists of regressing
over the drift of the SDE using a neural network:


Et,x0,x1


h


∥(x1 −xt)/(1 −t) −vθ(xt, t)∥2i


.
(3)


Finally, the estimated drift function vθ can be integrated into
standard SDE solvers to solve Eq. (2) to generate samples
that follow π1 from initial samples drawn from π0.


3.2. Latent bridge matching


In our case, since we want the model to handle high reso-
lution images and to have a scalable method, we propose to
rely on a latent bridge matching approach. In such a case,
the samples (x0, x1) ∼π0 × π1 are first embedded into a
latent space using a pre-trained model such as a Variational
Autoencoder (VAE) [39] in a similar fashion to [73]. Let us
denote z0 and z1 as the latents associated with the samples
x0 and x1. Using the same formulation as in the previous
section, this leads to the following objective function:


LLBM = E


h


∥(E(x1) −E(xt))/(1 −t) −vθ(zt, t)∥2i


,
(4)
where E is the encoder of the VAE and zt is given by


zt = z0(1 −t) + z1t + σ


p


t(1 −t)ϵ ,
(5)


where z0 = E(x0), z1 = E(x1), ϵ ∼N(0, I) and σ ≥0.
At inference time, one may sample from the distribution π1
using samples from π0 by first drawing a sample from π0,
mapping it to the latent space, solving the SDE in Eq. (2)
using a standard SDE solver and then mapping the latent
back to the image space using the decoder of the VAE. This
approach has the benefit of drastically reducing the compu-
tational cost of the method by reducing the dimensionality
of the data and so allows the training of models that can
scale to high dimensional data such as high resolution im-
ages. Note that computing the latents associated with any


samples from π0 or π1 can be done before training. In a sim-
ilar fashion to what was proposed for diffusion models, one
may derive a conditional setting of LBM. In such a case, in
addition to the pairing (x0, x1), an additional conditioning
variable c is introduced and will further guide the genera-
tion process. Hence, the drift function approximator vθ is
conditioned with respect to c so that vθ(zt, t, c) depends on
the conditioning variable c as well.


3.3. Training


Let us assume we have access to two distributions of images
π0 and π1 and we want to transport samples from π0 to π1.
The training procedure is as follows. First, we draw a pair
of samples (x0, x1) ∼π0 × π1. Those samples are then en-
coded into the latent space using a pre-trained VAE giving
the corresponding latents z0 and z1. A timestep t is drawn
from π(t), the timestep distribution and a noisy sample zt
is created using Eq. (5). This sample is then passed to the
denoiser vθ(zt, t) which is additionally conditioned with re-
spect to the timestep t and predicts the drift. Notably, one
may easily retreive the corresponding predicted latent bz1 for
the predicted drift using


bz1 = (1 −t) · vθ(zt, t) + zt.
(6)


During training, we also introduce a pixel loss Lpixel the in-
fluence of which is discussed in Sec. 4.5. The loss consists
of decoding the estimated target latent bx1 = D(bz1) where
D is the decoder of the VAE and comparing it to the real
target image x1. Several choices of loss functions are pos-
sible such as L1, L2 or LPIPS [114]. We found that LPIPS
works well in practice and speeds up domain shift. In or-
der to scale with the image size, we put in place a random
cropping strategy and only compute the loss on a patch if
the image size is larger than a certain threshold. This limits
the memory footprint of the model so it does not become a
burden to the training efficiency. The final objective can be
summarized as follows:


L = LLBM(E(x0), E(x1)) + λ · Lpixel(bx1, x1) .
(7)


We provide in Fig. 2 a scheme of the training procedure of
the proposed method in the conditional setting. For illustra-
tion purposes, we elect the context of controllable shadow
generation where the generation is further conditioned with
respect to a light map c indicating the position of a light
source. In this setting, π0 corresponds to the distribution of
latents associated with images without shadows while π1 is
the distribution of latents associated with images with shad-
ows. In practice, the conditioning variable c can be injected
into the denoiser vθ by concatenating the latent zt along the
channel dimension.


3.4. Timestep sampling


One key aspect of the proposed method also relies on the
choice of the timestep distribution π(t). In several works


3


Figure 2. Training procedure for a conditional latent bridge matching model in the context of controllable shadow generation.


focusing on accelerating the sampling of diffusion mod-
els, it was noted that only selecting a few timesteps during
training may be beneficial at inference time [8, 56, 78]. In
particular, training the model to denoise inputs at the same
timesteps used during inference proved to be highly effec-
tive for model distillation [8, 46, 76, 78]. We follow this ap-
proach and propose to only use 4 equally spaced timesteps
during training and ensure that these timesteps are the ones
used at inference. Notably, this choice limits the maximum
number of inference steps to only 4. This is discussed in
depth in Sec. 4.5. Note that the proposed framework would
also apply to other distributions such as the uniform or logit-
normal distribution.


4. Experiments


In this section, we validate our method on 6 different image-
to-image tasks: object-removal, depth and surface estima-
tion, object relighting with respect to a given background
image or light conditions as well as shadow generation. Ad-
ditionally, we also provide a qualitative overview of how
our method performs for image restoration in the appen-
dices. Finally, we also ablate the main components of the
proposed method such as the choice of the timestep distri-
bution, the loss function, the number of inference steps and
the choice of σ. In the following, unless stated otherwise,
we use a latent approach and so embed the source and tar-
get images in a latent space using a VAE. The parametrized
drift function vθ is a U-Net [74] initialized with the weights
of the pre-trained text-to-image model SDXL [66] and we
train the full U-Net using 2 H100 GPUs.


4.1. Object-removal


The first task we consider consists of removing objects from
an image the position of which are specified with a mask.
For this setting, π0 corresponds to the distribution of latents
associated with the masked images while π1 is the distribu-


tion of latents associated with the images without the ob-
jects. We create the masked images by replacing the pixels
in the masked region with uniformly sampled random pix-
els. The model is then trained to find a transport map from
π0 to π1 i.e. a mapping that transports the masked images to
the images without the objects. We train our model for 20k
iterations on a combination of: 1) the RORD train dataset
[75] (composed of paired images with and without objects
and associated masks), 2) a synthetic dataset where we cre-
ated pairs of images with and without objects using the ren-
dering engine Blender1 and 3) in-the-wild images where we
randomly masked an area of the image in a similar fashion
as [89]. In the latter case, since the mask is created ran-
domly, there may not be any object in the masked region
and so the task consists in simply reconstructing the origi-
nal image. This allows the model to handle cases where the
mask does not contain any object at inference time without
compromising the quality of the generation. See the appen-
dices for all relevant training parameters.


We compare our approach with LAMA [89], SDXL-
Inpainting [73], PowerPaint [121] and Attentive Eraser [88]
and evaluate all the methods on the validation set of RORD
dataset [75] composed of approximately 52k pairs of im-
ages with and without objects. For each image, both fine
semantic masks and coarse masks indicating the location of
the objects to be removed are provided. We compute the
FID score [26], Local FID (computed only on the masked
region) [95], foreground MSE (fMSE), SSIM and PSNR
metrics. As illustrated in Tab. 1, our model is able to out-
perform other approaches for most metrics even when using
a single inference step. The evolution of the performance
with respect to the number of inference steps is further dis-
cussed in Sec. 4.5. We also provide a qualitative comparison
of all the methods considered in Fig. 3. As illustrated, our
model can remove not only the object but also its shadow


1https://www.blender.org


4


Input
Mask
LAMA
PowerPaint
SDXL-Inpainting
Attentive Eraser
Ours


Figure 3. Qualitative results for object-removal on RORD validation dataset [75]. Best viewed zoomed in. Our model uses a single NFE
and is able to successfully remove not only the object but also its shadow. Additional results are provided in the appendices.


as shown in the figure. See the appendices for additional
samples as well as a discussion of the failure cases.


Method (NFE)
FID ↓
Local FID ↓
fMSE ↓
PSNR ↑
SSIM ↑


LAMA (1)
30.03
35.42
1596.71
19.65
54.49
SDXL inp. (50)
39.30
34.47
2976.42
19.04
65.31
PowerPaint (50)
29.83
26.04
2307.49
20.12
63.08
AE (50)
29.70
33.15
2029.04
20.93
65.69


Ours (1)
26.29
27.91
1314.58
22.38
69.06


Table 1. Metrics for object-removal task computed on RORD val-
idation set (52k images) using the coarse semantic masks. Our
method uses a single neural function evaluation (NFE). Best re-
sults are in bold, second best are underlined. The same results
using the fine semantic masks are provided in appendices.


4.2. Surface and depth estimation


Monocular depth and normal estimation are typically chal-
lenging image translation tasks that require the model to
build an understanding of the geometry of a given scene
with a single image. There exist a large number of meth-
ods trying to tackle either monocular depth estimation
[5, 15, 18, 20, 24, 25, 32, 35, 36, 45, 68, 69, 96, 98, 99,
104–107, 109] or normal estimation from a single image
[3, 4, 10, 15, 19, 20, 25, 96, 100, 104]. In this setting, π0 is
the latent distribution of the images while π1 is the distribu-
tion of the latents of the depth maps (resp. normal maps).
We train a model using our framework for both tasks and
provide in appendices any relevant training parameter.


We perform a zero-shot evaluation on commonly used
evaluation datasets such as NYUv2 [82], KITTI [22],
ETH3D [79], ScanNet [11] and DIODE [91] for depth es-
timation and NYUv2, ScanNet, i-Bims [41] and Sintel [6]
for normal estimation. For the latter, we report in Tab. 2 the
mean angular error and the percentage of pixels with an an-
gular error below 11.25 and 30 degrees. As highlighted on
Tab. 2, the method is either able to outperform competitors
or be competitive since it ranks amongst the top three mod-
els for each metric on all datasets. Moreover, our approach


ranks 1.4 on average. We provide in appendices the same
table for depth estimation showing the same tendency since
the model achieves again the best average ranking.


4.3. Image relighting


Setting
Another task we decide to tackle is object relight-
ing which consists of manipulating the appearance of an im-
age by changing the illumination of the scene. This can be
performed by relighting the foreground of an image using a
target background [9, 23, 37, 38, 70, 92, 112], or modifying
an object or the full scene appearance using target lightings
(e.g. high dynamic range (HDR) maps) [13, 34, 42, 108]. In
particular, portrait relighting is a special case of image re-
lighting that has driven strong interest in the past few years
[30, 60, 62, 87, 94, 101, 110, 115, 119].


In this section, we focus on the task aiming at relight-
ing a foreground object according to a given background,
also known as image harmonization. In this case, we set π0
to the encoded source images created by pasting the fore-
ground onto the target background image and π1 is the de-
sired target relighted image.


Dataset creation
This task is quite challenging since
most of the time there exist no such pairs of images i.e. im-
ages with the exact same foreground but on different back-
grounds and so under different light conditions. Since we
do not have access to such data we rely on the following
data creation strategy.


We collect a set of various publicly available and free-to-
use images with saliant foreground and compute the fore-
ground mask for each of them using [118] leading to a set
of images X. Then, given a pair of images x1, x2 ∈X, we
use the foreground of x1 (resp. x2) and the IC-light model
[112] to produce a relighted foreground xfg


1 (resp. xfg
2 ) ac-
cording to the background of x2 (resp. x1). Finally, xfg


1 and
xfg


2 are pasted back onto the original images x1 and x2 to
produce the source images y1 and y2 while x1 and x2 are
used as target images.


5


Method
NYUv2
ScanNet
iBims
Sintel
Avg.
m.↓
11.25◦↑
30.0◦↑
m.↓
11.25◦↑
30.0◦↑
m.↓
11.25◦↑
30.0◦↑
m.↓
11.25◦↑
30.0◦↑
Rank


OASIS
29.2
23.8
60.7
32.8
15.4
52.6
32.6
23.5
57.4
43.1
7.0
35.7
12.3
Omnidata
23.1
45.8
73.6
22.9
47.4
73.2
19.0
62.1
80.1
41.5
11.4
42.0
10.7
EESNU
16.2
58.6
83.5
-
-
-
20.0
58.5
78.2
42.1
11.5
41.2
8.7
GenPercept
18.2
56.3
81.4
17.7
58.3
82.7
18.2
64.0
82.0
37.6
16.2
51.0
7.5
Omnidata V2
17.2
55.5
83.0
16.2
60.2
84.7
18.2
63.9
81.1
40.5
14.7
43.5
7.1
DSINE
16.4
59.6
83.5
16.2
61.0
84.4
17.1
67.4
82.3
34.9
21.5
52.7
4.4
Marigold
20.9
50.5
-
21.3
45.6
-
18.5
64.7
-
-
-
-
9.8
GeoWizard
18.9
50.7
81.5
17.4
53.8
83.5
19.3
63.0
80.3
40.3
12.3
43.5
9.1
StableNormal
18.6
53.5
81.7
17.1
57.4
84.1
18.2
65.0
82.4
36.7
14.1
50.7
7.2
Lotus-D
16.2
59.8
83.9
14.7
64.0
86.1
17.1
66.4
83.0
32.3
22.4
57.0
2.4
Lotus-G
16.5
59.4
83.5
15.1
63.9
85.3
17.2
66.2
82.7
33.6
21.0
53.8
4.1
Diff.-E2E-FT
16.5
60.4
83.1
14.7
66.1
85.1
16.1
69.7
83.9
33.5
22.3
53.5
2.8


Ours
15.5
62.5
84.9
14.1
65.8
87.0
16.9
68.3
82.7
32.2
24.0
58.6
1.4


Table 2. Quantitative results for normal estimation. Our method uses a single NFE. Competitors results are taken from [25]. Best results
are in bold, second best are underlined. We provide the same table for depth estimation in appendices.


Additionally, we also rely on synthetic data created with
the rendering engine Blender. Our synthetic dataset creation
process begins by assembling a diverse collection of 3D ob-
ject and human models, along with HDR images. These el-
ements are then used to render high-quality images. For the
objects, we collect an extensive selection of high-quality 3D
models from BlenderKit2, a platform featuring profession-
ally crafted assets available under a free-to-use license. For
humans, we use a Blender addon3 to generate unique 3D hu-
man models by randomly customizing facial features, body
shapes, poses, hair, and clothing options. In each iteration
of the dataset creation process, we begin by randomly se-
lecting a 3D model. We then randomly select HDR images
to illuminate the foreground object. We render the scene,
and save the image and associated foreground mask giving
x1. We perform the same using another HDR map but with
the same 3D object giving x2. Finally, we can paste the
foreground of x1 on x2 and vice-versa to create the source
images y2 and y1 and use again x1 and x2 as target. Exam-
ple renders from our dataset are shown in Fig. 4.


BG 1
x1
BG 2
x2 (target)
y2 (source)


Figure 4. Sample renders from our synthetic dataset. BG 1 is used
to relight the 3D model and create x1. BG 2 is used to produce
another image with the same 3D model x2 which is used as target.
Finally, the source image y2 is created by pasting the foreground
of x1 on BG 2.


Results
We follow the same approach as described above
to create a test set composed of approximately 10k unseen


2https://www.blenderkit.com
3https://www.humgen3d.com


real images and evaluate the performance of the proposed
method. For this benchmark, we consider INR [9], Harmo-
nizer [37], PCT-Net [23], PIH [92] and IC-light [112]. We
report in Tab. 3 the FID, Local FID, fMSE and PSNR met-
rics computed on the test set. As highlighted in the table,
the method outperforms other competitors for most metrics.
Note that for IC-light since it needs a background image as
conditioning while other methods take as input directly the
composite image, we used the estimated background using
our object removal model proposed in Sec. 4.1 which can
lead to artifacts in the background. In addition, we also
provide qualitative samples for each method in Fig. 6. The
proposed approach appears able to add strong illumination
changes to the foreground object while preserving the back-
ground. Moreover, it is able to remove existing shadows and
reflections so the foreground object appears more realistic.
Finally, we also noted that while IC-light model seems to
degrade the quality of the foreground object (see the last
row of Fig. 6), the proposed approach allows to keep the
foreground object consistent with the input image.


Model
FID ↓
Local FID ↓
fMSE ↓
PSNR ↑


Harmonizer
13.91
14.21
1533.34
23.49
PCT-NET
13.96
14.53
1634.24
23.25
PIH
15.17
15.45
1755.86
22.83
INR Harmonization
13.86
14.65
1480.01
23.49
IC-Light∗
20.88
22.11
1897.19
22.39


Ours
12.79
12.83
1173.02
23.24


∗IC-Light uses backgrounds computed using our object removal model


Table 3. Metrics for image relighting task. Our method uses a
single NFE. Best results are in bold, second best are underlined.


Influence of synthetic data
We ablate the influence of
the additional synthetic data (created with the rendering en-
gine) on the overall model performance. We noticed that the
proportion of synthetic data strongly influences the model
performance. In Fig. 5, we plot the evolution of the FID


6


0.0 0.1
0.3
0.5
0.7
0.9 1.0
Synthetic Data Proportion


13


14


FID


Figure 5. Influence of the synthetic data


score with respect to the proportion of synthetic data in the
training set. Interestingly, the more synthetic data, the bet-
ter the model performance since it clearly helps the model
to learn the lighting conditions on simpler and controlled
scenes. However, we observe that adding too much syn-
thetic data may eventually lead to a performance drop since
the outputs realism is affected.


4.4. Controllable image relighting and shadow gen-
eration


Setting
Finally, we show the effectiveness of our pro-
posed Conditional Latent Bridge Matching model for two
tasks. The first one consists of controllable image relight-
ing where the model is additionally conditioned on a light
map representing the position, color and intensity of the
light sources and must relight the foreground object accord-
ing to these sources. The second one consists of control-
lable shadow generation where the model is conditioned on
a light map representing the position and sharpness of the
light source and must generate a shadow of the foreground
object on the ground. For shadow generation, we build a
2D light map inspired by [80] and [90] that represents the
light information as a gray-scaled image in which each light
source is represented as a mixture of Gaussians the ampli-
tude of which encodes the intensity while the variance rep-
resents the softness. For image relighting, we adapt this
representation by considering RGB light maps incorporat-
ing the color of the light sources.


Dataset creation
Creating a dataset consisting of real im-
ages for controllable relighting or shadow generation typ-
ically demands a costly setup, such as a light stage [62].
Therefore, we propose to rely on a synthetic dataset. For
controllable relighting, we generate a dataset by placing a
randomly selected 3D model at the center of Blender’s coor-
dinate system during each rendering iteration. To illuminate
the scene, we position one to three area lights with varying
colors and light intensities on the surface of the upper hemi-
sphere of a sphere with a fixed radius. We then render the
scene, capturing the desired lighting variations. For shadow
generation, we position a sufficiently large plane beneath
the 3D model to serve as the shadow receiver. We posi-
tion a single area light at a random location, emitting white
light with a variable area light size. The size determines the


sharpness of the shadows.


Results
In Fig. 7, we present the generated outputs for
both tasks under various lighting conditions, including vari-
ations in position, intensity, color, and number of light
sources. As highlighted in the figure, the model is able to
relight the object accordingly even in the context of multiple
light sources. Moreover, it respects the position, the inten-
sity and the color of the sources. An interresting property
of the approach is also that the model is able to remove ex-
isting shadows and reflections present on the original object
and add new ones improving realism.


4.5. Ablation study


In this section, we ablate the different components of our
method. To do so, we consider the object-removal task and
train all the models for 20k iterations on 2 H100 GPUs
unless stated otherwise. The ablated parameters are: the
timestep distribution π(t), the pixel loss weight λ in Eq. (7),
the magnitude of the noise parameter σ in Eq. (5) and the
number of inference steps (NFE).


Influence of σ
First, we ablate the noise parameter σ in
Eq. (5). We consider the same configuration as in Sec. 4.1
and report the FID computed on the RORD validation set
for σ ranging from 0 to 0.2 where σ = 0 corresponds to
flow matching. For the timestep distribution, we consider
a uniform distribution for this ablation. In Fig. 8 (left), we
plot the evolution of the FID according to the number of
inference steps for each considered configuration. The first
observation of such a study is that as expected, the method’s
performance improves as the number of inference steps in-
creases for small enough values of σ. However, if σ is too
large, the performance drops since too much noise is added
when solving Eq. (2) potentially removing too much infor-
mation from the source image. Notably, the method out-
performs flow matching in terms of FID for small σ. This
can be explained by the fact that adding this noise parame-
ter allows the model to reach a wider diversity of samples.
Given a source image, a LBM will indeed solve an SDE
and so generate a different sample each time thanks to its
intrinsic stochastic nature. On the contrary, in flow match-
ing we solve an ODE the solution of which is unique. This
emphasizes the importance of σ in the proposed method and
provides a hint why bridge models may be better suited than
flow models for generative tasks.


Influence of the timestep distribution π(t)
We train a
model using either a uniform distribution π(t) = U(0, 1)
or a distribution focusing on 4 discrete timesteps as we pro-
pose in Sec. 3.4. We set σ = 0.05 for the two settings
and report the FID computed on the RORD validation set in
Fig. 8 (right). Notably, the method outperforms again flow


7


Background
Composite
Harmonizer
PIH
PCT-Net
INR
IC-Light
Ours


Figure 6. Qualitative results for object relighting. The model is able to relight the object according to the provided background and also
remove existing shadows and reflections. See the appendices for more results.


Figure 7. Left: Controllable image relighting. Right: Control-
lable shadow generation. For both tasks, the foreground object is
extracted from the input image using a matting model [118] and
pasted on a white background. The control light map is repre-
sented at the top left of each image where the white square shows
the position of the object. The model is able to relight the ob-
ject and generate realistic shadows according to the light condi-
tions even when using multiple light sources. Moreover, it can
effectively remove existing shadows and reflections present on the
original foreground object.


matching for π(t) set to either a discrete distribution or a
uniform distribution. Interestingly, we observe that in most
cases, using a sharp distribution that focuses on 4 distinct
timesteps leads to better results than using a uniform dis-
tribution when inferring with those specific timesteps. This
is for instance visible by comparing the FID achieved with


1 2
4
8
20
# Inference Steps


24


25


26


27


28


FID


Flow Matching
LBM σ = 0.2
LBM σ = 0.05


LBM σ = 0.02
LBM σ = 0.01
LBM σ = 0.005


(a) LBM vs FM


1
2
4
8
# Inference Steps


24


25


26


27


28


FM - U(0, 1)
FM - U{i/4}i∈{0,...,3}


LBM - U(0, 1)
LBM - U{i/4}i∈{0,...,3}


(b) Influence of π(t)


Figure 8. Influence of the timestep distribution and σ as well as
the number of inference steps. Notably, the proposed LBM model
outperforms flow matching for small enough values of σ using
either a uniform or discrete timestep distribution.


flow matching using either a uniform or discrete timestep
distribution (blue curves). The same behaviour is observed
with LBM as well.
However, using a discrete distribu-
tion limits the number of inference steps to the number of
selected timesteps since we observe a strong performance
drop when inferring with more timesteps (solid lines) while
the performance with a uniform distribution still improves
(dotted lines). In a nutshell, these discrete distributions are
valuable because they concentrate the model’s knowledge
on specific timesteps, thereby improving performance when
these timesteps are used during inference. However, this
comes at the cost of limiting the number of possible infer-
ence steps.


Influence of the Pixel Loss
For this ablation, we vary the
weight λ in Eq. (7) associated with the pixel loss and re-
port in Tab. 4 the metrics. As shown in Tab. 4, using a pixel
loss is clearly beneficial to the model performance. More-
over, it was noted in our experiments that this specific loss


8


Input
1 NFE
2 NFE
4 NFE


Figure 9. Influence of the number of inference steps for depth
and normal estimation as well as image restoration. From left to
right: input image, output using a single neural function evalua-
tions (NFE), 2 NFEs or 4 NFEs. Best viewed zoomed in.


λ
LPIPS ↓
FID ↓
Local FID ↓
fMSE ↓
PSNR ↑


1
24.87
30.21
34.49
1233.99
22.55
5
23.57
26.84
28.94
1281.71
22.55
10
23.29
26.70
28.84
1305.68
22.39
20
23.35
27.09
29.27
1360.02
22.34


Table 4. Influence of the pixel loss weight λ for the object-removal
task.


also speeds up domain shift and allows to get better quality
results.


5. Conclusion


In this paper we introduced Latent Bridge Matching, a new
method based on bridge matching in a latent space scalable
to high-resolution images. We showed that this method is
able to demonstrate strong performances for various image
translation tasks. We carefully ablated the main elements of
the method and underlined the importance of each compo-
nent. A particularly interesting result of this study is that
the stochasticity of the method is beneficial to the model
performance. In particular, it outperforms flow matching
which corresponds to the zero-noise limit of our proposed
framework. A noticeable limitation of the method relies on
the need to have access to existing couplings of images be-
forehand to be able to train the model.


9


References


[1] Michael Albergo and Eric Vanden-Eijnden. Building nor-


malizing flows with stochastic interpolants. In ICLR 2023
Conference, 2023. 2
[2] Michael S Albergo, Nicholas M Boffi, and Eric Vanden-


Eijnden.
Stochastic interpolants: A unifying framework
for flows and diffusions. arXiv preprint arXiv:2303.08797,
2023. 2, 3
[3] Gwangbin Bae and Andrew J Davison. Rethinking induc-


tive biases for surface normal estimation. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 9535–9545, 2024. 5
[4] Gwangbin Bae, Ignas Budvytis, and Roberto Cipolla. Es-


timating and exploiting the aleatoric uncertainty in surface
normal estimation. In Proceedings of the IEEE/CVF In-
ternational Conference on Computer Vision, pages 13137–
13146, 2021. 5
[5] Aleksei Bochkovskii, Ama¨el Delaunoy, Hugo Germain,


Marcel Santos, Yichao Zhou, Stephan R Richter, and
Vladlen Koltun. Depth pro: Sharp monocular metric depth
in less than a second.
arXiv preprint arXiv:2410.02073,
2024. 5
[6] Daniel J Butler, Jonas Wulff, Garrett B Stanley, and


Michael J Black. A naturalistic open source movie for opti-
cal flow evaluation. In Computer Vision–ECCV 2012: 12th
European Conference on Computer Vision, Florence, Italy,
October 7-13, 2012, Proceedings, Part VI 12, pages 611–
625. Springer, 2012. 5
[7] Yohann Cabon, Naila Murray, and Martin Humenberger.


Virtual kitti 2. arXiv e-prints, pages arXiv–2001, 2020. 15
[8] Clement Chadedec, Onur Tasar, Eyal Benaroche, and Ben-


jamin Aubin. Flash diffusion: Accelerating any conditional
diffusion model for few steps image generation. In The 39th
Annual AAAI Conference on Artificial Intelligence, 2024. 2,
4
[9] Jianqi Chen, Yilan Zhang, Zhengxia Zou, Keyan Chen, and


Zhenwei Shi. Dense pixel-to-pixel harmonization via con-
tinuous image representation. IEEE Transactions on Cir-
cuits and Systems for Video Technology, 2023. 1, 5, 6
[10] Weifeng Chen, Shengyi Qian, David Fan, Noriyuki Ko-


jima, Max Hamilton, and Jia Deng. Oasis: A large-scale
dataset for single image 3d in the wild. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 679–688, 2020. 5
[11] Angela Dai, Angel X Chang, Manolis Savva, Maciej Hal-


ber, Thomas Funkhouser, and Matthias Nießner. Scannet:
Richly-annotated 3d reconstructions of indoor scenes. In
Proceedings of the IEEE conference on computer vision
and pattern recognition, pages 5828–5839, 2017. 5, 16
[12] Aram Davtyan, Sepehr Sameni, and Paolo Favaro. Efficient


video prediction via sparsely conditioned flow matching. In
Proceedings of the IEEE/CVF International Conference on
Computer Vision, pages 23263–23274, 2023. 2
[13] Kangle Deng, Timothy Omernick, Alexander Weiss, Deva


Ramanan, Jun-Yan Zhu, Tinghui Zhou, and Maneesh
Agrawala. Flashtex: Fast relightable mesh texturing with


lightcontrolnet. In European Conference on Computer Vi-
sion, pages 90–107. Springer, 2024. 5
[14] Prafulla Dhariwal and Alexander Nichol. Diffusion models


beat gans on image synthesis. Advances in neural informa-
tion processing systems, 34:8780–8794, 2021. 1, 2
[15] Ainaz Eftekhar, Alexander Sax, Jitendra Malik, and Amir


Zamir. Omnidata: A scalable pipeline for making multi-
task mid-level vision datasets from 3d scans. In Proceed-
ings of the IEEE/CVF International Conference on Com-
puter Vision, pages 10786–10796, 2021. 5
[16] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim


Entezari, Jonas M¨uller, Harry Saini, Yam Levi, Dominik
Lorenz, Axel Sauer, Frederic Boesel, et al. Scaling recti-
fied flow transformers for high-resolution image synthesis.
arXiv preprint arXiv:2403.03206, 2024. 1, 2
[17] Johannes S Fischer, Ming Gui, Pingchuan Ma, Nick


Stracke, Stefan A Baumann, and Bj¨orn Ommer.
Boost-
ing latent diffusion with flow matching.
arXiv preprint
arXiv:2312.07360, 2023. 2
[18] Huan Fu, Mingming Gong, Chaohui Wang, Kayhan Bat-


manghelich, and Dacheng Tao.
Deep ordinal regression
network for monocular depth estimation. In Proceedings of
the IEEE conference on computer vision and pattern recog-
nition, pages 2002–2011, 2018. 5
[19] Xiao Fu, Wei Yin, Mu Hu, Kaixuan Wang, Yuexin Ma, Ping


Tan, Shaojie Shen, Dahua Lin, and Xiaoxiao Long. Ge-
owizard: Unleashing the diffusion priors for 3d geometry
estimation from a single image. In European Conference
on Computer Vision, pages 241–258. Springer, 2024. 5
[20] Gonzalo Martin Garcia, Karim Abou Zeid, Christian


Schmidt, Daan de Geus, Alexander Hermans, and Bastian
Leibe. Fine-tuning image-conditional diffusion models is
easier than you think.
arXiv preprint arXiv:2409.11355,
2024. 5
[21] Leon A Gatys, Alexander S Ecker, and Matthias Bethge.


Image style transfer using convolutional neural networks.
In Proceedings of the IEEE conference on computer vision
and pattern recognition, pages 2414–2423, 2016. 1
[22] Andreas Geiger, Philip Lenz, Christoph Stiller, and Raquel


Urtasun. Vision meets robotics: The kitti dataset. The Inter-
national Journal of Robotics Research, 32(11):1231–1237,
2013. 5, 16
[23] Julian Jorge Andrade Guerreiro, Mitsuru Nakazawa, and


Bj¨orn Stenger. Pct-net: Full resolution image harmoniza-
tion using pixel-wise color transformations. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pat-
tern Recognition, pages 5917–5926, 2023. 5, 6
[24] Ming
Gui,
Johannes
Schusterbauer,
Ulrich
Prestel,
Pingchuan Ma, Dmytro Kotovenko, Olga Grebenkova, Ste-
fan Andreas Baumann, Vincent Tao Hu, and Bj¨orn Om-
mer. Depthfm: Fast monocular depth estimation with flow
matching. arXiv preprint arXiv:2403.13788, 2024. 2, 5
[25] Jing He, Haodong Li, Wei Yin, Yixun Liang, Leheng Li,


Kaiqiang Zhou, Hongbo Zhang, Bingbing Liu, and Ying-
Cong Chen.
Lotus: Diffusion-based visual foundation
model for high-quality dense prediction.
arXiv preprint
arXiv:2409.18124, 2024. 5, 6, 17


10


[26] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner,


Bernhard Nessler, and Sepp Hochreiter. Gans trained by a
two time-scale update rule converge to a local nash equilib-
rium. Advances in neural information processing systems,
30, 2017. 4
[27] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean.
Distill-
ing the knowledge in a neural network.
arXiv preprint
arXiv:1503.02531, 2015. 2
[28] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising dif-


fusion probabilistic models. Advances in neural informa-
tion processing systems, 33:6840–6851, 2020. 1, 2
[29] Jonathan Ho, William Chan, Chitwan Saharia, Jay Whang,


Ruiqi Gao, Alexey Gritsenko, Diederik P Kingma, Ben
Poole, Mohammad Norouzi, David J Fleet, et al.
Ima-
gen video: High definition video generation with diffusion
models. arXiv preprint arXiv:2210.02303, 2022. 1, 2
[30] Andrew Hou, Ze Zhang, Michel Sarkis, Ning Bi, Yiying


Tong, and Xiaoming Liu. Towards high fidelity face relight-
ing with realistic shadows. In Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition,
pages 14719–14728, 2021. 5
[31] Yi-Ting Hsiao, Siavash Khodadadeh, Kevin Duarte, Wei-


An Lin, Hui Qu, Mingi Kwon, and Ratheesh Kalarot.
Plug-and-play diffusion distillation. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 13743–13752, 2024. 2
[32] Mu Hu, Wei Yin, Chi Zhang, Zhipeng Cai, Xiaoxiao Long,


Hao Chen, Kaixuan Wang, Gang Yu, Chunhua Shen, and
Shaojie Shen. Metric3d v2: A versatile monocular geomet-
ric foundation model for zero-shot metric depth and surface
normal estimation. arXiv preprint arXiv:2404.15506, 2024.
5
[33] Vincent Tao Hu, Wei Zhang, Meng Tang, Pascal Mettes,


Deli Zhao, and Cees Snoek.
Latent space editing in
transformer-based flow matching.
In Proceedings of the
AAAI Conference on Artificial Intelligence, pages 2247–
2255, 2024. 2
[34] Haian Jin, Yuan Li, Fujun Luan, Yuanbo Xiangli, Sai Bi,


Kai Zhang, Zexiang Xu, Jin Sun, and Noah Snavely. Neural
gaffer: Relighting any object via diffusion. arXiv preprint
arXiv:2406.07520, 2024. 5
[35] O˘guzhan Fatih Kar, Teresa Yeo, Andrei Atanov, and Amir


Zamir. 3d common corruptions and data augmentation. In
Proceedings of the IEEE/CVF Conference on Computer Vi-
sion and Pattern Recognition, pages 18963–18974, 2022.
5
[36] Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Met-


zger, Rodrigo Caye Daudt, and Konrad Schindler.
Re-
purposing diffusion-based image generators for monocular
depth estimation. In Proceedings of the IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition, pages
9492–9502, 2024. 5
[37] Zhanghan Ke, Chunyi Sun, Lei Zhu, Ke Xu, and Ryn-


son WH Lau. Harmonizer: Learning to perform white-box
image and video harmonization. In European Conference
on Computer Vision, pages 690–706. Springer, 2022. 5, 6
[38] Hoon Kim,
Minje Jang,
Wonjun Yoon,
Jisoo Lee,
Donghyun Na, and Sanghyun Woo. Switchlight: Co-design


of physics-driven architecture and pre-training framework
for human portrait relighting.
In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 25096–25106, 2024. 5
[39] Diederik P. Kingma and Max Welling. Auto-encoding vari-


ational bayes. arXiv:1312.6114 [cs, stat], 2014. 3
[40] Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi


Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer
Whitehead, Alexander C Berg, Wan-Yen Lo, et al. Segment
anything. In Proceedings of the IEEE/CVF international
conference on computer vision, pages 4015–4026, 2023. 1
[41] Tobias Koch, Lukas Liebel, Friedrich Fraundorfer, and


Marco Korner. Evaluation of cnn-based single-image depth
estimation methods. In Proceedings of the European Con-
ference on Computer Vision (ECCV) Workshops, pages 0–0,
2018. 5
[42] Peter Kocsis, Julien Philip, Kalyan Sunkavalli, Matthias


Nießner, and Yannick Hold-Geoffroy. Lightit: Illumination
modeling and control for diffusion models. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pat-
tern Recognition, pages 9359–9369, 2024. 5
[43] Jonas Kohler, Albert Pumarola, Edgar Sch¨onfeld, Artsiom


Sanakoyeu, Roshan Sumbaly, Peter Vajda, and Ali Tha-
bet. Imagine flash: Accelerating emu diffusion models with
backward distillation.
arXiv preprint arXiv:2405.05224,
2024. 2
[44] Matthew Le, Apoorv Vyas, Bowen Shi, Brian Karrer, Leda


Sari, Rashel Moritz, Mary Williamson, Vimal Manohar,
Yossi Adi, Jay Mahadeokar, et al. Voicebox: Text-guided
multilingual universal speech generation at scale. Advances
in neural information processing systems, 36, 2024. 2
[45] Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, and


Il Hong Suh. From big to small: Multi-scale local planar
guidance for monocular depth estimation. arXiv preprint
arXiv:1907.10326, 2019. 5
[46] Shanchuan Lin, Anran Wang, and Xiao Yang.
Sdxl-
lightning:
Progressive adversarial diffusion distillation.
arXiv preprint arXiv:2402.13929, 2024. 2, 4
[47] Yaron Lipman, Ricky TQ Chen, Heli Ben-Hamu, Maxim-


ilian Nickel, and Matthew Le. Flow matching for gener-
ative modeling. In The Eleventh International Conference
on Learning Representations, 2023. 2, 3
[48] Guan-Horng Liu, Arash Vahdat, De-An Huang, Evange-


los A Theodorou, Weili Nie, and Anima Anandkumar. I2sb:
image-to-image schr¨odinger bridge. In Proceedings of the
40th International Conference on Machine Learning, pages
22042–22062, 2023. 2
[49] Xingchao Liu, Chengyue Gong, et al. Flow straight and


fast: Learning to generate and transfer data with rectified
flow. In The Eleventh International Conference on Learn-
ing Representations, 2022. 2, 3
[50] Xingchao Liu, Lemeng Wu, Mao Ye, et al. Let us build


bridges: Understanding and extending diffusion generative
models. In NeurIPS 2022 Workshop on Score-Based Meth-
ods, 2022. 2
[51] Xingchao Liu, Xiwen Zhang, Jianzhu Ma, Jian Peng, et al.


Instaflow: One step is enough for high-quality diffusion-


11


based text-to-image generation.
In The Twelfth Interna-
tional Conference on Learning Representations, 2023. 2
[52] Ilya Loshchilov and Frank Hutter. Decoupled weight de-


cay regularization. In International Conference on Learn-
ing Representations, 2019. 15
[53] Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongx-


uan Li, and Jun Zhu. Dpm-solver: A fast ode solver for
diffusion probabilistic model sampling in around 10 steps.
Advances in Neural Information Processing Systems, 35:
5775–5787, 2022. 2
[54] Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan


Li, and Jun Zhu. Dpm-solver++: Fast solver for guided
sampling of diffusion probabilistic models. arXiv preprint
arXiv:2211.01095, 2022. 2
[55] Eric Luhman and Troy Luhman. Knowledge distillation in


iterative generative models for improved sampling speed.
arXiv preprint arXiv:2101.02388, 2021. 2
[56] Simian Luo, Yiqin Tan, Longbo Huang, Jian Li, and Hang


Zhao.
Latent consistency models:
Synthesizing high-
resolution images with few-step inference. arXiv preprint
arXiv:2310.04378, 2023. 2, 4
[57] Simian Luo, Yiqin Tan, Suraj Patil, Daniel Gu, Patrick


von Platen, Apolin´ario Passos, Longbo Huang, Jian Li, and
Hang Zhao. Lcm-lora: A universal stable-diffusion accel-
eration module. arXiv preprint arXiv:2311.05556, 2023. 2
[58] S´egol`ene Tiffany Martin, Anne Gagneux, Paul Hagemann,


and Gabriele Steidl.
Pnp-flow:
Plug-and-play image
restoration with flow matching. In The Thirteenth Inter-
national Conference on Learning Representations, 2025. 2
[59] Chong Mou, Xintao Wang, Liangbin Xie, Yanze Wu, Jian


Zhang, Zhongang Qi, and Ying Shan. T2i-adapter: Learn-
ing adapters to dig out more controllable ability for text-to-
image diffusion models. In Proceedings of the AAAI Con-
ference on Artificial Intelligence, pages 4296–4304, 2024.
1, 2
[60] Thomas Nestmeyer, Jean-Franc¸ois Lalonde, Iain Matthews,


and Andreas Lehrmann. Learning physics-guided face re-
lighting under directional light.
In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 5124–5133, 2020. 5
[61] Alexander Quinn Nichol,
Prafulla Dhariwal,
Aditya
Ramesh, Pranav Shyam, Pamela Mishkin, Bob Mcgrew,
Ilya Sutskever, and Mark Chen. Glide: Towards photore-
alistic image generation and editing with text-guided dif-
fusion models.
In International Conference on Machine
Learning, pages 16784–16804. PMLR, 2022. 1, 2
[62] Rohit Pandey, Sergio Orts-Escolano, Chloe Legendre,


Christian Haene, Sofien Bouaziz, Christoph Rhemann,
Paul E Debevec, and Sean Ryan Fanello.
Total relight-
ing: learning to relight portraits for background replace-
ment. ACM Trans. Graph., 40(4):43–1, 2021. 5, 7
[63] Yingxue Pang, Jianxin Lin, Tao Qin, and Zhibo Chen.


Image-to-image translation:
Methods and applications.
IEEE Transactions on Multimedia, 24:3859–3881, 2021. 1
[64] Taesung Park, Ming-Yu Liu, Ting-Chun Wang, and Jun-


Yan Zhu. Semantic image synthesis with spatially-adaptive
normalization. In Proceedings of the IEEE/CVF conference


on computer vision and pattern recognition, pages 2337–
2346, 2019. 1
[65] Stefano Peluchetti. Non-denoising forward-time diffusions.


arXiv preprint arXiv:2312.14589, 2023. 2
[66] Dustin Podell,
Zion English,
Kyle Lacey,
Andreas
Blattmann, Tim Dockhorn, Jonas M¨uller, Joe Penna, and
Robin Rombach. Sdxl: Improving latent diffusion models
for high-resolution image synthesis. In The Twelfth Inter-
national Conference on Learning Representations, 2023. 1,
2, 4, 15
[67] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey


Chu, and Mark Chen.
Hierarchical text-conditional
image generation with clip latents.
arXiv preprint
arXiv:2204.06125, 2022. 1, 2
[68] Ren´e Ranftl, Katrin Lasinger, David Hafner, Konrad


Schindler, and Vladlen Koltun. Towards robust monocu-
lar depth estimation: Mixing datasets for zero-shot cross-
dataset transfer. IEEE transactions on pattern analysis and
machine intelligence, 44(3):1623–1637, 2020. 5
[69] Ren´e Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. Vi-


sion transformers for dense prediction. In Proceedings of
the IEEE/CVF international conference on computer vi-
sion, pages 12179–12188, 2021. 5
[70] Mengwei Ren, Wei Xiong, Jae Shin Yoon, Zhixin Shu,


Jianming Zhang, HyunJoon Jung, Guido Gerig, and He
Zhang. Relightful harmonization: Lighting-aware portrait
background replacement. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition,
pages 6452–6462, 2024. 5
[71] Yuxi Ren, Xin Xia, Yanzuo Lu, Jiacheng Zhang, Jie Wu,


Pan Xie, Xing Wang, and Xuefeng Xiao. Hyper-sd: Trajec-
tory segmented consistency model for efficient image syn-
thesis. arXiv preprint arXiv:2404.13686, 2024. 2
[72] Mike Roberts, Jason Ramapuram, Anurag Ranjan, At-


ulit Kumar, Miguel Angel Bautista, Nathan Paczan, Russ
Webb, and Joshua M Susskind. Hypersim: A photorealistic
synthetic dataset for holistic indoor scene understanding. In
Proceedings of the IEEE/CVF international conference on
computer vision, pages 10912–10922, 2021. 15
[73] Robin Rombach, Andreas Blattmann, Dominik Lorenz,


Patrick Esser, and Bj¨orn Ommer. High-resolution image
synthesis with latent diffusion models. In Proceedings of
the IEEE/CVF conference on computer vision and pattern
recognition, pages 10684–10695, 2022. 1, 2, 3, 4, 16
[74] Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-


net: Convolutional networks for biomedical image segmen-
tation. In Medical image computing and computer-assisted
intervention–MICCAI 2015: 18th international conference,
Munich, Germany, October 5-9, 2015, proceedings, part III
18, pages 234–241. Springer, 2015. 4
[75] Min-Cheol Sagong, Yoon-Jae Yeo, Seung-Won Jung, and


Sung-Jea Ko. Rord: A real-world object removal dataset.
In BMVC, page 542, 2022. 4, 5, 18
[76] Tim Salimans and Jonathan Ho. Progressive distillation for


fast sampling of diffusion models. In International Confer-
ence on Learning Representations, 2021. 2, 4


12


[77] Axel Sauer, Dominik Lorenz, Andreas Blattmann, and


Robin Rombach. Adversarial diffusion distillation. arXiv
preprint arXiv:2311.17042, 2023. 2
[78] Axel Sauer, Frederic Boesel, Tim Dockhorn, Andreas


Blattmann, Patrick Esser, and Robin Rombach. Fast high-
resolution image synthesis with latent adversarial diffusion
distillation. arXiv preprint arXiv:2403.12015, 2024. 2, 4
[79] Thomas Schops, Johannes L Schonberger, Silvano Galliani,


Torsten Sattler, Konrad Schindler, Marc Pollefeys, and An-
dreas Geiger. A multi-view stereo benchmark with high-
resolution images and multi-camera videos. In Proceed-
ings of the IEEE conference on computer vision and pattern
recognition, pages 3260–3269, 2017. 5, 16
[80] Yichen Sheng, Jianming Zhang, and Bedrich Benes. Ssn:


Soft shadow network for image compositing.
In CVPR,
pages 4380–4390, 2021. 7
[81] Yuyang Shi, Valentin De Bortoli, Andrew Campbell, and


Arnaud Doucet.
Diffusion schr¨odinger bridge matching.
Advances in Neural Information Processing Systems, 36,
2024. 2
[82] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob


Fergus. Indoor segmentation and support inference from
rgbd images. In Computer Vision–ECCV 2012: 12th Euro-
pean Conference on Computer Vision, Florence, Italy, Oc-
tober 7-13, 2012, Proceedings, Part V 12, pages 746–760.
Springer, 2012. 5, 16
[83] Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan,


and Surya Ganguli.
Deep unsupervised learning using
nonequilibrium thermodynamics. In International confer-
ence on machine learning, pages 2256–2265. PMLR, 2015.
1, 2
[84] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma,


Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-
based generative modeling through stochastic differential
equations. In International Conference on Learning Repre-
sentations, 2020. 1, 2
[85] Yang Song, Prafulla Dhariwal, Mark Chen, and Ilya


Sutskever.
Consistency models.
In Proceedings of the
40th International Conference on Machine Learning, pages
32211–32252, 2023. 2
[86] Julian Straub, Thomas Whelan, Lingni Ma, Yufan Chen,


Erik Wijmans, Simon Green, Jakob J Engel, Raul Mur-
Artal, Carl Ren, Shobhit Verma, et al.
The replica
dataset: A digital replica of indoor spaces. arXiv preprint
arXiv:1906.05797, 2019. 15
[87] Tiancheng Sun, Jonathan T Barron, Yun-Ta Tsai, Zexiang


Xu, Xueming Yu, Graham Fyffe, Christoph Rhemann, Jay
Busch, Paul Debevec, and Ravi Ramamoorthi. Single im-
age portrait relighting.
ACM Transactions on Graphics
(TOG), 38(4):1–12, 2019. 5
[88] Wenhao Sun, Benlei Cui, Jingqun Tang, and Xue-Mei


Dong. Attentive eraser: Unleashing diffusion model’s ob-
ject removal potential via self-attention redirection guid-
ance. In Proceedings of the AAAI Conference on Artificial
Intelligence, 2025. 1, 4
[89] Roman Suvorov, Elizaveta Logacheva, Anton Mashikhin,


Anastasia Remizova, Arsenii Ashukha, Aleksei Silvestrov,


Naejin Kong, Harshith Goka, Kiwoong Park, and Victor
Lempitsky. Resolution-robust large mask inpainting with
fourier convolutions. In Proceedings of the IEEE/CVF win-
ter conference on applications of computer vision, pages
2149–2159, 2022. 4, 15
[90] Onur Tasar, Cl´ement Chadebec, and Benjamin Aubin. Con-


trollable shadow generation with single-step diffusion mod-
els from synthetic data. arXiv preprint arXiv:2412.11972,
2024. 7
[91] Igor Vasiljevic, Nick Kolkin, Shanyi Zhang, Ruotian Luo,


Haochen Wang, Falcon Z Dai, Andrea F Daniele, Moham-
madreza Mostajabi, Steven Basart, Matthew R Walter, et al.
Diode: A dense indoor and outdoor depth dataset. arXiv
preprint arXiv:1908.00463, 2019. 5, 16
[92] Ke Wang, Micha¨el Gharbi, He Zhang, Zhihao Xia, and Eli


Shechtman. Semi-supervised parametric real-world image
harmonization. In Proceedings of the IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition, pages
5927–5936, 2023. 5, 6
[93] Xintao Wang, Liangbin Xie, Chao Dong, and Ying Shan.


Real-esrgan:
Training real-world blind super-resolution
with pure synthetic data. In Proceedings of the IEEE/CVF
international conference on computer vision, pages 1905–
1914, 2021. 17
[94] Zhibo Wang, Xin Yu, Ming Lu, Quan Wang, Chen Qian,


and Feng Xu. Single image portrait relighting via explicit
multiple reflectance channel modeling. ACM Transactions
on Graphics (ToG), 39(6):1–13, 2020. 5
[95] Shaoan Xie, Zhifei Zhang, Zhe Lin, Tobias Hinz, and Kun


Zhang. Smartbrush: Text and shape guided object inpaint-
ing with diffusion model. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition,
pages 22428–22437, 2023. 4
[96] Guangkai Xu, Yongtao Ge, Mingyu Liu, Chengxiang Fan,


Kangyang Xie, Zhiyue Zhao, Hao Chen, and Chunhua
Shen. Diffusion models trained with large data are trans-
ferable visual models. arXiv e-prints, pages arXiv–2403,
2024. 5
[97] Yanwu Xu, Yang Zhao, Zhisheng Xiao, and Tingbo Hou.


Ufogen: You forward once large scale text-to-image gener-
ation via diffusion gans. arXiv preprint arXiv:2311.09257,
2023. 2
[98] Lihe Yang, Bingyi Kang, Zilong Huang, Xiaogang Xu, Ji-


ashi Feng, and Hengshuang Zhao. Depth anything: Un-
leashing the power of large-scale unlabeled data. In Pro-
ceedings of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition, pages 10371–10381, 2024. 5
[99] Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiao-


gang Xu, Jiashi Feng, and Hengshuang Zhao. Depth any-
thing v2. Advances in Neural Information Processing Sys-
tems, 37:21875–21911, 2025. 5
[100] Chongjie Ye, Lingteng Qiu, Xiaodong Gu, Qi Zuo,


Yushuang Wu, Zilong Dong, Liefeng Bo, Yuliang Xiu, and
Xiaoguang Han. Stablenormal: Reducing diffusion vari-
ance for stable and sharp normal. ACM Transactions on
Graphics (TOG), 43(6):1–18, 2024. 5
[101] Yu-Ying Yeh, Koki Nagano, Sameh Khamis, Jan Kautz,


Ming-Yu Liu, and Ting-Chun Wang. Learning to relight


13


portrait images via a virtual light stage and synthetic-to-real
adaptation. ACM Transactions on Graphics (TOG), 41(6):
1–21, 2022. 5
[102] Tianwei Yin, Micha¨el Gharbi, Richard Zhang, Eli Shecht-


man, Fredo Durand, William T Freeman, and Taesung Park.
One-step diffusion with distribution matching distillation.
arXiv preprint arXiv:2311.18828, 2023. 2
[103] Tianwei Yin, Micha¨el Gharbi, Taesung Park, Richard


Zhang, Eli Shechtman, Fredo Durand, and William T Free-
man. Improved distribution matching distillation for fast
image synthesis. arXiv preprint arXiv:2405.14867, 2024. 2
[104] Wei Yin, Yifan Liu, and Chunhua Shen. Virtual normal:


Enforcing geometric constraints for accurate and robust
depth prediction. IEEE Transactions on Pattern Analysis
and Machine Intelligence, 44(10):7282–7295, 2021. 5
[105] Wei Yin, Jianming Zhang, Oliver Wang, Simon Niklaus,


Long Mai, Simon Chen, and Chunhua Shen. Learning to
recover 3d scene shape from a single image. In Proceed-
ings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 204–213, 2021.
[106] Wei Yin, Chi Zhang, Hao Chen, Zhipeng Cai, Gang Yu,


Kaixuan Wang, Xiaozhi Chen, and Chunhua Shen. Met-
ric3d: Towards zero-shot metric 3d prediction from a sin-
gle image. In Proceedings of the IEEE/CVF International
Conference on Computer Vision, pages 9043–9053, 2023.
[107] Weihao Yuan, Xiaodong Gu, Zuozhuo Dai, Siyu Zhu, and


Ping Tan. Neural window fully-connected crfs for monocu-
lar depth estimation. In Proceedings of the IEEE/CVF con-
ference on computer vision and pattern recognition, pages
3916–3925, 2022. 5
[108] Chong Zeng, Yue Dong, Pieter Peers, Youkang Kong,


Hongzhi Wu, and Xin Tong. Dilightnet: Fine-grained light-
ing control for diffusion-based image generation. In ACM
SIGGRAPH 2024 Conference Papers, pages 1–12, 2024. 5
[109] Chi Zhang, Wei Yin, Billzb Wang, Gang Yu, Bin Fu,


and Chunhua Shen. Hierarchical normalization for robust
monocular depth estimation. Advances in Neural Informa-
tion Processing Systems, 35:14128–14139, 2022. 5
[110] Longwen Zhang, Qixuan Zhang, Minye Wu, Jingyi Yu, and


Lan Xu. Neural video portrait relighting in real-time via
consistency modeling.
In Proceedings of the IEEE/CVF
international conference on computer vision, pages 802–
812, 2021. 5
[111] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding


conditional control to text-to-image diffusion models. In
Proceedings of the IEEE/CVF International Conference on
Computer Vision, pages 3836–3847, 2023. 1, 2
[112] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Scaling


in-the-wild training for diffusion-based illumination har-
monization and editing by imposing consistent light trans-
port. In The Thirteenth International Conference on Learn-
ing Representations, 2025. 1, 5, 6
[113] Qinsheng Zhang and Yongxin Chen. Fast sampling of dif-


fusion models with exponential integrator. In NeurIPS 2022
Workshop on Score-Based Methods, 2022. 2
[114] Richard Zhang, Phillip Isola, Alexei A Efros, Eli Shecht-


man, and Oliver Wang. The unreasonable effectiveness of


deep features as a perceptual metric. In Proceedings of the
IEEE conference on computer vision and pattern recogni-
tion, pages 586–595, 2018. 3
[115] Xuaner Zhang, Jonathan T Barron, Yun-Ta Tsai, Rohit


Pandey, Xiuming Zhang, Ren Ng, and David E Jacobs. Por-
trait shadow manipulation. ACM Transactions on Graphics
(TOG), 39(4):78–1, 2020. 5
[116] Wenliang Zhao, Lujia Bai, Yongming Rao, Jie Zhou, and


Jiwen Lu. Unipc: A unified predictor-corrector framework
for fast sampling of diffusion models. Advances in Neural
Information Processing Systems, 36, 2024. 2
[117] Hongkai Zheng, Weili Nie, Arash Vahdat, Kamyar Aziz-


zadenesheli, and Anima Anandkumar. Fast sampling of dif-
fusion models via operator learning. In International Con-
ference on Machine Learning, pages 42390–42402. PMLR,
2023. 2
[118] Peng Zheng, Dehong Gao, Deng-Ping Fan, Li Liu, Jorma


Laaksonen, Wanli Ouyang, and Nicu Sebe. Bilateral refer-
ence for high-resolution dichotomous image segmentation.
CAAI Artificial Intelligence Research, 3:9150038, 2024. 1,
5, 8
[119] Hao Zhou, Sunil Hadap, Kalyan Sunkavalli, and David W


Jacobs. Deep single-image portrait relighting. In Proceed-
ings of the IEEE/CVF international conference on com-
puter vision, pages 7194–7202, 2019. 5
[120] Jun-Yan Zhu, Taesung Park, Phillip Isola, and Alexei A


Efros. Unpaired image-to-image translation using cycle-
consistent adversarial networks. In Proceedings of the IEEE
international conference on computer vision, pages 2223–
2232, 2017. 1
[121] Junhao Zhuang, Yanhong Zeng, Wenran Liu, Chun Yuan,


and Kai Chen. A task is worth one word: Learning with
task prompts for high-quality versatile image inpainting. In
European Conference on Computer Vision, pages 195–211.
Springer, 2024. 4


14


A. Training details


In this section, we provide any relevant parameters used to
train our models.


A.1. Object-removal task


For the object-removal task, we trained our model for 20k
iterations on 2 H100 GPUs. We set σ = 0.05 and used
the timestep distribution we propose in the main paper i.e.
π(t) = U(i/4)i∈{0,1,2,3}. We use a bucketing strategy as
proposed in [66] allowing us to handle multiple aspect ratios
and resolutions. This strategy consists of defining buckets
with pre-defined aspect ratios and pixel budgets and filling
them with the data flow. During each training iteration, a
target pixel budget is sampled and then the upcoming im-
ages are assigned to the bucket with the closest aspect ra-
tio and budget and are resized accordingly.
We use the
following bucket pixel budgets: [2562, 5122, 7682, 10242]
sampled with probabilities [0.1, 0.2, 0.2, 0.5]. For each bud-
get we consider aspect ratios ranging from 0.25 to 4. The
batch sizes are respectively set to 32, 16, 8 and 4 for each
budget. We trained the model with LPIPS pixel loss with
weight λ = 10 and a learning rate of 3e−5 and we used
the AdamW optimizer [52]. For data sources, we randomly
sampled data from the RORD train set, our synthetic dataset
or our in-the-wild dataset with probabilities [0.3, 0.3, 0.4].
For the latter, we used the random masking strategy pro-
posed in [89] while for RORD and our synthetic dataset
we used the provided semantic masks. The denoiser is ini-
tialized using the weights of the pre-trained text-to-image
model SDXL [66].


A.2. Depth estimation


For depth estimation, we trained our model for 20k itera-
tions on 2 H100 GPUs. We set σ = 0.005 and set λ = 50
for the pixel loss (LPIPS) scale. We used the following
timestep distribution π(t) = 0.025·δt=0.75 +0.05·δt=0.5 +
0.025·δt=0.25+0.9·δt=0 to favor 1 step inference. We use a
batch size of 4 and trained the model with a combination of
hypersim [72] (40%), virtual KITTI [7] (10%) and replica
[86] (50%) datasets. For virtual KITTI, as is common, we
set the far plane to 80m. The learning rate is set to 4e−5 and
we used the AdamW optimizer during training.


A.2.1. Normal estimation


For surface normal estimation, we trained an LBM model
for 25k iterations on 2 H100 GPUs. We set σ = 0.1 and
λ = 50 and used a pixel loss chosen as L1. We used the
following timestep distribution π(t) = 0.05 · δt=0.75 + 0.1 ·
δt=0.5 + 0.05 · δt=0.25 + 0.8 · δt=0 to favour 1 step infer-
ence. We used a batch size of 4 and trained the model with
a combination of hypersim [72] (20%), virtual KITTI [7]
(10%) and replica [86] (70%) datasets. The learning rate


is set to 4e−5 and we used the AdamW optimizer during
training.


A.2.2. Image relighting


In the case of image relighting, we trained a LBM model
for 20k iterations on 2 H100 GPUs. We set σ = 0.01 and
λ = 10 and used a LPIPS pixel loss. We used the same
timestep distribution and the same data bucketing strategy
as for the object-removal task with the same bucket pixel
budgets and probabilities. The training data is composed
of synthetic data created using the rendering engine (90%)
and in-the-wild data (10%). We trained the model with a
learning rate of 3e−5 together with the AdamW optimizer.


A.2.3. Controllable shadow generation and controllable


image relighting


For these experiments, we trained a conditional LBM for
19k iterations using a pixel loss scale set to λ = 2.5 with
LPIPS loss. We used a timestep distribution π(t) similar to
the one used for the object-removal task. We used a batch
size of 4 and trained the model with a learning rate set to
5e−5 together with AdamW optimizer. The light map con-
ditioning is injected by concatenating it in the latent space
along the channels axis. In these cases, we only trained with
the synthetic data created using the rendering engine.


B. Additional object-removal results


In this appendix, we provide additional results for the ob-
ject removal task. In this case, instead of considering the
coarse semantic masks from RORD validation set, we con-
sider the fine semantic masks precisely indicating the object
to remove from the source image. We provide in Tab. 5, the
same metrics as in the main paper. Similar to what was ob-
served in the previous experiment, the proposed model is
again able to reach the best results.


Method (NFE)
FID ↓
Local FID ↓
fMSE ↓
PSNR ↑
SSIM ↑


LAMA (1)
30.43
36.69
2450.60
19.74
56.45
SDXL inp. (50)
42.55
45.35
3976.95
20.06
69.49
PowerPaint (50)
40.61
40.35
3673.91
20.71
66.85
AE (50)
18.43
22.24
1772.99
22.81
70.79


Ours (1)
15.50
15.62
1024.67
24.28
73.10


Table 5. Metrics for object-removal task with models fine-tuned
on RORD train set and evaluated on RORD validation set (52k
images) using the fine semantic masks. Our method uses a single
NFE. Best results are highlighted in bold, second best are under-
lined.


For the sake of completeness, we also fine-tune LAMA,
SDXL-inpaint., PowerPaint and our LBM checkpoint (At-
tentive Eraser is training-free) only on RORD train set such
that all the models see approx. 400k samples, which was
enough to reach convergence. For the sake of complete-
ness, we also train a LBM model from scratch only on the


15


RORD train set with the same number of iterations. We
share the results in Tab. 6. As shown in the table, while this
fine-tuning step improves competitors’ results, in particular
for fine masks, our method still outperforms competitors for
most metrics. Also note that our initial model is 047 trained
on 2 H100 for ≈18h vs. 240h on 8 V100 for LAMA.


Method
FID↓
Local FID↓
fMSE↓
PSNR↑
SSIM↑
Inf.
Coa. Fin.
Coa.
Fin.
Coa.
Fin.
Coa. Fin.
Coa. Fin.
time (s)


LAMA
30.3 21.4
38.0
28.2
1592.2 1350.3
19.7 20.6
55.9 57.1
0.1
SDXL-inp.
27.2 18.5
27.3
18.0
2297.3 2213.1
19.8 21.4
64.9 69.0
7.2
PowerPaint
29.9 27.0
30.0
23.7
2871.2 2679.7
18.5 19.9
58.3 63.4
4.2
AE
29.7 18.4
33.2
22.2
2029.0 1773.0
20.9 22.8
65.7 70.8
8.0


Ours
26.9 15.7
30.5
15.6
1306.6 997.4
22.5 24.5
69.2 73.2
0.3
Ours (scratch) 27.9 16.7
30.7
16.9
1329.5 1032.2
22.4 24.4
69.0 72.9
0.3


Table 6. Metrics for object-removal task computed on RORD val-
idation set using the coarse (Coa.) and fine (Fin.) masks. Our
method and LAMA use a single neural function evaluation (NFE),
others use 50 NFEs. Inference time is averaged over 50 images
and computed on a single H100 GPU.


C. Results for depth estimation


As mentioned in the main paper, we also consider the
monocular depth estimation task which consists of estimat-
ing a depth map from a two dimensional image. We provide
in Tab. 7 the zero-shot results of our method compared to
the state-of-the-art methods on commonly used evaluation
datasets such as NYUv2 [82], KITTI [22], ETH3D [79],
Scannet [11] and DIODE [91]. As shown in the table , the
proposed method is able to outperform or be competitive
with the state-of-the-art methods and achieves the best av-
erage ranking across all metrics and datasets.


D. Failure cases


In this section, we present some identified failure cases of
our model for the different tasks considered.


D.1. Object-removal


For object-removal, we noticed that our method can remove
shadows more efficiently than all the existing methods as
shown in the main paper, but there still exists some cases
where it is not able to remove the shadow perfectly. More-
over, sometimes the model is not able to remove complex
reflections of the object in the environment. These two fail-
ure cases are illustrated in Fig. 10. On the top row, the
shadow underneath the object to remove is still visible in
the output image. On the bottom row, the model success-
fully removed the person and associated shadow but failed
to remove the reflection on the glass door.


D.2. Image relighting


While the proposed method is able to handle most cases, we
noticed that it can sometimes fail to remove existing reflec-
tions on the foreground image, induce a color shift or add a


Input
Mask
Ours


Figure 10. Failure cases for object-removal. In the first row the
model is not able to remove completely the shadow underneath
the object. In the second row the model is not able to remove the
reflection on the glass.


Composite
Ours
Composite
Ours


Figure 11. Failure cases for image relighting. On the left, the
model is not able to remove the reflection in the subject glasses.
On the right, the model changes the color of the person’s jacket
and create a plastic effect on the face.


plastic effect to the output image due to the use of synthetic
data for training. We believe that these three failure cases
can be addressed with a more careful training data curation
and through more realistic renderings of the synthetic data.


E. Memory footprint and inference time


Our intuition to use a latent model is motivated by the key
observations made in [73] where the authors scale image
generation from diffusion models. Nevertheless, we quan-
titatively report in Tab. 8 the memory/latency comparison
between a pixel model and a latent model both for training
and inference. Note that the VAE compresses the source
image by a factor of 8 and is frozen during training drasti-
cally reducing the memory footprint of the model as shown
in the table.


F. Additional samples


Finally, we provide additional samples for object-removal
in Fig. 12 and for image relighting in Figs. 13 to 17. For
object-removal, our model remains the only one capable of
removing the target object as well as the associated shad-
ows. For image relighting, the proposed approach can cre-
ate strong illumination effects on the foreground object and
can handle complex lighting conditions. To further stress


16


Method
NYUv2
KITTI
ETH3D
ScanNet
DIODE
Avg
AbsRel↓
δ1 ↑
δ2 ↑
AbsRel↓
δ1 ↑
δ2 ↑
AbsRel↓
δ1 ↑
δ2 ↑
AbsRel↓
δ1 ↑
δ2 ↑
AbsRel↓
δ1 ↑
δ2 ↑
Rank


DiverseDepth
11.7
87.5
-
19.0
70.4
-
22.8
69.4
-
10.9
88.2
-
37.6
63.1
-
16.6
MiDaS
11.1
88.5
-
23.6
63.0
-
18.4
75.2
-
12.1
84.6
-
33.2
71.5
-
16.1
LeRes
9.0
91.6
-
14.9
78.4
-
17.1
77.7
-
9.1
91.7
-
27.1
76.6
-
13.2
Omnidata
7.4
94.5
-
14.9
83.5
-
16.6
77.8
-
7.5
93.6
-
33.9
74.2
-
13.2
DPT
9.8
90.3
-
10.0
90.1
-
7.8
94.6
-
8.2
93.4
-
18.2
75.8
-
10.8
HDN
6.9
94.8
-
11.5
86.7
-
12.1
83.3
-
8.0
93.9
-
24.6
78.0
-
10.2
DepthFM
6.0
95.5
-
9.1
90.2
-
6.5
95.4
-
6.6
94.9
-
22.4
78.5
-
7.2
GenPercept
5.6
96.0
99.2
13.0
84.2
97.2
7.0
95.6
98.8
6.2
96.1
99.1
35.7
75.6
86.6
8.3
Diff.-E2E-FT
5.4
96.5
99.1
9.6
92.1
98.0
6.4
95.9
98.7
5.8
96.5
98.8
30.3
77.6
87.9
5.6
DepthAnything V2
4.5
97.9
99.3
7.4
94.6
98.6
13.1
86.5
97.5
4.2
97.8
99.3
26.5
73.4
87.1
5.4
DepthAnything
4.3
98.1
99.6
7.6
94.7
99.2
12.7
88.2
98.3
4.3
98.1
99.6
26.0
75.9
87.5
4.1
GeoWizard
5.6
96.3
99.1
14.4
82.0
96.6
6.6
95.8
98.4
6.4
95.0
98.4
33.5
72.3
86.5
9.6
Marigold (LCM)
6.1
95.8
99.0
9.8
91.8
98.7
6.8
95.6
99.0
6.9
94.6
98.6
30.7
77.5
89.3
7.7
Marigold
5.5
96.4
99.1
9.9
91.6
98.7
6.5
95.9
99.0
6.4
95.2
98.8
30.8
77.3
88.7
6.4
Lotus-D
5.1
97.2
99.2
8.1
93.1
98.7
6.1
97.0
99.1
5.5
96.5
99.0
22.8
73.8
86.2
4.0
Lotus-G
5.4
96.8
99.2
8.5
92.2
98.4
5.9
97.0
99.2
5.9
95.7
98.8
22.9
72.9
86.0
5.3


Ours
5.6
97.2
99.2
9.4
93.0
98.9
6.3
96.5
99.3
5.7
97.0
99.2
30.3
77.5
89.3
3.7


Table 7. Metrics for depth estimation task. Our method uses a single NFE. Competitors results are taken from [25]. Best results are
highlighted in bold, second best are underlined.


Mode (Resolution)
Metric
Pixel Model
Latent Model
Gain


Inference (256 / 1024)
Latency (s)
0.19 / 20.11
0.14 / 0.27
26.3% / 98.7%
Peak Memory (Gb)
5.63 / 15.71
5.29 / 7.70
6.0% / 51.0%


Training (256 / 1024)
Latency (s)
0.71 / -
0.43 / 0.58
39.4% / -
Peak Memory (Gb)
43.19 / OoM
24.85/ 25.35
41.3% / -


Table 8. Training and inference memory usage and per-iteration
latency for a pixel and a latent bridge model. The metrics are
averaged over 10 images using a batch size of 1 with AdamW for
training and 1 NFE for inference on a single H100 80Gb GPU.


the method’s versatility, we also consider an image restora-
tion task and provide qualitative samples in Figs. 18 and 19.
For this task, π0 corresponds to the distribution of the la-
tents of the degraded images while π1 is the distribution of
the latents of the clean images. We artificially create de-
graded images using the method proposed in [93]. In line
with the performance observed for the tasks considered in
the paper, the proposed method is able to create realistic
outputs from degraded images.


17


Figure 12. Qualitative results for object-removal on RORD validation dataset [75]. Best viewed zoomed in. Our model uses a single NFE
and is able to successfully remove not only the object but also its shadow.


18


Figure 13. Qualitative results for object relighting. The model is able to relight the object according to the provided background and also
remove existing shadows and reflections.


19


Original
Ours (1 NFE)
Original
Ours (1 NFE)


Figure 14. Qualitative results for object relighting. The model is able to relight the object according to the provided background and also
remove existing shadows and reflections.


20


Composite
Ours (1 NFE)
Composite
Ours (1 NFE)


Figure 15. Qualitative results for object relighting. The model is able to relight the object according to the provided background and also
remove existing shadows and reflections.


21


Background
Composite
Ours (1 NFE)
Background
Composite
Ours (1 NFE)


Figure 16. Qualitative results for object relighting. The model is able to relight the object according to the provided background and also
remove existing shadows and reflections.


22


Figure 17. Qualitative results for controllable image relighting.


23


Figure 18. Qualitative results for object image restoration.


24


Figure 19. Qualitative results for object image restoration.


25
