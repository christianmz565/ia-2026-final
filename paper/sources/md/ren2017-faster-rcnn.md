# ren2017-faster-rcnn


<!-- Page 1 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


1


Faster R-CNN: Towards Real-Time Object


Detection with Region Proposal Networks


Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun


Abstract—State-of-the-art object detection networks depend on region proposal algorithms to hypothesize object locations. Advances like SPPnet [1] and Fast R-CNN [2] have reduced the running time of these detection networks, exposing region proposal computation as a bottleneck. In this work, we introduce a Region Proposal Network (RPN) that shares full-image convolutional features with the detection network, thus enabling nearly cost-free region proposals. An RPN is a fully convolutional network that simultaneously predicts object bounds and objectness scores at each position. The RPN is trained end-to-end to generate high-quality region proposals, which are used by Fast R-CNN for detection. We further merge RPN and Fast R-CNN into a single network by sharing their convolutional features—using the recently popular terminology of neural networks with ’attention’ mechanisms, the RPN component tells the uniﬁed network where to look. For the very deep VGG-16 model [3], our detection system has a frame rate of 5fps (including all steps) on a GPU, while achieving state-of-the-art object detection accuracy on PASCAL VOC 2007, 2012, and MS COCO datasets with only 300 proposals per image. In ILSVRC and COCO 2015 competitions, Faster R-CNN and RPN are the foundations of the 1st-place winning entries in several tracks. Code has been made publicly available.


Index Terms—Object Detection, Region Proposal, Convolutional Neural Network.


!


## 1 INTRODUCTION 1


One may note that fast region-based CNNs take 26 advantage of GPUs, while the region proposal meth27 ods used in research are implemented on the CPU, 28 making such runtime comparisons inequitable. An ob29 vious way to accelerate proposal computation is to re30 implement it for the GPU. This may be an effective en31 gineering solution, but re-implementation ignores the 32 down-stream detection network and therefore misses 33 important opportunities for sharing computation. 34 In this paper, we show that an algorithmic change— 35 computing proposals with a deep convolutional neu36 ral network—leads to an elegant and effective solution 37 where proposal computation is nearly cost-free given 38 the detection network’s computation. To this end, we 39 introduce novel Region Proposal Networks (RPNs) that 40 share convolutional layers with state-of-the-art object 41 detection networks [1], [2]. By sharing convolutions at 42 test-time, the marginal cost for computing proposals 43 is small (e.g., 10ms per image). 44 Our observation is that the convolutional feature 45 maps used by region-based detectors, like Fast R46 CNN, can also be used for generating region pro47 posals. On top of these convolutional features, we 48 construct an RPN by adding a few additional con49 volutional layers that simultaneously regress region 50 bounds and objectness scores at each location on a 51 regular grid. The RPN is thus a kind of fully convo52 lutional network (FCN) [7] and can be trained end-to53 end speciﬁcally for the task for generating detection 54 proposals. 55 RPNs are designed to efﬁciently predict region pro56 posals with a wide range of scales and aspect ratios. In 57 contrast to prevalent methods [8], [9], [1], [2] that use 58


Recent advances in object detection are driven by 2 the success of region proposal methods (e.g., [4]) 3 and region-based convolutional neural networks (R4 CNNs) [5]. Although region-based CNNs were com5 putationally expensive as originally developed in [5], 6 their cost has been drastically reduced thanks to shar7 ing convolutions across proposals [1], [2]. The latest 8 incarnation, Fast R-CNN [2], achieves near real-time 9 rates using very deep networks [3], when ignoring the 10 time spent on region proposals. Now, proposals are the 11 test-time computational bottleneck in state-of-the-art 12 detection systems. 13 Region proposal methods typically rely on inex14 pensive features and economical inference schemes. 15 Selective Search [4], one of the most popular meth16 ods, greedily merges superpixels based on engineered 17 low-level features. Yet when compared to efﬁcient 18 detection networks [2], Selective Search is an order of 19 magnitude slower, at 2 seconds per image in a CPU 20 implementation. EdgeBoxes [6] currently provides the 21 best tradeoff between proposal quality and speed, 22 at 0.2 seconds per image. Nevertheless, the region 23 proposal step still consumes as much running time 24 as the detection network. 25


• S. Ren is with University of Science and Technology of China, Hefei, China. This work was done when S. Ren was an intern at Microsoft Research. Email: sqren@mail.ustc.edu.cn • K. He and J. Sun are with Visual Computing Group, Microsoft Research. E-mail: {kahe,jiansun}@microsoft.com • R. Girshick is with Facebook AI Research. The majority of this work was done when R. Girshick was with Microsoft Research. E-mail: rbg@fb.com


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 2 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


feature map


multiple scaled images


image


2


multiple filter sizes


multiple references


feature map


feature map


image


image


(a) (b) (c)


Figure 1: Different schemes for addressing multiple scales and sizes. (a) Pyramids of images and feature maps are built, and the classiﬁer is run at all scales. (b) Pyramids of ﬁlters with multiple scales/sizes are run on the feature map. (c) We use pyramids of reference boxes in the regression functions.


pyramids of images (Figure 1, a) or pyramids of ﬁlters 59 (Figure 1, b), we introduce novel “anchor” boxes 60 that serve as references at multiple scales and aspect 61 ratios. Our scheme can be thought of as a pyramid 62 of regression references (Figure 1, c), which avoids 63 enumerating images or ﬁlters of multiple scales or 64 aspect ratios. This model performs well when trained 65 and tested using single-scale images and thus beneﬁts 66 running speed. 67 To unify RPNs with Fast R-CNN [2] object detec68 tion networks, we propose a training scheme that 69 alternates between ﬁne-tuning for the region proposal 70 task and then ﬁne-tuning for object detection, while 71 keeping the proposals ﬁxed. This scheme converges 72 quickly and produces a uniﬁed network with convo73 lutional features that are shared between both tasks.1 74 We comprehensively evaluate our method on the 75 PASCAL VOC detection benchmarks [11] where RPNs 76 with Fast R-CNNs produce detection accuracy bet77 ter than the strong baseline of Selective Search with 78 Fast R-CNNs. Meanwhile, our method waives nearly 79 all computational burdens of Selective Search at 80 test-time—the effective running time for proposals 81 is just 10 milliseconds. Using the expensive very 82 deep models of [3], our detection method still has 83 a frame rate of 5fps (including all steps) on a GPU, 84 and thus is a practical object detection system in 85 terms of both speed and accuracy. We also report 86 results on the MS COCO dataset [12] and investi87 gate the improvements on PASCAL VOC using the 88 COCO data. Code has been made publicly available 89 at https://github.com/shaoqingren/faster_ 90 rcnn (in MATLAB) and https://github.com/ 91 rbgirshick/py-faster-rcnn (in Python). 92 A preliminary version of this manuscript was pub93 lished previously [10]. Since then, the frameworks of 94 RPN and Faster R-CNN have been adopted and gen95 eralized to other methods, such as 3D object detection 96 [13], part-based detection [14], instance segmentation 97 [15], and image captioning [16]. Our fast and effective 98 object detection system has also been built in com99 mercial systems such as at Pinterests [17], with user 100


1. Since the publication of the conference version of this paper [10], we have also found that RPNs can be trained jointly with Fast R-CNN networks leading to less training time.


engagement improvements reported. 101 In ILSVRC and COCO 2015 competitions, Faster 102 R-CNN and RPN are the basis of several 1st-place 103 entries [18] in the tracks of ImageNet detection, Ima104 geNet localization, COCO detection, and COCO seg105 mentation. RPNs completely learn to propose regions 106 from data, and thus can easily beneﬁt from deeper 107 and more expressive features (such as the 101-layer 108 residual nets adopted in [18]). Faster R-CNN and RPN 109 are also used by several other leading entries in these 110 competitions2. These results suggest that our method 111 is not only a cost-efﬁcient solution for practical usage, 112 but also an effective way of improving object detec113 tion accuracy. 114


## 2 RELATED WORK 115


Object Proposals. There is a large literature on object 116 proposal methods. Comprehensive surveys and com117 parisons of object proposal methods can be found in 118 [19], [20], [21]. Widely used object proposal methods 119 include those based on grouping super-pixels (e.g., 120 Selective Search [4], CPMC [22], MCG [23]) and those 121 based on sliding windows (e.g., objectness in windows 122 [24], EdgeBoxes [6]). Object proposal methods were 123 adopted as external modules independent of the de124 tectors (e.g., Selective Search [4] object detectors, R125 CNN [5], and Fast R-CNN [2]). 126


Deep Networks for Object Detection. The R-CNN 127 method [5] trains CNNs end-to-end to classify the 128 proposal regions into object categories or background. 129 R-CNN mainly plays as a classiﬁer, and it does not 130 predict object bounds (except for reﬁning by bounding 131 box regression). Its accuracy depends on the perfor132 mance of the region proposal module (see compar133 isons in [20]). Several papers have proposed ways of 134 using deep networks for predicting object bounding 135 boxes [25], [9], [26], [27]. In the OverFeat method [9], 136 a fully-connected layer is trained to predict the box 137 coordinates for the localization task that assumes a 138 single object. The fully-connected layer is then turned 139 into a convolutional layer for detecting multiple class140 speciﬁc objects. The MultiBox methods [26], [27] gen141 erate region proposals from a network whose last 142


2. http://image-net.org/challenges/LSVRC/2015/results


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 3 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


