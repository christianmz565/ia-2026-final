# wolszczak2024-blue-stain-detection


<!-- Page 1 -->


applied sciences


Article Training of a Neural Network System in the Task of Detecting


Blue Stains in a Sawmill Wood Inspection System


Piotr Wolszczak 1,2,* , Grzegorz Kotnarowski 3, Arkadiusz Małek 4 and Grzegorz Litak 1


1 Faculty of Mechanical Engineering, Lublin University of Technology, Nadbystrzycka 36, 20-618 Lublin, Poland; g.litak@pollub.pl 2 Institute of Technology and Computer Science, Zamo´s´c Academy, Pereca 2, 22-400 Zamo´s´c, Poland 3 Woodinspector Ltd., Rusałka 11, 20-103 Lublin, Poland; grzegorz.kotnarowski@gmail.com 4 Institute of Technical Informatics and Telecommunications, University of Economics and Innovation, Projektowa 4, 20-209 Lublin, Poland; arkadiusz.malek@wsei.lublin.pl * Correspondence: p.wolszczak@pollub.pl


Abstract: This article presents the operation of an automatic pine sawn timber inspection system, which was developed at the Woodinspector company and is offered commercially. The vision inspection system is used to detect various wood defects, including knots, blue stain, and mechanical damage caused by worms. A blue stain is a defect that is difficult to detect based on the color of the wood, because it can be easily confused with wood defects or dirt that do not impair its strength properties. In particular, the issues of detecting blue stain in wood, the use of artificial neural networks, and improving the operation of the system in production conditions are discussed in this article. While training the network, 400 boards, 4 m long, and their cross-sections of 100 × 25 [mm] were used and photographed using special scanners with laser illuminators from four sides. The test stages were carried out during an 8-hour workday at a sawmill (8224 m of material was scanned) on material with an average of 10% blue stain (every 10th board has more than 30% of its length stained blue). The final learning error was assessed based on defective boards detected by humans after the automatic selection stage. The system error for 5387 boards, 550 m long, which had blue staining that was not detected by the scanner (clean) was 0.4% (25 pieces from 5387), and 0.1 % in the case of 3412 boards, 610 mm long, on which there were no blue stains, but were wrongly classified (blue stain). For 6491 finger-joint boards (180–400 mm), 48 pieces were classified as class 1 (clean), but had a blue stain (48/6491 = 0.7%), and 28 pieces did not have a blue stain, but were classified as class 2 (28/3561 = 0.7%).


Citation: Wolszczak, P.; Kotnarowski,


G.; Małek, A.; Litak, G. Training of a


Neural Network System in the Task of


Detecting Blue Stains in a Sawmill


Keywords: machine vision; vision system; wood inspection; neural networks


Wood Inspection System. Appl. Sci.


2024, 14, 3885. https://doi.org/


10.3390/app14093885


Academic Editor: Giuseppe Lazzara


## 1. Introduction


Received: 30 January 2024


Wood is an attractive and frequently used construction raw material, despite the appearance of new synthetic building materials on the market. In developed economies, the costs associated with logging and processing continue to increase along with the costs of labor and raw materials. It is important to develop techniques that minimize production costs, including waste raw materials or semi-finished products. Therefore, wood sorting improves the efficiency of raw material use.


Revised: 22 April 2024


Accepted: 25 April 2024


Published: 1 May 2024


Currently, the process of detecting wood defects, i.e., knots, cracks, resins, rings, and edges in most small- and medium-sized sawmill plants, involves marking the wood in appropriate places by people specially employed for this process. Usually, at least four people take part in this process: two for feeding the wood onto a conveyor and marking (hatching) the boards, and two for receiving and stacking the boards. Cutting out defects involves an employee marking the cutting location with a line on the wood. Then, an “optimizer” machine cuts the board at the marked location and throws the cut elements


Copyright: © 2024 by the authors.


Licensee MDPI, Basel, Switzerland.


This article is an open access article


distributed under the terms and


conditions of the Creative Commons


Attribution (CC BY) license (https://


creativecommons.org/licenses/by/


onto a sorting table, where they are picked up by an employee. Removing the defect


4.0/).


Appl. Sci. 2024, 14, 3885. https://doi.org/10.3390/app14093885 https://www.mdpi.com/journal/applsci


<!-- Page 2 -->


Appl. Sci. 2024, 14, 3885 2 of 15


