# zeng2022-small-object


<!-- Page 1 -->


## IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022 3507014


A Small-Sized Object Detection Oriented Multi-Scale Feature Fusion Approach With


Application to Defect Detection


Nianyin Zeng , Peishu Wu , Zidong Wang , Fellow, IEEE, Han Li , Weibo Liu , and Xiaohui Liu


Abstract—Object detection is a well-known task in the ﬁeld of computer vision, especially the small target detection problem that has aroused great academic attention. In order to improve the detection performance of small objects, in this article, a novel enhanced multiscale feature fusion method is proposed, namely, the atrous spatial pyramid pooling-balanced-feature pyramid network (ABFPN). In particular, the atrous convolution operators with different dilation rates are employed to make full use of context information, where the skip connection is applied to achieve sufﬁcient feature fusions. In addition, there is a balanced module to integrate and enhance features at different levels. The performance of the proposed ABFPN is evaluated on three public benchmark datasets, and experimental results demonstrate that it is a reliable and efﬁcient feature fusion method. Furthermore, in order to validate the applicational potential in small objects, the developed ABFPN is utilized to detect surface tiny defects of the printed circuit board (PCB), which acts as the neck part of an improved PCB defect detection (IPDD) framework. While designing the IPDD, several powerful strategies are also employed to further improve the overall performance, which is evaluated via extensive ablation studies. Experiments on a public PCB defect detection database have demonstrated the superiority of the designed IPDD framework against the other seven state-ofthe-art methods, which further validates the practicality of the proposed ABFPN.


Index Terms—Atrous spatial pyramid pooling (ASPP), defect detection, feature fusion, object detection, printed circuit board (PCB).


## I. INTRODUCTION C


OMPUTER vision is a simulation of biological vision using computers and related equipment. Recently, computer vision has attracted enormous attention in various ﬁelds, such as industrial production, agriculture, and medical health. It is known that computer vision tasks can be divided into


Manuscript received January 14, 2022; revised February 5, 2022; accepted February 13, 2022. Date of publication February 24, 2022; date of current version March 10, 2022. This work was supported in part by the National Natural Science Foundation of China under Grant 62073271, in part by the International Science and Technology Cooperation Project of Fujian Province of China under Grant 2019I0003, and in part by the Independent Innovation Foundation of AECC under Grant ZZCX-2018-017. The Associate Editor coordinating the review process was Dr. Damodar Reddy Edla. (Corresponding author: Nianyin Zeng.)


Nianyin Zeng, Peishu Wu, and Han Li are with the Department of Instrumental and Electrical Engineering, Xiamen University, Xiamen, Fujian 361005, China (e-mail: zny@xmu.edu.cn). Zidong Wang, Weibo Liu, and Xiaohui Liu are with the Department of Computer Science, Brunel University London, Uxbridge UB8 3PH, U.K. (e-mail: zidong.wang@brunel.ac.uk).


Digital Object Identiﬁer 10.1109/TIM.2022.3153997


four categories that are image classiﬁcation, object detection, semantic segmentation, and instance segmentation [7]. Due to its wide application potential in image processing and pattern recognition, object detection has received an ever-increasing research interest from both academic and industrial communities during the past few decades. With the rapid development of deep learning techniques, object detection algorithms can be divided into two groups: the one-stage object detection algorithms and the two-stage ones. The one-stage object detection algorithms can directly obtain the category probability and position coordinate values of objects, e.g., you only look once (YOLO) models, the single-shot multibox detector (SSD), and the corner network [1], [27], [37], [40]–[42]. The two-stage ones need to obtain the region proposals with rough location information and then classify the candidate regions into different groups. Some representative two-stage object detection algorithms are the region convolutional neural network (RCNN) [13], the fast RCNN [14], the faster RCNN [43], the mask RCNN [15], and the spatial pyramid pooling network [16].


Due to their strong abilities in defect detection and fault diagnosis, object detection algorithms have been successfully applied to a wide range of areas such as transportation, electrical and electronic engineering, biomedical engineering, and so on [2], [12], [22], [23], [51], [58]. It should be pointed out that the size of the object plays a critical role in object detection, especially in industrial applications. In fact, the performance of the conventional object detection algorithms is poor by using low-level features (e.g., edge information) for small object detection. In addition, it is difﬁcult to extract high-level semantic features of small objects. As such, it is challenging to accurately position and classify small objects by using conventional object detection algorithms.


During the past few years, tremendous efforts have been devoted to small object detection [20], [30], [32], [33], [35], [36]. To summarize, the recently developed small object detection methods can be divided into three types: 1) using context information; 2) applying feature fusion; and 3) generating enhanced features. For example, a fully end-to-end object detector has been proposed in [20], where an object relation module has been designed to integrate the context information of the features. In [33], a feature pyramid network (FPN) has been proposed to merge the feature maps at different stages. Recently, a path aggregation network has been introduced


1557-9662 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 2 -->


## 3507014 IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022


in [36] by designing a bottom-up path enhancement branch, which could integrate the information from high-level features and low-level ones in a sufﬁcient manner. To deal with the inconsistency among different feature scales, an adaptive spatial feature fusion method has been proposed in [35] by learning the weighting parameters. Very recently, a trident network has been presented in [32] for detecting objects in distinct sizes, where the atrous convolution method with multiple dilation rates has been employed to generate different receptive ﬁelds in parallel.


Unfortunately, the aforementioned small object detection methods still have some limitations, which do not fully mine latent information, such as more accurate location information and stronger semantic features from the feature maps. For instance, most context information-based object detection methods only concatenate high- and low-level features in a simple manner; however, such fusion stage with rough stacking may cause the increase of redundant information, such as noise information, which may decrease the detection performance. In this case, existing small object detection methods may not be suitable for complex small object detection tasks in real-world applications, such as surface defect detection for the printed circuit board (PCB) [9], tiny target detection for remote sensing images [31], and long-distance motion target detection [6]. A seemingly natural idea is to develop an advanced small object detection framework by making full use of context information and enhanced feature fusion together.


In this article, a novel feature fusion method, an atrous spatial pyramid pooling (ASPP) balanced FPN (ABFPN), is put forward for small object detection. The developed ABFPN makes full use of the advantages of the aforementioned three types of small object detection methods. Speciﬁcally, a skipASPP module is developed to enhance feature fusion and expand the receptive ﬁeld, where the ASPP with different dilation rate D is set in a skip-connection manner [7]. Besides, a balanced module consisting of three blocks (i.e., the resize & average block, the space nonlocal block, and the residual block) is applied to learn the semantic and detailed information more effectively. The features fused by the balanced module can have balanced information from each feature map with different resolutions, which can avoid the semantic information in nonadjacent layers being weakened with lateral connections. Notice that the FPN is selected as the basis of the proposed ABFPN due to its capability in dealing with multiscale changes through the integration of low- and highlevel features. It should be emphasized that the proposed ABFPN method is a competitive feature fusion approach, which can be embedded in any existing object detection framework.


As a typical small object detection task, PCB surface defect detection is very important in electrical and electronic engineering. Generally speaking, the surface defects in PCB can be classiﬁed into six categories: missing holes, mouse bite, open circuit, short circuit, spur, and spurious copper [9]. In the public datasets, it is found that the PCB surface defects normally lie in a concealed area, and some of them even exist in the tiny wiring part, which greatly increases the difﬁculty of surface defect detection.


Motivated by the above discussions, there is a need to develop an advanced object detection framework for PCB surface defect detection. In this article, an improved PCB defect detection (IPDD) framework is put forward for defect detection, where the proposed ABFPN is embedded as the feature fusion method in the IPDD framework. In summary, the main contributions of this article are outlined as follows.


