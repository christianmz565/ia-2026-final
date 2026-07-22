# chen2023-wood-defect-recognition


<!-- Page 1 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


Review of the Current State of Application of Wood Defect Recognition Technology Yutang Chen, Chengshuo Sun, Zirui Ren, and Bin Na *


Wood utilisation is an important factor affecting production costs, but the combined utilisation rate of wood is generally only 50 to 70%.  During the production process, the rejection scheme of wood defects is one of the most important factors affecting the wood yield.  This paper provides an overview of the main wood defects affecting wood quality, introduces techniques for detecting and identifying wood defects using different technologies, highlights the more widely used image recognition-based wood surface defect identification methods, and presents three advanced wood defect detection and identification equipment. In view of the relatively fixed wood defect recognition requirements in wood processing production, it is proposed that wood defect recognition technology should be further developed toward deep learning to improve the accuracy and efficiency of wood defect recognition. DOI: 10.15376/biores.18.1.Chen Keywords:  Wood defects; Detection and identification; Equipment; Wood processing Contact information: Nanjing Forestry University, Nanjing 210037 China; *Corresponding author: nabin8691@126.com INTRODUCTION Since The Paris Agreement was signed at the United Nations in New York in 2016, countries around the world have been working towards resource conservation, energy saving, and carbon reduction. Protecting forest resources and improving wood utilisation are becoming increasingly important in practical wood production. In wood processing and production, only 50 to 70% of the logs are utilised after the defects, bark, and branches have been removed (Zhuang 2010). As one of the main factors affecting the quality of wood products, the waste of resources caused by missed and misdirected inspections should not be underestimated. At the same time, timber defects can even cause safety hazards. An example from timber frame construction is the case where missed timber defects can lead to instability in the building, which is especially important in the conservation of ancient buildings (Xu et al. 2021; Tan et al. 2022). In the timber industry, a large proportion of companies use manual observation methods to identify timber defects. The manual observation method is highly subjective, with an accuracy of only around 70% (Kryl et al. 2020). Traditional manual timber defect detection is inefficient, limiting, and costly in terms of manpower (Fan et al. 2020). Therefore, it is necessary to make reasonable use of various wood defect recognition technologies. A number of valuable studies have been carried out by scholars on the detection of defects for in-situ assessment of structural timber, mainly consisting of non-destructive and semi-destructive techniques (Kasal and Tannert 2011; Nowak et al. 2016). The practical value of these defect detection techniques has been demonstrated in the assessment of the structural health of urban and forest


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2288


<!-- Page 2 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


standing trees (Feng et al. 2014; Kasal 2014; Papandrea et al. 2022). In recent studies, some academics have compared the efficiency of automated wood defect detection techniques with manual inspection, verifying the improvements in efficiency of automated detection techniques (Nguyen et al. 2020, 2021). These research results have contributed to the development of automated defect detection technology for use in wood processing lines. Designing and manufacturing wood defect recognition systems with lower costs and a wider audience is also very significant, so that new wood defect recognition technologies can be more widely used, to improve wood defect recognition efficiency, reduce wood waste, lower enterprise costs, and conserve forest resources. This paper intends to summarize the advantages and limitations of various wood defect recognition technologies and analyze the advantages of advanced Nordic wood defect recognition equipment, in order to provide reference for improving the accuracy, stability, and rapidity of wood defect recognition equipment. MAIN TIMBER DEFECTS Wood defects can be divided into three categories in terms of their causes: growth defects due to physiological reasons, pest damage defects due to pathological reasons, and processing defects due to human factors (Sang 2013). In the application of timber defect recognition, specific timber defects are identified and rejected depending on the application of the timber. For example, in the case of timber used for load-bearing structures, knots and splits that affect the strength of the timber are identified and removed. In the case of decorative timber, discolouration, decay, etc., which affect the appearance of the timber, are identified and removed. Growth Defects The main growth defects in timber are knots, cracks, slashes, burrs, resin capsules, etc. Most of these defects are due to the normal growth of the tree. However, from the perspective of wood panel utilisation, these are wood defects. Of these, knots are divided into live knots, as shown in Fig. 1a, and dead knots, as shown in Fig. 1b.


(a) live knots              (b) dead knots               (c) pest damages Fig. 1. Major wood defects


Growth defects destroy the uniformity and integrity of the timber structure, affecting not only the aesthetic and processing properties of the surface, but also, more importantly, reducing some of the strength of the timber and making it less effective for use. The extent to which growth defects affect the utilisation of the wood depends on the


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2289


<!-- Page 3 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


material, location, size, and density of the growth defects and the use of the wood (Jiang and Liu 2008). In addition, growth defects in wood can lead to a significant reduction in the life expectancy of woodworking tools during the woodworking process (Longuetaud et al. 2012). Pest Damage and Disease Defects The main pest damage and disease defects in wood are discolouration, decay, and insect infestation. The main types of discolouration are chemical discolouration and fungal discolouration. Chemical discolouration is an abnormal reddish-brown, brown, or orangeyellow discolouration caused by chemical and biochemical processes, which is generally more uniform (Yang et al. 2004). Chemical discolouration generally has no effect on the physical and mechanical properties of the wood, but in severe cases it can damage the appearance of the decorative timber. Fungal discolouration generally does not affect the physical and mechanical properties of the wood, but it slightly reduces the impact strength of the wood. Water absorption increases slightly and damages the appearance.