involves cutting it out and dividing the board into smaller parts. Accuracy in cutting out a defect involves cutting it out as sparingly as possible (as close to the defect as possible) in order to obtain the most material in a better class. The cut off part is treated as waste. This operation depends on the assessment of the material from four sides and the precision of the meaning of the defects by the employee. As a result of a visual inspection of the quality of the marking of defects by an operator, it is estimated that each defect that the employee marks is, on average, about 50 mm. During 8 h of work, the employee marks approximately 5760 defects (four boards with five defects per minute). During the year, the loss may amount to 92,160 m. Assuming that the cost is 1 EUR/m, the sawmill owner loses up to 92,160 EUR in revenue per year due to the work of the incorrectly hatching operator. This example illustrates the problem of large material losses for sawmill plants resulting from the removal of defects in wood. Moreover, an employee marking several boards per minute constantly has to subjectively assess whether a given section should be cut or left whole. At the same time, a solid and reliable calculation (appropriate estimation) for each board is not possible due to the need to maintain production efficiency. During such an assessment of sawn timber, it is necessary to analyze not only the defects in the wood, but also where they occur. Wood defects may only appear on one side and may be of a certain size. The scope of the board’s qualifications is determined by the product specification. On the one hand, frequent human errors mean that pieces with defects enter the final product and eliminate the entire element as the final product, resulting in a loss of material and work. On the other hand, elements that qualify for class 1 are often included in class 2. This reduces the effectiveness of obtaining the best quality material and reduces the profit. Work efficiency in this process is approximately 12 m/min per employee. The second important problem is finding people to accurately mark the wood, who will be able to mark the wood in continuous motion for 8 h a day. It is hard and tedious work. Due to the lack of suitably qualified people on the market, production efficiency decreases. The article discusses the implementation in the pine wood processing process. The basic approaches include the detection of defects in wood using vision techniques, automatic determination of the type and size of the defect, and automatic planning of sawn timber cutting and sorting according to scanning results. The lumber boards are then stacked in layers. This approach consists of the following:


• An input material scanning system (scanner), which is responsible for recognizing and classifying the type of defects using vision techniques; • Cutting optimization algorithms depending on the type of defect in order to eliminate selected process stages; • A module for parameterizing the scanner’s operation conducted by the operator; • A sorting module and the semi-automatic stacking of the output material; • An integral cutting module with a sorting system; • A module for the semi-automatic unstacking of the material for feeding to the cutting line.


An important element of the system is the scanning module, which includes a defect detection algorithm based on artificial neural networks. Blue stains are a tree disease that causes the wood to change color to blue or black. It is a defect that is difficult to detect based on the color of the wood, because it can be easily confused with wood defects or dirt.


Traditional methods of detecting blue stains in sawmill wood are time consuming and expensive. The use of neural networks allows for a faster and more effective detection of blue stains in sawmill wood, which can help increase sawmill production efficiency. Neural networks are a type of machine learning algorithm that imitate how the brain works. Neural networks are used due to their effectiveness in solving problems related to the processing of images, sounds, text, and other data. Due to their ability to generalize knowledge, neural networks are particularly useful for detecting objects in images. One of the applications of neural networks is the detection of blue stains in sawmill wood.


There are studies in the literature on the use of vision techniques for wood quality inspection [1–3].


<!-- Page 3 -->


Appl. Sci. 2024, 14, 3885 3 of 15


In 2005, Van den Bulcke et al. (2005) proposed a technique for assessing blue stains using image analysis [4]. The method of the quantitative assessment of the presence of a blue stain according to the standard [5] was found to be insufficient. A scale from 0 to 5 was used for visual assessment, where 0 means no blue stain and 5 means a complete coverage of the cross-section with blue-staining fungi to a depth of 5 mm. Neural networks were used as generalizing classifiers to measure surface blue stains, as well as to analyze the distribution of fungal invasion inside the wood. However, even with additional data reduction and clustering techniques, it has been difficult to obtain results comparable to subjective visual assessment. Nevertheless, it has been proven that image processing and 3D reconstruction seem to be valuable tools for assessing blue stains [6–8]. In another article [9], a modified wood testing methodology standardized according to the EN 152 standard was presented, intended to test the effectiveness of wood coatings. A method called the EN 152 reverse method was used for the computer-aided grading of coated wood to assess the discoloration of the coatings and analyze the blue-stained wood inside the samples. Three-dimensional (3D) reconstructions of the samples were obtained, which became a tool for an in-depth analysis of the presence of blue stains [10–12]. Similar results were obtained in studies published in [4,13]. The usefulness of vision methods was confirmed, and the development of modern computer-controlled planners with a scanning head that accelerate the process by controlling for the presence of blue stains was predicted [14,15].


In 2005, a color image segmentation method using neural networks was also proposed for detecting wood surface defects [16]. The proposed method is called FMMIS (Fuzzy Min-Max Neural Network for Image Segmentation). Automatic visual inspection (AVI) systems includes five processing steps: image acquisition, image enhancement, image segmentation, feature extraction, and classification. The recognized defects cover 10 defect categories: bird’s eye and freckle, pockets of bark and tar, fade, split, stain, blue stain, pith, dead knot, living knot, and hole. The FMMIS algorithm was compared with the Seed Region Growing (SRG) algorithm of Adams and Bischof, and it was proven that the former is very fast and more effective in detecting defects in the “bird’s eye” and “freckle” categories, as well as “spot”, “blueing”, and “split” (the number of true positives, i.e., correctly detected: TP < 50%) [1,17–22].