1) A novel feature fusion method, the ABFPN, is proposed for small object detection, where a skip-ASPP module with diverse dilation rates is designed to enlarge the receptive ﬁeld. A balanced module is deployed to extract latent features for feature fusion. Experimental results demonstrate the effectiveness of the ABFPN on benchmark datasets. 2) An IPDD framework is put forward for PCB surface defect detection, where the developed ABFPN is embedded as the feature fusion method in the IPDD framework. An ablation study is conducted to verify the effectiveness of the IPDD framework. 3) The proposed IPDD framework is successfully applied to a public PCB tiny defect detection task. Experimental results demonstrate the superiority of the IPDD framework over seven state-of-the-art methods [including the improved YOLOv3 (Impro YOLOv3), the improved faster RCNN (Impro faster RCNN), the fully convolutional one-stage object detection algorithm (FCOS), the PaddlePaddle-YOLO (PP-Yolo), the tiny defect detection network (TDD-Net), the efﬁcient multiscale training method (sniper), and the deformable detection transformer (deformable DETR)] in terms of detection precision and recall. The remainder of this article is organized as follows. The proposed enhanced feature fusion method ABFPN and applied robustness enhancement strategies are elaborated in Section II. Comprehensive benchmark evaluations of the ABFPN are performed in Section III with an in-depth analysis of adopted strategies. In Section IV, the proposed ABFPN is further used to develop the IPDD framework, which is applied to the PCB surface tiny defect detection task. Finally, conclusions and an outlook of future works are presented in Section V.


## II. METHODOLOGY


In this section, the structure of a typical object detection framework is ﬁrst illustrated. Then, the developed ABFPN is presented where the skip-ASPP module and the balanced module are analyzed with details, which is a multiscale feature fusion approach for small-sized object detection tasks. Meanwhile, some robustness enhancement strategies are introduced for further improving the overall performance.


A. Structure of a Typical Object Detection Framework


In a typical object detection network, there are generally four basic components that are the input layer, the backbone, the neck, and the detection head [1]. The architecture of the typical object detection network is shown in Fig. 1.


In general, the input of the object detection framework requires data augmentation to boost the robustness of the


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 3 -->


ZENG et al.: SMALL-SIZED OBJECT DETECTION ORIENTED MULTISCALE FEATURE FUSION APPROACH 3507014


Fig. 1. General object detection framework.


Fig. 2. Diagram of the enhanced feature fusion method ASPP-balanced-FPN (ABFPN).


training model, especially for industrial applications. Some commonly used data augmentation techniques include spatial transformations (such as random scaling, cropping, and ﬂipping) and color distortions (e.g., changing transparency, brightness, and saturation). The backbone part is set for extracting features from the input layer. Some widely used models include the visual geometry group [44], the residual network (ResNet) [17], and the dark network [42]. The neck part is of vital importance in object detection. To be speciﬁc, feature fusion is carried out in the neck part to reprocess the extracted features and study the latent features according to different requirements. For example, the SSD proposed in [37] is applied for up and down sampling. The FPN can be used for path aggregation [33]. The last component of the object


detection framework is the detection head, which is utilized for localization and classiﬁcation. It should be mentioned that there is always a postprocessing module in the detection head, which usually refers to the nonmaximum suppression (NMS) method [25] and its improved versions, such as the soft NMS method [3] and the weighted NMS method [26].


B. ABFPN: An Enhanced Feature Fusion Approach


The diagram of the proposed ABFPN is depicted in the red dashed box of Fig. 2, where the proposed ABFPN is the neck part of the object detection framework. In the ABPFN, there are two designed modules (which are the skip-ASPP module and the balanced module) for feature fusion.


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 4 -->


## 3507014 IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022


In Fig. 2, C1 denotes the feature map obtained by downsampling the input image; C = {C2, C3, C4, C5} denote the feature maps obtained by the corresponding residual block in the backbone at each stage. In this context, C5 is the output feature map of the last residual block at the ﬁnal stage of the backbone, which is the input of the skip-ASPP module.


Compared with the traditional convolution operator, the atrous convolution operator could obtain a larger receptive ﬁeld without increasing the number of kernel parameters. In this article, D in the D-ASPP block stands for the dilation rate. Notice that the larger the dilation rate, the larger the corresponding receptive ﬁeld. As a result, ﬁve different D-ASPP blocks are employed in the developed ABFPN, which enables the model to capture multiscale context information. In the simulation, the values of D in ﬁve D-ASPP blocks are set to be 3, 6, 12, 18, and 24, respectively, which are the same as DenseASPP [50]. It should be pointed out that [50] adopts dense connection, which works well in networks with deeper layers, while, in the proposed skip-ASPP module as a part of the ABFPN, skip connection has been employed, which could also reduce the computational complexity so as to speed up the convergence and inference.


The skip connection is applied in the skip-ASPP module to enhance the interaction of the preoutput and postoutput features of each D-ASPP block and enhance the feature fusion. The work principle of the whole skip-ASPP module is formulated as follows:


⎧ ⎨⎨


C5 ⊕Si(C5), if i = 1 outi−1 ⊕Si(outi−1), if i = 2, 3, 4 Si(outi−1), if i = 5


outi =


(1)


⎨⎩


where Si(·)(i = 1, 2, 3, 4, 5) stands for the operation of corresponding D-ASPP blocks; each D-ASPP block contains 1 × 1 and 3 × 3 atrous convolution operator with dilation_rate = 3, 6, 12, 18, 24, respectively; ⊕is the concatenate operation; and outi(i = 1, 2, 3, 4, 5) is the obtained result in each D-ASPP, as marked in Fig. 2.


The ﬁnal output of the skip-ASPP module is calculated by


Out = S1(C5) ⊕S2(out1) ⊕S3(out2) ⊕S4(out3) ⊕S5(out4).


(2)


As shown in Fig. 2, the ﬁnal output of the skip-ASPP module is then added with C5 in the elementwise manner after the 1 × 1 convolution operator to obtain the feature map


P5. Similar to the conventional FPN, P = {P2, P3, P4, P5} shares a concatenated path from P5, which is combined with C = {C2, C3, C4, C5} through lateral connection. In particular, the upsampled P5, P4, and P3 are merged with the corresponding feature maps C4, C3, and C2 in the elementwise manner. Note that the 1 × 1 convolution operation is performed on {C2, C3, C4} to reduce the channel dimension before merging with feature maps. After that, the obtained feature maps P (including P2, P3, P4, and P5) are fed into the balanced module. In order to balance detailed and semantic information on small target detection tasks and improve the overall detection performance, the utilized balanced module contains three blocks, which are the resize & average block,


the space nonlocal block, and the residual block [39], [48]. The work [39] proposed Libra RCNN that solves the problem of imbalance image sampling and feature selection, especially the balanced operation of different layers. Inspired by this, utilized “balanced module” in the ABFPN handles the further reﬁned feature maps from FPN and skip-ASPP, which enables detection models achieve the balance of enhanced feature fusion and obtain more sufﬁcient image context and receptive ﬁeld information. To be speciﬁc, the resize & average block B1 is designed for gathering multilevel features in P by resizing and averaging P2, P3, and P5 to the same size as P4. The output of B1 is





pool(P2, 4), pool(P3, 2), intp(P5, 2)


x =


3 (3)


where pool(P2, 4) and pool(P3, 2) represent the max pooling operations with stride equaling to 4 and 2 for P2 and P3, respectively; intp(P5, 2) denotes the nearest neighbor interpolation for P5 with multiplier factors of height and width equaling to 2.


