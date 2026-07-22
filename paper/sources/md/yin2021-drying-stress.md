# yin2021-drying-stress


<!-- Page 1 -->


applied sciences


Review Drying Stress and Strain of Wood: A Review


Qin Yin 1 and Hong-Hai Liu 1,2,3,*


1 College of Furnishings and Industrial Design, Nanjing Forestry University, Nanjing 210037, China; yanqiuhazel@163.com 2 Co-Innovation Center of Efﬁcient Processing and Utilization of Forest Resources, Nanjing Forestry University, Nanjing 210037, China 3 Key Laboratory of Bio-Based Material Science & Technology, Northeast Forestry University, Ministry of Education, Harbin 150040, China * Correspondence: liuhonghai2020@njfu.edu.cn


Abstract: Wood drying stress causes various drying defects, which result from the wood microstructure and the transfer of heat and mass during the drying. It is the fundamental way to solve the problem of defects to clarify the law and mechanism of wood stress and strain development during drying. In this paper, based on the defects of wood drying, the theory and experimental testing methods of drying stress and strain were summarized. Meanwhile, artiﬁcial neural networks (ANN) and their application in the wood drying ﬁeld were also investigated. The traditional prong and slicing methods were used practically in the research and industry of wood drying, but the stress changes in-process cannot be trapped. The technologies of image analysis and near-infrared spectroscopy provide a new opportunity for the detection of drying stress and strain. Hence, future interest should be attached to the combination of the theory of heat and mass transfer and their coupling during drying with the theory of microscopic cell wall mechanics and macroscopic drying. A more complete image acquisition and analysis system should be developed to realize the real-time monitoring of drying strain and cracking, practically. A more feasible and reasonable prediction model of wood drying stress and strain should be established to achieve the accuracy of the prediction.


 


Citation: Yin, Q.; Liu, H.-H. Drying


Keywords: drying stress; drying strain; detection methods; artiﬁcial neural network; back propagation network


Stress and Strain of Wood: A Review.


Appl. Sci. 2021, 11, 5023. https://


doi.org/10.3390/app11115023


Academic Editor: Giuseppe Lazzara


## 1. Introduction


Wood drying is an inevitable part of wood processing which increases wood’s physical properties, mechanical properties and dimensional stability and coating properties [1–4]. Wood material after drying is more suitable for wood-based panels [5], solid wood furniture [6], construction [7], etc. Researchers have been working to optimize wood drying to remove moisture from the wood in a relatively economical way while reducing damage.


Received: 30 April 2021


Accepted: 26 May 2021


Published: 29 May 2021


Publisher’s Note: MDPI stays neutral


Regarding the advancement of wood drying technology, the drying of veneers is moving in the direction of more efﬁcient and energy-saving combined drying. Compared with the wood-based panel unit, the heat and mass transfer mechanism and the stress and strain response of sawn timber are more complicated in the drying process. It therefore becomes vital to predict the changes in various physical parameters in wood drying and reduce the energy consumption of drying. In the future, the method of conventional drying and combined drying will be the development direction of wood drying techniques. Moreover, monitoring and predicting moisture, stress, strain and drying defects in wood drying processes have always been hot topics. Some new developments in recent years include the use of nuclear magnetic resonance (NMR) and low-ﬁeld nuclear magnetic resonance (LFNMR) to monitor moisture status and migration, and prediction of drying quality based on ANN models, etc. [8–13]. Besides, for the special drying of waterlogged wood, the pre-treatment of impregnation is necessary [14]. Some environmentally friendly solutions have been proposed for the collapse of waterlogged wood upon drying: exploring


with regard to jurisdictional claims in


published maps and institutional afﬁl


iations.


Copyright: © 2021 by the authors.


Licensee MDPI, Basel, Switzerland.


This article is an open access article


distributed under the terms and


conditions of the Creative Commons


Attribution (CC BY) license (https://


creativecommons.org/licenses/by/


4.0/).


Appl. Sci. 2021, 11, 5023. https://doi.org/10.3390/app11115023 https://www.mdpi.com/journal/applsci


<!-- Page 2 -->


Appl. Sci. 2021, 11, 5023 2 of 19


the possibility of organosilicons as consolidants to improve the dimensional stability of drying; adding nanotubes to the process to solve mechanical performance problems; and so on [15–17].


The physical and mechanical properties of wood are closely related to the water in wood [18], especially when the moisture content (MC) is lower than a certain critical point of MC which is termed as the ﬁber saturation point (FSP). Researchers have been discussing the deﬁnition of ﬁber saturation in wood drying. Initially, Tiemann [19] deﬁned the ﬁber FSP from the perspective of water state in cell lumens: when there is no liquid water in cell lumens, cell walls begin to dry and strength begins to decrease. However, the above phenomena cannot occur at the same MC. Stamm [20] argued that it is more reasonable to express the turning point (about 30%) where physical properties of wood produce strong variations. Hoffmeyer et al. [21] proposed to quantify FSP with the equilibrium moisture content (EMC) of wood at 100% relative humidity (RH). Based on this concept, the FSP obtained is from 38.5 to 42.5%, which has a deviation of up to 10% from the results of Stamm [20]. Regarding this difference, Engelund [22] had the following speculation: ﬁber saturation may not be a speciﬁc value/point, but a transitional region from the state that new water molecules cut off different H-bonds in the wood cell polymers (MC = 0–30%) to the state that new water molecules are accommodated without breaking any of the cell wall polymer H-bonds (MC = 30–40%). It can be seen that, as the watershed, the saturation point of wood ﬁber is a turning point or a transition state, which is still an unsolved mystery. In addition, Brischke et al. [23] claimed that the use of such terms (i.e., FSP) is somewhat misleading, because the ﬁbers are not saturated with water, but the cell wall is. Perhaps cell wall saturation (CWS) can better describe the phenomena in this special state. This needs to be further researched and developed.


Taking into account the utilization of wood value, defects in wood drying will cause signiﬁcant losses to wood processors. Most of the drying defects develop due to uneven drying stress. Furthermore, the drying stress occurs as a result of uneven shrinkage in wood drying, which is the combined effect of MC and temperature gradients, and shrinkage anisotropy of wood [24]. The drying stress is related to wood micro-structure and the transfer of water and heat during drying, which are the main causes of drying defects such as surface and internal checks. Studying the theory of drying stress and strain contributes to our understanding of the mechanism of defects during wood drying. Many researchers are committed to improving experimental methods [25–27] or establishing models [28,29] to measure and predict drying stress and strain accurately, and to analyze the change rules of them, which have signiﬁcance as scientiﬁc guidance for increasing drying rate, optimizing drying processes and improving drying quality.


It is difﬁcult to detect drying stress during drying; thus, people measure drying strain of wood at a speciﬁc stage to estimate the drying stress at that time. Drying strain detection includes the slicing method, acoustic emission method, etc. With the development of science and technology, digital image correlation (DIC) and near-infrared spectrometry (NIRS) have been gradually applied to the detection of drying stress and have obtained some breakthroughs, but there are still some limitations. It is a great way for researchers to study drying stress and strain, via establishing models to simulate the generation and development of drying stress and strain.


At present, the theoretical model of wood rheology and numerical analysis method are used to simulate the drying stress. Furthermore, ANNs have been gradually applied to the ﬁeld of wood science [11,30,31]. Beneﬁting from its characteristics of ﬁnding the optimal solution at a high speed, ANN is conducive to solving the complex and variable problems of stress and strain in wood drying.


The study of drying stress is signiﬁcant not only for the theory of wood science, but also for the actual process of wood processing. There have been few reports reviewing the research of wood drying stress in the past ten years. It is necessary to summarize the existing research results in order to promote the further development of drying stress research and application. Therefore, in this review, the relationship between drying stress


<!-- Page 3 -->


Appl. Sci. 2021, 11, 5023 3 of 19


and drying defects, the generation and development of mechanisms of drying stress and the composition of drying strain are presented ﬁrstly. Then, detection methods for stress and strain are introduced and compared, and the ANN simulation and prediction for drying stress and strain is summarized. Finally, the research emphases and development trend of drying stress in the future are put forward.


## 2. Wood Drying Stress 2.1. Wood Drying Defects and Drying Stress


There are many types of wood drying defects, which can be roughly divided into two categories [32]: (1) defects caused by shrinkage anisotropy, associated with the warping of timber boards, including cupping, bowing, twisting, spring, etc.; and (2) defects that arise owing to uneven drying, related to the rupture of the wood tissue and delamination. The latter type of defects includes checks (surface, internal and end), end splits due to delamination, honey-combing and case-hardening. Checks are cracks that are visible at the surface but not extending across the board [33]. The difference between these three checks is shown with labels in Figure 1: Surface checks are longitudinal cracks that occur along the wood ray, generating on the outer-tangential surface of plain-sawn timber. Internal checks split along the wood ray inside and can only be found when sawing off. End checks are cracks that occur at the end of the wood [34].