The contribution of this team of authors is a compact approach for the optimization (cross cutting) of sawn timber. This approach consists of the following:


1. An input material scanning system (scanner, resolution 76.2 dpi, 3 pixels/mm), which is responsible for recognizing and classifying the type of defects using vision techniques; 2. Cutting optimization algorithms depending on the type of defect in order to eliminate selected process stages; 3. A module for parameterizing the scanner operation conducted by the operator; 4. A sorting module and the semi-automatic stacking of the output material; 5. An integral cutting module with a sorting system; 6. A module for the semi-automatic unstacking of material for feeding to the cutting line.


Thanks to the use of such component lines, it is possible to detect defects in wood with a diameter accuracy of up to 10 mm, the automatic determination of the type and size of the defect (e.g., healthy knot 25 mm), the automatic planning of sawn timber cutting, sorting according to scanning results, stacking elements into layers to eliminate the cumbersome and non-ergonomic process of manually taking elements from the table and spreading them on pallets, and facilitating the unstacking of the material, which will eliminate the cumbersome operation of taking sawn timber from the stack and feeding it to the conveyor. So far, human-operated optimizers have been responsible for identifying and classifying the type of defect in sawmills with lower efficiency. Their task is to cut out defective parts, e.g., knots. As a result, friezes and semi-finished products for further processing are created. Accuracy in cutting out defects involves cutting out the defect as sparingly as possible to obtain as much material as possible in a better class. This activity depends on the operator’s precision and their assessment of the material from four sides. As a result of an inspection of the quality of the marking defects by the operator (waste bins


<!-- Page 4 -->


Appl. Sci. 2024, 14, 3885 4 of 15


were inspected in several sawmills in Poland—the result was the importance of defects according to employees), it was estimated that employees add approximately 50 mm to each defect. An employee marking several boards per minute constantly has to subjectively assess whether a given section should be cut or left whole. A solid and reliable calculation for each board throughout the entire operator’s work is not possible due to the need to maintain production efficiency. During such an assessment of sawn timber, it is necessary to analyze not only the defects in the wood, but also their location (the customer may indicate in the specification that there is a possibility of knots, but only on one side and of a specific size). Thanks to the use of a material scanning system with cutting optimization algorithms using vision techniques in the lumber optimization line, it is possible to reduce the amount of waste and increase the amount of high-quality output material, eliminate the unnecessary cutting out of defects, correctly sort elements, optimize the cutting of resin around the knot, and increase the efficiency of the optimization process per number of people, improving the ergonomics of their work. Thanks to the use of simple hardware solutions (with a low cost of the machine) and high efficiency of defect detection using complex and specialized algorithms, the proposed solution is able to achieve a high degree of automation for many processes with low device efficiency.


## 2. Materials and Methods


The vision system consists of four sets of laser line projectors and cameras exposing and recording four sides of a wooden board (lumber or laminated board). The optical sets were placed in a gate, into which the boards were automatically inserted. The system is shown in Figure 1. Figure 2 shows a view of the scanner gate (working space) and the guide rollers and belt feeders. The boards were fed automatically.


Figure 1. A Q-scan 60 system, which implements a blue stain detection algorithm using neural networks.


Figure 2. The working area of the vision system equipped with four sets of cameras and an illuminator, recording four sides of the board.


<!-- Page 5 -->


Appl. Sci. 2024, 14, 3885 5 of 15


## 2.1. Methodology for Building and Improving Defect Detection Systems


Training the system involved collecting images of boards and classifying them. The manual classification of boards was carried out. Engineers’ experience shows that this task cannot be accomplished using other methods


The procedure used involves the preparation of 400 boards (whole boards), of which 200 had a blue stain defect and 200 had a defect that can be confused with a blue stain. The boards were 4 m long, and their cross-sections were 100 × 25 mm. Each of these boards had a “blue stain defect” or “other defect” on 50% of the surface. The set was prepared for blue stain detection based on the color components of the board surface. According to this concept, all other objects that visually look similar to a blue stain for the color-based algorithm would constitute a potential “non-blue stain”.


The procedures include three stages. Keras, an API for the TensorFlow platform, was used for the machine learning task.


2.1.1. Stage 1—Creating a Set of Images for Training and Developing an Initial Neural Network Model


Using the first set of 100 (25% of the total) boards (50 pcs of which were defective, and 50 pcs of which were not faulty), the color component thresholds were corrected so that every blue stain was found. The color range covered 100% of the defect areas on the surface of the boards. This area was allowed to be slightly wider than the actual defect areas, but could not be narrower. Approximately 20,000 (+/−1000) samples were collected from the area marked in “color”. Creating a set involved cutting out square images representing the defect, spaced every 3 to 10 mm (distance between subsequent squares).


