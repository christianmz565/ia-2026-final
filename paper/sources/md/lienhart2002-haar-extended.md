# lienhart2002-haar-extended


<!-- Page 1 -->


An Extended Set of Haar-like Features for Rapid Object Detection


Rainer Lienhart and Jochen Maydt Intel Labs, Intel Corporation, Santa Clara, CA 95052, USA


Rainer. Lienhart@intel.com


## ABSTRACT


Recently Viola et al. [5] have introduced a rapid object detection. scheme based on a boosted cascade of simple feature classifiers. In this paper we introduce a novel set of rotated haar-like features. These novel features significantly enrich the simple features of (51 and can also be calculated efficiently. With these new rotated features our sample face detector shows off on average a 10% lower false alarm rate at a given hit rate. We also present a novel post optimization procedure for a given boosted cascade improving on average the false alarm rate further by 12.5%.


## 1 Introduction


Recently Viola et al. have proposed a multi-stage classification procedure that reduces the processing time substantially while achieving almost the same accuracy as compared to a much slower and more complex single stage classifier (51. This paper extends their rapid object detection framework in two important ways: Firstly, their basic and over-complete set of haar-like feature is extended by an efficient set of 45" rotated features, which add additional domain-knowledge to the leaming framework and which is otherwise hard to learn. These novel features can be computed rapidly at all scales in constant time. Secondly, we derive a new postoptimization procedure for a given boosted classifier that improves its performance significantly. 2 Features


The main purpose of using features instead of raw pixel values as the input to a leaming algorithm is to reducehncrease the in-clasdout


of-class variability compared 10 the raw input data, and thus making classification easier. Features usually encode knowledge about the domain. which is difncult to learn from a raw finite set of input data.


The complexity of feature evaluation is also a very important aspect since almost all object detection algorithms slide a fixed-size window at all scales over the input image. As we will see. our features can be computed at any position and any scale in the same constant time. Only 8 table lookups are needed. 2.1 Feature Pool


Our feature pool was inspired by the over-complete haar-like features used by Papageorgiou el al. in 14.31 and their very fast computation scheme proposed by Viola el al. in (51, and is a generalization of their work. Let us assume that the basic unit for testing for presence of an object is a window of M*H pixels. Also assume that we have a very fast way of computing the sum of pixels of any upright and 45" rotated rectangle inside the window. A rectangle is specified by the tuple


r=(x,y,w,h,a) with 05x,x+tdW. O5y,y+KH. x,y>O. w,h>O, and (IE {0",45') and its pixel sum Is denoted by RecSum(r), Two examples of such rectangles are given in Figure 1.


Our raw feature set is then the set of all possible features of the form


f e a t m i o,.RecSUm(r,),


## IE 141. ...,NI


where the weights op CR , the rectangles r,, and N are arbitrarily


Window


upright rectangle


## 9.1. Exampledanu~nand45'r~~reaangle.


chosen. This raw feature set is (almost) infinitely large. For practical reasons, it is reduced as follows:


1. Only weighted combinations of pixel sums of two rectangles are considered (i.e.. N= 2 ). 2. The weights have opposite signs, and are used to compensate for the difference in area size between the two rectangles. Thus, for non-overlapping rectangles we have -wo.Area(ro)= wi.Area(rl) . Without restrictions we can set wo=-l and get wi=Area(roYArea(r,). 3. The features mimic haar-like features and early features of the human visual pathway such as center-surround and directional responses. These cestrictions lead us to the 14 feature prototypes shown in Figure 2:


Four edge features.


Eight line features. and * Two center-surround features.


These prototypes are scaled independently in vertical and horizontal direction in order to generate a rich, over complete set of features. Note that the line features can be calculated by two rectangles only. Hereto it is assumed that the first rectangle ro encompasses the black and white rectangle and the second rectangle rl represents the black area. For instance, line feature (Za) with total height of 2 and width of 6 at the top left corner (5.3) can be written as


fea1ure~-1.RecSum(5,3,6,2,0")+3~RecSum(7,3,2,2,0')


Only features (la), (Ib). (2a). (23 and (43 of Figure 2 have been used by (3.4.51. In our experiments the additional features significantly enhanced the expressional power of the learning system and consequently improved the performance of the object detection system. Feature (4a) was not used since it is well approximated by feature (29) and @e). NUMBER OF FEATURES. The number of features derived from each prototype is quite large and differs from prototype to prototype and can be calculated as follows. Let X=iWwj and Y=LWhl be the maximum scaling factors in wand ydirection. A upright feature of size wxh then generates


0-7803-7622-6/02/$17.00 a2002 IEEE I - 900 IEEE ICIP 2002


<!-- Page 2 -->


## 3. Center-surround features


4. Not used, but used in [3.4,51 sc Fgr2. Feat& px" dsimple haar-like and center-wnamd fean~m. Black areas have regab% and white areas pmhe wi$ts


features for an image of size MH, while a 45" rotated feature generates


Table 1 Usts the number of features for a window size of 24x24


window foi each prolotype,


## 2.2 Fast Feature Computation


All wr features can be computed very fast in constant time for any size by means of two auxiliary images. For upright rectangles the auxiliary image is the SwnmedA~a Table SAT(x,y). SAT(x,y) is denned as the sum of the pixels of the upright rectangle ranging from the top left comer at (0.0) to the bottom right comer at (x.9


(see Figure 3a) [SI:


(a) Ib)


Fig 3,(a)Upngrl~AreaTa~(24l)and(b)RcC?rcd


SwnmedArea Tah'e(RSA7) calculaDonsdlemed uw pxel a m d upqM (c) am rotated (d) recraqlcs


From this the pixel suiit ufany upright rectangle i= (x,y, u.h.0) can be deierrnined by four trble luokups (SUI. alsu Figure 314:


RrcSum(r) = SARx- 1.y- I j+SAT(x- U 1.y. h- I )


SAqx- 1 .y+ h- I 1 -.SA q x + IC- I .y- I I


This insight wa) firri published in 151


For 15" rutdled reciangler the auxiliary inldge is drfined as the Roraid Summed Arra bble RSA7(x.y). It givcs ilic sum of thr pixels uf the reciangle roiated by 45' wiih ihc right mmi cornrr at


(xV, and extending iill the boundaries of the image (see Figure 3h).


RS.AI(x,))= I ~ X J J


x~x.x6"-,-,,


11 ran be calculated wiih 1\11) pdsses wcr all pixcls The fir51 p a s from left tu righi and top tu bottom dcierniincs


RSA Q x , ~ ) = RSAnx- 1.y- I )-RSA7(x- I .y)-/(x,yj-RSA~x. 2.y- I )


\\ith


RSA I ( - I ,y) = RSA ?( 2,y) = R.$A q x , - 1 1 = 0 ,


whereas ihe wrund pass fruni the righi to left and boiturn tu top calculaier


RSA7tx.yJ = RSA7(x,yJ- RS.4 n x - 1.p I ,-RSrll(x-Z,y,


From 11115 Ihe pixel sum of an) roiaied rrciangle r=(x,y, w,h,45"~ can be deiprmined by four iablc lookups (see alsa F~gure 3(dJ and Figure 1):


RecSum(r)= RSAqx+ ":p it')* RSARx-h,y+ h j -RSA T(.r,y)-KSAT(x+ w- h,y- U I hj


S A T v l = Z Wd1. 2.3 Fast Lighting Correction


x'sr,y'sy The special propenies of the haar-like features also enable fast contrast stretching of the form It can be calculated with one pass over all pixels from left to right and top to bottom by means of


SAqx,y)=SA~x,y-l)+Saqx-l,y)+lcx,y)-SAqx-l,y-l) , E R + .


## I - 901


p can easily be determined by means of SAT(x.y). Computing o , however. involves the sum of squared pixels. It can easily be derived by lculating a second set of SAT and RSAT auxiliary images for X x , y ) . Then, calculating o for any window requires


<!-- Page 3 -->


Fig. 4. Calurlaticm whemefardated areas.


only 4 additional table lookups. In our experiments cwas set to 2. 3 Cascade of Classifiers


A cascade of classifiers is a degenerated decision tree where at each stage a classifier is trained to detect almost all objects of interest


(frontal faces in our example) while rejecting a certain fraction of the non-object patterns [5] (see Figure 5). For instance. in our case each stage was trained to eliminated 50% of the non-face patterns while falsely eliminating only 0.2% of the frontal face patterns; 13 stages were trained Assuming that our test set is representative for


earning task, we can expect a !$se alarm rate about %11-1.2e-04 and a hit rate about 0.998 =0.97.


N slagel 2 3 N


hilrale= h


?sealarms= P


input pattern classified as a non-object


Fig. 5.carade ddasksnilh Nstages. AteachstageadaMw


isbainedtoachi a hnratecfhand a false alarm iate of f.


Each stage was trained using the Discrete AdaBwst algorithm [I]. Discrete Adaboost is a powerful machine learning algorithm. It can leam a stmng classifier based on a (large) set of weak classifiers by re-weightlng the training samples. Weak classifiers are only required to be slightly better than chance. Our set of weak classifiers are all classifiers which use one feature from our feature pool in combination with a simple binary thresholding decision. At each round of boosting. the feature-based classifier is added that best classifles the weighted training samples. With increasing stage number the number ofweak classifien. which are needed to achieve the desired false alarm rate at the given hit rate. increases (for more detail see 151). 4 Stage Post-Optimization


Given a discrete AdaBoost stage classifier


M. c(x)=sIg C a;f,(.#t,,,)+b wlth 6=0 L


I


we can easily constmct a non-optimal ROC (Receiver Operating Characteristic) by smoothly varying offset b (see Figure 6). While this stage classifiers is designed to yield a low error rate (misses + false alarms) on the tralning data. it in general performs unfavorable for b t 0 , specially in our case where we want to achieve a miss rate close to zem.


However. any given stage classifier can be post-optimized for a given hit rate. The free parameters are the lI 's, while the ul's must be chosen according to the AdaBoost loss function to preserve the properties of Adahost. We use the iterative procedure shown in Figure 7 for optimization. where step 4.2.1. is implemented in a gradient decent-like manner: Starting with the original I, value, tl is first slowly increased then decreased as long as the performance does not degrade. A true adient decent cannot be implemented since c(x) is not continuos F .


0.014


0.012


r


(Y 0.m ?i 'I 0.m


n


~ +.. ~w ....................................... ............ -., _ _ ... I I , ...~,.?...J 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 fa& alarm .Ne


## 0.W2


n


Fig. 6. Canparkm 0fd;le RoCs d a d m Adaboostdaaa with 11 feanres atzIage O ~ a r x J ~ sagepostqxi. m i a h .


## 5 Experimental Results


## 5.1 Basic vs. Extended Haar-like Features


Two face detection systems were trained: One with the basic and one with the extended haar-like feature set. On average the false alarm rate was about 10% lower for the extended haar-like feature set at comparable hit rates. Figure 7 shows the ROC for both classifiers using 12 stages. At the same time the computational complexity was comparable. The average number of features evaluation per patch was about 31.


These results suggest that although the larger haar-like feature set usually complicates learning, it was more than paid of by the added domain knowledge, In principle. the center surround feature would have been sufficient to approximate all other features. however. it is in general hard for any machine learning algorithm to learn joint behavior in a reliable way.


## 5.2 Stage Post-Optimization


A third face detection system was trained using the extended feature set as well as our novel post-optimization procedure for each


1. Note that any change in the threshold 1" requires recomputationof U,, f o r p n .


## I - 902


<!-- Page 4 -->


Given 2.I.Positive and negative examples (4 ,fl),...,(&;$,> and


n n (x;,yy) ,..., (xNn,yN.) where # = I and y;=-l


2.2.Stage classifier c(x)=sign(F& b) 2.3.Desired target hit rate h


While (err c errold) 4.1. errOld=err I.Z.Repeatforj=l, 2. .... M


4.2.1 Find combination{$b} that minimizes the expected weighted false alarm rate at target hit rate h:


and


7.1 set according to Adaboost rule. The superscript p anr n denotes that the expectation value and error is calci lated with respect to the weighted positive and negative sarnpies only. 4.3.Determine {$bJ} combination with smallest expected weighted false alarm rate at given hit rate:


n , - jtargm/derr (I, $bJ))


4.4. r - t ? - . , b t b , U date a. and wtJ according to Adaboost J J J 1°FJ rule, e r r t e r r o,tj9)


## I - 903


completed stage classifier. On average the false alarm rate was about 12.5% lower for the post-optimized classifier at comparable hit rates. Figure 8 shows the ROC for both classifiers using 9 stages. At the same time the computational complexity was also comparable. The average number of features evaluation per patch was about 28.


o.mi o.mx om2 omii om3 O.-I o.mr o.mii amr 18alar",, Fig. 8. Stagepst-oplmizatimimproves~anzdlhebooded


detectioncascadebyahout12.5%.


Frontal faces are detected in CIF images (320x240) at 5fps on a PentiumB-4 ZGhz while searching at all scales with a rescaling factor of 1.2 using a pure C++-based implementation. An improved. optimized and multi-threaded version of the face detector is available as an integral part of OpenCV at http:llsourceforge.net/ projectdopencvlibraryl.


## 6 Conclusion


The paper introduced an novel and fast to compute set of rotated haar-like features as well as a novel post-optimization procedure for boosted classifiers. It was shown that the overall performance could be improved by about 23.8% of which 10% could be constributed to the rotated features and 12.5% to the stage post-optimization scheme.


## 7 REFERENCES [I] Y. Freund and R. E. Schapire. Experiments with a new boost


ing algorithm. In Machine Learning: Proceedings of the Thirteenth International Conference, Morgan Kauman, San Francisco, pp. 148-156, 1996. 121 Chulhee Lee and David A. Landgrebe. Fast Likelihood Classification. IEEE Transactions on Geoscience and Remote Sensing, Vol. 29, No. 4, July 1991. [3] A. Mohan. C. Papageorgiou, T. Poggio. Example-based object


detection in images by components. IEEE Transactions on Pattern Analysis and Machine Intelligence. Vol. 23. No. 4. pp. 349 -361. April 2001. 141 C. Papageorgiou. M. Oren. and T. Poggio. A general framework for Object Detection. In Infernational Confemce on


Computer !&on. 1998. 151 Paul Viola and Michael 1. Tones. Raoid Obiect Detection mine . .


a Boosted Cascade of Si&Je Featu;es. IE6E CVPR. 2001. "


161 P. Pudil. J. Novovicova. S. Blaha. and J. Kittler. Multistage pattern recognition with reject option. 11th IAPR International Conference on Pattern Recognition. V01.2. pp. 92 -95. 1992. 171 H. Rowley. S. Baluja, and T. Kanade. Neural network-based face detection. In IEEE Patt. Anal. Mach. Intell.. Vol. 20, pp. 22-38. 1998.