Decay in wood is mainly caused by the invasion of wood-rotting fungi, which gradually causes damage to the cell walls, with consequent changes in physical and mechanical properties. Eventually the wood becomes soft and brittle. Decay seriously affects the physical and mechanical properties of wood. For example, wood loses weight, absorbs a lot of water, and loses strength. Especially, the wood loses hardness. Brown rot usually has the most significant effect on strength; in the later stages of brown rot, strength is essentially close to zero, while white rot can sometimes leave some residual integrity of the wood (Wang et al. 1994). Decayed timber generally loses its strength completely, and its use value is lost. Defects caused by various pests are known as wood pest damage, which is mainly manifested in the form of holes and grooves in wood cuts, as shown in Fig. 1c. Pest damage that involves eaten round timber to a radial depth of less than 10 mm is known as surface holes and grooves. Holes with a minimum diameter of less than 3 mm are known as small holes, and holes with a minimum diameter of 3 mm or more are known as large holes. Surface pest holes and grooves can often be removed with the veneer and therefore have little effect on the use of the timber. Scattered small pest holes have little effect, too. However, large holes with a depth of 10 mm or more and deep, dense small holes can damage the integrity of the timber and reduce its mechanical properties. Moreover, pest holes and grooves are an important channel for sapwood discolouration and decay. Processing Defects Processing defects are defects that occur during the processing of timber as a result of sawing, drying, and other man-made operations, including blunt edges, sharp edges, wavy saw marks, ripples, burrs, and saw kerf deflections. WOOD DEFECT RECOGNITION TECHNIQUES In traditional timber production, defects in timber are mainly removed by manual detection. The traditional manual defect rejection method is inefficient. On the one hand it is prone to leakage and mis-detection due to visual fatigue, and on the other hand the manually calibrated defect rejection scheme often does not maximise the use of wood (Lai et al. 2021). At the same time, wood processing is more conservative compared to other


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2290


<!-- Page 4 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


industries, so it is necessary to develop technology to work with intelligent algorithms for wood defect identification and rejection (Gergeľ et al. 2020). This has also become a new hot topic in the wood processing industry (de Geus et al. 2021; Zhang et al. 2018). Methods for Detecting Internal Defects in Wood Vibration-based detection of internal defects The vibration detection method is mainly used for the detection of internal defects in wood. The general approach is to give the wood a vibration excitation (discrete or continuous) e.g. by striking the wood with a stress hammer and using data acquisition equipment to capture the wood vibration signal, thus obtaining the response signal of the wood specimen to be tested. As the internal structure of the wood affects the vibration spectrum, the frequency response of the wood obtained is not dependent on the force of the strike. Therefore, the frequency can be used to determine whether the wood is defective and the condition of the wood defects. The difficulty with the vibration method for detecting wood defects is that the wood response spectrum is limited in the information it can provide, which can lead to poor accuracy when identifying wood defects (Deflorio et al. 2008). By using the transfer matrix method, the relationship between the location of the defect and the position of the vibration node can be derived from the magnitude of the frequency shift (Sobue et al. 2010). However, most studies on the identification of wood defects by vibration spectrum analysis have been unable to obtain the exact location of wood defects. The extent of wood defects can be determined by analysing the vibration pattern of a single known wood defect (Peterson et al. 2001; Hu et al. 2014). Liao et al. (2017) examined the internal defects of Larix gmelinii by means of a stress hammer and analyze the effect of the striking site of the stress hammer on defect identification. Liu et al. (2020) used the active sensing method of stress waves by mounting piezoelectric sensors on the surface of wood, using one piezoelectric sensor as a signal transmitter and another piezoelectric sensor as a signal receiver to monitor structural damage based on the attenuation of stress waves and converting them into damage indicators using the wavelet packet energy method. Ultrasound-based internal defect detection method Ultrasound detection of wood defects is achieved by ultrasound imaging, which, due to the higher excitation frequency, allows for higher resolution and thus more precise location of wood defects (Espinosa et al. 2020). The basic idea is to identify wood defects by exploiting the fact that the speed of ultrasound propagation decreases when it encounters a wood defect during propagation. In earlier studies, wood defects such as knots were found to cause deviations in the surrounding fibres, affecting the propagation velocity of the sound waves (Puccini et al. 2002). However, unlike metals, the individual anisotropies of wood allow the propagation velocity of ultrasound to vary due to the natural variation in wood texture. A difficulty in ultrasonic detection of wood defects lies in distinguishing between natural velocity variations and velocity variations caused by defects (Bucur 2003; Palma et al. 2018). On the other hand, the traditional use of oil or water as a coupling agent cannot be applied to wood due to its porous structure (Fang et al. 2017). Ultrasonic detection of wood defects needs to be implemented by air-coupled ultrasound techniques. By detecting changes in wood density through air-coupled ultrasonics, knots, holes, grooves, etc., can be detected and located (Hsu et al. 2010). With the improvement of ultrasonic testing instruments, the air-ultrasonic coupling technique is increasingly being used in the practical application of


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2291


<!-- Page 5 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