Then, the first training of the neural network was performed. We present the following sample results obtained during one of the implementations at a sawmill:


• Accuracy: 95%. • Loss: 15%. • Epoch: 10.


Then, the images in the set were mixed and divided again into subsets: training and validation. The proportions of the sizes of the training and validation set were 3/4 and 1/4. This means that 3/4 of the set, after mixing the photos, was included in the training set. The remaining images were for validation. The same division applied to images representing ’no fault’. The collection size was 40,000.


The next step was to verify the effectiveness of the obtained network model when scanning on subsequent boards as follows:


1. The model correctly classifies defects and non-defects in approximately 50% of the cases. 2. The model programmed in the Keras environment returns values from 0 (for defect) to 1 (for non-defect).


Below is a fragment of the code that built the model in the Keras environment (Listing 1). The input layer of the neural network model accepts images with dimensions of 32 × 32. The activation functions of hidden layers are linear in a range > 0 of the input value (name: ‘ReLU’, max (0, x)):


(


0 x < 0


y(x) = max(0, x) =


(1)


x x ≥0


The last layer has two output neurons, and their activation functions have a sigmoid form:


y(x) = σ(x) = 1 (1 + e−x). (2)


<!-- Page 6 -->


Appl. Sci. 2024, 14, 3885 6 of 15


Listing 1. Python code for model building in Keras environment.


sz = 32 model = Sequential() model.add(Conv2D(32, (2, 2), input\_shape=(sz, sz,3))) model.add(Activation(’relu’)) model.add(MaxPooling2D(pool\_size=(2,2)))


model.add(Conv2D(32, (2, 2))) model.add(Activation(\’relu\’)) model.add(MaxPooling2D(pool\_size=(2,2)))


model.add(Conv2D(64, (2, 2))) model.add(Activation(’relu’)) model.add(MaxPooling2D(pool\_size=(2,2)))


model.add(Flatten()) model.add(Dense(64)) model.add(Activation(’relu’)) model.add(Dropout (0.5)) model.add(Dense(outputs)) # OUTPUTS model.add(Activation(‘sigmoid’))


The difference expresses the difference between correct and incorrect classification:


NNDi f f = (%o f de f ective −%notde f ective)100%. (3)


A difference result with a plus means a defect, and a minus means non-defect. Areas on the board spaced 50 mm apart were scanned, and the following results were obtained with certain conditions:


• 56% of places that are blue stain have an NNDiff value > 50%; • 23% of places that are not blue stain have an NNDiff value > 50%; • 52% of places that are BLUE have NNDiff < −50%; • 18% of places that are blue stain have an NNDiff value < −50%.


## 2.1.2. Stage 2—Testing the Model’S Effectiveness and Improvement


Another series of 100 boards (25%) was prepared (50 pcs, defective and 50 pcs, not defective). This stage verified whether detection based on color components covers all areas covered by a blue stain, i.e., whether no blue stain was missed. If it turns out that one board has a blue stain that has not been marked (1% of the sample), then the color component thresholds are corrected.


After creating and adding an additional set of square image samples, the network returned the following results:


• NNDiff > 50% and the area was not a blue stain; • NNDiff < −50% and the area was a blue stain; • NNDiff > −10% and NNDiff < 10% are areas that are defective.


The network does not classify these areas as either a defect or non-defective. This step was repeated. Another series of 100 boards was scanned, and images that met the above criteria were collected.


At the end of the collection, the number of images of faults were 15,000, and 11,000 photos were of non-faults. Since the counts should be equal, the images of faults were mixed, and 4000 fault samples were randomly removed to make 11,000 each.


These images were added to the collection. The collection then had 62,000 images. This set was mixed and divided into training and validation subsets.


<!-- Page 7 -->


Appl. Sci. 2024, 14, 3885 7 of 15


Network training was performed, and the following statistics were obtained:


1. The results for the first round of training were as follows: Accuracy: 85%; Loss: 21%; Epoch: 10. 2. The results for the second round of training were as follows: Accuracy: 91% Loss: 12% Epoch: 20.


The network returned the following results:


• 95% of places that are blue stain have an NNDiff value > 50%; • 3% of places that are non-blue stain have an NNDiff value > 50%; • 91% of places that are non-blue stain have an NNDiff value < −50%; • 4% of places that are blue stain have NNDiff value < −50%.


## 2.1.3. Stage 3


During the image processing in the previous stage, representations of places were collected, and the following were observed:


• NNDiff > 50% and the area was not a blue stain; • NNDiff < −50% and the area was a blue stain; • NNDiff > −10% and NNDiff < 10% and the area was a defect.


The places in the third category were areas that the network could not classify into one or another group at all.According to the percentages of testing results (95%, 3%, 91%, 4%), there were fewer and fewer such (unspecified) places. The network worked better; until about 8000 samples were collected from each side of the board, they were scanned, and they constituted 50% of the input set.


At this stage, the final training of the neural network was performed. The sample size was 78,000 (62,000 + 16,000). Examples of learning outcomes are as follows:


1. Accuracy: 92%; Loss: 13%; Epoch: 10. 2. Accuracy: 95%; Loss: 8%; Epoch: 15. 3. Accuracy: 84%; Loss: 34%; Epoch: 20.


A model trained for 15 epochs was selected for further work. At this stage, work with the prepared set was completed. The network model and parameters were sent to production (to the production process), where testing took place under the following production conditions:


1. A total of 8 h of scanner (model) operation; 2. Material with an average of 10% blue stain (every 10th board had more than 30% of its length covered with blue stain); 3. A total of 8224 m of material was scanned.


The total production of boards was as follows:


a 5387 boards, 550 mm long; b 3412 boards, 610 mm long; c 6491 finger-joint boards (180–400 mm)—class 1; d 3561 finger-joint boards (180–400 mm)—class 2 (blue stain contained).


In these groups, the following were collected:


<!-- Page 8 -->


Appl. Sci. 2024, 14, 3885 8 of 15


a 25 boards, 550 m long, which had a blue stain but were not detected by the scanner (clean); b 13 boards, 610 mm long, on which there was no blue stain, but were wrongly classified (blue stain); c 48 pieces of finger-jointed strips (180–400 mm) with a blue stain, but were classified as class 1 (clean); d 28 pieces of finger-jointed strips (180–400 mm) that did not have a blue stain, but were classified as class 2 (blue).


The system errors for these groups were as follows:


a 25/5387 = 0.4%, b 13/3412 = 0.1%, c 48/6491 = 0.7%, d 28/3561 = 0.7%.


## 2.2. Operation of the Inspection System


The inspection algorithm includes the following image processing steps. The first stage is carried out on color images in an HSV space (the model for describing the color space containing Hue, Saturation, and Value components). Based on the pixel values, areas that may contain blue stain are pre-selected. The second stage is the filtration of the highlighted areas based on their geometric properties such as length, width, their proportions, and surface area. The third stage is preparing the set for the neural network. The input images are in the shape of a square with dimensions of 32 × 32 pixels. The images partially overlap, i.e., their margins contain common parts of the source image. The fourth stage is classification using a neural network. The system operates a set of neural networks dedicated to detecting individual wood defects. This article discusses a neural network designed to detect blue stains; other defects are not cross-detected. The algorithm’s operation diagram is shown in Figure 3.


Figure 3. Algorithm for detecting blue stain in sawmill wood.


The fifth, equally important stage is training the neural network while the system is operating under production conditions. Training the system involves completing the training set. New images are collected as it works. When replenishing the training set, its original size is preserved. For this purpose, images are randomly removed from the existing set. Then, the learning and testing procedures are started. Replacing data in the training set is limited. The network is not learned from scratch, but only trained. The weights are not randomized, but retained because they contain the current learning outcomes. The purpose


<!-- Page 9 -->


Appl. Sci. 2024, 14, 3885 9 of 15


of this practice is to accelerate the learning process. When implemented, the system is adapted to the individual requirements of the customer, which include the type of wood, surface, roughness, smoothness, and any defects in their quality classification. The neural network connection procedure used in the system speeds up the process of training the network and enriching its knowledge with new cases.


If an employee notices boards that have not been classified correctly, the boards are removed from the production line. Then, the operator passes them through the scanner again, this time, marking the areas covered by the blue stain on the computer. These data go to the training set, and the training of the network does not take place automatically, but on demand.


The stages of network improvement are discussed below with examples. 2.3. Teaching Networks to Solve Practical Problems


The creation of initial defect detection algorithms occurs after collecting wood samples and subjecting them to laboratory tests; programmers have developed a number of classic vision algorithms. Each solution was developed thanks to exposures obtained through the appropriate arrangement of the scanning head elements. Programmers first developed algorithms for detecting five defects that are crucial for glulam (glued laminated timber) producers. Later, the system was developed to include cases of rough wood and other wood species. The exposure of defects in wood with a rough surface was more difficult than in the case of smooth wood (after planing).


HSV values of areas showing a blue stain on the wood were recorded in the collected images of wood samples. This was not sufficient, so a classification of blue stains according to lightness was prepared. The classes prepared included the following: light, medium, dark, and very dark. The minimum and maximum values of the H, S, and V parameters were determined separately for these classes. The next step was to optimize these ranges. Distinguished HSV ranges allow for the preliminary detection of areas where blue stains may be present.


## 3. Results 3.1. Example 1—Dirt and Knot


Below is an example of using the HSV space classifier to highlight contours when analyzing an area showing dirt (Figure 4). Additionally, a knot is visible in the image. These two areas should not be classified as blue stains.


Figure 4. An image of a board that is dirty and has a knot, as well as a rough surface.


The dirt and blue stain have the same color. When extracting the stain with the HSV space classifier, suspicious areas are highlighted with a black outline.


Table 1 shows example values of the Hue, Saturation, and Value color component thresholds obtained after analyzing 16 samples with blue stains in various shades of colors. The records were sorted by shades of bluish color assessed visually and described with labels: light, medium, dark, and very dark. The highlighted areas are shown in Figure 5.


<!-- Page 10 -->


Appl. Sci. 2024, 14, 3885 10 of 15


Table 1. Hue, Saturation, and Value color component threshold values obtained after analyzing 16 samples.


Case No. Color of the Fault Min H Max H Min S Max S Min V Max V


1 light 18 21 131 137 121 131 2 light 18 21 137 144 139 148 5 light 18 21 132 140 134 142 7 light 19 22 140 146 136 142 9 light 21 23 144 148 138 148 10 light 21 23 147 152 141 145 11 light 22 23 143 150 137 146 13 light 18 19 152 156 151 158 4 medium 19 21 130 138 107 123 5 medium 18 21 131 137 121 143 6 medium 20 22 141 146 108 126 12 medium 20 21 131 143 117 125 16 medium 21 23 143 155 120 132 1 dark 18 20 133 144 88 109 2 dark 18 19 137 142 118 129 3 dark 19 22 140 153 113 123 4 dark 18 20 120 139 115 137 7 dark 20 21 148 160 109 120 8 dark 17 20 133 150 100 109 11 dark 21 22 151 161 121 134 14 dark 18 20 135 146 112 120 15 dark 18 20 133 138 111 121 16 dark 22 23 142 147 106 111 14 very dark 17 19 143 151 96 110 3 very dark 19 21 139 148 88 96 4 very dark 17 20 129 149 87 98 5 very dark 18 20 137 148 100 113 6 very dark 18 21 143 156 90 108 8 very dark 17 20 126 158 60 80


Figure 5. The surface of a board with areas highlighted using the HSV classifier.


The next step is to filter the highlighted areas based on their geometric properties. The result is a representation of the area suspected of containing blue stain fungi. An example of an outline is shown in the Figure 6.


Figure 6. An image of a board with highlighted areas (green outlines) suspected of containing blue stain fungi, the result after filtering the areas highlighted using the HSV classifier.


<!-- Page 11 -->


Appl. Sci. 2024, 14, 3885 11 of 15


The next stage is the division of the highlighted areas into squares that will constitute the input vector of the neural network. When designing the system, squares of different dimensions and with different densities (overlapping of adjacent squares) were tested.


In this case (See Figure 7), green squares mean that the detected object is not a blue stain.


Figure 7. An image of a board showing dirt and a knot marked with squares that was classified using a dedicated neural network. The green color of the squares means that no blue stain defect has been recognized.


In Figure 8 a green squares arranged at larger intervals during test phase are presented.


Figure 8. An image from the previous figure when testing the neural network with input images (squares) spaced at larger intervals.


The results of the classification of exemplary fragments of highlighted areas (squares) using a dedicated neural network are presented inf Figure 9. A green field indicates another defect. A red field indicates a blue-stain-type defect. Then, the difference between the determined probabilities is calculated. A minus value not exceeding a certain threshold, for example 70 percent, means no defect.


No Fault 93 % No Fault 97 %


–62%


–83%


Defect 31 %


Defect 15 %


Figure 9. Neural network results for input images showing dirt (left) and a knot (right).


## 3.2. Example 2—Blue Stain and Knots


The Figure 10 below shows an example of a wood surface with a visible defect in the form of a blue stain and a knot.


Figure 10. An image of a wood surface with a visible defect in the form of a blue stain and a knot.


<!-- Page 12 -->


Appl. Sci. 2024, 14, 3885 12 of 15


The HSV classifier initially distinguishes areas suspected of having blue stains. Highlighted areas are marked with a black outline (See Figure 11).


Figure 11. Areas highlighted using the HSV classifier.


Then, these areas are subjected to geometric filtration, and a result is shown in the Figure 12.


Figure 12. An image of a plank with the green outlines of defects marked.


The identified defects are then classified using a neural network. The result of detecting a blue type defect is marked with a red square in Figure 13. Results recognized as another defect are in green. The blue stain neural classifier does not recognize other defects. They are classified using other neural networks.


Figure 13. A result of the distribution of wood defects; the color red means the detection of blue stain and the color green means other defects (the knot in this case).


Classification results of sample input images are shown below in Figure 14.


<!-- Page 13 -->


Appl. Sci. 2024, 14, 3885 13 of 15


(a) (b)


No Fault 100 % No Fault 15 %


–100%


–81%


Defect 0 %


Defect 96 %


No Fault 4 %


96%


Defect 100 %


(c)


Figure 14. Examples of the classification of input images: (a) a knot recognized as not a defect; (b,c) cases diagnosed as blue stains.


Figure 15 shows an image of defect classification results on the operator panel. The green rectangles are the blue stains found. These are areas defined by combining small squares (input images of the neural network). Black cutting lines indicate the planned cuts of the board required to eliminate the defects. The photo shows one side of the board. However, the planned cutting lines take into account the examination carried out on all four sides of the board.


Figure 15. Preview of an image presented on the operator panel. Green squares mark the detected blue stain. The black lines mark the cutting lines of the saw. Rectangles in different colors indicate different defects.


In the case of implementing the system in a line processing a new type of wood, if samples were collected that were not correctly recognized by the system, then the system is retrained. This training involves replacing parts of the existing training set with new cases. Examples of neural network training and validation curves are shown below. Accuracy is the percentage of correct predictions made by the neural network. Loss is the sum of misclassified samples. Expressed as a logarithmic function (log loss) over a range of 0 to 1, the loss determines the probability or uncertainty of the forecast. Examples of model accuracy and model loss curves are shown in the Figure 16.


Figure 16. Plot of training and validation loss values.


<!-- Page 14 -->


Appl. Sci. 2024, 14, 3885 14 of 15


## 4. Conclusions


So far, human-operated optimizers have been responsible for identifying and classifying the type of defect in sawmills, with low efficiency. Their task is to cut out defective parts, e.g., knots. As a result, friezes and semi-finished products for further processing are created. Accuracy in cutting out defects involves cutting out the defect as sparingly as possible to obtain as much material as possible in a better class. The Q-Scan system created by Woodinspector is a pine sawn timber scanner that detects defects, classifies them, and optimizes the cutting of sawn timber in terms of the user-defined product. The scanner is based on digital image analysis technology, which allows for the detection of the most common defects in wood with high and repeatable accuracy throughout the entire working time. The scanner uses industrial cameras, LED illuminators, line lasers, and a high-performance PC computer. Optimization algorithms take into account the locations of defects and their permissible sizes depending on the product. Elements produced for micro-joining are optimized in three quality classes: class 1—no defects; class 2—resin, blue stain, and small knots; and class 3—fused knots.


The components of the developed line are as follows: an input material scanning system (scanner) for recognizing and classifying the type of defects using vision techniques, cutting optimization algorithms depending on the type of defect in order to eliminate selected process stages, a work parameterization module, and a cutting module, which is integrated with the sorting system. The main functionalities of the device are as follows: the detection of defects in wood with an average accuracy of up to 10 mm, the automatic determination of the type and size of the defect (e.g., healthy knot 25 mm), the automatic planning of sawn timber cutting, and sorting according to scanning results. The scanner’s efficiency in detecting defects is up to 60 m/min. The largest group of sawn timber producers are small- and medium-sized companies. The proposed approach is tailored to their needs.


Digital image analysis technology allows for the detection of blue stain defects in wood with high and repeatable accuracy throughout the entire working time. Optimization algorithms take into account the locations of defects and their permissible sizes depending on the product. Elements produced for micro-jointing are optimized in three quality classes: class 1—without defects; class 2—resin, blue stain, and small knots; and class 3—fused knots. Individual defects are detected using dedicated neural networks. This article presents an approach for detecting blue stains on wood. The neural network allowed us to distinguish blue stains from other defects, including wood staining, which does not impair the strength properties of the wood. The implementation of the system in the company allows for a faster and more effective detection of blue stains in sawmill wood, which can help increase the sawmill’s production efficiency.


The natural variability in wood species could not be fully captured in the training set. In the presented solution, the subject of research was pine wood from Poland. Wood samples from different manufacturers are similar to each other. In subsequent implementations, it is necessary and sufficient to additionally train the system, as described in this article.


A certain limitation of the system’s operation was the dirtying of the lenses and illuminators of the vision system, which requires the introduction of a systematic procedure for cleaning them.


The geographical context of wood and the development of a dirt detection system in the vision system may be areas for further development work.


Author Contributions: Conceptualization, P.W. and G.K.; methodology, A.M.; software, G.K.; validation, G.K. and G.L.; writing—original draft preparation, P.W. and G.K.; writing—review and editing, G.L. All authors have read and agreed to the published version of the manuscript.


Funding: This research was funded by The National Centre for Research and Development, Poland, agreement number: POIR.01.01.01-00-0923/18-01.


Institutional Review Board Statement: Not applicable.


<!-- Page 15 -->


Appl. Sci. 2024, 14, 3885 15 of 15


Informed Consent Statement: Not applicable.


Data Availability Statement: The data presented in this study are available on request from the author Grzegorz Kotnarowski.


Conflicts of Interest: Author Grzegorz Kotnarowski was employed by the company Woodinspector Ltd. The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.


## References


1. Nitka, A.; Sioma, A. Design of an automated rice grain sorting system using a vision system. In Proceedings of the Photonics Applications in Astronomy, Communications, Industry, and High-Energy Physics Experiments, Wilga, Poland, 26 May–4 June 2018. 2. Parkot, K.; Sioma, A. Development of an automated quality control system of confectionery using a vision system. In Proceedings of the Photonics Applications in Astronomy, Communications, Industry, and High-Energy Physics Experiments, Wilga, Poland, 26 May–4 June 2018. 3. Lenty, B.; Kwiek, P.; Sioma, A. Quality control automation of electric cables using machine vision. In Proceedings of the Photonics Applications in Astronomy, Communications, Industry, and High-Energy Physics Experiments, Wilga, Poland, 26 May–4 June 2018. 4. Van den Bulcke, J.; Van Acker J.; Stevens M. Image processing as a tool for assessment and analysis of blue stain discoloration of coated wood. Int. Biodeterior. Biodegrad. 2005, 56, 178–187. [CrossRef] 5. EN 152:2011; Wood preservatives—Determination of the protective effectiveness of a preservative treatment against blue stain in wood in service—Laboratory method. European Committee for Standardization: Brussels, Belgium, 2011. 6. Sioma, A. 3D imaging methods in quality inspection systems. In Proceedings of the Photonics Applications in Astronomy, Communications, Industry, and High-Energy Physics Experiments, Wilga, Poland, 27 May–2 June 2019. 7. Sioma, A. The estimation of resolution in 3D range image system. In Proceedings of the 14th International Carpathian Control Conference (ICCC), Rytro, Poland, 26–29 May 2013. 8. Sioma, A.; Karwat, B. The use of 3D imaging in surface flatness control operations. Adv. Sci. Technol. Res. J. 2023, 17, 335–344. [CrossRef] [PubMed] 9. Van den Bulcke, J.; Van Acker J.; Stevens M. Assessment of blue-stain resistance according to the EN 152 and a reverse test method using visual and computer-aided techniques. Int. Biodeterior. Biodegrad. 2006, 57, 229–238. [CrossRef] 10. Cinal, M.; Sioma, A.; Lenty, B. The quality control system of planks using machine vision. Appl. Sci. 2023, 13, 9187. [CrossRef] 11. Sioma, A.; Lenty, B. Detection of fungal infections on the wood surface using LTM imaging. Appl. Sci. 2023, 13, 490. [CrossRef] 12. Schubert, M.; Mourad, S.; Schwarze, F.W.M.R. Automated image processing for quantification of blue-stain discolouration of Norway spruce wood. Wood Sci. Technol. 2011, 45, 331–337. [CrossRef] 13. Van den Bulcke, J.; Van Acker J.; Stevens M. Laboratory testing and computer simulation of blue stain growth on and in wood coatings. Int. Biodeterior. Biodegrad. 2007, 59, 137–147. [CrossRef] 14. Burud, I.; Gobakken, L.R.; Flø, A.; Kvaal, K.; Thiis, T.K. Hyperspectral imaging of blue stain fungi on coated and uncoated wooden surfaces. Int. Biodeterior. Biodegrad. 2014, 88, 37e43. [CrossRef] 15. Hu, J.; Song, W.; Zhang, W.; Zhao, Y.; Yilmaz, A. Deep learning for use in lumber classification tasks. Wood Sci. Technol. 2019, 53, 505–517. [CrossRef] 16. Estévez, G.A.; Ruzz, P.A. Image segmentation using fuzzy min-max neural networks for wood defect detection. In Intelligent Production Machines and Systems; Elsevier Ltd.: Amsterdam, The Netherlands, 2005. 17. Pham, R.J.; Alcock, D.T. Smart Inspection Systems; Academic Press: London, UK, 2003; p. 218. 18. Ruz, G.A.; Estévez P.A.; Perez, C.A. A neurofuzzy color image segmentation method for wood surface defect detection. Forest Prod. J. 2005, 55, 52–58. 19. Estévez, P.A.; Flores, R.J.; Perez, C.A. Color image segmentation using fuzzy min-max neural networks. In Proceedings of the International Joint Conference on Neural Networks, Montreal, QC, Canada, 31 July–4 August 2005. 20. He, K.; Zhang, X.; Ren, S.; Sun, J. Deep residual learning for image recognition. In Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition, Boston, MA, USA, 7–12 June 2015; pp. 770–778. 21. He, T.; Liu, Y.; Xu, C.; Zhou, X.; Hu, Z.; Fan, J. A fully convolutional neural network for wood defect location and identification. IEEE Access 2019, 7, 123453–123462. [CrossRef] 22. He, T.; Liu, Y.; Yu, Y.; Zhao, Q.; Hu, Z. Application of deep convolutional neural network on feature extraction and detection of wood defects. Measurement 2020, 152, 107357. [CrossRef]


Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