classifier


RoI pooling


proposals


feature maps Region Proposal Network


conv layers


image


Figure 2: Faster R-CNN is a single, uniﬁed network for object detection. The RPN module serves as the ‘attention’ of this uniﬁed network.


fully-connected layer simultaneously predicts mul143 tiple class-agnostic boxes, generalizing the “single144 box” fashion of OverFeat. These class-agnostic boxes 145 are used as proposals for R-CNN [5]. The MultiBox 146 proposal network is applied on a single image crop or 147 multiple large image crops (e.g., 224×224), in contrast 148 to our fully convolutional scheme. MultiBox does not 149 share features between the proposal and detection 150 networks. We discuss OverFeat and MultiBox in more 151 depth later in context with our method. Concurrent 152 with our work, the DeepMask method [28] is devel153 oped for learning segmentation proposals. 154 Shared computation of convolutions [9], [1], [29], 155 [7], [2] has been attracting increasing attention for ef156 ﬁcient, yet accurate, visual recognition. The OverFeat 157 paper [9] computes convolutional features from an 158 image pyramid for classiﬁcation, localization, and de159 tection. Adaptively-sized pooling (SPP) [1] on shared 160 convolutional feature maps is developed for efﬁcient 161 region-based object detection [1], [30] and semantic 162 segmentation [29]. Fast R-CNN [2] enables end-to-end 163 detector training on shared convolutional features and 164 shows compelling accuracy and speed. 165


## 3 FASTER R-CNN 166


Our object detection system, called Faster R-CNN, is 167 composed of two modules. The ﬁrst module is a deep 168 fully convolutional network that proposes regions, 169 and the second module is the Fast R-CNN detector [2] 170 that uses the proposed regions. The entire system is a 171 single, uniﬁed network for object detection (Figure 2). 172 Using the recently popular terminology of neural 173 networks with ‘attention’ [31] mechanisms, the RPN 174 module tells the Fast R-CNN module where to look. 175 In Section 3.1 we introduce the designs and properties 176 of the network for region proposal. In Section 3.2 we 177


3


develop algorithms for training both modules with 178 features shared. 179


## 3.1 Region Proposal Networks 180


A Region Proposal Network (RPN) takes an image 181 (of any size) as input and outputs a set of rectangular 182 object proposals, each with an objectness score.3 We 183 model this process with a fully convolutional network 184 [7], which we describe in this section. Because our ulti185 mate goal is to share computation with a Fast R-CNN 186 object detection network [2], we assume that both nets 187 share a common set of convolutional layers. In our ex188 periments, we investigate the Zeiler and Fergus model 189 [32] (ZF), which has 5 shareable convolutional layers 190 and the Simonyan and Zisserman model [3] (VGG-16), 191 which has 13 shareable convolutional layers. 192 To generate region proposals, we slide a small 193 network over the convolutional feature map output 194 by the last shared convolutional layer. This small 195 network takes as input an n × n spatial window of 196 the input convolutional feature map. Each sliding 197 window is mapped to a lower-dimensional feature 198 (256-d for ZF and 512-d for VGG, with ReLU [33] 199 following). This feature is fed into two sibling fully200 connected layers—a box-regression layer (reg) and a 201 box-classiﬁcation layer (cls). We use n = 3 in this 202 paper, noting that the effective receptive ﬁeld on the 203 input image is large (171 and 228 pixels for ZF and 204 VGG, respectively). This mini-network is illustrated 205 at a single position in Figure 3 (left). Note that be206 cause the mini-network operates in a sliding-window 207 fashion, the fully-connected layers are shared across 208 all spatial locations. This architecture is naturally im209 plemented with an n×n convolutional layer followed 210 by two sibling 1 × 1 convolutional layers (for reg and 211 cls, respectively). 212


3.1.1 Anchors 213 At each sliding-window location, we simultaneously 214 predict multiple region proposals, where the number 215 of maximum possible proposals for each location is 216 denoted as k. So the reg layer has 4k outputs encoding 217 the coordinates of k boxes, and the cls layer outputs 218 2k scores that estimate probability of object or not 219 object for each proposal4. The k proposals are param220 eterized relative to k reference boxes, which we call 221 anchors. An anchor is centered at the sliding window 222 in question, and is associated with a scale and aspect 223 ratio (Figure 3, left). By default we use 3 scales and 224 3 aspect ratios, yielding k = 9 anchors at each sliding 225 position. For a convolutional feature map of a size 226


3. “Region” is a generic term and in this paper we only consider rectangular regions, as is common for many methods (e.g., [27], [4], [6]). “Objectness” measures membership to a set of object classes vs. background.


4. For simplicity we implement the cls layer as a two-class softmax layer. Alternatively, one may use logistic regression to produce k scores.


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 4 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


k anchor boxes


2k scores 4k coordinates


reg layer cls layer


256-d


intermediate layer


sliding window


conv feature map


4


person : 0.992


dog : 0.994


horse : 0.993


car : 1.000


cat : 0.982


person : 0.979


dog : 0.997


bus : 0.996


boat : 0.970


person : 0.983 person : 0.983


person : 0.736


person : 0.925


person : 0.989


Figure 3: Left: Region Proposal Network (RPN). Right: Example detections using RPN proposals on PASCAL VOC 2007 test. Our method detects objects in a wide range of scales and aspect ratios.


W × H (typically ∼2,400), there are WHk anchors in 227 total. 228


Translation-Invariant Anchors 229 An important property of our approach is that it 230 is translation invariant, both in terms of the anchors 231 and the functions that compute proposals relative to 232 the anchors. If one translates an object in an image, 233 the proposal should translate and the same function 234 should be able to predict the proposal in either lo235 cation. This translation-invariant property is guaran236 teed by our method5. As a comparison, the MultiBox 237 method [27] uses k-means to generate 800 anchors, 238 which are not translation invariant. So MultiBox does 239 not guarantee that the same proposal is generated if 240 an object is translated. 241 The translation-invariant property also reduces the 242 model size. MultiBox has a (4 + 1) × 800-dimensional 243 fully-connected output layer, whereas our method has 244 a (4 + 2) × 9-dimensional convolutional output layer 245 in the case of k = 9 anchors6. As a result, our output 246 layer has 2.8 × 104 parameters (512 × (4 + 2) × 9 247 for VGG-16), two orders of magnitude fewer than 248 MultiBox’s output layer that has 6.1 × 106 parameters 249 (1536 × (4 + 1) × 800 for GoogleNet [34] in MultiBox 250 [27]). If considering the feature projection layers, our 251 proposal layers still have an order of magnitude fewer 252 parameters than MultiBox7. We expect our method 253 to have less risk of overﬁtting on small datasets, like 254 PASCAL VOC. 255


Multi-Scale Anchors as Regression References 256 Our design of anchors presents a novel scheme 257 for addressing multiple scales (and aspect ratios). As 258 shown in Figure 1, there have been two popular ways 259 for multi-scale predictions. The ﬁrst way is based on 260


5. As is the case of FCNs [7], our network is translation invariant up to the network’s total stride.


6. 4 is the dimension of reg term for each category, and 1 or 2 is the dimension of cls term of sigmoid or softmax for each category


7. Considering the feature projection layers, our proposal layers’ parameter count is 3 × 3 × 512 × 512 + 512 × 6 × 9 = 2.4 × 106; MultiBox’s proposal layers’ parameter count is 7 × 7 × (64 + 96 + 64 + 64) × 1536 + 1536 × 5 × 800 = 27 × 106.


image/feature pyramids, e.g., in DPM [8] and CNN261 based methods [9], [1], [2]. The images are resized at 262 multiple scales, and feature maps (HOG [8] or deep 263 convolutional features [9], [1], [2]) are computed for 264 each scale (Figure 1(a)). This way is often useful but 265 is time-consuming. The second way is to use sliding 266 windows of multiple scales (and/or aspect ratios) on 267 the feature maps. For example, in DPM [8], models 268 of different aspect ratios are trained separately using 269 different ﬁlter sizes (such as 5×7 and 7×5). If this way 270 is used to address multiple scales, it can be thought 271 of as a “pyramid of ﬁlters” (Figure 1(b)). The second 272 way is usually adopted jointly with the ﬁrst way [8]. 273 As a comparison, our anchor-based method is built 274 on a pyramid of anchors, which is more cost-efﬁcient. 275 Our method classiﬁes and regresses bounding boxes 276 with reference to anchor boxes of multiple scales and 277 aspect ratios. It only relies on images and feature 278 maps of a single scale, and uses ﬁlters (sliding win279 dows on the feature map) of a single size. We show by 280 experiments the effects of this scheme for addressing 281 multiple scales and sizes (Table 8). 282 Because of this multi-scale design based on anchors, 283 we can simply use the convolutional features com284 puted on a single-scale image, as is also done by 285 the Fast R-CNN detector [2]. The design of multi286 scale anchors is a key component for sharing features 287 without extra cost for addressing scales. 288


3.1.2 Loss Function 289 For training RPNs, we assign a binary class label 290 (of being an object or not) to each anchor. We as291 sign a positive label to two kinds of anchors: (i) the 292 anchor/anchors with the highest Intersection-over293 Union (IoU) overlap with a ground-truth box, or (ii) an 294 anchor that has an IoU overlap higher than 0.7 with 295 any ground-truth box. Note that a single ground-truth 296 box may assign positive labels to multiple anchors. 297 Usually the second condition is sufﬁcient to determine 298 the positive samples; but we still adopt the ﬁrst 299 condition for the reason that in some rare cases the 300 second condition may ﬁnd no positive sample. We 301


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 5 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


