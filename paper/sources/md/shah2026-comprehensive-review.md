# shah2026-comprehensive-review


<!-- Page 1 -->


https://www.aimspress.com/journal/aci


Applied Computing and Intelligence


6(1): 1–22.


DOI: 10.3934/aci.2026001


Received: 12 December 2025


Revised: 24 December 2025


Accepted: 26 December 2025


Published: 07 January 2026 Review


A comprehensive review of automatic defect detection in wooden surface inspection


Himat Shah1,∗, Elisa Saarela2, Teemu Korkeakangas2 and Tomi Pitk¨aaho1


1 Robotics and Artiﬁcial Intelligence, Centria University of Applied Sciences, Vierimaantie 7, 84100 Ylivieska, Finland


2 Industrial Wood, Centria University of Applied Sciences, Joutsentie 11, 84100 Ylivieska, Finland * Correspondence: Email: himat.shah@centria.ﬁ.


Academic Editor: Chih-Cheng Hung


Abstract: This review focused on automated detection and classiﬁcation of wood surface defects, such as knots, cracks, and resin pockets. Machine learning and deep learning methods are increasingly replacing traditional inspection techniques, such as manual checks and imaging tools like X-rays and ultrasound. However, these conventional approaches suﬀer from signiﬁcant limitations in accuracy and eﬃciency. We reviewed both single-stage models, such as you only look once (YOLO) and its variants, and two-stage models like faster region-based convolutional neural networks (R-CNN), and examined their strengths, limitations, and relevance in real industrial applications. We further investigated emerging zero-shot learning approaches that use vision-language models and NLP techniques to detect previously unseen wood defects. Zero-shot models do not rely on annotated training data. These methods oﬀer scalable and ﬂexible solutions, especially in scenarios where collecting labelled samples for all defect types is impractical. The paper also discussed publicly available labelled datasets used to train and test these models, and discussed standard performance metrics such as precision, recall, and mean average precision. This review aimed to support further research and practical improvements in automated wood surface quality assessment by analyzing defect types, detection methods, and evaluation techniques.


Keywords: wood defect detection; deep learning; machine learning; YOLO model; single-stage model; two-stage model


## 1. Introduction


Detecting wood surface defects is critical to the wood industry. When defects like knots and cracks are identiﬁed early, we produce better wood products that are more valuable. Defect detection is a vital


<!-- Page 2 -->


2


process in wood processing, as defects such as knots, cracks, stains, and resin pockets can signiﬁcantly impact the quality, usability, and market value of wood products [1].


Visual quality inspections are still primarily carried out by trained personnel in the wood processing industry [2]. Traditionally, wood-based industries rely on manual inspections or conventional methods like ultrasonic and X-ray imaging to identify defects [3]. Manual wood inspection methods are error-prone and require high labour costs [4]. Moreover, these methods face challenges such as low eﬃciency, scalability, and limited accuracy. Consequently, manual inspection is unsuitable for modern, high-speed industrial process environments [5].


In recent years, deep learning has substantially improved the accuracy and robustness of object detection, enabling new opportunities to automate defect detection in wood processing [6]. Unlike traditional methods, deep learning oﬀers enhanced eﬃciency, scalability, and accuracy, addressing the limitations of manual inspection. Deep learning methods, particularly convolutional neural networks (CNNs), excel at analyzing image data to identify and classify objects, including various types of wood surface defects.


Among these methods, object detection models like YOLO (you only look once) [7], and faster RCNN [8] models have gained attention for their ability to combine high accuracy with speed, making them suitable for real-time industrial applications. Some methods even use zero-shot NLP [9], enabling the detection of defects without prior examples.


Zero-shot learning using NLP has recently emerged as a promising approach for defect detection, as it does not require large amounts of annotated training data. Zero-shot methods can recognize previously unseen defects by leveraging textual descriptions rather than labelled examples. This capability is enabled by vision-language models such as contrastive language-image pre-training (CLIP), which learn a shared embedding space by aligning image features with corresponding text descriptions. As a result, a model can identify defects such as a “small resin crack” even if no labelled training images for that speciﬁc defect type are available. This approach is particularly advantageous in industrial settings where collecting labelled data for all possible defect categories is impractical or costly.


This survey aims to provide a comprehensive overview of the current research landscape in wood defect detection. Speciﬁcally, we focus on:


• Categorizing state-of-the-art deep learning methods into single-stage and two-stage object detection algorithms. • Reviewing key models, including YOLO and its variants, and two-stage methods like faster RCNN. • A new way of ﬁnding wood defects in research, zero-shot NLP and vision-language models for ﬂexible and scalable defect detection. • Analyzing the datasets commonly used for wood defect detection, highlighting their strengths, limitations, and relevance to real-world scenarios. • Exploring evaluation metrics, such as mean average precision (mAP), precision, recall, and frames per second (FPS), to assess model performance.


Regardless of the many studies on wood defect detection using deep learning, existing reviews often focus on either traditional methods or practical applications and limitations within industrial settings. They primarily evaluate models based on accuracy, computational cost, and suitability for deployment.


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 3 -->


3


This review paper bridges that gap by systematically analyzing both established and new detection methods. It compares single-stage and two-stage deep learning models, including emerging zero-shot learning approaches from NLP.


Furthermore, this paper provides a detailed comparative analysis of key models like YOLO variants and faster R-CNN, also discusses their performance, data needs, and how well they scale for realworld use. It also highlights the limitations of current datasets and suggests future research directions for scalable, real-time industrial applications.


The structure of the paper is as follows: Section 2 provides detail about traditional wood surface defects, including common types and defect categories. Section 3 reviews both manual and automated wood inspection methods along with their limitations. Section 4 discusses machine learning and deep learning approaches, focusing on single-stage, two-stage, and zero-shot NLP models. Section 5 analyzes diﬀerent types of model evaluation metrics used in wood defect detection. Finally, Section 6 concludes the paper with a summary of key ﬁndings and recommendations.


## 2. Wood surface problems


This section builds on the introduction by exploring common wood surface problems in more detail. Various defects negatively impact the quality and usability of wood surfaces. The most common wood defects include knots, cracks, resin exudation, and surface damage, each with distinct causes and implications. Understanding these defects is crucial for eﬀective wood processing and maintaining product quality. We discuss these issues in Subsection 2.1, which are key aspects of common wood surface problems.


## 2.1. Defect categories


Wood defects appear in many forms, including knots (live, dead, cracked, or missing) [10–12], cracks and discolouration [13], insect damage [13], mineral inclusions such as quartzite [11], overgrowth [11], resin pockets [12], marrow [10], and blue stains [11].


Diﬀerent types of wood defects require diﬀerent levels of processing. Table 1 describes the datasets used and the types of faults shown in the images. It also shows how many images were used for classiﬁcation or model training. Table 2 categorizes the defect types according to common characteristics.


Table 1. Speciﬁcations of wood defect datasets used in recent research studies with extended metadata. Dataset Defect Image


count


Tree species Image resolution Setting


## 4000 Spruce, Pine 1024×768; RGB camera


## F1000


Live knot, dead knot,


research [14]


crack, resin, marrow


Laboratory


under controlled lighting


Knot, dead knot, crack 9000 Mixed hardwood 1280×720; Line-scan


Industrial


panel [15]