(a) (b) (c)


Figure 1. (a) Surface checks, (b) internal checks, (c) end checks.


Imperfect drying processes lead to defects and bad wood quality. Aggressive drying schedules make the situation worse, causing timber to crack or delaminate. Wood drying stress has been proved to be the major factor of drying defects and has become one of the indexes of drying quality.


Some techniques (e.g., pre-treatment) are normally used to eliminate stress, inhibit the occurrence of defects and improve the drying quality and drying efﬁciency of wood. Wood pre-treatment is to treat the wood before it is put into a drying oven or other drying equipment to prevent wood cracking. The method uses the elasticity and plasticity of wood to eliminate part of the growth stress, thereby reducing the possibility of wood bending and deformation, and improving the dimensional stability of wood. The media for pre-treating wood include water, steam, microwave, etc.


Relevant scholars have studied the influence of steam pre-treatment on wood drying rate and MC gradient. The research results show that steam pre-treatment can effectively accelerate the wood drying speed and alleviate the MC gradient during wood drying [35–37]. Steam pretreatment can shorten the drying cycle by varying degrees [38,39]. Lee et al. studied the effects of high-temperature and low-humidity pre-treatment, external load treatment and sapwood coating treatment on tangential stress and drying cracking during radio-frequency/vacuum drying of tree discs [40]. The results show that high-temperature and low-humidity pretreatment effectively avoids the occurrence of cracks on the wood surface, and external load treatment can reduce the probability of internal cracking. Ratnasingam et al. studied the effect of steam pre-treatment before drying on the drying quality of rubber wood, pointing out that steam pre-treatment for 10 h can effectively increase the drying rate and reduce drying defects [41].


<!-- Page 4 -->


Appl. Sci. 2021, 11, 5023 4 of 19


Microwave pre-treatment may significantly reduce the formation of internal/ honeycombing and surface checking in drying [42]. The experiment of Weng et al. witnessed the increase in the drying rate caused by microwave pre-treatment [43]. In Figure 2, it can be clearly seen that the drying time of the microwave pre-treatment sample is shorter than that of the control sample. The drying rate at an early stage was greatly increased after microwave pre-treatment, because the pre-treatment accelerated the moisture migration during the drying process, ensuring that a long-term evaporation interface was maintained at the wood surface at early stage. At the same time, acceleration of moisture movement improved the moisture distribution in the thickness direction and decreased the drying stress (Table 1).


Figure 2. Conventional drying curves of microwave-pre-treated and control wood samples [43].


Table 1. MC and residual stress index of microwave-pre-treated and control samples after drying.


MC Deviation in the


Residual Stress Index


Sample Final MC (%) Drying Uniformity


Thickness


(%)


(%)


(%)


Pre-treated quarter-sawn 8.55 ±0.54 1.34 ± 0.46 1.29 ± 0.44 Control quarter-sawn 9.23 ±0.87 2.58 ± 1.17 2.26 ± 0.85 Sig. — * * Pre-treated ﬂat-sawn 8.02 ±0.43 1.03 ± 0.27 1.28 ± 0.82 Control ﬂat-sawn 9.01 ±0.62 1.51 ± 0.38 2.49 ± 0.88 Sig. * * *


* means significant at 0.05 level, —means not significant at 0.05 level. Values of drying uniformity are standard deviations of the final MC [43].


Thermally modiﬁed timber can release part of the drying stress and reduce the recovery of deformation. Zhan studied the effect of thermal post-treatment on the residual stress and deformation of wood at 200 ◦C for 1 h treatment with atmospheric pressure superheated steam and believed that the residual stresses decreased somewhat after the thermal post-treatment [44].


Hou proposed that hot-press drying is beneﬁcial to reduce or eliminate the internal stress that causes warpage and deformation of the wood so that the wood remains ﬂat after drying [45]. From the perspective of porous mechanics, Scherer quantiﬁed the destructive stress generated during the supercritical CO2 drying process, which can not only take advantage of supercritical drying technology to avoid capillary forces, but also predict the risk of fracture defects [46]. Nevertheless, the above methods and techniques can only reduce part of the stress defects and distortion.


<!-- Page 5 -->


Appl. Sci. 2021, 11, 5023 5 of 19


## 2.2. The Generation and Development Mechanism of Wood Drying Stress


During wood drying, the generation of drying stress can be put down to uneven internal shrinkages and mutual restraint of adjacent layers. The main causes of uneven shrinkage are the MC gradient and the shrinkage anisotropy.


Ideally, assuming that the wood only produces an MC gradient along the thickness direction, the moisture on the surface of the wood will ﬁrst drop below the FSP at the beginning of drying, and shrinkage will occur, while the MC of the adjacent wood layer is still above the FSP and there is no shrinkage. Therefore, the unshrinking layer exerts tensile stress on the dried shrinkage layer, while the adjacent inner layer is subjected to compressive stress. Wood has viscoelasticity and plasticity. Wang et al. have proved that the wood would undergo plastic deformation and cracks (e.g., surface checks) when the tensile stress of the surface layer reaches the limit and becomes greater than the tensile strength of the surface layer [47–49].


In the middle stage of drying, the surface layer cannot fully shrink, forming casehardening, and accumulating a large amount of tensile residual deformation. The stress of the surface layer is reversed, and the core layer with MC over FSP is still under compressive stress, while the MC of the middle layer is lower than FSP and the tensile stress generates over there due to the restraint of the surface and the core layer.


In the later stage of drying, the internal layers with lower MC are suffering the force of surface compressive stress. When the internal tensile stress of the wood reaches the maximum and is greater than the internal tensile strength, internal checks will occur due to severe plasticizing deformation of the surface layer at the initial stage of drying.


The anisotropy of shrinkage refers to the difference between tangential shrinkage (T-Shr) and radial shrinkage (R-Shr) coefﬁcients. Fu et al. compared the development and distribution of the drying strain of Betula platyphylla Suk. under the sole effect of the shrinkage anisotropy and the joint effect of shrinkage anisotropy and moisture gradient [50]. The results indicate that when there was an MC gradient and the MC was lower than 26%, the actual shrinkage strain became lower, the viscoelastic creep strain was more easily recovered and diverted and the mechano-sorptive creep strain was signiﬁcantly reduced, while cracks and delamination became worse.


Uneven drying stress is also affected by temperature gradients. Liu designed a wood drying shrinkage force balance test system, testing the drying shrinkage development of Pinus sylvestris using different drying methods [51]. The results suggest that the drying rate of the specimens at higher temperatures could reach the stress equilibrium state faster, and the shrinkage force changed more remarkably. A study of high-frequency convection combined heating and drying by Song et al. proved that the strain of each layer of wood increased with the increase in temperature gradient during the early and middle stages of drying, and the middle layer was also signiﬁcantly affected by the temperature gradient in the middle of drying [52]. Additionally, growth stress and geometric growth characteristics will cause drying stress and deformation of wood as well.


## 2.3. Advances of the Wood Drying Stress Model


The wood drying stress model is a mathematical method to describe the causes and development of drying stress. The study of the drying stress model will provide a strong theoretical basis for the realization of drying stress control technology. Therefore, it has been highly valued by researchers for a long time.


Based on the ﬁnite difference method and successive iterations method, Ashworth quantiﬁed and calculated the drying stress of wood [28]. Morgan used the ﬁnite element method to calculate the drying stress of the wood and successfully simulated the stress transition phenomenon during the drying process [29]. Chen et al. established a model of water movement and strain of Pinus sapwood in high temperature drying (HTD) (temperature of the drying medium exceeds 100 ◦C). The mechanical hygroscopic strain and delayed elastic strain were considered in this model [48]. Salinas et al. tested and simulated the drying stress of Pinus radiata D. Don, and obtained the solutions by combining the method


<!-- Page 6 -->


Appl. Sci. 2021, 11, 5023 6 of 19


of volume control and ﬁnite element [53,54]. Then, a two-dimensional mathematical model of stress in the conventional drying process of eucalyptus was established based on the assumption of viscoelastic deformation [54].


The establishment and solution of drying stress and strain models need to be combined with diffusion theory. Wood drying is essentially a process of heat and mass transfer and internal stress development, and they are mutually coupled and correlated. The shrinkage is accompanied by changes in internal moisture migration path, moisture diffusion, thermal conductivity and other parameters accordingly. Truscott solved the thermal mass stress– strain coupling mathematical model by using the method of controlling the volume ﬁnite element [55]. Shi et al. established the residual stress model of the prestressed dry-grinding surface by the ﬁnite element method, and considered factors such as thermal ﬁeld and prestress in the model [56]. Due to the complexity of the actual drying process and the hypotheses of the models, to some extent, the calculated values from models are often quite different from the experimental values. However, in general, the mathematical model provides us with a powerful new idea of calculating drying stress quantitatively.


