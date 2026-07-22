# bilic2022-lits


<!-- Page 1 -->


HHS Public Access Author manuscript Med Image Anal. Author manuscript; available in PMC 2023 November 08.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Published in final edited form as:


Med Image Anal. 2023 February ; 84: 102680. doi:10.1016/j.media.2022.102680.


The Liver Tumor Segmentation Benchmark (LiTS)


This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).


*Corresponding author at: Department of Informatics, Technical University of Munich, Germany. hongwei.li@tum.de (H.B. Li). aOrganization team and data contributor. bP. Bilic, P. Christ, H. B. Li, and E. Vorontsov made equal contributions to this work.


CRediT authorship contribution statement Patrick Bilic: Writing, Data curation, Visualization, Investigation. Patrick Christ: Conceptualization, Writing – original draft, Data curation, Visualization, Software, Validation, Investigation. Hongwei Bran Li: Writing, Revision, Corresponding, Visualization, Investigation. Eugene Vorontsov: Writing, Visualization, Software, Investigation. Avi Ben-Cohen: Conceptualization, Data curation, Writing – review & editing. Georgios Kaissis: Conceptualization, Data curation, Writing – review & editing. Adi Szeskin: Conceptualization, Data curation, Writing – review & editing. Colin Jacobs: Conceptualization, Data curation, Writing – review & editing. Gabriel Efrain Humpire Mamani: Conceptualization, Data curation, Writing – review & editing. Gabriel Chartrand: Conceptualization, Data curation, Writing – review & editing. Fabian Lohöfer: Conceptualization, Data curation, Writing – review & editing. Julian Walter Holch: Conceptualization, Data curation, Writing – review & editing. Wieland Sommer: Conceptualization, Data curation, Writing – review & editing. Felix Hofmann: Conceptualization, Data curation, Writing – review & editing. Alexandre Hostettler: Conceptualization, Data curation, Writing – review & editing. Naama Lev-Cohain: Conceptualization, Data curation, Writing – review & editing. Michal Drozdzal: Conceptualization, Data curation, Writing – review & editing. Michal Marianne Amitai: Conceptualization, Data curation, Writing – review & editing. Refael Vivanti: Conceptualization, Data curation, Writing – review & editing. Jacob Sosna: Conceptualization, Data curation, Writing – review & editing. Ivan Ezhov: Writing – review & editing. Anjany Sekuboyina: Writing – review & editing. Fernando Navarro: Writing – review & editing. Florian Kofler: Writing – review & editing. Johannes C. Paetzold: Writing – review & editing. Suprosanna Shit: Writing – review & editing. Xiaobin Hu: Writing – review & editing. Jana Lipková: Writing – review & editing. Markus Rempfler: Writing – review & editing. Marie Piraud: Writing – review & editing. Jan Kirschke: Writing – review & editing. Benedikt Wiestler: Writing – review & editing. Zhiheng Zhang: Writing – review & editing. Christian Hülsemeyer: Writing – review & editing. Marcel Beetz: Writing – review & editing. Florian Ettlinger: Writing – review & editing. Michela Antonelli: Writing – review & editing. Woong Bae: Writing – review & editing. Míriam Bellver: Writing – review & editing. Lei Bi: Writing – review & editing. Hao Chen: Writing – review & editing. Grzegorz Chlebus: Writing – review & editing. Erik B. Dam: Writing – review & editing. Qi Dou: Writing – review & editing. Chi-Wing Fu: Writing – review & editing. Bogdan Georgescu: Writing – review & editing. Xavier Giró-i-Nieto: Writing – review & editing. Felix Gruen: Writing – review & editing. Xu Han: Writing – review & editing. Pheng-Ann Heng: Writing – review & editing. Jürgen Hesser: Writing – review & editing. Jan Hendrik Moltz: Writing – review & editing. Christian Igel: Writing – review & editing. Fabian Isensee: Writing – review & editing. Paul Jäger: Writing – review & editing. Fucang Jia: Writing – review & editing. Krishna Chaitanya Kaluva: Writing – review & editing. Mahendra Khened: Writing – review & editing. Ildoo Kim: Writing – review & editing. Jae-Hun Kim: Writing – review & editing. Sungwoong Kim: Writing – review & editing. Simon Kohl: Writing – review & editing. Tomasz Konopczynski: Writing – review & editing. Avinash Kori: Writing – review & editing. Ganapathy Krishnamurthi: Writing – review & editing. Fan Li: Writing – review & editing. Hongchao Li: Writing – review & editing. Junbo Li: Writing – review & editing. Xiaomeng Li: Writing – review & editing. John Lowengrub: Writing – review & editing. Jun Ma: Writing – review & editing. Klaus Maier-Hein: Writing – review & editing. Kevis-Kokitsi Maninis: Writing – review & editing. Hans Meine: Writing – review & editing. Dorit Merhof: Writing – review & editing. Akshay Pai: Writing – review & editing. Mathias Perslev: Writing – review & editing. Jens Petersen: Writing – review & editing. Jordi Pont-Tuset: Writing – review & editing. Jin Qi: Writing – review & editing. Xiaojuan Qi: Writing – review & editing. Oliver Rippel: Writing – review & editing. Karsten Roth: Writing – review & editing. Ignacio Sarasua: Writing – review & editing. Andrea Schenk: Writing – review & editing. Zengming Shen: Writing – review & editing. Jordi Torres: Writing – review & editing. Christian Wachinger: Writing – review & editing. Chunliang Wang: Writing – review & editing. Leon Weninger: Writing – review & editing. Jianrong Wu: Writing – review & editing. Daguang Xu: Writing – review & editing. Xiaoping Yang: Writing – review & editing. Simon Chun-Ho Yu: Writing – review & editing. Yading Yuan: Writing – review & editing. Miao Yue: Writing – review & editing. Liping Zhang: Writing – review & editing. Jorge Cardoso: Writing – review & editing. Spyridon Bakas: Writing – review & editing. Rickmer Braren: Conceptualization, Data curation, Writing – review & editing. Volker Heinemann: Conceptualization, Data curation, Writing – review & editing. Christopher Pal: Conceptualization, Data curation, Writing – review & editing. An Tang: Conceptualization, Data curation, Writing – review & editing. Samuel Kadoury: Conceptualization, Data curation, Writing – review & editing. Luc Soler: Conceptualization, Data curation, Writing – review & editing. Bram van Ginneken: Conceptualization, Data curation, Writing – review & editing. Hayit Greenspan: Conceptualization, Data curation, Writing – review & editing. Leo Joskowicz: Conceptualization, Data curation, Writing – review & editing. Bjoern Menze: Conceptualization, Writing – review & editing, Data curation, Visualization, Supervision, Investigation.


Declaration of competing interest The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.


<!-- Page 2 -->


Bilic et al. Page 2


A full list of authors and affiliations appears at the end of the article.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


## Abstract


In this work, we report the set-up and results of the Liver Tumor Segmentation Benchmark (LiTS), which was organized in conjunction with the IEEE International Symposium on Biomedical Imaging (ISBI) 2017 and the International Conferences on Medical Image Computing and Computer-Assisted Intervention (MICCAI) 2017 and 2018. The image dataset is diverse and contains primary and secondary tumors with varied sizes and appearances with various lesion-tobackground levels (hyper−/hypo-dense), created in collaboration with seven hospitals and research institutions. Seventy-five submitted liver and liver tumor segmentation algorithms were trained on a set of 131 computed tomography (CT) volumes and were tested on 70 unseen test images acquired from different patients. We found that not a single algorithm performed best for both liver and liver tumors in the three events. The best liver segmentation algorithm achieved a Dice score of 0.963, whereas, for tumor segmentation, the best algorithms achieved Dices scores of 0.674 (ISBI 2017), 0.702 (MICCAI 2017), and 0.739 (MICCAI 2018). Retrospectively, we performed additional analysis on liver tumor detection and revealed that not all top-performing segmentation algorithms worked well for tumor detection. The best liver tumor detection method achieved a lesion-wise recall of 0.458 (ISBI 2017), 0.515 (MICCAI 2017), and 0.554 (MICCAI 2018), indicating the need for further research. LiTS remains an active benchmark and resource for research, e.g., contributing the liver-related segmentation tasks in http://medicaldecathlon.com/. In addition, both data and online evaluation are accessible via https://competitions.codalab.org/ competitions/17094.


Keywords


Segmentation; Liver; Liver tumor; Deep learning; Benchmark; CT


## 1. Introduction


Background.


The liver is the largest solid organ in the human body and plays an essential role in metabolism and digestion. Worldwide, primary liver cancer is the second most common fatal cancer (Stewart and Wild, 2014). Computed tomography (CT) is a widely used imaging tool to assess liver morphology, texture, and focal lesions (Hann et al., 2000). Anomalies in the liver are essential biomarkers for initial disease diagnosis and assessment in both primary and secondary hepatic tumor disease (Heimann et al., 2009). The liver is a site for primary tumors that start in the liver. In addition, cancer originating from other abdominal organs, such as the colon, rectum, and pancreas, and distant organs, such as the breast and lung, often metastasize to the liver during disease. Therefore, the liver and its lesions are routinely analyzed for comprehensive tumor staging. The standard Response Evaluation Criteria in Solid Tumor (RECIST) or modified RECIST protocols require measuring the diameter of the largest target lesion (Eisenhauer et al., 2009). Hence, accurate and precise segmentation of focal lesions is required for cancer diagnosis, treatment planning, and monitoring of the treatment response. Specifically, localizing the tumor lesions in a given image scan is a


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 3 -->


Bilic et al. Page 3


prerequisite for many treatment options such as thermal percutaneous ablation (Shiina et al., 2018), radiotherapy, surgical resection (Albain et al., 2009) and arterial embolization (Virdis et al., 2019). Like many other medical imaging applications, manual delineation of the target lesion in 3D CT scans is time-consuming, poorly reproducible (Todorov et al., 2020) and segmentation shows operator-dependent results.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Technical challenges.


Fully automated segmentation of the liver and its lesions remain challenging in many aspects. First, the variations in the lesion-to-background contrast (Moghbel et al., 2017) can be caused by: (a) varied contrast agents, (b) variations in contrast enhancement due to different injection timing, and (c) different acquisition parameters (e.g., resolution, mAs and kVp exposure, reconstruction kernels). Second, the coexistence of different types of focal lesions (benign vs. malignant and tumor sub-types) with varying image appearances presents an additional challenge for automated lesion segmentation. Third, the liver tissue background signal can vary substantially in the presence of chronic liver disease, which is a common precursor of liver cancer. It is observed that many algorithms struggle with diseasespecific variability, including the differences in size, shape, and the number of lesions, as well as with modifications in shape and appearance to the liver organ itself induced by treatment (Moghbel et al., 2017). Examples of differences in liver and tumor appearance in two patients are depicted in Fig. 1, demonstrating the challenges of generalizing to unseen test cases with varying lesions.


Contributions.


In order to evaluate the state-of-the-art methods for automated liver and liver tumor segmentation, we organized the Liver Tumor Segmentation Challenge (LiTS) in three events: (1) in conjunction with the IEEE International Symposium on Biomedical Imaging (ISBI) 2017, (2) with MICCAI 2017 and (3) as a dedicated challenge task on liver and liver tumor segmentation in the Medical Segmentation Decathlon 2018 in MICCAI 2018 (Antonelli et al., 2022).


In this paper, we describe the three key contributions to fully automated liver and liver tumor segmentation. First, we generate a new public multi-center dataset of 201 abdominal CT Volumes and the reference segmentations of liver and liver tumors. Second, we present the set-up and the summary of our LiTS benchmarks in three grand challenges. Third, we review, evaluate, rank, and analyze the resulting state-of-the-art algorithms and results. The paper is structured as follows: Section 2 reviews existing public datasets and state-ofthe-art automated liver and liver tumors segmentation. Next, Section 3 describes the LiTS challenge setup, the released multi-center datasets, and the evaluation process. Section 4 reports results, analyzes the liver tumor detection task, showcases critical cases in the LiTS Challenge results, and discusses the technical trends and challenges in liver tumor segmentation. Section 5 discusses the limitations, summarizes this work, and points to future work.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 4 -->


Bilic et al. Page 4


## 2. Prior work: Datasets & approaches


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


## 2.1. Publicly available liver and liver tumor datasets


Compared to other organs, available liver datasets offer either a relatively small number of images and reference segmentation or provide no reference segmentation (see Table 1). The first grand segmentation challenge - SLIVER07 was held in MICCAI 2007 (Heimann et al., 2009), including the 30 CT liver images for automated segmentation. In MICCAI 2008, the LTSC’08 segmentation challenge offered 30 CT volumes with a focus on tumor segmentation (Deng and Du, 2008). The ImageCLEF 2015 liver CT reporting benchmark1


made 50 volumes available for computer-aided structured reporting instead of segmentation. The VISCERAL (Jimenez-del Toro et al., 2016) challenge provided 60 scans per two modalities (MRI and CT) for anatomical structure segmentation and landmark detection. The recent CHAOS challenge (Kavur et al., 2021) provide 40 CT volumes and 120 MRI volumes for healthy abdominal organ segmentation. However, none of these datasets represents well-defined cohorts of patients with lesions, and segmentation of the liver and its lesions are absent.


## 2.2. Approaches for liver and liver tumor segmentation


Before 2016, most automated liver and tumor segmentation methods used traditional machine learning methods. However, since 2016 and the first related publications at MICCAI (Christ et al., 2016), deep learning methods have gradually become a methodology of choice. The following section provides an overview of published automated liver and liver tumor segmentation methods.


2.2.1. Liver segmentation—Published work on liver segmentation methods can be grouped into three categories based on: (1) prior shape and geometric knowledge, (2) intensity distribution and spatial context, and (3) deep learning.


Methods based on shape and geometric prior knowledge.: Over the last two decades, statistical shape models (SSMs) (Cootes et al., 1995) have been used for automated liver segmentation tasks. However, deformation limitations prevent SSMs from capturing the high variability of the liver shapes. To overcome this issue, SSM approaches often rely on additional steps to obtain a finer segmentation contour. Therefore SSMs followed by a deformable model performing free form deformation became a valuable method for liver segmentation (Heimann et al., 2006; Kainmüller et al., 2007; Zhang et al., 2010; Tomoshige et al., 2014; Wang et al., 2015). Moreover, variations and further enhancement of SSMs such as 3D-SSM based on an intensity profiled appearance model (Lamecker et al., 2004), incorporating non-rigid template matching (Saddi et al., 2007), initialization of SSMs utilizing an evolutionary algorithm (Heimann et al., 2007), hierarchical SSMs (Ling et al., 2008), and deformable SSMs (Zhang et al., 2010) had been proposed to solve liver segmentation tasks automatically. SSMs-based methods showed the best results in SLIVER07, the first grand challenge held in MICCAI 2007 (Heimann et al., 2009; Dawant et al., 2007).


1 https://www.imageclef.org/2015/liver


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 5 -->


Bilic et al. Page 5


Methods based on intensity distribution and spatial context.: A probabilistic atlas (PA) is an anatomical atlas with parameters that are learned from a training dataset. Park et al. proposed the first PA utilizing 32 abdominal CT series for registration based on mutual information and thin-plate splines as warping transformations (Park et al., 2003) and a Markov random field (MRF) (Park et al., 2003) for segmentation. Further proposed atlasbased methods differ in their computation of the PA and how the PA is incorporated into the segmentation task. Furthermore, PA can incorporate relations between adjacent abdominal structures to define an anatomical structure surrounding the liver (Zhou et al., 2006). Multiatlas methods improved liver segmentation results by using non-rigid registration with a B-spline transformation model (Slagmolen et al., 2007), dynamic atlas selection and label fusion (Xu et al., 2015), or liver and non-liver voxel classification based on k-Nearest Neighbors (van Rikxoort et al., 2007).


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Graph cut methods offer an efficient way to binary segmentation problems, initialized by adaptive thresholding (Massoptier and Casciaro, 2007) and supervoxel (Wu et al., 2016).


