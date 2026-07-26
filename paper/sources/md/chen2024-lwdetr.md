LW-DETR: A Transformer Replacement to


YOLO for Real-Time Detection


Qiang Chen1⋆, Xiangbo Su1∗, Xinyu Zhang2,1∗, Jian Wang1, Jiahui Chen3,1,


Yunpeng Shen1, Chuchu Han1, Ziliang Chen1, Weixiang Xu1, Fanrong Li4,
Shan Zhang5, Kun Yao1, Errui Ding1, Gang Zhang1, and Jingdong Wang1†


1 Baidu Inc., China
2 The University of Adelaide, Australia
3 Beihang University, China
4 Institute of Automation, Chinese Academy of Sciences, China
5 Australian National University, Australia
{chenqiang13,suxiangbo,zhangxinyu14,wangjingdong}@baidu.com


Abstract. In this paper, we present a light-weight detection trans-
former, LW-DETR, which outperforms YOLOs for real-time object de-
tection. The architecture is a simple stack of a ViT encoder, a projector,
and a shallow DETR decoder. Our approach leverages recent advanced
techniques, such as training-effective techniques, e.g., improved loss and
pretraining, and interleaved window and global attentions for reducing
the ViT encoder complexity. We improve the ViT encoder by aggregat-
ing multi-level feature maps, and the intermediate and final feature maps
in the ViT encoder, forming richer feature maps, and introduce window-
major feature map organization for improving the efficiency of interleaved
attention computation. Experimental results demonstrate that the pro-
posed approach is superior over existing real-time detectors, e.g., YOLO
and its variants, on COCO and other benchmark datasets. Code and
models are available at https://github.com/Atten4Vis/LW-DETR.


Keywords: Object Detection · Real-Time · Detection Transformer


1
Introduction


Real-time object detection is an important problem in visual recognition and
has wide real-world applications. The current dominant solutions are based on
convolutional networks, such as the YOLO series [1, 2, 20, 29, 32, 33, 46, 59, 65].
Recently, transformer methods, e.g., detection transformer (DETR) [4], have
witnessed significant progress [7, 19, 41, 47, 63, 67, 74, 75]. Unfortunately, DETR
for real-time detection remains not fully explored, and it is unclear if the per-
formance is comparable to the state-of-the-art convolutional methods.


In this paper, we build a light-weight DETR approach for real-time object
detection. The architecture is very simple: a plain ViT encoder [17] and a DETR


⋆Equal contribution.
†Corresponding author.


arXiv:2406.03459v1  [cs.CV]  5 Jun 2024


2
Q. Chen et al.


0
5
10
15
20


40


45


50


55


59


Inference Time (ms)


mAP


LW-DETR


YOLO-NAS*


YOLOv8*


RTMDet*


YOLO-NAS


YOLOv8


RTMDet


Fig. 1: Our approach outperforms previous SoTA real-time detectors. The
x-axis corresponds to the inference time. The y-axis corresponds to the mAP score
on COCO val2017. All the models are trained with pretraining on Objects365. The
NMS post-processing times are included for other models and measured on the COCO
val2017 with the setting from the official implementation [1,29,46], and the well-tuned
NMS postprocessing setting (labeled as “*”).


decoder that are connected by a convolutional projector [29]. We propose to
aggregate the multi-level feature maps, the intermediate and final feature maps
in the encoder, forming stronger encoded feature maps. Our approach takes
advantage of effective training techniques. For example, we use the deformable
cross-attention forming the decoder [74], the IoU-aware classification loss [3],
and the encoder-decoder pretraining strategy [7,67,71].


On the other hand, our approach exploits inference-efficient techniques. For
example, we adopt interleaved window and global attentions [36, 37], replacing
some global attentions with window attentions in the plain ViT encoder to reduce
the complexity. We use an efficient implementation for the interleaved attentions
through a window-major feature map organization method, effectively reducing
the costly memory permutation operations.


Figure 1 shows that the proposed simple baseline surprisingly outperforms
the previous real-time detectors on COCO [39], e.g., YOLO-NAS [1], YOLOv8 [29],
and RTMDet [46]. These models are improved with pretraining on Objects365 [54],
and the end-to-end time cost, including the NMS time, is measured using the
setting from the official implementations6.


6 YOLO-NAS: https://github.com/Deci-AI/super-gradients
YOLOv8: https://docs.ultralytics.com
RTMDet: https://github.com/open-mmlab/mmyolo/tree/main/configs/rtmdet


LW-DETR
3


We conduct extensive experiments for the comparisons with existing real-
time detection algorithms [1,12,29,46,58]. We further optimize the NMS setting
and obtain improved performance for existing algorithms. The proposed baseline
still outperforms these algorithms (labeled as “*” in Figure 1). In addition, we
demonstrate the proposed approach with experimental results on more detection
benchmarks.


The proposed baseline merely explores simple and easily implemented tech-
niques and shows promising performance. We believe that our approach poten-
tially benefits from other designs, such as efficient multi-scale feature fusion [34],
token sparsification [36,72], distillation [5,5,9,64], as well as other training tech-
niques, such as the techniques used in YOLO-NAS [1]. We also show that the
proposed approach is applicable to the DETR approach with the convolutional
encoder, such as ResNet-18 and ResNet-50 [23], and achieves good performance.


2
Related Work


Real-time object detection. Real-time object detection has wide real-world
applications [18,25,30,31,49]. Existing state-of-the-art real-time detectors, such
as YOLO-NAS [1], YOLOv8 [29], and RTMDet [46], have been largely improved
compared with the first version of YOLO [50] through detection frameworks [20,
56], architecture designs [2,16,32,33,59,65], data augmentations [2,20,69], train-
ing techniques [1,20,29], and loss functions [38,68,73]. These detectors are based
on convolutions. In this paper, we study transformer-based solutions to real-time
detection that remains little explored.
ViT for object detection. Vision Transformer (ViT) [17,66] shows promising
performance in image classification. Applying ViT to object detection usually
exploits window attentions [17,43] or hierarchical architectures [21,43,62,70] to
reduce the memory and computation cost. UViT [8] uses progressive window
attention. ViTDet [36] implements the pre-trained plain ViT with interleaved
window and global attentions [37]. Our approach follows ViTDet to use inter-
leaved window and global attentions, and additionally uses window-major order
feature map organization for reducing the memory permutation cost.
DETR and its variants. Detection Transformer (DETR) is an end-to-end de-
tection method, with removing the necessity of many hand-crafted components,
such as anchor generation [51] and non-maximum suppression (NMS) [24]. There
are many followup methods for DETR improvement, such as architecture de-
sign [19,47,67,74], object query design [11,41,63], training techniques [6,7,27,35,
48,67,75], and loss function improvement [3,42]. Besides, various works have been
done for reducing the computational complexity, by architecture design [34,40],
computational optimization [74], pruning [53,72], and distillation [5,5,9,64]. The
interest of this paper is to build a simple DETR baseline for real-time detection
that are not explored by these methods.


Concurrent with our work, RT-DETR [45] also applies the DETR framework
to construct real-time detectors with a focus on the CNN backbone forming
the encoder. There are studies about relatively large models and a lack of tiny


4
Q. Chen et al.


Window Attention


Global Attention


Window Attention


Global Attention


Window Attention


Global Attention


Fig. 2: An example of transformer encoder with multi-level feature map aggre-
gation and interleaved window and global attentions. The FFN and LayerNorm layers
are not depicted for clarification.


models. Our LW-DETR explores the feasibility of plain ViT backbones and
DETR framework for real-time detection .


3
LW-DETR


3.1
Architecture


LW-DETR consists of a ViT encoder, a projector, and a DETR decoder.
Encoder. We adopt the ViT for the detection encoder. A plain ViT [17] consists
of a patchification layer and transformer encoder layers. A transformer encoder
layer in the initial ViT contains a global self-attention layer over all the tokens
and an FFN layer. The global self-attention is computationally costly, and its
time complexity is quadratic with respect to the number of tokens (patches). We
implement some transformer encoder layers with window self-attention to reduce
the computational complexity (detailed in Sec. 3.4). We propose to aggregate the
multi-level feature maps, the intermediate and final feature maps in the encoder,
forming stronger encoded feature maps. An example of the encoder is illustrated
in Figure 2.
Decoder. The decoder is a stack of transformer decoder layers. Each layer
consists of a self-attention, a cross-attention, and an FFN. We adopt deformable
cross-attention [74] for computational efficiency. DETR and its variants usually
adopt 6 decoder layers. In our implementation, we use 3 transformer decoder
layers. This leads to a time reduction from 1.4 ms to 0.7 ms, which is significant
compared to the time cost 1.3 ms of the remaining part for the tiny version in
our approach.