## 3. Composition of Drying Strain


At this stage, scholars are mainly studying wood drying stress and strain combined with rheological theories. It is generally believed that the total strain of wood drying includes the following parts: thermal strain εT, free shrinkage strain εF, elastic strain εE, viscoelastic creep strain εC and mechano-sorptive creep strain εM. During the drying process, wood will undergo thermal expansion or contraction under the inﬂuence of temperature. However, the resulting thermal strain εT is so small that it can be disregarded.


## 3.1. Free Shrinkage Strain


The free shrinkage of wood is the ideal shrinkage when wood is dried without any stress. When the MC is lower than FSP, the bound water in wood cell walls diffuses, the gaps between the ﬁbrils and microﬁbrils in the non-crystalline zones become smaller and the wood shrinks macroscopically. In the actual measurement of free shrinkage strain, the thin slice is usually used in low temperatures to maintain slow drying, so that the MC in the thin slice is distributed as evenly as possible.


Perre et al. used an optical microscope to detect the free shrinkage strain of Pseudotsuga menziesii and Picea asperata Mast. at the micro level, and then established a new model based on image processing and the Lattice Boltzmann Method to predict the stiffness and shrinkage values of wood during deformation by studying the microstructure characteristics [57,58]. Almeida et al. studied the linear relationship between shrinkage and MC of different tree species [59].


Kobayashi pointed out that the shrinkage differential is the difference between the actual drying shrinkage and the free shrinkage on wood surface [60]. Then, Tu and other scholars established a drying strain model of Pinus massoniana Lamb. using the drying shrinkage element, proving that the drying shrinkage differential is the decisive factor of the direction of drying stress [61]. It is concluded that when the shrinkage differential of the wood surface layer reaches the maximum, the drying rate is accelerated, and the time to reach its maximum value can be used as the evidence for the change of drying schedules. Kang studied the relationship between the tangential strain distribution and the drying behavior of Larix gmelinii (Rupr.) Kuzen. discs in the high-frequency/vacuum drying process and pointed out that the formation of cracking is closely related to the actual shrinkage differential [62].


## 3.2. Elastic Strain


Elastic strain refers to the strain that wood is subjected to by an external force within the range of its elastic limit and recovers immediately from when the force disappears. In the early stage of drying, as the MC decreases, the wood surface ﬁrst exhibits tensile deformation and then turns to compression deformation after reaching the limit [63].


<!-- Page 7 -->


Appl. Sci. 2021, 11, 5023 7 of 19


Surface checks occur as tensile deformation exceeds the limit value of the surface tensile elastic strain. The relationship between elastic stress δ and strain εE conforms to Hooke’s law and can be expressed by the following equation:


εE = δ E(W, T), (1)


where E is the static ﬂexural modulus in the transverse grain of wood, W is the moisture content and T is the temperature.


The modulus of elasticity (MOE) of wood is related to wood MC and temperature. When the MC is above FSP, the MC has a weak effect on MOE; when the MC is below FSP, the MOE is affected by the combined effect of MC and temperature. At this time, the MOE decreases as MC increases, and the effect of temperature is more complicated.


Bodig and Jayne pointed out that in the range of −40 to 80 ◦C, the MOE of wood with MCs of 12 and 23% generally decreases with increasing temperature, but the MOE of wood with an MC of 23% had a signiﬁcant step change at the freezing point [64]. Green et al. evaluated the MOE of wood with MCs of 4 and 12% in the temperature range of −26 to 66 ◦C (in Figure 3). They concluded that the decrease in MOE has a linear relationship with the increase in temperature, which is similar to the conclusion of Bodig et al. [65]. Gao further veriﬁed and explored the inﬂuence of temperature and MC on the MOE by using Pinus koraiensis Sieb. et Zucc. [66]. It was concluded that the relationship between MOE and the temperature of wood was based on the MC. The moisture state of wood cells is the essence of the changes in the mechanical properties of wood. When the MC is lower than FSP, the MOE of small specimens is not signiﬁcantly affected by the temperature below or above the freezing point. When the MC is higher than FSP, the MOE mainly responds to temperature. When the temperature drops below freezing point, the free water in wood cell vessels forms into ice crystals, resulting in MOE increasing rapidly; the decrease in MOE is relatively slow with temperatures above the freezing point.


Figure 3. Predicted-relationship between change in MOE and temperature at various MC levels. From Green et al. [65].


## 3.3. Viscoelastic Creep Strain


The creep phenomenon of wood is the hysteresis deformation behavior of elastic strain under stress, including viscoelastic creep (time-dependent), mechano-sorptive creep, pseudo creep and creep recovery [67].


Hanhijärvi’s research found that there was an interaction between viscoelastic creep and mechano-sorptive creep of Pinus sylvestris; in the recovery phase of the uniform wet cycle, due to the parallel effect of creep, a high-humidity cycle signiﬁcantly improved the


<!-- Page 8 -->


Appl. Sci. 2021, 11, 5023 8 of 19


creep recovery rate [68]. Han et al. tried to distinguish and separate the strain through the instantaneous deformation of the macro-slices. They obtained the viscoelastic coefﬁcient and the viscosity coefﬁcient from the established model, which is beneﬁcial to more accurately predict the stress and deformation at a speciﬁc time [69].


The viscoelastic creep strain is small and inﬂuenced by many factors, including MC, temperature and load time. Ranta-Maunus developed a theory of hydroviscoelasticity describing creep deformation due to variations in the MC [70]. The theory built a functional relationship between strain, stress and moisture history. Ranta-Maunus then discussed the material constants of the theory, and emphatically pointed out the creep limits in stress and MC for birch veneer and spruce. The effects of MC history and temperature were not studied experimentally. Similarly, Haque [71] established a mathematical model to study the viscoelastic creep strain of wood at different length rates and temperatures. Hering and Niemz used a four-point bending test device to study the development of viscoelastic creep strain of Fagus sylvatica at three different MCs [72]. The results indicate that the viscoelastic creep behavior is affected by the MC, and presents a linear relationship with MC.


## 3.4. Mechano-Sorptive Creep Strain


Armstrong [73] proposed ‘Mechano-Sorptive Creep’ for the ﬁrst time in 1960, and their experiments tried to determine to what extent the rate of loss or gain of moisture affected the creep rate and total creep. The mechanism of mechano-sorptive creep generation is that the change of MC causes the hydrogen bond to break and recombine under the action of external force [74]. The creep strain is related to temperature [75], load [76,77] and MC [78].


Li [79] explored the development of a drying strain of poplar wood during conventional drying and HTD through an improved slicing method. He selected four drying temperatures (85, 105, 115 and 125 ◦C). During the whole drying process, the dry and wet bulb temperature was kept constant, and the constant wind speed was 1.0 m/s. Table 2 and Figure 4 describe the change characteristics of mechanical adsorption creep strain. After reaching the maximum, the mechanical adsorption creep strain tends to be stable. The strain responds to temperature (especially high temperature), and the resulting permanent set (i.e., hardening) tends to hinder normal shrinkage in the later stage of drying and may cause internal checks. Therefore, the maximum value of the strain may be used as the basis for high-temperature and high-humidity intermediate treatment in the process.


Table 2. Maximum values of mechano-sorptive creep strain of surface wafer [79].


Drying Condition (◦C) Maximum (%) Time to Reach the Maximum (h)


85 1 3.65 5 105 4.96 5 115 3.14 3 125 4.23 1.5


1 The temperature of 85 ◦C is used to simulate conventional drying, and other temperatures are used to analyze HTD.


Bengtsson studied the bending creep variations of Picea abies during HTD and pointed out that the bending creep deformation of high-temperature (HT) dried wood is smaller than that of conventional low-temperature (LT) dried wood [80]. In Bengtsson’s research project, the HT drying was performed at a maximum temperature of 115 ◦C for approximately 30 h while the LT drying was performed at 70 ◦C for 168 h. According to the test results above, Honﬁet al. [81] model the mechano-sorptive creep of LT-dried and HT-dried timber beams by using a spring and a single Kelvin body. Figure 5 clearly shows us how the simulation matches the test results. Besides, signiﬁcant stress relief may occur along with the relatively high temperature of the wood and the slowdown of the moisture gradient [82]. Pang steam-dried Pinups radiata D. Don and pointed out that mechanosorptive creep affects the dimensional stability of wood during processing and use, which is beneﬁcial to release part of the drying stress [83].


<!-- Page 9 -->


Appl. Sci. 2021, 11, 5023 9 of 19


Figure 4. Mechano-sorptive creep strain changes with drying time [79].


Figure 5. Relative creep of the LT and HT specimens. Test (dashed lines) vs. Simulation (cont. lines) [81].


