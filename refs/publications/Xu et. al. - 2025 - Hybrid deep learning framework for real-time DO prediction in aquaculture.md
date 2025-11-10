www.nature.com/scientificreports

Hybrid deep learning framework
for real-time DO prediction in
aquaculture

Longqin Xu1,2,3, Wenjun Liu1,2,3, Cai Chengqing1,2,3, Tonglai Liu1,2,3, Xuekai Gao1,2,3,
Ferdous Sohel4, Murtaza Hasan5, Mansour Ghorbanpour6, Shahbaz Gul Hassan1,2,3 &
Shuangyin Liu1,2,3

Dissolved oxygen (DO) is a vital parameter in regulating water quality and sustaining the health of
aquatic organisms in aquaculture environments. Therefore, estimation and control of DO levels are
essential in aquaculture operations. However, traditional chemical and photochemical approaches
are limited by inaccuracies, environmental interferences, time consumption, and the inability
to provide real-time data. Recently, artificial intelligence techniques have been studied for DO
estimation. However, off-the-shelf models, such as Random Forest (RF) and Back Propagation (BP)
have demonstrated poor performance due to intricate interactions in aquatic ecosystems, which
leads to complex data patterns. This study proposes a water quality estimation model by combining
a convolutional neural network (CNN), self-attention (SA), and bidirectional simple recurrent unit
(BiSRU). One-dimensional convolution in CNN was employed to extract effective features and input
into the SA mechanism to assign weights and emphasise crucial information. The model’s accuracy
is improved by incorporating BiSRU. This model evaluated the DO levels of the intensive aquaculture
base in Nansha, Guangzhou City, Guangdong Province, China. The proposed CNN-SA-BiSRU achieved
MSE, MAE, RMSE, and R2 of 0.0022, 0.0341, 0.0471, and 0.9765, respectively. The results of the
experiments showed that the proposed model had a high level of accuracy in estimating the outcomes
with minimal fluctuations in estimation errors. Moreover, accuracy for short-term prediction was
significantly improved, surpassing the performance of existing methods. The highly accurate results
indicate the potential of the proposed methodology for DO-level monitoring in aquaculture and its
usage in the fishery industry.

Keywords  Non-linear, CNN, BiSRU, Self-Attention mechanism

Water is a vital resource for all living things, an irreplaceable and essential asset that provides a habitat for a
complex  array  of  aquatic  organisms1,2.  Of  the  various  properties  of  water,  water  quality,  in  particular,  has  a
significant impact on the aquatic environments3,4. Maintaining and improving the quality of water in intensive
aquaculture is beneficial to the health of aquatic organisms and it brings positive economic results5,6. Among the
water quality indicators, the DO is a critical determinant of the aquaculture environments7. Too high levels of
DO can cause bubonic disease in aquatic products.

Conversely, too low levels of DO can cause slow physiological metabolism, respiratory distress, and death
of  aquatic  products8.  These  results  show  that  the  losses  associated  with  poor  water  quality  management  can
be significant for marine organisms9. This situation has prompted a search for methods to accurately estimate
the DO levels in water10. Accurate monitoring and regulation of dissolved water can reduce disruptions in the
physiological mechanisms of aquatic products, improve the stability of marine habitats, and promote increased
aquatic production11.

1College of Artificial Intelligence, Zhongkai University of Agriculture and Engineering, Guangzhou 510225, China.
2Smart Agriculture Engineering Technology Research Center of Guangdong Higher Education Institutes, Zhongkai
University of Agriculture and Engineering, Guangzhou 510225, China. 3Guangdong Provincial Agricultural Products
Safety  Big  Data  Engineering Technology  Research  Center,  Zhongkai  University  of Agriculture  and  Engineering,
Guangzhou 510225, China. 4School of Information Technology, Murdoch University, Murdoch, Australia. 5Faculty of
Chemical and Biological Science, Department of Biotechnology, The Islamia University of Bahawalpur, Bahawalpur
63100, Pakistan. 6Department of Medicinal Plants, Faculty of Agriculture and Natural Resources, Arak University,
Arak 38156-8-8349, Iran. email: m-ghorbanpour@araku.ac.ir; mhasan387@zhku.edu.cn

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

1

OPENwww.nature.com/scientificreports/

DO refers to the presence of oxygen in water, which is crucial for the respiration of aquatic animals. Optimal
DO  levels  support  growth,  health,  disease  resistance,  and  efficient  feed  conversion  in  aquatic  species.  The
industry practices regular monitoring to maintain these levels using advanced equipment like oxygen probes12.
Aeration mechanical and natural techniques enhance oxygen levels13. Moreover, managing stocking densities,
controlling algal blooms, conducting water exchanges, and using supplemental oxygen are essential strategies in
DO management14. However, these practices come with challenges such as high costs, energy dependence, and
potential environmental impacts, especially from over-aeration.

Several studies have been conducted on estimating DO concentration. Liu proposed a method that integrates
grey matter correlation studies, wavelet transformations, the particle swarm algorithm, and the gravity search
method15. The study demonstrated that the model was suitable for analysing DO variations and concentration
trends. However, integrating these varied methods requires rigorous calibration and validation to ensure high
predictive  accuracy.  Implementing  this  comprehensive  strategy  demands  expertise  across  multiple  fields,
including neuroscience, signal processing, and optimization.

Moreover, the complexity introduced by combining multiple algorithms raises concerns about overfitting,
potentially reducing the model’s applicability to new data sets. Nallakaruppan used machine learning techniques
based  on  quantile  regression  forests16.  However,  Quantile  regression  forests  (QRF)  for  DO  prediction  have
limitations.  They  can  struggle  with  highly  dimensional  data  and  lack  the  interpretability  of  linear  models.
While  QRF  captures  complex  relationships,  overfitting  becomes  a  concern,  especially  with  limited  training
data. Additionally, their computational demand can be higher than a simpler regression model. Ta proposed a
simplified reverse-comprehension CNN model for DO prediction, which showed improved prediction stability
and convergence speed17.