wood defect detection. Zhang et al. (2016) used a Sylvatest-Duo ultrasonic detector to test healthy fir wood and fir wood containing different hole defect sizes. They obtained the quantitative relationship between ultrasonic propagation velocity and different hole diameters. Mori et al. (2016) measured and compared the bending strength of rods made of Japanese cypress and Japanese cedar using the ACU technique. Wang et al. (2021) used the Python language to write an upper computer software that can automate non-contact ultrasonic detection of wood defects. Besides, the use of some new material sensors can improve the signal-to-noise ratio and thus make the ACU technique detecting defects more accurately (Vössing et al. 2020). However, ultrasonic methods for detecting wood defects have limitations (Vössing and Niederleithinger 2018). Currently ultrasonic methods cannot detect wood discolouration defects, etc. X-ray based method for detecting internal defects X-ray detection of wood defects is based on the principle that when the rays pass through the wood being inspected, the normal wood part and the defective wood part absorb and attenuate the X-rays differently, thus enabling the detection of wood defects. Zhang (2017a) designed a fuzzy genetic and ant colony fusion algorithm when processing wood X-ray images, overcoming the limitations of standard genetic algorithms that are slow in later iterations. As the application of CT scanning technology expands from the medical field to other fields, it is considered a reliable solution when performing more accurate localization of wood defects (Beaulieu and Dutilleul 2019). The capability of CT scanning technology to detect defects has been proven in the inspection of historic wooden buildings and in the inspection of wooden furniture (Hansson et al. 2015; Wedvik et al. 2016; Wang et al. 2020). When applying CT techniques to identify wood defects, the choice of filter function directly affects the final defect recognition accuracy. In previous studies, some scholars have analysed and evaluated the effect of reconstructed images with various filters such as R-L, S-L, Cosine, and Hamming, and they concluded that the improved Butterworth filter could reveal finer defect features (Qi et al. 2018, Luo et al. 2018). Chen et al. (2018) designed a convolutional neural network-based defect recognition algorithm for CT images inside wood, which overcame the problems of tedious image preprocessing, complex training methods, too many training parameters, and excessive time consumption of traditional recognition methods (Chen et al. 2018). One difficulty in the popularization of CT technology in the field of wood defect recognition is its high cost. Chlewicki et al. (2011) designed a low-cost alternative system, but there is still room for improving its accuracy. In addition, the radiation damage caused to the operator by this method limits its application. Methods for Detecting Surface Defects in Wood From the point of view of market effects, the quality of the wood surface is visually presented to the user and can directly influence the customer's purchase intention (Manuel et al. 2015). Discolouration and small defects on the surface of wood cannot be identified by the internal defect detection methods described above. Fine features of the wood surface can be obtained by image recognition and laser triangulation for defect identification. Surface defect detection based on image recognition The identification of surface defects in wood by means of image recognition requires only computer analysis of the captured wood surface image (usually by means of


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2292


<!-- Page 6 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


a CCD camera) and does not require the introduction of additional equipment, thus offering lower costs. On the other hand, the detection process of the image recognition method is more conducive to the intervention of general operators, and the method is most widely used in practical wood production. The accuracy of image recognition for detecting surface defects in wood depends mainly on the design of the image analysis algorithm, and digital image processing is currently used for image recognition of wood defects (Xie 2013). Firstly, the image is pre-processed using grey scale transformation, histogram equalisation, spatial domain or frequency domain filtering, etc. Then, the wood defect images are subjected to defect feature extraction. Finally, a machine learning algorithm is used to classify the images. Among them, the defect feature extraction and the decision of feature information directly affect the final recognition effect. The features of the wood surface, mainly including the grey scale co-occurrence matrix, the colour matrix, and the colour histogram, will be colour features, geometric features, and texture features. As the wood surface is more complex, the features extracted from it are often more numerous and can increase the complexity of the decision algorithm to a certain extent. Therefore, it is necessary to fuse the extracted features, and principal component analysis (PCA) is considered a reliable method for fusing wood surface features (Zhang et al. 2015). Zhang (2017b) extracted image features of dead and live knots on wood surface by wavelet transform and LBP algorithm. Li et al. (2021) applied the OTSU algorithm combined with mathematical morphology to extract the features of insect eye, live knot, and dead knot defect contours on wood surface, and extract the edge contours of wood surface defects by Sobel operator. In addition, Li et al. (2019) improved the accuracy of wood surface defect classification by first establishing a histogram of associated wood surface image elements and then performing feature extraction. The most commonly used methods for decision making in wood surface image features are different neural networks such as convolution neural network (CNN) because of their non-linear discriminant function property that can obtain higher decision efficiency (Packianather and Drake 2005). Luo (2019) compared the effectiveness of BP neural network model, SVM support vector machine classification model, and CNN convolutional neural network model for wood defect classification, and the CNN convolutional neural network model and SVM support. The CNN convolutional neural network model and the SVM support vector machine model were considered more suitable for wood defect detection and classification than the BP neural network model, and they had higher classification accuracy for wood defect detection and classification (Luo 2019).


Deep learning is a branch of neural networks, and its superiority lies in the greater amount of data learned and the times it is learned. Typically, this means that deep learning will have more hidden layers. However, it is not the case that more hidden layers mean better learning results. Designing the right number of hidden layers for a specific issue is one of the keys to a successful deep learning design. A comparison of the structure of deep learning and ordinary neural networks is shown in Fig. 2.


With the development of deep learning, more and more scholars tend to adopt deep learning algorithms to classify defects in wood surface images. Frameworks, based on different kinds of CNN models, have been derived to be applied to wood surface defect recognition (Wang et al. 2021). Urbonas et al. (2019) used R-CNN for wood surface defect recognition with an accuracy of 96.1%. Shi et al. (2020) combined the neural architecture search (NAS) technique with the mask R-CNN technique to improve the speed and accuracy of detecting surface defects in wood veneer. Fan (2020) analysed R-CNN, Fast


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2293


