Stochastic Environmental Research and Risk Assessment
https://doi.org/10.1007/s00477-020-01776-2 (0123456789().,-volV)(0123456789().

,- volV)

ORIGINAL PAPER

Short-term water quality variable prediction using a hybrid CNN–LSTM
deep learning model

Rahim Barzegar1,2

• Mohammad Taghi Aalami2

• Jan Adamowski1

(cid:2) Springer-Verlag GmbH Germany, part of Springer Nature 2020

Abstract
Water quality monitoring is an important component of water resources management. In order to predict two water quality
variables, namely dissolved oxygen (DO; mg/L) and chlorophyll-a (Chl-a; lg/L) in the Small Prespa Lake in Greece, two
standalone deep learning (DL) models, the long short-term memory (LSTM) and convolutional neural network (CNN)
models, along with their hybrid, the CNN–LSTM model, were developed. The main novelty of this study was to build a
coupled CNN–LSTM model to predict water quality variables. Two traditional machine learning models, support-vector
regression (SVR) and decision tree (DT), were also developed to compare with the DL models. Time series of the
physicochemical water quality variables, speciﬁcally pH, oxidation–reduction potential (ORP; mV), water temperature
((cid:3)C), electrical conductivity (EC; lS/cm), DO and Chl-a, were obtained using a sensor at 15-min intervals from June 1,
2012 to May 31, 2013 for model development. Lag times of up to one (t - 1) and two (t - 2) for input variables pH, ORP,
water temperature, and EC were used to predict DO and Chl-a concentrations, respectively. Each model’s performance in
both training and testing phases was assessed using statistical metrics including the correlation coefﬁcient (r), root mean
square error (RMSE), mean absolute error (MAE), their normalized equivalents (RRMSE, RMAE; %), percentage of bias
(PBIAS), Nash–Sutcliffe coefﬁcient (ENS), Willmott’s Index, and graphical plots (Taylor diagram, box plot and spider
diagram). Results showed that LSTM outperformed the CNN model for DO prediction, but the standalone DL models
yielded similar performances for Chl-a prediction. Generally, the hybrid CNN–LSTM models outperformed the standalone
models (LSTM, CNN, SVR and DT models) in predicting both DO and Chl-a. By integrating the LSTM and CNN models,
the hybrid model successfully captured both the low and high levels of the water quality variables, particularly for the DO
concentrations.

Keywords Long short-term memory (cid:2) Convolutional neural network (cid:2) Water quality modeling (cid:2) Deep learning

1 Introduction

Water quality monitoring plays an important role in water
resources management. It can provide decision makers and
stakeholders with quantitative information to facili-
tate sustainable management of ongoing and emerging
environmental problems (Wu and Liu 2012; Wu and Chen

& Rahim Barzegar

rahim.barzegar@mail.mcgill.ca; rm.barzegar@tabrizu.ac.ir

1 Department of Bioresource Engineering, McGill University,
21111 Lakeshore, Ste Anne de Bellevue, Quebec H9X3V9,
Canada

2

Faculty of Civil Engineering, University of Tabriz, 29
Bahman Blvd., Tabriz 5166616471, Iran

2013). Speciﬁcally, water quality monitoring refers to the
collection, measurement and analysis of water samples to
determine the physicochemical and biological attributes of
a water body (Sinshaw et al. 2019). Dissolved oxygen (DO)
and chlorophyll-a (Chl-a) are two important water quality
variables used to monitor lakes. The DO concentration of a
water body indicates the equilibrium between the processes
that produce oxygen (e.g., photosynthesis) and consume
oxygen (e.g., chemical oxidation) (Fijani et al. 2019), and
Chl-a provides an estimate of the concentration of algae in
a water body, which is an indicator of eutrophication.
Monitoring these water quality variables is required for the
sustainable management of lake environments.

Conventional water quality monitoring techniques
require manual collection of water samples to later be

123

analyzed in a laboratory setting which is costly and time
consuming (Wu and Liu 2012). Another conventional
method involves the use of sensors, which have some
drawbacks. The main disadvantage is that they measure
few water quality variables, often with less accuracy than
manual collection (Oelen et al. 2018). Predictive modeling
using statistical and artiﬁcial intelligence approaches pro-
vide an alternative method for water quality monitoring.
These models have many beneﬁts: (1) reduce time and
costs (e.g., material and labor costs), (2) facilitate predic-
tion under various phases of a system, (3) simplify a
complicated system to improve its understanding, and (4)
predict
target values when site access is problematic
(Sinshaw et al. 2019). In recent decades, different predic-
tive models have been successfully applied to predict water
quality variables in water bodies, including the artiﬁcial
neural network (Alizadeh and Kavianpour 2015; Barzegar
et al. 2016a; Asadollahfardi et al. 2018; Sinshaw et al.
2019; Zhang et al. 2019; Goz et al. 2019; Zhu et al. 2019),
fuzzy logic (Chen and Mynett 2003; Pereira et al. 2009;
Huang et al. 2018), neuro fuzzy methods (Noori et al. 2013;
Barzegar et al. 2016a; Khadr 2017; Aghel et al. 2019; Kisi
et al. 2019; Zhu et al. 2019), M5P model-Tree (Yi et al.
2018), multivariate adaptive regression spline (MARS)
(Kisi and Parmar 2016; Najafzadeh and Ghaemi 2019),
extreme learning machines (ELM) (Fijani et al. 2019;
Barzegar et al. 2018; Goz et al. 2019), random forest
(Yajima and Derot 2018), decision tree (DT) (Jaloree et al.
2014) and least squares support vector machines (LSSVM)
(Noori et al. 2015b; Kisi and Parmar 2016; Fijani et al.
2019; Najafzadeh and Ghaemi 2019). However, the com-
plexity and non-linearity of water quality variables make it
challenging for these models to recognize the processes
that affect water quality. Therefore, more advanced pre-
diction models are still required to improve the accuracy of
water quality variable prediction.

Deep learning (DL), an advanced sub-ﬁeld of machine
learning (ML) for artiﬁcial intelligence, has been increas-
ing in popularity recently. It has been successfully applied
to many ﬁelds of science including computer vision (Fang
et al. 2019), image classiﬁcation (Affonso et al. 2017; Liu
et al. 2019c; Fan et al. 2019), speech recognition (Fayek
et al. 2017; Cummins et al. 2018), time series and spa-
tiotemporal prediction (Chen et al. 2018; Yang and Chen
2019; Xu et al. 2019; Bui et al. 2019) and natural language
processing (Shin et al. 2017; Plappert et al. 2018). DL
incorporates several ML algorithms that extract high-level
representations from complex data through a hierarchical
learning process using structures consisting of multiple
nonlinear transformations (Zuo et al. 2019).

Long short-term memory (LSTM) and convolutional
neural networks (CNN) are two popular DL models. The
LSTM is a type of recurrent neural network (RNN) which

123

Stochastic Environmental Research and Risk Assessment

collects extended sequential data in the hidden memory for
processing, representation and storage. Also, it updates
over time to ensure constancy in the time information (Kim
and Cho 2019). The CNN is composed of a sequence of
convolutional
layers, where each neuron in a layer is
connected to a small local region of neurons in the input
data. This is executed by sliding a weight matrix, called a
ﬁlter, over the input and the convolution (or dot product)
computed at each point, which is referred to as the feature
map, between the input and the ﬁlter. This architecture
enables the model to learn the ﬁlter needed to recognize
identiﬁed patterns in the input data (Borovykh et al. 2017).
Research on the application of DL models to the ﬁeld of
hydrology has recently been growing. For example, Tao
et al. (2016) used a stacked denoising autoencoder with
four layers and 1000 hidden nodes to extract precipitation
information from 15 9 15 pixel satellite cloud images.
Song et al. (2016) used a deep belief network with
observed land surface temperature and leaf area index as
inputs to predict ﬁeld-measured soil moisture. Zhang et al.
(2018) built different neural network models, including
LSTM and a gated recurrent network (GRU), to predict the
water
level of a combined sewage outﬂow structure.
Kratzert et al. (2018) used LSTM to model the rainfall-
runoff process of 241 catchments. More speciﬁcally, cer-
tain DL methods have been used to predict water quality
variables. For example, Liu et al. (2019b) used an LSTM
deep neural network in an Internet of Things (IoT) envi-
ronment to predict drinking-water quality in Yangzhou,
China. Chen et al. (2019) proposed a multivariate deep
belief network model with particle swarm optimization to
predict ammonia–nitrogen concentrations in aquaculture
ponds. Recently, Chl-a concentration in water bodies has
been predicted using DL models. Choi et al. (2019) applied
a CNN model to predict Chl-a concentration in Daechung
Lake, South Korea, with emphasis on handling data
imbalance and skewness. They indicated that using log
together
transformation and oversampling techniques
helped improve the performance of the CNN-based pre-
diction model, especially for small regions. Cho et al.
(2018) used LSTM for multi-step ahead prediction of Chl-a
in Gongju, South Korea. Their results showed that the
LSTM network model achieved higher accuracy than the
dense network model, and batch normalization as a regu-
larization method helped the learning process.

