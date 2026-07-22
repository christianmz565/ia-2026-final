# ramos2021-industry40-wood


<!-- Page 1 -->


We are IntechOpen, the world’s leading publisher of


Open Access books Built by scientists, for scientists


## 132,000 160M


5,400


Open access books available


International  authors and editors


Downloads


Our authors are among the


12.2%


## TOP 1% 154


Countries delivered to Contributors from top 500 universities


most cited scientists


Selection of our books indexed in the Book Citation Index


in Web of Science™ Core Collection (BKCI)


Interested in publishing with us? Contact book.department@intechopen.com


Numbers displayed above are based on latest data collected.


For more information visit www.intechopen.com


<!-- Page 2 -->


Chapter Trends and Opportunities of Industry 4.0 in Wood Manufacturing Processes


Mario Ramos-Maldonado and Cristhian Aguilera-Carrasco


## Abstract


Wood industry is key for sustainability and an important economic activity in many countries. In manufacturing plants, wood variability turns operation management more complex. In a competitive scenario, assets availability is critical to achieve higher productivity. In a new fourth industrial revolution, Industry 4.0, data engineering permits efficient decisions making. Phenomena difficult to model with conventional techniques are turned possible with algorithms based on artificial intelligence. Sensors and machine learning techniques allow intelligent analysis of data. However, algorithms are highly sensitive of the problem and his study to decide on which work is critical. For the manufacturing wood processes, Industry 4.0 is a great opportunity. Wood is a material of biological origin and generates variabilities over the manufacturing processes. For example, in the veneer drying, density and anatomical structure impact the product quality. Scanners have been developed to measure variables and outcomes, but decisions are made yet by humans. Today, robust sensors, computing capacity, communications and intelligent algorithms permit to manage wood variability. Real-time actions can be achieved by learning from data. This paper presents trends and opportunities provided by Industry 4.0 components. Sensors, decision support systems and intelligent algorithms use are reviewed. Some applications are presented.


Keywords: wood manufacturing, industry 4.0, multiple sensors, bigdata, machine learning


## 1. Introduction


In industrialized nations, manufacturing has become a key growth factor. “Great Britain was the first industrializer and became the technological leader of the world economy. Manufacturing became the main engine of the economic growth in the 19th century, spreading manufacturing production technologies to other countries” [1]. Digital manufacturing (Artificial Intelligence, bigdata analytics, cloud computing, among others) is changing the nature of manufacturing production. The adoption of these technologies (by developing countries) can foster inclusive and sustainable industrial development and the achievement of the Sustainable Development Goals [2].


Wood industry is key for sustainability and an important economic activity in many countries. In recent years, manufactured wood products for construction


1


<!-- Page 3 -->


Engineered Wood Products for Construction


have had special relevance. These represent 38.1% of wood-based products worldwide [3].


As a biological material, wood is variable in its physical and anatomical properties. Wood mechanical or chemical transformation processes are affected. In manufacturing processes, process variables must be managed to achieve quality and productivity standards. In industrial systems, productivity and product quality are affected by multiple variables. The “wood material” adds an additional complexity degree. Traditionally, human experience has been able to control many variables and maintain the operating system. However, the human capacity has limits and to use sensors and computers is needed to help online decision-making.


For decades, multiple sensors for generic physical variables such as pressure, speed, or temperature have been developed. Specific sensors capable of measuring and characterizing wood, including destructive and non-destructive testing, have been developed. For industrial use in manufacturing process control nondestructive characterization is the most important. This allows monitoring and control (usually by humans) the process in real time. In a competitive scenario, to achieve higher operating factors, lack assets availability is critical. To have in real time information on the operational behavior allows online decision-making. Lack of data and its analysis does not allow to forecast and prescribe operation behaviors and improve performance. Decision-making has become more complex, uncertain, and rapidly changing external conditions. However, the use of online data in industrial settings is still incipient. Computing power and robust algorithms capable of predicting behavior in complex environments using data are recent.


The fourth industrial revolution presents great opportunities for wood manufacturing processing. Sensor’s development, high computing capacity, industrial internet (Internet of Things, IoT) and learning algorithms can allow a much better handling of uncertainty and material variability. Algorithms based on artificial intelligence make possible online decisions and prediction of phenomena that are difficult to model with conventional techniques. Sensor’s availability and Machine Learning techniques allow the intelligent capture, display, and data analysis [4, 5]. Machine Learning (and Deep Learning) uses the history of data, of positive or negative experiences to model real processes and automatically conclude for other situations. The choice of the algorithms depends to the problem. Therefore, new opportunities are open for academia and industry to improve the industrial wood processing. Studying appropriate performant models and determining which variables and which sensors to use, among other considerations, are part of the data engineering and futures research work.