assign a negative label to a non-positive anchor if its 302 IoU ratio is lower than 0.3 for all ground-truth boxes. 303 Anchors that are neither positive nor negative do not 304 contribute to the training objective. 305 With these deﬁnitions, we minimize an objective 306 function following the multi-task loss in Fast R-CNN 307 [2]. Our loss function for an image is deﬁned as: 308


L({pi}, {ti}) = 1 Ncls


X


Lcls(pi, p∗


i )


i


(1)


+λ 1 Nreg


X


p∗


i Lreg(ti, t∗


i ).


i


Here, i is the index of an anchor in a mini-batch and 309 pi is the predicted probability of anchor i being an 310 object. The ground-truth label p∗


i is 1 if the anchor 311 is positive, and is 0 if the anchor is negative. ti is a 312 vector representing the 4 parameterized coordinates 313 of the predicted bounding box, and t∗


i is that of the 314 ground-truth box associated with a positive anchor. 315 The classiﬁcation loss Lcls is log loss over two classes 316 (object vs. not object). For the regression loss, we use 317 Lreg(ti, t∗


i ) = R(ti −t∗


i ) where R is the robust loss 318 function (smooth L1) deﬁned in [2]. The term p∗


i Lreg 319 means the regression loss is activated only for positive 320 anchors (p∗


i = 1) and is disabled otherwise (p∗


i = 0). 321 The outputs of the cls and reg layers consist of {pi} 322 and {ti} respectively. 323 The two terms are normalized by Ncls and Nreg 324 and weighted by a balancing parameter λ. In our 325 current implementation (as in the released code), the 326 cls term in Eqn.(1) is normalized by the mini-batch 327 size (i.e., Ncls = 256) and the reg term is normalized 328 by the number of anchor locations (i.e., Nreg ∼2, 400). 329 By default we set λ = 10, and thus both cls and 330 reg terms are roughly equally weighted. We show 331 by experiments that the results are insensitive to the 332 values of λ in a wide range (Table 9). We also note 333 that the normalization as above is not required and 334 could be simpliﬁed. 335 For bounding box regression, we adopt the param336 eterizations of the 4 coordinates following [5]: 337


tx = (x −xa)/wa, ty = (y −ya)/ha, tw = log(w/wa), th = log(h/ha), t∗


(2)


x = (x∗−xa)/wa, t∗


y = (y∗−ya)/ha,


h = log(h∗/ha),


t∗


w = log(w∗/wa), t∗


where x, y, w, and h denote the box’s center coordi338 nates and its width and height. Variables x, xa, and 339 x∗are for the predicted box, anchor box, and ground340 truth box respectively (likewise for y, w, h). This can 341 be thought of as bounding-box regression from an 342 anchor box to a nearby ground-truth box. 343 Nevertheless, our method achieves bounding-box 344 regression by a different manner from previous RoI345 based (Region of Interest) methods [1], [2]. In [1], 346 [2], bounding-box regression is performed on features 347


5


pooled from arbitrarily sized RoIs, and the regression 348 weights are shared by all region sizes. In our formula349 tion, the features used for regression are of the same 350 spatial size (3 × 3) on the feature maps. To account 351 for varying sizes, a set of k bounding-box regressors 352 are learned. Each regressor is responsible for one scale 353 and one aspect ratio, and the k regressors do not share 354 weights. As such, it is still possible to predict boxes of 355 various sizes even though the features are of a ﬁxed 356 size/scale, thanks to the design of anchors. 357


3.1.3 Training RPNs 358 The RPN can be trained end-to-end by back359 propagation and stochastic gradient descent (SGD) 360 [35]. We follow the “image-centric” sampling strategy 361 from [2] to train this network. Each mini-batch arises 362 from a single image that contains many positive and 363 negative example anchors. It is possible to optimize 364 for the loss functions of all anchors, but this will 365 bias towards negative samples as they are dominate. 366 Instead, we randomly sample 256 anchors in an image 367 to compute the loss function of a mini-batch, where 368 the sampled positive and negative anchors have a 369 ratio of up to 1:1. If there are fewer than 128 positive 370 samples in an image, we pad the mini-batch with 371 negative ones. 372 We randomly initialize all new layers by drawing 373 weights from a zero-mean Gaussian distribution with 374 standard deviation 0.01. All other layers (i.e., the 375 shared convolutional layers) are initialized by pre376 training a model for ImageNet classiﬁcation [36], as 377 is standard practice [5]. We tune all layers of the 378 ZF net, and conv3 1 and up for the VGG net to 379 conserve memory [2]. We use a learning rate of 0.001 380 for 60k mini-batches, and 0.0001 for the next 20k 381 mini-batches on the PASCAL VOC dataset. We use a 382 momentum of 0.9 and a weight decay of 0.0005 [37]. 383 Our implementation uses Caffe [38]. 384


## 3.2 Sharing Features for RPN and Fast R-CNN 385


Thus far we have described how to train a network 386 for region proposal generation, without considering 387 the region-based object detection CNN that will utilize 388 these proposals. For the detection network, we adopt 389 Fast R-CNN [2]. Next we describe algorithms that 390 learn a uniﬁed network composed of RPN and Fast 391 R-CNN with shared convolutional layers (Figure 2). 392 Both RPN and Fast R-CNN, trained independently, 393 will modify their convolutional layers in different 394 ways. We therefore need to develop a technique that 395 allows for sharing convolutional layers between the 396 two networks, rather than learning two separate net397 works. We discuss three ways for training networks 398 with features shared: 399 (i) Alternating training. In this solution, we ﬁrst train 400 RPN, and use the proposals to train Fast R-CNN. 401 The network tuned by Fast R-CNN is then used to 402


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 6 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


6


Table 1: the learned average proposal size for each anchor using the ZF net (numbers for s = 600).


anchor 1282, 2:1 1282, 1:1 1282, 1:2 2562, 2:1 2562, 1:1 2562, 1:2 5122, 2:1 5122, 1:1 5122, 1:2 proposal 188×111 113×114 70×92 416×229 261×284 174×332 768×437 499×501 355×715


initialize RPN, and this process is iterated. This is the 403 solution that is used in all experiments in this paper. 404


(ii) Approximate joint training. In this solution, the 405 RPN and Fast R-CNN networks are merged into one 406 network during training as in Figure 2. In each SGD 407 iteration, the forward pass generates region propos408 als which are treated just like ﬁxed, pre-computed 409 proposals when training a Fast R-CNN detector. The 410 backward propagation takes place as usual, where for 411 the shared layers the backward propagated signals 412 from both the RPN loss and the Fast R-CNN loss 413 are combined. This solution is easy to implement. But 414 this solution ignores the derivative w.r.t. the proposal 415 boxes’ coordinates that are also network responses, so 416 is approximate. In our experiments, we have empiri417 cally found this solver produces close results (mAP 418 70.0% compared with 69.9% of alternating training 419 reported in Table 3), yet reduces the training time 420 by about 25-50% comparing with alternating training. 421 This solver is included in our released Python code. 422


(iii) Non-approximate joint training. As discussed 423 above, the bounding boxes predicted by RPN are 424 also functions of the input. The RoI pooling layer 425 [2] in Fast R-CNN accepts the convolutional features 426 and also the predicted bounding boxes as input, so 427 a theoretically valid backpropagation solver should 428 also involve gradients w.r.t. the box coordinates. These 429 gradients are ignored in the above approximate joint 430 training. In a non-approximate joint training solution, 431 we need an RoI pooling layer that is differentiable 432 w.r.t. the box coordinates. This is a nontrivial problem 433 and a solution can be given by an “RoI warping” layer 434 as developed in [15], which is beyond the scope of this 435 paper. 436


4-Step Alternating Training. In this paper, we adopt 437 a pragmatic 4-step training algorithm to learn shared 438 features via alternating optimization. In the ﬁrst step, 439 we train the RPN as described in Section 3.1.3. This 440 network is initialized with an ImageNet-pre-trained 441 model and ﬁne-tuned end-to-end for the region pro442 posal task. In the second step, we train a separate 443 detection network by Fast R-CNN using the proposals 444 generated by the step-1 RPN. This detection net445 work is also initialized by the ImageNet-pre-trained 446 model. At this point the two networks do not share 447 convolutional layers. In the third step, we use the 448 detector network to initialize RPN training, but we 449 ﬁx the shared convolutional layers and only ﬁne-tune 450 the layers unique to RPN. Now the two networks 451 share convolutional layers. Finally, keeping the shared 452 convolutional layers ﬁxed, we ﬁne-tune the unique 453 layers of Fast R-CNN. As such, both networks share 454 the same convolutional layers and form a uniﬁed 455


network. A similar alternating training can be run 456 for more iterations, but we have observed negligible 457 improvements. 458


## 3.3 Implementation Details 459