We adopt a mixed-query selection scheme [67] to form the object queries as
an addition of content queries and spatial queries. The content queries are learn-
able embeddings, which is similar to DETR. The spatial queries are based on a
two-stage scheme: selecting top-K features from the last layer in the Projector,
predicting the bounding boxes, and transforming the corresponding boxes into
embeddings as spatial queries.
Projector. We use a projector to connect the encoder and the decoder. The pro-
jector takes the aggregated encoded feature maps from the encoder as the input.


LW-DETR
5


Projector
Transformer


Decoder


(a)


Projector


Projector


Transformer


Decoder


(b)


Fig. 3: Single-scale projector and multi-scale projector for (a) the tiny, small,
and medium models, and (b) the large and xlarge models.


The projector is a C2f block (an extension of cross-stage partial DenseNet [26,
60]) that is implemented in YOLOv8 [29].
When forming the large and xlarge version of LW-DETR, we modify the
projector to output two-scale ( 1


8 and
1
32) feature maps and accordingly use the
multi-scale decoder [74]. The projector contains two parallel C2f blocks. One
processes 1


8 feature maps, which are obtained by upsampling the input through
a deconvolution, and the other processes
1
32 maps that are obtained by down-
sampling the input through a stride convolution. Figure 3 shows the pipelines of
the single-scale projector and the multi-scale projector.


Objective function. We adopt an IoU-aware classification loss, IA-BCE loss [3],


  \e l


l _{
\


tex


ttt {cl s}} 


= \s
u


m _


{i


= 1}^{N_{pos}}\operatorname {BCE}(s_i, t_i) + \sum _{j=1}^{N_{neg}} s_j^2\operatorname {BCE}(s_j,0) ,
(1)


where Npos and Nneg are the number of positive and negative samples. s is the
predicted classification score. t is the target score absorbing the IoU score u
(with the ground truth): t = sαu1−α, and α is empirically set as 0.25 [3].


The overall loss is a combination of the classification loss and the bound-
ing box loss that is the same as in the DETR frameworks [4, 67, 74], which is
formulated as follows:


  \e l l _{\tex t tt {cls}} + \lambda _{\texttt {iou}}\ell _{\texttt {iou}} + \lambda _{\ell _1}\ell _1 .
(2)


where λiou and λℓ1 are set as 2.0 and 5.0 similar to [4,67,74]. ℓiou and ℓ1 are the
generalized IoU (GIoU) loss [52] and the L1 loss for the box regression.


6
Q. Chen et al.


Table 1: Architectures of five LW-DETR instances.


ViT encoder
Projector
DETR decoder


LW-DETR
#layers
dim
#global
attention


#window
attention
#blocks
dim
scales
#layers
#object


queries


tiny
6
192
3
3
1
256
1
16
3
100


small
10
192
4
6
1
256
1
16
3
300


medium
10
384
4
6
1
256
1
16
3
300


large
10
384
4
6
1
384
1
8 ,
1
32
3
300


xlarge
10
768
4
6
1
384
1
8 ,
1
32
3
300


3.2
Instantiation


We instantiate 5 real-time detectors: tiny, small, medium, large, and xlarge.
The detailed settings are given in Table 1.


The tiny detector consists of a transformer encoder with 6 layers. Each layer
consists of a multi-head self-attention module and a feed-forward network (FFN).
Each image patch is linear-mapped to a 192-dimensional representation vector.
The projector outputs single-scale feature maps with 256 channels. There are
100 object queries for the decoder.
The small detector contains 10 encoder layers, and 300 object queries. Same
as the tiny detector, the dimensions for the input patch representation and the
output of the projector are 192 and 256. The medium detector is similar to small,
and the differences include that the dimension of the input patch representation
is 384, and accordingly the dimension for the encoder is 384.


The large detector consists of a 10-layer encoder and uses two-scale feature
maps (see the part Projector in Section 3.1). The dimensions for the input patch
representation and the output of the projector are 384 and 384. The xlarge
detector is similar to large, and the difference is that the dimension of the
input patch representation is 768.


3.3
Effective Training


More supervision. Various techniques have been developed to introduce more
supervision for accelerating the DETR training, e.g., [6,27,75]. We adopt Group
DETR [6] that is easily implemented and does not change the inference process.
Following [6], we use 13 parallel weight-sharing decoders for training. For each
decoder, we generate the object queries for each group from the output features
of the projector. Following [6], we use the primary decoder for the inference.
Pretraining on Objects365. The pretraining process consists of two stages.
First, we pretrain the ViT on the dataset Objects365 using a MIM method,
CAEv2 [71], based on the pretrained models. This leads to a 0.7 mAP gain on
COCO.


Second, we follow [7, 67] to retrain the encoder and train the projector and
the decoder on Objects365 in a supervision manner.


3.4
Efficient Inference


We make a simple modification [36,37] and adopt interleaved window and global
attentions: replacing some global self-attention layers with window self-attention


LW-DETR
7


Table 2: The influence of effective training and efficient inference techniques.
We show empirical results from an initial detector with global attention layers to the
final LW-DETR-small model. ‘†’ means we use the ViTDet implementation. The re-
sults except the last row are obtained under 45K iterations (equal to 12 epochs). The
last row corresponds to the result of the final model with 180K training iterations.


model settings
#Params (M)
FLOPs (G)
Latency (ms)
mAP


initial detector
10.8
22.8
3.6
35.3


+ multi-level feature aggregation
11.0
23.0
3.7
36.0


+ interleaved window and global attention†
11.0
16.6
3.9
34.7


+ window-major feature map organization
11.0
16.6
2.9
34.7


+ iou-aware classification loss
11.0
16.6
2.9
35.4


+ more supervision
14.6
16.6
2.9
38.4


+ bounding box reparameterization
14.6
16.6
2.9
38.6


+ pretraining on Objects365
14.6
16.6
2.9
47.3


LW-DETR-small
14.6
16.6
2.9
48.0


layers. For example, in a 6-layer ViT, the first, third, and fifth layers are im-
plemented with window attentions. The window attention is implemented by
partitioning the feature map into non-overlapping windows and performing self-
attention over each window separately.


We adopt a window-major feature map organization scheme for efficient in-
terleaved attention, which organizes the feature maps window by window. The
ViTDet implementation [36], where feature maps are organized row by row (row-
major organization), requires costly permutation operations to transition feature
maps from a row-major to a window-major organization for window attention.
Our implementation removes these operations and thus reduces model latency.


We illustrate the window-major way using a toy example. Given a 4 × 4
feature map


 


 \b


egi n { bma tri
x} f_{ 11} & 
f_{ 12} & f_{
13} & f_{ 14}


\


\ f_{21} & f_{22} & f_{23} & f_{24}\\ f_{31} & f_{32} & f_{33} & f_{34}\\ f_{41} & f_{42} & f_{43} & f_{44}\\ \end {bmatrix}
,
(3)


the window-major organization for a window size 2 × 2 is as below:


  \b egin {al igne d} & f_{1 1}, f_{1


2}, f_{2 1}, f_{2 2}; f_{1 3}, f_{14}, f_{23}, f_{24};\\ &f_{31}, f_{32}, f_{41}, f_{42}; f_{33}, f_{34}, f_{43}, f_{44}. \end {aligned} 
(4)


This organization is applicable to both window attention and global attention
without rearranging the features. The row-major organization,


  \b egin {al igne d} & f_{1 1}, f_{1


2}, f_{1 3}, f_{1 4}; f_{2 1}, f_{22}, f_{23}, f_{24};\\ &f_{31}, f_{32}, f_{33}, f_{34}; f_{41}, f_{42}, f_{43}, f_{44}, \end {aligned} 
(5)


is fine for global attention, and needs to be processed with the costly permutation
operation for performing window attention.


3.5
Empirical Study


We empirically show how effective training and efficient inference techniques
improve the DETR. We use the small detector as the example. The study is


8
Q. Chen et al.