This work presents the industry 4.0 scopes, components, and opportunities for the wood industrial manufacturing. Data collection and engineering are the focus. Some author’s examples are shown.


## 2. Industry 4.0 and components


In recent decades, the industry has evolved toward more intensive use of digital technologies. And this has passed from traditional automation to a new industrial revolution, the fourth industrial revolution or Industry 4.0. The first revolution was the introduction of mechanization and steam power. The second was the incorporation of mass production and division of labor. And the third revolution incorporated electronics, automation and CAX (Computer Aided X) technologies.


The 1980s changed the direction of industrial production policies. Taylorian mass production evolved toward a production of a variety of products, with costs


2


<!-- Page 4 -->


Trends and Opportunities of Industry 4.0 in Wood Manufacturing Processes DOI: http://dx.doi.org/10.5772/intechopen.99581


like those of the production of large quantities. In 1990s, the focus was on integrating manufacturing automation technologies mainly robotics, CNC (Computer Numerical Control), CAD / CAM (Computer Aided Design/ Computer Aided Engineering), and automatic control (Advanced Manufacturing Technologies). Computer Integrated Manufacturing (CIM) emphasized data integration into the production cycle of the firm, it was the third industrial revolution [6]. Manufacturing evolved from the intensive labor use in traditional manufacturing to a sophisticated set of processes based on information technology [4].


In 2011, Industry 4.0 emerges as a focus of the competitiveness of Germany’s industry [7]. It is defined as networks that incorporate Cyber-Physical Systems that handle bigdata and use Artificial Intelligence. Industry 4.0 is based on developments of the last 20 years, at least four: research in artificial intelligence, better computing capacity and speed, internet development and wireless communication. For example, the combination of distributed systems, self-organizing systems and artificial intelligence was the prelude to what today in industry 4.0 is known as Cyber-Physical Systems [8–11].


Data science and artificial intelligence would be the “core” of Industry 4.0 [2]. The consequences are the virtual factory (or digital twin) and autonomous machines (Cyber-physical Systems) capable of interacting “intelligently” with other machines and humans [12]. Data analysis (data science) makes it possible to make decisions and predict dynamic phenomena that are difficult to model with conventional techniques. Industry 4.0 is the data revolution, especially in the manufacturing industry [13]. Today object is about the massive use of data and analysis for the design and operation of industrial systems.


## 2.1 Components


Many authors have defined components part of this fourth revolution. Some place more emphasis on hardware devices and others on software elements. However, both data and automatic analysis are the base and more common denominator: the data science approach. Several methodologies exist to drive data projects, but in general that consists in fourth steps: to know the problem, to understand the data, to extract features and to model an analyze [14]. Data engineering is complementary and fundamental to achieve implementations: from data capture to the action over the physical system. First task in data engineering is to make available data: to select sensors, to process signals and to generate descriptors and data warehouse. Second, it is to know the physical processes, to understand and visualize data and to extract features. And finally, tasks are modeling and implementation for actions (Figure 1).


Figure 1. Data engineering process.


3


<!-- Page 5 -->


Engineered Wood Products for Construction


Without data engineering 4.0 technologies would not be possible. In this work, four technological components are visited: Industrial Internet, Cloud Computing, Virtual Factory and Cyber-Physical Systems.


## 2.1.1 Industrial internet (II)


II Is to use the internet for industrial purposes. All is called Internet of Things (IoT). An IoT system consists of Industrial Wireless Networks (IWN) and Internet of Things (IoT) [15]. It includes machines and equipment, networks, the cloud, and terminals. “Things” and “objects” interact with each other and cooperate to achieve common goals. “IoT is capable of offering specific and personalized products. Users can customize products via web pages. Then, web servers transmit data to the industrial cloud and plants via wired or wireless networks” [5]. 5G technology will allow high speeds of communication and industrial internet feasible.


Also, it is possible to define Internet of Services (IoS). IoS allows providers to offer their services over the Internet. “IoS is emerging, based on the idea that services are made easily available through web technologies, allowing companies and private users to combine, create and offer new kind of value- added services” [16].


## 2.1.2 Cloud computing (CC)