Custom


Live knot, resin pocket,


Industrial


camera on production line


1920×1080; DSLR under


## 3600 Radiata Pine,


lumber [3]


knot with crack


Laboratory


Eucalyptus


natural light


## 4588 Pine, Birch 1280×960; RGB camera


Mixed species


Knot, crack, resin,


[11]


overgrowth, blue stain


Industrial


with variable lighting


## 4350 Toon, Pine 1024×768; Controlled


## WLSD


Small cracks, knots,


## YOLO [10]


resin


Laboratory


lighting


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 4 -->


4


Table 2. Classiﬁcation of wood defects and corresponding references.


Defect References Defect References knot [16] live knot [3,10–13] dead knot [3,10–13] knot with crack [3,10–13] knot missing [10–13] marrow [3,10–13] crack [3,10–13] resin [3,11–13] overgrown [11] blue stain [11] discolouration [13] insect damage [13] quartzite [11]


## 2.2. Knot family


Knots are common and critical defects on wood surfaces that signiﬁcantly reduce mechanical strength and increase the risk of cracking or failure near the aﬀected area [17]. Additionally, their hardness complicates cutting and sanding processes.


In many cases, especially for high-grade lumber or wood used for decorative purposes, knots are viewed as imperfections that diminish visual quality. The knot family includes several types, such as live knots, dead knots, and knots with cracks. Recent research [18] shows that the YOLOv5 detector eﬀectively identiﬁes knot defects. As shown in Figure 1, various types of knot defects appear on wood surfaces. However, the eﬀects of knots on bending strength are not fully understood [19].


Live knots [20] are areas in wood where the knot remains connected to the tree. Because the wood ﬁbres remain intact and actively grow, these knots are typically more solid and dense compared to dead knots. Consequently, live knots can signiﬁcantly aﬀect the physical and mechanical properties of the wood, as well as its aesthetic characteristics. The live knot is shown in Figure 1.


Live knots exhibit lower density compared to dead knots but are denser than clear wood, and thus aﬀects overall wood strength. Live knots appear in softwood and hardwood species; they vary in size and contribute to the wood’s distinct character and aesthetic appeal. However, they can also introduce speciﬁc challenges and require careful consideration during woodworking and processing.


Dead knots, in contrast, are sections of wood where branches were once attached to the tree but have since died and become separated from it. This is a characteristic that distinguishes them from live knots, where the branch is still connected. Over time, the wood ﬁbres in dead knots may deteriorate or break away, leaving empty spaces or holes behind. Figure 1 shows a dead knot on the wood surface.


These gaps can be ﬁlled with resin or other materials during processing to enhance the wood’s look and structural integrity. Because dead knots are often seen in reclaimed or salvaged wood, processors will often ﬁll them in in some types of softwood.


Knots with a crack are another issue found on the wood surface. Cracked knots are a visible issue in wood, as shown in Figure 1. Knots create stress, which changes how we predict wood failure by up to 23% [21]. Cracks form around knots because of tension and shear failures. Understanding these failures helps us understand how wood breaks [22]. Figure 1, illustrate knots with cracks and missing knots, respectively.


Wood surface defects include missing knots, which may aﬀect the aesthetic appeal of the surface. If a knot falls out and is lost, glue may be used for the remaining knots, and missing knots can be ﬁlled


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 5 -->


5


with epoxy [14].


knot on wood surface live knot dead knot


knot with crack knot missing resin on wood surface


Figure 1. Examples of typical wood surface defects.


## 2.3. Resin


Resin is another signiﬁcant defect found on wood surfaces. It refers to wood that holds an uncommonly high amount of resin, making it darker than normal wood material. To understand how much extra resin is in a piece of wood, we look at its surface. We then ﬁgure out what percentage of that total surface area shows this resin. Figure 1 illustrates a resin defect on the wood surface.


For example, if resin covers a quarter of the surface, we say it has 25% resin. Sometimes, one ﬁnd a long, narrow space, like a small channel, inside the wood. This space usually appears between two of the tree’s growth rings (the circles you see on a tree stump). This space is a resin pocket, and it often ﬁlls up with resin. We measure the length of the resin pocket in millimetres along the length of the wood piece where the pocket appears.


## 2.4. Cracks and their types


Drying cracks refers to cracks that form in wood when drying causes internal stresses. These cracks can appear straight or at an angle, depending on the wood’s grain structure. Typically, the length of a drying crack is proportional to its depth and width.


Heart cracks are radial cracks that start from the tree’s centre, caused by stresses inside the heartwood. The measurement and classiﬁcation of heart cracks follow similar methods to those used


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 6 -->


6


for drying cracks.


Ring cracks appear as ﬁssures that follow the tree’s growth rings, especially in freshly cut wood. These cracks are measured and classiﬁed similarly to drying cracks, using methods that assess their length relative to the total timber size and their impact on the piece’s overall quality. For example, longer or more numerous cracks can signiﬁcantly reduce the timber’s grade. These assessments are crucial for determining the suitability of the wood for diﬀerent applications.


Measurement of crack length is the length of each crack expressed as a percentage of the total length of the timber piece. In assessing the wood’s quality grade, the total length of any crack, or consecutive cracks, is expressed as a percentage of the piece’s total length. Cracks shorter than 100 millimetres are generally excluded from this assessment. When adjacent parallel drying cracks, or cracks angled towards the piece’s edge, are observed, the quality grade is based on the length of the cracked part or the combined length of all cracks.


## 2.5. Wane


Wane is another type of wood surface defect. Unlike other defects, such as knots, cracks, or resin pockets, wane refers to the portion of a sawn wood surface that remains uncut by the saw, retaining some of the tree’s original, rounded surface. Its length and depth are expressed as a percentage of the wood’s nominal size, while its width is measured in millimetres.


## 3. Wood inspection methods


In this section, we explain how people typically identify these wood problems, either by inspecting them directly or by using machines. Identifying these problems correctly helps maintain high quality. We now examine the two primary inspection approaches: manual and automatic inspection. We discuss the advantages and limitations of these techniques below.


Manual inspection has historically been used to detect issues like knots, cracks, and resin pockets (see Section 2). Manual inspection commonly involves trained personnel visually examining wood for quality, similar to how construction workers inspect lumber on site [3]. This method depends on experts’ judgment to decide if the wood meets quality standards [13]. It is inexpensive and simple. However, it lacks the accuracy and eﬃciency required for modern automated production.


Automatic inspection replaces manual labour with machines to detect surface and internal defects. Technologies such as ultrasonic testing, X-ray imaging, and acoustic emission are commonly applied in industrial settings. These techniques enhance repeatability and minimize human error when assessing defects such as internal cracks, resin pockets, and stress-related ﬂaws. However, while these methods provide better consistency than manual inspection, they still face limitations in scalability and versatility.


The emergence of data-driven techniques, such as machine learning and deep learning, builds upon these methods to oﬀer even higher accuracy and adaptability, topics discussed in detail in Section 4. Table 3 compares manual and automatic inspection methods.


Ultrasonic testing, X-ray imaging, and acoustic emission are common automatic inspection methods. We describe each in detail below.


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 7 -->


7


Table 3. Comparison of manual and automatic wood inspection methods.