<!-- Page 7 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


R-CNN, Faster R-CNN, and other models for wood defect recognition in solid wood panels and developed a human-computer interactive solid wood panel defect detection system. The image information tables of this system have been established by SQL Server software tools (Fan 2020).


Output layer


Hidden layers


Input layer


Neural networks Deep learning neural networks


Fig. 2. Different amounts of data between deep learning and ordinary neural networks Laser triangulation-based surface defect detection method Laser triangulation is based on the principle that the reflection of the wood from the laser source is received by a laser detector and the accepted emission data is processed using computer software. Each laser emission line contains fine data about the surface of the wood and can have a resolution of 0.01 mm (Siekański et al. 2019). When detecting the splits and the holes on the wood surface, laser triangulation can be more economical and accurate compared to image recognition because it taps into the three-dimensional shape features of both defects, thus eliminating the need to increase the image acquisition resolution of the CCD camera to achieve defect identification (Hu et al. 2003).


Sandak et al. (2020) compared the effectiveness of three laser sensors with different parameters for wood surface monitoring and arrived at a class of laser sensors suitable for different production requirements. To enhance the application of wood surface laser scanning technology in practical wood processing production, Wang et al. (2016) designed a device that could achieve laser scanning of wood flow lines. Peng et al. (2016) used a portable handheld laser scanner to scan the wood surface and achieved the first simultaneous identification of wood surface defects and wood species, and the accuracy rate could reach around 95% (Peng et al. 2016).


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2294


<!-- Page 8 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


RESEARCH ON THE CURRENT STATUS OF WOOD DEFECT RECOGNITION EQUIPMENT The commercialization of wood defect recognition equipment started many years ago, and early studies have compared commercial wood defect recognition equipment that was then available. Through the test of experiments, the equipment back then could not provide accurate and reliable recognition of wood defects in complex production environments due to reasons such as sensor and algorithm advancement (Buehlmann et al. 2007). However, with the development of sensor technology and artificial intelligence technology, today’s marketed wood defect recognition equipment is different from the past. These advanced scanners use a multi-sensor system, with targeted algorithms for different types of wood defects, and they work with front-end production demand solutions to achieve increased productivity, automation, and intelligent production (Gergeľ et al. 2019). However, for most small and medium-sized wood processing companies, the high price of these devices prevents them from purchasing them (Pan et al. 2021). At the same time, even in large wood processing companies in developing countries, the maintenance of their equipment is inconvenient. The Dilemma of Wood Defect Identification Equipment The wood processing industry has a long history and a large processing capacity. However, due to its low threshold, the overall quality of the wood processing industry in developing countries is not high, the scale of enterprises is small, and the quality and efficiency is poor (Zhao 2003). Most low-scale wood processing enterprises are not able to purchase expensive wood defect identification equipment. In China, for example, as the world's largest producer and consumer of wood-based panels and the second largest consumer of wood, the country's wood processing industry is still in a situation of few branded products, high consumption, rough processing, and little independent innovation (Xie 2013). Most wood processing plants use manual scribing in conjunction with preferential sawing for defect rejection. The relatively limited market for equipment purchases has caused a relative lag in the development of wood defect identification equipment in developing countries such as China. The agglomeration of regional industries has accelerated the merger and integration of large-scale and high-level wood processing enterprises with low-scale enterprises. This increases the demand for wood defect recognition equipment. Some universities and research institutes have started to independently develop wood defect recognition equipment that can adapt to actual processing scenarios. Research on wood defect recognition equipment in developing countries started late and had a poor foundation. On the contrary, the technology of wood defect recognition equipment in Nordic countries is more advanced, due to the high degree of automation of the wood processing industry. Among them, some large brands of wood defect scanners present stable and efficient results in addition to the accuracy and speed of detecting wood defects. Their ability to accumulate production information, reduce size for mobility, and adapt to multiple scenarios enables these products to gain a broader market. Mature Timber Defect Recognition Systems Due to the high requirements for surface wood defect recognition in actual wood processing production, the advanced Nordic wood defect recognition equipment generally uses multi-angle defect detection based on laser triangulation. The advantage of this


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2295


<!-- Page 9 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


architecture (Fig. 3) is that it enables high-speed detection of wood defects in conjunction with production lines. At the same time, these advanced wood defect recognition machines use other monitoring methods to achieve a wider range of applications and more accurate results.


Each face contains a laser


triangulation system


Each system integrates multiple sensing elements


Each wooden panel on the flow line


passes through the middle of the


instrument for defect detection Fig. 3. Schematic diagram of multi-faceted detection architecture WoodEye AB (Sweden) has designed a system for the automatic identification of defects on wood surfaces using laser detection in combination with image recognition. After identifying the defects in the wood, the system uses an artificial intelligence algorithm to classify the defects according to the type and size of the detected defects and to develop the most cost-efficient defect removal solution. This is shown in Fig. 4. The system is equipped with a laser sensor targeted primarily at identifying defects on the surface of the wood such as black knots, stains, and blind knots due to changes in the arrangement of the wood fibres. A high-resolution CCD camera works with the image recognition algorithm to calculate the location, shape, and extent of the defects. The significant advantage of this wood defect recognition system in real wood processing production is that it is able to use deep learning algorithms over a long period of time to accumulate and statistically correlate production data with entities such as suppliers, customers, work shifts, and products in operation. This ability to statistically analyse job information is attractive to large wood processing companies because it facilitates the computerisation of wood processing production.