In contrast, it has limitations in handling non-linear relationships due to its architecture. Its reliance on vast
amounts of labelled training data can be constraining. Furthermore, the model might overfit specific datasets,
diminishing its generalizability. Shi used a clustering-based soft plus extreme learning machine (CSELM) DO
estimation, demonstrating good accuracy in the practical prediction of DO18. But, its reliance on clustering can
cause sensitivity to initial data partitioning. ELM’s single-layer feedforward structure may not always capture
intricate patterns. Overfitting with complex datasets has risks, and model generalizability could be compromised.
Dissolved oxygen has complex, non-linear characteristics and is highly susceptible to various factors, such
as climate and facilities, as one of the essential elements of the water environment19. Dissolved oxygen exhibits
complex, non-linear characteristics. It is influenced by various factors, including climate and facilities, which
are  crucial  elements  of  the  water  environment.  Therefore,  the  potential  long-term  correlation  among  data  is
complex for dissolved oxygen prediction. RNNs support serial data, so the RNN output correlates with the initial
time step, reflecting sequence data trends20. Attention-based RNN is a sophisticated technique that dynamically
learns spatiotemporal relationships in multivariate time series. It can also extract long-term correlations from
the series data. Therefore, it has achieved better results in implementing single-step and short-term forecasting
of geo-sensitive time series21,22. With advancements in research, traditional RNN algorithms, including LSTM
and GRU, are commonly used as deformation models in predicting dissolved oxygen content in time series data,
resulting in improved outcomes.

Shi implemented a spatiotemporal model for predicting dissolved oxygen using LSTM in both spatial and
temporal  directions,  spanning  both  temporal  and  spatial  dimensions23.  Cao  integrated  GRU  and  attention
mechanism to developed a DO prediction model by monitoring the pond at an intermediate point, where reference
is the central point, using a 3D coordinate system24. The GBRT algorithm was improved using a random search
(RS) technique, covering the pond rate rather than a specific pond area. Based on the experimental findings, it
seems that the model may improve the precision of 3-dimensional predictions of dissolved oxygen in ponds and
meet the demand for various water products at multiple depths. Egbueri developed a model for characterising
water quality across short and long periods using a CNN and a GRU25. The model also includes an attention
mechanism to control the relative importance of individual neurons. A typical small contaminated watershed
in central China was studied. The results showed that the model significantly increased forecast efficiency and
provided a sufficient foundation for decision-making regarding the integrated water quality management of the
watershed. Boulila combined CNN and LSTM to propose an urban sprawl prediction model, which provided
better  accuracy  predictions  than  the  comparison  model26.  Jiang  presented  a  model  for  indoor  temperature
prediction  that  combines  the  attention  mechanism  and  LSTM27. The  model  employs  TPE  Bayes  to  optimize
the hyperparameters, which helps to determine the different parameter values of the deep model. The testing
findings indicated that the suggested model accurately predicted interior temperatures more rapidly than widely
used time series prediction algorithms.

The RNN variant models that utilise the attention mechanism have found widespread application in various
fields.  Nonetheless,  the  GRU  and  LSTM  models  continue  to  experience  certain  time-dependent  limitations.
Specifically, computation for each step is halted until the preliminary step has been entirely executed. Bidirectional
networks are frequently incorporated into RNN variants that use attention mechanisms to enhance prediction
model accuracy and capture dependencies in data28. One approach is constructing bidirectional networks that
capture  future  moments29,30.  By  introducing  a  bidirectional  structure,  Ling  transformed  the  simple  recursive
unit (SRU) into a bi-directional SRU (BiSRU) model31. This modification dramatically enhances parallelism and
offers several benefits, including a straightforward structure, fast convergence, and robust stability. As a result,
the  BiSRU  model  presents  a  promising  solution  to  the  issues  previously  discussed.  Liu  used  a  deep  stacked
simple recursive unit (BI-S-SRU) learning network to develop a prediction model, which increased accuracy
and  decreased  time  complexity32.  Through  experimental  studies,  he  confirmed  this  model’s  effectiveness  in
enhancing the accuracy of predictions while reducing time complexity. The bidirectional simple recursive unit
(BiSRU) model is characterised by a highly parallel bidirectional network structure, which has been shown to
enhance prediction accuracy and efficiency. However, few studies have explored the use of this model DO level

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

2

www.nature.com/scientificreports/

prediction in intensively farmed water quality, making this study particularly significant in its contribution to
this under-researched area.

Previous research has revealed that accurately predicting dissolved oxygen levels in intensively farmed water
quality parameters using traditional models remains challenging, with low accuracy and high precision reported.
In response to this challenge, an integrated (CNN-SA-BiSRU) model is proposed to improve the accuracy of
predictions. Firstly, CNN is used for data feature extraction to reduce data redundancy and minimise model
complexity. Secondly, the feature of the extract is weighted by a self-attention mechanism to highlight important
information. The data are then passed into the BiSRU model to fully seize the global information of the temporal
data context and achieve the optimal solution.

This study developed a combined prediction model that integrates a convolutional neural network (CNN),
the self-attentive mechanism (SA), and a bidirectional simple recursive unit (BiSRU) to forecast dissolved oxygen
levels in intensively farmed water quality parameters. After comparing this model’s performance to other models,
it was shown to provide more precise forecasts of future trends in dissolved oxygen changes in intensively farmed
water quality metrics. The proposed model also demonstrated a favourable effect in predicting dissolved oxygen
content. The main contribution of this study is:

  i.  Constructing data sets using environmental data collected by IoT environmental monitoring systems in-
stalled at intensive aquaculture bases, as well as normalising the data sets with data set segmentation, miss-
ing value processing, outlier processing, and time window segmentation.

 ii.  Using CNN one-dimensional convolution to extract features from different environmental parameters, the
extracted local feature combinations are abstracted into high-level feature values, effectively reducing data
redundancy and complexity and highlighting important relevant information in the data.

 iii.  BiSRU is used to capture past and future global context information and is combined and integrated with

