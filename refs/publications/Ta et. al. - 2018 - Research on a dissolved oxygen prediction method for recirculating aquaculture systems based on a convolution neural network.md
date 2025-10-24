Computers and Electronics in Agriculture 145 (2018) 302–310

Contents lists available at ScienceDirect

Computers and Electronics in Agriculture

journal homepage: www.elsevier.com/locate/compag

Original papers

Research on a dissolved oxygen prediction method for recirculating
aquaculture systems based on a convolution neural network

T

Xuxiang Ta, Yaoguang Wei

⁎

College of Information and Electrical Engineering, China Agricultural University, 17 Tsinghua East Road, Beijing 100083, China

A R T I C L E I N F O

A B S T R A C T

Keywords:
Reverse understanding convolutional neural
network
Recirculating aquaculture systems
Dissolved oxygen
Self-multiplication vector
Prediction

Dissolved oxygen is the most critical parameter to be controlled in Recirculating Aquaculture Systems strictly to
maintain healthy conditions for aquatic products. Because of the lag between dissolved oxygen control measures
and the regulation eﬀect, changes in the dissolved oxygen must be forecast to maintain stable water quality.
Traditional methods, such as back propagation (BP) neural networks and time-series analyses, have poor sta-
bility and dynamic responses and thus present diﬃculties meeting the real-time dynamic regulation needs of
industrial aquaculture. Therefore, a simpliﬁed reverse understanding convolutional neural network (CNN)
prediction model is proposed in this study to solve the dissolved oxygen prediction problem. The model mul-
tiplies the input vector by its transpose to format a single depth input matrix. By removing the pooling layer, the
characteristics of the relational factors of dissolved oxygen are reﬁned by two successive convolutions of the
input matrix. Finally, the data are processed by the full connection layer, which uses the gradient descent
algorithm for the reverse update. Real-time data obtained from the Mingbo Experimental Base in Shandong
Province are analyzed, and the results show that the reverse understanding CNN is suitable for the prediction of
dissolved oxygen. Moreover, its convergence rate during pre-training is faster than that of the BP network under
the same conditions, and its prediction stability is superior. The accuracy and stability of the new model results
are suﬃcient to meet actual production demands.

1. Introduction

A recirculating aquaculture system (RAS) is a production mode that
adopts modern technologies to monitor water parameters, such as the
dissolved oxygen (An et al., 2015; Gao et al., 2016; Guo et al., 2013; Lu
et al., 2017; Terry et al., 2017; Xu and Xu, 2016; Schmautz et al., 2017),
pH, and electrical conductivity, for real-time puriﬁcation, real-time
increases in oxygen, and other operations. For an aquatic product,
dissolved oxygen supports the entire metabolic process of an organism.
The appropriate dissolved oxygen concentration promotes biological
growth and shortens the breeding cycle, thereby improving the eco-
nomic eﬃciency. Conversely, a dissolved oxygen concentration that is
too low will inhibit biological growth (Judd et al., 2016) and may even
lead to death, resulting in serious economic losses.

A water environment contains aquaculture organisms as well as a
variety of micro-organisms that cannot be observed by the naked eye.
These microbes and aquaculture organisms have a symbiotic relation-
ship (Judd et al., 2016; Scully, 2016), and a number of these micro-
organisms are aerobic, while others are anaerobic. An appropriate
symbiotic relationship must be established during the growth of

aquaculture organisms. In dynamic processes involving changes in the
dissolved oxygen, there are complex interactions between various en-
vironmental factors. A lag occurs between the implementation of
methods for controlling dissolved oxygen the realization of the eﬀects
of these methods. Therefore, throughout the breeding cycle, the dis-
solved oxygen trends must be predicted so that methods of controlling
and eliminating the risks to aquaculture caused by this lag eﬀect can be
implemented as soon as possible. Finally, reductions in unnecessary
energy consumption and economic cost are needed.