In general, once the scale of convolutional kernels is determined, the generated receptive ﬁeld will be restricted to some local regions of the feature map. To overcome the limitation of local information, the space nonlocal module B2 is employed to gather global information of the feature map. Based on the output of B1, the nonlocal output yi is obtained by


∀j f xi, x j


c x j





(4)


yi =





xi, x j


∀j f


where xi ∈x indicates the information of the current focused location; x j represents the global information of the output of


B1; c(·) is the 1 × 1 convolution operator; and f (·) is the Embedded Gaussian function used to calculate the similarity of xi and x j. f (·) is deﬁned by


= eθ(xi)T ·φ(x j) (5)


xi, x j


f


where θ(·) and φ(·) both stand for 1 × 1 convolution operator. According to [48], the output of block B2 is


zi = c(yi) + xi (6)


where c(·) is the 1 × 1 convolution operator.


The residual block B3 scatters reﬁned features from the output of B2 in a multilevel manner through a residual path. To be speciﬁc, the operation of block B3 can be expressed by the following formula:


zk, 0.5k−4


, (k = 2, 3, 4, 5) (7)


Fk = Pk + intp


where intp(·) resizes the output of the space nonlocal block zk to be identical with the corresponding feature maps Pk(k = 2, 3, 4, 5). Finally, via a skip connection, the output feature maps F = {F2, F3, F4, F5} of the entire ABFPN approach are obtained.


## C. Robustness Enhancement Strategies for Object Detection


It is worth pointing out that the proposed ABFPN serves as the neck part in an object detection framework.


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 5 -->


ZENG et al.: SMALL-SIZED OBJECT DETECTION ORIENTED MULTISCALE FEATURE FUSION APPROACH 3507014


The developed ABFPN aims to sufﬁciently merge abundant context information with the hope to achieve satisfactory detection accuracy for small-size objects. To further improve the generalization ability and detection accuracy of the framework, some existing robustness enhancement strategies are employed in other components of the object detection framework.


In this article, two well-known data augmentation techniques, the AutoAugmetImage method [8] and the Mixup method [52], are applied in the input part of the model training process. Both of them can enhance the model performance, and to be speciﬁc, AutoAugmetImage can automatically select the optimal combination of enhancement strategies for different datasets, which customizes a data-speciﬁc augmentation scheme, whereas the Mixup method can enrich the database via randomly mixing two samples, including their labels. In this way, the inﬂuence of samples with the wrong label can be greatly reduced so that the model robustness is improved.


In the backbone part, the ResNet proposed in [17] has become a popular network structure. In this article, the ResNeXt structure [49] is adopted as the backbone, which includes stacked bottleneck paths with the same topology and one shortcut pooling path. It should be highlighted that each bottleneck path contains a squeeze-and-excitation (SE) attention mechanism, which is denoted as the attention bottleneck path in this article. Unimportant channel features are suppressed via an SE operator in each path, and the SE operator essentially consists of one global average pooling layer and two fully connected layers with the sigmoid function [21]. Moreover, the deformable convolution operator [54] is employed as a substitution of the traditional convolution operator so that the receptive ﬁeld can be adaptively adjusted according to size, posture, and other geometric changes of the objects. Furthermore, a stride equaling to 2 is shifted from the ﬁrst 1 × 1 convolution operator to the 3 × 3 one in each attention bottleneck path. In addition, a stride equaling to 2 is shifted from the 1 × 1 convolution operator to the 2 × 2 average pooling operator in the shortcut pooling path. The operation of shifting the position with a stride size of 2 could prevent the loss of a large amount of feature information. The diagram of the enhanced ResNeXt block is displayed in Fig. 3.


The cascade RCNN introduced in [4] is selected as the detection head in this article, which is denoted by cascade RCNN* in Fig. 2. Speciﬁcally, the complete intersection over union (CIoU) loss proposed in [57] is applied to evaluate the predicted bounding box. The DIoU-NMS serves as the postprocessing method [57]. The CIoU loss and DIoU-NMS are utilized in the postprocessing stage of the head part in the object detection framework. It is remarkable that the employment of CIoU loss and DIoU-NMS considers: 1) the overlap areas between the predicted box and ground truth; 2) the distance between the center points of the predicted box and ground truth; and 3) the aspect ratio of the bounding box, which would lead to a more reliable prediction result than traditional methods.


Fig. 3. Illustration of the enhanced ResNeXt block.


## III. EVALUATIONS OF THE PROPOSED


## ASPP-BALANCED-FPN ON


BENCHMARK DATASETS In this section, sufﬁcient ablation studies are conducted on three public benchmark datasets for verifying the performance of the proposed ABFPN, which are the COCO [34], the VOC [11], and the VisDrone detection dataset [56]. A brief introduction of adopted datasets and experimental settings is presented. Meanwhile, the faster RCNN with ResNet50 [43] is selected as the baseline of detection method to verify the effectiveness and generalization ability of the proposed ABFPN along with the utilized robustness enhancement strategies. A series of ablation studies are performed under the same condition for evaluation.


A. Experiment Settings and Datasets


In this work, three well-known benchmark datasets in object detection, the MS COCO2017, the Pascal VOC07+12, and the VisDrone2019 detection datasets, are applied for performance evaluation. The COCO2017 dataset is a large-scale image dataset consisting of 330 000 images of which more than 200 000 are labeled. In COCO2017, there are 1.5 million object instances belonging to 80 categories. The Pascal VOC07+12 dataset contains two mutually exclusive image datasets (i.e., VOC2007 and VOC2012), which covers 20 kinds of objects, and the number of instances in Pascal VOC07+12 is over 20 000. The VisDrone2019 dataset contains ten classes and 54200 instances of remotely sensed objects collected by drones, which covers complex scenes under different weather and lighting conditions, and the detected targets are relatively small in size, which makes the detection more challenging.


In the experiment on the COCO2017 dataset, the numbers of training and testing samples are 118 287 and 5000, respectively. For the VOC07+12 dataset, 16 551 images are used for training, and 4952 images are utilized for testing. The training and validation sets of the VisDrone2019 detection dataset have 7018 and 1609 images, respectively. All models are trained on the PaddlePaddle 1.8.4 framework with a single


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 6 -->


## 3507014 IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022


## TABLE I


## EXPERIMENTAL SETTINGS


## TABLE II


## ABLATION STUDY ON THE MS COCO2017 DATASET


GPU TeslaV100 (16 GB memory). Detailed information of experimental settings on three datasets is presented in Table I.


B. Experimental Results


As aforementioned, evaluations of the proposed ABFPN and several designed strategies are performed mainly in the form of an ablation study on three benchmarks, where the two-stage network faster RCNN is selected as the baseline method.


1) Validation on COCO2017: Table II presents the experimental results of the ablation study on the COCO2017 dataset, where the evaluation metrics include average precision and its extensions. To be speciﬁc, AP is average precision over IoU at [0.5:0.95:0.05] (from 0.5 to 0.95 with the interval of 0.05). AP@50 is AP over IoU at 0.5. APs, APm, and APl refer to average detection precision on small-, medium-, and largescale objects, respectively. As shown in Table II, the AP of the proposed ABFPN is 0.9% larger than that of the FPN. On the APs and APm metrics, the results of the ABFPN are 3.7% and 0.7% larger than that of the FPN, respectively, while the APl result of the ABFPN is slightly smaller than that of the FPN, and the AP@50 of both methods are the same. Furthermore, experimental results of the model (that combines the ABFPN with the robustness enhancement strategies) are better than that of the faster RCNN with the neck of the FPN on all metrics. Speciﬁcally, the AP, AP@50, APs, APm, and APl of the faster RCNN with the ABFPN and strategies are larger than that with the FPN by 4.7%, 4.4%, 6.6%, 4.3%, and 4.1%, respectively.