self-attention mechanisms to improve the prediction accuracy of BiSRU significantly.

 iv.  This study conducted a comparison test with the established models, and the tested results showed that the
proposed model effectively integrates the advantages of each component, making the integrated model have
efficient performance. The model can accurately predict the future trend of DO in intensive aquaculture
and provides an effective technical tool for predicting DO content in intensive aquaculture water quality
parameters.

Materials and methods
Experimental configuration and area
Python 3.8 (64-bit) was used as a programming language, and Anaconda3 as the testing software. Computer
specifications include an 11th-generation Intel (R) platform with 16 GB of RAM, 2.3 GHz CPU frequency, and
a Windows 10 (64-bit) operating system.

This  study  selected  an  experimental  aquaculture  facility  in  Haizhu  District,  Guangzhou  City,  Guangdong
Province,  China,  as  the  testing  site  for  collecting  dissolved  oxygen,  pH,  and  conductivity  data.  These
measurements were obtained using an Internet of Things (IoT)-based water quality monitoring system depicted
in Fig. 1. The IoT sensors can collect data through GPRS, 4G, and other technologies to upload to the cloud.
Eventually, the data saved in the database can be accessed by the users. The water quality monitoring system

Fig. 1.  IoT-based water quality monitoring.

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

3

www.nature.com/scientificreports/

Fig. 2.  Map of water quality monitoring pools.

Time

Dissolved oxygen content (mg/L) Conductivity (S/m) pH

2022-02-18 00:00:02

2022-02-18 00:10:02

2022-02-18 00:20:02

…

2022-03-13 23:40:02

2022-03-13 23:50:02

9.9

9.9

9.9

…

8.0

8.0

31.8

31.8

31.5

…

34.7

33.4

7.8

7.9

7.9

…

7.3

7.3

Table 1.  Raw data on intensive aquaculture water quality metrics.

has three layers: perceptual, transport, and application. The perceptual layer is the location of the IoT sensors.
As shown in Fig. 2, the image of the water quality monitoring pool shows that the sensors located in different
locations can effectively collect water quality data in real-time. The transport layer is where the collected data is
transmitted to the cloud through a series of technical gateways that transport the data. The application layer is
where the users can access the data stored in the database by the app.

Methodologies
This  study’s  IoT-based  water  quality  monitoring  system  gathered  data  from  sensors  installed  within  the  fish
pond, with readings taken every ten minutes and stored on a server, as shown in Figs. 1 and 2. The monitoring
system enabled real-time visualisation of data on a terminal. Specifically, dissolved oxygen, pH, and conductivity
were collected during the experiment. Table 1 presents the data on the selected water-quality parameters for
intensively farmed aquaculture.

Data capturing
This study used a sample data set of 3 environmental factors, comprising 3500 entries. Of these, 2790 entries were
designated for training, while 698 were used for testing. The data pertained specifically to intensive aquaculture
water quality parameters known to be non-linear and non-stationary. Variation curves are shown in Fig. 3.

As  shown  in  Fig.  3,  the  highest  value  of  dissolved  oxygen  in  the  source  data  was  as  high  as  11.5  (mg/L),
and  the  lowest  value  was  as  low  as  8.2  (mg/L).  Seasonal  factors  and  biological  activities  influence  the  range
of  variations  in  the  data.  From  mid-February  to  mid-March,  warmer  temperatures  increased  fish  activity  in
the  water  column,  which  triggered  an  acceleration  of  respiration  and,  thus,  a  significant  increase  in  oxygen
consumption. Therefore, the decrease in DO levels can be reasonably attributed to a combination of seasonal
variations and biological activity. An increase in temperature is positively correlated with increased metabolic
activity  of  cultured  organisms,  leading  to  increased  release  of  carbon  dioxide.  In  the  water  column,  carbon
dioxide reacts with water to form carbonic acid, which leads to a gradual decrease in the pH of the water column.

Data processing
In the data collection process, the sensor equipment is prone to erosion due to year-round use and immersion
in water, and transmission over longer distances can easily lead to the loss of water quality data, thus causing
the problems of inaccurate sensor accuracy and abnormal water quality data. Since the data in this study was
collected by relying on the sensors in the fishponds in the intensive aquaculture bases, it is necessary to pre-
process the data to obtain more accurate water body data and ensure that the subsequent prediction process will
be carried out smoothly.

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

4

www.nature.com/scientificreports/

Fig. 3.  Graph of raw data variation.

 i.  Outlier handling:

In this study, the data are first detected for missing values, and outliers are processed when it is determined that
there are no missing values. The study uses the mean smoothing method to deal with data outliers, through
which the points with large jumps are better fused into the original data to obtain a high-quality dataset.

 ii.  Normalisation:

Secondly, due to the existence of data with large numerical differences in the original data, if the original data
are directly input into the model for prediction, it is easy to make the model prediction effect poor. Therefore, to
reduce the impact of different data scales and magnitudes, this study uses the normalisation method to scale the
data, scales all the data to be between [0,1], and fits them. The calculation formula is as follows:

x′ = x

xmin

xmin

−
xmax−

(1)

In  this  example,  let  x  represent  the  initial  environmental  parameter  values  in  the  water  quality  of  intensive
aquaculture, xmin is the lowest record of these environmental parameter values, xmax is the highest record, and x’
represents the normalised environmental parameter values of intensive aquaculture.

The hybrid DO Estimation model based on CNN-SA-BiSRU
CNN layers
Convolutional neural networks (CNNs) consist of an input layer, convolutional layers, and an output layer and
have been widely applied in various field33–36. In this study, CNN’s input layer takes raw time series data. The
convolutional layer has 0 kernel-size, 0 padding, and a stride of 1. The primary purpose of the one-dimensional
convolutional layers is to compress and cleanse the data, add low-level features, and extract them efficiently37as
shown in the following Eq.

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

yi = tanh

g

s=1

ξ sxi

−

s+g + τ

(∑

)

(2)

5

www.nature.com/scientificreports/

Here,  the  variable  xi  represents  the  original  time  series  input  data,  ξ
convolution kernels, and the bias value is τ.