based on an initial detector: the encoder is formed with global attention in all
the layers and outputs the feature map of the last layer. The results are shown
in Table 2.
Latency improvements. The interleaved window and global attention, adopted
by ViTDet, reduces the computational complexity from 23.0 GFlops to 16.6
GFlops, validating the benefit of replacing expensive global attention with cheaper
window attention. The latency is not reduced and even increased by 0.2 ms. This
is because extra costly permutation operations are needed in the row-major fea-
ture map organization. Window-major feature map organization alleviates the
side effects and leads to a larger latency reduction of 0.8 ms, from 3.7 ms to 2.9
ms.
Performance improvements. Multi-level feature aggregation brings a 0.7
mAP gain. Iou-aware classification loss and more supervision improve the mAP
scores from 34.7 to 35.4 and 38.4. Bounding box reparameterization for box
regression target [40] (details in the Supplementary Material) makes a slight
performance improvement. The significant improvement comes from pretraining
on Objects365 and reaches 8.7 mAP, implying that the transformer indeed ben-
efits from large data. A longer training schedule can give further improvements,
forming our LW-DETR-small model.


4
Experiments


4.1
Settings


Datasets. The dataset for pretraining is Objects365 [54]. We follow [7, 67] to
combine the images of the train set and the images in the validate set except
the first 5k images for detection pretraining. We use the standard COCO2017 [39]
data splitting policy and perform the evaluation on COCO val2017.
Data augmentations. We adopt the data augmentations in the DETR and
its variants [4, 74]. We follow the real-time detection algorithms [1, 29, 46] and
randomly resize the images into squares for training. For evaluating the per-
formance and the inference time, we follow the evaluation scheme used in the
real-time detection algorithms [1, 29, 46] to resize the images to 640 × 640. We
use a window size of 10 × 10 to make sure that the image size can be divisible
by the window size.
Implementation details. We pretrain the detection model on Objects365 [54]
for 30 epochs and finetune the model on COCO [39] for a total number of
180K training iterations. We adopt the exponential moving average (EMA) tech-
nique [55] with a decay of 0.9997. We use the AdamW optimizer [44] for training.


For pretraining, we set the initial learning rate of the projector and the DETR
decoder as 4 × e−4, the initial learning rate of the ViT backbone is 6 × e−4, and
the batch size is 128. For fine-tuning, we set the initial learning rate of the
projector and the DETR decoder as 1 × e−4, and the initial learning rate of the
ViT backbone as 1.5 × e−4. We set the batch size as 32 in the tiny, small,
and medium models, and the batch size as 16 in the large and xlarge models.


LW-DETR
9


Table 3: Comparisons with state-of-the-art real-time detectors, including RT-
MDet [46], YOLOv8 [29], and YOLO-NAS [1]. The total latency is evaluated in an
end-to-end manner on COCO val2017 and includes the model latency and the postpro-
cessing procedure NMS for non-DETR methods. We measure the total latency in two
settings for NMS: official implementation and tuned score threshold. Our LW-DETR
does not need NMS and the total latency is equal to the model latency. ‘pretraining’
means the result is based on pretraining on Objects365.


Method
pretraining
#Params


(M)


FLOPs


(G)


Model
Latency


(ms)


official implementation
tuned score threshold
Total Latency


(ms)
mAP
Total Latency


(ms)
mAP


RTMDet-tiny
4.9
8.1
2.1
7.4
41.0
2.4
40.8


RTMDet-tiny
✓
4.9
8.1
2.1
7.4
41.7
2.4
41.5


YOLOv8n
3.2
4.4
1.5
6.2
37.4
1.6
37.3


YOLOv8n
✓
3.2
4.4
1.5
6.2
37.6
1.6
37.5


LW-DETR-tiny
✓
12.1
11.2
2.0
2.0
42.6
-
-


RTMDet-s
8.9
14.8
2.8
7.9
44.6
2.9
44.4


RTMDet-s
✓
8.9
14.8
2.8
7.9
44.9
2.9
44.7


YOLOv8s
11.2
14.4
2.6
7.0
45.0
2.7
44.8


YOLOv8s
✓
11.2
14.4
2.6
7.0
45.2
2.7
45.1


YOLO-NAS-s
✓
19.0
17.6
2.8
4.7
47.6
2.9
47.3


LW-DETR-small
✓
14.6
16.6
2.9
2.9
48.0
-
-


RTMDet-m
24.7
39.2
6.2
10.8
49.3
6.5
49.1


RTMDet-m
✓
24.7
39.2
6.2
10.8
49.7
6.5
49.5


YOLOv8m
25.6
39.7
5.9
10.1
50.3
6.0
50.0


YOLOv8m
✓
25.6
39.7
5.9
10.1
50.6
6.0
50.4


YOLO-NAS-m
✓
51.1
48.0
5.5
7.8
51.6
5.7
51.1


LW-DETR-medium
✓
28.2
42.8
5.6
5.6
52.5
-
-


RTMDet-l
52.3
80.1
10.3
14.9
51.4
10.5
51.2


RTMDet-l
✓
52.3
80.1
10.3
14.9
52.4
10.5
52.2


YOLOv8l
43.7
82.7
9.3
13.2
53.0
9.4
52.5


YOLOv8l
✓
43.7
82.7
9.3
13.2
53.3
9.4
53.0


YOLO-NAS-l
✓
66.9
65.5
7.5
8.8
52.3
7.6
51.9


LW-DETR-large
✓
46.8
71.6
8.8
8.8
56.1
-
-


RTMDet-x
94.9
141.7
18.4
22.8
52.8
18.8
52.5


RTMDet-x
✓
94.9
141.7
18.4
22.8
54.0
18.8
53.5


YOLOv8x
68.2
129.3
14.8
19.1
54.0
15.0
53.5


YOLOv8x
✓
68.2
129.3
14.8
19.1
54.5
15.0
54.1


LW-DETR-xlarge
✓
118.0
174.2
19.1
19.1
58.3
-
-


The number of training iterations 180K is 50 epochs for the tiny, small, and
medium models, and 25 epochs for the large and xlarge models. More details,
such as weight decay, layer-wise decay in the ViT encoder, and component-wise
decay [7] in the fine-tuning process, are given in the Supplementary Material.


We measure the averaged inference latency in an end-to-end manner with
fp16 precision and a batch size of 1 on COCO val2017 with a T4 GPU, where
the environment settings are with TensorRT-8.6.1, CUDA-11.6, and CuDNN-8.7.0.
The efficientNMSPlugin in TensorRT is adopted for efficient NMS implementa-
tion. The performance and the end-to-end latency are measured for all real-time
detectors using the official implementations.


4.2
Results


The results of our five LW-DETR models are reported in Table 3. LW-DETR-
tiny achieves 42.6 mAP with 500 FPS on a T4 GPU. LW-DETR-small and
LW-DETR-medium get 48.0 mAP with over 340 FPS and 52.5 mAP with a


10
Q. Chen et al.


speed of over 178 FPS respectively. The large and xlarge models achieve 56.1
mAP with 113 FPS, and 58.3 mAP with 52 FPS.


Comparisons with state-of-the-art real-time detectors. In Table 3, we
report the comparison of the LW-DETR models against representative real-time
detectors, including YOLO-NAS [1], YOLOv8 [29], and RTMDet [46]. One can
see that LW-DETR consistently outperforms previous SoTA real-time detectors
with and without using pretraining. Our LW-DETR shows clear superiority over
YOLOv8 and RTMDet in terms of latency and detection performance for the
five scales from tiny to xlarge.


In comparison to one of previous best methods YOLO-NAS, that is obtained
with neural architecture search, our LW-DETR model outperforms it by 0.4
mAP and 0.9 mAP, and runs 1.6× and ∼1.4× faster at the small and medium
scales. When the model gets larger, the improvement becomes more significant:
a 3.8 mAP improvement when running at the same speed at the large scale.


We further improve other methods by well-tuning the classification score
threshold in the NMS procedure, and report the results in the right two columns.
The results are greatly improved, and still lower than our LW-DETR. We expect
that our approach potentially benefits from other improvements, such as neural
architecture search (NAS), data augmentation, pseudo-labeled data, and knowl-
edge distillation that are exploited by previous real-time detectors [1,29,46].


Comparison with concurrent works. We compare our LW-DETR with con-
current works in real-time detection, YOLO-MS [12], Gold-YOLO [58], RT-
DETR [45], and YOLOv10 [57]. YOLO-MS improves the performance by en-
hancing the multi-scale feature representations. Gold-YOLO boosts the multi-
scale feature fusion and applies MAE-style pretraining [22] to improve the YOLO
performance. YOLOv10 designs several efficiency and accuracy driven modules
to improve the performance. RT-DETR [45], closely related to LW-DETR, is
also built on the DETR framework, with many differences from our approach in
the backbone, the projector, the decoder, and the training schemes.