Fig. 4. Sawing scheme based on defect location WEINIG (Germany) has also designed a wood defect recognition system using laser detection in conjunction with image detection. As the laser detection has a stronger three-dimensional feature mining capability and the image detection has a stronger twodimensional feature mining capability, these two methods can be used together to improve the stability and accuracy of defect detection. The system is designed for the processing environment. In such systems, wood dust can be dispersed during the wood processing process and the device is protected by separate sealed air chambers for each angle of the sensor to obtain more stable defect identification results. In addition, the system's real-time status monitoring software makes it easy for the operator to follow the real-time status of


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2296


<!-- Page 10 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


the wood defect identification and to intervene manually if necessary, with the status monitoring interface shown in Fig. 5. The small size and mass of the system compared to the previous system makes it easy to move around, allowing it to be used in a variety of factory environments, even in small workshops.


Fig. 5. The status monitoring interface In addition to the two above-mentioned systems for the identification of wood defects mainly on the surface, Microtec CT (Italy) has enhanced the use of X-ray inspection to more accurately identify internal defects in wood. This is because the system can be used not only for the identification of surface defects in boards, but also for quality grading of lumber. In practice, the system achieves an accuracy of 92.22% for hardwood lumber grading, which far exceeds the industry standard of 80% (NHLA 2015; Gazo et al. 2018). CONCLUSION Wood defect identification can be achieved by a variety of techniques, but single techniques generally have drawbacks. For example, vibration-based detection methods have difficulty in accurately locating defects, and ultrasonic-based detection results can be influenced by the medium. Therefore, the advanced wood defect detection equipment described above incorporates a variety of defect detection techniques to improve the stability and accuracy of the final detection. Companies from regions where wood defect detection technology is more widespread and advanced have already designed systems for the identification of wood defects that are excellent and can be used in actual processing production. However, for wood processing companies from regions with relatively poor wood defect detection technology, high research, development, and maintenance costs limit the spread and application of these techniques. Much research has been done by academics in these regions to develop wood defect recognition systems, but most of it is still in the experimental stage. The future direction of the development of wood defect recognition systems is clear. On the one hand, it relies on the innovation of artificial intelligence algorithms and the progress of sensor technology to improve the efficiency of defect recognition and reduce the price of equipment. On the other hand, it combines the information of defect recognition decisions with the sales strategy of the wood enterprise, the source of raw materials, and other information to improve the information technology of the wood processing industry.


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2297


<!-- Page 11 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


ACKNOWLEDGMENT This research is supported by the Postgraduate Research & Practice Innovation Program of Jiangsu Province SJCX22_0317. REFERENCES CITED Beaulieu, J., and Dutilleul, P. (2019). "Applications of computed tomography (CT)


scanning technology in forest research: A timely update and review," Canadian Journal of Forest Research 49(10), 1173-1188. DOI: 10.1139/cjfr-2018-0537 Bucur, V. (2003). "Ultrasonic imaging," in: Nondestructive Characterization and


Imaging of Wood, T. E. Timell (ed.), Springer–Verlag, Berlin, BER, GER, pp. 181214. Buehlmann, U., Lihra, T., Rancourt, V., and Ait-Kadi, D. (2007). "Detection capabilities


of automated hardwood lumber defect-detection systems," Forest Products Journal 57(10), 51-57. DOI: 10.1111/j.1439-0329.2007.00514.x Chen, L. X., Ge, Z. D., Luo, R, Liu, C. Z., Liu, X. P., and Zhou, Y. C. (2018).


"Identification of CT image defects in wood based on convolution neural network," Scientia Silvae Sinicae 54(11), 127-133. DOI: 10.11707/j.1001-7488.20181118 Chlewicki, W., Baniukiewicz, P., Chady, T., and Brykalski, A. (2011). "Identification of


defects in 3D space using computer radiography system," Electromagnetic Nondestructive Evaluation 35, 30-35. DOI: 10.3233/978-1-60750-750-5-30 Deflorio, G., Fink, S., and Schwarze, F. W. M. R. (2008). "Detection of incipient decay


in tree stems with sonic tomography after wounding and fungal inoculation," Wood Science and Technology 42(2), 117-132. DOI: 10.1007/s00226-007-0159-0 de Geus, A. R., Backes, A. R., Gontijo, A. B., Albuquerque, G. H. Q., and Souza, J. R.


(2021). "Amazon wood species classification: A comparison between deep learning and pre-designed features," Wood Science and Technology 55(3), 857-872. DOI: 10.1007/s00226-021-01282-w Espinosa, L., Brancheriau, L., Cortes, Y., Prieto, F., and Lasaygues, P. (2020).


"Ultrasound computed tomography on standing trees: Accounting for wood anisotropy permits a more accurate detection of defects," Annals of Forest Science 77(3). DOI: 10.1007/s13595-020-00971-z Fan, J. N. (2020). Research on Defect Detection Algorithm of Solid Wood Plate Based on


Deep Learning, Master’s Thesis, Nanjing Forestry University, Nanjing, China. Fan, J. N, Liu, Y., Yang, Y. T., and Gou, B. L. (2020). "Research progress in the


application of machine vision to wood defect detection," World Forestry Research 33(3), 32-37. DOI: 10.13348/j.cnki.sjlyyj.2020.0020.y Fang, Y. M., Lin, L. J., Feng, H. L., Lu, Z. X. and Emms, G. W. (2017). "Review of the