CC is a set of resources, including physical servers, networks, storage, and user applications accessible from Internet [17]. CC is a new concept. it is a collection of configurable computing services to be made accessible and released as specified [18]. It also allows easy and on-demand network access. Different networks, servers, storage, applications, and services resources are disponible today. Services providers, e.g., Microsoft Azure, Alibaba Cloud, Amazon, and Google Cloud, provide access through the internet. Clients pay only for the resources they use. CC services are one crucial components of the Industry 4.0 including IoT and CPSs [19].


## 2.1.3 Cyber-physical system (CPS)


CPS comprise intelligent devices capable of exchanging information autonomously, causing actions and controlling each other independently. “CPS are systems of collaborating computational entities which are in intensive connection with the surrounding physical world and its on-going processes, providing and using, at the same time, data-accessing and data-processing services available on the Internet” [20]. CPS is an integration of computation with physical world. Computers monitor and control the physical processes. Feedback loops act where physical processes affect computations and vice versa [21, 22]. Software and hardware with sensor and action are integrated (Figure 2).


## 2.1.4 Virtual factory (VF)


VF is defined as a virtual model that assists people and machines in the execution of their tasks. They are systems that work in the background. In 1993, the VF concept was introduced by Onosato and Iwata [23]. VF It considers the actual context information such as the position and state of an object. In a virtual factory, the CPS perform tasks, communicate, and take those actions to the real world of the plant [9]. VF include virtual organization, emulation facility and integrated simulation. In [24]. VF is defined “as an integrated simulation model of major subsystems in a factory that considers the factory as a whole and provides an advanced decision


4


<!-- Page 6 -->


Trends and Opportunities of Industry 4.0 in Wood Manufacturing Processes DOI: http://dx.doi.org/10.5772/intechopen.99581


Figure 2. CFS: Interaction of agents [10].


support capability.” Virtual models can guide physical entities responding to the changes in their environment and to improve operations [25].


A similar concept, Digital Twin (DT) has been proposal. In [26] DT a production line is integrated with the real production processes using a simulation model. Real-time interaction between virtual and physical world allows DTs to respond to unexpected changes in manufacturing processes more rapidly [23].


## 3. Manufacturing processes in the wood industry


## 3.1 Manufacturing and process industry


It is “manufacturing, any industry that makes products from raw materials using manual labour or machinery and that is usually carried out systematically with a division of labour. In a more limited sense, manufacturing denotes the fabrication or assembly of components into finished products on a fairly large scale” [27]. Many authors difference manufacturing and process industry [28].


Manufacturing is a discrete system and uses machines or workstations to change forms, dimensions, or surfaces. Lines or cells assembly parts to obtain final products. Process industry is a continuous system and put emphasis over chemical processes, or batch like reaction, heat, cold, to generate final product liquid, gas or solid. In the forest industry, manufacturing is concerned to the “solid” wood transformation and process industry more with pulp and paper industry.


## 3.2 Wood transformation


The first wood transformation begins with the log after harvest. In the sawmill industry the main product is dry sawn wood. In the board industry products are veneers, flakes, particles, and fibers. Second transformation generates appearance and engineering products such as moldings, furniture parts, plywood, CLT (Cross Laminated Timber), OSB (Oriented Strands Board) and particle or fiberboard. Different operations can be considered: milling, molding, peeling, pressing, drying, gluing, painting, among others.


Main operations of the manufacturing industry are cutting operations that produce changes in shape, dimensions, and surfaces. Wood is an anisotropic material, but it is treated as an orthotropic material. Its mechanical properties change on the radial,


5


<!-- Page 7 -->


Engineered Wood Products for Construction


tangential and longitudinal axes. This affects the “cutting” behavior according to the direction of the stress of the cutting tool [29]. Similarly, anatomy, density, singularities, and moisture content impact product quality and productivity. For example, well known is the effect of properties and species on the drying of lumber or veneer.


In cutting with or without chip, the tool interaction with the material produces cutting forces that release energy producing pressure waves and tool wear [29]. In the sawmill and remanufacturing industry, tool wear directly affects production costs due to its negative effects on dimensional and surface quality of the product. In sawmill, cutting forces wear the tooth on all faces, increasing friction. Friction changes heat and cutting angles producing inefficient cut over time. The surface quality increases its roughness.


Wear and heat of tool lead to loss of rigidity increasing kerf and dimensional inaccuracy.