According to the experimental results, the proposed ABFPN is a reliable feature fusion method, which greatly increases the detection precision of small-size objects. Though the proposed ABFPN performs not well on the indicator APl, which may be caused by overﬁtting because the ABFPN concentrates on the latent context information. By introducing a series of robustness enhancement strategies, the deﬁciency of the ABFPN on the indicator APl is overcome. Other indicators have been signiﬁcantly increased as well, indicating improved overall performance. As such, the combination of the ABFPN and robustness enhancement strategies performs better than the


## TABLE III


## ABLATION STUDY ON THE PASCAL VOC07+12 TESTING DATASET


ABFPN-based faster RCNN and the traditional faster RCNN based on experimental results on the COCO2017 dataset.


2) Validation on VOC07+12: Experimental results on the VOC07+12 testing set are displayed in Table III. The popular metric mAP (0.50, 11point) is employed on the VOC07+12 dataset, where mAP (0.50, 11point) stands for the mean average precision values of 11 points with IoU greater than 0.5 and recall in the range of [0:1:0.1] (from 0 to 1 with the interval of 0.1).


In Table III, it can be clearly observed that the mAP of the ABFPN is 84.06%, which is nearly 1% larger than that of the standard FPN. After introducing the robustness enhancement strategies, the mAP value of the modiﬁed ABFPN-based object detection framework is further increased to 85.59%, which indicates that the applied robustness enhancement strategies, indeed, improve the overall performance of the framework.


Furthermore, the performance comparison of the faster RCNN [43], the hierarchical shot detector (HSD) [5], the Perona Malik [24], the intertwiner network (InterNet) [28], the reﬁnement detector (ReﬁneDet) [53], the Blitz Network (BlitzNet) [10], the early exit evolutionary architecture network (EEEA-Net) [46], and our method on the VOC07+12 dataset is shown in Table IV. Notice that the data of the utilized methods are directly obtained from the corresponding literature, which is marked in Table IV. Experimental results demonstrate the effectiveness of the proposed ABFPN for small-size objects’ detection compared with some state-of-theart algorithms. It is noteworthy that the comparison algorithms


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 7 -->


ZENG et al.: SMALL-SIZED OBJECT DETECTION ORIENTED MULTISCALE FEATURE FUSION APPROACH 3507014


Fig. 4. Diagram of the proposed IPDD framework.


## TABLE IV


## DETECTION EVALUATION RESULTS OF DIFFERENT ALGORITHMS ON THE


## PASCAL VOC07+12 TESTING DATASET


used are architecturally designed to be suitable for application to small target detection tasks; hence, the results are totally comparable. Speciﬁcally, the proposed method achieves the best result in terms of mAP.


3) Validation on VisDrone2019: In this part, the results of the ABFPN-based object detection framework with the robustness enhancement strategies on the VisDrone2019 detection dataset are with the ablation studies in Table V. It is worth mentioning that the detection on the VisDrone2019 dataset is a difﬁcult small-sized target detection task, and the chosen evaluation metrics are the same as used on the COCO2017 dataset. As can be seen from Table V, the ABFPN can also guarantee a 1% improvement in average precision on complex detection tasks compared to the FPN, and the better performance is especially noticeable on smaller size targets. When related strategies are further introduced, the improvement in the ﬁve metrics AP, AP@50, APs, APm, and APl is 2.5%, 3.2%, 2.3%, 3.5%, and 2.7%, respectively, compared to the original FPN.


The validation of the ablation experiments on the above three public challenging datasets demonstrates the effectiveness of the proposed ABFPN and related strategies, which are particularly suitable for small-sized detection tasks; meanwhile, the generalization ability of the ABFPN is also proven


on multiple databases. To further validate the practicality of the ABFPN, in next section, it is applied to detect tiny surface defects of PCB.


## IV. APPLICATION IN PCB DEFECT DETECTION


In this section, an IPDD framework is designed to detect tiny surface defects in PCB, where the proposed ABFPN is incorporated with the aforementioned robustness enhancement strategies. To verify its effectiveness and practicality, the developed IPDD framework is tested on the public PCB defect dataset.


A. IPDD Framework


The proposed IPDD framework consists of the input layer, the backbone, the neck, and the detection head. The diagram of the IPDD framework is displayed in Fig. 4. The enhancement strategies used in each part of the IPDD framework are described in Section II-C. It is worth emphasizing that the enhanced ResNeXt structure (including 152 layers with 50 blocks) is selected as the backbone, which is denoted as Enhanced-ResNeXt-152. Meanwhile, the proposed ABFPN is chosen as the neck part, and the cascade RCNN* is selected as the detection head.


In object detection, localization and classiﬁcation are the most signiﬁcant tasks, by which the object bounding box and the corresponding category are determined correctly. In Fig. 4, the localization and classiﬁcation are highlighted within a blue box. In the proposed IPDD framework, the head part employs a region proposal network (RPN) to obtain regions of interest (RoI). In addition, the RPN is applied to distinguish the foreground (i.e., the PCB surface defects) and the background.


As stated previously, the feature maps F = {F2, F3, F4, F5} are the ﬁnal output of the neck part and are also the input of the detection head. Then, multiple proposals with different sizes and aspect ratios are generated at each position of the feature map. Each proposal is matched with corresponding ground truth and performed by the IoU threshold ﬁltering operation, which could, thus, distinguish positive and negative samples.


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 8 -->


## 3507014 IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022


## TABLE V


## ABLATION STUDY ON THE VISDRONE2019 DETECTION DATASET


The bounding box loss function Lrpn_bbox in the RPN is expressed by


2


0.5 ∗


, if dif < σ


locp −loct


M


Lrpn_bbox =


locp −loct


 −0.5 ∗σ 2





, otherwise


σ ∗


M


(8)


where M is the average operation; locp and loct represent the location of bbox (short for bounding box) predicted by the RPN and the target bbox, respectively; dif = |locp−loct| is the absolute value of the difference between locp and loct; and σ is the threshold parameter, which is set to 3 in this simulation. Besides, the classiﬁcation loss function of the RPN is





##  K 


−s j


si


Lrpn_cls = M


cls · l j + log


exp


cls


i=0


( j = 1, 2, . . . , K) (9)


where scls denotes the prediction score, l is the real label, and


K represents the total number of categories.


It should be highlighted that the RPN only accomplishes the rough proposals, which needs further reﬁnements. In fact, a single PCB image may probably contain more than one defect. As such, it is of vital signiﬁcance to further identify each type precisely from the proposals. Both the feature map


F and the generated RoI have performed a series of cascade operations, denoted by the RoI align and the Bbox head blocks, as shown in Fig. 4.


Three cascade levels are resampled to increase the IoU value of the proposals stage by stage. The “RoI align” blocks adjust features of the candidate areas to a ﬁxed size through the pooling operation. The “Bbox head” blocks obtain the prediction bounding box Bpre and classiﬁcation score Scls. Each cascade stage is trained by using the positive and negative samples with different IoUs, and the output of the previous stage serves as the input of the next stage. If the IoU of the generated RoI increases, the next cascade stage will focus on a certain area in the updated proposal, so as to improve the detection accuracy.