The comparisons are given in Table 4 and Figure 4. Our LW-DETR con-
sistently achieves a better balance between the detection performance and the
latency. YOLO-MS and Gold-YOLO clearly show worse results than our LW-
DETR for all the model scales. LW-DETR-large outperforms the closely related
RT-DETR-R50 by 0.8 mAP and shows faster speed (8.8 ms vs. 9.9 ms). LW-
DETR with other scales also shows better results than RT-DETR. Compared to
the latest work, YOLOv10-X [57], our LW-DETR-large achieves higher perfor-
mance (56.1 mAP vs. 54.4 mAP) with lower latency (8.8 ms vs. 10.70 ms).


4.3
Discussions


NMS post-processing. The DETR method is an end-to-end algorithm that
does not need the NMS post-processing procedure. In contrast, existing real-
time detectors, such as YOLO-NAS [1], YOLOv8 [29], and RTMDet [46], needs
NMS [24] post-processing. The NMS procedure takes extra time. We include
the extra time for measuring the end-to-end inference cost, which is counted in


LW-DETR
11


Table 4: Comparisons with concurrent works, including YOLO-MS [12], Gold-
YOLO [58], YOLOv10 [57], and RT-DETR [45] on COCO. For YOLO-MS and Gold-
YOLO, we measure the total latency in two settings for NMS: official implementation
and tuned score threshold. For YOLOv10, we report the results in the official paper [57].
RT-DETR is based on DETR, and the total latency is equal to the model latency. We
provide the best latency among the reported inference time in the paper [45] and the
measured time in our environment for RT-DETR. LW-DETR consistently gets superior
results. ‘pretraining’ means that the results are based on pretraining on Objects365.


Method
pretraining
#Params


(M)


FLOPs


(G)


Model
Latency


(ms)


official implementation
tuned score threshold
Total Latency


(ms)
mAP
Total Latency


(ms)
mAP


YOLO-MS-XS
4.5
8.7
3.0
6.9
43.4
3.2
43.3


YOLO-MS-XS
✓
4.5
8.7
3.0
6.9
43.9
3.2
43.8


YOLO-MS-S
8.1
15.6
5.4
9.2
46.2
5.6
46.1


YOLO-MS-S
✓
8.1
15.6
5.4
9.2
46.8
5.6
46.7


YOLO-MS
22.0
40.1
8.6
12.3
51.0
9.0
50.8


Gold-YOLO-S
21.5
23.0
2.9
3.6
45.5
3.4
45.4


Gold-YOLO-S
✓
21.5
23.0
2.9
3.6
46.1
3.4
46.0


Gold-YOLO-M
41.3
43.8
5.8
6.3
50.2
6.1
50.2


Gold-YOLO-M
✓
41.3
43.8
5.8
6.3
50.4
6.1
50.3


Gold-YOLO-L
75.1
75.9
10.2
10.6
52.3
10.5
52.2


YOLOv10-N
2.3
6.7
-
1.84
38.5
-
-


YOLOv10-S
7.2
21.6
-
2.49
46.3
-
-


YOLOv10-M
15.4
59.1
-
4.74
51.1
-
-


YOLOv10-B
19.1
92.0
-
5.74
52.5
-
-


YOLOv10-L
24.4
120.3
-
7.28
53.2
-
-


YOLOv10-X
29.5
160.4
-
10.70
54.4
-
-


RT-DETR-R18
20
30.0
4.6
4.6
46.5
-
-


RT-DETR-R18
✓
20
30.0
4.6
4.6
49.2
-
-


RT-DETR-R50
42
69.4
9.3
9.3
53.1
-
-


RT-DETR-R50
✓
42
69.4
9.3
9.3
55.3
-
-


RT-DETR-R101
76
131.0
13.5
13.5
54.3
-
-


RT-DETR-R101
✓
76
131.0
13.5
13.5
56.2
-
-


LW-DETR-tiny
✓
12.1
11.2
2.0
2.0
42.6
-
-


LW-DETR-small
✓
14.6
16.6
2.9
2.9
48.0
-
-


LW-DETR-medium
✓
28.2
42.8
5.6
5.6
52.5
-
-


LW-DETR-large
✓
46.8
71.6
8.8
8.8
56.1
-
-


LW-DETR-xlarge
✓
118.0
174.2
19.1
19.1
58.3
-
-


real-world application. The results using the NMS setting in the official imple-
mentations are shown in Figure 1 and Table 3.


We further make improvements for the methods with NMS by tuning the
classification score threshold for the NMS post-processing. We observe that the
default score threshold, 0.001, in YOLO-NAS, YOLOv8, and RTMDet, results
in a high mAP, but a large number of boxes and thus high latency. In particular,
when the model is small, the end-to-end latency is dominated by the NMS la-
tency. We tune the threshold, obtaining a good balance between the mAP score
and the latency. It is observed that the mAP scores are slightly dropped, e.g.,
by −0.1 mAP to −0.5 mAP, and the running times are largely reduced, e.g.,
with a reduction of 4∼5 ms for RTMDet and YOLOv8, a reduction of 1∼2 ms
for YOLO-NAS. These reductions are from that fewer predicted boxes are fed
into NMS after tuning the score threshold. Detailed results with different score
thresholds, along with the distribution of the number of remaining boxes across
the COCO val2017 are given in the Supplementary Material.


12
Q. Chen et al.


0
5
10
15


40


45


50


55


59


Inference Time (ms)


mAP


LW-DETR


RT-DETR


YOLO-MS*


Gold-YOLO*


YOLO-MS


Gold-YOLO


YOLOv10