We train and test both region proposal and object 460 detection networks on images of a single scale [1], [2]. 461 We re-scale the images such that their shorter side 462 is s = 600 pixels [2]. Multi-scale feature extraction 463 (using an image pyramid) may improve accuracy but 464 does not exhibit a good speed-accuracy trade-off [2]. 465 On the re-scaled images, the total stride for both ZF 466 and VGG nets on the last convolutional layer is 16 467 pixels, and thus is ∼10 pixels on a typical PASCAL 468 image before resizing (∼500×375). Even such a large 469 stride provides good results, though accuracy may be 470 further improved with a smaller stride. 471 For anchors, we use 3 scales with box areas of 1282, 472 2562, and 5122 pixels, and 3 aspect ratios of 1:1, 1:2, 473 and 2:1. These hyper-parameters are not carefully cho474 sen for a particular dataset, and we provide ablation 475 experiments on their effects in the next section. As dis476 cussed, our solution does not need an image pyramid 477 or ﬁlter pyramid to predict regions of multiple scales, 478 saving considerable running time. Figure 3 (right) 479 shows the capability of our method for a wide range 480 of scales and aspect ratios. Table 1 shows the learned 481 average proposal size for each anchor using the ZF 482 net. We note that our algorithm allows predictions 483 that are larger than the underlying receptive ﬁeld. 484 Such predictions are not impossible—one may still 485 roughly infer the extent of an object if only the middle 486 of the object is visible. 487 The anchor boxes that cross image boundaries need 488 to be handled with care. During training, we ignore 489 all cross-boundary anchors so they do not contribute 490 to the loss. For a typical 1000 × 600 image, there 491 will be roughly 20000 (≈60 × 40 × 9) anchors in 492 total. With the cross-boundary anchors ignored, there 493 are about 6000 anchors per image for training. If the 494 boundary-crossing outliers are not ignored in training, 495 they introduce large, difﬁcult to correct error terms in 496 the objective, and training does not converge. During 497 testing, however, we still apply the fully convolutional 498 RPN to the entire image. This may generate cross499 boundary proposal boxes, which we clip to the image 500 boundary. 501 Some RPN proposals highly overlap with each 502 other. To reduce redundancy, we adopt non-maximum 503 suppression (NMS) on the proposal regions based on 504 their cls scores. We ﬁx the IoU threshold for NMS 505 at 0.7, which leaves us about 2000 proposal regions 506 per image. As we will show, NMS does not harm the 507 ultimate detection accuracy, but substantially reduces 508


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 7 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


7


Table 2: Detection results on PASCAL VOC 2007 test set (trained on VOC 2007 trainval). The detectors are Fast R-CNN with ZF, but using various proposal methods for training and testing.


train-time region proposals test-time region proposals method # boxes method # proposals mAP (%)


SS 2000 SS 2000 58.7 EB 2000 EB 2000 58.6 RPN+ZF, shared 2000 RPN+ZF, shared 300 59.9


ablation experiments follow below


RPN+ZF, unshared 2000 RPN+ZF, unshared 300 58.7 SS 2000 RPN+ZF 100 55.1 SS 2000 RPN+ZF 300 56.8 SS 2000 RPN+ZF 1000 56.3 SS 2000 RPN+ZF (no NMS) 6000 55.2 SS 2000 RPN+ZF (no cls) 100 44.6 SS 2000 RPN+ZF (no cls) 300 51.4 SS 2000 RPN+ZF (no cls) 1000 55.8 SS 2000 RPN+ZF (no reg) 300 52.1 SS 2000 RPN+ZF (no reg) 1000 51.3 SS 2000 RPN+VGG 300 59.2


the number of proposals. After NMS, we use the 509 top-N ranked proposal regions for detection. In the 510 following, we train Fast R-CNN using 2000 RPN pro511 posals, but evaluate different numbers of proposals at 512 test-time. 513


## 4 EXPERIMENTS 514


## 4.1 Experiments on PASCAL VOC 515


We comprehensively evaluate our method on the 516 PASCAL VOC 2007 detection benchmark [11]. This 517 dataset consists of about 5k trainval images and 5k 518 test images over 20 object categories. We also provide 519 results on the PASCAL VOC 2012 benchmark for a 520 few models. For the ImageNet pre-trained network, 521 we use the “fast” version of ZF net [32] that has 522 5 convolutional layers and 3 fully-connected layers, 523 and the public VGG-16 model8 [3] that has 13 con524 volutional layers and 3 fully-connected layers. We 525 primarily evaluate detection mean Average Precision 526 (mAP), because this is the actual metric for object 527 detection (rather than focusing on object proposal 528 proxy metrics). 529 Table 2 (top) shows Fast R-CNN results when 530 trained and tested using various region proposal 531 methods. These results use the ZF net. For Selective 532 Search (SS) [4], we generate about 2000 proposals by 533 the “fast” mode. For EdgeBoxes (EB) [6], we generate 534 the proposals by the default EB setting tuned for 0.7 535 IoU. SS has an mAP of 58.7% and EB has an mAP 536 of 58.6% under the Fast R-CNN framework. RPN 537 with Fast R-CNN achieves competitive results, with 538 an mAP of 59.9% while using up to 300 proposals9. 539 Using RPN yields a much faster detection system than 540


8. www.robots.ox.ac.uk/∼vgg/research/very deep/ 9. For RPN, the number of proposals (e.g., 300) is the maximum number for an image. RPN may produce fewer proposals after NMS, and thus the average number of proposals is smaller.


using either SS or EB because of shared convolutional 541 computations; the fewer proposals also reduce the 542 region-wise fully-connected layers’ cost (Table 5). 543


Ablation Experiments on RPN. To investigate the be544 havior of RPNs as a proposal method, we conducted 545 several ablation studies. First, we show the effect of 546 sharing convolutional layers between the RPN and 547 Fast R-CNN detection network. To do this, we stop 548 after the second step in the 4-step training process. 549 Using separate networks reduces the result slightly to 550 58.7% (RPN+ZF, unshared, Table 2). We observe that 551 this is because in the third step when the detector552 tuned features are used to ﬁne-tune the RPN, the 553 proposal quality is improved. 554 Next, we disentangle the RPN’s inﬂuence on train555 ing the Fast R-CNN detection network. For this pur556 pose, we train a Fast R-CNN model by using the 557 2000 SS proposals and ZF net. We ﬁx this detector 558 and evaluate the detection mAP by changing the 559 proposal regions used at test-time. In these ablation 560 experiments, the RPN does not share features with 561 the detector. 562 Replacing SS with 300 RPN proposals at test-time 563 leads to an mAP of 56.8%. The loss in mAP is because 564 of the inconsistency between the training/testing pro565 posals. This result serves as the baseline for the fol566 lowing comparisons. 567 Somewhat surprisingly, the RPN still leads to a 568 competitive result (55.1%) when using the top-ranked 569 100 proposals at test-time, indicating that the top570 ranked RPN proposals are accurate. On the other 571 extreme, using the top-ranked 6000 RPN proposals 572 (without NMS) has a comparable mAP (55.2%), sug573 gesting NMS does not harm the detection mAP and 574 may reduce false alarms. 575 Next, we separately investigate the roles of RPN’s 576 cls and reg outputs by turning off either of them 577 at test-time. When the cls layer is removed at test578


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 8 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


8


Table 3: Detection results on PASCAL VOC 2007 test set. The detector is Fast R-CNN and VGG-16. Training data: “07”: VOC 2007 trainval, “07+12”: union set of VOC 2007 trainval and VOC 2012 trainval. For RPN, the train-time proposals for Fast R-CNN are 2000. †: this number was reported in [2]; using the repository provided by this paper, this result is higher (68.1).


method # proposals data mAP (%)


## SS 2000 07 66.9†


SS 2000 07+12 70.0 RPN+VGG, unshared 300 07 68.5 RPN+VGG, shared 300 07 69.9 RPN+VGG, shared 300 07+12 73.2 RPN+VGG, shared 300 COCO+07+12 78.8


Table 4: Detection results on PASCAL VOC 2012 test set. The detector is Fast R-CNN and VGG-16. Training data: “07”: VOC 2007 trainval, “07++12”: union set of VOC 2007 trainval+test and VOC 2012 trainval. For RPN, the train-time proposals for Fast R-CNN are 2000. †: http://host.robots.ox.ac.uk:8080/anonymous/HZJTQA.html. ‡: http://host.robots.ox.ac.uk:8080/anonymous/YNPLXB.html. §: http://host.robots.ox.ac.uk:8080/anonymous/XEDH10.html.


method # proposals data mAP (%)


SS 2000 12 65.7 SS 2000 07++12 68.4 RPN+VGG, shared† 300 12 67.0 RPN+VGG, shared‡ 300 07++12 70.4 RPN+VGG, shared§ 300 COCO+07++12 75.9


Table 5: Timing (ms) on a K40 GPU, except SS proposal is evaluated in a CPU. “Region-wise” includes NMS, pooling, fully-connected, and softmax layers. See our released code for the proﬁling of running time.


model system conv proposal region-wise total rate


VGG SS + Fast R-CNN 146 1510 174 1830 0.5 fps VGG RPN + Fast R-CNN 141 10 47 198 5 fps ZF RPN + Fast R-CNN 31 3 25 59 17 fps