Criterion Manual inspection Automatic inspection Automation suitability Not suitable for automation Suitable for automation Cost Low initial cost High initial investment Operational eﬃciency Low; slow and laborintensive


High; fast and scalable


Consistency Subjective; depends on operator experience


High repeatability and consistency Accuracy Limited, especially for subtle defects


High, particularly with advanced sensors Industrial scalability Poor Well suited for industrial production lines


## 3.1. Ultrasonic methods


Ultrasonic methods use high-frequency sound waves to identify internal ﬂaws in wood. A device transmits these waves into the wood; internal defects cause the waves to reﬂect or attenuate (weaken). The system detects and locates discontinuities by analyzing changes in the returning or passing sound waves. Ultrasonic methods have been widely studied for internal defect detection [23, 24]. Although eﬀective, these methods require good acoustic coupling (e.g., a strong transmission interface between the sensor and material). This often requires a liquid or gel couplant to transmit waves between the sensor and the wood, making the method less practical for some situations.


## 3.2. X-ray methods


X-ray detection analyzes the attenuation to detect internal defects with high accuracy. X-ray imaging provides high accuracy but raises safety concerns due to harmful radiation exposure [25,26]. These limitations restrict its widespread use in industrial environments.


## 3.3. Acoustic emission methods


Acoustic emission methods detect defects by capturing transient elastic waves caused by sudden stress in wood. This technique works well for identifying structural defects but cannot detect nonstructural issues. Acoustic emission methods detect transient elastic waves eﬃciently and have been applied in wood quality assessment [27, 28]. Although other methods exist, they often face similar challenges, such as complexity, limited scalability, or operational constraints. These issues make them less practical for industrial applications.


## 3.4. Limitations of methods


Manual and automatic inspection methods help identify wood defects, but both approaches face signiﬁcant limitations in industrial applications. Manual methods rely on human judgment and are not suitable for large-scale operations, while automatic techniques, though more precise, still encounter technical and operational challenges. Table 4 summarizes the advantages and limitations of these methods, highlighting their practical strengths and shortcomings.


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 8 -->


8


Table 4. Comparison of detection techniques for wood defects: advantages and disadvantages.


Manual methods Technique Advantages Disadvantages Manual detection Simple and inexpensive method


Highly ineﬃcient and arbitrary; not suitable for automation; ineﬃcient for industrial-scale operations Automatic methods Ultrasonic methods


Eﬀective at detecting internal defects; non-invasive


Requires a transmission medium; limited ﬂexibility; dependence on coupling medium reduces adaptability in diﬀerent environments X-ray methods High accuracy in detecting internal defects


Exposure to harmful radiation; safety concerns; health risks limit prolonged or widespread use Acoustic emission


Detects transient elastic waves due to wood deformation; non-invasive and eﬃcient


Can not detect non-structural defects; limited to certain defect types; restricted applicability due to inability to detect non-structural defects Other methods May oﬀer tailored alternatives


Often require complex setups; face similar challenges as above methods; lack adaptability and scalability for broad industrial adoption


Ultrasonic and X-ray methods detect defects well but face issues such as the need for a transmission medium or safety concerns. Acoustic emission detects structural defects eﬃciently, but cannot identify non-structural issues. These challenges show the need for better methods that improve adaptability, scalability, and safety. Table 5 shows the advantages and limitations of diﬀerent inspection methods. This overview highlights key challenges and opportunities, setting the stage for exploring advanced methods like deep learning, machine learning, and computer vision in the subsequent discussion.


Recent advances in computer-based methods are improving how we detect wood defects. A critical application of these technologies is object detection, which combines machine learning with computer vision to identify and classify objects in images. In wood defect detection, these deep learning approaches transform traditional methods by enabling automated, fast, and accurate defect identiﬁcation. Two primary types of algorithms drive this transformation: single-stage and two-stage object detection models.


Single-stage algorithms, such as YOLO, prioritize speed by performing object localization and classiﬁcation simultaneously, making them well-suited for real-time applications. In contrast, twostage algorithms, such as faster R-CNN, ﬁrst generate region proposals and then classify the detected regions, oﬀering superior accuracy at the cost of reduced processing speed. These deep learning approaches form a foundation to solve complex defect detection challenges, balancing eﬃciency and precision in industrial environments.


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 9 -->


9


Table 5. Qualitative comparison of wood inspection methods.


Method Eﬃciency Adaptability Key strengths Main limitations


Manual inspection Low High Flexible judgment; minimal


Subjective; inconsistent;


equipment; handles rare cases


slow; high labor demand; not


scalable


Requires good sensor contact;


Ultrasonic testing High Medium Internal defect sensing;


sensitive to wood grain;


non-destructive; repeatable;


limited for surface-only


suitable for many internal


defects


ﬂaws


Radiation safety and


X-ray imaging High Low medium High-resolution internal


shielding; high cost;


visualization; strong


operational constraints


performance for hidden


defects


Other methods Medium Low medium Useful for speciﬁc defect


Setup-dependent; limited


mechanisms; complements


defect coverage; integration


other sensors


complexity


## 4. Machine learning and deep learning methods


Following our examination of inspection methods, this section now looks at deep learning-based object detection methods. We will explore how these methods are categorized into one-stage and two-stage algorithms and examine what makes them useful, where they excel, and their potential drawbacks. The key diﬀerences between the one-stage and two-stage models are their operational eﬃciency and accuracy.


One-stage models, like YOLOv8, are designed for end-to-end detection, allowing faster processing times. This speed is vital in industrial applications where rapid decision-making is essential [15]. These models have been successfully used to identify various wood defects, such as colour variations, bug eyes, cracks, knots, and scars [15].


## 4.1. One-stage object detection methods


One-stage object detection methods perform classiﬁcation and localisation in a single step, making them faster and more suitable for real-time applications. YOLO is one such model known for its speed and eﬃciency. Other examples of one-stage detection models include single shot detector (SSD) and RetinaNet. These models are particularly useful in applications like wood defect detection, where rapid processing is essential. In this survey, we only focus on YOLO-based models, and we discuss this as follows.


## 4.1.1. Overview of YOLO-based models


SiM-YOLO [13] method enhances the YOLOv8 algorithm for wood surface defect detection through several innovative modiﬁcations aimed at improving accuracy and eﬃciency. During the training, 3600 images of seven types of wood defects were used (for more details, see Table 1).


SiM-YOLO method improves defect classiﬁcation accuracy using several key components that


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 10 -->


10


enhance feature extraction, feature fusion, localisation, and loss optimisation. It begins with a custom feature extraction module called SPD-Conv, which preserves ﬁne-grained defect details. This module captures subtle variations and complex patterns on wood surfaces, reducing the loss of important features within and across defect types.


SiM-YOLO method also includes a scale-invariant attention fusion feature-path aggregation network (SiAFF-PANet) feature fusion module to address scale and semantic diﬀerences between defect types. It merges features from multiple levels while maintaining semantic consistency. As a result, the model better understands local context better and pinpoints defect locations more accurately.


The model integrates a multi-attention detection head (MADH) that focuses on cross-channel interactions and sharp spatial details. This design helps the model detect overlapping defects and clearly separate their boundaries, improving classiﬁcation and localisation.


To improve localization, SiM-YOLO replaces the standard complete intersection over union (CIOU) loss with the minimum point distance intersection over union (MPDIOU) loss. This modiﬁcation reduces distorted bounding boxes under strong overlap, improving boundary separation and localization accuracy.