s  is  the  weight  matrix,  and  g  denotes

Self-attention mechanism
A variation of the attention mechanism that emphasizes essential information by querying the data itself, thereby
reducing its dependency on external information, is known as the self-attention (SA) mechanism38. It captures
the intrinsic relationship between data or features better than other attention mechanisms, such as static and
global attention mechanisms. The self-attentive mechanism is formulated as follows.

hv = Di

Tu = Di

ς = Di

ξ hv

ξ Tu
ξ ς

·

·

·

S = sof tmax

hvTuT
√Fr )

ς

(

(3)

(4)

(5)

(6)

where,  hv refers to “query”,  Tu represents “key”,  ς represents “value”. ӻ is a scaling factor for r dimension. S is
the sum of the weights, measured by multiplying the attention weights by the matrix  ς.

Bidirectional simple recurrent unit (BiSRU)
The BiSRU model takes the output of the original data as input, which has undergone feature extraction by CNN
and self-attentive mechanisms. It contains two SRU models linked to the same output layer but run in opposing
directions. Each input sequence point may be understood in the larger context provided by this design. Unlike
other types of bidirectional stacked neural networks, BiSRU’s constituent model SRU is designed to tackle the
issue of time step dependence on the previous time step by achieving parallel computing while retaining control
over the information39.

The bidirectional SRU model consists of two opposite SRU networks stacked on each other. The output of
each time step is obtained by concatenating the forward and backward outputs. Each time step can be expressed
in Eq. (7). The two-way SRU model structure is shown in Fig. 4.

Ht =

−→ht, ←−ht

[

]

(7)

The hybrid model based on CNN-SA-BiSRU
The proposed study proposes a combined DO prediction based on CNN, SA, and BISRU in intensive aquaculture.
The  CNN  extract  low-level  and  meaningful  features  from  raw  data.  The  BiSRU  offers  a  straightforward  and
consistent approach to grasping the overarching traits of time series data. By integrating CNN, SA, and BiSRU
techniques, the model’s prediction precision and efficiency are significantly enhanced. Figure 5 depicts the whole
approach and procedure of the proposed model, which entails the following actions.

Fig. 4.  Structure of the BiSRU model.

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

6

www.nature.com/scientificreports/

Fig. 5.  Framework for predicting dissolved oxygen (DO) levels using time-series data. It involves
preprocessing (handling missing values, outliers, and normalisation), feature extraction through convolutional
layers, and temporal modelling with a self-attention bidirectional SRU (SA-BiSRU) network, followed by a fully
connected layer for final prediction.

Step 1: Using an IoT-based water quality monitoring system, the collected data was pre-processed and split

into training and test sets to collect real-time data of intensively farmed water quality metrics.

Step 2: CNN one-dimensional convolution extracts the compelling features of DO, eliminating redundant

data and reducing computational complexity.

Step 3: Using the self-attention mechanism, the hidden layer weights are redistributed, by ignoring unessential

information, the focus is highlighted, and the efficiency of the model is further improved.

Step  4:  Input  the  data  obtained  in  the  process  of  step  3  into  the  BiSRU  model,  fully  consider  the  global
contextual  information,  effectively  improve  the  model  prediction  accuracy,  and  apply  the  CNN-SA-BiSRU
combined prediction model to estimate DO in intensive aquaculture.

Simulation results and discussion
Performance criteria
During  the  experiment,  several  models  were  used  to  predict  the  outcomes  of  the  data  set.  Several  standard
indices were used to assess the accuracy of these models’ predictions and facilitate comparisons between them.
These included mean absolute error (MAE), MSE, RMSE, and R2. Using these indexes allowed for a quantitative
assessment of the accuracy and effectiveness of the predictions generated by each model in operation. They are
defined as follows.

ERM SE =

1
N

(cid:31)

EM SE =

EM AE =

1
N

1
N

(cid:30)

(cid:31)

N
i=1

y

(cid:29)
N
i=1(yi

−

−

2

yi

(cid:26)

(cid:28)
yi)2
(cid:27)

N
i=1 |

yi

R2 = 1

−

(cid:31)
N
i=1(yi

(cid:31)

N
i=1

yi

−

−

(cid:31)

(cid:29)

|

yi
(cid:30)
−
yi)2
(cid:30)
2

−y i
(cid:30)

(cid:28)

(8)

(9)

(10)

(11)

Simulation results and analysis
All models were trained on the same time series data to predict future dissolved oxygen levels. Figures 6 and
7 show the DO level estimation results by the models. It shows that all models could estimate the data trend
with reasonable accuracy. An analysis of both Figs. 6 and 7 reveals that the combined models outperformed the
individual models, with the proposed CNN-SA-BiSRU producing the best results (referred to as the zoomed in-
set). Single models, e.g., GRU and SVR models exhibited high volatility and the lease agreement with the actual
curve.

Figure 6 illustrates that the fitted curve of the combined CNN-BiSRU model demonstrated a higher degree
of agreement and fit than the fitted curve of the BiSRU single model and was generally closer to the actual curve.
CNN feature extraction reduced duplicate and less predictive characteristics from time series data.

Figure 8 shows violin plots for all predictive models. The violin plots show the data distribution and allow
comparison of multiple groups. The white dot in the middle of the violin plot indicates the median and the width
indicates the density of the data. From the shape of each violin and the position of the median in Fig. 8, it can be
seen that the median of all the prediction models moves up and down less. The models are more symmetrical,
which  indicates  that  the  predicted  values  are  concentrated.  The  model  proposed  in  this  study  has  the  most

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

7

www.nature.com/scientificreports/

Fig. 6.  Comparison of the results of all comparative models with respect to the ground truth data.

Fig. 7.  Radar diagram showcasing assessment metrics of various prediction models.

consistent shape with the original data, indicating that the model has the best prediction performance and can
have good prediction results on the data distribution.

The CNN-SA-BiSRU model is closest to the original data and has the best fit. Figure 9 shows the ablation
performance of the proposed model. If it is a single BiSRU model, it can only achieve parallel operation, which
is suitable for capturing the dependency of long data. However, BiSRU alone lacks the highlighting of important
information, so the model prediction results most deviate from the original data. The CNN-BiSRU model adds
CNN for feature extraction, which can add the advantages of CNN to the benefits of BiSRU to interpret the
data better. CNN feature extraction reduced duplicate and less predictive characteristics from time series data.
Therefore,  this  model’s  predictive  performance  increases.  The  Self-Attention  method  calibrated  the  weights
assigned to the data retrieved by the CNN features. The newly calibrated weight distributions were then entered
into BiSRU to determine which parameter combinations provide the optimal results for CNN-SA-BiSRU. The

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

8

www.nature.com/scientificreports/

Fig. 8.  Violin diagram of all prediction models.

Fig. 9.  An ablation study of the proposed model: Comparison of BiSRU, CNN-BiSRU and CNN-SA-BiSRU
curves.

Contrast model

CNN-SA-BiSRU

MAE↓ MSE↓ RMSE↓ R2↑
0.0341

0.0022

0.0471

0.9765

CNN-SA-BiLSTM 0.1508

0.0227

0.1508

0.8604

CNN-BiSRU

0.0447

0.0046

0.0681

0.9560

CNN

BiSRU

LSTM

GRU

SVR

0.0595

0.0078

0.0880

0.9061

0.0611

0.0068

0.0822

0.9185

0.0553

0.0077

0.0876

0.9012

0.0963

0.0113

0.1062

0.9021

0.0923

0.0173

0.1314

0.8217

Table 2.  Experimental results of different DO Estimation models.

findings  of  the  experiments  revealed  that  the  model  had  an  excellent  generalisation  capacity  in  terms  of  its
ability  to  forecast  water  quality  metrics  in  water  bodies  that  were  extensively  farmed.The  CNN-SA-BiSRU
model combines the advantages of the three modules for efficient feature extraction and highlighting of crucial
information for long data; therefore, this model can have the best fitting effect even during peaks and troughs.

Table 2 shows the quantitative results of all the prediction models. Dissolved oxygen concentration in water
quality parameters for intensive aquaculture is predicted to have the best results using the combined CNN-SA-
BiSRU prediction model suggested in this research. The MSE, MAE, RMSE, and R2 were 0.0022, 0.0341, 0.0471,

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

9

www.nature.com/scientificreports/

and 0.9765, respectively. For individual models, the root mean square error of BiSRU is 0.0822, which is 0.58%,
0.54%, 2.4%, and 4.92%, smaller than CNN, LSTM, GRU, and SVR, respectively.

In this study, a comparison was made between the CNN-BiSRU and BiSRU models. The evaluation metrics
were mean MSE, MAE, RMSE, and R2. The CNN-BiSRU model had a lower MAE, MSE, and RMSE by 1.64%,
0.22%,  and  1.41%,  respectively,  and  a  higher  R2  by  3.75%  compared  to  the  BiSRU  model.  The  enhancement
can  be  credited  to  the  BiSRU  model  receiving  the  raw  time  series  data  directly  without  undergoing  CNN-
based feature extraction. As a result, this led to data redundancy and increased computational effort, ultimately
affecting  the  model’s  accuracy.  By  incorporating  CNN  feature  extraction  before  inputting  the  data  into  the
BiSRU model, the original input data can be extracted for hierarchical information. This enhances the model’s
predictive performance and, thus, results in a better outcome.

The CNN-SA-BiSRU model had a lower MAE, MSE, and RMSE by 1.06%, 0.24%, and 2.1%, respectively, and
a higher R2 by 2.05% compared to the CNN-BiSRU model. This improvement can be attributed to the efficiency
of CNN’s one-dimensional convolution in extracting features from the original time series data. However, this
approach  is  limited  because  all  concealed  layer  units  have  the  same  weight,  which  increases  computational
complexity  and  reduces  the  model’s  efficacy.  The  Self-Attention  (SA)  method  assigns  varying  importance  to
elements in the hidden layer. This enhances the emphasis on essential data, minimises the attrition of records,
and  marginally  boosts  prediction  precision.  After  the  SA  mechanism  with  different  weights,  the  data  are
inputted into the BiSRU model. The performance is significantly improved compared to the model without the
SA mechanism. The prediction value has the slightest error with the measured value, resulting in the optimal
prediction effect.

The findings from the experiment above reveal that integrating CNN with the Self-Attention feature enhances
the accuracy of the BiSRU model. Through parameter refinement, this suggested approach excels in prediction
precision and adaptability.

The prediction framework introduced by Lap yielded promising results1. Nonetheless, our research utilised
a distinct dataset, opted for a unique feature selection approach, and employed a different prediction technique
tailored  to  our  issue.  Relative  to  Lap’s  model,  our  approach  in  this  study  demonstrates  superior  predictive
accuracy. Their model uses embedded feature selection, which automatically assesses the importance of features
without manually setting thresholds or using domain knowledge to help reduce component dimensionality40.
However, this feature selection method suffers from shortcomings. It is limited to the representational capability
to capture complex image or data features adequately.

In contrast, in our study the CNN feature extraction can learn features with more representational power
through  convolution  and  pooling  operations,  thus  achieving  a  certain  degree  of  accuracy  improvement41.  In
terms  of  prediction  model  selection,  this  reference  model  chooses  an  ML  (Machine  Learning)  based  model,
like  the  model  in  this  paper.  This  reference  prediction  model  determines  RF  (Random  Forest),  which  has
good explanatory and interpretable features, higher parallelism, and faster training42but due to its inability to
better prediction accuracy is low due to the failure to capture the dependencies between data. In contrast, the
prediction model BiSRU in this paper has better data dependency and can perform feature learning better, thus
further improving the prediction accuracy and robustness.

In addition, Fig. 10 shows the error profiles of the eight prediction models. Figure 10(a). GRU shows high
volatility in the error range, indicating that the model is unstable in its ability to generalise to samples and is
not sufficiently adaptive; Fig. 10(b). The LSTM error value fluctuation range is more stable than that of GRU.
However,  it  increases  in  some  regions,  indicating  that  the  model’s  performance  deteriorates  in  dealing  with
specific sequential data. Still, there is room for improvement; Fig. 10(c). CNN shows that the error rate fluctuates
sideways  with  the  increase  of  samples,  indicating  that  the  model  has  limitations  in  adapting  to  new  data;
Fig. 10(d). The overall trend of SVR error is relatively flat. However, there are spikes at specific points, which
is due to the model’s insensitivity to changes in the samples, which leads to inaccurate prediction of individual
samples; Fig. 10(e). BiSRU error volatility is lower than that of GRU and LSTM models, which indicates that the
model achieves a certain balance of stability and adaptability, and has a better prediction performance; Fig. 10(f).
CNN-BiSRU combines the advantages of CNN and BiSRU, but the error rate volatility suggests that there may
be room for adjustment in model fusion; Fig. 10(g). CNN-SA-BiLSTM shows that BiLSTM is more complex
in the structure of the prediction model, which reduces the prediction performance of the model, which is not
conducive to the prediction of the water quality parameter dissolved oxygen; Fig. 10(h). CNN-SA- BiSRU shows
that the inclusion of the self-attention mechanism is beneficial to improve the overall model performance, which
can better capture the long range dependencies and make the model reduce the error rate. These results indicate
that the CNN-SA-BiSRU model is the most effective in predicting dissolved oxygen content. Using this method,
researchers can obtain more accurate predictions of dissolved oxygen content for environmental monitoring and
water quality control.

The model combining CNNs, self-attention, and BiSRU emerges as a leading method for estimating dissolved
oxygen levels in water metrics crucial for high-density aquaculture.The research demonstrates that the suggested
model  has  calibrated  precision  and  effectiveness  and  can  successfully  capture  variations  in  dissolved  oxygen
concentration  in  intensively  farmed  water  systems.  As  a  result,  it  responds  to  real-world  demands  and  aids
in  making  crucial  decisions  about  the  quality  of  water  used  in  intensive  farming.  Compared  to  the  CNN,
BiSRU,  LSTM,  GRU,  and  SVR  models,  the  CNN-SA-BiSRU  model  outperforms  predicting  DO  of  intensive
agriculture. Based on these results, it is reasonable to assume that the suggested model might be used for various
environmental monitoring and prediction tasks.

Conclusions
This  paper  proposed  a  novel  dissolved  oxygen  prediction  model  (CNN-SA-BiSRU)  for  intensive  aquaculture
water quality parameters. The proposed model utilises one-dimensional convolution for feature extraction of

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

10

www.nature.com/scientificreports/

Fig. 10.  Comparison of different model errors.

raw  water  quality  data,  a  self-attentive  mechanism  to  adjust  the  hidden  layer  weights,  and  BiSRU  to  capture
global  contextual  information.  Our  findings  indicate  that  the  CNN-SA-BiSRU  method  achieves  better
prediction performance than CNN, BiSRU, LSTM, GRU, and SVR models based on various evaluation metrics,
including MAE, MSE, RMSE, and R2. The proposed model makes it a reliable tool for monitoring and regulating
dissolved oxygen water quality parameters in intensive farming. It considers complex time series data effectively,
providing robust support for environmental management and decision-making processes. Overall, this research
contributes to developing accurate and efficient dissolved oxygen prediction models, which can help improve
water quality monitoring and management in intensive farming.

Several limitations of our study need to be explored in depth in the future. First, feature engineering is a
crucial step in the data pre-processing process. However, our current feature engineering needs to be further
optimised  by  incorporating  domain  expertise  to  introduce  more  relevant  features  to  improve  the  model’s
predictive accuracy. Secondly, to obtain better model parameters, we plan to compare and study our algorithm
with cutting-edge algorithms such as the sailfish optimisation algorithm, coral reef optimisation algorithm, and
cockroach swarm optimisation algorithm in the future. This will help verify our algorithm’s performance and
effectiveness and provide more references for the tuning of model parameters. Finally, considering the need for
interpretability, we will use interpretable deep learning models. It is essential to interpret the prediction results of
the model in our research, which will provide a deeper understanding and reasonable explanation for our study
and more meaningful guidance for the application practice.

Data availability
The data will be availbile from corsponding author on request from corresponding authors.

Received: 7 January 2025; Accepted: 7 July 2025

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

11

www.nature.com/scientificreports/

References
  1.  Lap, B. Q. et al. Predicting water quality index (WQI) by feature selection and machine learning: A case study of an Kim Hai

irrigation system. Ecol. Inf. 74, 101991. https://doi.org/10.1016/j.ecoinf.2023.101991 (2023).

  2.  Parra, L., Sendra, S., Lloret, J. & Bosch, I. Development of a conductivity sensor for monitoring groundwater resources to optimize

water management in smart City environments. Sensors 15 (9), 20990–21015. https://doi.org/10.3390/s150920990 (2015).

  3.  Chou, J. S., Ho, C. C. & Hoang, H. S. Determining quality of water in reservoir using machine learning. Ecol. Inf. 44, 57–75.  h t t p s :

/ / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o i n f . 2 0 1 8 . 0 1 . 0 0 1     (2018).

  4.  Parra, L., Rocher, J., Escrivá, J. & Lloret, J. Design and development of low-cost smart turbidity sensor for water quality monitoring

in fish farms. Aquacult. Eng. 81, 10–18. https://doi.org/10.1016/j.aquaeng.2018.02.002 (2018).

  5.  Banerjee, A., Chakrabarty, M., Bandyopadhyay, G., Roy, P. K. & Ray, S. Forecasting environmental factors and zooplankton of
Bakreswar reservoir in India using time series model. Ecol. Inf. 60, 101157. https://doi.org/10.1016/j.ecoinf.2020.101157 (2020).
  6.  Garcia,  M.,  Sendra,  S.,  Lloret,  G.  &  Lloret,  J.  Monitoring  and  control  sensor  system  for  fish  feeding  in  marine  fish  farms.  IET

Commun. 5 (12), 1682–1690. https://doi.org/10.1049/iet-com.2010.0641 (2011).

  7.  Dehghani, R., Poudeh, T., Izadi, Z. & H., & Dissolved oxygen concentration predictions for running waters with hybrid machine

learning techniques. Model. Earth Syst. Environ. 1–15. https://doi.org/10.1007/s40808-021-01155-5 (2021).

  8.  Guo, J. et al. A hybrid model for the prediction of dissolved oxygen in Seabass farming. Comput. Electron. Agric. 198, 106971.

https://doi.org/10.1016/j.compag.2022.106971 (2022).

  9.  Mahammad, S., Islam, A. & Shit, P. K. Geospatial assessment of groundwater quality using entropy-based irrigation water quality
index and heavy metal pollution indices. Environ. Sci. Pollut. Res. 30 (55), 116498–116521.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 3 5 6 - 0 2 3 - 2 5
9 3 3 - 5     (2023).

 10.  Kruk, M. Prediction of environmental factors responsible for chlorophyll a-induced hypereutrophy using explainable machine

learning. Ecol. Inf. 75, 102005. https://doi.org/10.1016/j.ecoinf.2023.102005 (2023).

 11.  Li, D., Zhang, X., Yang, Y., Yang, H. & Liu, S. An interpretable hierarchical neural network insight for long-term water quality
forecast: A study in marine ranches of Eastern China. Ecol. Ind. 146, 109771. https://doi.org/10.1016/j.ecolind.2023.109771 (2023).
 12.  Entradas, T., Waldron, S. & Volk, M. The detection sensitivity of commonly used singlet oxygen probes in aqueous environments.

J. Photochem. Photobiol., B. 204, 111787. https://doi.org/10.1016/j.jphotobiol.2020.111787 (2020).

 13.  Åmand, L., Olsson, G. & Carlsson, B. Aeration control–a review. Water Sci. Technol. 67 (11), 2374–2398.  h t t p s : / / d o i . o r g / 1 0 . 2 1 6 6 /

w s t . 2 0 1 3 . 1 4 6     (2013).

 14.  Boyd, C. E. Dissolved oxygen management in aquaculture. Global Aquaculture Advocate. 7, 60–62 (2008).
 15.  Liu, H., Yang, R., Duan, Z. & Wu, H. A hybrid neural network model for marine dissolved oxygen concentrations time-series
forecasting based on multi-factor analysis and a multi-model ensemble. Engineering 7 (12), 1751–1765.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e
n g . 2 0 2 0 . 0 8 . 0 1 5     (2021).

 16.  Nallakaruppan, M. K. et al. Reliable water quality prediction and parametric analysis using explainable AI models. Sci. Rep. 14 (1),

7520. https://doi.org/10.1038/s41598-024-24373-3 (2024).

 17.  Ta, X. & Wei, Y. Research on a dissolved oxygen prediction method for recirculating aquaculture systems based on a Convolution

neural network. Comput. Electron. Agric. 145, 302–310. https://doi.org/10.1016/j.compag.2018.01.020 (2018).

 18.  Shi,  P.,  Li,  G.,  Yuan,  Y.,  Huang,  G.  &  Kuang,  L.  Prediction  of  dissolved  oxygen  content  in  aquaculture  using  clustering-based

softplus extreme learning machine. Comput. Electron. Agric. 157, 329–338. https://doi.org/10.1016/j.compag.2019.01.042 (2019).

 19.  Yin, L. et al. Modeling dissolved oxygen in a crab pond. Ecol. Model. 440, 109385. https://doi.org/10.1016/j.ecolmodel.2021.109385

(2021).

 20.  Chen, Z., Hu, Z., Xu, L., Zhao, Y. & Zhou, X. DA-Bi-SRU for water quality prediction in smart mariculture. Comput. Electron. Agric.

200, 107219. https://doi.org/10.1016/j.compag.2022.107219 (2022).

 21.  Qin, Y. et al. A dual-stage attention-based recurrent neural network for time series prediction. ArXiv Preprint (2017).  h t t p s : / / a r x i v

. o r g / a b s / 1 7 0 4 . 0 2 9 7 1

 22.  Liang, Y., Ke, S., Zhang, J., Yi, X. & Zheng, Y. Geoman: Multi-level attention networks for geo-sensory time series prediction. IJCAI

2018 Proceedings, 3428–3434. (2018). https://doi.org/10.24963/ijcai.2018/477

 23.  Shi, J., Wang, S., Qu, P. & Shao, J. Time series prediction model using LSTM-Transformer neural network for mine water inflow.

Sci. Rep. 14 (1), 18284. https://doi.org/10.1038/s41598-024-26398-3 (2024).

 24.  Cao, X., Ren, N., Tian, G., Fan, Y. & Duan, Q. A three-dimensional prediction method of dissolved oxygen in pond culture based

on Attention-GRU-GBRT. Comput. Electron. Agric. 181, 105955. https://doi.org/10.1016/j.compag.2021.105955 (2021).

 25.  Egbueri, J. C. & Agbasi, J. C. Combining data-intelligent algorithms for the assessment and predictive modeling of groundwater
resources quality in parts of southeastern Nigeria. Environ. Sci. Pollut. Res. 29 (38), 57147–57171.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 3 5 6 - 0
2 2 - 2 0 7 9 6 - 9     (2022).

 26.  Boulila, W., Ghandorh, H., Khan, M. A., Ahmed, F. & Ahmad, J. A novel CNN-LSTM-based approach to predict urban expansion.

Ecol. Inf. 64, 101325. https://doi.org/10.1016/j.ecoinf.2021.101325 (2021).

 27.  Jiang, B., Gong, H., Qin, H. & Zhu, M. Attention-LSTM architecture combined with bayesian hyperparameter optimisation for

indoor temperature prediction. Build. Environ. 224, 109536. https://doi.org/10.1016/j.buildenv.2022.109536 (2022).

 28.  Li, L., Jiang, P., Xu, H., Lin, G. & Guo, D. Water quality prediction based on recurrent neural network and improved evidence
theory: A case study of qiantang river, China. Environ. Sci. Pollut. Res. 26, 19879–19896.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 3 5 6 - 0 1 9 - 0 5 2 5
6 - 9     (2019).

 29.  Dangut, M. D., Skaf, Z. & Jennions, I. K. Rare failure prediction using an integrated auto-encoder and bidirectional gated recurrent

unit network. IFAC-PapersOnLine 53 (3), 276–282. https://doi.org/10.1016/j.ifacol.2020.11.209 (2020).

 30.  She, D. & Jia, M. A BiGRU method for remaining useful life prediction of machinery. Measurement 167, 108277.  h t t p s : / / d o i . o r g / 1

0 . 1 0 1 6 / j . m e a s u r e m e n t . 2 0 2 0 . 1 0 8 2 7 7     (2021).

 31.  Ling, J., Zhu, Z., Luo, Y. & Wang, H. An intrusion detection method for industrial control systems based on bidirectional simple

recurrent unit. Comput. Electr. Eng. 91, 107049. https://doi.org/10.1016/j.compeleceng.2021.107049 (2021).

 32.  Liu, J. et al. Accurate prediction scheme of water quality in smart mariculture with deep Bi-S-SRU learning network. IEEE Access.

8, 24784–24798. https://doi.org/10.1109/ACCESS.2020.2972524 (2020).

 33.  Kanipriya, M., Hemalatha, C., Sridevi, N., SriVidhya, S. R. & Shabu, S. J. An improved capuchin search algorithm optimised hybrid
CNN-LSTM architecture for malignant lung nodule detection. Biomed. Signal Process. Control. 78, 103973.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1
6 / j . b s p c . 2 0 2 2 . 1 0 3 9 7 3     (2022).

 34.  Liu,  X.,  Lu,  D.,  Zhang,  A.,  Liu,  Q.  &  Jiang,  G.  Data-driven  machine  learning  in  environmental  pollution:  gains  and  problems.

Environ. Sci. Technol. 56 (4), 2124–2133. https://doi.org/10.1021/acs.est.1c05971 (2022).

 35.  Zeng, L., Sun, B. & Zhu, D. Underwater target detection based on faster R-CNN and adversarial occlusion network. Eng. Appl.

Artif. Intell. 100, 104190. https://doi.org/10.1016/j.engappai.2021.104190 (2021).

 36.  Wu, H. et al. Evaluating surface water quality using water quality index in Beiyun river, China. Environ. Sci. Pollut. Res. 27, 35449–

35458. https://doi.org/10.1007/s11356-020-09465-2 (2020).

 37.  Wang,  Z.,  Duan,  L.,  Shuai,  D.  &  Qiu,  T.  Research  on  water  environmental  indicators  prediction  method  based  on  EEMD

decomposition with CNN-BiLSTM. Sci. Rep. 14 (1), 1676. https://doi.org/10.1038/s41598-024-19436-4 (2024).

 38.  Zheng, Y., Shao, Z., Deng, M., Gao, Z. & Fu, Q. MOOC dropout prediction using a fusion deep model based on behaviour features.

Comput. Electr. Eng. 104, 108409. https://doi.org/10.1016/j.compeleceng.2022.108409 (2022).

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

12

www.nature.com/scientificreports/

 39.  Chen,  Y.  et  al.  Waterfowl  breeding  environment  humidity  prediction  based  on  the  SRU-based  sequence  to  sequence  model.

Comput. Electron. Agric. 201, 107271. https://doi.org/10.1016/j.compag.2022.107271 (2022).

 40.  Kushwaha,  N.  L.  et  al.  Metaheuristic  approaches  for  prediction  of  water  quality  indices  with  relief  algorithm-based  feature

selection. Ecol. Inf. 75, 102122. https://doi.org/10.1016/j.ecoinf.2023.102122 (2023).

 41.  Dehghani, A. et al. Comparative evaluation of LSTM, CNN, and ConvLSTM for hourly short-term streamflow forecasting using

deep learning approaches. Ecol. Inf. 75, 102119. https://doi.org/10.1016/j.ecoinf.2023.102119 (2023).

 42.  Lan, C. et al. State prediction of hydro-turbine based on WOA-RF-Adaboost. Energy Rep. 8, 13129–13137.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6

/ j . e g y r . 2 0 2 2 . 1 0 . 0 0 7     (2022).

Author contributions
Wenjun  Liu,  Xuekai  Gao  and  Longqin  Xu  conducted  the  research  design,  performed  the  data  analysis,  and
drafted the manuscript. Shuangyin Liu, Tonglai Liu and Cai Chengqing assisted in refining the methods and
critically reviewed the manuscript. Shahbaz Gul Hassan writes and coordinated the research project and revised
the manuscript critically for important intellectual content. Ferdous Sohel contributed to the conception of the
study and helped perform the analysis with constructive discussions. Murtaza Hasan and Mansour Ghorban-
pour: review, writing and editing.

Funding
This paper was supported partly by the National Natural Science Foundation of China under Grant 62373390,
the natural Science Foundation of Guangdong Province under Grant2022B1515120059, Science and Technology
Program of Guangzhou under Grant 2023E04J1238, 2023E04J1239, Guangdong Science and Technology Project
under Grant 2020B0202080002, Major Science and Technology Special Projects in Xinjiang Uygur Autonomous
Region 2022A02011.

Declarations

Competing interests
The authors declare no competing interests.

Ethical approval
This research involved no human participants or animal studies. All procedures performed in studies involving
data on aquatic organisms were in accordance with the ethical standards of the institution at which the studies
were conducted.

Consent to participate
Not applicable. This research did not involve human participants.

Consent to publish
Not applicable. This manuscript does not contain data from any person.

Additional information
Correspondence and requests for materials should be addressed to M.G. or S.G.H.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.

Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have
permission under this licence to share adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o
n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /     .

© The Author(s) 2025

Scientific Reports |        (2025) 15:24643

| https://doi.org/10.1038/s41598-025-10786-5

13