time (thus no NMS/ranking is used), we randomly 579 sample N proposals from the unscored regions. The 580 mAP is nearly unchanged with N = 1000 (55.8%), but 581 degrades considerably to 44.6% when N = 100. This 582 shows that the cls scores account for the accuracy of 583 the highest ranked proposals. 584 On the other hand, when the reg layer is removed 585 at test-time (so the proposals become anchor boxes), 586 the mAP drops to 52.1%. This suggests that the high587 quality proposals are mainly due to the regressed box 588 bounds. The anchor boxes, though having multiple 589 scales and aspect ratios, are not sufﬁcient for accurate 590 detection. 591 We also evaluate the effects of more powerful net592 works on the proposal quality of RPN alone. We use 593 VGG-16 to train the RPN, and still use the above 594 detector of SS+ZF. The mAP improves from 56.8% 595 (using RPN+ZF) to 59.2% (using RPN+VGG). This is a 596 promising result, because it suggests that the proposal 597 quality of RPN+VGG is better than that of RPN+ZF. 598 Because proposals of RPN+ZF are competitive with 599 SS (both are 58.7% when consistently used for training 600 and testing), we may expect RPN+VGG to be better 601 than SS. The following experiments justify this hy602 pothesis. 603


slightly higher than the SS baseline. As shown above, 607 this is because the proposals generated by RPN+VGG 608 are more accurate than SS. Unlike SS that is pre609 deﬁned, the RPN is actively trained and beneﬁts from 610 better networks. For the feature-shared variant, the 611 result is 69.9%—better than the strong SS baseline, yet 612 with nearly cost-free proposals. We further train the 613 RPN and detection network on the union set of PAS614 CAL VOC 2007 trainval and 2012 trainval. The mAP 615 is 73.2%. Figure 5 shows some results on the PASCAL 616 VOC 2007 test set. On the PASCAL VOC 2012 test set 617 (Table 4), our method has an mAP of 70.4% trained 618 on the union set of VOC 2007 trainval+test and VOC 619 2012 trainval. Table 6 and Table 7 show the detailed 620 numbers. 621 In Table 5 we summarize the running time of the 622 entire object detection system. SS takes 1-2 seconds 623 depending on content (on average about 1.5s), and 624 Fast R-CNN with VGG-16 takes 320ms on 2000 SS 625 proposals (or 223ms if using SVD on fully-connected 626 layers [2]). Our system with VGG-16 takes in total 627 198ms for both proposal and detection. With the con628 volutional features shared, the RPN alone only takes 629 10ms computing the additional layers. Our region630 wise computation is also lower, thanks to fewer pro631 posals (300 per image). Our system has a frame-rate 632 of 17 fps with the ZF net. 633


Performance of VGG-16. Table 3 shows the results 604 of VGG-16 for both proposal and detection. Using 605 RPN+VGG, the result is 68.5% for unshared features, 606


Sensitivities to Hyper-parameters. In Table 8 we 634


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 9 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


9


Table 6: Results on PASCAL VOC 2007 test set with Fast R-CNN detectors and VGG-16. For RPN, the train-time proposals for Fast R-CNN are 2000. RPN∗denotes the unsharing feature version.


method # box data mAP areo bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv


SS 2000 07 66.9 74.5 78.3 69.2 53.2 36.6 77.3 78.2 82.0 40.7 72.7 67.9 79.6 79.2 73.0 69.0 30.1 65.4 70.2 75.8 65.8


SS 2000 07+12 70.0 77.0 78.1 69.3 59.4 38.3 81.6 78.6 86.7 42.8 78.8 68.9 84.7 82.0 76.6 69.9 31.8 70.1 74.8 80.4 70.4


RPN∗ 300 07 68.5 74.1 77.2 67.7 53.9 51.0 75.1 79.2 78.9 50.7 78.0 61.1 79.1 81.9 72.2 75.9 37.2 71.4 62.5 77.4 66.4


RPN 300 07 69.9 70.0 80.6 70.1 57.3 49.9 78.2 80.4 82.0 52.2 75.3 67.2 80.3 79.8 75.0 76.3 39.1 68.3 67.3 81.1 67.6


RPN 300 07+12 73.2 76.5 79.0 70.9 65.5 52.1 83.1 84.7 86.4 52.0 81.9 65.7 84.8 84.6 77.5 76.7 38.8 73.6 73.9 83.0 72.6


RPN 300 COCO+07+12 78.8 84.3 82.0 77.7 68.9 65.7 88.1 88.4 88.9 63.6 86.3 70.8 85.9 87.6 80.1 82.3 53.6 80.4 75.8 86.6 78.9


Table 7: Results on PASCAL VOC 2012 test set with Fast R-CNN detectors and VGG-16. For RPN, the train-time proposals for Fast R-CNN are 2000.


method # box data mAP areo bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv


SS 2000 12 65.7 80.3 74.7 66.9 46.9 37.7 73.9 68.6 87.7 41.7 71.1 51.1 86.0 77.8 79.8 69.8 32.1 65.5 63.8 76.4 61.7


SS 2000 07++12 68.4 82.3 78.4 70.8 52.3 38.7 77.8 71.6 89.3 44.2 73.0 55.0 87.5 80.5 80.8 72.0 35.1 68.3 65.7 80.4 64.2


RPN 300 12 67.0 82.3 76.4 71.0 48.4 45.2 72.1 72.3 87.3 42.2 73.7 50.0 86.8 78.7 78.4 77.4 34.5 70.1 57.1 77.1 58.9


RPN 300 07++12 70.4 84.9 79.8 74.3 53.9 49.8 77.5 75.9 88.5 45.6 77.1 55.3 86.9 81.7 80.9 79.6 40.1 72.6 60.9 81.2 61.5


RPN 300 COCO+07++12 75.9 87.4 83.6 76.8 62.9 59.6 81.9 82.0 91.3 54.9 82.6 59.0 89.0 85.5 84.7 84.1 52.2 78.9 65.5 85.4 70.2


Figure 4: Recall vs. IoU overlap ratio on the PASCAL VOC 2007 test set.


Table 11: One-Stage Detection vs. Two-Stage Proposal + Detection. Detection results are on the PASCAL VOC 2007 test set using the ZF model and Fast R-CNN. RPN uses unshared features.


proposals detector mAP (%)


Two-Stage RPN + ZF, unshared 300 Fast R-CNN + ZF, 1 scale 58.7 One-Stage dense, 3 scales, 3 aspect ratios 20000 Fast R-CNN + ZF, 1 scale 53.8 One-Stage dense, 3 scales, 3 aspect ratios 20000 Fast R-CNN + ZF, 5 scales 53.9


Table 8: Detection results of Faster R-CNN on PASCAL VOC 2007 test set using different settings of anchors. The network is VGG-16. The training data is VOC 2007 trainval. The default setting of using 3 scales and 3 aspect ratios (69.9%) is the same as that in Table 3.


Table 9: Detection results of Faster R-CNN on PASCAL VOC 2007 test set using different values of λ in Equation (1). The network is VGG-16. The training data is VOC 2007 trainval. The default setting of using λ = 10 (69.9%) is the same as that in Table 3.


λ 0.1 1 10 100 mAP (%) 67.2 68.9 69.9 69.1


settings anchor scales aspect ratios mAP (%)


1 scale, 1 ratio 1282 1:1 65.8 2562 1:1 66.7


Table 10: Detection results of Faster R-CNN on PASCAL VOC 2007 test set using different numbers of proposals in testing. The network is VGG-16. The training data is VOC 2007 trainval. The default setting of using 300 proposals is the same as that in Table 3.


1 scale, 3 ratios 1282 {2:1, 1:1, 1:2} 68.8 2562 {2:1, 1:1, 1:2} 67.9 3 scales, 1 ratios {1282, 2562, 5122} 1:1 69.8 3 scales, 3 ratios {1282, 2562, 5122} {2:1, 1:1, 1:2} 69.9


# proposals 50 100 150 200 300 500 1000 mAP (%) 66.3 68.9 69.5 69.8 69.9 69.8 69.8


investigate the settings of anchors. By default we use 635 3 scales and 3 aspect ratios (69.9% mAP in Table 8). 636 If using just one anchor at each position, the mAP 637 drops by a considerable margin of 3-4%. The mAP 638 is higher if using 3 scales (with 1 aspect ratio) or 3 639 aspect ratios (with 1 scale), demonstrating that using 640 anchors of multiple sizes as the regression references 641 is an effective solution. Using just 3 scales with 1 642


aspect ratio (69.8%) is as good as using 3 scales with 643 3 aspect ratios on this dataset, suggesting that scales 644 and aspect ratios are not disentangled dimensions for 645 the detection accuracy. But we still adopt these two 646 dimensions in our designs to keep our system ﬂexible. 647 In Table 9 we compare different values of λ in Equa648 tion (1). By default we use λ = 10 which makes the 649


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 10 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


two terms in Equation (1) roughly equally weighted 650 after normalization. Table 9 shows that our result is 651 impacted just marginally (by ∼1%) when λ is within 652 a scale of about two orders of magnitude (1 to 100). 653 This demonstrates that the result is insensitive to λ in 654 a wide range. 655 In Table 10 we investigate the numbers of proposals 656 in testing. 657


Analysis of Recall-to-IoU. Next we compute the 658 recall of proposals at different IoU ratios with ground659 truth boxes. It is noteworthy that the Recall-to-IoU 660 metric is just loosely [19], [20], [21] related to the 661 ultimate detection accuracy. It is more appropriate to 662 use this metric to diagnose the proposal method than 663 to evaluate it. 664 In Figure 4, we show the results of using 300, 1000, 665 and 2000 proposals. We compare with SS, EB and 666 MCG, and the N proposals are the top-N ranked ones 667 based on the conﬁdence generated by these meth668 ods. The plots show that the RPN method behaves 669 gracefully when the number of proposals drops from 670 2000 to 300. This explains why the RPN has a good 671 ultimate detection mAP when using as few as 300 672 proposals. As we analyzed before, this property is 673 mainly attributed to the cls term of the RPN. The recall 674 of SS, EB and MCG drops more quickly than RPN 675 when the proposals are fewer. 676