For loss functions of the detection head, the classiﬁcation loss function Lhead_cls adopts the cross-entropy loss function, as shown in (9), and the CIoU loss mentioned in Section II-C is used for the bounding box loss Lhead_bbox. The bounding box loss Lhead_bbox of the head is calculated by








1 −IoU + dist


+ αν


Lhead_bbox = M


bp, bt


(10)


where bp and bt represent the predicted box and the real bounding box, respectively; α and ν are two inﬂuence factors with respect to the aspect ratio of bp and bt. dist(·) calculates


the distance between bp and bt, which is deﬁned by


= ρ2


bp, bt


bp, bt


dist


c2 (11)


where c is the diagonal distance of the smallest bounding rectangle, which can cover both bp and bt; ρ(·) stands for the Euclidean distance.


The total loss function of the cascade RCNN* is given by


3 


Li


head_cls + Li


Ltotal = Lrpn_cls + Lrpn_bbox +


(12)


head_bbox


i=1


where Lhead_cls is the cross-entropy loss function, as shown in (9).


The DIoU-NMS method is applied for further reﬁning the prediction results to preserve the best bounding box, as there may be other redundant PCB tiny defects. It is worth mentioning that the DIoU-NMS method considers not only the IoU value but also the distance between center points of two bounding boxes. The DIoU-NMS method provides a score as reference, and the process of the method is


scorei, if |IoU −dist(bM, bi)| < 0, otherwise (13)


scorei =


where is the threshold of the DIoU-NMS method, which is set to be 0.5 in this work; bM is the bounding box with the highest conﬁdence value, and bi stands for nearby boxes. If the score is set to be 0, the corresponding box will be redundant for a certain defect, which will be ﬁltered out. Otherwise, a small value of |IoU −dist(bM, bi)| implies that the obtained box may belong to another defect, which should not be eliminated arbitrarily.


The pseudocode of the proposed IPDD framework is provided in Algorithm 1.


B. Evaluation Results and Discussions of the IPDD Framework


To evaluate the performance of the proposed IPDD framework, the PKU public PCB defect detection dataset has been adopted [9]. Some existing defect detection algorithms have been utilized for performance evaluation, including the Impro YOLOv3 [29], the FCOS [47], the PP-Yolo [38], the Impro faster RCNN [19], the TDD-Net [9], the deformable DETR [55], and the sniper [45]. Among the utilized methods, the Impro faster RCNN, the TDD-Net, the deformable DETR, and the sniper are two-stage methods, which are similar to our IPDD framework.


The utilized dataset contains 693 images with six different types of defects (including missing hole, mouse bite, open


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 9 -->


ZENG et al.: SMALL-SIZED OBJECT DETECTION ORIENTED MULTISCALE FEATURE FUSION APPROACH 3507014


Algorithm 1 Pseudocode of the Proposed IPDD Framework Require:


RGB images with PCB surface defects Ensure:


The predicted bounding boxes and corresponding classiﬁcation results of PCB defects


1: Use the AutoAugmetImage and mixup techniques for data augmentation; 2: the Backbone part Enhanced-ResNeXt-152 returns feature maps C = {C2, C3, C4, C5}; 3: the Neck part ABFPN outputs feature maps F = {F2, F3, F4, F5} based on Eq. 1 - Eq. 7;


4: Enter the region proposal network (RPN) in the head part to generate regions of interest (RoI);


5: Calculate the loss of the RPN, including Lrpn_bbox by Eq. 8 and Lrpn_cls by Eq. 9; 6: For i from 1 to 3: Perform RoI align feature extraction; Obtain the updated bounding box Bpre and classiﬁcation score Scls;


Calculate Lhead_bbox and Lhead_cls referring to Eq. 10 and Eq. 11; Endfor


7: Calculate total loss Ltotal of the head part according to Eq. 12;


8: Apply the DIoU-NMS method for further reﬁnement; 9: Get the ﬁnal prediction bounding boxes and corresponding classiﬁcation scores.


circuit, short, spur, and spurious copper). The dataset is visualized in Fig. 5, where the number of each defect type is plotted in Fig. 5(a). area_ratios is the proportion of the ground-truth bounding box to the entire image, which also reﬂects the relative size of objects for detection. In Fig. 5(b), it is clear that almost all defects only occupy a tiny area in an image, which makes it challenging to achieve accurate positioning and classiﬁcation results.


In the simulation, the proposed IPDD framework is trained with 50 000 iterations, and the initial learning rate is 0.00125. The decay factor is 0.1 in the iteration interval of [42 000, 48 000]. 593 PCB images are randomly selected as the training samples, whereas the rest 100 pictures are used for testing. Other experimental settings and environments remain the same, as presented in Section III.


1) Algorithm Veriﬁcation and Comparison: The change curves of ﬁve loss functions (i.e., Lrpn_cls, Lrpn_bbox, Lhead_cls,


Lhead_bbox, and Ltotal) are shown in Fig. 6, where each loss value is calculated every 50 iterations. It is observed that, when iteration passes nearly 880 × 50 = 44 000, the oscillation of


Ltotal is restricted in a small range, which can be deemed to reach the stable state. Besides, Fig. 6(f) presents the change of AP, where AP@50 and AP@75 denote AP over IoU at 0.5 and 0.75, respectively. The precision value is sampled every 2000 iteration, and when evaluation times reach 22, i.e., the number of iterations is 22 × 2000 = 44 000, the curves tend


Fig. 5. Partial visualization information of the PCB defect detection dataset. (a) Number of each PCB defect type. (b) Frequency of various area_ratios.


to be converged when AP, AP@50, and AP@75 are 56.4%, 98.8%, and 57.8%, respectively. Table VI displays the comparison results of the proposed IPDD framework and the other seven state-of-the-art detection methods. It is noteworthy that Impro YOLOv3, FCOS, deformable DETR, and sniper are all the detection methods with excellent performance in small-sized object detection tasks, and TDD-Net is a speciﬁc method proposed for PCB small defect detection. Evaluation metrics are the same, as presented in Table II, with two extra ones that are AP@75 and average recall (AR) rate. The larger the AR rate, the more positive samples are classiﬁed correctly. As shown in Table VI, the proposed IPDD framework achieves the best results on all performance indicators, which demonstrates the effectiveness of the IPDD framework for PCB defect detection. In particular, the IPDD framework outperforms the suboptimal method sniper on all evaluation metrics of AP, AP@50, AP@75, APs, APm, APl, and AR. Compared with Impro YOLOv3 (which ranks second on APs), the indicator APs is improved by 1.7% when using the IPDD framework, which indicates the superiority of the proposed IPDD framework on detecting small defects.


In addition, TDD-Net, a dedicated algorithm proposed for PCB tiny defect detection, is selected in this article as a comparison method for visualization and subsequent error analysis. For an intuitive view, experimental results of the proposed IPDD framework and the TDD-Net are visualized in Fig. 7. The ﬁrst two columns are results obtained by the IPDD framework, where images are enlarged for a clear view. Similarly, the last two columns are results obtained by the TDD-Net. It should be highlighted that, for the mouse_bite defect shown in line 3, the TDD-Net outputs a


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 10 -->


## 3507014 IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022


Fig. 6. Iteration curves of loss functions and precision. (a) Lrpn_cls. (b) Lrpn_bbox. (c) Lcls_head. (d) Lbbox_head. (e) Ltotal. (f) precision.


## TABLE VI


## COMPARISONS OF DIFFERENT METHODS FOR PCB DEFECT DETECTION