Tests show that SiM-YOLO outperforms earlier models, achieving a 9.3% increase in mean average precision (mAP) over YOLOX model and a 4.3% increase over YOLOv8, conﬁrming its eﬀectiveness in wood surface defect detection.


SiM-YOLO method combines advanced feature extraction, eﬀective fusion, focused attention, and optimized loss design to detect wood defects with high precision. However, it still faces challenges such as reliance on high-quality datasets, increased computational demands, and the need for ﬁnetuning in real-time applications. Future research should address these limitations to support wider industrial use.


FRCE-YOLO [11] method is a lightweight model based on YOLOv8 that improves the detection of wood surface defects. It increases mAP@0.5 by 6.9%, reaching 80.7%, and boosts mAP@0.5:0.95 by 8.4%, while reducing computational complexity by 1.2 GFLOPs. The model targets ten distinct defect types, including live knots, dead knots, quartzite, knots with cracks, missing knots, cracks, overgrowth, resin, marrow, and stains (see Table 1). Its lightweight structure and ability to manage noisy or inconsistent data make it a practical choice for industrial use.


Several architectural improvements enhance the model’s eﬃciency. The C2f-fast module, a lightweight variant of the C2f block, simpliﬁes the YOLOv8 backbone by reducing network complexity without sacriﬁcing accuracy. The RG-C2f module further improves feature extraction by replacing computationally expensive operations with more eﬃcient alternatives. The convolutional block attention module (CBAM) directs the network’s focus toward defect-relevant spatial and channel features, while the eﬃcient intersection over union (EIOU) loss improves localization accuracy for defects with varying shapes and sizes. Together, these modiﬁcations make FRCE-YOLO eﬀective for identifying a wide range of defects under challenging conditions.


The model is evaluated on a specialized dataset designed for wood defect detection and demonstrates faster and more accurate performance than YOLOv8. The dataset includes defects of varying sizes, orientations, and lighting conditions, reﬂecting realistic industrial scenarios. Table 2 summarizes the defect categories included in the dataset. FRCE-YOLO also uses standard evaluation metrics such as precision, recall, mAP, and F1-score to validate its performance (Table 6). These results conﬁrm its eﬀectiveness for quality control in industrial environments with limited computational


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 11 -->


11


resources.


Table 6. Evaluation metrics used in wood defect detection and corresponding references.


Metric(s) References Precision [3,10–13,29–32] Recall [3,10–13,29–32] F1-score [10,11,29–32] Mean average precision (mAP) [3,10–13] Parameters, GFLOPs [11]


Although FRCE-YOLO performs well for wood surface defects, its eﬀectiveness in other industries remains untested. The model may also require further optimisation for use on low-power hardware. Despite these limitations, it oﬀers a strong balance of accuracy, eﬃciency, and practicality, making it a valuable tool for automated wood processing.


The WLSD-YOLO [10] model presents a novel approach to detecting surface defects in wood lumber. The model integrates a squeeze-and-excitation (SE) attention mechanism, a GVC-neck layer structure, and advanced loss functions to improve the detection accuracy of small wood defects. The experimental results show that the WLSD-YOLO model achieves a recognition accuracy of 76.5%, outperforms the YOLOv8 model in mean average precision (mAP) by 2.9%, and enhances processing. YOLO brought accuracy, eﬃciency, and speed at stage one, which were diﬃcult and complex issues earlier.


CWB-YOLOv8 [3] improves wood defect detection by enhancing the YOLOv8 algorithm with three key modules: conditional parametric convolution (CondConv), Wise-IoU, and BiFormer. The model dynamically adjusts convolution kernel weights with CondConv to better identify complex defect features. BiFormer, a multi-scale attention mechanism, enhances the model’s ability to detect both small and large defects. Wise-IoU replaces the standard loss function, improving anchor box quality and handling low- and medium-quality samples eﬀectively.


The authors created a custom dataset of 6134 images, including defects from diverse tree species like radiata pine, eucalyptus, and toon trees. They addressed the scarcity of rare defect types, such as cracks and resin, through data augmentation. This dataset provides a strong foundation for training and testing the improved model.


CWB-YOLOv8 outperforms standard YOLOv8, achieving a 3.5% improvement in mAP@0.5 and a 5.8% improvement in mAP@0.5:0.95. It also detects challenging defect types like cracks and resin with high accuracy (96% and 93%, respectively). These enhancements make CWB-YOLOv8 a reliable and eﬃcient solution for wood defect detection in industrial applications.


By addressing limitations of traditional methods and improving upon other YOLO-based models, CWB-YOLOv8 oﬀers a practical approach for real-time wood processing. Its integration with other advances in one-stage object detection, such as SiM-YOLO and FRCE-YOLO, highlights the growing potential of automated defect detection systems in the timber industry.


R. Wang et al. [33] used a model that enhances the YOLOv7 algorithm by incorporating dynamic convolution and a full-dimensional dynamic coordinate attention mechanism to improve wood defect detection in a public dataset. However, these enhancements render the algorithm unsuitable for deployment on edge devices [34].


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 12 -->


12


## 4.1.2. Limitations of YOLO-based models


The YOLO model has several limitations in accurately detecting and classifying wood surface defects such as knots, cracks, resin, and marrow. Researchers frequently highlight these challenges in multiple studies [22, 34]. One key challenge is the model’s struggle to identify rare or complex defects, like cracks and resin, since these appear less frequently in datasets than knots [14]. YOLO can produce false positives (identifying a defect where there isn’t one) and false negatives (missing a defect that is there). This could lead to inaccurate defect detection.


The performance of the YOLO model is likely dependent on the quality and diversity of the dataset used for training. If the dataset does not encompass a wide range of defect types or real-world scenarios, the model may struggle to generalize eﬀectively to unseen data. This limitation is common in machine learning models, where the training data signiﬁcantly inﬂuences the model’s performance. Additionally, if the model is trained on a speciﬁc type of wood or speciﬁc types of defects, it might not generalize well to other types of wood or defects.


## 4.2. Two-stage object detection methods


Two-stage object detection algorithms divide the detection process into two steps: region proposal generation and classiﬁcation with bounding box reﬁnement. Faster R-CNN is the most widely used two-stage model in wood defect detection [8]. These models typically use datasets with over 5,000 annotated images covering defects such as knots, cracks, resin pockets, and stains. Reported mean average precision (mAP), values range from 85% to 90%, with GFLOPs between 25 and 40, depending on the backbone network [5, 27, 28]. faster R-CNN achieves high accuracy for small and irregular defects but requires signiﬁcant computational resources, making real-time deployment challenging. Table 7 summarizes the performance of faster R-CNN and its variants compared to YOLO-based models.


Table 7. Comparative analysis of object detection models for wood defect detection.


Model Architecture Data requirements mAP% GFLOPs YOLOv8 One-stage (Single-shot) 3600 img,7 defects 76.0 2.5 SiM-YOLO One-stage (Improved YOLO) 3600 img, 7 defects 85.0 3.1 FRCE-YOLO One-stage (YOLOv8-based) 6134 img,10 defects 80.7 1.2 WLSD-YOLO One-stage (YOLO-based) 2000 img, 5 defects 76.5 1.8 Faster R-CNN Two-stage (Region Proposal Network)