In longitudinal sawing, working angles α, β and γ of the cutting tool, geometry, feed per tooth, the feed and cutting speed movement must be optimized (Figure 3). These and other variables depend on the properties of the wood and the cutting height. In high productivity sawmilling feeding speeds of over 120 m / min are driven, correct monitoring and control in real time is key. In [30], factors involved in the sawing process are classified into three categories: (1) workpiece, (2) feed, and (3) tool. Combined effects are analyzed showing a complete review of studies. Here, emphasis is to put the sensor to allow online prediction and intelligent monitoring systems and increase the productivity.


## 3.3 Main factors


For wood manufacturing processes, influencing factors are the material, the operation, and the transformation technology. In cutting processes, factors are combined, the cutting tool being important. These impact on assets, rotating mechanisms, landings, materials, motors, auxiliary systems, and other devices. Heat and mechanical power impact machine availability. In sawing, saws fatigue generates cracks and microcracks in the bottom of the blade throat. Vibrations impact on clamping and feeding systems acting on the products dimensional accuracy [31].


Figure 3. A typical sawmill tool and material interaction.


6


<!-- Page 8 -->


Trends and Opportunities of Industry 4.0 in Wood Manufacturing Processes DOI: http://dx.doi.org/10.5772/intechopen.99581


Figure 4. Factors in a sawmill monitoring.


In other manufacturing operations such as drying, painting, gluing, or pressing, heat and mass transfer phenomena, adhesion and stress-deformation intervene. For example, in veneer continuous drying, air velocity, steam temperature and feed rate determine the cracks presence and the product moisture content. For years, for different species different transformation technologies have been studied. For sawmill, main factors are presented Figure 4.


## 4. Data engineering and wood manufacturing processes


## 4.1 Sensors and data in wood manufacturing


To make available data is a key task. Unfortunately, many industrial environmental have not yet all availability. Wood industries are not the exception. To measure power, temperatures, tool wear, pressions, velocities, vibrations and physical and wood anatomical characteristics requires robust sensors. Today, dimensions, moisture, density and many wood and panels defects can be tested online. Indirectly certain critical variables can be quantified. That is especially important when these variables depend on more conventional measurable physical phenomena (e.g., electrical variables, temperatures, vibrations, sound, etc.). In [32], cutting and feed per tooth are correlate with acoustic emission and saw temperature. In mechanical operations, cutting forces explain good machining behavior [33, 34]. In general, tool wear can be related indirectly with heat liberation, power consummation vibrations or acoustic emission.


In the plywood industry, peeling cutting forces with vibrations, acoustic emission and artificial vision can be correlated [33]. Cutting in particle panels can be explained by power consummation [34]. For milling, [35] show that sound and vibrations can be used to predict the online surface quality. For P. radiata, both acoustic emission and electric power to predict surface quality are showed in [36].


7


<!-- Page 9 -->


Engineered Wood Products for Construction


In [37], microwaves are used to detect knots and log defect using laser are shown in [38]. Others researches on non-destructive test exist.


In the same order, many superficial wood characteristics can be measured by artificial vision techniques [39, 40]. Today, industrial scanners can extract different knout types and singularities, colors, timber edger and in certain applications X-ray determines internal defects [41–43]. In the panel industry, dimensions, density, and panel moisture are captured online. To classify veneers, scanner test splits, discoloration, and holes. However mechanical properties are yet tested outline.


Several industrial applications are today available. For example, in sawmills, vision and laser are used to capture the logs true shape and the dimensions of boards (by companies like USNR, MPM and Microtec). Many modern sawmills around the word are users of these technologies. X-rays was yet developed for logs, probably Microtec is a company leader over this segment. To detects wood defects, both internal and external, to board in second transformation applications exist. Main suppliers are Weining, GreCon and Microtec with WoodEye©.


In the wood manufacturing industry, normally scanners aide to control specifical and local operation like parts classification, first cutting in sawmill or thickness mat on particle or fiber panels. Yet, data is non stocked for analysis or to create prediction models. World class wood producers are beginning to use and collect real-time data to extract information and add value (interviews and experiences of the authors).


## 4.2 Artificial intelligence


Artificial Intelligence (AI) or more specific Machine Learning (ML) is the core of industry 4.0 [44]. Artificial Intelligent has been defined by E. Rich like “the study of how to make computers do things at which, at the moment, people are better” [45]. If it is believed that intelligence is only a human property. Another Langton’s definition of intelligence involves all living system [46]. A prominent AI area is Machine Learning (ML) consisting in the capacity to learn to solve problems. ML is the study of computer algorithms that improve automatically through experience [47]. And experience are historical data. Last years, Deep Learning (DL) is a new approach and area of ML. In DL, news algorithms using multi-layer artificial neural network work [48]. ML and DL permit today successful applications and an increase considerable research in many fields.