Methods based on deep learning.: In contrast to the methods above, deep learning, especially convolutional neural networks (CNN), is a data-driven method that can be optimized end-to-end without hand-craft feature engineering (Litjens et al., 2017). The U-shape CNN architecture (Ronneberger et al., 2015) and its variants (Milletari et al., 2016; Isensee et al., 2020; Li et al., 2018b) are widely used for biomedical image segmentation and have already proven their efficiency and robustness in a wide range of segmentation tasks. Top-performing methods share the commonality of multi-stage processes, beginning with a 3D CNN for segmentation, and post-process the resulting probability maps with Markov random field (Dou et al., 2016). Many early deep learning algorithms for liver segmentation combine neural networks with dedicated post-processing routines: Christ et al. (2016) uses 3D fully connected neural networks combined with conditional random fields, Hu et al. (2016) rely on a 3D CNN followed by a surface model. In contrast, Lu et al. (2017) use a CNN regularized by a subsequent graph-cut segmentation.


2.2.2. Liver tumor segmentation—Compared to the liver, its lesions feature a more comprehensive range of shape, size, and contrast. Liver tumors can be found in almost any location, often with ambiguous boundaries. Differences in the uptake of contrast agents may introduce additional variability. Therefore liver tumor segmentation is considered to be the more challenging task. Published methods of liver tumor segmentation can be categorized into (1) thresholding and spatial regularization, (2) local features and learning algorithms, and (3) deep learning.


Methods with thresholding and spatial regularization.: Based on the assumption that gray level values of tumor areas differ from pixels/voxels belonging to regions outside the tumor, thresholding is a simple yet effective tool to automatically separate tumor from liver and background, first shown by Soler et al. (2001). Since then the threshold have set by histogram analysis (Ciecholewski and Ogiela, 2007), maximum variance between classes (Nugroho et al., 2008) and iterative algorithm (Abdel-massieh et al., 2010) to improve tumor segmentation results. Spatial regulation techniques rely on (prior) information about the image or morphologies, e.g., tumor size, shape, surface, or spatial


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 6 -->


Bilic et al. Page 6


information. This knowledge is used to introduce constraints in the form of regularization or penalization. Adaptive thresholding methods can be combined with model-based morphological processing for heterogeneous lesion segmentation (Moltz et al., 2008, 2009). Active contour (Kass et al., 1988) based tumor segmentation relies on shape and surface information and utilize probabilistic models (Ben-Dan and Shenhav, 2008) or histogram analysis (Linguraru et al., 2012) to create segmentation maps automatically. Level set (Osher and Sethian, 1988) methods allow numerical computations of tumor shapes without parametrization. Level set approaches for liver tumor segmentation are combined with supervised pixel/voxel classification in 2D (Smeets et al., 2008) and 3D (Jiménez Carretero et al., 2011).


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Methods using local features and learning algorithms.: Clustering methods include kmeans (Massoptier and Casciaro, 2008) and fuzzy c-means clustering with segmentation refinement using deformable models (Häme, 2008). Among supervised classification methods are a fuzzy classification based level set approach (Smeets et al., 2008), support vector machines in combination with a texture based deformable surface model for segmentation refinement (Vorontsov et al., 2014), AdaBoost trained on texture features (Shimizu et al., 2008) and image intensity profiles (Li et al., 2006), logistic regression (Wen et al., 2009), and random forests recursively classifying and decomposing supervoxels (Conze et al., 2017).


Methods based on deep learning.: Before LiTS, deep learning methods have been rarely used for liver tumor segmentation tasks. Christ et al. (2016) was the first to use 3D U-Net for liver and liver tumor segmentation, proposing a cascaded segmentation strategy, together with a 3D conditional random field refinement. Many of the subsequent deep learning approaches were developed and tested in conjunction with the LiTS dataset.


Benefiting from the availability of the LiTS public dataset, many new deep learning solutions on liver and liver segmentation were proposed. U-Net-based architectures are extensively used and modified to improve segmentation performance. For example, the nn-UNet (Isensee et al., 2020) first presented in LiTS at MICCAI 2018, was shown to be one of the most top-performing methods in 3D image segmentation tasks. The related works will be discussed in the results section.


## 3. Methods


## 3.1. Challenge setup


The first LiTS benchmark was organized in Melbourne, Australia, on April 18, 2017, in a workshop held at the IEEE ISBI 2017 conference. During Winter 2016/2017, participants were solicited through private emails, public email lists, social media, and the IEEE ISBI workshop announcements. Participants were requested to register at our online benchmarking system hosted on CodaLab and could download annotated training data and unannotated test data. The online benchmarking platform automatically computed performance scores. They were asked to submit a four-page summary of their algorithm after successful submissions to the CodaLab platform. Following the successful submission process at ISBI 2017, the second LiTS benchmark was held on September


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 7 -->


Bilic et al. Page 7