5000 img, 7 defects 85.0 25.0


Faster R + ResNet (Region Proposal Network) + ResNet


5000 img, 7 defects 87.0 40.0


## 4.2.1. Faster R-CNN: Limitations and advantages


Faster R-CNN is one of the most widely used two-stage detection models [8]. It introduces a region proposal network (RPN) that streamlines the generation of region proposals, signiﬁcantly improving speed and eﬃciency over earlier R-CNN models.


The model achieves high accuracy for detecting wood defects, particularly those with intricate


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 13 -->


13


patterns such as ﬁne cracks or resin pockets [35]. Despite these strengths, faster R-CNN faces notable limitations. Its slower processing speed restricts real-time applications in industrial settings [10].


The model relies on rectangular bounding boxes, which poorly capture irregular defect shapes like elongated cracks or resin pockets. It is also sensitive to anchor box conﬁgurations and may struggle with very small or low-contrast defects unless enhanced with modules such as feature pyramid networks (FPN). Furthermore, variations in wood species, grain, lighting, and moisture can aﬀect robustness, and extensive expert-driven annotation is required for eﬀective training. These challenges are summarized in Table 8.


Table 8. Key limitations of faster R-CNN in wood defect detection with supporting references.


Category Keywords (wood defect context) References Computational cost/speed


[23,24]


two-stage detector; slower inference; realtime limitation; industrial line throughput; hardware/optimisation


rectangular boxes; poor ﬁt for cracks/resin pockets; localization mismatch; motivates segmentation


Irregular shape accuracy


[25,26]


Anchor box sensitivity anchor mismatch; scale/aspect variation; thin cracks; multi-scale tuning; optimisation required


[27,28]


Small/subtle defects pin knots; ﬁne cracks; low contrast; complex grain; FPN/feature enhancement


[4,27]


species variation; grain/moisture/lighting; domain shift; augmentation; generalization challenge


Appearance variability


[36,37]


Data annotation burden


large labeled datasets; expert bounding boxes; time/cost; scalability barrier


[26,29]


However, faster R-CNN oﬀers clear advantages through its two-stage reﬁnement mechanism. The RPN ﬁrst generates candidate regions, and the second stage reﬁnes these proposals for classiﬁcation and bounding box adjustment. This process enables precise detection of small, low-contrast, and irregular defects, even under challenging conditions such as complex wood grain or subtle resin spots.


These strengths make faster R-CNN ideal for applications where accuracy matters more than speed. In high-value, low-throughput production environments—such as custom wood product manufacturing or premium lumber processing—every defect can signiﬁcantly impact quality and value. In such cases, the ability to detect subtle defects accurately outweighs the cost of slower processing. While faster R-CNN is not the best choice for fast-paced, mass-production settings, its precision and reﬁnement capabilities make it indispensable for tasks that prioritize detection accuracy over real-time performance.


## 4.2.2. Backbone networks for feature extraction


The backbone network in a two-stage detector, like faster R-CNN, is responsible for extracting meaningful visual features from input images. The choice of backbone signiﬁcantly aﬀects the model’s performance in terms of both accuracy and computational eﬃciency.


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 14 -->


14


MobileNetV3 [38] is a lightweight network optimized for real-time applications. It uses advanced techniques such as squeeze-and-excitation modules and network search to balance accuracy and speed, making it suitable for deployment on edge devices. However, due to its compact architecture, it may struggle to capture highly detailed or subtle wood defect patterns [39].


Visual geometry group 16-layer network (VGG16) and visual geometry group 19-layer network (VGG19) are well-known for their simplicity and uniform architecture, consisting of sequential 3x3 convolutional layers. These deep networks provide strong hierarchical feature extraction, which is beneﬁcial for capturing complex defect structures. Their main limitation lies in their high computational and memory requirements [16].


ResNet introduces residual connections that eﬀectively address the vanishing gradient problem in deep networks. This allows for the training of very deep architectures, enabling improved performance in detecting complex and varied defect types. Despite its beneﬁts, ResNet comes with added model complexity and increased training time [40].


GoogLeNet utilizes Inception modules, which enable multi-scale feature extraction within a single architecture. This design oﬀers a good balance between accuracy and computational eﬃciency, making it suitable for defect detection tasks requiring both speed and precision. Nevertheless, the model’s internal complexity can make it more diﬃcult to implement and tune [41].


AlexNet was one of the ﬁrst deep convolutional networks to gain widespread attention for image classiﬁcation. It is valued for its simplicity and fast inference but lacks the depth and representational power needed for accurately detecting subtle or irregular wood defects [42].


## 4.2.3. Advantages and limitations


Two-stage object detection methods oﬀer high accuracy, especially for small, overlapping, or irregularly shaped defects. They beneﬁt from precise region proposal mechanisms and robust feature extractors, making them suitable for tasks requiring detailed defect classiﬁcation. Additionally, the use of pre-trained backbone networks allows for eﬀective transfer learning across datasets, reducing the need for training from scratch.


However, these strengths come at a cost. Two-stage methods are generally slower and more resource-intensive than one-stage models like YOLO. Their complex architectures can limit real-time performance in industrial environments where speed is critical. The training process also requires substantial annotated data and computing resources, which may be a barrier to adoption for some applications.


## 4.3. Comparative analysis of object detection models for wood defect detection


In this subsection, we provide a comparative analysis of several popular object detection models used for wood defect detection, including YOLO variants and faster R-CNN. The table summarizes key aspects of these models, including their architecture, data requirements, mean average precision (mAP) values, and computational load in giga ﬂoating point operations (GFLOPs).


The Table 7 provides a detailed comparison of various deep learning models commonly used for wood defect detection. These models, including YOLO variants and faster R-CNN, vary in terms of their architecture, data requirements, mAP values, and computational load.


Model: The models listed include both one-stage (e.g., YOLO) and two-stage (e.g., faster R


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 15 -->


15


CNN) architectures. One-stage models like YOLO perform object classiﬁcation and localization simultaneously, making them faster and well-suited for real-time applications. In contrast, two-stage models like faster R-CNN generate region proposals in the ﬁrst stage and classify them in the second stage, which often results in better accuracy at the cost of slower processing.


Architecture: This column describes the type of architecture used. One-stage models like YOLOv8 and its variants are designed for quick inference, which is crucial for industrial applications. Two-stage models like faster R-CNN oﬀer higher accuracy by reﬁning object proposals, but they are generally slower and more computationally intensive.


Data requirements: The data required for training each model varies. YOLO-based models typically require datasets with thousands of images and defect types, while two-stage models like faster R-CNN may require larger and more highly annotated datasets to achieve optimal performance. The variety of wood defects and the need for high-quality annotations signiﬁcantly impact the model’s training process and its generalizability to real-world scenarios.


Mean average precision(mAP): mAP is a standard performance metric used to evaluate the accuracy of object detection models. It combines precision and recall across diﬀerent threshold levels. YOLO-based models, such as YOLOv8, tend to have lower mAP scores (around 76%) but are much faster, making them suitable for real-time applications. In contrast, models like faster R-CNN and its variants (e.g., faster R-CNN with ResNet) generally achieve higher mAP values (up to 90%) but at the cost of increased computational demand.