redundant prediction bounding box. By using the proposed IPDD framework, the positioning is more accurate than that of the TDD-Net with a higher conﬁdence value that equals 0.99, which shows that the proposed IPDD framework demonstrates better overall performance than TDD-Net in terms of both localization and classiﬁcation of small objects.


Furthermore, to comprehensively evaluate the detection performance of the proposed IPDD framework on each type of defect, the precision–recall (PR) and score–recall (SR) curves are employed for evaluation. Experimental results are shown in Fig. 8, where the IoU threshold is ﬁxed to 0.5. The PR curve reﬂects a tradeoff between classiﬁcation accuracy and capability to cover positive samples (i.e., recall). The SR curve shows the conﬁdence scores under different recall values.


Generally, the value of precision and conﬁdence scores will monotonically decline as recall increases. Thus, an effective and practical model is supposed to enable the precision and conﬁdence scores to maintain stability even when the recall is increased. As a result, the larger area enclosed by PR, SR curves, and coordinate axes, the better performance of the model. Fig. 8 shows that the IPDD framework is able to keep the value of precision and conﬁdence score at a high


Fig. 7. Comparison of visualization results of our IPDD framework (left two columns) and TDD-Net (right two columns).


level with growing recall, which validates the robustness and reliability of the IPDD framework on PCB defect detection.


2) Ablation Study and Error Analysis: To further validate the effectiveness of our proposed IPDD framework, an ablation study has been conducted in this article, where two


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 11 -->


ZENG et al.: SMALL-SIZED OBJECT DETECTION ORIENTED MULTISCALE FEATURE FUSION APPROACH 3507014


Fig. 8. Precision–recall and score–recall curves of each defect type (IoU = 0.5).


## TABLE VII


## ABLATION STUDY RESULTS OF THE IPDD FRAMEWORK


variant IPDD frameworks (i.e., IPDD-Nv1 and IPDD-Nv2) are adopted. To be speciﬁc, the IPDD framework employs both the designed ABFPN and other robustness enhancement strategies. In the variant IPDD framework, IPDD-Nv1, the input layer is the original one without using data argumentation techniques, the backbone is the conventional ResNeXt-152, the neck part is the proposed ABFPN, and the cascade RCNN is used as the detection head. The only difference between IPDD-Nv2 and IPDD-Nv1 is that the neck part in IPDD-Nv2 is a conventional FPN.


The ablation study results are shown in Table VII. It can be seen in Table VII that IPDD-Nv1 outperforms IPDD-Nv2 on all indicators, particularly on APs. The APs of IPDD-Nv1 is 3.1% larger than that of the IPDD-Nv2, which indicates the competitiveness of the designed ABFPN (that can be seen as an outstanding feature fusion method). By further introducing robustness enhancement strategies, it is found that, except for APs, the IPDD framework has increased by 0.6%, 0.6%, 3.6%, 0.6%, 2.9%, and 0.7%, respectively, on AP, AP@50, AP@75, APm, APl, and AR compared with IPDD-Nv1. On the APs metric, the value of APs in the proposed IPDD framework is slightly smaller than that of the IPDD-Nv1 due mainly to the reason that the applied strategies focus on objects with middle size or large size. As such, the proposed IPDD framework could achieve satisfactory overall detection performance. Improvements on the other six indicators have demonstrated


that other introduced strategies can effectively enhance the robustness of the model.


Fig. 9 is the scatter plot of the precision and recall, including eight PCB defect detection methods and the two variant IPDD frameworks. Based on the relationship between precision and recall, the point in the upper right corner indicates that the model is robust. As can be seen in Fig. 9, the proposed IPDD framework is the best out of ten methods. It should also be noticed that the variant IPDD-Nv1 that only employs the proposed ABFPN ranks second, which implies that the introduced ABFPN is competitive in small object detection.


In addition, the PR curve is used for error analysis [18]. Fig. 10(a) and (b) shows the PR curves of the TDD-Net and the IPDD framework, where seven colored areas are marked. To be speciﬁc, C75 and C50 stand for the area enclosed by the PR curve and coordinate axes at IoU = 0.75 and IoU = 0.5, respectively. Compared with the TDD-Net, the proposed IPDD framework has an improvement on the AP by 3.6% on C50 and 14.1% on C75, which indicates the effectiveness and superiority of the proposed ABFPN in positioning. After removing location errors, the obtained new area is denoted by the indicator Loc. Notice that AP of the IPDD framework on Loc is further increased from 98.8% to 99.3%, whereas AP of TDD-Net on Loc is changed from 95.2% to 96.5%, which indicates that inaccurate localization is a common reason


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 12 -->


## 3507014 IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022


Fig. 9. Scatter plot of the precision–recall relationship of each algorithm.


Fig. 10. Error analysis via precision–recall curves. (a) TDD-Net. (b) IPDD framework.


that causes the low detection performance. To conclude, the proposed IPDD framework performs better than the TDD-Net.


The indicator Oth is the value of AP after eliminating all misclassiﬁcation results; furthermore, when all false-positive samples are removed, the AP value is characterized by BG. It is found that both Oth and BG remain unchanged in Fig. 10(b), which shows that the IPDD framework could


achieve precise classiﬁcations. The results on AP regarding Oth and BG in the TDD-Net demonstrate that the classiﬁcation accuracy of the TDD-Net is worse than that of the proposed IPDD framework. The last indicator FN is the AP value after eliminating all kinds of mistakes. Based on the above discussions, the proposed IPDD framework demonstrates remarkable classiﬁcation accuracy, and the main reason for inaccurate detection is imperfect positioning performance.


## V. CONCLUSION


In this article, an IPDD framework has been put forward for PCB surface defect detection, where an ABFPN has been designed as the neck part of the IPDD framework for feature fusion. In the developed ABFPN, the atrous convolution operator with different dilation rates has been utilized to enlarge the receptive ﬁeld. The skip connection has been adopted for the atrous convolution operators, which could enhance the interactions among features at different levels. In addition, a balanced module has been introduced in the ABFPN for studying the semantic information of the obtained features. The performance of the ABFPN has been evaluated on three public datasets, and the ablation studies prove the effectiveness of the ABFPN, especially for small-sized objects. The designed IPDD framework has been successfully applied to small object detection with application to PCB surface defect detection. Several robustness enhancement strategies have been employed in the IPDD framework to further improve the overall detection performance. Experimental results have demonstrated the superiority of the proposed IPDD framework over seven state-of-the-art methods in terms of both localization and classiﬁcation.


In the future, we aim to: 1) apply the proposed IPDD framework to other small object detection tasks, such as defect detection of industrial components and object detection in pastoral landscapes; 2) investigate a precise localization method to improve the positioning performance of the IPDD framework; and 3) utilize evolutionary computation algorithms to tune the hyperparameters of the proposed IPDD framework.


## REFERENCES


[1] A. Bochkovskiy, C.-Y. Wang, and H.-Y. Mark Liao, “YOLOv4: Optimal


speed and accuracy of object detection,” 2020, arXiv:2004.10934. [2] Y. Bao et al., “Triplet-graph reasoning network for few-shot metal


generic surface defect segmentation,” IEEE Trans. Instrum. Meas., vol. 70, pp. 1–11, 2021. [3] N. Bodla, B. Singh, R. Chellappa, and L. S. Davis, “Soft-NMS–


improving object detection with one line of code,” in Proc. IEEE Int. Conf. Comput. Vis., Oct. 2017, pp. 5562–5570. [4] Z. Cai and N. Vasconcelos, “Cascade R-CNN: High quality object


detection and instance segmentation,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 43, no. 5, pp. 1483–1498, May 2021. [5] J. Cao, Y. Pang, J. Han, and X. Li, “Hierarchical shot detector,” in Proc.