Complex structure of bigdata can be discovery using DL technics like Convolutional Neural Network (CNN) [49, 50]. Support Vector Machine, Random Forest or Bayes technics work on an important set of problems. However, CNN are advantageous to extract features of industrial bigdata [48]. Computing capacity and bigdata turn possible DL technics to industrial systems applications [51–53].


To wood industry several authors have showed advances using ML. In [54], plywood defects are classified by Support Vector Machine (SVM). In [55], wood quality is automatically classified. In [35], Neural Networks like cutting prediction is used. Recurrent Neural Networks (RNN) is special type of Neural Network. Pass knowledge can be used to learning and predict. In [56], by RNN productivity prediction of a high production sawmill is modeled.


In ML, practice and testing are keys. Data engineering methodologies are important to validate complex problems having many variables and non-lineal relations [52]. Choice of model’s hyperparameters, learning and evaluation data size can become decisive to achieve good performances. Learning data sizes can be different according to the problem. Always, more data is better. Fortunately, in industrial environments data can be “bigdata”. To validate models, data size can go from some miles to millions.


8


<!-- Page 10 -->


Trends and Opportunities of Industry 4.0 in Wood Manufacturing Processes DOI: http://dx.doi.org/10.5772/intechopen.99581


Figure 5. Data collection in a drying veneer process.


Figure 6. Multispectral data process to classify industrial melamine panels [58, 59].


## 4.3 Cases: ML and data collection


Studies in sawmill industrial process show that RNN to predict productivity with 30,000 records 0.8 of coefficient of determination can be obtained [56]. To classify veneer quality in a plywood continuous industrial drying using Neural Network and Random Forest 6,000 records allowed accuracies over O.8 [57]. In this case, online data collection was implemented to stock veneers, operation, and technology variables. Raw data was pre-process and filtered and a data set warehouse was generated. Material factors considered dimensions, moisture, and forest origin. Operations taken account feed and batch sizes. Drying technology variables were different important factors like steam temperature, pressions and opening. Response was veneer quality (Figure 5).


In a melamine particle panels industry too much money can be lost if the final product classification is not good. Using computer vision, multispectral sensors, cloud computing and ML algorithms it is possible to classify panels with 0.95 of accuracy (Figure 6). Multi sensor and data integration permit better performances. More of 14,000 records were used to learning and testing.


## 5. Conclusions


Benefices and components of Industry 4.0 was presented. Focus is on data engineering. Data analysis, Machine Learning and Deep Learning are in the core of Industry 4.0. Availability of sensors, better computing processor and wireless communication turn possible this new revolution and great opportunities for manufacturing industries. IoT is beginning. 5G technology will allow high speeds of communication and industrial internet feasible. Computing cloud represents


9


<!-- Page 11 -->


Engineered Wood Products for Construction


opportunities for Small and Medium Enterprises too. Lower cost can be obtained when data processing and stockage is done in the cloud. CFS are still in growth and ML models to autonomous computing are showing auspicious and robust. Virtual factory (digital twin) is subject of a series of investigations. Prototypes of virtual reality and simulation models using real-time data is a reality.


In the wood manufacturing industry, last year, research contributions toward 4.0 techniques have been focuses in developing no-destructive sensors and models. Most of the investigations have been driven into the labs. But industry 4.0 woks with data, bigdata. Learning and testing ML models requires a lot of experiences. Industry to increase productivity and product quality need robust algorithms working within hazard environment to carry out intelligent actions. Either actions to aide decision making or automatic control. ML or DP models must be performants. The authors argue that it is necessary to approach academy and producers. Experience is fundamental to understanding data. The fourth revolution is the data revolution. In this context, researcher and practitioners should be overcome three factors: know the wood, understand the process, and use data engineering methodologies.


## Acknowledgements


Authors thank to: Research Office of University of Bio-Bio, Chile: Research Project 2060360 IF/R, Machine Learning and Vision Computer Group and Intelligent Industry and Complex System Research Group; CORFO-Chile Agency; FONDEF-IDEA of R&D National Agency of Chile (ANID), Project ID14I20364; Project CYTED TICs4CI: Applications TICS for Intelligent Cities; Arauco Company; MASISA Company; Biobio Manufacturers Association (AGMET); Wood Engineering Department at the University of Bio-Bio.


Author details


Mario Ramos-Maldonado* and Cristhian Aguilera-Carrasco University of Bio-Bio, Concepcion, Chile