Computational load (GFLOPs): This column shows the **computational complexity** of each model, measured in giga ﬂoating point operations (GFLOPs). Lower GFLOPs values indicate that the model is less computationally demanding and can perform faster, which is important in industrial environments. YOLO-based models like FRCE-YOLO and WLSD-YOLO have relatively low GFLOPs values, making them more suitable for real-time defect detection on low-power devices. In contrast, two-stage models like faster R-CNN require signiﬁcantly more computational resources due to their more complex architecture, making them less suited for real-time deployment without specialized hardware.


The Table 7 helps highlight the trade-oﬀs between diﬀerent object detection models, enabling a better understanding of their suitability for various industrial applications in wood defect detection. By providing both performance and computational requirements, this comparison serves as a guide for selecting the most appropriate model based on the speciﬁc needs of a given use case.


## 4.4. Zero-shot NLP for wood defect detection


Traditional deep learning models, such as convolutional neural networks (CNN), have been widely used to detect wood defects like knots, cracks, and resin pockets. These models typically require large, labelled datasets to perform well. However, in industrial practice, it is often diﬃcult to collect enough labelled data for every possible defect, especially rare or newly emerging types [43].


Zero-shot learning (ZSL), originally developed in the ﬁeld of NLP, oﬀers a promising solution. It enables models to recognize or classify unseen data based on semantic descriptions, without requiring prior labelled examples. For instance, a zero-shot model can detect a “thin surface crack” in a wood image simply by understanding that phrase, even if no such image was included during training.


Tools like Stanza support multilingual NLP tasks and can help extract wood-speciﬁc terminology such as resin leak or deep knot from technical documents [44]. These tools often rely on transfer


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 16 -->


16


learning and hierarchical modelling techniques, such as Bayesian hierarchical zero-inﬂated models, to handle small, sparse, or imbalanced datasets commonly found in wood processing [45].


In computer vision, models like CLIP link image features to textual descriptions, allowing zero-shot visual recognition of defects using only semantic prompts [46]. This is especially helpful for detecting rare or subtle wood defects when labelled data are unavailable. For example, an image showing “a dark line across the grain” could be correctly identiﬁed by the model even without prior exposure to such examples.


Zero-shot techniques can also support broader industrial and environmental applications. In studies related to air pollutant emissions and material degradation, models trained on general wood data could help identify patterns associated with chemical or structural changes in new contexts [47,48].


In summary, zero-shot learning presents an exciting opportunity to improve wood defect detection depending on large labelled datasets. NLP tools and vision-language models enable ﬂexible and scalable detection of defects such as cracks, knots, and resin marks. As research advances, zero-shot techniques could signiﬁcantly enhance the adaptability and eﬃciency of automated inspection systems in the wood industry.


## 4.4.1. Prompt-guided zero-shot defect detection: case studies


We show how vision–language models (e.g., open-vocabulary detectors) use text prompts to localize and classify wood defects without task-speciﬁc labels. Case 1: Resin pocket (descriptive prompt). Prompt: “a long, narrow resin-ﬁlled channel between growth rings”. Result: The model highlights the resin pocket and suppresses grain texture, even though no resin examples appear in training. Case 2: Hairline crack (semantic guidance). “a thin surface crack running diagonally across the grain”. Result: The model localizes a faint, diagonal crack that supervised baselines miss at standard thresholds. Case 3: Knot type diﬀerentiation (prompt contrast). Prompts: “a live knot with intact ﬁbers” vs. “a dead knot with a hollow center”. Result: The model separates live and dead knots by aligning region features to the prompt semantics. Case 4: Prompt-based QC ﬁltering. Prompt: “exclude boards with missing knots or deep cracks”. Result: The system ﬂags boards for rejection using the prompt as a rule, enabling fast, adjustable grading.


## 5. Performance evaluation of detection models


This section explains how researchers use diﬀerent metrics to evaluate model performance on wood surfaces. Each metric shows something diﬀerent about how the model works, what it handles well, and where it may fail.


## 5.1. Precision


Precision is one of the most widely used metrics, especially for wood surface issues. In Table 6, we provide references that use precision as a metric in wood-related issues. Precision reveals how often


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 17 -->


17


the model’s positive predictions are correct. It tells us the percentage of predicted positives that are true positives.


For example, the model checks 100 wooden boards and predicts that 80 have defects. After manual checking, we ﬁnd that only 60 of those 80 really have defects. So, the precision is 60 divided by 80, or 75%. This means the model is correct 75% of the time when it says a board is defective.


Precision = TP TP + FP. (1)


In Eq (1) above, TP means true positives and FP means false positives.


## 5.2. Recall


Recall measures how many of the real defects the model managed to catch. While precision looks at correct predictions, recall focuses on ﬁnding every true case.


Recall (RCL) = TP TP + FN. (2)


Here, FN means false negatives. Table 6 shows where researchers use recall. For example, a model checks 100 wooden boards, and 80 of them have defects. If the model ﬁnds all 80 defective boards, its recall is 1.0 or 100%. High recall is useful when missing a defect can lead to signiﬁcant issues.


## 5.3. F1-score


F1-score measures how well a model balances ﬁnding all the right things (recall) and not getting confused by too many wrong ones (precision). In the context of wooden surface defect detection, a high F1-score indicates that the model accurately identiﬁes defects while minimizing false positives and false negatives. One advantage of using the F1-score is that it considers both precision and recall, making it more comprehensive [35]. F1-score is measured using the following formula:


F1-score = 2 · Precision · Recall


Precision + Recall . (3)


This is especially useful with imbalanced datasets where defective surfaces are rare. However, the F1-score may not help when comparing models with very diﬀerent precision and recall values, and it can be sensitive to small changes in data or model settings.


## 5.4. Mean average precision (mAP)


Mean average precision (mAP) gives an overview of model performance. It combines precision and recall across diﬀerent classes and thresholds. It checks how many defects the model ﬁnds (recall) and how accurate those predictions are (precision).


The mAP provides a clear overall score and helps to compare models. It shows how the model performs on all defect types. However, mAP struggles with rare defect types, hides details such as false positives, and varies based on settings like overlap thresholds. Equation (4) shows how to calculate mAP.


Z 1


N X


Mean average precision (mAP) = 1


## 0 P(R). (4)


N


i=1


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 18 -->


18


There are two ways to measure mAP: mAP@0.5 and mAP@0.5:0.95. mAP@0.5 accepts predictions with just 50% overlap, which helps catch as many defects as possible. mAP@0.5:0.95 averages overlap from 50% to 95% and provides a more precise picture of model performance.


## 5.4.1. Parameters


Parameters are matrices that represent the conﬁgurable elements of a model. They determine the model’s complexity and capacity. These values are learned from training data and help the model identify defects like knots, cracks, and resin spots.


For example, parameters include the number of layers in a neural network or the learning rate used during training, both of which aﬀect how well the model detects defects.


## 5.5. Giga ﬂoating-point operations (GFLOPs)


GFLOPs quantify the number of ﬂoating-point operations performed during model inference, providing a direct measure of computational complexity. Models with lower GFLOPs generally achieve faster inference and are more appropriate for real-time and mobile deployments.


These operations are especially useful in evaluating performance for models detecting wood surface issues. For example, detecting knots, cracks, and resin pockets requires quick processing of large images for accurate and timely results.