One-Stage Detection vs. Two-Stage Proposal + De677 tection. The OverFeat paper [9] proposes a detection 678 method that uses regressors and classiﬁers on sliding 679 windows over convolutional feature maps. OverFeat 680 is a one-stage, class-speciﬁc detection pipeline, and ours 681 is a two-stage cascade consisting of class-agnostic pro682 posals and class-speciﬁc detections. In OverFeat, the 683 region-wise features come from a sliding window of 684 one aspect ratio over a scale pyramid. These features 685 are used to simultaneously determine the location and 686 category of objects. In RPN, the features are from 687 square (3×3) sliding windows and predict proposals 688 relative to anchors with different scales and aspect 689 ratios. Though both methods use sliding windows, the 690 region proposal task is only the ﬁrst stage of Faster R691 CNN—the downstream Fast R-CNN detector attends 692 to the proposals to reﬁne them. In the second stage of 693 our cascade, the region-wise features are adaptively 694 pooled [1], [2] from proposal boxes that more faith695 fully cover the features of the regions. We believe 696 these features lead to more accurate detections. 697 To compare the one-stage and two-stage systems, 698 we emulate the OverFeat system (and thus also circum699 vent other differences of implementation details) by 700 one-stage Fast R-CNN. In this system, the “proposals” 701 are dense sliding windows of 3 scales (128, 256, 512) 702 and 3 aspect ratios (1:1, 1:2, 2:1). Fast R-CNN is 703 trained to predict class-speciﬁc scores and regress box 704 locations from these sliding windows. Because the 705 OverFeat system adopts an image pyramid, we also 706


10


evaluate using convolutional features extracted from 707 5 scales. We use those 5 scales as in [1], [2]. 708 Table 11 compares the two-stage system and two 709 variants of the one-stage system. Using the ZF model, 710 the one-stage system has an mAP of 53.9%. This is 711 lower than the two-stage system (58.7%) by 4.8%. 712 This experiment justiﬁes the effectiveness of cascaded 713 region proposals and object detection. Similar obser714 vations are reported in [2], [39], where replacing SS 715 region proposals with sliding windows leads to ∼6% 716 degradation in both papers. We also note that the one717 stage system is slower as it has considerably more 718 proposals to process. 719


## 4.2 Experiments on MS COCO 720


We present more results on the Microsoft COCO 721 object detection dataset [12]. This dataset involves 80 722 object categories. We experiment with the 80k images 723 on the training set, 40k images on the validation set, 724 and 20k images on the test-dev set. We evaluate the 725 mAP averaged for IoU ∈[0.5 : 0.05 : 0.95] (COCO’s 726 standard metric, simply denoted as mAP@[.5, .95]) 727 and mAP@0.5 (PASCAL VOC’s metric). 728 There are a few minor changes of our system made 729 for this dataset. We train our models on an 8-GPU 730 implementation, and the effective mini-batch size be731 comes 8 for RPN (1 per GPU) and 16 for Fast R-CNN 732 (2 per GPU). The RPN step and Fast R-CNN step are 733 both trained for 240k iterations with a learning rate 734 of 0.003 and then for 80k iterations with 0.0003. We 735 modify the learning rates (starting with 0.003 instead 736 of 0.001) because the mini-batch size is changed. For 737 the anchors, we use 3 aspect ratios and 4 scales 738 (adding 642), mainly motivated by handling small 739 objects on this dataset. In addition, in our Fast R-CNN 740 step, the negative samples are deﬁned as those with 741 a maximum IoU with ground truth in the interval of 742 [0, 0.5), instead of [0.1, 0.5) used in [1], [2]. We note 743 that in the SPPnet system [1], the negative samples 744 in [0.1, 0.5) are used for network ﬁne-tuning, but the 745 negative samples in [0, 0.5) are still visited in the SVM 746 step with hard-negative mining. But the Fast R-CNN 747 system [2] abandons the SVM step, so the negative 748 samples in [0, 0.1) are never visited. Including these 749 [0, 0.1) samples improves mAP@0.5 on the COCO 750 dataset for both Fast R-CNN and Faster R-CNN sys751 tems (but the impact is negligible on PASCAL VOC). 752 The rest of the implementation details are the same 753 as on PASCAL VOC. In particular, we keep using 754 300 proposals and single-scale (s = 600) testing. The 755 testing time is still about 200ms per image on the 756 COCO dataset. 757 In Table 12 we ﬁrst report the results of the Fast 758 R-CNN system [2] using the implementation in this 759 paper. Our Fast R-CNN baseline has 39.3% mAP@0.5 760 on the test-dev set, higher than that reported in [2]. 761 We conjecture that the reason for this gap is mainly 762


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 11 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


11


Table 12: Object detection results (%) on the MS COCO dataset. The model is VGG-16.


COCO val COCO test-dev method proposals training data mAP@.5 mAP@[.5, .95] mAP@.5 mAP@[.5, .95]


Fast R-CNN [2] SS, 2000 COCO train - - 35.9 19.7 Fast R-CNN [impl. in this paper] SS, 2000 COCO train 38.6 18.9 39.3 19.3 Faster R-CNN RPN, 300 COCO train 41.5 21.2 42.1 21.5 Faster R-CNN RPN, 300 COCO trainval - - 42.7 21.9


due to the deﬁnition of the negative samples and also 763 the changes of the mini-batch sizes. We also note that 764 the mAP@[.5, .95] is just comparable. 765 Next we evaluate our Faster R-CNN system. Using 766 the COCO training set to train, Faster R-CNN has 767 42.1% mAP@0.5 and 21.5% mAP@[.5, .95] on the 768 COCO test-dev set. This is 2.8% higher for mAP@0.5 769 and 2.2% higher for mAP@[.5, .95] than the Fast R770 CNN counterpart under the same protocol (Table 12). 771 This indicates that RPN performs excellent for im772 proving the localization accuracy at higher IoU thresh773 olds. Using the COCO trainval set to train, Faster R774 CNN has 42.7% mAP@0.5 and 21.9% mAP@[.5, .95] on 775 the COCO test-dev set. Figure 6 shows some results 776 on the MS COCO test-dev set. 777


Faster R-CNN in ILSVRC & COCO 2015 compe778 titions We have demonstrated that Faster R-CNN 779 beneﬁts more from better features, thanks to the fact 780 that the RPN completely learns to propose regions by 781 neural networks. This observation is still valid even 782 when one increases the depth substantially to over 783 100 layers [18]. Only by replacing VGG-16 with a 101784 layer residual net (ResNet-101) [18], the Faster R-CNN 785 system increases the mAP from 41.5%/21.2% (VGG786 16) to 48.4%/27.2% (ResNet-101) on the COCO val 787 set. With other improvements orthogonal to Faster R788 CNN, He et al. [18] obtained a single-model result of 789 55.7%/34.9% and an ensemble result of 59.0%/37.4% 790 on the COCO test-dev set, which won the 1st place 791 in the COCO 2015 object detection competition. The 792 same system [18] also won the 1st place in the ILSVRC 793 2015 object detection competition, surpassing the sec794 ond place by absolute 8.5%. RPN is also a building 795 block of the 1st-place winning entries in ILSVRC 2015 796 localization and COCO 2015 segmentation competi797 tions, for which the details are available in [18] and 798 [15] respectively. 799


## 4.3 From MS COCO to PASCAL VOC 800


Large-scale data is of crucial importance for improv801 ing deep neural networks. Next, we investigate how 802 the MS COCO dataset can help with the detection 803 performance on PASCAL VOC. 804 As a simple baseline, we directly evaluate the 805 COCO detection model on the PASCAL VOC dataset, 806 without ﬁne-tuning on any PASCAL VOC data. This 807 evaluation is possible because the categories on 808 COCO are a superset of those on PASCAL VOC. The 809 categories that are exclusive on COCO are ignored in 810


Table 13: Detection mAP (%) of Faster R-CNN on PASCAL VOC 2007 test set and 2012 test set using different training data. The model is VGG-16. “COCO” denotes that the COCO trainval set is used for training. See also Table 6 and Table 7.


training data 2007 test 2012 test


VOC07 69.9 67.0 VOC07+12 73.2 - VOC07++12 - 70.4 COCO (no VOC) 76.1 73.0 COCO+VOC07+12 78.8 - COCO+VOC07++12 - 75.9


## VOC07+12


## COCO+VOC07+12


Cor: 77.1%


Cor: 83.3%


Loc: 8.1%


Loc: 7.1%


Sim: 2.0%


Sim: 1.7%


Oth: 1.3%


Oth: 1.3%


## BG: 11.6%


## BG: 6.7%


Loc: 8.1%


Loc: 7.1%


Cor: 77.1%


Cor: 83.3%


Figure 7: Error analyses on models trained with and without MS COCO data. The test set is PASCAL VOC 2007 test. Distribution of top-ranked Cor (correct), Loc (false due to poor localization), Sim (confusion with a similar category), Oth (confusion with a dissimlar category), BG (ﬁred on background) is shown, which is generated by the published diagnosis code of [40].