*Address all correspondence to: mramos@ubiobio.cl


© 2021 The Author(s). Licensee IntechOpen. This chapter is distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/ by/3.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


10


<!-- Page 12 -->


Trends and Opportunities of Industry 4.0 in Wood Manufacturing Processes DOI: http://dx.doi.org/10.5772/intechopen.99581


## References


[1] Szirmai A. Industrialization as an engine of growth in developing countries. Structural Change and Economic Dynamics, 1950-2005. 2012; (23): 406-420


[2] United Nations Industrial Development Organization, 2019. Industrial Development Report 2020. Industrializing in the digital age. Vienna: 2019. 206 p.


[3] Ramage M, Burridge H, Wicher M, Fereday G, Thomas R, Shah D, Guanglu W, Li Y, Fleming P, & Densley D, Allwood J, Dupree P, Linden P.F, Scherman O. The wood from the trees: The use of timber in construction. Renewable and Sustainable Energy Reviews. 2017; 68. 333-359. DOI: 10.1016/j.rser.2016.09.107.


[4] Shipp S, Gupta N, Lal B, Scott J.A, Weber C. L, Finnin M. S, Blake M, Newsome S, Thomas S. Emerging Global Trends in Advanced Manufacturing. Virginia, USA: Institute for Defense Analyses; March 2012


[5] Lu Y. Industry 4.0: A survey on technologies, applications, and open research issues. Journal of Industrial Information Integration. 2017; 6: 1-10


[6] Rembold U, Nnaji B.O, Storr A. Computer integrated manufacturing and engineering. Addison-Wesley; 1996. 640 P.


[7] Hermann M, Pentek T, Boris O. Design Principles for Industrie 4.0 Scenarios: A Literature Review. Technische Universität Dortmund: Working Paper No. 01; 2015


[8] Van Brussel H, Bongaerts L, Wyns J. Valckenaers P, Van Ginderatcher T. A conceptual framework for holonic manufacturing: identification of manufacturing holons, Journal of Manufacturing Systems. 1999; Vol. 18


11


Issue 1: 35-52. DOI:10.1016/S0278-6125 (99)80011-9


[9] Patriti V, Schäfer K, Ramos M, Charpentier P, Martin P, Veron M. Multi-agent and manufacturing: A multilevel point of view. In Plonka F, Olling G, editors. Computer Applications in Production and Engineering. CAPE 1997. IFIP — The International Federation for Information Processing, Boston, MA: Springer 1998. p. 47-57 DOI/10. 1007/978-0-387-35291-6_50


[10] Ramos, M. Vers un pilotage autoorganisant de systèmes flexibles de fabrication [Thèse de Docteur]. Nancy, France: Université Henri Poincaré Nancy I; 1998.


[11] Ramos M, Maness T, Salinas D. Modelo de un sistema multi-agente para la optimización de la cadena de suministros en la industria de la madera de coníferas. Maderas: Ciencia y tecnología. 2015; 17(3): 613 – 624, DOI:10.4067/S0718-221X20150050 00054


[12] Pranab K. Muhuri, Amit K. Shukla, Ajith Abraham. Industry 4.0: A bibliometric analysis and detailed overview. Engineering Applications of Artificial Intelligence. 2019; 78: 218-235


[13] McKinsey Global Institute, Manufacturing the future: The next era of global growth and innovation. Report, November 2012


[14] Martinez I, Viles G. Data Science Methodologies: Current Challenges and Future Approaches. Big Data Research. 2021; Volume 24, 100183. DOI: 10.1016/j. bdr.2020.100183.


[15] Lin F, Chen C, Zhang N, Guan X, Shen X. Autonomous channel switching: towards efficient spectrum sharing for industrial wireless sensor networks.


<!-- Page 13 -->


Engineered Wood Products for Construction


IEEE Internet Things J. 2016; 3 (2): 231-243


[16] . Wahlster W, Grallert H.J, Wess S, Friedrich H, Widenka T. (Eds.). Towards the Internet of Services. Switzerland: The THESEUS Research Program, Springer;2014


[17] Mohamed A, Hamdan M, Khan S, Abdelaziz A, Babiker S, Imran M, Marsono M.N. Software-Defined Networks for Resource Allocation. In: Cloud Computing: A Survey, Computer Networks; 2021. 108151, DOI: 10.1016/j. comnet.2021.108151


[18] Mell P, Grance T. The NIST definition of cloud computing. National Institute of Standards and Technology. Inf. Technol. Lab. Version; 2009, 915 (10.07)