## 6. Conclusions and future directions


This review provides a comprehensive analysis of automated wood surface defect detection methods, focusing on deep learning models such as YOLO variants and faster R-CNN, along with emerging zero-shot NLP approaches. These models demonstrate strong potential for improving accuracy and eﬃciency in industrial applications. However, several challenges remain.


Rare defects such as resin pockets, hairline cracks, and blue stains are among the most diﬃcult to detect due to their low occurrence in datasets, subtle visual patterns, and variability in size and shape. These defects often exhibit low contrast against complex wood grain, making detection harder even for advanced models. Key diﬃculties include dataset imbalance, lighting variations, and generalization to unseen defect types. To address these challenges and advance the ﬁeld, future research should prioritize the following directions: Developing diverse datasets: Current datasets often lack rare defect types and variability in wood species, lighting, and grain patterns. Creating large-scale, annotated datasets that reﬂect real-world conditions will improve model robustness and generalization. Leveraging zero-shot and few-shot learning: These approaches enable detection of previously unseen defects without extensive labeled data, oﬀering scalable solutions for industrial environments where data collection is costly or impractical. Optimizing models for edge deployment: Lightweight architectures and eﬃcient inference strategies are essential for real-time defect detection on low-power devices in high-speed production settings. Integrating traditional and deep learning techniques: Combining ultrasonic testing, X-ray imaging, and deep learning can enhance detection accuracy, particularly for internal or non-visible defects that current vision-based models struggle to identify.


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 19 -->


19


Incorporating explainable AI (XAI): Interpretability will help operators understand model decisions, increasing trust and facilitating adoption in quality control processes.


Although current models achieve high accuracy, computational complexity and real-time deployment remain major challenges. Future research is moving toward several promising strategies: Model compression and knowledge distillation: Techniques such as pruning, quantization, and distillation reduce model size and computational load without sacriﬁcing accuracy, enabling deployment on resource-constrained devices. Multimodal fusion: Combining RGB images with infrared or acoustic data improves robustness under varying lighting and surface conditions. Multimodal approaches leverage complementary information to enhance defect detection precision. Edge computing and adaptive inference: Deploying lightweight models on edge devices and using adaptive inference strategies (e.g., early exit mechanisms) supports real-time quality inspection in highspeed production lines. Dynamic optimization: Future systems may incorporate on-device learning and dynamic model updates to adapt to changing defect patterns and environmental conditions.


By addressing these challenges, future systems can achieve scalable, accurate, and real-time defect detection, making automated inspection practical for modern wood processing industries.


Use of AI tools declaration


The authors declare they have not used Artiﬁcial Intelligence (AI) tools in the creation of this article.


Acknowledgments


This research was funded by the European Union under the Renewing and Competent Finland 2021–2027 programme (Project No. 81414).


Conﬂict of interest


The authors declare no conﬂict of interest.


## References


1. C. ¨Unsalan, Wood surface inspection using structural and conditional statistical features, arXiv: 2407.03630. https://doi.org/10.48550/arXiv.2407.03630 2. M. Mohsin, O. S. Balogun, K. Haataja, P. Toivanen, Real-time defect detection and classiﬁcation on wood surfaces using deep learning, Electronic Imaging, 34 (2022), IPAS-382. https://doi.org/10.2352/EI.2022.34.10.IPAS-382 3. H. An, Z. Liang, M. Qin, Y. Huang, F. Xiong, G. Zeng, Wood defect detection based on the CWBYOLOv8 algorithm, J. Wood Sci., 70 (2024), 26. https://doi.org/10.1186/s10086-024-02139-z 4. H. C. Teo, U. R. Hashim, S. Ahmad, L. Salahuddin, H. C. Ngo, K. Kanchymalay, A review of the automated timber defect identiﬁcation approach, International Journal of Electrical and Computer Engineering, 13 (2023), 2156–2166. https://doi.org/10.11591/ijece.v13i2.pp21562166


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 20 -->


20


5. Z. Yi, L. Luo, Q. Lu, M. Chen, W. Zhu, Y. Zhang, An eﬃcient and accurate surface defect detection method for quality supervision of wood panels, Meas. Sci. Technol., 35 (2024), 055209. https://doi.org/10.1088/1361-6501/ad26c9 6. B. Syla, S. Saleh, W. Hardt, Automated identiﬁcation of wood surface defects based on deep learning, Embedded Selforganising Systems, 10 (2023), 55–61. https://doi.org/10.14464/ess.v10i7.627 7. J. Redmon, S. Divvala, R. Girshick, A. Farhadi, You only look once: uniﬁed, real-time object detection, Proceedings of IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, 779–788. https://doi.org/10.1109/CVPR.2016.91 8. S. Ren, K. He, R. Girshick, J. Sun, Faster R-CNN: towards real-time object detection with region proposal networks, IEEE Trans. Pattern Anal., 39 (2017), 1137–1149. https://doi.org/10.1109/TPAMI.2016.2577031 9. X. Su, Y. Zhang, H. Luo, X. Liu, L. Huang, Mistake notebook learning: selective batch-wise context optimization for in-context learning, arXiv: 2512.11485. https://doi.org/10.48550/arXiv.2512.11485 10. Q. Zhang, L. Liu, Z. Yang, J. Yin, Z. Jing, Wlsd-yolo: a model for detecting surface defects in wood lumber, IEEE Access, 12 (2024), 65088–65098. https://doi.org/10.1109/ACCESS.2024.3395623 11. Y. Guo, W. Cao, Wood surface defect detection using improved deep learning algorithm: FRCEYOLO, Proceedings of 6th International Conference on Electronic Engineering and Informatics (EEI), 2024, 324–328. https://doi.org/10.1109/EEI63073.2024.10696054 12. R. Wang, Y. Chen, F. Liang, B. Wang, X. Mou, G. Zhang, BPN-YOLO: a novel method for wood defect detection based on YOLOv7, Forests, 15 (2024), 1096. https://doi.org/10.3390/f15071096 13. H. Xi, R. Wang, F. Liang, Y. Chen, G. Zhang, B. Wang, SiM-YOLO: a wood surface defect detection method based on the improved YOLOv8, Coatings, 14 (2024), 1001. https://doi.org/10.3390/coatings14081001 14. P. Kodytek, A. Bodz´as, P. Bilik, A large-scale image dataset of wood surface defects for automated vision-based quality control processes, F1000Res., 10 (2022), 581. https://doi.org/10.12688/f1000research.52903.2 15. R. Li, Z. Xu, F. Yang, B. Yang, Defect detection for melamine-impregnated paper decorative particleboard surface based on deep learning, Wood Mater. Sci. Eng., in press. https://doi.org/10.1080/17480272.2024.2428963 16. K. Simonyan, A. Zisserman, Very deep convolutional networks for large-scale image recognition, arXiv: 1409.1556. https://doi.org/10.48550/arXiv.1409.1556 17. S. Koman, S. Feher, J. Abraham, R. Taschner, Eﬀect of knots on the bending strength and the modulus of elasticity of wood, Wood Res., 58 (2013), 617–626. 18. Y. Fang, X. Guo, K. Chen, Z. Zhou, Q. Ye, Accurate and automated detection of surface knots on sawn timbers using YOLO-V5 model, BioResources, 16 (2021), 5390–5406. https://doi.org/10.15376/biores.16.3.5390-5406 19. J. van Blokland, A. Olsson, J. Oscarsson, G. Daniel, S. Adamopoulos, Crack formation, strain distribution and fracture surfaces around knots in thermally modiﬁed timber loaded in static bending, Wood Sci. Technol., 54 (2020), 1001–1028. https://doi.org/10.1007/s00226-020-011905


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 21 -->