Hybrid neural networks, that incorporate the advantages
of several networks, have gained increasing attention in
recent years. It has been found that the combination of
CNN and LSTM can be useful to develop accurate pre-
dictive models (Kim and Cho 2019). Huang et al. (2018)
found that it is advantageous to perform feature extraction
using CNN, and then input the feature values in the LSTM
architecture. In the hybrid CNN–LSTM model, the one

Stochastic Environmental Research and Risk Assessment

dimensional-CNN extracts deep features of the main ele-
ments. Then, the LSTM model is applied to perform the
prediction by using these in-depth features. A combined
CNN–LSTM model was applied to predict crash risk (Li
et al. 2020), residential energy consumption (Kim and Cho
2019), as well as household power consumption (Kim and
Cho 2018, 2019).

The main focus of this research is to: (1) explore the
capability of DL models, namely the LSTM, CNN and
hybrid CNN–LSTM models, compared to traditional ML
models (the support vector regression (SVR) and decision
tree (DT) models) in predicting water quality variables
(DO and Chl-a concentrations); (2) compare the perfor-
mances of the LSTM and CNN methods for short-term
water quality variable prediction; and (3) develop a hybrid
model (CNN–LSTM) that combines the advantages of the
CNN and LSTM methods. Although, as mentioned above,
previous studies explored the ability of these methods to
predict water quality variables, no studies have compared
their performances. Also,
to the best of the authors’
knowledge, this is the ﬁrst time a coupled CNN–LSTM
model has been used to predict water quality variables.

2 Materials and methods

2.1 Case study area and data collection

The Prespa basin is situated in the Balkan peninsula in
southeastern Europe and is shared between three countries:
Albania, Greece and Macedonia. The basin is comprised of
two inter-linked lakes, Big Prespa and Small Prespa. These
lakes are separated by an alluvial
isthmus situated in
Greece (Panagiotopoulos et al. 2013) and the lakes are
connected by a small artiﬁcial channel (Krstic´ 2012). Small
Prespa Lake has a total area of 47.4 km2, of which
43.5 km2 belong to Greece and 3.9 km2 to Albania
(Fig. 1). This study focuses on predicting water quality
variables solely for Small Prespa Lake. The lake is mostly
recharged by runoff from different surface bodies and lat-
eral sub-surface ﬂow that occurs due to cross ﬂows in the
interacting aquifer systems of the area (Tziritis 2014).
Another important source of recharge for the lake, during
speciﬁc periods of the year, comes from the Devoll River
into the southwest portion of the lake, on the Albanian side
(Fijani et al. 2019). The Prespa area experiences a hot and
dry climate during the summer, with a mean annual tem-
perature of 23.6 (cid:3)C in July. In contrast, the winters are cold
with a mean temperature of 0.8 (cid:3)C in January (Hollis and
Stevenson 1997; Fijani et al. 2019). The average annual
rainfall and air
temperature are 647 mm and 14 (cid:3)C,
respectively.

In recent decades, anthropogenic pressures on Small
Prespa Lake have signiﬁcantly decreased the water level
and caused deterioration of the water quality. The water
loss is mainly due to intensiﬁed irrigated agricultural
practices (Patceva and Mitic 2010). Moreover, the lake
may be threatened by eutrophication due to elevated con-
centrations of Chl-a. Therefore, monitoring the water
quality in this lake is increasingly important. The water
quality data used to develop the models in this study were
gathered using sensors between June 1, 2012 and May 31,
2013 at 15-min intervals (Tziritis 2014). The physico-
chemical variables, including electrical conductivity (EC),
oxidation–reduction potential (ORP), pH, water tempera-
ture, dissolved oxygen (DO) and chlorophyll-a (Chl-a),
were measured by a multi-probe sensor CYCLOPS-7 of
TURNER DESIGS(cid:4) in Small Prespa Lake. The sensor was
deployed at a depth of 1.5 m at the northern side of the
lake. The sensor reached a total depth of approximately
3 m, with minor ﬂuctuations throughout the year (Tziritis
2014).

Descriptive statistics of the water quality data used in
this study, including minimum, maximum, mean, standard
deviation, skewness and kurtosis, can be found in Table 1.
Standard deviation was highest for the EC (57.33 lS/cm)
and ORP (52.63 mV), while pH (0.19) had the lowest
standard deviation. The DO concentration ranged between
0.02 and 14.97 mg/L, with a mean of 8.83 mg/L. The
minimum and maximum values of Chl-a were 0.6 and
22.8 lg/L (with a mean of 2.67 lg/L). The skewness and
kurtosis for the ORP (- 1.64 and 2.98 mV, respectively)
and Chl-a (2.65 and 14.76 lg/L, respectively) variables
were outside the range of - 2 and ? 2, indicating that
these variables did not follow a normal (Gaussian) distri-
bution (Barzegar et al. 2016b).

2.2 Long short-term memory (LSTM)

LSTM neural networks are an improvement over RNNs,
which were designed for sequence prediction, because they
address the stability restriction (i.e., the vanishing gradient
problem) of traditional RNNs by combining gating func-
tions with state dynamics (Hochreiter and Schmidhuber
1997). An LSTM network includes several memory blocks
that are connected via layers. Each layer is comprised of a
set of recurrently connected memory cells and three mul-
tiplicative units: the input, forget and output gates (Yuan
et al. 2018). The input gate provides the information to the
cell state in three steps. First, input values added to the cell
state are regulated with the sigmoid function. Second, a
vector is created containing all possible values to be added
to the cell state using the hyperbolic tangent function.
Finally, the regulatory ﬁlter is multiplied by the newly
created vector, and the information is added to the cell

123

Stochastic Environmental Research and Risk Assessment

Fig. 1 Location of Small Prespa Lake. Adapted from https://commons.wikimedia.org/wi

Table 1 Statistical summary of
the physicochemical water
quality variables in Small
Prespa Lake

Water quality variable

Min

Max

Mean

SD

Skewness

Kurtosis

EC (lS/cm)

ORP (mV)

pH

Water temperature ((cid:3)C)
DO (mg/L)
Chl-a (lg/L)

247.00

139.10

6.80

2.90
0.02

0.60

493.00

474.30

8.60

29.00
14.97

22.80

325.59

392.29

8.04

15.48
8.83

2.67

57.33

52.63

0.19

8.14
2.26

1.50

0.87

- 1.64

- 0.22

- 0.03
0.09

2.65

- 0.23

2.98

0.41

- 1.49
- 1.15

14.76

state. Using a multiplying ﬁlter, the forget gate removes the
information that is no longer required for the LSTM to
understand processes or the information of lesser impor-
tance. The output gate chooses the useful information from
the current cell state and displays it as the output.

The architecture of the LSTM model and the structure of
an LSTM cell are shown in Fig. 2. Suppose the input time
series data is x ¼ ðx1; x2; . . .; xt(cid:3)1; xtÞ. A typical LSTM cell
contains sigmoid (r) and hyperbolic tangent layers, along
with pointwise summation ((cid:4)), and multiplication ((cid:5))

123

Stochastic Environmental Research and Risk Assessment

Fig. 2 Architecture of the LSTM model and LSTM cell structure (Wu and Lin 2019)

operations. The LSTM can predict the target variables y ¼
y1; y2; . . .; yt(cid:3)1; yt
Þ by updating the gates (input gate it,
ð
forget gate ft and output gate yt) on the memory cell ct,
from time t ¼ 1 to T. The mathematical equations for the
LSTM are deﬁned as follows (Wu and Lin 2019):

output gate bias vectors, respectively, ct(cid:3)1 and ht(cid:3)1 are the
previous cell and its output vector, respectively, and ht is
the output vector.

2.3 Convolutional neural network (CNN)

it ¼ rðwixt þ Riht(cid:3)1 þ biÞ

ft ¼ rðwf xt þ Rf ht(cid:3)1 þ bf Þ

yt ¼ rðwyxt þ Ryht(cid:3)1 þ byÞ

ct ¼ ftct(cid:3)1 þ it (cid:2)ct

(cid:2)ct ¼ rðwcxt þ Rcht(cid:3)1 þ bcÞ

ht ¼ ytrðctÞ

ð1Þ

ð2Þ

ð3Þ

ð4Þ

ð5Þ

ð6Þ