The traditional aquaculture model usually relies on artiﬁcial ex-
periences to control the water quality, creating challenges for meeting
the real-time monitoring of factory farming needs. In recent years, a
back propagation (BP) neural network (Scully, 2016; Pascanu et al.,
2013), time-series analysis (Chanda et al., 2017), and other methods
have been rapidly developed; however, they can easily fall into local
minima and present issues with stability and reliability. Improved op-
timization algorithms have increased the computational complexity and
instability of the model. Because of these problems, this paper presents
a simpliﬁed convolutional neural network (CNN) prediction model
the original
based on reverse understanding. To ensure that

⁎

Corresponding author.
E-mail addresses: taxuxiang@gmail.com (X. Ta), wyg@cau.edu.cn (Y. Wei).

https://doi.org/10.1016/j.compag.2017.12.037
Received 29 June 2017; Received in revised form 31 October 2017; Accepted 25 December 2017

0168-1699/ © 2017 Elsevier B.V. All rights reserved.

X. Ta, Y. Wei

Computers and Electronics in Agriculture 145 (2018) 302–310

characteristics are maintained, we subjected the input to a speciﬁc
treatment and then convoluted the data for processing. This method
simpliﬁes the overall computational complexity, increases the stability
of the model in practical applications, and improves the convergence
speed of the training model in a new environment.

2. Materials and methods

2.1. Model for predicting dissolved oxygen based on a reverse understanding
convolutional neural network

2.1.1. Reverse understanding convolutional neural network

In the 1960s, Hubel and Wiesel proposed a new method (the pro-
totype of the CNN’s receptive ﬁelds) for studying a cat’s cortex (Hubel
and Wiesel, 1962). Recently, CNNs have been extensively used for
solving various problems (Bengio, 2009; Bouvrie, 2006; Jafrasteh and
Fathianpour, 2017; Schmidhuber, 2015; Zeiler and Fergus, 2014;
Hejnol and Rentzsch, 2015). This type of network is a feed-forward
neural network that is mainly used in pattern recognition, pattern
classiﬁcation, and other ﬁelds. A CNN utilizes the direct input of the
original data through diﬀerent parts and levels of convolution, pooling,
and other series of operations to obtain and extract features in the
process of increasing the level of abstraction to achieve content preci-
sion identiﬁcation. The main network levels (such as the LeNet-5 model
(Zhao et al., 2010)) are the convolution layers, pooling layers, and full
connection layers. In the classiﬁcation model, a CNN has a prominent
performance. The error obtained by a CNN for handwritten MNIST
image classiﬁcation has been reduced to 0.23% (Ciresan, 2017). For the
more complex ImageNet (Deng, 2009) problem, an image recognition
algorithm based on a CNN has a far better performance than a human.
Because of the high accuracy of a CNN, a simpliﬁed reverse-un-
derstanding-CNN-based model is proposed to solve the problem of
dissolved oxygen prediction and eﬃciently manage graphics classiﬁ-
cation problems and depth network models. The model simpliﬁes cer-
tain calculations in the original CNN model (essentially because of the
support of reverse understanding) and changes its original abstract
progressive process. The model has the following characteristics:

(1) The input vector is multiplied by its transpose to format a self-mode
matrix to simulate a single-channel image in a two-dimensional
format;

(2) The model includes two consecutive convolution processes, and the
principle is changed from the original abstract progressive to the
reﬁned extraction of a potential relationship between the para-
meters that are output by the matrix;

(3) The pooling layers (Nielsen, 2017; Zaccone, 2016) of the original
CNN are removed. In the traditional CNN structure, each convolu-
tion layer usually follows a pool layer. The purpose of the pooling
layer is to extract the results of the convolution layer to a higher
level rather than to reﬁne of the results. The purpose of our model is
to reﬁne the potential factors; however, the inclusion of a pool layer
is not consistent with our goal; thus, it needs to be removed, which
would then reduce the number of calculations. Moreover, this re-
ﬁnement process also explains the meaning of reversing under-
standing.

The simpliﬁed network structure is shown in Fig. 1.
In this structure, we multiply the original vector by its transpose,
simulate the single depth matrix by using a 2 ∗ 2 ∗ 4 ﬁlter (length,
width, depth), and then obtain the ﬁrst convolution layer. The depth
(also called the “channel”) of the ﬁrst convolution layer is equal to the
depth of the ﬁlter. Four layers (L1, L L L
)
,
4 are observed, and each
layer is a 3 ∗ 3 matrix. Based on the ﬁrst convolution layer, we use the
same size as the ﬁlter and ultimately format the second convolution
layer. The second convolution layer is a 2 ∗ 2 matrix. Finally, the
multidimensional matrix is transformed by the stretching process.