use of air-coupled ultrasonic technologies for nondestructive testing of wood and wood products," Computers and Electronics in Agriculture 137, 79-87. DOI: 10.1016/j.compag.2017.03.015 Feng, H., Li, G. H., Fu, S., and Wang, X. P. (2014). "Tomographic image reconstruction


using an interpolation method for tree decay detection," BioResources 9(2), 32483263. DOI: 10.15376/biores.9.2.3248-3263 Gazo, R., Wells, L., Krs, V., and Benes, B. (2018). "Validation of automated hardwood


lumber grading system," Computers and Electronics in Agriculture 155, 496-500. DOI: 10.1016/j.compag.2018.06.041


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2298


<!-- Page 12 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


Gergeľ, T., Sedliak, M., Bucha, T., Oravec, M., Slamka, M., and Pástor. M. (2020).


"Prediction model of wooden logs cutting patterns and its efficiency in practice," Applied Sciences 10(9), 3003. DOI: 10.3390/app10093003 Gergeľ, T., Bucha, T., Gejdoš, M., and Vyhnáliková, Z. (2019). "Computed tomography


log scanning – high technology for forestry and forest based industry," Central European Forestry Journal 65(1), 51-59. DOI: 10.2478/forj-2019-0003 Hsu, D. K., Utrata, D., and Kuo, M. (2010). "NDE of lumber and natural fiber based


products with air coupled ultrasound," Review of Progress in Quantitative Nondestructive Evaluation 1211, 1533. DOI: 10.1063/1.3362250 Hu, C. S., Tanaka, C., and Ohtani, T. (2003). "Locating and identifying splits and holes


on sugi by the laser displacement sensor," Journal of Wood Science 49(6), 492-498. DOI: 10.1007/s10086-002-0509-3 Hu, X. Y., Zhu, H. P., and Wang, D. S. (2014). "A study of concrete slab damage


detection based on the electromechanical impedance method," Sensors 14(10), 19897-19909. DOI: 10.3390/s141019897 Jiang, C. Z., and Liu, X. M. (2008). "The impact of wood defects on wood utilisation,"


Science & Technology Information 24, 331. DOI: CNKI:SUN:KJXX.0.2008-24-279 Kasal, B. and Tannert, T. (2011). In Situ Assessment of Structural Timber, Vol. 7,


Springer, Berlin, Germany. Kasal, B. (2014). "Structural health assessment of in situ timber: An interface between


service life planning and timber engineering," Wood Material Science & Engineering 9(3), 134-138. DOI: 10.1080/17480272.2014.903298 Kryl, M., Danys, L., Jaros, R., Martinek, R., Kodytek, P., and Bilik, P. (2020). "Wood


recognition and quality imaging inspection systems," Journal of Sensors 2020, 1-19. DOI: 10.1155/2020/3217126 Lai, F., Luo, T. F., Ding, R., Luo, R. H., Deng, T. T., Wang, M. H., and Li, M. (2021).


"Application of image processing technology to wood surface defect detection," Forestry Machinery & Woodworking Equipment 49(2), 16-21. DOI: 10.13279/j.cnki.fmwe.2021.0016 Li, S. L., Yuan, W. Q., Yang, J. Y., and Li, D. J. (2019). "Wood defect classification


based on local binary difference excitation pattern," Chinese Journal of Scientific Instrument 40(06), 68-77. DOI: 10.19650/j.cnki.cjsi.J1905194 Li, Y. G., Yang, J., and Dong, C. L. (2021). "Research on feature extraction algorithm of


wood surface defects," Journal of Northwest Forestry University 36(04), 204208+281. DOI: 10.3969/j.issn.1001-7461.2021.04.29 Liao, C. H., Zhang, H. J., Song, X. C., Chen, T., and Huang, S. L. (2017). "The screening


method of the internal defects in wood members of the ancient architectures by hammering sound," BioResources 12(2), 2711-2720. DOI: 10.15376/biores.12.2.2711-2720 Liu, X. Y., Rao, Y. L., Zhang, J. C., and Xiao, J. H. (2020). "Timber axial pressure


damage monitoring based on piezoceramic sensor," Piezoelectrics & Acoustooptics 42(05), 681-685. DOI: 10.11977/j.issn.1004-2474.2020.05.022 Longuetaud, F., Mothe, F., Kerautret, B., Krähenbühl, A., Hory, L., Leban, J. M., and


Debled-Rennesson, I. (2012). "Automatic knot detection and measurements from Xray CT images of wood: A review and validation of an improved algorithm on softwood samples," Computers and Electronics in Agriculture 85, 77-89. DOI: 10.1016/j.compag.2012.03.013


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2299


<!-- Page 13 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


Luo, R., Ge, Z. D., Chen, L. X., Liu, C. Z., Zhou, Y. C., and Xu, W. Q. (2018).


"Selection of the optimum filter in the back projection algorithm based on X-Ray wood tomography," Scientia Silvae Sinicae 54(11), 143-148. DOI: 10.11707/j.10017488.20181120 Luo, W. (2019). Research on Wood Classification and Sorting Algorithms Based on


Image Multi-feature Pattern Recognition, Ph.D. Dissertation, Northeast Forestry University, Haerbin, China. Manuel, A., Leonhart, R., Broman, O., and Becker, G. (2015). "Consumers’ perceptions