Zhan studied the dynamic free shrinkage behavior, as well as provided a theoretical basis for determining the mechanical-optical creep mechanism of drying. He sought to separate mechano-sorptive creep from viscoelastic creep deformation, and calculated the theoretical value of mechano-sorptive creep strain during conventional drying and post-drying conditioning stages [84,85].


4. Testing Methods of Wood Drying Stress and Strain 4.1. Commonly Used Testing Methods


Due to the complexity of wood structure and the drying mechanism, and the difﬁculty of controlling the drying environment, it is difﬁcult to study the drying stress of wood. Thus, in recent decades, scholars have focused on accurate and rapid measurement of drying stress and strain, and are committed to perfecting the drying stress and deformation test method.


In the 1950s, McMillen proposed to use the layered slicing method to measure the stress and strain along the thickness of the wood during the drying process (Figure 6a) [86]. Because of its simple operation, it is widely used in laboratory to quantitatively study the drying stress and deformation of wood in the transverse direction.


<!-- Page 10 -->


Appl. Sci. 2021, 11, 5023 10 of 19


(a) Slicing method (b) Prong method


Figure 6. Two commonly used testing methods of drying stress and strain. Dimensions are in mm [44].


In the 1970s, Japanese scholars proposed the Kapp method, that can continuously measure stress, but it can only qualitatively characterize the changes in the surface stress of wood [87]. Based on the Kapp method, Chang proposed a method using a non-contact probe to measure the deformation of Fraxinus mandshurica Rupr. to solve the problem of continuous stress measurement. Then, he calculated the stress based on the elastic modulus of the sample [88,89]. Later, An et al. designed a non-contact, non-destructive testing method for drying stress based on the principle of the digital speckle correlation method (DSCM) to detect stress [90]. Simpson proposed the prong test method to discuss the drying stress at different drying stages (Figure 6b) [25]. Then, Zhou et al. used the same method to ﬁnd that the residual stress is greater than the corresponding drying stress [91]. Stohr proposed a shrinkage differential approach that can measure the drying strain of wood continuously and non-destructively [27]. This method has the assumption that under the same drying conditions, the shrinkage of the tangential timber caused by the drying stress decreases with the reduction in the board’s tangential width. These experimental methods have limitations in experimental conditions and measurement accuracy, but they are still worthy of further research and improvement by scholars.


## 4.2. Modern Testing Methods


With the development of modern detection and scanning technology, the acoustic emission method, strain gauge method and optical method are gradually applied to determine the drying stress and strain of wood. The common point of these methods is to indirectly analyze the stress and strain in the drying process through the changes in the measured parameters. The principle of the method proposed by Skaar using acoustic emission is to estimate the stress change by sensing and measuring the size and frequency of the wave caused by the internal stress of wood drying [26]. Nasir uses accelerometers and acoustic emission sensors to detect the stress wave of wood to explore the physical and mechanical properties of thermally modiﬁed wood and the inﬂuence of wave speed and acoustic emission signals [92]. Cheng used a strain gauge sensor to study the relationship between stress and treatment temperature, MC and relative humidity during high-temperature steam drying of Cryptomeria fortune [93]. Muszynski measured the deformation of the sample under tensile action using optical pachymetry [94].


Modern technologies of DIC and NIRS provide a new opportunity for the study of drying stress and strain. The image analysis algorithm is a non-contact point distance measurement method based on image analysis, combined with the conventional slicing method [95]. As provided in Figure 7, the principle is to magnify the multiples of the collected image before measuring, which reduces the human error in the process of measuring the length with a micrometer or vernier caliper, and can obtain a higher-accuracy tangential strain. Han et al. [96] completed the measurement of transverse shrinkage with DIC (Figure 8a). As shown in Figure 8b, the shrinkage at the tissue level was also measured


<!-- Page 11 -->


Appl. Sci. 2021, 11, 5023 11 of 19


in the speciﬁc parts including the cell walls and pores to monitor the little drying stress of a small, thin specimen. Fu et al. used the image analysis method to calculate the length of the specimen and analyzed the stress state at different MC stages during the drying process and the relationship between stress and each strain [97]. We can use NIRS equipment to evaluate the surface moisture content of wood [96,98,99]. Recently, it has been used to investigate surface drying stress and strain during wood drying [100].


Figure 7. Digital image acquisition device.


(a) Virtual grid of 35 markers used for DIC. (b) Virtual grid of about 330 markers used for


DIC of a 30-µm-thick slice.


Figure 8. Images collected with DIC. The purposes of image collection: (a) measurement of transverse shrinkage, (b) measurement of shrinkage at the tissue level. From Han et al. [96].


Combining the literature review abovementioned, it is not difﬁcult to see that whether it is a direct or indirect measurement of drying stress and strain, the accuracy and speed of the measurement will be the focus of current and future research. As the mainstream and classic method of stress and strain detection in the wood drying process, the slicing method is simple to operate and is favored by researchers. However, insufﬁcient accuracy and human error in the measurement are indeed unavoidable problems. Although the use of modern technology and equipment requires higher costs, it provides new opportunities for stress and strain detection and research.


<!-- Page 12 -->


Appl. Sci. 2021, 11, 5023 12 of 19


5. Artiﬁcial Neural Network and Its Application in the Field of Wood Drying 5.1. Artiﬁcial Neural Network (ANN)


The artiﬁcial neural network is a network structure built by the interaction of a great many processing units [101]. Its source of inspiration is the biological neuron theory, as exhibited in Figure 9. Neurons, as the basic unit of information processing in the nervous system, can effectively communicate, integrate, input and output information. The ANN model is built to imitate the biological nervous system. It has excellent structural variability, fault tolerance, adaptability and learning ability. It can be used to solve a series of intricate and non-linear problems, so it is widely used in image processing, face recognition, actual production, control and many other research ﬁelds.


(a)


(b)


Figure 9. (a) Biological neuron model, (b) artiﬁcial neuron model.


5.2. Back Propagation (BP) Neural Network Structure and Algorithm 5.2.1. BP Neural Network Structure


Neural networks can be considered as multiple neurons connecting and interacting with each other, and can generally be divided into feedforward neural networks, feedback neural networks, self-organizing neural networks and stochastic neural networks. The BP neural network is a multi-layer feedforward neural network. Its network structure includes an input layer, a hidden layer (usually one) and an output layer, as shown in Figure 10. The layers are connected by weights. Inevitable errors in the learning process will be tested in the network learning training through this algorithm. Error minimization can be achieved by adjusting and correcting the weights between layers.


<!-- Page 13 -->


Appl. Sci. 2021, 11, 5023 13 of 19


Figure 10. BP neural network structure.


## 5.2.2. BP Neural Network Algorithm


In the forward propagation signal of the three-layer network, the number of units is assumed to be i, j and k, respectively. x1, x2, x3, . . ., xi are input values of the input layer; h1, h2, h3, . . ., hj are output values of the hidden layer; y1, y2, y3, . . ., yk are output values of the output layer; and d1, d2, d3, . . ., dk are the expected outputs. Assume that vij is the weight matrix of the input layer and the hidden layer, wjk is the weight matrix of the hidden layer and the output layer, θj and θk are the thresholds of the hidden layer unit and the output layer unit, respectively, and hj and yk are output signals of each unit in the hidden layer and the output layer. Thereout, we can get the following equations:


i i=1 vijxi −θj] (2)


hj = f[∑


j i=1 wjkhj −θk] (3)