,

3

2

When the multidimensional matrix becomes a vector, it is then entered
into the full connection layer for further processing.

2.2. Key features of the model

2.2.1. Self-multiplication of the input vector

The most important feature of a CNN is the use of a high-dimen-
sional matrix as an input, and the shared weights and shared biases are
used to obtain the characteristics by the extraction process of pro-
gressive abstraction during convolution. Furthermore, complex non-
linear relationships are observed among the many factors that aﬀect the
dissolved oxygen, such as the conductivity, temperature, and power -
of hydrogen (pH). To obtain the uncertain relationships between each
parameter by convolution and adapt to the input characteristics of a
CNN, four inﬂuencing factors are used as the input vector and the
EC T DO pH
matrix is calculated. Let =Z
,
(

)T; then,

,

,

Input

Z
= ×

T

Z

=

⎡
⎢
⎢
⎢
⎢
⎣

EC T
T
T

EC DO EC pH EC
EC
×
EC
pH T
T
×
EC DO T DO DO DO pH DO
×
pH DO pH pH pH
EC
×

×
DO T
×
×
×

×
×
×
×

×
×
×
×

pH T

⎤
⎥
⎥
⎥
⎥
⎦

(1)

where EC is the conductivity, T is the temperature, and DO is the dis-
solved oxygen. The symmetric array consists of four rows and four
columns, and this matrix has a single channel depth. This matrix results
from the multiplication of a vector and its transpose; thus, it can ac-
count for all combinations of any two parameters.

2.2.2. Reverse understanding of two consecutive convolution reﬁnement
extraction processes

The human and artiﬁcial recognition of an image begins from the
bottom of point recognition and then layer by layer to higher content
layers. In this process, the abstraction level becomes increasingly
higher, and a more accurate decision can be achieved. This process of
increasing the level of abstraction is achieved by the convolution op-
erations (Nielsen, 2017; Zaccone, 2016), and it simpliﬁes feature ex-
traction by the pooling layer. Convolution at the same level recognizes
the same level of abstraction of an image in diﬀerent parts with dif-
ferent methods (diﬀerent convolutions). Each of the local receptive
ﬁelds (Hubel and Wiesel, 1962; Nielsen, 2017; Zaccone, 2016) describe
a potential feature of the image. The convolution of a subsequent layer
is conducted with the convolution of the previous layer, thereby
achieving an improvement at the abstraction level. Complex interac-
tions occur among the dissolved oxygen, temperature, pH, conductivity,
and other water quality parameters; simultaneously, the change in the
dissolved oxygen is a continuous dynamic process. The relationships
between various water quality parameters are diﬃcult to describe with
a precise mathematical model, and the complex relationships between
them represent a popular and diﬃcult research topic. The process of
revealing this relationship is a reﬁnement process, that is, the reverse
process of abstraction. Through the above analysis, if the self-multi-
plication matrix is a relationship between the various factors of a
combination, then the ﬁrst convolution in the simpliﬁed reverse un-
derstanding CNN proposed in this paper is the ﬁrst latent relationship
reﬁnement of the factors and the second convolution is a reﬁnement of
the reﬁnement of the ﬁrst convolution. The two relationship reﬁnement
processes identify potential impactful relationships between the input
reﬁned to
parameters. Furthermore,
4 × 4 = 16 parameters (latent relationship). The implementation of
the simpliﬁed CNN and the original CNN convolution feature extraction
method are similar to a top-down search (reverse understanding CNN)
and bottom-up merging (original CNN).

the four parameters are

The two successive convolution processes of the input matrix are

illustrated in Fig. 2.

The parameters are marked as horizontal and vertical coordinates
by name. The input vector is self-accumulated to obtain the input

303

Download English Version:

https://daneshyari.com/en/article/6539798

Download Persian Version:

https://daneshyari.com/article/6539798

Daneshyari.com