Fig. 4: Our approach outperforms concurrent works. The x-axis corresponds
to the inference time. The y-axis corresponds to the mAP score on COCO val2017.
Our LW-DETR, RT-DETR [45], YOLO-MS [12], and Gold-YOLO [58] are trained with
pretraining on Objects365, while YOLOv10 [57] is not. The NMS post-processing times
are included for YOLO-MS and Gold-YOLO, and measured on the COCO val2017
with the setting from the official implementation, and the well-tuned NMS postpro-
cessing setting (labeled as “*").


Table 5: The effect of pertaining in our LW-DETR. Pretraining on Objects365
improves our approach a lot. This observation is consistent with the observations from
methods with large models [7,67,75].


LW-DETR
#Params (M)
FLOPs (G)
Latency (ms)
mAP w/o pretraining
mAP w/ pretraining


tiny
12.1
11.2
2.0
36.5
42.6


small
14.6
16.6
2.9
43.6
48.0


medium
28.2
42.8
5.6
47.2
52.5


large
46.8
71.6
8.8
49.5
56.1


xlarge
118.0
174.2
19.1
53.0
58.3


R18
21.2
21.4
2.5
40.9
44.4


R50
54.6
67.7
8.7
49.7
54.4


Figure 1 shows the comparison against other methods with well-tuned NMS
procedures. The methods with NMS are improved. Our approach still outper-
forms other methods. The second-best approach, YOLO-NAS, is a network ar-
chitecture search algorithm and performs very closely to the proposed baseline.
We believe that the complicated network architecture search procedure, like the
one used in YOLO-NAS, potentially benefits the DETR approach, and further
improvement is expected.


Pretraining. We empirically study the effect of pretraining. The results, shown
in Table 5, indicate that pretraining leads to significant improvements for our
approaches, with an average improvement of 5.5 mAP. The tiny model gets an
mAP gain of 6.1, and the xlarge model gets an mAP gain of 5.3. This implies
that pretraining on a large dataset is highly beneficial for DETR-based models.


LW-DETR
13


Table 6:
The effect of pertaining along with training epochs for non-end-
to-end detectors.


Model
pretraining
20 epochs
60 epochs
100 epochs
200 epochs
300 epochs
500 epochs


YOLOv8n
26.2
30.1
32.3
34.0
35.0
37.4


YOLOv8n
✓
31.5
32.8
33.2
34.3
35.2
37.6


RTMDet-t
30.4
34.2
35.2
36.8
41.0
-


RTMDet-t
✓
33.4
36.5
36.7
37.5
41.7
-


YOLO-MS-XS
24.7
34.3
36.4
39.2
43.4
-


YOLO-MS-XS
✓
37.5
38.6
39.1
40.0
43.9
-


Gold-YOLO-S
33.4
37.1
38.2
43.6
45.5
-


Gold-YOLO-S
✓
39.3
41.3
42.1
44.9
46.1
-


We further show that the training procedure applies to the DETR approach
with convolutional encoders. We replace transformer encoders with ResNet-18
and ResNet-50. One can see that in Table 5, the results of these LW-DETR
variants are close to LW-DETR with transformer encoders in terms of latency
and mAP, and the pretraining brings benefits that are similar to and a little
lower than LW-DETR with transformer encoders.


Meanwhile, we investigate the pretraining improvements on non-end-to-end
detectors. According to the results in Table 3, Table 4 and Table 6, it seems
that pretraining on Objects365 only show limited gains for non-end-to-end de-
tectors [12, 29, 46, 58], which is different from the phenomenon in DETR-based
detectors, where pretraining give large improvements. As the non-end-to-end de-
tectors train 300 epochs even 500 epochs in YOLOv8, we wonder if the limited
gain is related to the training epochs. We compare the improvements brought by
the pretrained weights along with the training epochs. Table 6 shows that the
improvements diminished along with the training epochs, which partly supports
the above hypothesis. The above illustration is a preliminary step. We believe
that more investigations are needed to figure out the underlying reasons for the
difference in benefits of pretraining.


4.4
Experiments on more datasets


We test the generalizability of our LW-DETR on more detection datasets. We
consider two types of evaluation methods, cross-domain evaluation and multi-
domain finetuning. For cross-domain evaluation, we directly evaluate the real-
time detectors trained on COCO on the Unidentified Video Objects (UVO) [61].
For multi-domain fine-tuning, we finetune the pretrained real-time detectors on
the multi-domain detection dataset Roboflow 100 (RF100) [13]. We do a coarse
search on the hyperparameters on each dataset for all models, such as the learn-
ing rate. Please refer to the Supplementary Material for more details.


Cross-domain evaluation. One possible way to evaluate the generalizability of
the models is to directly evaluate them on the datasets with different domains.
We adopt a class-agnostic object detection benchmark, UVO [61], where 57%
object instances do not belong to any of the 80 COCO classes. UVO is based
on YouTube videos, whose appearance is very different from COCO, e.g., some


14
Q. Chen et al.


Table 7: Cross-domain evaluation on UVO. We evaluate the performance in a
class-agnostic way as UVO is class-agnostic. LW-DETR demonstrates higher AP and
AR than other detectors.


Method
mAP
AP50
AR@100
ARs
ARm
ARl


RTMDet-s
29.7
43.3
55.7
26.5
49.4
71.5


YOLOv8-s
29.1
42.4
54.3
27.4
48.6
68.8


YOLO-NAS-s
31.0
44.5
55.1
25.8
48.1
71.6


LW-DETR-small
32.3
45.1
59.8
29.4
52.4
77.1


Table 8: Multi-domain finetuning on RF100. We compare our LW-DETR with
previous real-time detectors, including YOLOv5, YOLOv7, RTMDet, YOLOv8, and
YOLO-NAS on all data domains of RF100. Gray entries are the results from the RF100
paper [13]. The data domains are aerial, videogames, microscopic, underwater, doc-
uments, electromagnetic, and real world. The AP50 metric is used. ‘-’ means that
YOLO-NAS [1] does not report their detailed results.


Method
Average
Domains in Roboflow 100


aerial
videogames
microscopic
underwater
documents
electromagnetic
real world


YOLOv5-s
73.4
63.6
85.9
65.0
56.0
71.6
74.2
76.9


YOLOv7-s
67.4
50.4
79.6
59.1
66.2
72.2
63.9
70.5


RTMDet-s
79.2
70.1
88.0
68.1
68.0
81.0
77.4
83.3


YOLOv8-s
80.1
70.7
87.9
74.7
70.2
79.8
79.0
82.9


YOLO-NAS-s
81.5
-
-
-
-
-
-
-


YOLO-NAS-m
81.8
-
-
-
-
-
-
-


LW-DETR-small
82.5
71.8
88.9
74.5
69.6
86.7
84.6
85.3


LW-DETR-medium
83.5
72.9
90.8
75.4
70.5
86.1
86.2
86.4


videos are in egocentric views and have significant motion blur. We evaluate the
models trained with COCO (taken from Table 3) on the validation split of UVO.


Table 7 provides the results. LW-DETR excels over competing SoTA real-
time detectors. Specifically, LW-DETR-small is 1.3 mAP and 4.1 AR higher
than the best result among RTMDet-s, YOLOv8-s, and YOLO-NAS-s. In terms
of recall, it also shows enhanced abilities to detect more objects across different
scales: small, medium, and large. The above findings imply that the superiority
of our LW-DETR over previous real-time detectors is attributed not to specific
tuning for COCO, but to its capacity for producing more generalizable models.


Multi-domain finetuning. Another way is to finetune the pretrained detectors
on small datasets across different domains. RF100 consists of 100 small datasets,
7 imagery domains, 224k images, and 829 class labels. It can help researchers
test the model’s generalizability with real-life data. We finetune the real-time
detectors on each small dataset of RF100.


The results are given in Table 8. LW-DETR-small shows superiority over
current state-of-the-art real-time detectors across different domains. In partic-
ular, for the ‘documents’ and the ‘electromagnetic’ domains, our LW-DETR is
significantly better than YOLOv5, YOLOv7, RTMDet, and YOLOv8 (5.7 AP
and 5.6 AP higher than the best among the four). LW-DETR-medium can give
further improvements overall. These findings highlight the versatility of our LW-
DETR, positioning it as a strong baseline in a range of closed-domain tasks.


LW-DETR
15


5
Limitation and future works


Currently, we only demonstrate the effectiveness of LW-DETR in real-time de-
tection. This is the first step. Extending LW-DETR for open-world detection and
applying LW-DETR to more vision tasks, such as multi-person pose estimation
and multi-view 3D object detection, needs more investigation. We leave them
for future work.


6
Conclusion


This paper shows that detection transformers achieve competitive and even supe-
rior results over existing real-time detectors. Our method is simple and efficient.
The success stems from multi-level feature aggregation and training-effective and
inference-efficient techniques. We hope our experience can provide insights for
building real-time models with transformers in vision tasks.


References


1. Aharon, S., Louis-Dupont, Ofri Masad, Yurkova, K., Lotem Fridman, Lkdci,
Khvedchenya, E., Rubin, R., Bagrov, N., Tymchenko, B., Keren, T., Zhilko, A.,
Eran-Deci: Super-gradients (2021). https://doi.org/10.5281/ZENODO.7789328,
https://zenodo.org/record/7789328
2. Bochkovskiy, A., Wang, C.Y., Liao, H.Y.M.: Yolov4: Optimal speed and accuracy
of object detection. arXiv preprint arXiv:2004.10934 (2020)
3. Cai, Z., Liu, S., Wang, G., Ge, Z., Zhang, X., Huang, D.: Align-detr: Improving
detr with simple iou-aware bce loss. arXiv preprint arXiv:2304.07527 (2023)
4. Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., Zagoruyko, S.: End-
to-end object detection with transformers. In: European conference on computer
vision. pp. 213–229. Springer (2020)
5. Chang, J., Wang, S., Xu, H.M., Chen, Z., Yang, C., Zhao, F.: Detrdistill: A uni-
versal knowledge distillation framework for detr-families. In: Proceedings of the
IEEE/CVF International Conference on Computer Vision. pp. 6898–6908 (2023)
6. Chen, Q., Chen, X., Wang, J., Zhang, S., Yao, K., Feng, H., Han, J., Ding, E.,
Zeng, G., Wang, J.: Group detr: Fast detr training with group-wise one-to-many
assignment. In: Proceedings of the IEEE International Conference on Computer
Vision (ICCV) (2023)
7. Chen, Q., Wang, J., Han, C., Zhang, S., Li, Z., Chen, X., Chen, J., Wang, X., Han,
S., Zhang, G., et al.: Group detr v2: Strong object detector with encoder-decoder
pretraining. arXiv preprint arXiv:2211.03594 (2022)
8. Chen, W., Du, X., Yang, F., Beyer, L., Zhai, X., Lin, T.Y., Chen, H., Li, J., Song,
X., Wang, Z., et al.: A simple single-scale vision transformer for object localization
and instance segmentation. arXiv preprint arXiv:2112.09747 (2021)
9. Chen, X., Chen, J., Liu, Y., Zeng, G.: D3 etr: Decoder distillation for detection
transformer. arXiv preprint arXiv:2211.09768 (2022)
10. Chen, X., Ding, M., Wang, X., Xin, Y., Mo, S., Wang, Y., Han, S., Luo, P., Zeng, G.,
Wang, J.: Context autoencoder for self-supervised representation learning. arXiv
preprint arXiv:2202.03026 (2022)


16
Q. Chen et al.


11. Chen, X., Wei, F., Zeng, G., Wang, J.: Conditional detr v2: Efficient detection
transformer with box queries. arXiv preprint arXiv:2207.08914 (2022)
12. Chen, Y., Yuan, X., Wu, R., Wang, J., Hou, Q., Cheng, M.M.: Yolo-ms: Rethinking
multi-scale representation learning for real-time object detection. arXiv preprint
arXiv:2308.05480 (2023)
13. Ciaglia, F., Zuppichini, F.S., Guerrie, P., McQuade, M., Solawetz, J.: Roboflow 100:
A rich, multi-domain object detection benchmark. arXiv preprint arXiv:2211.13523
(2022)
14. Clark, K., Luong, M.T., Le, Q.V., Manning, C.D.: Electra: Pre-training text en-
coders as discriminators rather than generators. arXiv preprint arXiv:2003.10555
(2020)
15. Deng, J., Dong, W., Socher, R., Li, L.J., Li, K., Fei-Fei, L.: Imagenet: A large-
scale hierarchical image database. In: 2009 IEEE conference on computer vision
and pattern recognition. pp. 248–255. Ieee (2009)
16. Ding, X., Zhang, X., Ma, N., Han, J., Ding, G., Sun, J.: Repvgg: Making vgg-style
convnets great again. In: Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition. pp. 13733–13742 (2021)
17. Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner,
T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., et al.: An image is
worth 16x16 words: Transformers for image recognition at scale. arXiv preprint
arXiv:2010.11929 (2020)
18. Feng, D., Haase-Schütz, C., Rosenbaum, L., Hertlein, H., Glaeser, C., Timm, F.,
Wiesbeck, W., Dietmayer, K.: Deep multi-modal object detection and semantic
segmentation for autonomous driving: Datasets, methods, and challenges. IEEE
Transactions on Intelligent Transportation Systems 22(3), 1341–1360 (2020)
19. Gao, Z., Wang, L., Han, B., Guo, S.: Adamixer: A fast-converging query-based
object detector. In: Proceedings of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition. pp. 5364–5373 (2022)
20. Ge, Z., Liu, S., Wang, F., Li, Z., Sun, J.: Yolox: Exceeding yolo series in 2021.
arXiv preprint arXiv:2107.08430 (2021)
21. Hatamizadeh, A., Heinrich, G., Yin, H., Tao, A., Alvarez, J.M., Kautz, J.,
Molchanov, P.: Fastervit: Fast vision transformers with hierarchical attention.
arXiv preprint arXiv:2306.06189 (2023)
22. He, K., Chen, X., Xie, S., Li, Y., Dollár, P., Girshick, R.: Masked autoencoders are
scalable vision learners. In: Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition. pp. 16000–16009 (2022)
23. He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition. In:
Proceedings of the IEEE conference on computer vision and pattern recognition.
pp. 770–778 (2016)
24. Hosang, J., Benenson, R., Schiele, B.: Learning non-maximum suppression. In:
Proceedings of the IEEE conference on computer vision and pattern recognition.
pp. 4507–4515 (2017)
25. Hu, Y., Yang, J., Chen, L., Li, K., Sima, C., Zhu, X., Chai, S., Du, S., Lin, T.,
Wang, W., et al.: Planning-oriented autonomous driving. In: Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 17853–
17862 (2023)
26. Huang, G., Liu, Z., Van Der Maaten, L., Weinberger, K.Q.: Densely connected
convolutional networks. In: Proceedings of the IEEE conference on computer vision
and pattern recognition. pp. 4700–4708 (2017)


LW-DETR
17


27. Jia, D., Yuan, Y., He, H., Wu, X., Yu, H., Lin, W., Sun, L., Zhang, C., Hu, H.:
Detrs with hybrid matching. In: Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition. pp. 19702–19712 (2023)
28. Jocher, G.: Ultralytics yolov5 (2020), https://github.com/ultralytics/yolov5
29. Jocher, G., Chaurasia, A., Qiu, J.: Ultralytics yolov8 (2023), https://github.
com/ultralytics/ultralytics
30. Karaoguz, H., Jensfelt, P.: Object detection approach for robot grasp detection.
In: 2019 International Conference on Robotics and Automation (ICRA). pp. 4953–
4959. IEEE (2019)
31. Li, B., Ouyang, W., Sheng, L., Zeng, X., Wang, X.: Gs3d: An efficient 3d object
detection framework for autonomous driving. In: Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition. pp. 1019–1028 (2019)
32. Li, C., Li, L., Geng, Y., Jiang, H., Cheng, M., Zhang, B., Ke, Z., Xu, X., Chu, X.:
Yolov6 v3. 0: A full-scale reloading. arXiv preprint arXiv:2301.05586 (2023)
33. Li, C., Li, L., Jiang, H., Weng, K., Geng, Y., Li, L., Ke, Z., Li, Q., Cheng, M.,
Nie, W., et al.: Yolov6: A single-stage object detection framework for industrial
applications. arXiv preprint arXiv:2209.02976 (2022)
34. Li, F., Zeng, A., Liu, S., Zhang, H., Li, H., Zhang, L., Ni, L.M.: Lite detr: An
interleaved multi-scale encoder for efficient detr. In: Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition. pp. 18558–18567 (2023)
35. Li, F., Zhang, H., Liu, S., Guo, J., Ni, L.M., Zhang, L.: Dn-detr: Accelerate detr
training by introducing query denoising. In: Proceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition. pp. 13619–13627 (2022)
36. Li, Y., Mao, H., Girshick, R., He, K.: Exploring plain vision transformer backbones
for object detection. In: European Conference on Computer Vision. pp. 280–296.
Springer (2022)
37. Li, Y., Xie, S., Chen, X., Dollar, P., He, K., Girshick, R.: Benchmarking detection
transfer learning with vision transformers. arXiv preprint arXiv:2111.11429 (2021)
38. Lin, T.Y., Goyal, P., Girshick, R., He, K., Dollár, P.: Focal loss for dense object
detection. In: Proceedings of the IEEE international conference on computer vision.
pp. 2980–2988 (2017)
39. Lin, T.Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollár, P.,
Zitnick, C.L.: Microsoft coco: Common objects in context. In: Computer Vision–
ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12,
2014, Proceedings, Part V 13. pp. 740–755. Springer (2014)
40. Lin, Y., Yuan, Y., Zhang, Z., Li, C., Zheng, N., Hu, H.: Detr doesn’t need multi-
scale or locality design. arXiv preprint arXiv:2308.01904 (2023)
41. Liu, S., Li, F., Zhang, H., Yang, X., Qi, X., Su, H., Zhu, J., Zhang, L.: Dab-detr:
Dynamic anchor boxes are better queries for detr. arXiv preprint arXiv:2201.12329
(2022)
42. Liu, S., Ren, T., Chen, J., Zeng, Z., Zhang, H., Li, F., Li, H., Huang, J., Su,
H., Zhu, J., et al.: Detection transformer with stable matching. arXiv preprint
arXiv:2304.04742 (2023)
43. Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., Lin, S., Guo, B.: Swin
transformer: Hierarchical vision transformer using shifted windows. In: Proceedings
of the IEEE/CVF international conference on computer vision. pp. 10012–10022
(2021)
44. Loshchilov, I., Hutter, F.: Decoupled weight decay regularization. arXiv preprint
arXiv:1711.05101 (2017)


18
Q. Chen et al.


45. Lv, W., Xu, S., Zhao, Y., Wang, G., Wei, J., Cui, C., Du, Y., Dang, Q., Liu, Y.:
Detrs beat yolos on real-time object detection. arXiv preprint arXiv:2304.08069
(2023)
46. Lyu, C., Zhang, W., Huang, H., Zhou, Y., Wang, Y., Liu, Y., Zhang, S., Chen, K.:
Rtmdet: An empirical study of designing real-time object detectors. arXiv preprint
arXiv:2212.07784 (2022)
47. Meng, D., Chen, X., Fan, Z., Zeng, G., Li, H., Yuan, Y., Sun, L., Wang, J.: Con-
ditional detr for fast training convergence. In: Proceedings of the IEEE/CVF In-
ternational Conference on Computer Vision. pp. 3651–3660 (2021)
48. Ouyang-Zhang, J., Cho, J.H., Zhou, X., Krähenbühl, P.: Nms strikes back. arXiv
preprint arXiv:2212.06137 (2022)
49. Paul, S.K., Chowdhury, M.T., Nicolescu, M., Nicolescu, M., Feil-Seifer, D.: Object
detection and pose estimation from rgb and depth data for real-time, adaptive
robotic grasping. In: Advances in Computer Vision and Computational Biology:
Proceedings from IPCV’20, HIMS’20, BIOCOMP’20, and BIOENG’20, pp. 121–
142. Springer (2021)
50. Redmon, J., Divvala, S., Girshick, R., Farhadi, A.: You only look once: Unified,
real-time object detection. In: Proceedings of the IEEE conference on computer
vision and pattern recognition. pp. 779–788 (2016)
51. Ren, S., He, K., Girshick, R., Sun, J.: Faster r-cnn: Towards real-time object de-
tection with region proposal networks. Advances in neural information processing
systems 28 (2015)
52. Rezatofighi, H., Tsoi, N., Gwak, J., Sadeghian, A., Reid, I., Savarese, S.: General-
ized intersection over union: A metric and a loss for bounding box regression. In:
Proceedings of the IEEE/CVF conference on computer vision and pattern recog-
nition. pp. 658–666 (2019)
53. Roh, B., Shin, J., Shin, W., Kim, S.: Sparse detr: Efficient end-to-end object de-
tection with learnable sparsity. arXiv preprint arXiv:2111.14330 (2021)
54. Shao, S., Li, Z., Zhang, T., Peng, C., Yu, G., Zhang, X., Li, J., Sun, J.: Objects365:
A large-scale, high-quality dataset for object detection. In: Proceedings of the
IEEE/CVF international conference on computer vision. pp. 8430–8439 (2019)
55. Tarvainen, A., Valpola, H.: Mean teachers are better role models: Weight-averaged
consistency targets improve semi-supervised deep learning results. Advances in
neural information processing systems 30 (2017)
56. Tian, Z., Shen, C., Chen, H., He, T.: Fcos: Fully convolutional one-stage object
detection. In: Proceedings of the IEEE/CVF international conference on computer
vision. pp. 9627–9636 (2019)
57. Wang, A., Chen, H., Liu, L., Chen, K., Lin, Z., Han, J., Ding, G.: Yolov10: Real-
time end-to-end object detection. arXiv preprint arXiv:2405.14458 (2024)
58. Wang, C., He, W., Nie, Y., Guo, J., Liu, C., Han, K., Wang, Y.: Gold-yolo:
Efficient object detector via gather-and-distribute mechanism. arXiv preprint
arXiv:2309.11331 (2023)
59. Wang, C.Y., Bochkovskiy, A., Liao, H.Y.M.: Yolov7: Trainable bag-of-freebies
sets new state-of-the-art for real-time object detectors. In: Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 7464–
7475 (2023)
60. Wang, C.Y., Liao, H.Y.M., Wu, Y.H., Chen, P.Y., Hsieh, J.W., Yeh, I.H.: Cspnet:
A new backbone that can enhance learning capability of cnn. In: Proceedings of
the IEEE/CVF conference on computer vision and pattern recognition workshops.
pp. 390–391 (2020)


LW-DETR
19


61. Wang, W., Feiszli, M., Wang, H., Tran, D.: Unidentified video objects: A bench-
mark for dense, open-world segmentation. In: Proceedings of the IEEE/CVF In-
ternational Conference on Computer Vision. pp. 10776–10785 (2021)
62. Wang, W., Xie, E., Li, X., Fan, D.P., Song, K., Liang, D., Lu, T., Luo, P., Shao,
L.: Pyramid vision transformer: A versatile backbone for dense prediction with-
out convolutions. In: Proceedings of the IEEE/CVF international conference on
computer vision. pp. 568–578 (2021)
63. Wang, Y., Zhang, X., Yang, T., Sun, J.: Anchor detr: Query design for transformer-
based detector. In: Proceedings of the AAAI conference on artificial intelligence.
vol. 36, pp. 2567–2575 (2022)
64. Wang, Y., Li, X., Wen, S., Yang, F., Zhang, W., Zhang, G., Feng, H., Han, J., Ding,
E.: Knowledge distillation for detection transformer with consistent distillation
points sampling. arXiv preprint arXiv:2211.08071 (2022)
65. Xu, S., Wang, X., Lv, W., Chang, Q., Cui, C., Deng, K., Wang, G., Dang, Q.,
Wei, S., Du, Y., et al.: Pp-yoloe: An evolved version of yolo. arXiv preprint
arXiv:2203.16250 (2022)
66. Zhai, X., Kolesnikov, A., Houlsby, N., Beyer, L.: Scaling vision transformers. In:
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recog-
nition. pp. 12104–12113 (2022)
67. Zhang, H., Li, F., Liu, S., Zhang, L., Su, H., Zhu, J., Ni, L.M., Shum, H.Y.: Dino:
Detr with improved denoising anchor boxes for end-to-end object detection. arXiv
preprint arXiv:2203.03605 (2022)
68. Zhang, H., Wang, Y., Dayoub, F., Sunderhauf, N.: Varifocalnet: An iou-aware
dense object detector. In: Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition. pp. 8514–8523 (2021)
69. Zhang, H., Cisse, M., Dauphin, Y.N., Lopez-Paz, D.: mixup: Beyond empirical risk
minimization. arXiv preprint arXiv:1710.09412 (2017)
70. Zhang, X., Tian, Y., Huang, W., Ye, Q., Dai, Q., Xie, L., Tian, Q.: Hivit:
Hierarchical vision transformer meets masked image modeling. arXiv preprint
arXiv:2205.14949 (2022)
71. Zhang, X., Chen, J., Yuan, J., Chen, Q., Wang, J., Wang, X., Han, S., Chen, X.,
Pi, J., Yao, K., Han, J., Ding, E., Wang, J.: CAE v2: Context autoencoder with
CLIP latent alignment. Transactions on Machine Learning Research (2023)
72. Zheng, D., Dong, W., Hu, H., Chen, X., Wang, Y.: Less is more: Focus attention
for efficient detr. In: Proceedings of the IEEE/CVF International Conference on
Computer Vision. pp. 6674–6683 (2023)
73. Zheng, Z., Wang, P., Liu, W., Li, J., Ye, R., Ren, D.: Distance-iou loss: Faster
and better learning for bounding box regression. In: Proceedings of the AAAI
conference on artificial intelligence. vol. 34, pp. 12993–13000 (2020)
74. Zhu, X., Su, W., Lu, L., Li, B., Wang, X., Dai, J.: Deformable detr: Deformable
transformers for end-to-end object detection. arXiv preprint arXiv:2010.04159
(2020)
75. Zong, Z., Song, G., Liu, Y.: Detrs with collaborative hybrid assignments training.
In: Proceedings of the IEEE/CVF International Conference on Computer Vision.
pp. 6748–6758 (2023)


20
Q. Chen et al.


Supplementary Material


A
Experimental Details


This section includes details on the hyper-parameters of pretraining on Ob-
jects365 [54], finetuning on COCO [39], and finetuning on Roboflow 100 [13],
on the architectures of convolutional encoders, and on the modeling of box re-
gression. We represent the tiny/small/medium/large/xlarge versions of our
LW-DETR with T/S/M/L/X in the tables for neat representations.


A.1
Experimental settings


Pretraining settings. The default settings are in Table 9. We do not use the
learning rate drop schedule and keep the initial learning rate along with the
training process. When performing window attention in the ViT encoder, we fix
the number of windows as 16 for different image resolutions for easy implementa-
tion. We use layer-wise lr decay [14] following previous MIM methods [10,22,71].


Table 9: Pretraining settings.


Setting
Value


optimizer
AdamW


base learning rate
4.0 × e−4


encoder learning rate
6.0 × e−4


weight decay
1 × e−4


batch size
128


epochs
30


training images resolutions
[448, 512, 576, 640, 704, 768, 832, 896]


encoder layer-wise lr decay
0.8 (T/S), 0.7 (M/L), 0.75 (X)


number of encoder layers
6 (T), 10(S/M/L/X)


drop path
0 (T/S/M), 0.05 (L/X)


window numbers
16


window attention indexes
[0, 2, 4] (T), [0, 1, 3, 6, 7, 9] (S/M/L/X)


output feature indexes
[0, 2, 4] (T), [2, 4, 5, 9] (S/M/L/X)


feature scales
1
16 (T/S/M), [ 1
8 ,
1
32 ] (L/X)


number of object queries
100 (T), 300 (S/M/L/X)


number of decoder layers
3


hidden dimensions
256 (T/S/M), 384 (L/X)


decoder self-attention heads
8 (T/S/M), 12 (L/X)


decoder cross-attention heads
16 (T/S/M), 24 (L/X)


decoder sampling points
2 (T/S/M), 4 (L/X)


group detr
13


ema decay
0.997


COCO experimental settings. Most of the settings follow the ones in the
pretraining stage. We share the modifications of settings in Table 10. When
finetuning LW-DETR on COCO, we use component-wise lr decay [7], which gives
different scale factors for the learning rate in the ViT encoder, the Projector, and
the DETR decoder. For example, the component-wise lr decay is 0.7 means that
we set the lr scale factor as 0.70 for the prediction heads, 0.71 for the transformer
decoder layers in DETR decoder, 0.72 for the Projector, and 0.73 for the ViT
encoder.


LW-DETR
21


Table 10: COCO experimental settings.


Setting
Value


base learning rate
1.0 × e−4


encoder learning rate
1.5 × e−4


weight decay
1 × e−4 (T/S/M/L), 1 × e−3 (X)


batch size
32 (T/S/M), 16 (L/X)


epochs
50 (T/S/M), 25 (L/X)


drop path
0 (T/S/M), 0.1 (L/X)


component-wise lr decay
0.7 (T/S/M), 0.5 (L/X)


Table 11: Roboflow 100 experimental settings.


Setting
Value


base learning rate
8.0 × e−4 (S), 3.0 × e−4 (M)


batch size
16 (S/M)


encoder learning rate
1.2 × e−3 (S), 4.5 × e−4 (M)


encoder layer-wise lr decay
0.9 (S), 0.8 (M)


component-wise lr decay
0.7 (S), 0.9 (M)


Roboflow 100 experimental settings. Roboflow 100 [13] consists of 100 small
datasets. We finetune our LW-DETR on these datasets based on the pretrained
model on Objects365 [54]. As the training images are insufficient, we set the
batch size as 16 and finetune the model for 100 epochs following [13] on all small
datasets to make sure to have sufficient training iterations.


We tune the learning rate, encoder layer-wise lr decay, and component-wise lr
decay (as shown in Table 11), we do a coarse search on the ‘microscopic’ domain
and fix these hyper-parameters for other datasets. The other hyper-parameters
are kept same with the finetuning experiments on COCO. We also perform the
same processes for RTMDet [46] and YOLOv8 [29] for fair comparisons.


A.2
Settings for convolutional encoders


We also explore convolutional encoders, ResNet-18 and ResNet-50, in our LW-
DETR. We load the ImageNet [15] pretrained encoder weights from the RT-
DETR repo7. Instead of directly outputting multi-level feature maps with scales
of [ 1


8, 1
16, 1
32], we make a simple modification to only output a feature map in
1
16.
We first upsample the feature map in
1
32 scale to
1
16, downsample the feature map
in 1


8 to
1
16, and then concatenates all the feature maps. We add additional con-
volution layers to reduce the feature dimension to prevent the final concatenated
feature map from having extremely large feature dimensions.


A.3
Box regression target reparameterization


Box regression target parameterization is a widely used technique in two-stage
and one-stage detectors [2, 28, 38, 51], which predicts the parameters for a box
transformation that transforms an input proposal into a predicted box. We follow
Plain DETR [40] to use this technique in our LW-DETR.


For box regression in the first stage and each decoder layer, we predict
four parameters [δx, δy, δw, δh] to a transformation, which transforms a proposal


7 https://github.com/lyuwenyu/RT-DETR/issues/42#issue-1860463373


22
Q. Chen et al.


Table 12: Tuning score threshold for non-end-to-end detectors. We show
how the score threshold affects the time of NMS and the detection performance in
YOLO-NAS, YOLOv8, RTMDet, YOLO-MS, and Gold-YOLO. We share the detection
performance and total latency under three different score thresholds. The first score
threshold is the default one in the official implementations. The score threshold in bold
represents a good balance between the mAP score and the NMS latency.


Model
Model Latency


(ms)
mAP
Total Latency


(ms)
mAP
Total Latency


(ms)
mAP
Total Latency


(ms)


Thresholds
score = 0.018
score =0.1
score = 0.15


YOLO-NAS-s
2.75
47.6
4.68
47.3
2.88
46.7
2.82


YOLO-NAS-m
5.52
51.6
7.76
51.1
5.70
50.6
5.53


YOLO-NAS-l
7.49
52.3
8.84
51.9
7.64
51.2
7.52


Thresholds
score = 0.001
score =0.01
score = 0.05


YOLOv8n
1.51
37.4
6.21
37.3
1.62
36.0
1.54


YOLOv8s
2.64
45.0
7.00
44.8
2.71
43.7
2.70


YOLOv8m
5.90
50.3
10.11
50.0
6.06
49.0
5.92


YOLOv8l
9.30
53.0
13.16
52.5
9.44
51.3
9.31


YOLOv8x
14.88
54.0
19.17
53.5
15.09
52.3
14.91


Thresholds
score = 0.001
score =0.1
score = 0.25


RTMDet-t
2.16
41.0
7.41
40.8
2.45
39.1
2.37


RTMDet-s
2.88
44.6
7.88
44.4
2.94
42.6
2.93


RTMDet-m
6.27
49.3
10.82
49.1
6.52
47.2
6.31


RTMDet-l
10.37
51.4
14.84
51.2
10.54
49.2
10.48


RTMDet-x
18.44
52.8
22.81
52.5
18.88
50.5
18.69


Thresholds
score = 0.001
score =0.1
score = 0.25


YOLO-MS-XS
3.02
43.4
6.99
43.3
3.26
41.9
3.19


YOLO-MS-S
5.40
46.2
9.18
46.1
5.62
44.2
5.56


YOLO-MS
8.56
51.0
12.38
50.8
9.09
48.8
8.87


Thresholds
score = 0.03
score =0.05
score = 0.25


Gold-YOLO-S
2.94
45.5
3.63
45.4
3.35
43.1
3.08


Gold-YOLO-M
5.84
50.2
6.34
50.2
6.14
47.6
5.98


Gold-YOLO-L
10.15
52.3
10.58
52.2
10.46
50.5
10.22


[pcx, pcy, pw, ph] to a predicted bounding box [bcx, bcy, bw, bh] by applying:


  \ b eg i n { alig ned } b _ {c _ x} =


 \ d elta _x * p _w + p_{c_ x }, b_{c_y} = \delta _y * p_h + p_{c_y}, \\ b_w = \exp (\delta _w) * p_w, b_h = \exp (\delta _h) * p_h. \end {aligned} 
(6)


The predicted box [bcx, bcy, bw, bh] is used for calculating the box regression losses
and for output.


B
Analysis on NMS


Tuning score threshold. The score threshold in non-end-to-end detectors, de-
cides the number of predicted boxes that are passed to the NMS, which largely
affects the NMS latency. Table 12 verifies it with YOLO-NAS, YOLOv8, RT-
MDet, YOLO-MS, and Gold-YOLO. A large score threshold can largely reduce
the overhead of NMS, but bring negative results to detection performance. We
optimize the NMS latency by carefully tuning the score thresholds for non-end-
to-end detectors, achieving a balance between the detection performance and the


8 We have corrected a typo in the main paper regarding YOLO-NAS: the default score
threshold should be 0.01, not the value mentioned in L298.


LW-DETR
23


total latency. The overhead brought by NMS is significantly reduced to 0.1∼0.5
ms with slight drops in detection performance.
Distribution of the number of boxes for NMS. The latency is measured
on the COCO val2017, which is an average of 5000 images. Figure 5 gives the
distribution of the number of remaining boxes in NMS across the COCO val2017
under different score thresholds in YOLO-NAS. The large overhead brought by
the NMS is due to the large number of remaining boxes under the default score
threshold. Tuning the score threshold effectively decreases the remaining boxes in
NMS, thus providing optimization in total latency for non-end-to-end detectors.


0
100
500
1000 5000 30000


12
89


1,265


3,634


(a) YOLO-NAS-s score threshold = 0.01


0
100
500
1000 5000 30000


1,956
2,421


525
98


(b) YOLO-NAS-s score threshold = 0.1


0
100
500
1000 5000 30000


2,792


2,054


149
5


(c) YOLO-NAS-s score threshold = 0.15


Fig. 5: Distribution of the number of boxes. The x-axis corresponds to the number
of boxes that are fed into NMS. The y-axis corresponds to the number of images on
COCO val2017 whose remaining box numbers are in the corresponding interval. (a) is
under the default score threshold. (b) is tuning the score threshold to get the balance
between detection performance and latency. (c) is tuning a higher score threshold.