and preference profiles for wood surfaces tested with pairwise comparison in Germany," Annals of Forest Science 72(6), 741-751. DOI: 10.1007/s13595-0140452-7 Mori, M., Hasegawa, M., Yoo, J., Kang, S., and Matsumura, J. (2016). "Nondestructive


evaluation of bending strength of wood with artificial holes by employing air-coupled ultrasonics," Construction and building materials 110, 24-31. DOI: 10.1016/j.conbuildmat.2016.02.020 National Hardwood Lumber Association (2015). Rules for the Measurement and


Inspection of Hardwood and Cypress Lumber, NHLA. Memphis, TN. Nguyen, V. -T., Constant, T. and Colin, F. (2021). "An innovative and automated method


for characterizing wood defects on trunk surfaces using high-density 3D terrestrial LiDAR data," Annals of Forest Science 78(32), DOI: 10.1007/s13595-020-01022-3 Nguyen, V. -T., Constant, T., Kerautret, B., Debled-Rennesson, I., and Colin, F. (2020).


"A machine-learning approach for classifying defects on tree trunks using terrestrial LiDAR," Computers and Electronics in Agriculture 171, DOI: 10.1016/j.compag.2020.105332 Nowak, T. P., Jasieńko, J., and Hamrol-Bielecka, K. (2016). "In situ assessment of


structural timber using the resistance drilling method – Evaluation of usefulness," Construction and Building Materials 102, 403-415. DOI: 10.1016/j.conbuildmat.2015.11.004 Packianather, M. S., and Drake, P. R. (2005). "Comparison of neural and minimum


distance classifiers in wood veneer defect identification," Proceedings of the Institution of Mechanical Engineers, Part B: Journal of Engineering Manufacture 219(11), 831-841. DOI: 10.1243/095440505X32823 Palma, S. S. A., Goncalves, R., Trinca, A. J., Costa, C. P., Reis, M. N. D., and Martins,


G. A. (2018). "Interference from knots, wave propagation direction, and effect of juvenile and reaction wood on velocities in ultrasound tomography," BioResources 13(2), 2834-2845. DOI: 10.15376/biores.13.2.2834-2845 Pan, L., Rogulin, R., and Kondrashev, S. (2021). "Artificial neural network for defect


detection in CT images of wood," Computers and Electronics in Agriculture 187, article no. 106312. DOI: 10.1016/j.compag.2021.106312 Papandrea, S. F., Cataldo, M. F., Zimbalatti, G., and Proto, A. R. (2022). "Comparative


evaluation of inspection techniques for decay detection in urban trees," Sensors and Actuators A: Physical 340. DOI: 10.1016/j.sna.2022.113544 Peng, Z., Yue, L., and Xiao, N. (2016). "Simultaneous wood defect and species detection


with 3D laser scanning scheme," International Journal of Optics 2016, 1-6. DOI: 10.1155/2016/7049523 Peterson, S., McLean, D., Symans, M., Pollock, D., Cofer, W., Emerson, R., and Fridley,


K. (2001). "Application of dynamic system identification to timber beams. I," Journal


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2300


<!-- Page 14 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


of Structural Engineering 4(127), 418-425. DOI: 10.1061/(ASCE)07339445(2001)127:4(418). Puccini, C. T., Gonçalves, R., and Monteiro, M. E. A. (2002). "Avaliação estatística da


variação da velocidade de propagação de ondas de ultra-som na madeira em presença de defeitos," Revista Brasileira de Engenharia Agrícola e Ambiental 6(3), 499-503. DOI: 10.1590/S1415-43662002000300020 Qi, Y. H., Zhou, Y. C., Xu, J. H., and Ge, Z. D. (2018). "Development of wood CT


imaging system using Butterworth filter based filtered back-projection algorithm," Forest Products Journal 68(2), 147-156, DOI: 10.13073/FPJ-D-17-00029 Sandak, J., Orlowski, K. A., Sandak, A., Chuchala, D., and Taube, P. (2020). "On-line


measurement of wood surface smoothness," Drvna Industrija 71(2), 193-200. DOI: 10.5552/drvind.2020.1970 Sang, Q. L. (2013). "How to improve inspection techniques for wood defects,"


Contemporary Horticulture (10), 222. DOI: 10.14051/j.cnki.xdyy.2013.20.003 Shi, J. H., Li, Z. Y., Zhu, T. T., Wang, D. Y. and Ni, C. (2020). "Defect detection of


industry wood veneer based on NAS and multi-channel mask R-CNN," Sensors 20(16), 4398. DOI: 10.3390/s20164398 Siekański, P., Magda, K., Malowany, K., Rutkiewicz, J., Styk, A., Krzesłowski, J.,


Kowaluk, T., and Zagórski, A. (2019). "On-line laser triangulation scanner for wood logs surface geometry measurement," Sensors 19(5), article no. 1074. DOI: 10.3390/s19051074 Sobue, N., Fujita, M., Nakano, A., and Suzuki, T. (2010). "Identification of defect


position in a wooden beam from the power spectrum of longitudinal vibration," Journal of Wood Science 56(2), 112-117. DOI: 10.1007/s10086-009-1080-y Tan, Y. J., Yang, X. J., Bai, X. C., Dong, H. R., Liu, J. M., and Zhang, L. (2022).


"Inspection and evaluation of wood components of ancient buildings in the SouthThree Courts of the Forbidden City," BioResources 17(1), 962-974. DOI: 10.15376/biores.17.1.962-974 Urbonas, A., Raudonis, V., Maskeliūnas, R., and Damaševičius, R. (2019). "Automated