14, 2017, in Quebec City, Canada, as a MICCAI workshop. The third edition of LiTS was a part of the Medical Segmentation Decathlon at MICCAI 2018 (available at http:// medicaldecathlon.com/).


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


At ISBI 2017, five out of seventeen participating teams presented their methods at the workshop. At MICCAI 2017, the LiTS challenge introduced a new benchmark task — liver segmentation. Participants registered a new CodaLab benchmark and were asked to describe their algorithm after the submission deadline, resulting in 26 teams. The training and test data for the benchmark were identical to the ISBI benchmark. The workshop at the MICCAI 2017 was organized similarly to the ISBI edition. At MICCAI 2018, LiTS was a part of a medical image segmentation decathlon organized by King’s College London in conjunction with eleven partnerships for data donation, challenge design, and administration. The LiTS benchmark dataset described in this paper constitutes the decathlon’s liver and liver lesion segmentation tasks. However, the overall challenge also required the participants to address nine other tasks, including brain tumor, heart, hippocampus, lung, pancreas, prostate, hepatic vessel, spleen, and colon segmentation. To this end, algorithms were not necessarily optimized only for liver CT segmentation.


## 3.2. Dataset


Training and test cases both represented abdomen CT images. The data is licensed as CC BY-NC-SA. Only the organizers from TUM have access to the labels of test images. The participants could download annotated training data from the LiTS Challenge website.2


Contributors.—The image data for the LiTS challenge are collected from seven clinical sites all over the world, including (a) Rechts der Isar Hospital, the Technical University of Munich in Germany, (b) Radboud University Medical Center, the Netherlands, (c) Polytechnique Montréal and CHUM Research Center in Canada, (d) Sheba Medical Center in Israel, (e) the Hebrew University of Jerusalem in Israel, (f) Hadassah University Medical Center in Israel, and (g) IRCAD in France. The distribution of the number of scans per institution is described in Table 2. The LiTS benchmark dataset contains 201 computed tomography images of the abdomen, of which 194 CT scans contain lesions. All data are anonymized, and the images have been reviewed visually to preclude the presence of personal identifiers. The only processing applied to the images is a transformation into a unified NIFTY format using NiBabel in Python.3 All parties agreed to make the data publicly available; ethics approval was not required.


Data diversity.—The studied cohort covers diverse types of liver tumor diseases, including primary tumor disease (such as hepatocellular carcinoma and cholangiocarcinoma) and secondary liver tumors (such as metastases from colorectal, breast and lung primary cancers). The tumors had varying lesion-to-background ratios (hyper- or hypo-dense). The images represented a mixture of pre- and post-therapy abdominal CT scans and were acquired with different CT scanners and acquisition protocols, including imaging artifacts (e.g., metal artifacts) commonly found in real-world clinical data. Therefore, it was


2 www.lits-challenge.com 3 https://nipy.org/nibabel/


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 8 -->


Bilic et al. Page 8


considered to be very diverse concerning resolution and image quality. The in-plane image resolution ranges from 0.56 mm to 1.0 mm, and 0.45 mm to 6.0 mm in slice thickness. Also, the number of axial slices ranges from 42 to 1026. The number of tumors varies between 0 and 12. The size of the tumors varies between 38 mm3 and 1231 mm3. The test set shows a higher number of tumor occurrences compared to the training set. The statistical test (p-value = 0.6) shows that the liver volumes in the training and test sets do not differ significantly. The average tumor HU value is 65 and 59 in the train and test sets, respectively. The LiTS data statistics are summarized in Table 3. The training and test split is with a ratio of 2:1 and the training and test sets were similar in center distribution. Generalizability to unseen centers has, hence, not been tested in LiTS.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Annotation protocol.—The image datasets were annotated manually using the following strategy: A radiologist with > 3 years of experience in oncologic imaging manually labeled the datasets slice-wise using the ITK-SNAP (Yushkevich et al., 2006) software and assigning one of the labels ‘Tumor’ or ‘Healthy Liver’. Here, the “Tumor” label included any neoplastic lesion irrespective of origin (i.e. both primary liver tumors and metastatic lesions). Any part of the image not assigned one of the aforementioned labels was considered ‘Background’. The segmentations were verified by three further readers blinded to the initial segmentation, with the most senior reader serving as tie-breaker in cases of labeling conflicts. Those scans with very small and uncertain lesion-like structures were omitted in the annotation.


## 3.3. Evaluation


3.3.1. Ranking strategy—The main objective of LiTS was to benchmark segmentation algorithms. We assessed the segmentation performance of the LiTS submissions considering three aspects: (a) volumetric overlap, (b) surface distance, and (c) volume similarity. All the values of these metrics are released to the participating teams. Considering that the volumetric overlap is our primary interest in liver and liver tumor segmentation, for simplicity, we only use the Dice score to rank the submissions at ISBI-2017 and MICCAI-2017. However, the exact choice of evaluation metric does sometimes affect the ranking results, as different metrics are sensitive to different types of segmentation errors. Hence, we provide a post-challenge ranking, considering three properties by summing up three ranking scores and re-ranking by the final scores. The evaluation codes for all metrics can be accessed in Github.4


3.3.2. Statistical tests—To compare the submissions from two teams in a per case manner, we used Wilcoxon signed-rank test (Rey and Neuhäuser, 2011). To compare the distributions of submissions from two years, we used the Mann–Whitney U Test (McKnight and Najab, 2010) (unpaired) for the two groups.


3.3.3. Segmentation metrics—Dice score. The Dice score evaluates the degree of overlap between the predicted and reference segmentation masks. For example, given two binary masks A and B, it is formulated as:


4 https://github.com/PatrickChrist/lits-challenge-scoring


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 9 -->


Bilic et al. Page 9


Dice(A, B) = 2 ∣A ∩B ∣ ∣A ∣+ ∣B ∣ (1)


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


The Dice score is applied per case and then averaged over all cases consistently for three benchmarks. This way, the Dice score applies a higher penalty to prediction errors in cases with fewer actual lesions.


Average symmetric surface distance.: Surface distance metrics are correlated measures of the distance between the surfaces of a reference and the predicted region. Let S(A) denote the set of surface voxels of A. Then, the shortest distance of an arbitrary voxel v to S(A) is defined as:


d(v, S(A)) = min sA ∈S(A)


‖v −sA‖, (2)


where ‖ . ‖ denotes the Euclidean distance. The average symmetric surface distance (ASD) is then given by:


ASD(A, B) = 1 ∣S(A) ∣+ ∣S(B) ∣ ∑ sA ∈S(A)


d(sA, S(B)) + ∑ sB ∈S(B)


d(sB, S(A)) . (3)


Maximum symmetric surface distance.: The maximum symmetric surface distance (MSSD), also known as the Symmetric Hausdorff Distance, is similar to ASD except that the maximum distance is taken instead of the average:


MSSD(A, B) = max max sA ∈S(A)


d(sA, S(B)), max sB ∈S(B)


d(sB, S(A)) . (4)


Relative volume difference.: The relative volume difference (RVD) directly measures the volume difference without considering the overlap between reference A and the prediction


B.


## RV D(A, B) = ∣B ∣−∣A ∣


## ∣A ∣ . (5)


For the other evaluation metrics, such as tumor burden estimation and the corresponding rankings, please check Appendix.


3.3.4. Detection metrics—Considering the clinical relevance of lesion detection, we introduce three detection metrics in the additional analysis. The metrics are calculated globally to avoid potential issues when the patient has no tumors. There must be a known correspondence between predicted and reference lesions to evaluate the lesion-wise metrics. Since lesions are all defined as a single binary map, this correspondence must be determined between the prediction and reference masks’ connected components. Components may not


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 10 -->


Bilic et al. Page 10


necessarily have a one-to-one correspondence between the two masks. The details of the correspondence algorithm are presented in Appendix C.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Individual lesions are defined as 3D connected components within an image. A lesion is considered detected if the predicted lesion has sufficient overlap with its corresponding reference lesion, measured as the intersection over the union of their respective segmentation masks. It allows for a count of true positive, false positive, and false-negative detection, from which we compute the precision and recall of lesion detection. The metrics are defined as follows:


Individual lesions are defined as 3D connected components within an image. A lesion is considered detected if the predicted lesion has sufficient overlap with its corresponding reference lesion, measured as the intersection over the union of their respective segmentation masks. It allows for a count of true positive, false positive, and false-negative detection, from which we compute the precision and recall of lesion detection. The metrics are defined as follows:


IoU = ∣A ∩B ∣


## ∣A ∪B ∣. (6)


Precision.: It relates the number of true positives (TP) to false positives (FP), also known as positive predictive value:


precision = TP TP + FP . (7)


Recall.: It relates the number of true positives (TP) to false negatives (FN), also known as sensitivity or true positive rate:


recall = TP TP + FN . (8)


F1 score.: It measures the harmonic mean of precision and recall:


F1 = 2 precision−1 + recall−1 . (9)


3.3.5. Participating policy and online evaluation platform—The participants were allowed to submit three times per day in the test stage during the challenge week. Members of the organizers’ groups could participate but were not eligible for awards. The awards were given to the top three teams for each task. The top three performing methods gave 10-min presentations and were announced publicly. For a fair comparison, the participating teams were only allowed to use the released training data to optimize their methods. All participants were invited to be co-authors of the manuscript summarizing the challenge.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 11 -->


Bilic et al. Page 11


A central element of LiTS was – and remains to be – its online evaluation tool hosted by CodaLab. On Codalab, participants could download annotated training and “blinded” test data and upload their segmentation for the test cases. The system automatically evaluated the uploaded segmentation maps’ performance and made the overall performance available to the participants. Average scores for the different liver and lesion segmentation tasks and tumor burden estimation were also reported online on a leaderboard. Reference segmentation files for the LiTS test data were hosted on the Codalab but not accessible to participants. Therefore, the users uploaded their segmentation results through a web interface, reviewed the uploaded segmentation, and then started an automated evaluation process. The evaluation to assess the segmentation quality took approximately two minutes per volume. In addition, the overall segmentation results of the evaluation were automatically published on the Codalab leaderboard web page and could be downloaded as a csv file for further statistical analysis.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


The Codalab platform remained open for further use after the three challenges and will remain so in the future. As of April 2022, it has evaluated more than 3414 valid submissions (238,980 volumetric segmentation) and recorded over 900 registered LiTS users. The up-to-date ranking is available at Codalab for researchers to continuously monitor new developments and streamline improvements. In addition, the code to generate the evaluation metrics between reference and predictions is available as open-source at GitHub.5


## 4. Results


## 4.1. Submitted algorithms and method description


The submitted methods in ISBI-2017, MICCAI-2017 and MICCAI-2018 are summarized in Tables 4 and 5, and the reference paper of Medical Segmentation Decathlon (Antonelli et al., 2022). In the following, we grouped the algorithms with several properties.


Algorithms and architectures.—Seventy-three submissions were fully automated approaches, while only one was semi-supervised (■ J. Ma et al.). U-Net derived architectures were overwhelmingly used in the challenge with only two automated methods using a modified VGG-net (■ J. Qi et al.) and a k-CNN (■ J. Lipkova et al.) respectively. Most submissions adopted the coarse-to-fine approach in which multiple U-nets were cascaded to perform liver and liver segmentation at different stages. Additional residual connections and adjusted input resolution were the most common changes to the basic UNet architecture. Three submissions combined individual models as an ensemble technique. In 2017, 3D methods were not directly employed on the original image resolution by any of the submitted methods due to high computational complexity. However, some submissions used 3D convolutional neural networks solely for tumor segmentation tasks with small input patches. Instead of full 3D, other methods tried to capture the advantages of threedimensionality by using a 2.5 D model architecture, i.e., providing a stack of images as a multi-channel input to the network and receiving the segmentation mask of the center slice of this stack as a network output.


5 https://github.com/PatrickChrist/LiTS-CHALLENGE


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 12 -->


Bilic et al. Page 12


Critical components of the segmentation methods.—Data pre-processing with HU-value clipping, normalization, and standardization were the most frequent techniques in most of the methods. Data augmentation was also widely used and mainly focused on standard geometric transformations such as flipping, shifting, scaling, or rotation. Individual submissions implemented more advanced techniques such as histogram equalization and random contrast normalization. The most common optimizer varied between ADAM and Stochastic gradient descent with momentum, with one approach relying on RMSProp. Multiple loss functions were used for training, including standard and class-weighted cross-entropy, Dice loss, Jaccard loss, Tversky loss, L2 loss, and ensemble loss techniques combining multiple individual loss functions into one.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Post-processing.—Some types of post-processing methods were also used by the vast majority of the algorithm. The common post-processing steps were to form connected tumor components and overlay the liver mask on the tumor segmentation to discard tumors outside the liver region. More advanced methods included a random forest classifier, morphological filtering, a particular shallow neural network to eliminate false positives or custom algorithms for tumor hole filling.


Features of top-performing methods.—The best-performing methods at ISBI 2017 used cascaded U-Net approaches with short and long skip connections and 2.5D input images (■ X. Han et al.). In addition, weighted cross-entropy loss functions and a few ensemble learning techniques were employed by most of the top-performing methods, together with some common pre- and post-processing steps such as HU-value clipping and connected component labeling, respectively. Some top-performing submissions at MICCAI 2017 (e.g., ■ J. Zou) integrated the insights from the ISBI 2017, including the idea of the ensemble, adding residual connections, and featuring more sophisticated rule-based post-processing or classical machine learning algorithms. Therefore, the main architectural differences compared to the ISBI submissions were the higher usage of ensemble learning methods, a higher incidence of residual connections, and an increased number of more sophisticated post-processing steps. Another top-performing method by ■ X. Li et al. proposed a hybrid insight by integrating the advantages of the 2D and 3D networks in the 3D liver tumor segmentation task (Li et al., 2018a). Therefore, compared to the methods in ISBI submissions that solely rely on 2D or 3D convolutions, the main architecture difference was the hybrid usage of 2D and 3D networks. In MICCAI-LiTS 2018, 3D deep learning models became popular and generally outperformed 2.5D or 2D without more sophisticated pre-processing steps.


## 4.2. Results of individual challenges


At ISBI 2017 and MICCAI 2017, the LiTS challenges received 61 valid submissions and 32 contributing short papers as part of the two workshops. At MICCAI 2018, LiTS was held as part of the Medical Segmentation Decathlon and received 18 submissions (one of them was excluded from the analysis as requested by the participating team). In this work, the segmentation results were evaluated based on the same metrics described to ensure the comparability between the three events. For ISBI 2017, no liver segmentation task was


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 13 -->


Bilic et al. Page 13


evaluated. The results of the tumor segmentation task were shown for all the events, i.e., ISBI 2017, MICCAI 2017, and MICCAI 2018.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


## 4.2.1. Liver segmentation


Overview.: The results of the liver segmentation task showed high Dice scores; most teams achieved more than 0.930. It indicated that solely using the Dice score could not distinguish a clear winner. When we compared the progress with the two LiTS benchmarks, the results of MICCAI 2017 were slightly better than the MICCAI-MSD 2018 in terms of ASD (1.104 vs. 1.342). It might be because the algorithms for MICCAI-MSD were optimized considering their generalizability on different organs and imaging modalities. In contrast, the methods for MICCAI 2017 were specifically optimized for liver and CT imaging. The ranking result is shown in Table 6.


LiTS–MICCAI 2017.: The evaluation of the liver segmentation task relied on the three metrics explained in the previous chapter, with the Dice score per case acting as the primary metric used for the final ranking. Almost all methods except the last three achieved Dice per case values above 0.920, with the best one scoring 0.963. Ranking positions remain relatively stable when ordering submissions according to the other surface distance metric. Most methods changed by a few spots, and the top four methods were only interchanging positions among themselves. The position variation was more significant than the Dice score when using the surface distance metric ASD for the ranking, with some methods moving up to 4 positions. However, on average, the top-2 performing Dice per case methods still achieved the lowest surface distance values, with the winning method retaining the top spot in two rankings.


LiTS–MICCAI–MSD 2018.: The performance of Decathlon methods in liver segmentation showed similar results compared to MICCAI 2017. In both challenges, one could observe that the difference in Dice scores between top-performing methods was insignificant mainly because the liver is a large organ. The comparison of ASD between MICCAI 2018 and MICCAI 2017 confirmed that state-of-the-art methods could automatically segment the liver with similar performance to manual expert annotation for most cases. However, the methods exclusively trained for liver segmentation in MICCAI 2017 showed better segmentations under challenging cases (1.104 vs. 1.342).


## 4.2.2. Liver tumor segmentation and detection


Overview.: While automated liver segmentation methods showed promising results (comparable to expert annotation), the liver tumor segmentation task remained room for improvement. To illustrate the difficulty of detecting small lesions, we grouped the lesions into three categories with a clinical standard: (a) small lesions less than 10 mm in diameter, (b) medium lesions between 10 mm and 20 mm in diameter, and (c) large lesion bigger than 20 mm in diameter. The ranking result is shown in Table 7.


LiTS–ISBI 2017.: The highest Dice scores for liver tumor segmentation were in the middle 0.60s range, with the winner team achieving a score of 0.674 followed by 0.652 and 0.645 for the second and third places, respectively. However, there were no statistically significant


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 14 -->


Bilic et al. Page 14


differences between the top three teams in all three metrics. The final ranking changed to some degree when considering the ASD metric. For example, Bi et al. obtained the best ASD score but retained its order with the best methods overall. In lesion detection, we found that detecting small lesions was very challenging in which top-performing teams achieved only around 0.10 in F1 score. Fig. 6 shows some sample results of the top-performing methods.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


LiTS–MICCAI 2017.: The best tumor segmentation Dice scores improved significantly compared to ISBI, with MICCAI’s highest average Dice (per case) of 0.702 compared to 0.674 in ISBI on the same test set. However, the ASD metric did not improve (1.189 vs. 1.118) on the best top-performing method. In addition, there were no statistically significant differences between the top three teams in all three metrics. There was an overall positive correlation of ranking positions with submissions that performed well at the liver segmentation task concerning the liver tumor segmentation task. A weak positive correlation between the Dice ranking and the surface distance metrics could still be observed, although a considerable portion of methods changes positions by more than a few spots. The detection performance in MICCAI 2017 showed improvement over ISBI 2017 in lesion recall (0.479 vs. 0.458 for the best team). Notably, the best-performing team (■ J. Zou et al.) achieved a very low precision of 0.148, which indicated that the method generates many false positives. Fig. 7 shows some sample results of the top-performing methods.


LiTS–MICCAI–MSD 2018.: The LiTS evaluation of MICCAI 2018 was integrated into MSD and attracted much attention, receiving 18 valid submissions. Methods were ranked according to two metrics: Dice score and ASD (in liver and liver tumor segmentation tasks). Compared to MICCAI 2017 and ISBI 2016, the two top-performing teams significantly improved the Dice scores (0.739 and 0.721 vs. 0.702) and ASD (0.903 and 0.896 vs. 1.189). However, there were no statistically significant differences between the top two teams in all three metrics. The first place (F. Isensee et al.) statistically significant (p-value < 0.001) outperformed the third place (S. Chen et al.) considering Dice score. More importantly, the same team won the two tasks using a self-adapted 3D deep learning solution, indicating a step forward in the development of segmentation methodology. The detection performance in MICCAI 2018 showed improvement over MICCAI 2017 in lesion recall (0.554 vs. 0.479 for the best-performing teams).


From the scatter plots shown in Fig. 2, we observed that not all the top-performing methods in three LiTS challenges achieved good scores on tumor detection. The behavior of distanceand overlap-based metrics was similar. The detection metrics with clinical relevance could prevent the segmentation model from tending to segment large lesions. Thus it should be considered when ranking participating teams and performing the comprehensive assessment.


## 4.3. Meta analysis


In this section, we focus on liver tumor segmentation and analyze the inter-rater variability and method development during the last six years.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 15 -->


Bilic et al. Page 15


4.3.1. Inter-rater agreement—To better interpret the algorithmic variability and performance, we recruited another radiologist (Z. Z.) with > 3 years of experience in oncologic imaging to re-annotate 15 3D CT scans, and two board-certified radiologists (J. K. and B. W.) to re-evaluate the original annotations. In Fig. 3, R2 re-annotated 15 CT scans from scratch. R3 and R4 are board-certified radiologists who checked and corrected the annotations. Specifically, one board-certified radiologist (R3) reviewed and corrected existing annotations. R4 re-evaluated R3’s final annotations and corrected them. The interrater agreement was calculated by the Dice score per case between the pairs of two raters. We observed high inter-rater variability (median Dice of 70.2%)between the new annotation (R2) and the existing consensus annotation. We observed very high agreement (median Dice of 95.2%) between the board-certified radiologist and the existing annotations. Considering that the segmentation models were solely optimized on R1 and the best model achieved 82.5% on the leader-board (last access: 04.04.2022), we argue that there is still room for improvement.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


## 4.3.2. Performance improvement


Top-performing teams over three events.: First, we plotted the scores of Dice and ASD for three top-performing teams over the three events, as shown in Fig. 4. We observed incremental improvement (e.g., the median scores) over the three events. We further performed Wilcoxon signed-rank tests on the best teams (ranked by mean Dice) between each pair of two events. We observed that MSD’18 shows significant improvement against ISBI’17 on both metrics (see Table 8). For MSD’18, the submitted algorithms architectures were the same for all subtasks. They were trained individually for sub-tasks (e.g., liver, kidney, pancreas), focusing on the generalizability of segmentation models. The main advance was the advent of 3D deep learning models after 2017. Tables 4 and 5 show that most of the approaches were 2D and 2.5D based. The winner of MSD — the nn-Unet approach was a 3D UNet based, self-configured and adaptive for specific tasks. We attributed the main improvement to the 3D architectures, which was in line with other challenges and benchmark results in medical image segmentation that occurred during this time.


CodaLab submissions in the last six years.: First, we separated the submissions yearly and summarized them by individual violin plots shown in Fig. 5. We observed a continuous improvement over the years, with the best results obtained in 2022. We excluded the submissions that achieved Dice scores >10% in the analysis. We further performed the Mann–Whitney U test on the distributions of mean Dice and ASD scores of all teams for each year. We observed that the scores achieved in 2022 are significantly better than in 2021, indicating that the LiTS challenge remains active and contributes to methodology development (see Table 9).


## 4.4. Technique trend and recent advances


We have witnessed that the released LiTS dataset contributes to novel methodology development in medical image segmentation in recent years. We reviewed sixteen papers that used the LiTS dataset for method development and evaluation from three sources: (a)


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 16 -->


Bilic et al. Page 16


Journal of Medical Image Analysis (MIA), (b) MICCAI conference proceeding, and (c) IEEE Transaction on Medical Imaging (TMI), as shown in Table 10.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


A significant advance was on the 3D deep learning model besides the 2D approaches. Zhou et al. (2021b), Haghighi et al. (2021) proposed self-supervised pre-training frameworks to initialize 3D models for better representation than training them from scratch. Isensee et al. (2020) proposed a self-configuring pipeline to facilitate the model training and the automated design of network architecture. Wang et al. (2019) added a 3D attention module for 3D segmentation models. These works improved the efficiency of 3D models and popularized the 3D models in many image segmentation tasks (Ma, 2021).


Ma et al. (2020) focused on the special trait of liver and liver tumor segmentation and proposed a novel active contour-based loss function to preserve the segmentation boundary. Similarly, Tang et al. (2020) proposed to enhance edge information and cross-feature fusion for liver and tumor segmentation. Shirokikh et al. (2020) considered the varying lesion sizes and proposed a loss reweighting strategy to deal with size imbalance in tumor segmentation. Wang et al. (2020) attempted to deal with the heterogeneous image resolution with a multi-branch decoder.


One emerging trend was leveraging available sparse labeled images to perform multi-organ segmentation. Huang et al. (2020) attempted to perform co-training of single-organ datasets (liver, kidney, and pancreas). Fang and Yan (2020) proposed a pyramid-input and pyramidoutput network to condense multi-scale features to reduce the semantic gaps. Finally, Yan et al. (2020) developed a universal lesion detection algorithm to detect a variety of lesions in CT images in a multitask fashion and propose strategies to mine missing annotations from partially-labeled datasets.


## 4.4.1. Remaining challenges


Segmentation performance w.r.t. lesion size.: Overall, the submitted methods performed very well for large liver tumors but struggled to segment smaller tumors (see Fig. 8). Many small tumors only have diameters of a few voxels; further, the image resolution is relatively high with 512 × 512 pixels in axial slices. Therefore, detecting such small structures is difficult due to the small number of potentially differing surrounding pixels, which can indicate a potential tumor border (see Fig. 8). It is exacerbated by the considerable noise and artifacts in medical imaging, which occur from size similarity; texture differences from the surrounding liver tissue and their arbitrary shapes are difficult to distinguish from an actual liver tumor. Overall, state-of-the-art methods performed well on volumes with large tumors and worse on volumes with small tumors. Worst results were achieved in exams where single small tumors (<10 mm3) occur. Best results were achieved when volumes showed less than six tumors with an overall tumor volume above 40 mm3 (see Fig. 8). In the appendix, we show the performance of all submitted methods of the three LiTS challenges, compared for every test volume, clustered by the number of tumor appearances and tumor sizes, see Fig. A.10.


Segmentation performance w.r.t. image contrast.: Another important influence of the methods’ segmentation quality was the difference in tumor and liver HU values. Current


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 17 -->


Bilic et al. Page 17


state-of-the-art methods perform best for volumes showing higher contrast between liver and tumor. Especially in the case of focal lesions with a density 40–60 HU higher than that of the background liver (see Fig. 8). Worst results are achieved in cases where the contrast is below 20 HU (see Fig. 8), including tumors having a lower density than the liver. An average difference in HU values eases the network’s task of distinguishing liver and tumor since a simple threshold-derived rule could be applied as part of the decision process. Interestingly, an even more significant difference value did not result in an even better segmentation.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


The performance of all submitted methods of three LiTS challenges was compared for every test volume, clustered by the HU level difference between liver and tumor and the HU level difference within tumor ROIs, shown in appendix Fig. B.11.


## 5. Discussion


## 5.1. Limitations


The datasets were annotated by only one rater from each medical center. Thus it may introduce label bias, especially for small lesion segmentation, which is only ambiguous. However, further quality control of the annotations with consensus can reduce label noise and benefit supervised training and method evaluation. The initial rankings were conducted considering only the Dice score in which the large tissue will dominate. We observe that solely using Dice does not distinguish the top-performing teams but combining multiple metrics can do better. Unfortunately, imaging information (e.g., scanner type) and demographic information are unavailable when collecting the data from multiple centers. However, they are essential for in-depth analysis and further development of the challenge result (Maier-Hein et al., 2020; Wiesenfarth et al., 2021). The BIAS (Maier-Hein et al., 2020) report has proven to provide a good guideline for organizing a challenge and analyzing the outcome of the challenge. Tumor detection task is of clinical relevance, and the detection metric should be considered in future challenges (see Fig. 9).


To allow for quick evaluation of the submissions, we release the test data to the participant. Hence, we cannot prevent potential over-fitting behavior by multiple iterative submissions or cheating behavior (e.g., manual correction of the segmentation). One option to improve this is using image containers (such as Docker6 and Singularity7) without releasing the test images. However, this would potentially limit the popularity of the challenge.


## 5.2. Future work


Organizing LiTS has taught us lessons relevant for future medical segmentation benchmark challenges and their organizers. Given that many of the algorithms in this study offered good liver segmentation results compared to tumors, it seems valuable to evaluate liver tumor segmentation based on their different size, type, and occurrence per volume. Generating large labeled datasets is time-consuming and costly. It might be more efficiently performed


6 https://www.docker.com/ 7 https://sylabs.io/singularity/


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 18 -->


Bilic et al. Page 18


by advanced semiautomated methods, thereby helping to bridge the gap to a fully automated solution.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Further, we recommend providing multiple reference annotations of liver tumors from multiple raters. This is because the segmentation of liver tumors presents high uncertainty due to the small structure and the ambiguous boundary (Schoppe et al., 2020). While most of the segmentation tasks in existing benchmarks are formulated to be one-to-one mapping problems, it does not fully solve the image segmentation problem where the data uncertainty naturally exists. Modeling the uncertainty in segmentation task is a trend8 (Mehta et al., 2020; Zhang et al., 2020b) and would allow the model generates not only one but various plausible outputs. Thus, it would enhance the applicability of automated methods in clinical practice. The released annotated dataset is not limited to benchmarking segmentation tasks but could also serve as data for recent shape modeling methods such as implicit neural functions (Yang et al., 2022; Kuang et al., 2022; Amiranashvili et al., 2021) Considering the size and, importantly, the demographic diversity of the patient populations from the seven institutions that contributed cases in the LiTS benchmark dataset, we think its value and contribution to medical image analysis will be greatly appreciated across numerous directions. One example use case is within the research direction of domain adaptation, where the LiTS dataset can be used to account for the apparent differences/shift of the data distribution due to the domain change (e.g., acquisition setting) (Glocker et al., 2019; Castro et al., 2020). Another recent and intriguing use case is the research direction of federated learning, where the multi-institutional nature of the LiTS benchmark dataset could further contribute to federated learning simulations studies and benchmarks (Sheller et al., 2018, 2020; Rieke et al., 2020; Pati et al., 2021). It will target potential solutions to the LiTS-related tasks without sharing patient data across institutions. We consider federated learning of particular importance, as scientific maturity in this field could lead to a paradigm shift for multi-institutional collaborations. Furthermore, it is overcoming technical, legal, and cultural data sharing concerns since the patient involved in such collaboration will always be retained within their acquiring institutions.


Authors


Patrick Bilic1,a,b, Patrick Christ1,a,b, Hongwei Bran Li1,2,*,b, Eugene Vorontsov3,a,b, Avi Ben-Cohen5,a, Georgios Kaissis10,12,15,a, Adi Szeskin18,a, Colin Jacobs4,a, Gabriel Efrain Humpire Mamani4,a, Gabriel Chartrand26,a, Fabian Lohöfer12,a, Julian Walter Holch29,30,69,a, Wieland Sommer32,a, Felix Hofmann31,32,a, Alexandre Hostettler36,a, Naama Lev-Cohain38,a, Michal Drozdzal34,a, Michal Marianne Amitai35,a, Refael Vivanti37,a, Jacob Sosna38,a, Ivan Ezhov1, Anjany Sekuboyina1,2, Fernando Navarro1,76,78, Florian Kofler1,13,57,78, Johannes C. Paetzold15,16, Suprosanna Shit1, Xiaobin Hu1, Jana Lipková17, Markus Rempfler1, Marie Piraud57,1, Jan Kirschke13, Benedikt Wiestler13, Zhiheng Zhang14, Christian Hülsemeyer1, Marcel Beetz1, Florian Ettlinger1, Michela Antonelli9, Woong Bae73, Míriam Bellver43, Lei Bi61, Hao Chen39, Grzegorz Chlebus62,64, Erik B. Dam72, Qi Dou41, Chi-Wing Fu41, Bogdan Georgescu60, Xavier Giró-i-Nieto45, Felix


8 https://qubiq.grand-challenge.org/Home/


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 19 -->


Bilic et al. Page 19


Gruen28, Xu Han77, Pheng-Ann Heng41, Jürgen Hesser48,49,50, Jan Hendrik Moltz62, Christian Igel72, Fabian Isensee69,70, Paul Jäger69,70, Fucang Jia75, Krishna Chaitanya Kaluva21, Mahendra Khened21, Ildoo Kim73, Jae-Hun Kim53, Sungwoong Kim73, Simon Kohl69, Tomasz Konopczynski49, Avinash Kori21, Ganapathy Krishnamurthi21, Fan Li22, Hongchao Li11, Junbo Li8, Xiaomeng Li40, John Lowengrub66,67,68, Jun Ma54, Klaus Maier-Hein69,70,7, Kevis-Kokitsi Maninis44, Hans Meine62,65, Dorit Merhof74, Akshay Pai72, Mathias Perslev72, Jens Petersen69, Jordi Pont-Tuset44, Jin Qi56, Xiaojuan Qi40, Oliver Rippel74, Karsten Roth47, Ignacio Sarasua51,12, Andrea Schenk62,63, Zengming Shen59,60, Jordi Torres46,43, Christian Wachinger51,12,1, Chunliang Wang42, Leon Weninger74, Jianrong Wu25, Daguang Xu71, Xiaoping Yang55, Simon Chun-Ho Yu58, Yading Yuan52, Miao Yue20, Liping Zhang58, Jorge Cardoso9, Spyridon Bakas19,23,24, Rickmer Braren6,12,30,a, Volker Heinemann33,a, Christopher Pal3,a, An Tang27,a, Samuel Kadoury3,a, Luc Soler36,a, Bram van Ginneken4,a, Hayit Greenspan5,a, Leo Joskowicz18,a, Bjoern Menze1,2,a


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Affiliations


1Department of Informatics, Technical University of Munich, Germany


2Department of Quantitative Biomedicine, University of Zurich, Switzerland


3Ecole Polytechnique de Montréal, Canada


4Department of Medical Imaging, Radboud University Medical Center, Nijmegen, The Netherlands


5Department of Biomedical Engineering, Tel-Aviv University, Israel


6German Cancer Consortium (DKTK), Germany


7Pattern Analysis and Learning Group, Department of Radiation Oncology, Heidelberg University Hospital, Heidelberg, Germany


8Philips Research China, Philips China Innovation Campus, Shanghai, China


9School of Biomedical Engineering & Imaging Sciences, King’s College London, London, UK


10Institute for AI in Medicine, Technical University of Munich, Germany


11Department of Computer Science, Guangdong University of Foreign Studies, China


12Institute for diagnostic and interventional radiology, Klinikum rechts der Isar, Technical University of Munich, Germany


13Institute for diagnostic and interventional neuroradiology, Klinikum rechts der Isar,Technical University of Munich, Germany


14Department of Hepatobiliary Surgery, the Affiliated Drum Tower Hospital of Nanjing University Medical School, China


15Department of Computing, Imperial College London, London, United Kingdom


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 20 -->


Bilic et al. Page 20


16Institute for Tissue Engineering and Regenerative Medicine, Helmholtz Zentrum München, Neuherberg, Germany


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


17Brigham and Women’s Hospital, Harvard Medical School, USA


18School of Computer Science and Engineering, the Hebrew University of Jerusalem, Israel


19Center for Biomedical Image Computing and Analytics (CBICA), University of Pennsylvania, PA, USA


20CGG Services (Singapore) Pte. Ltd., Singapore


21Medical Imaging and Reconstruction Lab, Department of Engineering Design, Indian Institute of Technology Madras, India


22Sensetime, Shanghai, China


23Department of Radiology, Perelman School of Medicine, University of Pennsylvania, USA


24Department of Pathology and Laboratory Medicine, Perelman School of Medicine, University of Pennsylvania, PA, USA


25Tencent Healthcare (Shenzhen) Co., Ltd, China


26The University of Montréal Hospital Research Centre (CRCHUM) Montréal, Québec, Canada


27Department of Radiology, Radiation Oncology and Nuclear Medicine, University of Montréal, Canada


28Institute of Control Engineering, Technische Universität Braunschweig, Germany


29Department of Medicine III, University Hospital, LMU Munich, Munich, Germany


30Comprehensive Cancer Center Munich, Munich, Germany


31Department of General, Visceral and Transplantation Surgery, University Hospital, LMU Munich, Germany


32Department of Radiology, University Hospital, LMU Munich, Germany


33Department of Hematology/Oncology & Comprehensive Cancer Center Munich, LMU Klinikum Munich, Germany


34Polytechnique Montréal, Mila, QC, Canada


35Department of Diagnostic Radiology, Sheba Medical Center, Tel Aviv university, Israel


36Department of Surgical Data Science, Institut de Recherche contre les Cancers de l’Appareil Digestif (IRCAD), France


37Rafael Advanced Defense System, Israel


38Department of Radiology, Hadassah University Medical Center, Jerusalem, Israel


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 21 -->


Bilic et al. Page 21


39Department of Computer Science and Engineering, The Hong Kong University of Science and Technology, China


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


40Department of Electrical and Electronic Engineering, The University of Hong Kong, China


41Department of Computer Science and Engineering, The Chinese University of Hong Kong, Hong Kong, China


42Department of Biomedical Engineering and Health Systems, KTH Royal Institute of Technology, Sweden


43Barcelona Supercomputing Center, Barcelona, Spain


44Eidgenössische Technische Hochschule Zurich (ETHZ), Zurich, Switzerland


45Signal Theory and Communications Department, Universitat Politecnica de Catalunya, Catalonia, Spain


46Universitat Politecnica de Catalunya, Catalonia, Spain


47University of Tuebingen, Germany


48Mannheim Institute for Intelligent Systems in Medicine, department of Medicine Mannheim, Heidelberg University, Germany


49Interdisciplinary Center for Scientific Computing (IWR), Heidelberg University, Germany


50Central Institute for Computer Engineering (ZITI), Heidelberg University, Germany


51Department of Child and Adolescent Psychiatry, Ludwig-Maximilians-Universität, Munich, Germany


52Department of Radiation Oncology, Icahn School of Medicine at Mount Sinai, NY, USA


53Department of Radiology, Samsung Medical Center, Sungkyunkwan University School of Medicine, South Korea


54Department of Mathematics, Nanjing University of Science and Technology, China


55Department of Mathematics, Nanjing University, China


56School of Information and Communication Engineering, University of Electronic Science and Technology of China, China


57Helmholtz AI, Helmholtz Zentrum München, Neuherberg, Germany


58Department of Imaging and Interventional Radiology, Chinese University of Hong Kong, Hong Kong, China


59Beckman Institute, University of Illinois at Urbana-Champaign, USA


60Siemens Healthineers, USA


61School of Computer Science, the University of Sydney, Australia


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 22 -->


Bilic et al. Page 22


62Fraunhofer MEVIS, Bremen, Germany


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


63Institute for Diagnostic and Interventional Radiology, Hannover Medical School, Hannover, Germany


64Diagnostic Image Analysis Group, Radboud University Medical Center, Nijmegen, The Netherlands


65Medical Image Computing Group, FB3, University of Bremen, Germany


66Departments of Mathematics, Biomedical Engineering, University of California, Irvine, USA


67Center for Complex Biological Systems, University of California, Irvine, USA


68Chao Family Comprehensive Cancer Center, University of California, Irvine, USA


69Division of Medical Image Computing, German Cancer Research Center (DKFZ), Heidelberg, Germany


70Helmholtz Imaging, Germany


71NVIDIA, Santa Clara, CA, USA


72Department of Computer Science, University of Copenhagen, Denmark


73Kakao Brain, Republic of Korea


74Institute of Imaging & Computer Vision, RWTH Aachen University, Germany


75Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, China


76Department of Radiation Oncology and Radiotherapy, Klinikum rechts der Isar, Technical University of Munich, Germany


77Department of computer science, UNC Chapel Hill, USA


78TranslaTUM - Central Institute for Translational Cancer Research, Technical University of Munich, Germany


Acknowledgments


Bjoern Menze is supported through the DFG funding (SFB 824, subproject B12) and a Helmut-HortenProfessorship for Biomedical Informatics by the Helmut-Horten-Foundation. Florian Kofler is Supported by Deutsche Forschungsgemeinschaft (DFG) through TUM International Graduate School of Science and Engineering (IGSSE), GSC 81. An Tang was supported by the Fonds de recherche du Québec en Santé and Fondation de l’association des radiologistes du Québec (FRQS-ARQ 34939 Clinical Research Scholarship – Junior 2 Salary Award). Hongwei Bran Li is supported by Forschungskredit (Grant NO. FK-21-125) from University of Zurich. We thank the CodaLab team, especially Eric Carmichael and Flavio Alexander for helping us with the setup.


Data availability


Data are publicly available.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 23 -->


Bilic et al. Page 23


Appendix


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Appendix A. Segmentation performance w.r.t tumor size and number of


tumors.


See Fig. A.10.


Fig. A.10. Performance w.r.t tumor size and number of tumors. The test dataset is clustered by the number of tumors (#T) and size of the largest tumor per volume. Overall, participating methods perform well on volumes with large tumors and worse for volumes with small tumors. Worst results are achieved in chase where single small tumors (<15 mm3) occur. Best results are achieved when volumes show less than 6 tumors with an overall tumor volume above 40 mm3.


Appendix B. Segmentation performance w.r.t. HU value differences.


See Fig. B.11.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 24 -->


Bilic et al. Page 24


Appendix C. Correspondence algorithm


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Components may not necessarily have a one-to-one correspondence between the two masks. For example, a single reference component can be predicted as multiple components (split error); similarly, multiple reference components can be covered by a single significant predicted component (merge error), as shown in Fig. C.12.


Fig. B.11. Performance w.r.t HU value difference between tumor and non-tumor liver tissue. Two robust metrics are calculated to cluster the results on the test set. First, the HU value difference between liver and tumor is calculated using both regions’ robust median absolute deviation per volume. Further, the clusters are split up by the tumor HU value difference calculated by the difference of the 90th percentile and 10th percentile. Participating methods perform best for volumes showing higher contrast between liver and tumor. Especially in the case of the liver, HU values are 40–60 points higher than the liver. Worst results are achieved in cases where the contrast is below 20 HU value, including tumors having a lower HU value than the liver.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 25 -->


Bilic et al. Page 25


Once connected components are found and enumerated in the reference and prediction masks, the correspondence algorithm determines the mapping between reference and prediction. Consider NR connected components in the reference mask and NP in the prediction mask. First, the many-to-many mapping is turned into a many-to-one mapping by merging all reference components ri(i ∈NR) that are connected by a single predicted component pj(j ∈NP), as shown in Fig. C.13 (left). In the case where an ri overlaps multiple


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


pj, the pj with the largest total intersected area is used. Thus, for every index i ∈NR, a corresponding ji ∈NP is determined as:


∀i ∈NR, ji = arg maxjpj ∩ri, pj ∩ri > 0


## (C.1)


none, else


and the ri are merged to ρj according to:


ρj = ⋂


ri, (C.2)


i:ji = j


resulting in Nρ = ∣{ρj} ∣ regions. Any ri without a corresponding pj is a false negative.


Fig. C.12. Split and merge errors where a prediction splits a reference lesion into more than one connected component or merges multiple reference components into one, respectively. Reference connected components are shown with a solid color and predicted as regions with a dashed boundary and hatched interior. One-to-one correspondence is shown in green. Oneto-two (a), two-to-one (b), and two-to-three (c) correspondence in orange. False negative in gray.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 26 -->


Bilic et al. Page 26


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. C.13. Two examples (top and bottom) of the process to establish a correspondence between connected components in the reference and prediction masks. Reference: solid color; prediction: dashed boundary and hatched interior. Left: reference components merged if the same predicted component overlaps them. Right: predicted components are merged together if the same merged reference component overlaps them. Corresponding reference and predicted components share the same color (green, orange). An undetected reference component is shown in solid gray. During the merge of reference components (left), predicted components that do not have the most significant overlap with a reference component are left unmatched (gray, dashed, and hatched). Their mapping is completed during the merge of predicted components (right).


In the second step, the mapping is completed by associating each remaining pj with a single


ρk (k ∈Nρ) with which it shares the largest total intersected area and merging all the pj that share the same ρk, as shown in Fig. C.13 (right). Thus, for every index j ∈NP, a


corresponding k ∈Nρ is determined as:


∀j ∈NP, kj = arg maxkpj ∩ρk, pj ∩ρk > 0


and the pj are merged to πk according to:


## (C.3)


none, else


πk = ⋂


pj, (C.4)


j:kj = k


resulting in Nπ = ∣{πk} ∣ regions. Any pj without a corresponding ri is a false positive.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 27 -->


Bilic et al. Page 27


The result is a map with a correspondence between sets of predicted components and sets of reference components. In order to maintain the immutability of the reference, any metrics evaluated on a set of merged reference components are attributed to each constituent reference component. For example, if two connected components in the reference mask are merged, and a Dice score of 0.7 is computed on the mask combining both components, then each component is considered to have a Dice score of 0.7. If the reference components were not merged, the errors computed for each of the two components would be exaggerated (e.g., 0.3 and 0.5 Dice).


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Appendix D. Automated tumor burden analysis in MICCAI-LiTS 2017


Motivation.


The tumor burden, defined as the liver/tumor ratio, plays an essential role in surgical resection planning (Nordlinger et al., 1996; Jagannath et al., 1986). Instead of measuring diameters of target tumors, a fully volumetric segmentation of both the liver and its tumor and the subsequent tumor burden analysis offers valuable insights into the disease progression (Blachier et al., 2013). Further, tumor burden is also essential in assessing the effectiveness of different treatments and can potentially replace the RECIST protocol (Gobbi et al., 2004; Bornemann et al., 2007; Heussel et al., 2007; Kuhnigk et al., 2006; Puesken et al., 2010; Bauknecht et al., 2010). A fully automated liver and tumor segmentation allows more straightforward computation of tumor burden and simplifies surgical liver resection planning.


Table D.11


Tumor burden ranking in MICCAI-LiTS 2017.


Ranking Ref. name Institution RMSE Max error


## 1 C. Li et al. CUHK 0.015 (1) 0.062 (6)


## 2 J. Wu et al. NJU 0.016 (2) 0.048 (2)


## 3 C. Wang et al. KTH 0.016 (3) 0.058 (4)


## 4 Y. Yuan et al. MSSM 0.017 (4) 0.049 (3)


## 5 J. Zou et al. Lenovo 0.017 (5) 0.045 (1)


## 6 K. Kaluva et al. Predible Health 0.020 (6) 0.090 (12)


## 7 X. Han et al. Elekta Inc. 0.020 (7) 0.080 (10)


## 8 A. Ben-Cohen et al. Uni Tel Aviv 0.020 (8) 0.070 (7)


## 9 G. Chlebus et al. Fraunhofer 0.020 (9) 0.070 (8)


## 10 L. Zhang et al. CUHK 0.022 (10) 0.074 (11)


## 11 E. Vorontsov et al. MILA 0.023 (11) 0.112 (13)


## 12 J. Lipkova et al. TUM 0.030 (12) 0.140 (14)


## 13 K. Roth et al. Volume Graphics 0.030 (13) 0.180 (15)


## 14 M. Piraud et al. TUM 0.037 (14) 0.143 (16)


## 15 Jin Qi 0.0420 (12) 0.0330 (2)


## 16 L. Bi et al. Uni Sydney 0.170 (15) 0.074 (9)


## 17 J. Ma et al. NJUST 0.920 (16) 0.061 (5)


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 28 -->


Bilic et al. Page 28


Metrics.


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


The tumor burden of the liver is a measure of the fraction of the liver afflicted by cancer. As a metric, we measure the root mean square error (RMSE) in tumor burden estimates from lesion predictions.


n


## 2 (D.1)


RMSE = 1 n ∑


Ai −Bi


i = 1


Results.


The tumor burden was well predicted by many methods, with the best-performing method achieving the lowest RMSE of 0.015 and the lowest maximum error at 0.033 (Table D.11). There was a slight variation in RMSE values by the last. 15th method still obtains the fifth rank due to the high number of duplicates in the low range of values. In overall, methods achieving high Dice per case scores also obtained lower RMSE values. Only small correlation exists between RMSE and the maximum error ranking.


## References


Abdel-massieh NH, Hadhoud MM, Amin KM, 2010. Fully automatic liver tumor segmentation


from abdominal CT scans. In: Computer Engineering and Systems (ICCES), 2010 International Conference on. IEEE, pp. 197–202. Albain KS, Swann RS, Rusch VW, Turrisi AT, Shepherd FA, Smith C, Chen Y, Livingston RB, Feins


RH, Gandara DR, et al. , 2009. Radiotherapy plus chemotherapy with or without surgical resection for stage III non-small-cell lung cancer: A phase III randomised controlled trial. Lancet 374 (9687), 379–386. [PubMed: 19632716] Amiranashvili T, Lüdke D, Li H, Zachow S, et al., 2021. Learning shape reconstruction from sparse


measurements with neural implicit functions. In: Medical Imaging with Deep Learning. Antonelli M, Reinke A, Bakas S, Farahani K, Kopp-Schneider A, Landman BA, Litjens G, Menze B,


Ronneberger O, Summers RM, et al. , 2022. The medical segmentation decathlon. Nature Commun. 13 (1), 1–13. [PubMed: 34983933] Bauknecht H-C, Romano VC, Rogalla P, Klingebiel R, Wolf C, Bornemann L, Hamm B, Hein PA,


2010. Intra-and interobserver variability of linear and volumetric measurements of brain metastases using contrast-enhanced magnetic resonance imaging. Invest. Radiol 45 (1), 49–56. [PubMed: 19996757] Ben-Dan I, Shenhav E, 2008. Liver tumor segmentation in CT images using probabilistic methods. In:


MICCAI Workshop, vol. 41, p. 43. Blachier M, Leleu H, Peck-Radosavljevic M, Valla D-C, Roudot-Thoraval F, 2013. The burden of


liver disease in Europe: A review of available epidemiological data. J. Hepatol 58 (3), 593–608. [PubMed: 23419824] Bornemann L, Dicken V, Kuhnigk J-M, Wormanns D, Shin H-O, Bauknecht H-C, Diehl V, Fabel M,


Meier S, Kress O, et al. , 2007. Oncotreat: A software assistant for cancer therapy monitoring. Int. J. Comput. Assist. Radiol. Surg 1 (5), 231–242. Cano-Espinosa C, González G, Washko GR, Cazorla M, Estépar RSJ, 2020. Biomarker localization


from deep learning regression networks. IEEE Trans. Med. Imaging 39 (6), 2121–2132. [PubMed: 31940523] Castro DC, Walker I, Glocker B, 2020. Causality matters in medical imaging. Nature Commun. 11 (1),


1–10. [PubMed: 31911652]


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 29 -->


Bilic et al. Page 29


Chlebus G, Schenk A, Moltz JH, van Ginneken B, Hahn HK, Meine H, 2018. Automatic liver tumor


segmentation in CT with fully convolutional neural networks and object-based postprocessing. Sci. Rep 8 (1), 1–7. [PubMed: 29311619] Christ P, Elshaer MEA, Ettlinger F, Tatavarty S, Bickel M, Bilic P, Rempfler M, Armbruster M,


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Hofmann F, D’Anastasi M, Sommer WH, Ahmadi S-A, Menze BH, 2016. Automatic liver and lesion segmentation in CT using cascaded fully convolutional neural networks and 3D conditional random fields. In: Medical Image Computing and Computer-Assisted Intervention – MICCAI 2016: 19th International Conference. pp. 415–423. Ciecholewski M, Ogiela MR, 2007. Automatic segmentation of single and multiple neoplastic hepatic


lesions in CT images. In: International Work-Conference on the Interplay Between Natural and Artificial Computation. Springer, pp. 63–71. Cleary K., 2017. MIDAS - original datasets. http://insight-journal.org/midas/item/view/1346.


(Accessed 01 December 2019). Conze P-H, Noblet V, Rousseau F, Heitz F, De Blasi V, Memeo R, Pessaux P, 2017. Scale-adaptive


supervoxel-based random forests for liver tumor segmentation in dynamic contrast-enhanced CT scans. Int. J. Comput. Assist. Radiol. Surg 12 (2), 223–233. [PubMed: 27771843] Cootes TF, Taylor CJ, Cooper DH, Graham J, 1995. Active shape models-their training and


application. Comput. Vis. Image Underst 61 (1), 38–59. Dawant BM, Li R, Lennon B, Li S, 2007. Semi-automatic segmentation of the liver and its evaluation


on the MICCAI 2007 grand challenge data set. 3D Segm. Clin.: Grand Chall 215–221. Deng X, Du G, 2008. 3D segmentation in the clinic: A grand challenge II-liver tumor segmentation. In:


MICCAI Workshop. Dou Q, Chen H, Jin Y, Yu L, Qin J, Heng P-A, 2016. 3D deeply supervised network for automatic


liver segmentation from ct volumes. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, pp. 149–157. Eisenhauer E, Therasse P, Bogaerts J, Schwartz L, Sargent D, Ford R, Dancey J, Arbuck S, Gwyther


S, Mooney M, et al. , 2009. New response evaluation criteria in solid tumours: Revised RECIST guideline (version 1.1). Eur. J. Cancer 45 (2), 228–247. [PubMed: 19097774] Erickson B, Kirk S, Lee Y, Bathe O, Kearns M, Gerdes C, Rieger-Christ K, Lemmerman J, 2016.


Radiology data from the cancer genome atlas liver hepatocellular carcinoma [TCGA-LIHC] collection. Cancer Imaging Arch.. Fang X, Yan P, 2020. Multi-organ segmentation over partially labeled datasets with multi-scale feature


abstraction. IEEE Trans. Med. Imaging 39 (11), 3619–3629. [PubMed: 32746108] Glocker B, Robinson R, Castro DC, Dou Q, Konukoglu E, 2019. Machine learning with multi


site imaging data: An empirical study on the impact of scanner effects. arXiv preprint arXiv:1910.04597. Gobbi PG, Broglia C, Di Giulio G, Mantelli M, Anselmo P, Merli F, Zinzani PL, Rossi G, Callea V,


Iannitto E, et al. , 2004. The clinical value of tumor burden at diagnosis in Hodgkin lymphoma. Cancer: Interdiscipl. Int. J. Am. Cancer Soc 101 (8), 1824–1834. Haghighi F, Taher MRH, Zhou Z, Gotway MB, Liang J, 2020. Learning semantics-enriched


representation via self-discovery, self-classification, and self-restoration. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, pp. 137– 147. Haghighi F, Taher MRH, Zhou Z, Gotway MB, Liang J, 2021. Transferable visual words: Exploiting


the semantics of anatomical patterns for self-supervised learning. IEEE Trans. Med. Imaging. Häme Y., 2008. Liver tumor segmentation using implicit surface evolution. Midas J. 1–10. Hann LE, Winston CB, Brown KT, Akhurst T, 2000. Diagnostic imaging approaches and relationship


to hepatobiliary cancer staging and therapy. In: Seminars in Surgical Oncology, vol. 19, (no. 2), Wiley Online Library, pp. 94–115. [PubMed: 11126385] Heimann T, Münzing S, Meinzer H-P, Wolf I, 2007. A shape-guided deformable model with


evolutionary algorithm initialization for 3D soft tissue segmentation. In: Information Processing in Medical Imaging. Springer, pp. 1–12. Heimann T, Van Ginneken B, Styner M, Arzhaeva Y, Aurich V, Bauer C, Beck A, Becker C, Beichel


R, Bekes G, Bello F, Binnig G, Bischof H, Bornik A, Cashman P, Chi Y, Córdova A, Dawant B,


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 30 -->


Bilic et al. Page 30


Fidrich M, Furst J, Furukawa D, Grenacher L, Hornegger J, Kainmüller D, Kitney R, Kobatake H, Lamecker H, Lange T, Lee J, Lennon B, Li R, Li S, Meinzer H, Németh G, Raicu D, Rau A, Van Rikxoort E, Rousson M, Ruskó L, Saddi K, Schmidt G, Seghers D, Shimizu A, Slagmolen P, Sorantin E, Soza G, Susomboon R, Waite J, Wimmer A, Wolf I, 2009. Comparison and evaluation of methods for liver segmentation from CT datasets. IEEE Trans. Med. Imaging 28 (8), 1251– 1265. [PubMed: 19211338] Heimann T, Wolf I, Meinzer H-P, 2006. Active shape models for a fully automated 3D segmentation


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


of the liver–an evaluation on clinical data. In: Medical Image Computing and Computer-Assisted Intervention–MICCAI 2006. Springer, pp. 41–48. Heussel CP, Meier S, Wittelsberger S, Götte H, Mildenberger P, Kauczor H-U, 2007. Follow-up CT


measurement of liver malignoma according to RECIST and WHO vs. volumetry. RoFo: Fortschr. Geb. Rontgenstr. Nuklearmed 179 (9), 958–964. [PubMed: 17594629] Hu P, Wu F, Peng J, Liang P, Kong D, 2016. Automatic 3D liver segmentation based on deep learning


and globally optimized surface evolution. Phys. Med. Biol 61 (24), 8676. [PubMed: 27880735] Huang R, Zheng Y, Hu Z, Zhang S, Li H, 2020. Multi-organ segmentation via co-training weight


averaged models from few-organ datasets. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, pp. 146–155. Isensee F, Jaeger PF, Kohl SA, Petersen J, Maier-Hein KH, 2020. Nnu-Net: A self-configuring


method for deep learning-based biomedical image segmentation. Nature Methods 1–9. [PubMed: 31907477] Jagannath S, Velasquez WS, Tucker SL, Fuller LM, McLaughlin PW, Manning JT, North LB,


Cabanillas FC, 1986. Tumor burden assessment and its implication for a prognostic model in advanced diffuse large-cell lymphoma. J. Clin. Oncol 4 (6), 859–865. [PubMed: 2423653] Jiménez Carretero D, Fernández de Manuel L, Pascau González Garzón J, Tellado JM, Ramon E,


Desco Menéndez M, Santos A, Ledesma Carbayo MJ, 2011. Optimal multiresolution 3D level-set method for liver segmentation incorporating local curvature constraints. Kainmüller D, Lange T, Lamecker H, 2007. Shape constrained automatic segmentation of the liver


based on a heuristic intensity model. In: Proc. MICCAI Workshop 3D Segmentation in the Clinic: A Grand Challenge. pp. 109–116. Kass M, Witkin A, Terzopoulos D, 1988. Snakes: Active contour models. Int. J. Comput. Vis 1 (4),


321–331. Kavur AE, Gezer NS, Barış M, Aslan S, Conze P-H, Groza V, Pham DD, Chatterjee S, Ernst P, Özkan


S, et al. , 2021. CHAOS challenge-combined (CT-MR) healthy abdominal organ segmentation. Med. Image Anal 69, 101950. [PubMed: 33421920] Kuang K, Zhang L, Li J, Li H, Chen J, Du B, Yang J, 2022. What makes for automatic reconstruction


of pulmonary segments. arXiv preprint arXiv:2207.03078. Kuhnigk J-M, Dicken V, Bornemann L, Bakai A, Wormanns D, Krass S, Peitgen H-O, 2006.


Morphological segmentation and partial volume analysis for volumetry of solid pulmonary lesions in thoracic CT scans. IEEE Trans. Med. Imaging 25 (4), 417–434. [PubMed: 16608058] Lamecker H, Lange T, Seebass M, 2004. Segmentation of the Liver using a 3D Statistical Shape


Model. Konrad-Zuse-Zentrum für Informationstechnik Berlin. Li X, Chen H, Qi X, Dou Q, Fu C-W, Heng P-A, 2018a. H-DenseUNet: Hybrid densely connected


unet for liver and tumor segmentation from CT volumes. IEEE Trans. Med. Imaging 37 (12), 2663–2674. [PubMed: 29994201] Li Y, Hara S, Shimura K, 2006. A machine learning approach for locating boundaries of liver tumors


in ct images. In: Null. IEEE, pp. 400–403. Li H, Jiang G, Zhang J, Wang R, Wang Z, Zheng W-S, Menze B, 2018b. Fully convolutional network


ensembles for white matter hyperintensities segmentation in MR images. NeuroImage 183, 650– 665. [PubMed: 30125711] Ling H, Zhou SK, Zheng Y, Georgescu B, Suehling M, Comaniciu D, 2008. Hierarchical, learning


based automatic liver segmentation. In: Computer Vision and Pattern Recognition, 2008. CVPR 2008. IEEE Conference on. IEEE, pp. 1–8.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 31 -->


Bilic et al. Page 31


Linguraru MG, Richbourg WJ, Liu J, Watt JM, Pamulapati V, Wang S, Summers RM, 2012. Tumor


burden analysis on computed tomography by automated liver and tumor segmentation. Med. Imaging, IEEE Trans 31 (10), 1965–1976. Litjens G, Kooi T, Bejnordi BE, Setio AAA, Ciompi F, Ghafoorian M, van der Laak JA, van Ginneken


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


B, Sánchez CI, 2017. A survey on deep learning in medical image analysis. arXiv preprint arXiv:1702.05747. Lu F, Wu F, Hu P, Peng Z, Kong D, 2017. Automatic 3D liver location and segmentation via


convolutional neural network and graph cut. Int. J. Comput. Assist. Radiol. Surg 12 (2), 171–182. [PubMed: 27604760] Ma J., 2021. Cutting-edge 3D medical image segmentation methods in 2020: Are happy families all


alike? arXiv preprint arXiv:2101.00232. Ma J, He J, Yang X, 2020. Learning geodesic active contours for embedding object global information


in segmentation cnns. IEEE Trans. Med. Imaging Maier-Hein L, Reinke A, Kozubek M, Martel AL, Arbel T, Eisenmann M, Hanbury A, Jannin P,


Müller H, Onogur S, et al. , 2020. BIAS: Transparent reporting of biomedical image analysis challenges. Med. Image Anal 66, 101796. [PubMed: 32911207] Massoptier L, Casciaro S, 2007. Fully automatic liver segmentation through graph-cut technique.


In: Engineering in Medicine and Biology Society, 2007. EMBS 2007. 29th Annual International Conference of the IEEE. IEEE, pp. 5243–5246. Massoptier L, Casciaro S, 2008. A new fully automatic and robust algorithm for fast segmentation of


liver tissue and tumors from CT scans. Eur. Radiol.s 18 (8), 1658. McKnight PE, Najab J, 2010. Mann-whitney u test. In: The Corsini Encyclopedia of Psychology.


Wiley Online Library, p. 1. Mehta R, Filos A, Gal Y, Arbel T, 2020. Uncertainty evaluation metric for brain tumour segmentation.


arXiv preprint arXiv:2005.14262. Milletari F, Navab N, Ahmadi S-A, 2016. V-net: Fully convolutional neural networks for volumetric


medical image segmentation. In: 2016 Fourth International Conference on 3D Vision. 3DV, IEEE, pp. 565–571. Moghbel M, Mashohor S, Mahmud R, Saripan MIB, 2017. Review of liver segmentation and computer


assisted detection/diagnosis methods in computed tomography. Artif. Intell. Rev 1–41. Moltz JH, Bornemann L, Dicken V, Peitgen H, 2008. Segmentation of liver metastases in CT scans by


adaptive thresholding and morphological processing. In: MICCAI Workshop, vol. 41, (no. 43), p. 195. Moltz JH, Bornemann L, Kuhnigk J-M, Dicken V, Peitgen E, Meier S, Bolte H, Fabel M, Bauknecht


H-C, Hittinger M, et al. , 2009. Advanced segmentation techniques for lung nodules, liver metastases, and enlarged lymph nodes in CT scans. IEEE J. Sel. Top. Sign. Proces 3 (1), 122–134. Nordlinger B, Guiguet M, Vaillant J-C, Balladur P, Boudjema K, Bachellier P, Jaeck D, 1996. Surgical


resection of colorectal carcinoma metastases to the liver: A prognostic scoring system to improve case selection, based on 1568 patients. Cancer: Interdiscipl. Int. J. Am. Cancer Soc 77 (7), 1254– 1262. Nugroho HA, Ihtatho D, Nugroho H, 2008. Contrast enhancement for liver tumor identification. In:


MICCAI Workshop, vol. 41, (no. 43), p. 201. Osher S, Sethian JA, 1988. Fronts propagating with curvature-dependent speed: Algorithms based on


Hamilton-Jacobi formulations. J. Comput. Phys 79 (1), 12–49. Park H, Bland PH, Meyer CR, 2003. Construction of an abdominal probabilistic atlas and its


application in segmentation. IEEE Trans. Med. Imaging 22 (4), 483–492. [PubMed: 12774894] Pati S, Baid U, Zenk M, Edwards B, Sheller M, Reina GA, Foley P, Gruzdev A, Martin J,


Albarqouni S, et al. , 2021. The federated tumor segmentation (FeTS) challenge. arXiv preprint arXiv:2105.05874. Puesken M, Buerke B, Gerss J, Frisch B, Beyer F, Weckesser M, Seifarth H, Heindel W, Wessling


J, 2010. Prediction of lymph node manifestations in malignant lymphoma: Significant role of volumetric compared with established metric lymph node analysis in multislice computed tomography. J. Comput. Assist. Tomogr 34 (4), 564–569. [PubMed: 20657226]


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 32 -->


Bilic et al. Page 32


Rey D, Neuhäuser M, 2011. Wilcoxon-signed-rank test. In: International Encyclopedia of Statistical


Science. Springer, pp. 1658–1659. Rieke N, Hancox J, Li W, Milletari F, Roth HR, Albarqouni S, Bakas S, Galtier MN, Landman BA,


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Maier-Hein K, et al. , 2020. The future of digital health with federated learning. NPJ Digit. Med 3 (1), 1–7. [PubMed: 31934645] Ronneberger O, Fischer P, Brox T, 2015. U-Net: Convolutional networks for biomedical image


segmentation. In: MICCAI, vol. 9351. pp. 234–241. Saddi KA, Rousson M, Chefd’hotel C, Cheriet F, 2007. Global-to-local shape matching for liver


segmentation in CT imaging. In: Proceedings of MICCAI Workshop on 3D Segmentation in the Clinic: A Grand Challenge. pp. 207–214. Schoppe O, Pan C, Coronel J, Mai H, Rong Z, Todorov MI, Müskes A, Navarro F, Li H, Ertürk A,


et al. , 2020. Deep learning-enabled multi-organ segmentation in whole-body mouse scans. Nature Commun. 11 (1), 1–14. [PubMed: 31911652] Sheller MJ, Edwards B, Reina GA, Martin J, Pati S, Kotrotsou A, Milchenko M, Xu W, Marcus


D, Colen RR, et al. , 2020. Federated learning in medicine: Facilitating multi-institutional collaborations without sharing patient data. Sci. Rep 10 (1), 1–12. [PubMed: 31913322] Sheller MJ, Reina GA, Edwards B, Martin J, Bakas S, 2018. Multi-institutional deep learning


modeling without sharing patient data: A feasibility study on brain tumor segmentation. In: International MICCAI Brainlesion Workshop. Springer, pp. 92–104. Shiina S, Sato K, Tateishi R, Shimizu M, Ohama H, Hatanaka T, Takawa M, Nagamatsu H, Imai


Y, 2018. Percutaneous ablation for hepatocellular carcinoma: Comparison of various ablation techniques and surgery. Canad. J. Gastroenterol. Hepatol 2018. Shimizu A, Narihira T, Furukawa D, Kobatake H, Nawano S, Shinozaki K, 2008. Ensemble


segmentation using AdaBoost with application to liver lesion extraction from a CT volume. In: Proc. MICCAI Workshop on 3D Segmentation in the Clinic: A Grand Challenge II. NY, USA. Shirokikh B, Shevtsov A, Kurmukov A, Dalechina A, Krivov E, Kostjuchenko V, Golanov A, Belyaev


M, 2020. Universal loss reweighting to balance lesion size inequality in 3D medical image segmentation. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, pp. 523–532. Slagmolen P, Elen A, Seghers D, Loeckx D, Maes F, Haustermans K, 2007. Atlas based liver


segmentation using nonrigid registration with a B-spline transformation model. In: Proceedings of MICCAI Workshop on 3D Segmentation in the Clinic: A Grand Challenge. pp. 197–206. Smeets D, Stijnen B, Loeckx D, De Dobbelaer B, Suetens P, 2008. Segmentation of liver metastases


using a level set method with spiral-scanning technique and supervised fuzzy pixel classification. In: MICCAI Workshop, vol. 42, p. 43. Soler L, Delingette H, Malandain G, Montagnat J, Ayache N, Koehl C, Dourthe O, Malassagne


B, Smith M, Mutter D, et al. , 2001. Fully automatic anatomical, pathological, and functional segmentation from CT scans for hepatic surgery. Comput. Aided Surg. 6 (3), 131–142. [PubMed: 11747131] Soler L, Hostettler A, Agnus V, Charnoz A, Fasquel J, Moreau J, Osswald A, Bouhadjar M, Marescaux


J, 2010. 3D Image Reconstruction for Comparison of Algorithm Database: A Patient-Specific Anatomical and Medical Image Database. IRCAD, Strasbourg. Tech. Rep. Stewart BW, Wild CP, 2014. World cancer report 2014. In: World Heal. Organ.. Technical Report,


WHO Press, World Health Organization, p. 630. Tang Y, Tang Y, Zhu Y, Xiao J, Summers RM, 2020. Ê Net: An edge enhanced network for accurate


liver and tumor segmentation on CT scans. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, pp. 512–522. Todorov M, Paetzold JC, Schoppe O, Tetteh G, Shit S, Efremov V, Todorov-Völgyi K, Düring M,


Dichgans M, Piraud M, et al. , 2020. Machine learning analysis of whole mouse brain vasculature. Nature Methods 17 (4), 442–449. [PubMed: 32161395] Tomoshige S, Oost E, Shimizu A, Watanabe H, Nawano S, 2014. A conditional statistical shape


model with integrated error estimation of the conditions; Application to liver segmentation in non-contrast CT images. Med. Image Anal 18 (1), 130–143. [PubMed: 24184436]


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 33 -->


Bilic et al. Page 33


Jimenez-del Toro O, Müller H, Krenn M, Gruenberg K, Taha AA, Winterstein M, Eggel I,


Foncubierta-Rodríguez A, Goksel O, Jakab A, et al. , 2016. Cloud-based evaluation of anatomical structure segmentation and landmark detection algorithms: VISCERAL anatomy benchmarks. IEEE Trans. Med. Imaging 35 (11), 2459–2475. [PubMed: 27305669] van Rikxoort E, Arzhaeva Y, van Ginneken B, 2007. Automatic segmentation of the liver in computed


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


tomography scans with voxel classification and atlas matching. In: Proceedings of the MICCAI Workshop. Citeseer, pp. 101–108. Virdis F, Reccia I, Di Saverio S, Tugnoli G, Kwan S, Kumar J, Atzeni J, Podda M, 2019. Clinical


outcomes of primary arterial embolization in severe hepatic trauma: A systematic review. Diagn. Interv. Imaging 100 (2), 65–75. [PubMed: 30555019] Vorontsov E, Abi-Jaoudeh N, Kadoury S, 2014. Metastatic liver tumor segmentation using texture


based omni-directional deformable surface models. In: International MICCAI Workshop on Computational and Clinical Challenges in Abdominal Imaging. Springer, pp. 74–83. Wang S, Cao S, Chai Z, Wei D, Ma K, Wang L, Zheng Y, 2020. Conquering data variations in


resolution: A slice-aware multi-branch decoder network. IEEE Trans. Med. Imaging 39 (12), 4174–4185. [PubMed: 32755853] Wang R, Cao S, Ma K, Zheng Y, Meng D, 2021. Pairwise learning for medical image segmentation.


Med. Image Anal 67, 101876. [PubMed: 33197863] Wang X, Han S, Chen Y, Gao D, Vasconcelos N, 2019. Volumetric attention for 3D medical image


segmentation and detection. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, pp. 175–184. Wang X, Yang J, Ai D, Zheng Y, Tang S, Wang Y, 2015. Adaptive mesh expansion model (AMEM) for


liver segmentation from CT image. PLoS One 10 (3), e0118064. [PubMed: 25769030] Wen J, Zhang X, Xu Y, Li Z, Liu L, 2009. Comparison of AdaBoost and logistic regression


for detecting colorectal cancer patients with synchronous liver metastasis. In: Biomedical and Pharmaceutical Engineering, 2009. ICBPE’09. International Conference on. IEEE, pp. 1–6. Wiesenfarth M, Reinke A, Landman BA, Eisenmann M, Saiz LA, Cardoso MJ, Maier-Hein L, Kopp


Schneider A, 2021. Methods and open-source toolkit for analyzing and visualizing challenge results. Sci. Rep. 11 (1), 1–15. [PubMed: 33414495] Wu W, Zhou Z, Wu S, Zhang Y, 2016. Automatic liver segmentation on volumetric CT images using


supervoxel-based graph cuts. Comput. Math. Methods Med 2016. Xu Z, Burke RP, Lee CP, Baucom RB, Poulose BK, Abramson RG, Landman BA, 2015. Efficient


multi-atlas abdominal segmentation on clinically acquired CT with SIMPLE context learning. Med. Image Anal 24 (1), 18–27. [PubMed: 26046403] Yan K, Cai J, Zheng Y, Harrison AP, Jin D, Tang Y.-b., Tang Y-X, Huang L, Xiao J, Lu L,


2020. Learning from multiple datasets with heterogeneous and partial labels for universal lesion detection in CT. IEEE Trans. Med. Imaging Yang J, Wickramasinghe U, Ni B, Fua P, 2022. ImplicitAtlas: Learning deformable shape templates in


medical imaging. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 15861–15871. Yushkevich PA, Piven J, Hazlett HC, Smith RG, Ho S, Gee JC, Gerig G, 2006. User-guided 3D active


contour segmentation of anatomical structures: significantly improved efficiency and reliability. Neuroimage 31 (3), 1116–1128. [PubMed: 16545965] Zhang F, Dvornek N, Yang J, Chapiro J, Duncan J, 2020a. Layer embedding analysis in convolutional


neural networks for improved probability calibration and classification. IEEE Trans. Med. Imaging 39 (11), 3331–3342. [PubMed: 32356739] Zhang L, Tanno R, Xu M-C, Jacob J, Ciccarelli O, Barkhof F, Alexander DC, 2020b. Disentangling


human error from the ground truth in segmentation of medical images. arXiv preprint arXiv:2007.15963. Zhang X, Tian J, Deng K, Wu Y, Li X, 2010. Automatic liver segmentation using a statistical shape


model with optimal surface detection. IEEE Trans. Biomed. Eng 57 (10), 2622–2626. [PubMed: 20615804] Zhang L, Yu SC-H, 2021. Context-aware PolyUNet for liver and lesion segmentation from abdominal


CT images. arXiv preprint arXiv:2106.11330.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 34 -->


Bilic et al. Page 34


Zhou B, Augenfeld Z, Chapiro J, Zhou SK, Liu C, Duncan JS, 2021a. Anatomyguided multimodal


registration by learning segmentation without ground truth: Application to intraprocedural CBCT/MR liver segmentation and registration. Med. Image Anal 71, 102041. [PubMed: 33823397] Zhou X, Kitagawa T, Hara T, Fujita H, Zhang X, Yokoyama R, Kondo H, Kanematsu M, Hoshi


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


H, 2006. Constructing a probabilistic model for automated liver region segmentation using non-contrast X-ray torso CT images. In: Medical Image Computing and Computer-Assisted Intervention–MICCAI 2006. Springer, pp. 856–863. Zhou Z, Sodha V, Pang J, Gotway MB, Liang J, 2021b. Models genesis. Med. Image Anal 67, 101840.


[PubMed: 33188996]


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 35 -->


Bilic et al. Page 35


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 1. Example from the LiTS dataset depicting a variety of shapes of on contrast-enhanced abdominal CT scans acquired. While most exams in the dataset contain only one lesion, a large group of patients with some (2–7) or many (10–12) lesions, as shown in the histogram calculated over the whole dataset.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 36 -->


Bilic et al. Page 36


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 2. Scatter plots of methods’ performances considering: (a) both segmentation and detection, (b) both distance- and overlap-based metrics for three challenge events. We observe that not all the top-performing methods in three LiTS challenges achieved good scores on tumor detection. The behavior of distance- and overlap-based metrics is similar.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 37 -->


Bilic et al. Page 37


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 3. Inter-rater agreement between the existing annotation and new annotation sets. R1 represented the rater for the existing consensus annotation of the LiTS dataset. R2 reannotated 15 CT scans from scratch. R3 and R4 are board-certified radiologists who checked and corrected the annotations. Specifically, one board-certified radiologist (R3) reviewed and corrected existing annotations. R4 re-evaluated R3’s final annotations and corrected them. The inter-rater agreement was calculated by the Dice score per case between the pairs of two raters.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 38 -->


Bilic et al. Page 38


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 4. Dice and ASD scores of three top-performing teams over the three events.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 39 -->


Bilic et al. Page 39


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 5. Distribution of mean Dice and ASD scores of all submissions in the CodaLab platform from the year 2017 to the year 2022.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 40 -->


Bilic et al. Page 40


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 6. Tumor segmentation results of the ISBI–LiTS 2017 challenge. The reference annotation is marked with green contour, while the prediction is with blue contour. One could observe that the boundary of liver lesion is rather ambiguous.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 41 -->


Bilic et al. Page 41


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 7. Tumor segmentation results of the MICCAI–LiTS 2017 challenge. The reference annotation is marked with green contour, while the prediction is with blue contour. One could observe that it is highly challenging to segment the liver lesion with poor contrast.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 42 -->


Bilic et al. Page 42


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 8. Tumor segmentation results with selected cases of the tumor segmentation analysis regarding low (<20) and high (40–60) HU value difference. Compared are reference annotation (green), best-performing teams from ISBI 2017 (purple), MICCAI 2017 (orange), and MICCAI 2018 (blue). We can observe that a low HU value difference (<20) between tumor and liver tissue poses a challenge for tumor segmentation.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 43 -->


Bilic et al. Page 43


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Fig. 9. Samples of segmentation and detection results for small liver tumor. Compared are reference annotation (green), best-performing teams from ISBI 2017 (purple), MICCAI 2017 (orange), and MICCAI 2018 (blue).


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 44 -->


Bilic et al. Page 44


Overview of publicly available medical datasets of liver and liver tumor images. The LiTS dataset offers a comparably large amount of 3D scans,


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


TCGA-LIHC (Erickson et al., 2016) TCIA ✓ ✓ ✗ 1688 CT, MR, PT


Dataset Institution Liver Tumor Segmentation #Volumes Modality


VISCERAL’16 (Jimenez-del Toro et al., 2016) Uni. of Geneva ✓ ✗ ✓ 60/60 CT/MRI


CHAOS’19 (Kavur et al., 2021) Dokuz Eylul Uni. ✓ ✗ ✓ 40/120 CT/MRI


MIDAS (Cleary, 2017) IMAR ✓ ✓ ✗ 4 CT


3Dircadb-01 and 3Dircadb-02 (Soler et al., 2010) IRCAD ✓ ✓ ✓ 22 CT


SLIVER’07 (Heimann et al., 2009) DKFZ ✓ ✗ ✓ 30 CT


LTSC’08 (Heimann et al., 2009) Siemens ✗ ✓ ✓ 30 CT


ImageCLEF’15 () Bogazici Uni. ✓ ✗ ✓ 30 CT


LiTS TUM ✓ ✓ ✓ 201 CT


Table 1


including liver and liver tumor annotations.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 45 -->


Bilic et al. Page 45


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Distribution of the number of scans per institution in the train and test in the LiTS dataset.


Table 2


Institutions Train Test


Rechts der Isar Hospital, TUM, Germany 28 28


Radboud University Medical Center, the Netherlands 48 12


Polytechnique Montreal and CHUM Research Center in Canada 30 25


Total 131 70


IRCAD, France 20 0


Hebrew University of Jerusalem 5 5


Sheba Medical Center


Hadassah University


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 46 -->


Bilic et al. Page 46


values were obtained by Mann–Whitney u test, describing the significance between the training set and test set shown in the last column. An alpha level


The characteristics of the LiTS training and test sets. The median values and the interquartile range (IQR) are shown for each parameter. In addition, P


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Train Test p-value


In-plane resolution (mm) 0.76 (0.7, 0.85) 0.74 (0.69, 0.8) 0.042


Slice thickness (mm) 1.0 (0.8, 1.5) 1.5 (0.8, 4.0) 0.004


Volume size 512 × 512 × 432 (512 × 512 × 190, 512 × 512 × 684) 512 × 512 × 270 (512 × 512 × 125, 512 × 512 × 622) 0.058


Number of tumors 3 (1, 9) 5 (2, 12) 0.016


(10.41 × 103, 98.90 × 103) 0.039


(1315.94 × 103, 1977.27 × 103) 0.60


Table 3


(1337.75 × 103, 1832.46 × 103) 1622.64 × 103 ± 546.48 × 103


(3.40 × 103, 107.77× 103) 34.78 × 103


of 0.05 was chosen to determine significance.


Liver volume (mm3) 1586.48 × 103 ± 447.14 × 103


Tumor volume (mm3) 16.11 × 103


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 47 -->


Bilic et al. Page 47


different inputs


ensembling by


outputs from.


averaging the


majority vote


component for liver Ensemble of


three models


Multi-scale


training Pre-processing Post-processing Ensemble


For liver:


strategy


sizes.


None


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


[−160, 240] Morphological filter to


maximum probability


filtering based on RF


classifier to remove


elastic deformations. Dice loss RMSprop None largest connected


components with


Tumor candidate


below 0.8 were


false positives


fill the holes


Connected


removed


soft Dice Adam Liver: resampling


to isotropic 2 mm


momentum Value-clipping to


crops and flips cross-entropy SGD Value-clipping to


[−200, 200]


voxels.


Modifications Data augmentation Loss function Optimizer


entropy SGD with


stack of 5 slices) cropping, flipping weighted cross


Table 4


rotations, zooming,


trained FCN on 2D axial slices. Random scaling,


flawed reference


Manual removal


Random flips,


of cases with


segmentation


Details of the participating teams’ methods in LiTS-ISBI-2017.


■ X. Han; Residual U-Net with 2.5D input (a


Tumor: 2D U-net working on four


on 256 × 256, finetuned on 512 ×


working on four resolution levels.


■L. Bi; Jinman Kim Cascaded ResNet based on a pre


weights for tumor FCN. Trained


Liver FCN provides pre-trained


Liver: 3 orthogonal 2D U-nets


team members Method, Architecture &


resolution levels


512.


■ E. Vorontsov; A. Tang, C.


■ G. Chlebus; H. Meine, J.


H. Moltz, A. Schenk


Lead author &


Pal, S. Kadoury


and scaling Soft Dice SGD None None None


Energy function SGD None None None


[−100, 400] None None


3D CRF. None


Component analysis to


remove false positives.


momentum 3D Conditional Random Field


Value-clipping to


Loss function Adam Value-clipping to


Value-clipping to


normalization to


normalization to


and intensity


and intensity


[−160, 240]


[−150, 250]


[0,255]


[0,255]


Momentum


entropy SGD with


cross entropy SGD with


Clustering None None None


Coefficient based


channel 2D input. None Weighted binary


entropy; Tumor:


additional noise weighted cross


J. Hesser Dense 2D U-Nets (Tiramisu) None Soft Tversky


separation for lesions None Liver:cross


random translation,


Random rotation,


■ P. Christ views Cascaded U-Net mirror, cropping,


Cascaded FCN with side outputs


at different resolutions. Three


and Cahn-Hilliard Phase field


U-Net for liver segmentation


■ C. Wang Cascaded 2D U-Net in three


Zhang, X. Yang Random Forest and Fuzzy


orthogonal


■ T. Konopczynski; K. Roth,


■ J. Lipkova; M. Rempfler,


J. Tuset, X. Giro-i-Nieto, J.


■M. Bellver; K. Maninis,


■J. Ma; Y. Li, Y. Wu, M.


J. Lowengrub, B. Menze


Torres


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 48 -->


Bilic et al. Page 48


training Pre-processing Post-processing Ensemble


strategy


entropy SGD None None None


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Modifications Data augmentation Loss function Optimizer


maps None binary cross


concatenated multi-scale feature


team members Method, Architecture &


■ J. Qi; M. Yue A pretrained VGG with


Lead author &


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 49 -->


Bilic et al. Page 49


ensemble of two


models from 5


different inputs


ensembling 5


majority vote


model with


training Pre-processing Post-processing Ensemble


fold cross


validation


For liver:


strategy


[−160, 240] None None


filling None


■ J. Wu Cascade 2D FCN scaling Dice Loss Adam None None None


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


[−75, 175] hole filling and noise


Largest connected


Tumor candidate


component; hole


on RF-classifier


to remove false


filtering based


positives


removal


[−100, 400] None


Jaccard distance Adam Clipping HU values to


channel input scaling softmax log loss SGD Clipping HU values to


entropy Adam Clipping HU values to


scaling Cross-entropy SGD Clipping HU values to


isotropic 2 mm voxels.


soft Dice Adam Liver: resampling to


[−200, 250]


Modifications Data augmentation Loss function Optimizer


Table 5


rotating, scaling and


Details of the participating teams’ methods in LiTS-MICCAI-2017.


Dou, C. Fu, P. Heng H-DenseUNet (Li et al., 2018a) rotation, flipping,


flipping, shifting,


flawed reference


Manual removal


random contrast


■ J. Zou; Cascaded U-Nets weighted cross


normalization


of cases with


segmentation


Tumor: 2D U-net working on four


working on four resolution levels.


resolution levels (Chlebus et al.,


■Y. Yuan; Hierarchical 2.5D FCN network


Liver: 3 orthogonal 2D U-nets


■ A. Ben-Cohen; VGG-16 as a backbone and 3


team members Method, Architecture &


2018)


■ X. Li, H. Chen, X. Qi, Q.


■G. Chlebus; H. Meine, J.


H. Moltz, A. Schenk


Lead author &


ensembling by


component for liver Ensemble of


three models


to fill the holes Multi-scale


and scaling Soft Dice SGD None None None


[−100, 600] None None


None


Energy function SGD None None None


probability below 0.8


[−160, 240] Morphological filter


elastic deformations. Dice loss RMSprop None largest connected


with maximum


were removed


components


Connected


Adam Clipping HU values to


momentum Value-clipping to


crops and flips cross-entropy SGD Value-clipping to


[−200, 200]


entropy SGD with


smooth Dice loss


entropy; Tumor:


stack of 5 slices) cropping, flipping weighted cross


and weighted


cross-entropy


separation for lesions None Liver:cross


Mixture of


flipping, rotation, and


random translation,


rotations, zooming,


Random rotation,


trained FCN on 2D axial slices. Random scaling,


Random flips,


zooming


■ X. Han; Residual U-Net with 2.5D input (a


on 256 × 256, finetuned on 512 ×


2D and 3D U-Net, however with an iterative Mask Mining process


■L. Bi; Jinman Kim Cascaded ResNet based on a pre


weights for tumor FCN. Trained


Liver FCN provides pre-trained


and Cahn-Hilliard Phase field


U-Net for liver segmentation


■C. Wang Cascade 2D U-Net in three


similar to model boosting.


orthogonal views


512.


■E. Vorontsov A. Tang, C.


■ J. Lipkova M. Rempfler,


Konopczynski, J. Hesser


Pal, S. Kadoury


■ K. Roth; T.


J. Lowengrub


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 50 -->


Bilic et al. Page 50


different inputs


outputs from.


averaging the


training Pre-processing Post-processing Ensemble


strategy


sizes.


normalization None None


normalization None None


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


component None


[−100, 400]; intensity


[−100, 400]; intensity


largest connected


entropy Adam Value-clipping to


method) None None None Value-clipping to


[−200, 300]


Modifications Data augmentation Loss function Optimizer


clipping to


entropy SGD Value


activation None weighted cross


Weighted cross


■L. Zhang; S. C. YU Context-aware PolyUNet with


Zhang, X. Yang Label propagation (Interactive


strategy (Zhang and Yu, 2021)


zooming out/in and two-stage


Sekuboyina, B. Menze U-Net with a double sigmoid


team members Method, Architecture &


■J. Ma Y. Li, Y. Wu M.


Lead author &


■M. Piraud A.


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 51 -->


Bilic et al. Page 51


challenge ranking considering two metrics by averaging the ranking scores. Notably only consider Dice and RVD are considered as the volume difference


Liver segmentation submissions of LiTS–MICCAI 2017 and LiTS–MICCAI–MSD 2018 ranked by Dice score and ASD. Top-performing teams in liver


segmentation tasks are highlighted with blue in each metric. A ranking score follows each metric value in the bracket. Re-ranking* denotes a post


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Ranking Ref. Name Dice ASD Re-ranking*


Table 6


## 4 X. Li et al. 0.961 (3) 1.692 (8) 10 (4)


## 5 L. Zhang et al. 0.960 (4) 1.510 (7) 11 (5)


## 7 J. Wu et al. 0.959 (5) 1.311 (5) 10 (4)


## 8 C. Wang et al. 0.958 (6) 1.367 (6) 12 (6)


## 9 E. Vorontsov et al. 0.951 (7) 1.785 (9) 16 (7)


## 10 K. Kaluva et al. 0.950 (8) 1.880 (10) 18 (8)


## 11 K. Roth et al. 0.946 (9) 1.890 (11) 20 (9)


## 1 Y. Yuan et al. 0.963 (1) 1.104 (1) 2 (1)


## 2 A. Ben-Cohen et al. 0.962 (2) 1.130 (2) 4 (2)


## 3 J. Zou et al. 0.961 (3) 1.268 (4) 7 (3)


## 6 G. Chlebus et al. 0.960 (4) 1.150 (3) 7 (3)


of the liver is not of interest, as opposed to the liver tumor.


## LITS–MICCAI 2017


## 12 X. Han et al. 0.943 (10) 2.890 (12) 22 (10)


## 13 J. Lipkova et al. 0.938 (11) 3.540 (13) 24 (11)


## 14 L. Bi et al. 0.934 (12) 258.598 (15) 26 (12)


## 15 M. Piraud et al. 0.767 (13) 37.450 (14) 26 (12)


## 16 J. Ma et al. 0.041 (14) 8231.318 (15) 29 (13)


## 1 F. Isensee et al. 0.962 (1) 2.565 (9) 10 (5)


## 7 M. Perslev et al. 0.953 (6) 2.360 (8) 14 (6)


## 8 I. Kim et al. 0.948 (7) 2.942 (12) 19 (8)


## 9 O. Kodym et al. 0.942 (8) 2.710 (11) 19 (8)


## 2 Z. Xu et al. 0.959 (2) 1.342 (1) 3 (1)


## 3 D. Xu et al. 0.959 (2) 1.722 (5) 7 (3)


## 4 B. Park et al. 0.955 (3) 1.651 (4) 7 (3)


## 5 S. Chen et al. 0.954 (4) 1.386 (2) 6 (2)


## 6 R. Chen et al. 0.954 (5) 1.435 (3) 8 (4)


## LITS–MICCAI-MSD 2018


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 52 -->


Bilic et al. Page 52


Ranking Ref. Name Dice ASD Re-ranking*


## 11 S. Kim et al. 0.934 (10) 6.937 (14) 24 (10)


## 14 I. Sarasua et al. 0.924 (13) 6.273 (13) 26 (11)


## 15 O. Rippel et al. 0.904 (14) 16.163 (16) 30 (12)


## 16 R. Rezaeifar et al. 0.864 (15) 9.358 (15) 30 (12)


## 17 J. Ma et al. 0.706 (16) 159.314 (17) 33 (13)


## 10 F. Jia et al. 0.942 (9) 2.198 (6) 15 (7)


## 12 W. Bae et al. 0.934 (11) 2.615 (10) 21 (9)


## 13 Y. Wang et al. 0.926 (12) 2.313 (7) 19 (8)


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 53 -->


Bilic et al. Page 53


recall and separated F1 scores with three different sizes of lesion). Each metric value is followed by a ranking score in the bracket. Top performing teams


in tumor segmentation and tumor detection are highlighted with blue and pink colors in each metric, respectively. Re-ranking* denotes a post-challenge


Liver tumor segmentation results of three challenges ranked by segmentation metrics (i.e., Dice, ASD and RVD) and detection metrics (i.e., precision,


8 J. Ma et al. 0.465 (7) 2.778 (10) 0.045 (4) 21 (8) 0.107 (7) 0.080 (10) 0.000 (10) 0.033 (10) 0.361 (10)


1 X. Han et al. 0.674 (1) 1.118 (3) −0.103 (7) 11 (3) 0.354 (4) 0.458 (1) 0.103 (3) 0.450 (1) 0.879 (1)


2 G. Chlebus et al. 0.652 (2) 1.076 (2) −0.025 (2) 6 (2) 0.385 (3) 0.406 (4) 0.116 (1) 0.421 (3) 0.867 (3)


3 E. Vorontsov et al. 0.645 (3) 1.225 (6) −0.124 (8) 17 (6) 0.529 (2) 0.439 (2) 0.109 (2) 0.369 (4) 0.850 (4)


4 L. Bi et al. 0.645 (3) 1.006 (1) 0.016 (1) 5 (1) 0.316 (5) 0.431 (3) 0.057 (5) 0.441 (2) 0.876 (2)


5 C. Wang et al. 0.576 (4) 1.187 (5) −0.073 (5) 14 (5) 0.273 (6) 0.346 (7) 0.038 (7) 0.323 (5) 0.806 (7)


6 P. Christ et al. 0.529 (5) 1.130 (4) 0.031 (3) 12 (4) 0.552 (1) 0.383 (5) 0.075 (4) 0.221 (7) 0.837 (6)


7 J. Lipkova et al. 0.476 (6) 2.366 (8) −0.088 (6) 20 (7) 0.105 (8) 0.357 (6) 0.054 (6) 0.250 (6) 0.843 (5)


9 T. Konopczynski et al. 0.417 (8) 1.342 (7) −0.150 (9) 24 (9) 0.057 (9) 0.189 (8) 0.014 (9) 0.106 (8) 0.628 (8)


10 M. Bellver et al. 0.411 (9) 2.776 (9) −0.263 (11) 29 (10) 0.028 (10) 0.172 (9) 0.031 (8) 0.175 (9) 0.512 (9)


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


ranking* Precision Recall F1small F1medium F1large


Ranking Ref. Name Dice ASD RVD Re


Table 7


ranking considering three metrics by averaging the ranking scores.


## LITS–ISBI 2017


11 J. Qi et al. 0.188 (10) 6.118 (11) −0.229 (10) 31 (11) 0.008 (11) 0.009 (11) 0.000 (10) 0.000 (11) 0.041 (11)


3 G. Chlebus et al. 0.676 (3) 1.143 (6) 0.464 (7) 16 (4) 0.519 (1) 0.463 (3) 0.129 (6) 0.494 (2) 0.836 (10)


6 J. Ma et al. 0.655 (6) 5.949 (12) 5.949 (11) 29 (9) 0.409 (4) 0.293 (14) 0.024 (13) 0.200 (13) 0.770 (13)


9 C. Wang et al. 0.625 (9) 1.260 (10) 8.300 (13) 32 (10) 0.156 (12) 0.408 (8) 0.081 (10) 0.423 (7) 0.832 (11)


13 K. Roth et al. 0.570 (13) 0.950 (1) 0.020 (1) 15 (3) 0.070 (14) 0.300 (13) 0.167 (1) 0.411 (9) 0.786 (12)


14 J. Lipkova et al. 0.480 (14) 1.330 (12) 0.060 (2) 28 (8) 0.060 (16) 0.190 (16) 0.014 (14) 0.206 (12) 0.755 (13)


1 J. Zou et al. 0.702 (1) 1.189 (8) 5.921 (10) 14 (2) 0.148 (13) 0.479 (2) 0.163 (2) 0.446 (4) 0.876 (5)


2 X. Li et al. 0.686 (2) 1.073 (4) 5.164 (9) 16 (4) 0.426 (3) 0.515 (1) 0.150 (4) 0.544 (1) 0.907 (3)


4 E. Vorontsov et al. 0.661 (4) 1.075 (5) 12.124 (15) 24 (6) 0.454 (2) 0.455 (6) 0.142 (5) 0.439 (6) 0.877 (4)


5 Y. Yuan et al. 0.657 (5) 1.151 (7) 0.288 (6) 18 (5) 0.321 (5) 0.460 (5) 0.112 (8) 0.471 (3) 0.870 (8)


7 K. Kaluva et al. 0.640 (7) 1.040 (2) 0.190 (4) 13 (1) 0.165 (10) 0.463 (4) 0.112 (7) 0.421 (8) 0.910 (1)


8 X. Han et al. 0.630 (8) 1.050 (3) 0.170 (3) 14 (2) 0.160 (11) 0.330 (11) 0.129 (6) 0.411 (9) 0.908 (2)


10 J. Wu et al. 0.624 (10) 1.232 (9) 4.679 (8) 27 (7) 0.179 (9) 0.372 (9) 0.093 (9) 0.373 (11) 0.875 (6)


11 A. Ben-Cohen et al. 0.620 (11) 1.290 (11) 0.200 (5) 27 (7) 0.270 (7) 0.290 (15) 0.079 (11) 0.383 (10) 0.864 (9)


12 L. Zhang et al. 0.620 (12) 1.388 (13) 6.420 (12) 37 (11) 0.239 (8) 0.446 (7) 0.152 (3) 0.445 (5) 0.872 (7)


## LITS–MICCAI 2017


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 54 -->


Bilic et al. Page 54


15 M. Piraud et al. 0.445 (15) 1.464 (14) 10.121 (14) 43 (12) 0.068 (15) 0.325 (12) 0.038 (12) 0.196 (14) 0.738 (15)


10 W. Bae et al. 0.517 (10) 1.650 (12) −0.039 (5) 27 (7) 0.061 (14) 0.308 (11) 0.078 (6) 0.244 (9) 0.742 (11)


11 I. Sarasua et al. 0.486 (11) 1.374 (10) −0.084 (11) 32 (10) 0.043 (16) 0.298 (12) 0.045 (8) 0.294 (6) 0.678 (12)


12 R. Rezaeifar et al. 0.472 (12) 1.776 (13) −0.258 (15) 40 (12) 0.112 (11) 0.216 (13) 0.005 (12) 0.081 (14) 0.650 (13)


13 O. Rippel et al. 0.451 (13) 1.345 (9) −0.068 (9) 31 (9) 0.044 (15) 0.356 (6) 0.083 (5) 0.353 (4) 0.771 (10)


14 S. Kim et al. 0.404 (14) 1.891 (14) 0.151 (13) 41 (13) 0.116 (10) 0.170 (14) 0.005 (12) 0.091 (13) 0.589 (14)


15 F. Jia et al. 0.316 (15) 12.762 (16) −0.620 (16) 47 (14) 0.069 (12) 0.011 (17) 0.015 (10) 0.000 (16) 0.024 (17)


1 F. Isensee et al. 0.739 (1) 0.903 (2) −0.074 (10) 13 (2) 0.502 (4) 0.554 (1) 0.239 (1) 0.564 (1) 0.915 (2)


2 D. Xu et al. 0.721 (2) 0.896 (1) −0.002 (1) 4 (1) 0.549 (2) 0.503 (2) 0.149 (3) 0.475 (2) 0.937 (1)


3 S. Chen et al. 0.611 (3) 1.397 (11) −0.113 (12) 26 (6) 0.182 (9) 0.368 (4) 0.035 (9) 0.239 (12) 0.859 (3)


4 B. Park et al. 0.608 (4) 1.157 (6) −0.067 (8) 18 (5) 0.343 (5) 0.350 (7) 0.044 (8) 0.267 (7) 0.845 (4)


5 O. Kodym et al. 0.605 (5) 1.134 (4) −0.048 (6) 16 (3) 0.523 (3) 0.336 (8) 0.063 (7) 0.243 (10) 0.819 (6)


6 Z. Xu et al. 0.604 (6) 1.240 (8) −0.025 (4) 18 (5) 0.396 (6) 0.334 (9) 0.015 (10) 0.243 (11) 0.837 (5)


7 R. Chen et al. 0.569 (7) 1.238 (7) −0.188 (14) 28 (8) 0.339 (7) 0.427 (3) 0.207 (2) 0.366 (3) 0.804 (8)


8 I. Kim et al. 0.562 (8) 1.029 (3) 0.012 (2) 13 (2) 0.594 (1) 0.360 (5) 0.092 (4) 0.328 (5) 0.781 (9)


9 M. Perslev et al. 0.556 (9) 1.134 (5) 0.020 (3) 17 (4) 0.024 (17) 0.330 (10) 0.034 (10) 0.251 (8) 0.811 (7)


ranking* Precision Recall F1small F1medium F1large


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Ranking Ref. Name Dice ASD RVD Re


## LITS–MICCAI 2018


16 Y. Wang et al. 0.311 (16) 2.105 (15) 0.054 (7) 38 (11) 0.154 (8) 0.068 (15) 0.000 (13) 0.005 (15) 0.336 (15)


17 J. Ma et al. 0.142 (17) 34.527 (17) 0.685 (17) 51 (15) −0.066 (13) 0.013 (16) 0.000 (13) 0.000 (16) 0.049 (16)


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 55 -->


Bilic et al. Page 55


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Results of Wilcoxon signed-rank tests between each pair of two events. MSD’18 significantly improved over ISBI’17 on both metrics.


Table 8


p-value MICCAI’17 vs. ISBI’17 MSD’18 vs. MICCAI’17 MSD’18 vs. ISBI’17


Dice 0.236 0.073 0.015


## ASD 0.219 0.144 0.006


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 56 -->


Bilic et al. Page 56


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


Table 9


Results of Mann–Whitney U tests between the year of 2022 and the other years.


p-value 2022 vs. 2021 2022 vs. 2020 2022 vs. 2019 2022 vs. 2018 2022 vs. 2017


Dice 0.013 0.088 0.235 <0.001 0.024


## ASD 0.002 0.158 0.129 <0.001 0.016


Med Image Anal. Author manuscript; available in PMC 2023 November 08.


<!-- Page 57 -->


Bilic et al. Page 57


Brief summary of sixteen published work using LiTS for the development of novel segmentation methods in medical imaging. While many of them focus


Author Manuscript Author Manuscript Author Manuscript Author Manuscript


on methodological contribution, they also advance the state-of-the-art in liver and liver tumor segmentation.


MIA Wang et al. (2021) conjugate fully convolutional network, pairwise segmentation, proxy supervision


MIA Zhou et al. (2021a) multimodal registration, unsupervised segmentation, image-guided intervention


TMI Fang and Yan (2020) multi-organ segmentation, multi-scale training, partially labeled data


Nature Methods Isensee et al. (2020) self-configuring framework, extensive evaluation on 23 challenges


MICCAI Haghighi et al. (2020) self-supervised learning, transfer learning, 3D model pre-training


MIA Zhou et al. (2021b) 3D Deep learning, self-supervised learning, transfer learning


Table 10


MICCAI Huang et al. (2020) co-training of sparse datasets, multi-organ segmentation


TMI Haghighi et al. (2021) self-supervised learning, anatomical visual words


TMI Zhang et al. (2020a) interpretable learning, probability calibration


MICCAI Tang et al. (2020) edge enhanced network, cross feature fusion


MICCAI Wang et al. (2019) volumetric attention, 3D segmentation


TMI Cano-Espinosa et al. (2020) biomarker regression and localization


MICCAI Shirokikh et al. (2020) loss reweighting, lesion detection


Source Authors Key features


TMI Yan et al. (2020) training on partially-labeled dataset, lesion detection, multi-dataset learning


TMI Ma et al. (2020) geodesic active contours learning, boundary segmentation


TMI Wang et al. (2020) 2.5D semantic segmentation, attention


Med Image Anal. Author manuscript; available in PMC 2023 November 08.