this experiment, and the softmax layer is performed 811 only on the 20 categories plus background. The mAP 812 under this setting is 76.1% on the PASCAL VOC 2007 813 test set (Table 13). This result is better than that trained 814 on VOC07+12 (73.2%) by a good margin, even though 815 the PASCAL VOC data are not exploited. 816 Then we ﬁne-tune the COCO detection model on 817 the VOC dataset. In this experiment, the COCO model 818 is in place of the ImageNet-pre-trained model (that 819 is used to initialize the network weights), and the 820 Faster R-CNN system is ﬁne-tuned as described in 821 Section 3.2. Doing so leads to 78.8% mAP on the 822 PASCAL VOC 2007 test set. The extra data from 823 the COCO set increases the mAP by 5.6%. Table 6 824 shows that the model trained on COCO+VOC has 825 the best AP for every individual category on PASCAL 826 VOC 2007. This improvement is mainly resulted from 827 fewer false alarms on background (Figure 7). Similar 828 improvements are observed on the PASCAL VOC 829 2012 test set (Table 13 and Table 7). We note that 830


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 12 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


person : 0.918


bird : 0.902


person : 0.988


person : 0.797 bird : 0.978


car : 0.955 55 55 car : 0.745 .745 horse : 0.991


bird : 0.972


bird : 0.941


person : 0.988 pers p person : 0.976 person : 0.964


car : 0.999


person : 0.929 person : 0.994 person : 0.991


person : 0.961


person person person : 0.958


bus : 0.999


person : 0.960


person : 0.985


person : 0.996 per per per person : 0.995 person : 0.994


person : 0.757


dog : 0.697


cat : 0.998


person : 0.917


car : 1.000


person : 0.930


boat : 0.992


person : 0.962


pottedplant : 0.951


bottle : 0.962 0 962 bottle : 0.851


boat : 0.693


diningtable : 0.791


boat : 0.846


pottedplant : 0.728


car : 0.982 car car car : 0.981 car : 0.880


car : 1.000


chair : 0.630


diningtable : 0.862


bottle : 0.826


aeroplane : 0.992


aeroplane : 0.986 sheep : 0.970


aeroplane : 0.998


pottedplant : 0.820


pottedplant : 0.993


car : 0.907 907 907 person : 0.993 person : 0.987


pottedplant : 0.715


pottedplant : 0.940


pottedplant : 0.869


tvmonitor : 0.945


aeroplane : 0.978


tvmonitor : 0.993


chair : 0.723


e : 0.789 person : 0.968


bottle : 0.789


person : 0.988


diningtable : 0.903


12


cow : 0.995


person : 0.992


cow : 0.998


bottle : 0.726


person : 0.993 person person person person person : 0.986 0 993 : n86 n : n : nperson : 0.959


car : 0.997 car : 0.980


dog : 0.981


cow : 0.979


person : 0.998


cow : 0.974


cow : 0.979


cow : 0.892


cow : 0.985


boat : 0.749 boat : 0.671


boat : 0.895


boat : 0.877


person : 0.988


person : 0.995


bicycle : 0.987


person : 0.994 e : 0.987 e : 0 987 bicyc bicyc bicyc b 4person : 0.981


person : 0.940 940 940 person : 0.893


bicycle : 0.977 7 bicycle : 0.972


dog : 0.987


person : 0.948


person : 0.972


person : 0.919


boat : 0.995


boat : 0.948


boat : 0.808 : 0 808 :boat : 0.692


person : 0.975


bird : 0.998


bird : 0.980


person : 0.670


bird : 0.806


horse : 0.984


chair : 0.984


984 984 diningtable : 0.997


chair : 0.978


chair : 0.976 chair : 0.962


person : 0.983


bird : 0.997


tvmonitor : 0.993


chair : 0.982


person : 0.959


bottle : 0.858


b bottle : 0 bot bottle : 0.616


chair : 0.852


bottle : 0.903


: 0 903 person : 0.897 person : 0.870


bottle : 0.884


bird : 0.727


Figure 5: Selected examples of object detection results on the PASCAL VOC 2007 test set using the Faster R-CNN system. The model is VGG-16 and the training data is 07+12 trainval (73.2% mAP on the 2007 test set). Our method detects objects of a wide range of scales and aspect ratios. Each output box is associated with a category label and a softmax score in [0, 1]. A score threshold of 0.6 is used to display these images. The running time for obtaining these results is 198ms per image, including all steps.


the test-time speed of obtaining these state-of-the-art 831 results is still about 200ms per image. 832


## 5 CONCLUSION 833


We have presented RPNs for efﬁcient and accurate 834 region proposal generation. By sharing convolutional 835 features with the down-stream detection network, the 836 region proposal step is nearly cost-free. Our method 837 enables a uniﬁed, deep-learning-based object detec838 tion system to run at 5-17 fps. The learned RPN also 839


improves region proposal quality and thus the overall 840 object detection accuracy. 841


## REFERENCES 842


[1] K. He, X. Zhang, S. Ren, and J. Sun, “Spatial pyramid pooling 843 in deep convolutional networks for visual recognition,” in 844 European Conference on Computer Vision (ECCV), 2014. 845 [2] R. Girshick, “Fast R-CNN,” in IEEE International Conference on 846 Computer Vision (ICCV), 2015. 847 [3] K. Simonyan and A. Zisserman, “Very deep convolutional 848 networks for large-scale image recognition,” in International 849 Conference on Learning Representations (ICLR), 2015. 850


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 13 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


person : 0.975 rson : 0.975 rson son : 0 on person : 0.958


pe pe person : 0.928 958 958 0 975 n : 0. n : 0. 0.975 0.975 0. person : 0.823


person : 0.941


.941 4 person : 0.673


airplane : 0.997


person : 0.759


p backpack : 0.756


person : 0.766


0.976 0 976 person : 0.939


0 939


person : 0.976


person : 0.867


person : 0.950


on : 0.950 0 50 person : 0.805


handbag : 0.848


dog : 0.996


dog : 0.691


person : 0.996


13


traffic light : 0.802


person : 0.897 person : 0.842 person : 0.841 person : 0.84 person : 0.772


car : 0.957


umbrella : 0.824


clock : 0.986


person : 0.970 person : 0.950 person : 0.931 p person : 0.916


clock : 0.981


motorcycle : 0.713


bicycle : 0.891 bicycle : 0.639


person : 0.800


motorcycle : 0.827


person : 0.808


pizza : 0.985


pizza : 0.938 dining table : 0.956 person : 0.998


clock : 0.982


skis : 0.919


bowl : 0.759


giraffe : 0.993 giraffe : 0.989


giraffe : 0.988


broccoli : 0.953


teddy bear : 0.999


bus : 0.999


teddy bear : 0.802 teddy bear : 0.738


teddy bear : 0.890


person : 0.970 : 0.970 erson person : 0.869


book : 0.611


tv : 0.964


bottle : 0.768


laptop : 0.986


couch : 0.627


couch : 0.991


mouse : 0.871


m keyboard : 0.956


tv : 0.959


couch : 0.719


dining table : 0.637


mouse : 0.677


chair : 0.631


chair : 0.644


cup : 0.720


frisbee : 0.998


dog : 0.966


zebra : 0.996


zebra : 0.970 970 zebra : 0.848


zebra : 0.993


person : 0.917 person : 0.792 : 0.792 0 792 tv : 0.711


refrigerator : 0.699


person : 0.993


bottle : 0.982


laptop : 0.973


oven : 0.655


keyboard : 0.638


keyboard : 0.615


mouse : 0.981


cup : 0.990


dining table : 0.888 person : 0.984 person person car : 0.816


pizza : 0.919


refrigerator : 0.631


bowl : 0.816 bowl : 0.744


bowl : 0.710


bowl : 0.847


cup : 0.807


pizza : 0.965


chair : 0.772


oven : 0.969


dining table : 0.618


bed : 0.999


pizza : 0.995


pizza : 0.982


bottle : 0.627


person : 0.999


boat : 0.992


person : 0.934


surfboard : 0.979


umbrella : 0.885


p person : 0.691


person : 0.716


person : 0.940 person : 0.927


0.940 person : 0.854


927 927 person : 0.665


person : 0.618


person : 0.692


person : 0.825person : 0.813


person : 0.864


potted plant : 0.769


sink : 0.976sink : 0.938


bowl : 0.602


sink : 0.994 sink : 0.992


toilet : 0.921 sink : 0.969


traffic light : 0.869 traffic light : 0.713


train : 0.965


boat : 0.758 boat : 0.746 boat : 0.613


bench : 0.971


person : 0.986


person : 0.723


cup : 0.986 cup : 0.931


dining table : 0.941


bird : 0.968


bowl : 0.958


sandwich : 0.629


bird : 0.987


bird : 0.894


person : 0.999 person : 0.999 person : 0.999 perso perso tennis racket : 0.960


bird : 0.746 horse : 0.990


bird : 0.956


bird : 0.906


toothbrush : 0.668


kite : 0.934


clock : 0.988


person : 0.998


Figure 6: Selected examples of object detection results on the MS COCO test-dev set using the Faster R-CNN system. The model is VGG-16 and the training data is COCO trainval (42.7% mAP@0.5 on the test-dev set). Each output box is associated with a category label and a softmax score in [0, 1]. A score threshold of 0.6 is used to display these images. For each image, one color represents one object category in that image.