identification of wood veneer surface defects using faster region-based convolutional neural network with data augmentation and transfer learning," Applied Sciences 9(22) 4898. DOI: 10.3390/app9224898 Vössing, K. J., Gaal, M., and Niederleithinger, E. (2020). "Imaging wood defects using


air coupled ferroelectret ultrasonic transducers in reflection mode," Construction and Building Materials 241. DOI: 10.1016/j.conbuildmat.2020.118032 Vössing, K. J. and Niederleithinger, E. (2018). "Nondestructive assessment and imaging


methods for internal inspection of timber. A review.," Holzforschung 72(6), 467-476. DOI: 10.1515/hf-2017-0122 Wang, J. D., Zhao, Q., Liu, Y., Zhai, F. F., and Zhao, T. (2016). "Design of laser


scanning and detection devices for wood surface defects," Forestry Machinery & Woodworking Equipment 44(11), 24-27. DOI: CNKI:SUN:LJMG.0.2016-11-006 Wang, M. L., Wang, J., Li, Q. X., Wang, X. S., and Cao, Q. (2021). "Design and


implementation of a non-contact ultrasonic wood defect detection system," Shanxi Electronic Technology (06), 16-19. DOI: 10.3969/j.issn.1674-4578.2021.06.005 Wang, Q. P., Liu, X. E. and Yang, S. M. (2020). "Predicting density and moisture content


of Populus xiangchengensis and Phyllostachys edulis using the X-ray computed tomography technique," Forest Products Journal 70(2), 193-199. DOI: 10.13073/FPJ-D-20-00001


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2301


<!-- Page 15 -->


PEER-REVIEWED REVIEW ARTICLE bioresources.com


Wang, S. Y., Wang, S. A., Ding, Y. W., Liu, J. Y., and Che, Z. Y. (1994). "An


introduction to the effect of wood defects on material and timber properties," Forestry Science and Technology Information (2), 1-3. DOI: CNKI:SUN:LYKQ.0.1994-02000 Wang, Y., Zhang, W., Gao, R., Jin, Z., and Wang, X. H. (2021). "Recent advances in the


application of deep learning methods to forestry," Wood Science and Technology 55(5), 1171-1202. DOI: 10.1007/s00226-021-01309-2 Wedvik, B., Stein, M., Stornes, J. M., and Mattsson, J. (2016). "On-site radioscopic


qualitative assessment of historic timber structures: Identification and mapping of biological deterioration of wood," International Journal of Architectural Heritage 10(5), 646-662. DOI: 10.1080/15583058.2015.1077905 Xie, D. Y. (2013). "Analysis to situation and countermeasure of wood manufacture


industry of our country," Forest Investigation Design (03), 85-92. DOI: 10.3969/j.issn.1673-4505.2013.03.038 Xie, Y. H. (2013). The Application and Research of Digital Image Processing On Wood


Surface Texture Inspection, Master’s Thesis, Northeast Forestry University, Shenyang, China. Xu, P. F., Guan, C., Zhang, H. J., Li, G. H., Zhao, D., Ross, R. J., and Shen, Y. L. (2021).


"Application of nondestructive testing technologies in preserving historic trees and ancient timber structures in China," Forests 12(3), 318. DOI: 10.3390/f12030318 Yang, C. M., Hu, W. Y., Bai, F., and Tang, X. H. (2004). "The development of theory


and method in assaying wood defection," Forestry Machinery & Woodworking Equipment (03), 8-10. DOI: 10.3969/j.issn.2095-2953.2004.03.002 Zhang, Y. Z., Xu, C., Li, C., Yu, H. L., and Cao, J. (2015). "Wood defect detection


method with PCA feature fusion and compressed sensing," Journal of Forestry Research 26(3), 745-751. DOI: 10.1007/s11676-015-0066-4 Zhang, T., Cheng, X. W., Lu, W. D., and Liu, W. Q. (2016). "Experimental study on


testing internal hole defects of wood by ultrasonic method," Journal of Southwest Forestry University (Natural Sciences) 36(01), 121-125+130. DOI: 10.11929/j.issn.2095-1914.2016.01.020 Zhang, Y. G. (2017a). Restoration and Segmentation of Wood X-ray Images Based on


Optimization Algorithm, Master’s Thesis, Northeastern University, Shenyang, China. Zhang, Y. X. (2017b). Wood Surface Defect Recognition Based on Wavelet Transform


and LBP, Master’s Thesis, Nanjing Forestry University, Nanjing, China. Zhang, K., Yuan, B. L. and Li, Y. X. (2018). "Efficiency analysis of wood processing


industry in China during 2006-2015," IOP Conf. Series: Materials Science and Engineering 322 DOI: 10.1088/1757-899X/322/5/052062 Zhao, G. (2003). "Discussion on the developing wood industry in China: current


problems and solutions," China Wood Industry 17(03), 1-3. DOI: 10.19455/j.mcgy.2003.03.001 Zhuang, R. (2010). "Exploration of some issues in improving the utilisation of plywood


wood," Forestry Science & Technology 35(05), 59-60. DOI: 10.3969/j.issn.10019499.2010.05.018 Article submitted: June 28, 2022; Peer review completed: September 24, 2022; Revised version received and accepted: November 5, 2022; Published: December 2, 2022. DOI: 10.15376/biores.18.1.Chen


Chen et al. (2023). “Wood defect recognition,” BioResources 18(1), 2288-2302. 2302