IEEE Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 9704–9713. [6] E. Chen, O. Haik, and Y. Yitzhaky, “Online spatio-temporal action


detection in long-distance imaging affected by the atmosphere,” IEEE Access, vol. 9, pp. 24531–24545, 2021. [7] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille,


“DeepLab: Semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected CRFs,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 40, no. 4, pp. 834–848, Apr. 2018. [8] E. D. Cubuk, B. Zoph, D. Mane, V. Vasudevan, and Q. V. Le, “AutoAug


ment: Learning augmentation strategies from data,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2019, pp. 113–123.


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 13 -->


ZENG et al.: SMALL-SIZED OBJECT DETECTION ORIENTED MULTISCALE FEATURE FUSION APPROACH 3507014


[9] R. Ding, L. Dai, G. Li, and H. Liu, “TDD-Net: A tiny defect detection


network for printed circuit boards,” CAAI Trans. Intell. Technol., vol. 4, no. 2, pp. 110–116, 2019. [10] N. Dvornik, K. Shmelkov, J. Mairal, and C. Schmid, “BlitzNet: A real


time deep network for scene understanding,” in Proc. 16th IEEE Int. Conf. Comput. Vis. (ICCV), Venice, Italy, Oct. 2017, pp. 4174–4182. [11] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and A. Zisser


man, “The Pascal visual object classes (VOC) challenge,” Int. J. Comput. Vis., vol. 88, no. 2, pp. 303–338, Sep. 2009. [12] H. Geng, H. Liu, L. Ma, and X. Yi, “Multi-sensor ﬁltering fusion


meets censored measurements under a constrained network environment: Advances, challenges and prospects,” Int. J. Syst. Sci., vol. 52, no. 16, pp. 3410–3436, Dec. 2021. [13] R. Girshick, J. Donahue, T. Darrell, and J. Malik, “Rich feature


hierarchies for accurate object detection and semantic segmentation,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Columbus, OH, USA, Jun. 2014, pp. 580–587. [14] R. Girshick, “Fast R-CNN,” in Proc. ICCV, Sep. 2015, pp. 1440–1448. [15] K. He, G. Gkioxari, P. Dollár, and R. Girshick, “Mask R-CNN,”


IEEE Trans. Pattern Anal. Mach. Intell., vol. 42, no. 2, pp. 386–397, Feb. 2020. [16] K. He, X. Zhang, S. Ren, and J. Sun, “Spatial pyramid pool


ing in deep convolutional networks for visual recognition,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 37, no. 9, pp. 1904–1916, Sep. 2014. [17] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for


image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Apr. 2016, pp. 770–778. [18] D. Hoiem, Y. Chodpathumwan, and Q. Dai, “Diagnosing error in


object detectors,” in Proc. Eur. Conf. Comput. Vis. (ECCV), Oct. 2012, pp. 340–353. [19] B. Hu and J. Wang, “Detection of PCB surface defects with improved


faster-RCNN and feature pyramid network,” IEEE Access, vol. 8, pp. 108335–108345, 2020. [20] H. Hu, J. Gu, Z. Zhang, J. Dai, and Y. Wei, “Relation networks for object


detection,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2018, pp. 3588–3597. [21] J. Hu, L. Shen, S. Albanie, G. Sun, and E. Wu, “Squeeze-and-excitation


networks,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 42, no. 8, pp. 2011–2023, Aug. 2020. [22] J. Hu, H. Zhang, H. Liu, and X. Yu, “A survey on sliding mode


control for networked control systems,” Int. J. Syst. Sci., vol. 52, no. 6, pp. 1129–1147, Apr. 2021. [23] Y. Ju, X. Tian, H. Liu, and L. Ma, “Fault detection of networked


dynamical systems: A survey of trends and techniques,” Int. J. Syst. Sci., vol. 52, no. 16, pp. 3390–3409, Dec. 2021. [24] S. Mishra et al., “Learning visual representations for transfer learning


by suppressing texture,” 2020, arXiv:2011.01901. [25] A. Neubeck and L. J. Van Gool, “Efﬁcient non-maximum suppression,”


in Proc. IEEE Int. Conf. Pattern Recognit., Aug. 2006, pp. 850–855. [26] C. Ning, H. Zhou, Y. Song, and J. Tang, “Inception single shot MultiBox


detector for object detection,” in Proc. IEEE Int. Conf. Multimedia Expo. Workshops (ICMEW), Jul. 2017, pp. 549–554. [27] H. Law and J. Deng, “CornerNet: Detecting objects as paired keypoints,”


in Proc. Eur. Conf. Comput. Vis., Sep. 2018, pp. 734–750. [28] H. Li, B. Dai, S. Shi, W. Ouyang, and X. Wang, “Feature intertwiner


for object detection,” 2019, arXiv:1903.11851. [29] J. Li, J. Gu, Z. Huang, and J. Wen, “Application research of improved


YOLO v3 algorithm in PCB electronic component detection,” Appl. Sci., vol. 9, pp. 3738–3750, 2019. [30] J. Li, X. Liang, Y. Wei, T. Xu, J. Feng, and S. Yan, “Perceptual


generative adversarial networks for small object detection,” in Proc. IEEE CVPR, Jul. 2017, pp. 1951–1959. [31] J. Li and Z. Liu, “Self-measurements of point-spread function for remote


sensing optical imaging instruments,” IEEE Trans. Instrum. Meas., vol. 69, no. 6, pp. 3679–3686, Jun. 2020. [32] Y. Li, Y. Chen, N. Wang, and Z.-X. Zhang, “Scale-aware trident


networks for object detection,” in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 6053–6062. [33] T.-Y. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan, and S. Belongie,


“Feature pyramid networks for object detection,” in Proc. CVPR, Jul. 2017, pp. 936–944.


[34] T. Lin et al., “Microsoft COCO: Common objects in context,” in Proc.


Eur. Conf. Comput. Vis., Oct. 2014, pp. 740–755. [35] S. Liu, D. Huang, and Y. Wang, “Learning spatial fusion for single-shot


object detection,” 2019, arXiv:1911.09516. [36] S. Liu, L. Qi, H. Qin, J. Shi, and J. Jia, “Path aggregation network for


instance segmentation,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Jun. 2018, pp. 8759–8768. [37] W. Liu et al., “SSD: Single shot multibox detector,” in Proc. Eur. Conf.


Comput. Vis., Aug. 2016, pp. 21–37. [38] X. Long et al., “PP-YOLO: An effective and efﬁcient implementation


of object detector,” 2020, arXiv:2007.12099. [39] J. Pang, K. Chen, J. Shi, H. Feng, W. Ouyang, and D. Lin, “Libra


R-CNN: Towards balanced learning for object detection,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., no. 3, Jun. 2019, pp. 821–830. [40] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You only look


once: Uniﬁed, real-time object detection,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2016, pp. 779–788. [41] J. Redmon and A. Farhadi, “YOLO9000: Better, faster, stronger,”


in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jul. 2017, pp. 6517–6525. [42] J. Redmon and A. Farhadi, “YOLOV3: An incremental improvement,”


in Proc. IEEE Conf. CVPR, Apr. 2017, pp. 1–6. [43] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN: Towards


real-time object detection with region proposal networks,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 39, no. 6, pp. 1137–1149, Jun. 2017. [44] K. Simonyan and A. Zisserman, “Very deep convolutional networks for