where xt is the input vector, wi, wf , and wy denote the
matrix of weights from the input, forget, and output gates
to the input, respectively, Ri, Rf , and Ry deﬁne the matrix
of weights from the input, forget, and output gates to the
input, respectively, bi, bf , by are the input, forget, and

The CNN model consists of three layers: the input, hidden
and output layers. The input of a three-dimensional array is
usually fed to a convolutional layer where the dimensions
are represented by height, weight and the number of
channels. Assuming a one-dimensional input x ¼ xtð ÞN(cid:3)1
t¼0
of size N with no zero padding in the ﬁrst layer, the feature
output map is generated through convolving this input with
a set of M1 three-dimensional ﬁlters, w1
h for h ¼ 1; . . .; M1,
in which the ﬁlters are employed over all the input channels
(Borovykh et al. 2017):

a1ði; hÞ ¼ w1

h (cid:6) x

(cid:2)

(cid:3)ðiÞ ¼

1
X

j¼(cid:3)1

w1

hðjÞ (cid:6) ði (cid:3) jÞ

ð7Þ

123

Stochastic Environmental Research and Risk Assessment

features to LSTM cells, and several hidden layers. The
hidden layer typically includes a convolution layer, an
activation function, and a pooling layer. The output of the
LSTM is used as the input to the fully connected layer. The
CNN layers are used to learn sequential features of the
inputs, which conventional neural networks cannot do, and
the lower LSTM layer incorporates these features by han-
dling long-range dependencies for prediction of the target
values. The topological architecture of the CNN–LSTM
model is presented in Fig. 4.

2.4 Support vector regression (SVR)

SVR is a classical supervised machine learning method that
was ﬁrst proposed by Cortes and Vapnik (1995). Initially,
the purpose of the SVR was to convert a low-dimensional
nonlinear feature into a high-dimensional linear feature
through kernel functions to avoid dimensionality (Huang
et al. 2019). It is implemented through the frame of sta-
tistical
learning theory and the minimal structure risk
principle (Lei et al. 2019). Many papers and books (Vapnik
1995; Cortes and Vapnik 1995; Li et al. 2013; Noori et al.
2009, 2011, 2015a; Barzegar et al. 2017; Yu et al. 2017;
Babaei et al. 2019) describe the principles and mathemat-
ical equations entailed in SVR; therefore, this paper does
not include this.

2.5 Decision tree (DT)

DT is a non-parametric white-box supervised ML method
(Quinlan 1986) based on a collection of decision rules (i.e.,
if–then rules). This method is composed of three types of
nodes: (1) root nodes, also called decision nodes, which
represent a choice that brings the subdivision of all samples
into two or more similarly independent subsets, (2) internal
nodes, also referred to as chance nodes, which indicate the
possible choice of the feature (or attribute) in the tree, and
(3) leaf nodes, also termed end nodes, which show the
outcome as an aggregation of decisions (Song and Ying
2015). The model is created top-down in the form of a tree
where the training data are partitioned in a recursive
manner from a root node, followed by subsequent splitting
points (internal nodes), which end in distinct leaves where
the division terminates (Bacal et al. 2019). Each node in a
decision tree is designated by an attribute which is chosen
according to its ability to decrease chaos in the classiﬁca-
tion (Bacal et al. 2019). Additional details about the DT
model can be found in Quinlan (1986) and Song and Ying
(2015).

h 2 R1(cid:6)k(cid:6)1 and a1 2 R1(cid:6)N(cid:3)kþ1(cid:6)M1. There will be
where w1
one input channel, and the output of the ﬁrst layer is then
passed through the non-linear activation function h((cid:2)) to
give f 1 ¼ hða1Þ.

The hidden layer includes a convolutional layer, pooling
layer, and fully connected layer. The convolutional layer is
responsible for automatically extracting features at various
regions of the entire raw input or the intermediate feature
maps with learnable ﬁlters (Zuo et al. 2019). Neurons in
one convolution layer are not connected to all the neurons
in the next layer but only to a small region of it. Therefore,
the ﬁlter employs a shared weight matrix to perform the
convolutional operation. Note that the weights are updated
during the training process (Hoseinzade and Haratizadeh
2019). The pooling layer converts all the values in the
pooling window to one value. This
transformation
decreases the size of the input layer with a max-pooling
operation, which selects the maximum value from each
subarea of the previous layer (Zuo et al. 2019). Moreover,
this layer reduces the computational cost of the learning
process and handles any overﬁtting issues (Hoseinzade and
Haratizadeh 2019).

In the hidden layer l ¼ 2; . . .; L, the input feature map
f l(cid:3)1 2 R1(cid:6)Nl(cid:3)1(cid:6)Ml(cid:3)1 , where 1 (cid:6) Nl(cid:3)1 (cid:6) Ml(cid:3)1 is the size of
the output ﬁlter map from the previous convolution with
Nl(cid:3)1 ¼ Nl(cid:3)2 (cid:3) k þ 1, is convolved with a set of M1 ﬁlters
h 2 R1(cid:6)k(cid:6)Ml(cid:3)1, h ¼ 1; . . .; M1, to create a feature map a1 2
w1
R1(cid:6)Nl(cid:6)Ml as follows (Borovykh et al. 2017):

a1ði; hÞ ¼ wl

h (cid:6) f l(cid:3)1

(cid:2)

(cid:3)ðiÞ ¼

X1

Ml(cid:3)1
X

j¼(cid:3)1

m¼1

hðj; mÞf l(cid:3)1ði (cid:3) j; mÞ
wl

ð8Þ

The fully connected layer ﬂattens

the high-level
extracted features that are learned by the convolution layer,
and incorporates them to obtain the ﬁnal output. Then the
resulting feature values are passed through the non-linear
activation functions to give f 1 ¼ hða1Þ. After L convolu-
tional layers, the output of the network will be the matrix
f L, whose size depends on the ﬁlter size and number of
ﬁlters used in the ﬁnal layer (Borovykh et al. 2017). Fig-
ure 3 represents the architecture of the CNN model.

2.3.1 CNN–LSTM hybrid model

Both CNN and LSTM models have their speciﬁc features.
In this study, a hybrid CNN–LSTM DL model, which
integrates the advantages of both the CNN and LSTM
models, was developed to predict water quality variables.
First, the upper layer of the CNN–LSTM architecture was
composed of CNN layers. CNN includes an input layer that
enters the input variables, an output layer that extracts

123

Stochastic Environmental Research and Risk Assessment

Fig. 3 The structure of the CNN model (Zuo et al. 2019)

Fig. 4 The structure of the hybrid CNN–LSTM model (Liu et al. 2019a)

2.6 Model performance

The performance of the different models was evaluated
using the correlation coefﬁcient (r), root mean square error
(RMSE), mean absolute error (MAE), and their normalized
equivalents expressed as a percentage (RRMSE, RMAE),
percentage of bias (PBIAS), Nash–Sutcliffe coefﬁcient
(ENS) and Willmott’s Index (WI). Equations and explana-
tions of all these statistical metrics are widely discussed
elsewhere (Ghorbani et al. 2018; Barzegar et al. 2019;
Fijani et al. 2019).

The r metric represents the strength of

the linear
regression between observed and predicted values. The
strongest linear relationship occurs when r equals 1. The
RMSE and MAE express the accuracy of the models. Both
metrics can range from 0 to !, where 0 indicates the

or

unsatisfactory