[4] J. R. Uijlings, K. E. van de Sande, T. Gevers, and A. W. Smeul851 ders, “Selective search for object recognition,” International 852 Journal of Computer Vision (IJCV), 2013. 853 [5] R. Girshick, J. Donahue, T. Darrell, and J. Malik, “Rich feature 854 hierarchies for accurate object detection and semantic seg855 mentation,” in IEEE Conference on Computer Vision and Pattern 856 Recognition (CVPR), 2014. 857 [6] C. L. Zitnick and P. Doll´ar, “Edge boxes: Locating object 858 proposals from edges,” in European Conference on Computer 859 Vision (ECCV), 2014. 860 [7] J. Long, E. Shelhamer, and T. Darrell, “Fully convolutional 861 networks for semantic segmentation,” in IEEE Conference on 862 Computer Vision and Pattern Recognition (CVPR), 2015. 863 [8] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and D. Ra864 manan, “Object detection with discriminatively trained part865


based models,” IEEE Transactions on Pattern Analysis and Ma866 chine Intelligence (TPAMI), 2010. 867 [9] P. Sermanet, D. Eigen, X. Zhang, M. Mathieu, R. Fergus, 868 and Y. LeCun, “Overfeat: Integrated recognition, localization 869 and detection using convolutional networks,” in International 870 Conference on Learning Representations (ICLR), 2014. 871 [10] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN: Towards 872 real-time object detection with region proposal networks,” in 873 Neural Information Processing Systems (NIPS), 2015. 874 [11] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and 875 A. Zisserman, “The PASCAL Visual Object Classes Challenge 876 2007 (VOC2007) Results,” 2007. 877 [12] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ra878 manan, P. Doll´ar, and C. L. Zitnick, “Microsoft COCO: Com879 mon Objects in Context,” in European Conference on Computer 880


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


<!-- Page 14 -->


This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI


10.1109/TPAMI.2016.2577031, IEEE Transactions on Pattern Analysis and Machine Intelligence


Vision (ECCV), 2014. 881 [13] S. Song and J. Xiao, “Deep sliding shapes for amodal 3d object 882 detection in rgb-d images,” arXiv:1511.02300, 2015. 883 [14] J. Zhu, X. Chen, and A. L. Yuille, “DeePM: A deep part-based 884 model for object detection and semantic part localization,” 885 arXiv:1511.07131, 2015. 886 [15] J. Dai, K. He, and J. Sun, “Instance-aware semantic segmenta887 tion via multi-task network cascades,” arXiv:1512.04412, 2015. 888 [16] J. Johnson, A. Karpathy, and L. Fei-Fei, “Densecap: Fully 889 convolutional localization networks for dense captioning,” 890 arXiv:1511.07571, 2015. 891 [17] D. Kislyuk, Y. Liu, D. Liu, E. Tzeng, and Y. Jing, “Human cu892 ration and convnets: Powering item-to-item recommendations 893 on pinterest,” arXiv:1511.04003, 2015. 894 [18] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning 895 for image recognition,” arXiv:1512.03385, 2015. 896 [19] J. Hosang, R. Benenson, and B. Schiele, “How good are de897 tection proposals, really?” in British Machine Vision Conference 898 (BMVC), 2014. 899 [20] J. Hosang, R. Benenson, P. Doll´ar, and B. Schiele, “What makes 900 for effective detection proposals?” IEEE Transactions on Pattern 901 Analysis and Machine Intelligence (TPAMI), 2015. 902 [21] N. Chavali, H. Agrawal, A. Mahendru, and D. Batra, 903 “Object-Proposal Evaluation Protocol is ’Gameable’,” arXiv: 904 1505.05836, 2015. 905 [22] J. Carreira and C. Sminchisescu, “CPMC: Automatic ob906 ject segmentation using constrained parametric min-cuts,” 907 IEEE Transactions on Pattern Analysis and Machine Intelligence 908 (TPAMI), 2012. 909 [23] P. Arbel´aez, J. Pont-Tuset, J. T. Barron, F. Marques, and J. Malik, 910 “Multiscale combinatorial grouping,” in IEEE Conference on 911 Computer Vision and Pattern Recognition (CVPR), 2014. 912 [24] B. Alexe, T. Deselaers, and V. Ferrari, “Measuring the object913 ness of image windows,” IEEE Transactions on Pattern Analysis 914 and Machine Intelligence (TPAMI), 2012. 915 [25] C. Szegedy, A. Toshev, and D. Erhan, “Deep neural networks 916 for object detection,” in Neural Information Processing Systems 917 (NIPS), 2013. 918 [26] D. Erhan, C. Szegedy, A. Toshev, and D. Anguelov, “Scalable 919 object detection using deep neural networks,” in IEEE Confer920 ence on Computer Vision and Pattern Recognition (CVPR), 2014. 921 [27] C. Szegedy, S. Reed, D. Erhan, and D. Anguelov, “Scalable, 922 high-quality object detection,” arXiv:1412.1441 (v1), 2015. 923 [28] P. O. Pinheiro, R. Collobert, and P. Dollar, “Learning to 924 segment object candidates,” in Neural Information Processing 925 Systems (NIPS), 2015. 926 [29] J. Dai, K. He, and J. Sun, “Convolutional feature masking 927 for joint object and stuff segmentation,” in IEEE Conference on 928 Computer Vision and Pattern Recognition (CVPR), 2015. 929 [30] S. Ren, K. He, R. Girshick, X. Zhang, and J. Sun, “Ob930 ject detection networks on convolutional feature maps,” 931 arXiv:1504.06066, 2015. 932 [31] J. K. Chorowski, D. Bahdanau, D. Serdyuk, K. Cho, and 933 Y. Bengio, “Attention-based models for speech recognition,” 934 in Neural Information Processing Systems (NIPS), 2015. 935 [32] M. D. Zeiler and R. Fergus, “Visualizing and understanding 936 convolutional neural networks,” in European Conference on 937 Computer Vision (ECCV), 2014. 938 [33] V. Nair and G. E. Hinton, “Rectiﬁed linear units improve 939 restricted boltzmann machines,” in International Conference on 940 Machine Learning (ICML), 2010. 941 [34] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, 942 D. Erhan, and A. Rabinovich, “Going deeper with convo943 lutions,” in IEEE Conference on Computer Vision and Pattern 944 Recognition (CVPR), 2015. 945 [35] Y. LeCun, B. Boser, J. S. Denker, D. Henderson, R. E. Howard, 946 W. Hubbard, and L. D. Jackel, “Backpropagation applied to 947 handwritten zip code recognition,” Neural computation, 1989. 948 [36] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh, S. Ma, 949 Z. Huang, A. Karpathy, A. Khosla, M. Bernstein, A. C. Berg, 950 and L. Fei-Fei, “ImageNet Large Scale Visual Recognition 951 Challenge,” in International Journal of Computer Vision (IJCV), 952 2015. 953 [37] A. Krizhevsky, I. Sutskever, and G. Hinton, “Imagenet classi954 ﬁcation with deep convolutional neural networks,” in Neural 955 Information Processing Systems (NIPS), 2012. 956


14


[38] Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Gir957 shick, S. Guadarrama, and T. Darrell, “Caffe: Convolutional 958 architecture for fast feature embedding,” arXiv:1408.5093, 2014. 959 [39] K. Lenc and A. Vedaldi, “R-CNN minus R,” in British Machine 960 Vision Conference (BMVC), 2015. 961 [40] D. Hoiem, Y. Chodpathumwan, and Q. Dai, “Diagnosing error 962 in object detectors,” in European Conference on Computer Vision 963 (ECCV), 2012. 964


Shaoqing Ren received the BS degree from 965 the University of Science and Technology of 966 China in 2011. He is currently a PhD student 967 in a joint PhD program between University 968 of Science and Technology of China and 969 Microsoft Research Asia. His research in970 terests are in computer vision, especially in 971 detection and localization of general objects 972 and faces. 973


974


Kaiming He is a lead researcher at Microsoft 975 Research Asia. He received the BS degree 976 from Tsinghua University in 2007, and the 977 PhD degree from the Chinese University of 978 Hong Kong in 2011. He joined Microsoft Re979 search Asia in 2011. His current research 980 interests are deep learning for visual recog981 nition, including image classiﬁcation, object 982 detection, and semantic segmentation. He 983 has won the Best Paper Award at CVPR 984 2009. 985


Ross Girshick is a Research Scientist at 986 Facebook AI Research. He holds a PhD and 987 MS in computer science, both from the Uni988 versity of Chicago where he studied under 989 the supervision of Pedro Felzenszwalb. Prior 990 to joining Facebook AI Research, Ross was 991 a Researcher at Microsoft Research, and 992 a Postdoctorial Fellow at the University of 993 California, Berkeley where he collaborated 994 with Jitendra Malik and Trevor Darrell. During 995 the course of PASCAL VOC object detection 996 challenge, Ross participated in multiple winning object detection 997 entries and was awarded a “lifetime achievement” prize for his work 998 on the widely used Deformable Part Models. 999


Jian Sun is a principal researcher at Mi1000 crosoft Research Asia. He got the BS de1001 gree, MS degree and PhD degree from Xian 1002 Jiaotong University in 1997, 2000 and 2003. 1003 He joined Microsoft Research Asia in July, 1004 2003. His current major research interests 1005 are computer vision, computational photog1006 raphy, and deep learning. He has won the 1007 Best Paper Award at CVPR 2009. 1008


1009


0162-8828 (c) 2016 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