[19] Arwa M, Mosab M, Khan S, Abdelaziz A, Babiker S, Imran M, Marsono M.N. Software-Defined Networks for Resource Allocation in Cloud Computing: A Survey, Computer Networks (2021), DOI: 10.1016/j. comnet.2021.108151


[20] Monostori L, Kadar B, Bauernhansl T, Kondoh S, Kumara S, Reinhart G, Ueda K. Cyber-physical systems in manufacturing, CIRP Ann.-Manuf. Technol; 2016; 65 (2): 621-641


[21] Lee E. A. Cyber physical systems: design challenges. In: Proceedings of 11th IEEE Symposium on Object Oriented Real-Time Distributed Computing (ISORC), May 5-7; 2008 Orlando, FL: IEEE; 2008: 363-369


[22] Ramos M, Duran-Faundez C, Monsalve D, Aguilera C. Towards an Agent-Based Control of a CyberPhysical Production System using JADE: The CIMUBB Case. In: International Conference of Production Research, ICPR- Americas 2016 January 2016 [Internet]. 2020 Available from: https://


12


www.researchgate.net/publication/ 314283737_Towards_an_Agent-Based_ Control_of_a_Cyber-Physical_ Production_System_using_JADE_The_ CIMUBB_Case


[23] Yildiz E, Møller C, Bilberg A. Virtual Factory: Digital Twin Based Integrated Factory Simulations, Procedia CIRP; 2020 Volume 93: 216-221. DOI: 10.1016/j.procir.2020. 04.043


[24] Jain S, Choong N. F, Aye K. M, Luo M. Virtual factory: an integrated approach to manufacturing systems modeling. Int. J. Oper. Prod. Manag. 2001; vol. 21, N° 5/6: 594-608


[25] Schluse M, Rossmann J. From simulation to experimentable digital twins: Simulation-based development and operation of complex technical systems. ISSE 2016 - 2016 Int. Symp. Syst. Eng. - Proc. Pap.; 2016


[26] Vachálek J, Bartalský L, Rovný O, Šišmišová D, Morháč M, Lokšík M. The Digital Twin of an Industrial Production Line Within the Industry 4.0 Concept. In: 21st International Conference on Process Control (PC). 2017: 258-262


[27] Britannica, The Editors of Encyclopedia. "Manufacturing". Encyclopedia Britannica, [Internet]. 2021. Available from: https://www. britannica.com/technology/ manufacturing.


[28] Russell R, Taylor B. Operations Management. USA: Prentice Hall; 2011, 810 p


[29] Koch, P. Wood Machining Processes. USA: The Ronald Press Company; 1964. 530p


[30] Aguilera C, Ramos M, Roa G. An Automatic Grading System for Panels Surfaces Using Artificial Vision. International Journal of Computers,


<!-- Page 14 -->


Trends and Opportunities of Industry 4.0 in Wood Manufacturing Processes DOI: http://dx.doi.org/10.5772/intechopen.99581


Communications & Control. 2006; Vol. I, N° 2: 15-22


[31] Nasir V, Cool J. A review on wood machining: Characterization, optimization, and monitoring of the sawing process, Wood Material Science & Engineering. 2018; 15(3):1-16. DOI: 10.1080/17480272.2018.1465465


[32] Hutton S. G, Taylor J. Operating stresses in band saws and their effects on fatigue life. Journal of Forestry Production. 1999; 141, 7: 12-20.


[33] Zhao C, Tanaka C, Nakao T, Takahashi A. Adaptive-Control Optimization. In: Band Sawing. 1. Monitoring Methods of Band-Saw Deviation in Sawing. Mokuzai Gakkaishi. 1991; 37(10): 897-903


[34] Marchal R, Mothe F, Denaud L. Cutting forces in wood machining - Basics and applications in industrial processes. A review. Wood machining - micromechanics and fracture. 2009; 63 (2):157-167


[35] Mandic M, Svrzic S, Danon G. The Comparative Analysis of two Methods for the Power Consumption Measurement in Circular Saw Cutting of Laminated Particle Board. Wood Research. 2015; 60 (1): 125-136


[36] Iskra P, Hernández R. Towards a process monitoring of CNC wood router. Sensor selection and surface roughness prediction. Wood Sciences and Technology 2012; 46:115-112


[37] Aguilera A, Méausoone P.J, Rolleri A, Barros J.L, Burgos F, Aguilar C. Advances on indirect methods to evaluate tool wear for Radiata pine solid wood molding. Wear. 2016; 350-351: 27-34