yk = f[∑


The sigmoid as the activation function is commonly chosen for calculation and back propagation of related errors until the predetermined target learning error is reached. The problems of the BP neural network algorithm include large ﬂuctuations in the convergence speed, a minimum value in the application function and the difﬁculty in determining the number of hidden layers and the number of nodes in hidden layers. Many researchers have proposed improved methods by adding momentum terms, using input normalization and quasi-Newton algorithms.


## 5.3. Application of ANNs in the Field of Wood Drying


The application of ANNs in the ﬁeld of wood science is late, but has a rapid development. Researchers have successively conﬁrmed the powerful simulation and prediction capabilities of artiﬁcial neural networks:


Avramidis’s research team made use of ANNs to estimate the thermal conductivity of wood under conditions of different MC, temperature and apparent density [30]. In the following year, a neural network that could predict the dielectric loss factor of wood based on the basic chemical properties of wood was successfully developed [102]. They also discussed the feasibility of artiﬁcial network models in predicting the static bending strength, elastic modulus and density of wood [103,104].


Fernández’s research group tested wood MC, density and ultrasonic propagation speed to predict the elastic modulus of ﬁr; then, four neural networks were established to predict and determine the physical and mechanical properties of plywood (board thickness, MC, speciﬁc gravity, bending strength and MOE) [31,105].


Tiryaki’s team studied the strength properties of thermally modiﬁed wood. The method adopted was to establish a model with the input parameters of wood type, heat treatment temperature and heat treatment time to predict the compressive strength, elastic


<!-- Page 14 -->


Appl. Sci. 2021, 11, 5023 14 of 19


modulus and modulus of rupture of heat-treated wood. The results suggest that compared with multiple regression analysis, the ANN model has good predictive performance [106]. After that, they also simulated and predicted the modulus of rupture and modulus of elasticity of the particleboard under different pressing conditions [107].


Nguyen et al. used temperature, treatment time and wood type as the input layer, and wood hardness as the output layer [108]. The measurement coefﬁcient (R2) of all data sets obtained is greater than 0.99, and the prediction is more effective. In the following year, they once again proved the plasticity and developability of the artiﬁcial neural network model by predicting the color change of heat-treated wood during the artiﬁcial weathering process [109].


In the aspect of wood drying, the ANN model also shows its predictive effect. The researchers used wood MC and drying stress as the output variable matrix, and made a reasonable three-layer ANN model through the BP neural network algorithm, aiming to predict the characteristics of wood drying more accurately.


Avramidis et al. successively determined the diffusion of water under non-isothermal conditions by using ANNs [11,110]. Ceylan combined artiﬁcial neural networks and mathematical models to predict and analyze the MC of poplar and pine [111]. Zhang established a time-delay neural network model to explore the correlation between wood MC, drying temperature and humidity. Meanwhile, she tracked and predicted wood MC dynamically [112,113].


Watanabe et al. used ANN theory to simulate and predict the ﬁnal MC of air-dried wood by setting the input variables of the initial MC, basic density, annual ring orientation, annual ring width, heartwood ratio and wood lightness, and compared with the principal component regression model. They found the ANN prediction model has better performance, and the predicted value is closer to the actual measured value [12]. Based on the near-infrared spectroscopy technology, they established an artiﬁcial neural network model to predict and analyze the dry stress on the wood surface [114]. Compared with the partial least squares model, the time required to reach the maximum tensile stress and the direction of the stress reversal of the near-infrared spectroscopy model are basically anastomotic with the experiment value. The prediction of the near-infrared spectroscopy model is better.


Bedelean tried to predict the value of the radio frequency heating rate and found that the MC has a greater impact on the radio frequency heating rate [115]. Heating the wood in groups of different MCs can reduce the possibility of deformation or cracking caused by uneven heating. Through experiments and training models, Ma predicted that the overall ﬁtting accuracy of larch wood MC was 96.86% [116]. This model can be applied to wood drying of other tree species under the same conditions. Chai et al. input four parameters of drying time, measuring point location, internal temperature and pressure of wood into the BP neural network model, and predicted the MC of wood during the high-frequency/vacuum drying process [117]. Afterwards, Fu inspected the distribution of drying stress from the pith to the bark during the conventional drying process and predicted wood elastic strain and mechano-sorptive creep strain, respectively [118]. The results prove that the prediction was excellent. In the future, there is considerable feasibility for ANN in the prediction of drying stress and strain.


## 6. Conclusions and Prospects


Advanced technology has been applied to eliminate as much stress as possible. Nevertheless, current methods and techniques can only reduce part of the stress defects and distortion. Although the prong and slicing methods cannot measure drying stress inprocess, they are used practically in the research and industry of wood drying. Modern technologies such as digital images and near-infrared detection are also widely used in the measurement of wood drying stress and strain. Future research should maybe focus on the new technology, which can measure the drying stress of wood rapidly, accurately and continuously.


<!-- Page 15 -->


Appl. Sci. 2021, 11, 5023 15 of 19


This paper put forward three prospects: (1) The wood drying stress analysis should combine with the theory of heat and mass transfer during drying and deeply investigate the coupling of them. The theory of microscopic cell wall mechanics also should combine with the macroscopic drying theory to explore the mechanisms of stress and deformation; (2) It is necessary to establish a more perfect image acquisition and analysis system to realize the real-time monitoring of drying strain and cracking practically; and (3) A reasonable prediction model of wood drying stress and strain should be established.


This article mainly reviews the research progress of wood drying stress and strain. The next step of our research is dedicated to the pursuit of real-time, accurate and efﬁcient related detection techniques. Moreover, there are few studies on the prediction of drying strain based on ANN models, which also suggests how highly exploratory the prediction of the ANN model is. Therefore, we will verify the drying strain-related ANN model on the basis of the research results to obtain more accurate prediction results.


Author Contributions: Conceptualization, H.-H.L.; investigation, Q.Y.; resources, Q.Y.; writing— original draft preparation, Q.Y.; writing—review and editing, Q.Y., H.-H.L.; visualization, Q.Y.; supervision, H.-H.L.; project administration, H.-H.L.; funding acquisition, H.-H.L. All authors have read and agreed to the published version of the manuscript.


Funding: This research was funded by the National Natural Science Foundation of China, grant number 31870545, and the Key Laboratory of Bio-based Material Science and Technology (Northeast Forestry University), Ministry of Education, grant number SWZ-MS201903. The APC was funded by SWZ-MS201903.


Conﬂicts of Interest: The authors declare no conﬂict of interest.


## References


1. Liu, X.Y.; Lv, M.Q.; Liu, M.; Lv, J.F. Repeated humidity cycling’s effect on physical properties of three kinds of wood-based panels. Bioresources 2019, 14, 9444–9453. Available online: https://ojs.cnr.ncsu.edu/index.php/BioRes/article/view/BioRes_14_4_9444_ Liu_Humidity_Cycling_Wood_Panels/7219 (accessed on 12 December 2020). 2. Liu, X.Y.; Tu, X.W.; Liu, M. Effects of light thermal treatments on the color, hygroscopity and dimensional stability of wood. Wood Res. 2021, 66, 95–104. Available online: http://www.woodresearch.sk/wr/202101/09.pdf (accessed on 7 May 2021). [CrossRef] 3. Wan, Y.; Hou, S.J.; Guo, M.Y.; Fu, Y.C. Surface Properties of Spray-Assisted Layer-By-Layer ElectroStatic Self-Assembly Treated Wooden Take-Off Board. Appl. Sci. 2021, 11, 836. Available online: https://www.mdpi.com/2076-3417/11/2/836 (accessed on 7 May 2021). [CrossRef] 4. Liu, Y.; Hu, J. Investigation of polystyrene-based microspheres from different copolymers and their structural color coatings on wood surface. Coatings 2021, 11, 14. Available online: https://www.mdpi.com/2079-6412/11/1/14 (accessed on 2 May 2021). [CrossRef] 5. Zhao, Z.; Sakai, S.; Wu, D.; Chen, Z.; Zhu, N.; Huang, C.; Sun, S.; Zhang, M.; Umemura, K.; Yong, Q. Further exploration of sucrose–citric acid adhesive: Investigation of optimal hot-pressing conditions for plywood and curing behavior. Polymers 2019, 11, 1996. Available online: https://www.mdpi.com/2073-4360/11/11/1875 (accessed on 12 December 2020). 6. Xiong, X.Q.; Ma, Q.R.; Yuan, Y.Y.; Wu, Z.H.; Zhang, M. Current situation and key manufacturing considerations of green furniture in China: A review. J. Clean. Prod. 2020, 267, 121957. [CrossRef] 7. Lu, X.R.; Teng, Q.C.; Li, Z.R.; Zhang, X.L.; Wang, X.M.; Komatsu, K.H.; Que, Z.L. Study on shear property of spruce glulam and steel plate connected with inclined screw. J. For. Eng. 2020, 5, 48–53. Available online: https://qzl.njfu.edu.cn/kindeditor/ attached/ﬁle/20200514/20200514215442524252.pdf (accessed on 20 December 2020). 8. Gao, X.; Zhou, F.; Fu, Z.Y.; Zhou, Y.D. Analysis of rosin in pine wood by time domain nuclear magnetic resonance. J. For. Eng. 2019, 4, 42–47. [CrossRef] 9. Telkki, V.V.; Yliniemi, M.; Jokisaari, J. Moisture in softwoods: Fiber saturation point, hydroxyl site content, and the amount of micropores as determined from NMR relaxation time distributions. Holzforschung 2013, 67, 291–300. [CrossRef] 10. Ma, E.N.; Wang, W.; Li, X.; Yang, T.T. The States of Water in Wood during Drying Process Studied by Low-Field Nuclear Magnetic Resonance (LFNMR). Sci. Silvae Sin. 2017, 53, 111–117. Available online: http://www.linyekexue.net/CN/abstract/abstract7626. shtml (accessed on 15 April 2021). (In Chinese) 11. Rostom, L.; Caré, S.; Courtier-Murias, D. Analysis of water content in wood material through 1D and 2D 1H NMR relaxometry: Application to the determination of the dry mass of wood. Magn. Reson. Chem. 2021, 59, 614–627. Available online: https: //analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/mrc.5125 (accessed on 15 April 2021). [CrossRef] 12. Avramidis, S.; Wu, H. Artiﬁcial neural network and mathematical modeling comparative analysis of nonisothermal diffusion of moisture in wood. Holz Roh Werkstoff 2007, 65, 89–93. [CrossRef]


<!-- Page 16 -->


Appl. Sci. 2021, 11, 5023 16 of 19


13. Liu, Y.; Zhou, X.L.; Hu, Z.K.; Yu, Y.B.; Yang, Y.T.; Xu, C.Y. Wood defect recognition based on optimized convolution neural network algorithm. J. For. Eng. 2019, 4, 115–120. [CrossRef] 14. Broda, M. Natural Compounds for Wood Protection against Fungi—A Review. Molecules 2020, 25, 3538. Available online: https://www.mdpi.com/1420-3049/25/15/3538 (accessed on 2 February 2020). [CrossRef] [PubMed] 15. Broda, M.; D ˛abek, I.; Dutkiewicz, A.; Dutkiewicz, M.; Popescu, C.-M.; Mazela, B.; Maciejewski, H. Organosilicons of different molecular size and chemical structure as consolidants for waterlogged archaeological wood—A new reversible and retreatable method. Sci. Rep. 2020, 10, 2188. [CrossRef] 16. Broda, M.; Mazela, B.; Dutkiewicz, A. Organosilicon compounds with various active groups as consolidants for the preservation of waterlogged archaeological wood. J. Cult. Herit. 2019, 35, 123–128. Available online: https://www.sciencedirect.com/science/ article/pii/S1296207418302462 (accessed on 2 February 2020). [CrossRef] 17. Lisuzzo, L.; Hueckel, T.; Cavallaro, G.; Sacanna, S.; Lazzara, G. Pickering Emulsions Based on Wax and Halloysite Nanotubes: An Ecofriendly Protocol for the Treatment of Archeological Woods. ACS Appl. Mater. Interfaces 2021, 13, 1651–1661. [CrossRef] 18. Yang, L.; Han, T.Q.; Fu, Y.D. Effect of Heat Treatment and Wax Impregnation on Dimensional Stability of Pterocarpus Macrocarpus wood. Wood Res. 2020, 65, 963–974. Available online: http://www.woodresearch.sk/wr/202006/10.pdf (accessed on 12 December 2020). [CrossRef] 19. Tiemann, H.D. Effect of Moisture on the Strength and Stiffness of Wood; J Frankl Associates, Inc.: New York, NY, USA, 1906; Volume 162, pp. 465–466. Available online: https://www.sciencedirect.com/science/article/pii/S0016003206902658 (accessed on 12 December 2020). 20. Stamm, A.J. Review of nine methods for determining the ﬁber saturation points of wood and wood products. Wood Sci. 1971, 4, 114–128. 21. Hoffmeyer, P.; Engelund, E.T.; Thygesen, L.G. Equilibrium moisture content (EMC) in Norway spruce during the ﬁrst and second desorptions. Holzforschung 2011, 65, 875–882. [CrossRef] 22. Engelund, E.T.; Thygesen, L.G.; Svensson, S.; Hill, C.A.S. A critical discussion of the physics of wood–water interactions. Wood Sci. Technol. 2013, 47, 141–161. [CrossRef] 23. Brischke, C.; Alfredsen, G. Wood-water relationships and their role for wood susceptibility to fungal decay. Appl. Microbiol. Biotechnol. 2020, 104, 3781–3795. Available online: https://www.ncbi.nlm.nih.gov/pubmed/32144473 (accessed on 2 February 2020). [CrossRef] 24. Pang, S. Mathematical Modeling of Kiln Drying of Softwood Timber: Model Development, Validation, and Practical Application. Dry. Technol. 2007, 25, 421–431. [CrossRef] 25. Simpson, W.T. Dry kiln operator’s manual. In Agriculture Handbook; U.S. Department of Agriculture, Forest Service, Forest Products Laboratory: Madison, WI, USA, 1991; Available online: https://www.woodweb.com/knowledge_base/Dry_kiln_ operators_manual.html?fb_locale=fr_FR (accessed on 12 December 2020). 26. Skaar, C.; Simpson, W.T.; Honeycutt, R.M. Use of acoustic emissions to identify high levels of stress during oak lumber drying. For. Prod. J. 1980, 30, 21–22. [CrossRef] 27. Stöhr, H.P. Shrinkage differential as a measure for drying stress determination. Wood Sci. Technol. 1988, 22, 121–128. [CrossRef] 28. Ashworth, J.G. The Mathematical Simulation of Drying of Softwood Timber. Ph.D. Thesis, University of Canterburg, Christchurch, New Zealand, 1977. 29. Morgan, K.; Thomas, H.R.; Lewis, R.W. Numerical modeling of stress reversal in timber drying. Wood Sci. 1982, 15, 139–149. 30. Avramidis, S.; Liadis, L. Predicting wood thermal conductivity using artificial neural networks. Wood Fiber Sci. 2005, 37, 682–690. Available online: https://www.mendeley.com/catalogue/366618fd-0598-3982-b4e0-966d4a94d0b6/ (accessed on 11 October 2020). 31. Fernández, F.; Esteban, L.G.; Palacios, P.D.; Casasús, A. Use of artiﬁcial neural networks in timber engineering: Calculating modulus of elasticity using non-destructive testing. In Proceedings of the 11th World Conference on Timber Engineering, Riva del Garda, Italy, 20–24 June 2010; pp. 66–72. 32. Desch, H.E.; Dinwoodie, J.M. Timber: Structure, Properties, Conversion and Use, 7th ed.; Macmillan Press: London, UK, 1996; 306p. 33. Haque, N. Delamination in timber induced by drying. In Delamination in Wood, Wood Products and Wood-Based Composites; Bucur, V., Ed.; Springer: Cham, Switzerland, 2007; p. 212. 34. Gao, J.M.; Wang, X.M. Wood Drying, 2nd ed.; Science Press: Peking, China, 2018; pp. 104–133. 35. Campbell, G.S. The value of pre-steaming for drying some collapse-susceptible Eucalypts. For. Prod. J. 1961, 11, 343–347. 36. Chen, P.Y. The effect of steaming time and temperature on the longitudinal permeability of black walnut. Wood Fiber 1975, 7, 222–225. 37. Simpson, W.T. Effect of pre-steaming on moisture gradient of northern red oak during drying. Wood Sci. 1976, 8, 272–276. 38. Alexiou, P.N.; Marchant, J.F.; Groves, K.W. Effect of pre-steaming on moisture gradients, dryinag stresses and sets, and face checking in regrowth Eucalyptus pilularis Sm. Wood Sci. Technol. 1990, 24, 201–209. [CrossRef] 39. Alexiou, P.N.; Wilkins, A.P.; Hartley, J. Effect of pre-steaming on drying rate, wood anatomy and shrinkage of regrowth Eucalyptus pilularis Sm. Wood Sci. Technol. 1990, 24, 103–110. [CrossRef] 40. Lee, N.H.; Li, C.; Zhao, X.F.; Park, M.J. Effect of pretreatment with high temperature and low humidity on drying time and prevention of checking during radio-frequency/vacuum drying of Japanese cedar pillar. J. Wood Sci. 2010, 56, 19–24. [CrossRef] 41. Ratnasingam, J.; Grohmann, R.; Scholz, F. Effects of pre-steaming on the drying quality of Rubberwood. Eur. J. Wood Wood Prod. 2014, 72, 135–137. [CrossRef]


<!-- Page 17 -->


Appl. Sci. 2021, 11, 5023 17 of 19


42. Harris, G.; Torgovnikov, G.; Vinden, P.; Brodie, G.; Shaginov, A. Microwave Pretreatment of Backsawn Messmate Boards to Improve Drying Quality: Part 1. Dry. Technol. 2008, 26, 579–584. [CrossRef] 43. Weng, X.; Zhou, Y.; Fu, Z.; Gao, X.; Zhou, F.; Jiang, J. Effects of microwave pretreatment on drying of 50 mm-thickness Chinese ﬁr lumber. J. Wood Sci. 2021, 67, 1–9. [CrossRef] 44. Zhan, J.F.; Avramidis, S. Impact of conventional drying and thermal post-treatment on the residual stresses and shape deformations of larch lumber. Dry. Technol. 2017, 35, 15–24. [CrossRef] 45. Hou, J.F.; Zhou, Y.D. The research status and application prospects of wood hot-press drying. World For. Res. 2017, 30, 41–45. (In Chinese) 46. Scherer, G.W. Stress and strain during supercritical drying. J. Sol Gel Sci. Technol. 2019, 90, 8–19. [CrossRef] 47. Wang, H.H.; Youngs, R.L. Drying Stress and Check Development in the Wood of two Oaks. IAWA J. 1996, 17, 15–30. [CrossRef] 48. Chen, G.; Keey, R.B.; Walker, J.C.F. The drying stress and check development on high-temperature kiln seasoning of sapwoodPinus radiata boards: I. Moisture movement and strain model. Holz Roh Werkstoff 1997, 55, 59–64. [CrossRef] 49. Chen, G.; Keey, R.B.; Walker, J.C.F. The drying stress and check development on high-temperature kiln seasoning of sapwoodPinus radiata boards: II. Stress development. Holz Roh Werkstoff 1997, 55, 169–173. [CrossRef] 50. Fu, Z.; Zhao, J.; Huan, S.; Sun, X.; Cai, Y. The variation of tangential rheological properties caused by shrinkage anisotropy and moisture content gradient in white birch disks. Holzforschung 2015, 69, 573–579. Available online: https://www.researchgate.net/ publication/282551406 (accessed on 11 October 2020). [CrossRef] 51. Liu, J.X. Research of Wood Drying Shrinkage Development Process and Drying Contraction Stress. Master’s Thesis, Inner Mongolia Agricultural University, IMAR, China, 2017. 52. Song, T.Y.; Fu, Z.F.; Cai, Y.C. The effect of high-frequency-convection combined heating and drying on wood temperature gradient and drying quality. J. Nor. For. Univ. 2018, 46, 74–79. (In Chinese) 53. Salinas, C.; Chavez, C.; Ananias, R.A.; Elustondo, D. Unidimensional Simulation of Drying Stress in Radiata Pine Wood. Dry. Technol. 2015, 33, 996–1005. [CrossRef] 54. Salinas, C.H.; Chávez, C.A.; Pérez-Peña, N.; Vargas, H.; Ananías, R.A. Two-dimensional simulation of mechanical stresses during isothermal drying of Eucalyptus nitens wood. Wood Sci. Technol. 2020, 54, 187–201. [CrossRef] 55. Truscott, S.L.; Turner, I.W. A heterogeneous three-dimensional computational model for wood drying. Appl. Math. Model. 2005, 29, 381–410. Available online: https://www.sciencedirect.com/science/article/pii/S0307904x04001040 (accessed on 20 October 2020). [CrossRef] 56. Shi, X.L.; Xiu, S.C.; Su, H.L. Residual stress model of pre-stressed dry grinding considering coupling of thermal, stress, and phase transformation. Adv. Manuf. 2019, 7, 401–410. [CrossRef] 57. Perré, P.; Huber, F. Measurement of free shrinkage at the tissue level using an optical microscope with an immersion objective: Results obtained for Douglas ﬁr (Pseudotsuga menziesii) and spruce (Picea abies). Ann. For. Sci. 2007, 64, 255–265. [CrossRef] 58. Perré, P.; Almeida, G.; Ayouz, M.; Frank, X. New modelling approaches to predict wood properties from its cellular structure: Image-based representation and meshless methods. Ann. For. Sci. 2016, 73, 147–162. [CrossRef] 59. Almeida, G.; Assor, C.; Perré, P. The Dynamic of Shrinkage/Moisture Content Behavior Determined During Drying of Microsamples for Different Kinds of Wood. Dry. Technol. 2008, 26, 1118–1124. [CrossRef] 60. Kobayashi, I. Application of surface strain reasoning for wood drying. In Proceedings of the 7th International IUFRO Wood Drying Conference, Tsukuba, Japan, 9–13 July 2001; pp. 336–341. 61. Tu, D.Y. Research on Drying Stress Model and Strain Continuous Measurement of Masson Pine Board. Ph.D. Thesis, Nanjing Forestry University, Nanjing, China, 2005. 62. Kang, W.; Lee, N.H. Relationship between radial variations in shrinkage and drying defects of tree disks. J. Wood Sci. 2004, 50, 209–216. [CrossRef] 63. Li, C.Y.; Lee, N.H. Effect of compressive load on shrinkage of larch blocks during radio-frequency vacuum heating. Wood Fiber Sci. 2004, 36, 9–16. 64. Bodig, J.; Jayne, B.A. Mechanics of Wood and Wood Composites; Krieger Publishing: Malabar, FL, USA, 1982. 65. Green, D.W.; Evans, J.W. The immediate effect of temperature on the modulus of elasticity of green and dry lumber. Wood Fiber Sci. 2008, 40, 374–383. 66. Gao, S.; Wang, X.P. The inﬂuence of temperature and moisture state on the ﬂexural elastic modulus of American Korean pine. J. For. Eng. 2014, 28, 38–42. (In Chinese) 67. Sun, L.W.; Bian, Y.L.; Zhou, A.P.; Zhu, Y. Study on short-term creep property of bamboo scrimber. J. For. Eng. 2020, 5, 69–75. [CrossRef] 68. Hanhijärvi, A.; Hunt, D. Experimental indication of interaction between viscoelastic and mechano-sorptive creep. Wood Sci. Technol. 1998, 32, 57–70. [CrossRef] 69. Han, Y.; Yang, S.Y.; Park, J.H.; Chang, Y.S.; Eom, C.D.; Yeo, H. Separation of drying strains and the calculation of drying stresses considering the viscoelasticity of red pine wood during drying. Dry. Technol. 2017, 35, 1858–1866. [CrossRef] 70. Ranta-Maunus, A. The viscoelasticity of wood at varying moisture content. Wood Sci. Technol. 1975, 9, 189–205. [CrossRef] 71. Haque, M.N.; Langrish, T.A.G.; Keep, L.B.; Keey, R.B. Model ﬁtting for visco-elastic creep of Pinus radiata during kiln drying. Wood Sci. Technol. 2000, 34, 447–457. [CrossRef]


<!-- Page 18 -->


Appl. Sci. 2021, 11, 5023 18 of 19


72. Hering, S.; Niemz, P. Moisture-dependent, viscoelastic creep of European beech wood in longitudinal direction. Eur. J. Wood Wood Prod. 2012, 70, 667–670. [CrossRef] 73. Armstrong, L.D.; Kingston, R.S. Effect of Moisture Changes on Creep in Wood. Nature 1960, 185, 862–863. [CrossRef] 74. Hunt, D.G. Dimensional changes and creep of spruce, and consequent model requirements. Wood Sci. Technol. 1997, 31, 3–16. [CrossRef] 75. Wu, Q.L.; Milota, M.R. Rheological behavior of Douglas-ﬁr perpendicular to the grain at elevated temperatures. Wood Fiber Sci. 1995, 27, 285–295. 76. Pérez-Peña, N.; Cloutier, A.; Segovia, F.; Salinas-Lira, C.; Sepúlveda-Villarroel, V.; Salvo-Sepúlveda, L.; Elustondo, D.M.; Ananías, R.A. Hygromechanical strains during the drying of Eucalyptus nitens boards. Maderas Cienc. Tecnol. 2016, 18, 235–244. Available online: http://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-221x2016000200001&nrm=iso (accessed on 25 October 2020). [CrossRef] 77. Pérez-Peña, N.; Segovia, F.; Salinas, C.; Ananias, R. Perpendicular Mechano-Sorptive Strains during Moisture Desorption from Eucalyptus nitens Specimens. BioResources 2016, 11, 8277–8284. [CrossRef] 78. Mårtensson, A. Mechano-sorptive effects in wooden material. Wood Sci. Technol. 1994, 28, 437–449. [CrossRef] 79. Li, D.G.; Gu, L.B. Study on rheological behavior of surface layer of poplar during high-temperature drying. Sci. Silvae Sin. 1999, 35, 85–91. Available online: http://www.linyekexue.net/article/1999/1001-7488/19990114.shtml (accessed on 12 December 2020). (In Chinese) 80. Bengtsson, C.; Kliger, R. Bending Creep of High-Temperature Dried Spruce Timber. Holzforschung 2003, 57, 95–100. [CrossRef] 81. Honﬁ, D.; Mårtensson, A.; Thelandersson, S.; Kliger, R. Modelling of bending creep of low- and high-temperature-dried spruce timber. Wood Sci. Technol. 2013, 48, 1–14. [CrossRef] 82. Erickson, R.W.; Seavey, R.T. Energy Quantication and mechano-sorptive behavior in the kiln drying of 2.5 cm thick Red Oak lumber. Dry. Technol. 1992, 10, 1183–1206. [CrossRef] 83. Pang, S. Modelling of stress developent during drying and relief during steaming in pinus radiata lumber. Dry. Technol. 2000, 18, 1677–1696. [CrossRef] 84. Zhan, J.F.; Avramidis, S. Mechanosorptive Creep of Hemlock under Conventional Drying: I. The Determination of Free Shrinkage Strain. Dry. Technol. 2011, 29, 789–796. [CrossRef] 85. Zhan, J.F.; Avramidis, S. Mechanosorptive Creep of Hemlock Under Conventional Drying: II. Description of Actual Creep Behavior in Drying Lumber. Dry. Technol. 2011, 29, 1140–1149. [CrossRef] 86. Mcmillen, J.M. Drying stress in wood drying. For. Prod. J. 1955, 5, 230. 87. Nishio, S. KAP Method Drying Stress Estimation; Wood Industry: Tokyo, Japan, 1972; p. 27. 88. Chang, J.M. Research on non-contact testing methods of wood drying stress. In Proceedings of the 6th National Wood Drying Symposium, Beijing, China, 27–31 August 1997. 89. Chang, J.M.; Hu, S.T.; Run, Y.Z. Research on Non-contact Testing Method of Wood Drying Stress. For. Prod. Ind. 1998, 5, 21–24. (In Chinese) 90. An, L.; Gao, J.M.; Hu, C.K. Non-contact non-destructive testing method for wood drying stress. For. Environ. Sci. 2007, 23, 63–66. (In Chinese) 91. Zhou, F.; Fu, Z.; Zhou, Y.; Zhao, J.; Gao, X.; Jiang, J. Moisture transfer and stress development during high-temperature drying of Chinese ﬁr. Dry. Technol. 2020, 38, 545–554. [CrossRef] 92. Nasir, V.; Nourian, S.; Avramidis, S.; Cool, J. Stress wave evaluation for predicting the properties of thermally modiﬁed wood using neuro-fuzzy and neural network modeling. Holzforschung 2019, 73, 827–838. [CrossRef] 93. Cheng, W.L.; Liu, Y.X.; Shi Gang, M.L. Tensile stress relaxation of wood under high temperature and high pressure steam conditions. J. Beijing For. Univ. 2007, 29, 84–89. (In Chinese) 94. Muszy´nski, L.; Lagana, R.; Shaler, S.M. An optical method for characterization of basic hygro-mechanical properties of solid wood in tension. In Proceedings of the 8th International IUFRO Wood Drying Conference, Brasov, Romania, 24–29 August 2003; pp. 77–82. 95. Rice, R.W.; Youngs, R.L. The mechanism and development of creep during drying of red oak. Holz Roh Werkstoff 1990, 48, 73–79. [CrossRef] 96. Han, Y.; Park, Y.; Park, J.H.; Yang, S.Y.; Eom, C.D.; Yeo, H. The shrinkage properties of red pine wood assessed by image analysis and near-infrared spectroscopy. Dry. Technol. 2016, 34, 1613–1620. [CrossRef] 97. Fu, Z.Y.; Zhao, J.Y.; Cai, Y.C. Measurement and analysis of strain caused by anisotropy of trunk shrinkage. Eng. Sci. 2014, 16, 25–29. (In Chinese) 98. Tsuchikawa, S.; Hayashi, K.; Tsutsumi, S. Nondestructive Measurement of the Subsurface Structure of Biological Material Having Cellular Structure by Using Near-Infrared Spectroscopy. Appl. Spectrosc. 1996, 50, 1117–1124. [CrossRef] 99. Yang, S.Y.; Han, Y.; Chang, Y.S.; Kim, K.M.; Choi, I.G.; Yeo, H. Moisture Content Prediction Below and Above Fiber Saturation Point by Partial Least Squares Regression Analysis on Near Infrared Absorption Spectra of Korean Pine. Wood Fiber Sci. 2013, 45, 415–422. 100. Watanabe, K.; Kobayashi, I.; Saito, S.; Kuroda, N.; Noshiro, S. Nondestructive evaluation of drying stress level on wood surface using near-infrared spectroscopy. Wood Sci. Technol. 2013, 47, 299–315. [CrossRef]


<!-- Page 19 -->


Appl. Sci. 2021, 11, 5023 19 of 19


101. Hagan, M.T.; Demuth, H.B.; Beale, M.H.; De Jesús, O. Neural Network Design, 2nd ed.; Hagan, M.T., Ed.; University of Kansas: Lawrence, KS, USA, 2002; pp. 23–54. Available online: http://hagan.okstate.edu/nnd.html (accessed on 12 December 2020). 102. Avramidis, S.; Iliadis, L.; Mansﬁeld, S.D. Wood dielectric loss factor prediction with artiﬁcial neural networks. Wood Sci. Technol. 2006, 40, 563. [CrossRef] 103. Mansﬁeld, S.D.; Iliadis, L.; Avramidis, S. Neural network prediction of bending strength and stiffness in western hemlock (Tsuga heterophylla Raf.). Holzforschung 2007, 61, 707–716. [CrossRef] 104. Iliadis, L.; Mansﬁeld, S.D.; Avramidis, S.; El-Kassaby, Y.A. Predicting Douglas-ﬁr wood density by artiﬁcial neural networks (ANN) based on progeny testing information. Holzforschung 2013, 67, 771–777. [CrossRef] 105. Fernández, F.G.; de Palacios, P.; Esteban, L.G.; Garcia-Iruela, A.; Rodrigo, B.G.; Menasalvas, E. Prediction of MOR and MOE of structural plywood board using an artiﬁcial neural network and comparison with a multivariate regression model. Compos. Part B 2012, 43, 3528–3533. Available online: https://www.sciencedirect.com/science/article/pii/S1359836811005233 (accessed on 30 November 2020). [CrossRef] 106. Tiryaki, S.; Aydın, A. An artiﬁcial neural network model for predicting compression strength of heat treated woods and comparison with a multiple linear regression model. Constr. Build. Mater. 2014, 62, 102–108. [CrossRef] 107. Tiryaki, S.; Aras, U.; Kalaycıo˘glu, H.; Eri¸sir, E.; Aydın, A. Predictive Models for Modulus of Rupture and Modulus of Elasticity of Particleboard Manufactured in Different Pressing Conditions. High Temp. Mater. Process. 2017, 36, 623–634. [CrossRef] 108. Van Nguyen, T.H.; Nguyen, T.T.; Ji, X.; Lanh Do, K.T.; Guo, M. Using Artiﬁcial Neural Networks (ANN) for Modeling Predicting Hardness Change of Wood during Heat Treatment. IOP Conf. Ser. Mater. Sci. Eng. 2018, 394, 032044. [CrossRef] 109. Nguyen, T.T.; Van Nguyen, T.H.; Ji, X.; Yuan, B.; Trinh, H.M.; Do, K.T.L.; Guo, M. Prediction of the color change of heat-treated wood during artiﬁcial weathering by artiﬁcial neural network. Eur. J. Wood Wood Prod. 2019, 77, 1107–1116. [CrossRef] 110. Schmid, M. Discussion of: “Artiﬁcial neural network and mathematical modeling comparative analysis of nonisothermaldiffusion of moisture in wood” by Stavros Avramidis and Hongwei Wu. Holz Roh Werkstoff 2008, 66, 71–73. [CrossRef] 111. Ceylan, ˙I. Determination of Drying Characteristics of Timber by Using Artiﬁcial Neural Networks and Mathematical Models. Dry. Technol. 2008, 26, 1469–1476. [CrossRef] 112. Zhang, D.Y.; Liu, Y.X.; Cao, J.; Sun, L.P. Modeling of temperature-humidity for wood drying based on time-delay neural network. J. For. Res. 2006, 17, 141–144. [CrossRef] 113. Zhang, D.Y.; Sun, L.P.; Cao, J. Neural Network Prediction Model of Wood Moisture Content for Drying Process. Sci. Silvae Sin. 2008, 44, 94–98. [CrossRef] 114. Watanabe, K.; Kobayashi, I.; Matsushita, Y.; Saito, S.; Kuroda, N.; Noshiro, S. Application of Near-Infrared Spectroscopy for Evaluation of Drying Stress on Lumber Surface: A Comparison of Artiﬁcial Neural Networks and Partial Least Squares Regression. Dry. Technol. 2014, 32, 590–596. [CrossRef] 115. Bedelean, B.; Lazarescu, C.; Avramidis, S. Predicting RF heating rate during pasteurization of green softwoods using artiﬁcial neural networks and Monte Carlo method. Wood Res. 2015, 60, 83–94. Available online: http://www.centrumdp.sk/wr/201501 /08.pdf (accessed on 5 December 2020). 116. Ma, X.Y.; Wang, X.F.; Duan, W.Y. Research on BP Neural Network Model of Larch Wood Drying. For. Eng. 2015, 31, 63–65. (In Chinese) 117. Chai, H.; Chen, X.; Cai, Y.; Zhao, J. Artiﬁcial Neural Network Modeling for Predicting Wood Moisture Content in High Frequency Vacuum Drying Process. Forests 2019, 10, 16. [CrossRef] 118. Fu, Z.Y.; Cai, Y.C.; Gao, X.; Zhou, F.; Jiang, J.H.; Zhou, Y.D. Simulation and prediction of wood drying strain based on artiﬁcial neural network model. Sci. Silvae Sin. 2020, 56, 76–82. Available online: http://www.linyekexue.net/article/2020/1001-7488/2 0200608.shtml (accessed on 20 December 2020).