large-scale image recognition,” in Proc. Int. Conf. Learn. Represent. (ICLR), San Diego, CA, USA, May 2015, pp. 1–14. [45] B. Singh, M. Najibi, and L. S. Davis, “SNIPER: Efﬁcient multi-scale


training,” in Proc. Adv. Neural Inf. Process. Syst., Montréal, QC, Canada, Dec. 2018, pp. 9333–9343. [46] C. Termritthikun, Y. Jamtsho, J. Ieamsaard, P. Muneesawang, and I. Lee,


“EEEA-Net: An early exit evolutionary neural architecture search,” Eng. Appl. Artif. Intell., vol. 104, Sep. 2021, Art. no. 104397, doi: 10.1016/j.engappai.2021.104397. [47] Z. Tian, C. Shen, H. Chen, and T. He, “FCOS: Fully convolutional


one-stage object detection,” in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 9626–9635. [48] X. Wang, R. Girshick, A. Gupta, and K. He, “Non-local neural


networks,” in Proc. IEEE Int. Conf. Comput. Vis., Jun. 2018, pp. 7794–7803. [49] S. Xie, R. Girshick, P. Dollar, Z. Tu, and K. He, “Aggregated residual


transformations for deep neural networks,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2017, pp. 5987–5995. [50] M. Yang, K. Yu, C. Zhang, Z. Li, and K. Yang, “DenseASPP for


semantic segmentation in street scenes,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Salt Lake City, UT, USA, Jun. 2018, pp. 3684–3692. [51] W. Yue, Z. Wang, J. Zhang, and X. Liu, “An overview of recommen


dation techniques and their applications in healthcare,” IEEE/CAA J. Automatica Sinica, vol. 8, no. 4, pp. 701–717, Apr. 2021. [52] H. Zhang, M. Cisse, Y. N. Dauphin, and D. Lopez-Paz, “Mixup: Beyond


empirical risk minimization,” 2017, arXiv:1710.09412. [53] S. Zhang, L. Wen, X. Bian, Z. Lei, and S. Z. Li, “Single-shot reﬁnement


neural network for object detection,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2018, pp. 4203–4212. [54] X. Zhu, H. Hu, S. Lin, and J. Dai, “Deformable ConvNets v2: More


deformable, better results,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2019, pp. 9300–9308. [55] X. Zhu, W. Su, L. Lu, B. Li, X. Wang, and J. Dai, “Deformable DETR:


Deformable transformers for end-to-end object detection,” in Proc. 9th Int. Conf. Learn. Represent. (ICLR), Vienna, Austria, May 2021. [56] P. Zhu et al., “Detection and tracking meet drones challenge,” IEEE


Trans. Pattern Anal. Mach. Intell., early access, Oct. 14, 2021, doi: 10.1109/TPAMI.2021.3119563. [57] Z. Zheng, P. Wang, W. Liu, J. Li, R. Ye, and D. Ren, “Distance-IoU


loss: Faster and better learning for bounding box regression,” in Proc. AAAI Conf. Artif. Intell., Feb. 2020, pp. 12993–13000. [58] L. Zou, Z. Wang, J. Hu, Y. Liu, and X. Liu, “Communication-protocol


based analysis and synthesis of networked systems: Progress, prospects and challenges,” Int. J. Syst. Sci., vol. 52, no. 14, pp. 3013–3034, Oct. 2021.


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.


<!-- Page 14 -->


## 3507014 IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022


Nianyin Zeng was born in Fujian, China, in 1986. He received the B.Eng. degree in electrical engineering and automation and the Ph.D. degree in electrical engineering from Fuzhou University, Fuzhou, China, in 2008 and 2013, respectively.


From October 2012 to March 2013, he was an RA with the Department of Electrical and Electronic Engineering, The University of Hong Kong, Hong Kong. From September 2017 to August 2018, he was an ISEF Fellow founded by the Korea Foundation for Advanced Studies, Seoul, South Korea, and also a Visiting Professor at the Korea Advanced Institute of Science and Technology, Daejeon, South Korea. He is currently an Associate Professor with the Department of Instrumental and Electrical Engineering, Xiamen University, Xiamen, China. He is the author or coauthor of several technical papers and also a very active reviewer for many international journals and conferences. His current research interests include intelligent data analysis, computational intelligence, time-series modeling, and applications.


Dr. Zeng is currently serving as an Associate Editor for Neurocomputing, Evolutionary Intelligence, and Frontiers in Medical Technology, and also an Editorial Board Member of Computers in Biology and Medicine, Biomedical Engineering Online, and Mathematical Problems in Engineering.


Peishu Wu received the bachelor’s degree in measurement and control technology and instrumentation from the Tianjin University of Science and Technology, Tianjin, China, in 2020. He is currently pursuing the master’s degree in measuring and testing technologies and instruments with Xiamen University, Xiamen, China.


His research interests include computer vision and deep learning techniques.


Zidong Wang (Fellow, IEEE) was born in Jiangsu, China, in 1966. He received the B.Sc. degree in mathematics from Suzhou University, Suzhou, China, in 1986, and the M.Sc. degree in applied mathematics and the Ph.D. degree in electrical engineering from the Nanjing University of Science and Technology, Nanjing, China, in 1990 and 1994, respectively.


He is currently a Professor of dynamical systems and computing with the Department of Computer Science, Brunel University London, Uxbridge, U.K. From 1990 to 2002, he held teaching and research appointments in universities in China, Germany, and the U.K. His research interests include dynamical systems, signal processing, bioinformatics, control theory, and applications. He has published more than 600 articles in international journals. He is a holder of the Alexander von Humboldt Research Fellowship of Germany, the JSPS Research Fellowship of Japan, and the William Mong Visiting Research Fellowship of Hong Kong.


Prof. Wang is a member of the Academia Europaea, the European Academy of Sciences and Arts, and the program committee for many international conferences; an Academician of the International Academy for Systems and Cybernetic Sciences; and a fellow of the Royal Statistical Society. He serves (or has served) as the Editor-in-Chief for International Journal of Systems Science, Neurocomputing, and Systems Science & Control Engineering and an Associate Editor for 12 international journals, including IEEE TRANSACTIONS ON AUTOMATIC CONTROL, IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, IEEE TRANSACTIONS ON NEURAL NETWORKS AND LEARNING SYSTEMS, IEEE TRANSACTIONS ON SIGNAL PROCESSING, and IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART C: APPLICATIONS AND REVIEWS.


Han Li received the bachelor’s degree in measurement and control technology and instrumentation from Xiamen University, Xiamen, China, in 2018, where he is currently pursuing the Ph.D. degree in measuring and testing technologies and instruments.


His research interests include intelligent optimization algorithms and deep learning techniques.


Weibo Liu received the B.S. degree in electrical engineering from the Department of Electrical Engineering and Electronics, University of Liverpool, Liverpool, U.K., in 2015, and the Ph.D. degree in computer science from Brunel University London, Uxbridge, U.K., in 2019.


He is currently a Lecturer with the Department of Computer Science, Brunel University London, Uxbridge, U.K. His research interests include big data analysis and deep learning techniques.


Xiaohui Liu received the B.Eng. degree in computing from Hohai University, Nanjing, China, in 1982, and the Ph.D. degree in computer science from Heriot-Watt University, Edinburgh, U.K., in 1988.


He is currently a Professor of computing at Brunel University London, Uxbridge, U.K., where he conducts research in artiﬁcial intelligence and intelligent data analysis, with applications in diverse areas, including biomedicine and engineering.


Authorized licensed use limited to: UCLA Library. Downloaded on November 20,2022 at 17:27:40 UTC from IEEE Xplore.  Restrictions apply.