[38] Baradit E, Aedo R, Correa J. Knot detection in Wood using microwaves, Wood Science and Technology. 2006; 40: 118-123


13


[39] Thomas L, Mili L. Defect Detection on Hardwood Logs Using Laser Scanning. Wood and Fiber Science. 2006; 38: 243-246


[40] Aguilera C, Ramos M, Sappa A. Simulated Annealing: A Novel Application of Image Processing in the Wood Area. In: Guerra M. Editor. Simulated Annealing - Advances, Applications and Hybridizations. London, UK: Intechopen; 2012. DOI: 10.5772/50635


[41] Oja J, Wallbäcks L, Grundberg S, Hägerdal E, Grönlund A. Automatic grading of Scots pine (Pinus sylvestris L.) sawlogs using an industrial X-ray log scanner. Computers and Electronics in Agriculture. 2003; Volume 41, Issues 1-3: 63-75


[42] Salinas D. Búsqueda del cilindro nudoso en trozas de pinus Radiata d. Don utilizando imágenes de CT y patrones de nudos [tesis]. Concepción, Chile: Universidad del Bío-Bío; 2004


[43] Rojas G, Condal A, Beauregard R, Verret D, Hernández R. Identification of internal defect of sugar maple logs from CT images using supervised classification methods. Holz als Rohund Werkstoff. 2006; 64: 295-303. DOI:10.1007/s00107-006-0105-0.


[44] Schwab K. La cuarta revolución industrial. Foro Económico Mundial. Barcelona, España: Editorial Debate; 2016. 216 p.


[45] Rich, E. A. Artificial Intelligence. New York: McGraw-Hill; 1983. 806 p.


[46] Langton C. Artificial Life p. 37. In: Wilson R, Keil F, editors. The MIT Encyclopedia of the Cognitive Sciences. MA, USA: The MIT Press; 1999


[47] Mitchell T. Machine Learning. USA: McGraw Hill; 1997. 440 p.


[48] Sharp M, Ak R, Hedberg T. A survey of the advancing use and development


<!-- Page 15 -->


Engineered Wood Products for Construction


of machine learning in smart manufacturing. Journal of Manufacturing Systems. 2018; 48: 170-179


[49] Qingchen Z, Yang L, Chen Z, Li P. A survey on deep learning for big data. Information Fusion. 2018; 42: 146-157


[50] G.E. Hinton, R.R. Salakhutdinov. Reducing the dimensionality of data with neural networks, Science. 2006; 313 (5786): 504-507


[51] LeCun Y, Bengio Y, Hinton G. Deep Learning. Nature. 2015; 521(7553): 436-444


[52] Berzal, Fernando. Redes Neuronales & Deep Learning. Publicado independiente (Edición en español). 2018. 753 p.


[53] Diez-Olivan A, Del Ser J, Galar D, Sierra B. Data fusion and machine learning for industrial prognosis: Trends and perspectives towards Industry 4.0. Information Fusion. 2019; 50: 92-111


[54] Pham D. T, Muhamad Z, Mahmuddin M, Ghanbarzadeh A, Koc E, Otri S. Using the bees algorithm to optimize a support vector machine for wood defect classification. In: Innovative Production Machines and Systems Virtual Conference [Internet]. 2007. Available from: http://repo.uum. edu.my/154/


[55] Koskinen J, Vaarala T, Alatalo J, Heikkilä T. Automated Quality Classification of Wooden Parts for Flexible Manufacturing. Journal of Engineering Technology (JET). 2013; Vol. 2, N° 1: 239-243


[56] Reyes D. Análisis de datos a través de Machine Learning para predecir el comportamiento de máquinas de aserrío de alta productividad [tesis]. Concepción, Chile: Universidad del Bío-Bío. 2020


14


[57] Navarrete C. Evaluación de método predictivo para variables de secado de chapas en planta de paneles Arauco Nueva Aldea [tesis]. Concepción, Chile: Universidad del Bío-Bío. 2020


[58] Aguilera C, Ramos M. Project: multispectral sensors to detect defects and to control quality in the panels industry. FONDEF-IDEA Stage 2, Internal Report. ANID Chile, University of Bio-Bio: 2020


[59] Aguilera C. A, Aguilera C, Sappa, A. D. Melamine Faced Panels Defect Classification beyond the Visible Spectrum. Sensors. 2018; 18, 3644. DOI:10.3390/s18113644