21


20. J. Lyu, H. Qu, M. Chen, Inﬂuence of wood knots of chinese weeping cypress on selected physical properties, Forests, 14 (2023), 1148. https://doi.org/10.3390/f14061148 21. P. Guindos, Comparison of diﬀerent failure approaches in knotty wood, Drewno, 57 (2014), 51– 68. https://doi.org/10.12841/wood.1644-3985.065.03 22. R. Jockwer, E. Serrano, P. J. Gustafsson, R. Steiger, Impact of knots on the fracture propagating along grain in timber beams, Int. Wood Prod. J., 8 (2017), 39–44. https://doi.org/10.1080/20426445.2016.1275093 23. A. Senalik, G. Schueneman, R. Ross, Ultrasonic-based nondestructive evaluation methods for wood: a primer and historical review, FPL-GTR-235, 2014. https://doi.org/10.2737/FPL-GTR235 24. N. Pahnabi, T. Schumacher, A. Sinha, Imaging of structural timber based on in situ radar and ultrasonic wave measurements: a review of the state-of-the-art, Sensors, 24 (2024), 2901. https://doi.org/10.3390/s24092901 25. M. Zieli´nska, M. Rucka, Assessment of wooden beams from historical buildings using ultrasonic transmission tomography, Int. J. Archit. Herit., 17 (2023), 249–261. https://doi.org/10.1080/15583058.2022.2086505 26. Y. Chen, C. Sun, Z. Ren, B. Na, Review of the current state of application of wood defect recognition technology, BioResources, 18 (2023), 2288–2302. https://doi.org/10.15376/biores.18.1.Chen 27. X. Zou, C. Wu, H. Liu, Z. Yu, X. Kuang, An accurate object detection of wood defects using an improved faster R-CNN model, Wood Mater. Sci. Eng., 20 (2025), 413–419. https://doi.org/10.1080/17480272.2024.2352605 28. A. Urbonas, V. Raudonis, R. Maskeli¯unas, R. Damaˇseviˇcius, Automated identiﬁcation of wood veneer surface defects using faster region-based convolutional neural network with data augmentation and transfer learning, Appl. Sci., 9 (2019), 4898. https://doi.org/10.3390/app9224898 29. R. Ehtisham, W. Qayyum, C. V. Camp, V. Plevris, J. Mir, Q. Z. Khan, et al., Classiﬁcation of defects in wooden structures using pre-trained models of convolutional neural network, Case Stud. Constr. Mat., 19 (2023), e02530. https://doi.org/10.1016/j.cscm.2023.e02530 30. H. Shah, N. Myller, C. Sedano, Forecasting daily customer ﬂow in restaurants: a multifactor machine learning approach, Appl. Comput. Intell., 5 (2025), 168–190. https://doi.org/10.3934/aci.2025011 31. H. Shah, P. Fr¨anti, Combining statistical, structural, and linguistic features for keyword extraction from web pages, Appl. Comput. Intell., 2 (2022), 115–132. https://doi.org/10.3934/aci.2022007 32. H. Shah, R. Mariescu-Istodor, P. Fr¨anti, Webrank: language-independent extraction of keywords from webpages, Proceedings of IEEE International Conference on Progress in Informatics and Computing (PIC), 2021, 184–192. https://doi.org/10.1109/PIC53636.2021.9687047 33. R. Wang, F. Liang, B. Wang, X. Mou, ODCA-YOLO: an omni-dynamic convolution coordinate attention-based YOLO for wood defect detection, Forests, 14 (2023), 1885. https://doi.org/10.3390/f14091885 34. Y. Cui, S. Lu, S. Liu, Real-time detection of wood defects based on spp-improved yolo algorithm, Multimed. Tools Appl., 82 (2023), 21031–21044. https://doi.org/10.1007/s11042-023-14588-7


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.


<!-- Page 22 -->


22


35. L. Yi, M. Akbar, M. Wahab, B. Rosdi, M. Fauthan, N. Shrifan, The prospect of artiﬁcial intelligence-based wood surface inspection: a review, IEEE Access, 12 (2024), 84706–84725. https://doi.org/10.1109/ACCESS.2024.3412928 36. S. Hwang, J. Sugiyama, Computer vision-based wood identiﬁcation and its expansion and contribution potentials in wood science: a review, Plant Methods, 17 (2021), 47. https://doi.org/10.1186/s13007-021-00746-1 37. J. Silva, R. Bordalo, J. Pissarra, P. de Palacios, Computer vision-based wood identiﬁcation: a review, Forests, 13 (2022), 2041. https://doi.org/10.3390/f13122041 38. A. Howard, M. Sandler, G. Chu, L. Chen, B. Chen, M. Tan, et al., Searching for MobileNetV3, Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2019, 1314–1324. https://doi.org/10.1109/ICCV.2019.00140 39. M. Ali, U. Hashim, K. Kanchymalay, A. Wibawa, L. Salahuddin, R. Rahiddin, A review of recent deep learning applications in wood surface defect identiﬁcation, IAES International Journal of Artiﬁcial Intelligence, 14 (2025), 1696. https://doi.org/10.11591/ijai.v14.i3.pp1696-1707 40. K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, 770–778. https://doi.org/10.1109/CVPR.2016.90 41. C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, et al., Going deeper with convolutions, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015, 1–9. https://doi.org/10.1109/CVPR.2015.7298594 42. A. Krizhevsky, I. Sutskever, G. E. Hinton, Imagenet classiﬁcation with deep convolutional neural networks, Commun. ACM, 60 (2017), 84–90. https://doi.org/10.1145/3065386 43. L. Zhang, Y. Bian, P. Jiang, F. Zhang, A transfer residual neural network based on ResNet-50 for detection of steel surface defects, Appl. Sci., 13 (2023), 5260. https://doi.org/10.3390/app13095260 44. CRAN, Available CRAN packages by date of publication, The comprehensive R archive network, 2025. Available from: https://cran.r-project.org/web/packages/available_ packages_by_date.html. 45. Posit software, RPubs, RStudio, 2025. Available from: https://rpubs.com/. 46. M. Deitke, Scaling embodied artiﬁcial intelligence: massive 3d simulations to train agents, Bachelors Thesis, University of Washington, 2023. 47. EPA, Ap-42: compilation of air pollutant emission factors from stationary sources, third edition, U. S. Environmental Protection Agency, 2024. Available from: https://www.epa.gov/air-emissions-factors-and-quantification/ ap-42-compilation-air-emissions-factors-stationary-sources. 48. ISEF, Regeneron international science and engineering fair, Society for Science, 2023. Available from: https://www.societyforscience.org/annual-reports/2023-annual-report/ regeneron-isef/.


c⃝2026 the Author(s), licensee AIMS Press. This is an open access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0)


Applied Computing and Intelligence Volume 6, Issue 1, 1–22.