highest accuracy. Model precision was evaluated with
RRMSE and RMAE, which compare the percentage devi-
ation from the predicted data. The performance of the
model for PBIAS is considered very good, good, satisfac-
PBIAS \ ± 10, ± 10 B
tory
if
PBIAS \ ± 15, ± 15 B PBIAS \ ± 25 or PBIAS [ ±
25, respectively (Legates and McCabe 1999). According
to the ENS metric, each model’s performance is categorized
as very good, good, satisfactory, acceptable or unsatisfac-
0.65 \ ENS B 0.75,
tory
0.50 \ ENS B 0.65, 0.40 \ ENS B 0.50 or ENS B 0.4,
respectively (Moriasi et al. 2007; Khosravi et al. 2018).
The WI metric is used to detect sensitivity to outliers in the
observed data or insensitivity to the additive or propor-
tional differences between predictions and observations,

0.75 \ ENS B 1.00,

if

123

Stochastic Environmental Research and Risk Assessment

from each neuron cluster was in the previous layer. A
dropout layer with a rate of 0.001 was used after the
pooling layer in the CNN to adjust for overﬁtting; the
pooling layer can also be helpful to overcome overﬁtting
(Kim and Cho 2019). A fully connected layer, which is
called ‘‘dense’’, was applied to the output layer where a
linear activation function was used. Finally, the model was
compiled with an MSE loss function and an AdaGrad
optimizer with a learning rate of 0.01. For the DO pre-
diction, the CNN model had a similar structure except that
a ﬁlter size of 32 was used. The loss plots for the CNN
models are presented in Fig. 5.

In the hybrid model, the convolutional layer, the hidden
layer and the pooling layer, which are part of the CNN
model, were formatted in the same way as those of the
standalone CNN model. Similarly, the LSTM part was
formatted like the standalone LSTM model. The structures
of the DL models are listed in Table 2.

The SVR models were constructed using the epsilon-
SVR kernel-type equation. Different kernel function types,
e.g.,
linear, radial basis function (RBF), sigmoid, and
polynomial, were considered when developing the SVR
models. The RBF was the optimal kernel, with the smallest
error for both DO and Chl-a prediction. It performed better
than other kernel functions because it has fewer hyper-
parameters, which decrease the complexity of the model.
While training the SVR model with the RBF kernel func-
tion, the regulation factor (C), epsilon (e), and gamma (c)
hyper-parameters were set. A grid search with tenfold
cross-validation, as suggested by Noori et al. (2009, 2011),
was employed in the training phase for hyper-parameter
tuning. In this procedure, samples were chosen from the
space of the independent variables. Then, an error score
was computed for each sample prediction and compared
with the error scores found from the previous iterations. If
the obtained error score at an iteration was lower than the
previous one, the predictions with the lower error score
were retained. This process was repeated until the end of
iterations was reached. For the DO model, the optimal
values of the C, e, and c were 1, 0.01, and 0.1, respectively,
while the optimal values for the Chl-a model were 1, 0.1,
and 0.1, respectively. The scikit-learn library (Pedregosa
et al. 2011) for Python was used to implement the SVR
models.

When developing the DT models, the maximum depth
parameter had to be selected. It was chosen by trial and
error using different maximum depth values between 1 and
10 at intervals of 1. The optimal maximum depths, based
on the lowest RMSE, for the DO and Chl-a prediction
models were 8 and 3, respectively.

which can occur with r, RMSE, MAE and BIAS metrics
(Willmott 1981; Yaseen et al. 2018).

2.7 Predictive model implementation

Easily measured and accessible physicochemical water
variables (e.g., pH, ORP (mV)), water temperature ((cid:3)C)
and EC (lS/cm) were used to develop the predictive
models for water quality variables (i.e., DO (mg/L) and
Chl-a (lg/L)) in Small Prespa Lake, Greece. First, the
dataset of each prediction model was partitioned into two
subsets: 70% for the training stage and 30% for the testing
stage. The training dataset was used to develop the models,
while the testing dataset was used to validate and compare
the performance of models developed in the training phase.
All input and output variables of the models were scaled
between 0 and 1 via normalization and minimum–maxi-
mum scaling techniques, executed in the scikit-learn pre-
processing library (Pedregosa et al. 2011) using Python.
This process prevents dramatic changes in gradient and
smooths the convergence. Also, all training and testing
datasets were transformed into a supervised learning frame
with the ‘series_to_supervised’ Python function, in which
time series sequences are converted to input–output pairs
using the sliding windows procedure (Cai et al. 2019). This
was executed using lag observations (i.e., t - 1) as inputs
and the current observation (t) as the output variable. The
best lag times were determined by trial and error and
indicated by the lowest RMSE. Therefore, lag times of up
to one (t - 1) and two (t - 2) for the input variables,
which included pH, ORP, water temperature and EC, were
used when developing the DO and Chl-a prediction mod-
els, respectively.

The LSTM models consist of an input layer, where the
inputs (i.e., pH, ORP (mV), water temperature ((cid:3)C) and EC
(lS/cm)) and their lag times were imported to all three
layers. To develop this model, an LSTM layer with an
activation function represented by an Exponential Linear
Unit (ELU), and having units of 64 and 32 for Chl-a and
DO predictions, was used in the hidden layer. To avoid
overﬁtting, a dropout layer with a rate of 0.001 was applied
after the LSTM layer. A fully connected layer, termed
‘‘dense’’, with a unit of 1 and a linear activation function,
were used. Then, the model was compiled with a mean
squared error (MSE) loss function and an adaptive gradient
algorithm (AdaGrad) optimizer with a learning rate of 0.01.
Figure 5 shows the loss function plots for the models.

The CNN model for Chl-a prediction was trained with a
hidden layer, where a convolution layer (Conv1D) with a
ﬁlter size of 128, a kernel size of 2, the same padding type,
an ELU activation type, and a uniform kernel initializer
were used. Also, a pooling layer with max-pooling and a
pooling size of 1, was applied where the maximum value

123

Stochastic Environmental Research and Risk Assessment

Fig. 5 Loss function plots for the DL models developed to predict DO and Chl-a

3 Results and discussion

The objective of this research was to investigate the per-
formance of three DL models, namely the LSTM, CNN,
and hybrid CNN–LSTM models, to predict water quality
variables (i.e., DO and Chl-a). Also, two traditional ML
models,
the SVR and DT models, were developed to
compare their performances to that of the DL models. After
training the abovementioned models, the testing data were
fed into the models to predict the target variables. The
models were evaluated and compared using statistical
including r, RMSE, RRMSE, MAE, RMAE,
indicators,
PBIAS, ENS and WI, in the training and testing periods.
The results are summarized in Table 3.

the LSTM model

For DO prediction,

(r = 0.968,
RMSE = 0.545mg/L, MAE = 0.410mg/L, ENS = 0.932 and
WI = 0.984) outperformed the CNN model (r = 0.967,
RMSE = 0.658mg/L, MAE = 0.522 mg/L, ENS = 0.902
and WI = 0.977) in the training and testing phases. This is
consistent with results from a previous study by Gu et al.
(2019), which concluded that the LSTM model performed
better than the CNN model in time series prediction. This is

likely due to the fact that the CNN model cannot capture
the long-term dependency. The hybrid CNN–LSTM
(r = 0.970,
RMSE = 0.518mg/L, MAE = 0.392mg/L,
ENS = 0.939 and WI = 0.982) model outperformed the
standalone models in the testing period for DO prediction.
Overall, the RMAE of the CNN–LSTM-based DO predic-
tion model was 0.24% and 1.45% lower than the LSTM
and CNN models in the testing period, respectively. Fig-
ure 6 illustrates the observed and predicted DO values
computed by the models in the testing period. Interestingly,
in the testing period, the LSTM model performed better
when predicting higher levels of DO, while the CNN model
was better at predicting lower levels of DO. The hybrid
CNN–LSTM model better captured both the lower and
higher levels of DO concentrations by combining the
strengths of the standalone models. All established DL
models outperformed the traditional ML models (i.e., SVR
and DT models) when predicting DO in the testing period.
The CNN–LSTM model had an RMAE 2.55% and 1.18%
lower than the SVR and DT models, respectively. Based on
the PBIAS and ENS values, all had good performances in
predicting DO in the testing period.

123

Stochastic Environmental Research and Risk Assessment

Table 2 The structures of the developed DL models

Model

Predicted
variable

Structure

LSTM

DO

1 LSTM layer (32 neurons, ELU activation) ? 1 Dropout layer (0.001) ? 1 Dense layer (1 neuron, linear

activation) ? Compile (MSE loss, Adam optimizer with a learning rate of 0.01)

Chl-a

1 LSTM layer (64 neurons ? ELU activation) ? 1 Dropout layer (0.001) ? 1 Dense layer (1 neuron, linear

activation) ? Compile (MSE loss, Adam optimizer with a learning rate of 0.001)

CNN

DO

Convolutional layer (32 ﬁlters ? 2 ﬁlter sizes ? ELU activation ? padding ‘same’ ? 1 stride) ? Maxpooling (1
pooling size) ? Flatten ? Dense layer (12 neurons, linear activation) ? 1 Dropout layer (0.001) ? 1 Dense
layer (1 neuron) ? Compile (MSE loss, Adagrad optimizer with a learning rate of 0.01)

Chl-a

Convolutional layer (128 ﬁlters ? 2 ﬁlter sizes ? ELU activation ? padding ‘same’ ? 1 stride) ? Maxpooling
(1 pooling size) ? Flatten ? Dense layer (30 neurons, SELU activation) ? 1 Dropout layer (0.001) ? 1 Dense
layer (1 neuron) ? Compile (MSE loss, Adagrad optimizer with a learning rate of 0.002)

CNN–

LSTM

DO

Dense layer (32 neuros) ? Convolutional layer (32 ﬁlters ? 1 ﬁlter size ? ELU activation ? padding ‘same’ ? 1
stride) ? Maxpooling (1 pooling size) ? 1 Dropout layer (0.001) ? Convolutional layer (64 ﬁlters ? 2 ﬁlter
sizes ? ELU activation ? padding ‘same’ ? 1 stride) ? MaxPooling (2 pooling size) ? 1 Dropout layer
(0.001) ? 1 LSTM layer (64 neurons ? ELU activation) ? 1 Dropout layer (0.001) ? Flatten ? 1 Dense layer
(1 neuron, linear activation) ? 1 Dropout layer (0.001) ? 1 Dense layer (1 neuron) ? Compile (MSE loss,
Adagrad optimizer with a learning rate of 0.01)

Chl-a

Dense layer (256 neuros) ? Convolutional layer (128 ﬁlters ? 1 ﬁlter size ? ELU activation ? padding

‘same’ ? 1 stride) ? Maxpooling (1 pooling size) ? 1 Dropout layer (0.001) ? Convolutional layer (64
ﬁlters ? 2 ﬁlter size ? ELU activation ? padding ‘same’ ? 1 stride) ? MaxPooling (2 pooling sizes) ? 1
Dropout layer (0.001) ? 1 LSTM layer (32 neurons ? ELU activation) ? 1 Dropout layer
(0.001) ? Flatten ? 1 Dense layer (8 neuron, linear activation) ? 1 Dropout layer (0.001) ? 1 Dense layer (1
neuron) ? Compile (MSE loss, Adagrad optimizer with a learning rate of 0.01)

Table 3 The results of the developed DL and ML models for predicting DO and Chl-a in Small Prespa Lake

Variable Metric

Training period

Testing period

LSTM CNN

CNN–LSTM SVR

DT

LSTM CNN

CNN–LSTM SVR

DT

DO

r

RMSE (mg/L)
MAE (mg/L)
PBIAS
ENS
RRMSE (%)
RMAE (%)
WI

Chl-a

r

RMSE (mg/L)
MAE (mg/L)
PBIAS
ENS
RRMSE (%)
RMAE (%)
WI

0.960

0.680

0.960

0.632

0.960

0.682

0.521

0.526
- 2.733 - 1.324 - 2.922

0.472

0.907

8.007

8.666

0.971

0.924

0.641

0.325

1.828

0.841

0.920

7.451

7.125

0.978

0.923

0.651

0.328

3.395

0.836

23.447

11.701

0.940

23.808

11.552

0.938

0.907

8.030

8.046

0.972

0.9237

0.6465

0.3087

4.332

0.839

23.636

10.197

0.9416

0.944

0.734

0.529
0.251

0.892

8.646

7.741

0.971

0.893

1.151

0.974

0.949

0.706

0.511
0.001

0.900

8.318

6.751

0.973

0.913

0.655

0.344

0.968

0.545

0.410
1.050

0.932

5.668

4.425

0.984

0.869

0.614

0.433

0.967

0.658

0.522
3.983

0.902

6.837

5.629

0.977

0.872

0.611

0.432

- 23.895

0.005 - 4.617 - 5.194

0.970

0.518

0.392
0.221

0.939

5.381

4.176

0.982

0.874

0.579

0.359

2.190

0.757

0.489

0.834

42.092

23.972

53.191

11.693

0.845

0.950

0.727

24.445

21.507

0.877

0.730

24.325

22.05

21.580

15.093

0.879

0.905

0.953

0.804

0.634
5.241

0.854

8.354

6.730

0.965

0.854

0.766

0.618

0.932

0.764

0.569
0.531

0.868

7.946

6.059

0.962

0.844

0.646

0.404

- 11.570 - 0.893

0.575

30.505

33.534

0.742

0.698

25.705

16.773

0.918

The scatter plots of the observed and predicted DO in
the testing period (Fig. 6) show that
the CNN–LSTM
model was more accurate than the other models. It had the

highest r and was well described by the linear regression
equation y = 0.9065x - 0.8789. The DT model had more

123

Stochastic Environmental Research and Risk Assessment

Fig. 6 Plots of the observed and
predicted DO concentrations
using the models developed

123

scattered DO predictions, and its linear regression equation
was y = 0.8776x - 1.1275.

For Chl-a prediction, the predictive power of the LSTM
(r = 0.869,
RMSE = 0.614mg/L, MAE = 0.433mg/L,
ENS = 0.727, and WI = 0.877) and CNN (r = 0.872,
RMSE = 0.611mg/L, MAE = 0.432mg/L, ENS = 0.730, and
WI = 0.879) models were similar. The hybrid CNN–LSTM
model had an r of 0.874, an RMSE of 0.579 mg/L, an MAE
of 0.359 mg/L, an ENS of 0.757 and a WI of 0.905. The
RMAE of the CNN–LSTM-based Chl-a prediction model
was 6.41% and 6.48% lower than the LSTM and CNN-
based Chl-a prediction models in the testing phase,
respectively. Therefore,
the hybrid CNN–LSTM model
outperformed the LSTM and CNN models in predicting
Chl-a values. Based on the ENS values for the predictive
modeling of Chl-a in the testing phase, the hybrid CNN–
LSTM model (ENS = 0.757) had a very good performance,
while the other models, i.e., LSTM (0.727), CNN (0.730),
SVR (0.575) and DT (0.698), exhibited only good perfor-
mances. Also, according to the PBIAS metric in the testing
period, all models developed for Chl-a prediction had very
good performances, except the SVR model, which only had
a good performance. Again, the DL models performed
better than the traditional ML models. The scatter plots of
the observed and predicted Chl-a concentrations in the
testing period (Fig. 7) show that the hybrid CNN–LSTM
predictions, ﬁtted by the linear
regression equation
y = 0.6998x - 0.7008, resulted in more accurate and less
scattered predictions. In contrast, the DT model was the
least accurate and most scattered, with a linear regression
equation of y = 0.8121x - 0.4951.

The models’ efﬁciency was investigated using Taylor
diagrams (Fig. 8). For DO prediction, the CNN–LSTM,
with a correlation coefﬁcient of 0.97 and a normalized
standard deviation of 0.93, had the best results. The SVR
model, with a correlation coefﬁcient of 0.95 and a nor-
malized standard deviation of 1.0, had the worst results.
Similar to DO prediction, the CNN–LSTM-based Chl-a
predictive model, with a correlation coefﬁcient of 0.87 and
normalized standard deviation of 0.79, was the best at
predicting Chl-a. Once again,
the SVR model, with a
correlation coefﬁcient of 0.85 and normalized standard
deviation of 0.57, performed the worst of all the models. In
summary,
the CNN–LSTM hybrid model was the best
at predicting both DO and Chl-a.

Figure 9 shows the box plots of the observed and pre-
dicted values of DO and Chl-a in Small Prespa Lake. The
median values generated by the LSTM and CNN–LSTM
models were similar to the observed DO values. These
models differed in the lower quartile, the 25th percentile
(Q25), and in data range (maximum and minimum). The
Q25 for the CNN–LSTM model was similar to the observed
DO values, while the data range of the LSTM model was

123

Stochastic Environmental Research and Risk Assessment

close to the observed DO values. Although the medians for
the LSTM, CNN and CNN–LSTM models were close to
the observed Chl-a values, the Q25 and minimum values
were closer to the observed Chl-a values. Also, the upper
outliers for the CNN–LSTM model were closest to the
observed Chl-a values, followed by the CNN and LSTM
models. For both the DO and Chl-a variables, the SVR
model had the most different statistical variables, indicat-
ing that it performed the worst out of all the models.
Overall, the DL-based prediction models closely matched
the observed values within the testing period, while the
SVR and DT models failed to do so. The DT and SVR
models require well-structured data for more accurate
predictions (Bui et al. 2020). However, DL models are
powerful predictive models even when the data are poorly
structured.

Figure 10a, b illustrate the spider-plots of the RRMSE
and ENS for the models, which were used to validate the
models’ performance. For both the DO and Chl-a simula-
tions, the CNN–LSTM yielded the lowest RRMSE and the
largest ENS, indicating that it was the best performing
model. In contrast, the SVR model obtained the highest
RRMSE and smallest value of ENS, indicating it was the
worst performing model.

The histogram plots of the models’ prediction errors
were used to investigate the distribution of prediction
errors for the different models in the testing period. The
plots were generated using several prediction error inter-
vals with widths of ± 0.1 mg/L and ± 0.1 lg/L for the
DO and Chl-a simulations, respectively (Fig. 11). For the
predictive DO models, the height of the error bin for the
CNN–LSTM model showed the greatest frequency (18.1%)
for the smallest error magnitude (0.1 mg/L) compared to
the LSTM and CNN models, which had the highest fre-
quencies of 14.7% and 12.8% for the error magnitude of
0.2 mg/L, respectively. Similarly, for the Chl-a predictions,
the CNN–LSTM model, with a frequency of 21.6%,
the smallest error
frequency for
obtained the largest
(0.1 lg/L) compared to the LSTM (14.8%) and CNN
(15.4%) models for the error magnitude of 0.4 lg/L. These
histogram plots show that the hybrid CNN–LSTM models
are more reliable than the LSTM and CNN models when
predicting DO and Chl-a as most of their prediction errors
occurred within the lowest magnitude band. Generally, the
models developed for DO prediction performed better than
those developed for Chl-a prediction. This may be due to
the linear and nonlinear relationships between the input and
output variables. The Pearson’s correlation for Chl-a and
the input variables (EC (- 0.31), ORP (0.08), pH (0.11)
and water temperature (- 0.13)), and for the DO and the
input variables (EC (- 0.29), ORP (0.29), pH (0.49) and
water temperature (- 0.72)), indicate that the linear rela-
tionship between the inputs and output in the DO model

Stochastic Environmental Research and Risk Assessment

Fig. 7 Plots of the observed and
predicted Chl-a concentrations
using the models developed

123

Stochastic Environmental Research and Risk Assessment

Fig. 8 Taylor plot of the models’ performances in predicting DO and Chl- in Small Prespa Lake

Fig. 9 Box plot comparing the models’ abilities to predict DO and Chl-a in Small Prespa Lake

was more signiﬁcant than the linear relationship between
the inputs and output variables in the Chl-a model.
Therefore,
the prediction of the DO variable is more
dependent on the physicochemical variables than the Chl-a
variable.

It was observed that all the developed DL models had a
high level of learning and predictive power, with minor
variations that may be related to their different learning
approaches (Bui et al. 2020). Although implementation of
the DL models is more complex than traditional ML
learning
models,

higher ﬂexibility

have

they

in

nonlinearity, especially in large datasets. Although this
study conﬁrmed the capability of the CNN, LSTM and
CNN–LSTM models for short-term prediction tasks, Wang
et al. (2019) indicated that LSTM is robust with respect to
medium-term and long-term simulations. However, as
indicated by Li et al. (2017), it is more difﬁcult to make a
long-term prediction because long-term prediction tasks
require more pertinent historical input data than a short-
term prediction. Hence, exploration of the capability of
different DL approaches for medium- and long-term water
quality predictions is recommended. The hybrid CNN–

123

Stochastic Environmental Research and Risk Assessment

Fig. 10 Spider plot of the
models’ performances in
predicting DO and Chl-a using
the developed models in the
testing period; a relative root
mean square error (RRMSE; %)
and b Nash–Sutcliffe model
efﬁciency coefﬁcient (ENS)

LSTM model outperformed the standalone individual
LSTM and CNN models, as well as the ML models. This is
because the LSTM is capable of
learning long-term
dependency and CNN can extract time-invariant features.
Thus, their combination improved the overall accuracy. In
conventional ML models, most of the features need to be
classiﬁed by a domain expert to reduce the complexity of
the data and make patterns more visible to the learning
algorithms. In contrast, the DL models learn high-level
features from data in an incremental manner, which
removes the need for domain expertise and feature
extraction. The results established that the low-cost model
developed in this study, which used easily measured water
variables, can be an alternative to monitor water quality in
Small Prespa Lake. The proposed model can also be used
to rebuild past Chl-a and DO conditions using these same
easily measured variables.

Future studies should explore the ability of DL models
to simulate water quality parameters over medium- and
long-term periods. Preprocessing methods, e.g., wavelet
decomposition combined with DL models, could also be
explored to predict water quality. Using decomposition

methods, some of the noise of the data is removed, and the
accuracy of
the predictive model can sometimes be
improved. The methodology used in this study could also
be applied to predict other hydrological variables. Fur-
thermore, other DL models, e.g., stacked auto-encoder,
restricted Boltzmann machine deep reinforcement learning,
and generative adversarial network, could also be inter-
esting to explore for water quality prediction.

4 Conclusions

This research used four easily measured water quality
variables, i.e., EC, pH, ORP, and water temperature, to
construct DL (i.e., LSTM, CNN, and hybrid CNN–LSTM
for the ﬁrst time in the ﬁeld of water quality modeling) and
traditional ML (i.e., SVR and DT) models to predict DO
and Chl-a concentrations in Small Prespa Lake, Greece.
Water quality data were collected at 15-min intervals from
June 1, 2012 to May 31, 2013. The input dataset was
transformed into a supervised frame and then split into
training (70%) and testing (30%) datasets. The models

123

Stochastic Environmental Research and Risk Assessment

123

Stochastic Environmental Research and Risk Assessment

b Fig. 11 The frequency plots of the absolute prediction error produced
by the models in the testing period for DO and Chl-a predictions

were trained using the optimal hyper-parameters for each
model. The testing period data were used to evaluate the
performance of the models using statistical criteria: r,
RMSE, MAE and their normalized equivalents expressed as
a percentage (RRMSE, RMAE), along with ENS and WI.

Although the LSTM model outperformed the CNN
model in predicting DO concentrations, their performances
were similar for Chl-a prediction. The performance eval-
uation of the hybrid CNN–LSTM model, which has the
strengths of both standalone DL models, demonstrated that
it decreased the RMAE for DO prediction by 0.24% and
1.45% in the testing period compared to the LSTM and
CNN models, respectively. For Chl-a prediction, the hybrid
CNN–LSTM model decreased the RMAE by 6.41% and
6.48% in the testing period compared to the LSTM and
CNN models, respectively. The LSTM models were much
better at predicting higher levels of DO and Chl-a con-
centrations in the testing period, while the CNN model was
better at predicting the lower levels of these variables. By
integrating these models, the hybrid CNN–LSTM model
successfully captured both low and high levels of the water
quality variables, particularly for the DO concentrations.

Acknowledgements Data acquisition was performed in the context
of
the ‘‘Vodafone World of Difference’’ program which is a chari-
table volunteer initiative delivered by Vodafone Foundations and
funded by Vodafone Greece. The project was supported by the
Society for the Protection of Prespa (SPP) as the host organization in
liaison with Prespa Municipality. The authors wish to express their
acknowledgment
to the above for their fruitful contribution and
overall support. The authors are also thankful to Evangelos Tziritis
for providing the data. Funding for this research was provided by an
NSERC Discovery Grant held by Jan Adamowski.

References

Affonso C, Rossi ALD, Vieira FHA, de Leon Ferreira ACP (2017)
Deep learning for biological image classiﬁcation. Expert Syst
Appl 85:114–122

Aghel B, Rezaei A, Mohadesi M (2019) Modeling and prediction of
water quality parameters using a hybrid particle swarm opti-
mization–neural fuzzy approach. Int J Environ Sci Technol
16(8):4823–4832

Alizadeh MJ, Kavianpour MR (2015) Development of wavelet-ANN
models to predict water quality parameters in Hilo Bay, Paciﬁc
Ocean. Mar Pollut Bull 98(1–2):171–178

Asadollahfardi G, Zangooi H, Asadi M, Tayebi Jebeli M, Meshkat-
Dini M, Roohani N (2018) Comparison of Box-Jenkins time
series and ANN in predicting total dissolved solid at
the
Za¯yande´-Ru¯d River,
J Water Supply Res Technol
67(7):673–684

Iran.

Babaei M, Moeini R, Ehsanzadeh E (2019) Artiﬁcial neural network
and support vector machine models for inﬂow prediction of dam

reservoir (case study: Zayandehroud dam reservoir). Water
Resour Manag 33(6):2203–2218

Bacal MCJO, Hwang S, Guevarra-Segura I

(2019) Predictive
lithologic mapping of South Korea from geochemical data using
decision trees. J Geochem Explor 205:106326. https://doi.org/10.
1016/j.gexplo.2019.06.008

Barzegar R, Adamowski J, Moghaddam AA (2016a) Application of
wavelet-artiﬁcial intelligence hybrid models for water quality
prediction: a case study in Aji-Chay River, Iran. Stoch Environ
Res Risk Assess 30(7):1797–1819

Barzegar R, Moghaddam AA, Tziritis E (2016b) Assessing the
hydrogeochemistry and water quality of the Aji-Chay River,
northwest of Iran. Environ Earth Sci 75(23):1486

Barzegar R, Moghaddam AA, Adamowski J, Fijani E (2017)
Comparison of machine learning models for predicting ﬂuoride
contamination in groundwater. Stoch Environ Res Risk Assess
31(10):2705–2718

Barzegar R, Moghaddam AA, Adamowski J, Ozga-Zielinski B (2018)
Multi-step water quality forecasting using a boosting ensemble
multi-wavelet extreme learning machine model. Stoch Environ
Res Risk Assess 32(3):799–813

Barzegar R, Ghasri M, Qi Z, Quilty J, Adamowski J (2019) Using
ice
bootstrap ELM and LSSVM models to estimate river
thickness in the Mackenzie River Basin in the Northwest
Territories, Canada. J Hydrol 577:123903. https://doi.org/10.
1016/j.jhydrol.2019.06.075

Borovykh A, Bohte S, Oosterlee CW (2017) Conditional time series
forecasting with convolutional neural networks. arXiv preprint
arXiv:1703.04691

Bui DT, Hoang ND, Alvarez FM, Ngo PTT, Hoa PV, Pham TD,
Samui P, Costache R (2019) A novel deep learning neural
network approach for predicting ﬂash ﬂood susceptibility: a case
study at a high frequency tropical storm area. Sci Total Environ.
https://doi.org/10.1016/j.scitotenv.2019.134413

Bui DT, Tsangaratos P, Nguyen VT, Liem NV, Trinh PT (2020)
Comparing the prediction performance of a Deep Learning
Neural Network model with conventional machine learning
susceptibility assessment. CATENA
models
188:104426. https://doi.org/10.1016/j.catena.2019.104426
Cai M, Pipattanasomporn M, Rahman S (2019) Day-ahead building-
level load forecasts using deep learning vs. traditional time-
series techniques. Appl Energy 236:1078–1088

in landslide

Chen Q, Mynett AE (2003) Integration of data mining techniques and
heuristic knowledge in fuzzy logic modelling of eutrophication
in Taihu Lake. Ecol Model 162(1–2):55–67

Chen J, Zeng GQ, Zhou W, Du W, Lu KD (2018) Wind speed
forecasting using nonlinear-learning ensemble of deep learning
time series prediction and extremal optimization. Energy Con-
vers Manag 165:681–695

Chen Y, Cheng Y, Yang L, Liu Y, Li D (2019) Prediction model of
ammonia-nitrogen in pond aquaculture water based on improved
multi-variable deep belief network. Nongye Gongcheng Xuebao/
Trans Chin Soc Agric Eng 35(7):195–202. https://doi.org/10.
11975/j.issn.1002-6819.2019.07.024

Cho H, Choi UJ, Park H (2018) Deep learning application to time-
series prediction of daily chlorophyll-a concentration. WIT
Trans Ecol Environ 215:157–163

Choi J, Kim J, Won J, Min O (2019) Modelling chlorophyll-a
concentration using deep neural networks considering extreme
data imbalance and skewness. In: 21st International conference
on advanced communication technology (ICACT), Pyeong-
Chang Kwangwoon Do, Korea (South), pp 631–634. https://
doi.org/10.23919/icact.2019.8702027

Cortes C, Vapnik V (1995) Support-vector networks. Mach Learn

20(3):273–297

123

Cummins N, Baird A, Schuller BW (2018) Speech analysis for health:
current state-of-the-art and the increasing impact of deep
learning. Methods 151:41–54

Fan L, Zhang T, Zhao X, Wang H, Zheng M (2019) Deep topology
network: a framework based on feedback adjustment learning
rate for image classiﬁcation. Adv Eng Inf 42:100935

Fang W, Zhong B, Zhao N, Love PE, Luo H, Xue J, Xu S (2019) A
deep learning-based approach for mitigating falls from height
with computer vision: convolutional neural network. Adv Eng
Inf 39:170–177

Fayek HM, Lech M, Cavedon L (2017) Evaluating deep learning
architectures for Speech Emotion Recognition. Neural Netw
92:60–68

Fijani E, Barzegar R, Deo R, Tziritis E, Konstantinos S (2019) Design
and implementation of a hybrid model based on two-layer
decomposition method coupled with extreme learning machines
to support real-time environmental monitoring of water quality
parameters. Sci Total Environ 648:839–853

Ghorbani MA, Deo RC, Karimi V, Yaseen ZM, Terzi O (2018)
Implementation of a hybrid MLP-FFA model for water level
prediction of Lake Egirdir, Turkey. Stoch Environ Res Risk
Assess 32(6):1683–1697

Goz E, Yuceer M, Karadurmus E (2019) Total organic carbon
prediction with artiﬁcial intelligence techniques. In: Munoz SG,
Laird CD, Realff MJ (eds) Computer aided chemical engineer-
ing, vol 46. Elsevier, Amsterdam, pp 889–894

Gu Y, Lu W, Qin L, Li M, Shao Z (2019) Short-term prediction of
lane-level trafﬁc speeds: a fusion deep learning model. Transp
Res Part C Emerg Technol 106:1–16

Hochreiter S, Schmidhuber J (1997) Long short-term memory. Neural

Comput 9(8):1735–1780

Hollis GE, Stevenson AC (1997) The physical basis of the Lake Mikri
Prespa systems: geology, climate, hydrology and water quality.
In: Crivelli AJ, Catsadorakis G (eds) Lake Prespa, Northwestern
Greece. Springer, Dordrecht, pp 1–19

Hoseinzade E, Haratizadeh S (2019) CNNpred: CNN-based stock
market prediction using a diverse set of variables. Expert Syst
Appl 129:273–285

Huang M, Tian D, Liu H, Zhang C, Yi X, Cai J, Ruan J, Zhang T,
Kong S, Ying G (2018) A hybrid fuzzy wavelet neural network
model with self-adapted fuzzy-means clustering and genetic
algorithm for water quality prediction in rivers. Complexity.
https://doi.org/10.1155/2018/8241342

Huang H, Liang Z, Li B, Wang D, Hu Y, Li Y (2019) Combination of
multiple data-driven models for
long-term monthly runoff
predictions based on Bayesian model averaging. Water Resour
Manag 33:3321–3338

Jaloree S, Rajput A, Gour S (2014) Decision tree approach to build a

model for water quality. Bin J Data Min Netw 4:25–28

Khadr M (2017) Modeling of water quality parameters in Manzala
lake using adaptive neuro-fuzzy inference system and stochastic
models. In: Negm A, Bek M, Abdel-Fattah S (eds) Egyptian
coastal lakes and wetlands: part II. The handbook of environ-
mental chemistry, vol 72. Springer, Cham. https://doi.org/10.
1007/698_2017_110

Khosravi K, Mao L, Kisi O, Yaseen ZM, Shahid S (2018) Quantifying
hourly suspended sediment load using data mining models: case
study of a glacierized Andean catchment in Chile. J Hydrol
567:165–179

Kim TY, Cho SB (2018) Predicting the household power consump-
tion using CNN-LSTM hybrid networks.
International
conference on intelligent data engineering and automated
learning. Springer, Cham, pp 481–490

In:

Kim TY, Cho SB (2019) Predicting residential energy consumption

using CNN-LSTM neural networks. Energy 182:72–81

123

Stochastic Environmental Research and Risk Assessment

Kisi O, Parmar KS (2016) Application of least square support vector
machine and multivariate adaptive regression spline models in
J Hydrol
long term prediction of
534:104–112

river water pollution.

Kisi O, Azad A, Kashi H, Saeedian A, Hashemi SAA, Ghorbani S
(2019) Modeling groundwater quality parameters using hybrid
neuro-fuzzy methods. Water Resour Manag 33(2):847–861
Kratzert F, Klotz D, Brenner C, Schulz K, Herrnegger M (2018)
Rainfall–runoff modelling using long short-term memory
(LSTM) networks. Hydrol Earth Syst Sci 22(11):6005–6022
Krstic´ SS (2012) Environmental changes in lakes catchments as a
trigger for rapid eutrophication: a Prespa Lake case study. In:
Piacentini T, Miccadei E (eds) Studies on environmental and
applied geomorphology.
IntechOpen. https://doi.org/10.5772/
27246

Legates DR, McCabe GJ (1999) Evaluating the use of ‘‘goodness-of-
ﬁt’’ measures in hydrologic and hydroclimatic model validation.
Water Resour Res 35(1):233–241

Lei C, Deng J, Cao K, Xiao Y, Ma L, Wang W, Ma T, Shu C (2019)
A comparison of random forest and support vector machine
approaches to predict coal spontaneous combustion in gob. Fuel
239:297–311

Li W, Yang M, Liang Z, Zhu Y, Mao W, Shi J, Chen Y (2013)
Assessment for surface water quality in Lake Taihu Tiaoxi River
Basin China based on support vector machine. Stoch Environ
Res Risk Assess 27(8):1861–1870

Li X, Peng L, Yao X, Cui S, Hu Y, You C, Chi T (2017) Long short-
term memory neural network for air pollutant concentration
predictions: Method development and evaluation. Environ pollut
231:997–1004

Li P, Abdel-Aty M, Yuan J (2020) Real-time crash risk prediction on
arterials based on LSTM-CNN. Accid Anal Prev 135:105371.
https://doi.org/10.1016/j.aap.2019.105371

Liu H, Mi X, Li Y, Duan Z, Xu Y (2019a) Smart wind speed deep
learning based multi-step forecasting model using singular
spectrum analysis, convolutional gated recurrent unit network
and support vector regression. Renew Energy 143:842–854
Liu P, Wang J, Sangaiah AK, Xie Y, Yin X (2019b) Analysis and
prediction of water quality using LSTM deep neural networks in
IoT environment. Sustainability (Switzerland) 11(7):2058.
https://doi.org/10.3390/su11072058

Liu Y, Wang H, Gu Y, Lv X (2019c) Image classiﬁcation toward lung
recognition by learning deep quality model. J Vis
cancer
Commun Image Represent 63:102570. https://doi.org/10.1016/
j.jvcir.2019.06.012

Moriasi DN, Arnold JG, Van Liew MW, Bingner RL, Harmel RD,
Veith TL (2007) Model evaluation guidelines for systematic
quantiﬁcation of accuracy in watershed simulations. Trans
ASABE 50(3):885–900

Najafzadeh M, Ghaemi A (2019) Prediction of

the ﬁve-day
biochemical oxygen demand and chemical oxygen demand in
natural streams using machine learning methods. Environ Monit
Assess 191(6):380

Noori R, Karbassi A, Farokhnia A, Dehghani M (2009) Predicting the
longitudinal dispersion coefﬁcient using support vector machine
and adaptive neuro-fuzzy inference system techniques. Environ
Eng Sci 26(10):1503–1510

Noori R, Karbassi AR, Moghaddamnia A, Han D, Zokaei-Ashtiani
MH, Farokhnia A, Gousheh MG (2011) Assessment of input
variables determination on the SVM model performance using
PCA, Gamma test, and forward selection techniques for monthly
stream ﬂow prediction. J Hydrol 401(3–4):177–189

Noori R, Safavi S, Shahrokni SAN (2013) A reduced-order adaptive
neuro-fuzzy inference system model as a software sensor for
rapid estimation of ﬁve-day biochemical oxygen demand.
J Hydrol 495:175–185

Stochastic Environmental Research and Risk Assessment

Noori R, Deng Z, Kiaghadi A, Kachoosangi FT (2015a) How reliable
are ANN, ANFIS, and SVM techniques for predicting longitu-
dinal dispersion coefﬁcient in natural rivers? J Hydraul Eng
142(1):04015039.
https://doi.org/10.1061/(ASCE)HY.1943-
7900.0001062

Noori R, Yeh HD, Abbasi M, Kachoosangi FT, Moazami S (2015b)
Uncertainty analysis of support vector machine for online
prediction of ﬁve-day biochemical oxygen demand. J Hydrol
527:833–843

Oelen A, van Aart CJ, De Boer V (2018) Measuring surface water
quality using a low-cost sensor kit within the context of rural
Africa. In: P-ICT4D@ WebSci

Panagiotopoulos K, Aufgebauer A, Scha¨bitz F, Wagner B (2013)
Vegetation and climate history of the Lake Prespa region since
the Lateglacial. Quat Int 293:157–169

Patceva S, Mitic V (2010) Chlorophyll a content as indicator of
eutrophication of Lake Prespa. BALWOIS 2010 — Ohrid,
Republic of Macedonia — 25, 29 May 2010, pp 1–5

Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel
O, Blondel M, Prettenhofer P, Weiss R, Dubourg V, Vanderplas
J (2011) Scikit-learn: machine learning in Python. J Mach Learn
Res 12:2825–2830

Pereira GC, Evsukoff A, Ebecken NF (2009) Fuzzy modelling of
chlorophyll production in a Brazilian upwelling system. Ecol
Model 220(12):1506–1512

Plappert M, Mandery C, Asfour T (2018) Learning a bidirectional
mapping between human whole-body motion and natural
language using deep recurrent neural networks. Rob Auton Syst
109:13–26
Quinlan JR (1986)
1(1):81–106

Induction of decision trees. Mach Learn

Shin HC, Lu L, Summers RM (2017) Natural language processing for
large-scale medical image analysis using deep learning. In: Zhou
SK, Greenspan H, Shen D (eds) Deep learning for medical image
analysis. Academic Press, Cambridge, pp 405–421

Sinshaw TA, Surbeck CQ, Yasarer H, Najjar Y (2019) Artiﬁcial
neural network for prediction of total nitrogen and phosphorus in
US lakes. J Environ Eng 145(6):04019032

Song YY, Ying LU (2015) Decision tree methods: applications for
prediction. Shanghai Arch Psychiatry

and

classiﬁcation
27(2):130

Song X, Zhang G, Liu F, Li D, Zhao Y, Yang J (2016) Modeling
spatio-temporal distribution of soil moisture by deep learning-
based cellular automata model. J Arid Land 8(5):734–748
Tao Y, Gao X, Hsu K, Sorooshian S, Ihler A (2016) A deep neural
network modeling framework to reduce bias in satellite precip-
itation products. J Hydrometeorol 17(3):931–945

Tziritis EP (2014) Environmental monitoring of Micro Prespa Lake
basin (Western Macedonia, Greece): hydrogeochemical charac-
teristics of water resources and quality trends. Environ Monit
Assess 186(7):4553–4568

Vapnik V (1995) The nature of statistical learning theory. Springer,

Berlin

Wang Y, Xu C, Zhang S, Yang L, Wang Z, Zhu Y, Yuan J (2019)
Development and evaluation of a deep learning approach for

modeling seasonality and trends in hand-foot-mouth disease
incidence in mainland China. Sci Rep 9(1):1–15

Willmott CJ (1981) On the validation of models. Phys Geogr

2:184–194

Wu Y, Chen J (2013) Investigating the effects of point source and
nonpoint source pollution on the water quality of the East River
(Dongjiang) in South China. Ecol Indic 32:294–304

Wu Q, Lin H (2019) Daily urban air quality index forecasting based
on variational mode decomposition, sample entropy and LSTM
neural network. Sustain Cities Soc 50:101657. https://doi.org/10.
1016/j.scs.2019.101657

Wu Y, Liu S (2012) Modeling of land use and reservoir effects on
nonpoint source pollution in a highly agricultural basin. J Environ
Monit 14(9):2350–2361

Xu Z, Cao Y, Kang Y (2019) Deep spatiotemporal residual early-late
fusion network for city region vehicle emission pollution
prediction. Neurocomputing 355:183–199

Yajima H, Derot J (2018) Application of the Random Forest model
for chlorophyll-a forecasts in fresh and brackish water bodies in
Japan, using multivariate long-term databases. J Hydroinform
20:206–220

Yang HF, Chen YPP (2019) Hybrid deep learning and empirical
mode decomposition model for time series applications. Expert
Syst Appl 120:128–138

Yaseen ZM, Deo RC, Hilal A, Abd AM, Bueno LC, Salcedo-Sanz S,
Nehdi ML (2018) Predicting compressive strength of lightweight
foamed concrete using extreme learning machine model. Adv
Eng Softw 115:112–125

Yi HS, Lee B, Park S, Kwak KC, An KG (2018) Prediction of short-
term algal bloom using the M5P model-tree and extreme
learning machine. Environ Eng Res 24(3):404–411

Yu PS, Yang TC, Chen SY, Kuo CM, Tseng HW (2017) Comparison
of random forests and support vector machine for real-time
radar-derived rainfall forecasting. J Hydrol 552:92–104

Yuan X, Chen C, Lei X, Yuan Y, Adnan RM (2018) Monthly runoff
forecasting based on LSTM–ALO model. Stoch Environ Res
Risk Assess 32(8):2199–2212

Zhang D, Lindholm G, Ratnaweera H (2018) Use long short-term
memory to enhance Internet of Things for combined sewer
overﬂow monitoring. J Hydrol 556:409–418

Zhang Y, Fitch P, Thorburn P, Vilas MDLP (2019) Applying multi-
layer artiﬁcial neural network and mutual information to the
prediction of trends in dissolved oxygen. Front Environ Sci 7:46
Zhu S, Hadzima-Nyarko M, Gao A, Wang F, Wu J, Wu S (2019) Two
hybrid data-driven models for modeling water-air temperature
relationship
Res
26(12):12622–12630

Environ

rivers.

Pollut

Sci

in

Zuo R, Xiong Y, Wang J, Carranza EJM (2019) Deep learning and its
application in geochemical mapping. Earth Sci Rev 192:1–14.
https://doi.org/10.1016/j.earscirev.2019.02.023

Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.

123

