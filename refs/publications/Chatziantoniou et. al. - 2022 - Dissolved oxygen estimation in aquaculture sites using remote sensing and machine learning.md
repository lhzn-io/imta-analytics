Contents lists available at ScienceDirect

Remote Sensing Applications: Society and
Environment

journal homepage: www.elsevier.com/locate/rsase

Dissolved oxygen estimation in aquaculture sites using remote
sensing and machine learning

Andromachi Chatziantoniou a, *, Spyros Charalampis Spondylidis a,
Orestis Stavrakidis-Zachou b, Nikos Papandroulakis b, Konstantinos Topouzelis a
a Laboratory of Environmental Quality and Geospatial Applications, Department of Marine Sciences, University of the Aegean, Greece
b Institute of Marine Biology, Biotechnology and Aquaculture, Hellenic Centre for Marine Research, Crete, Greece

A R T I C L E   I N F O

A B S T R A C T

Keywords:

SVR
Dissolved oxygen
CMEMS
Remote sensing
Aquaculture

Dissolved oxygen (DO) is one of the most critical parameters for aquaculture, as it is vital for all
living organisms. The survival, growth and food intake of fish is directly affected by changes in
DO concentration. Therefore, the systematic and continuous monitoring of DO is of crucial im-
portance for proper production management. DO does not change the optical properties of water,
so it is impossible to estimate its concentration directly from the reflection values of satellite sen-
sors. However, several studies have suggested that it can be estimated indirectly, based on its cor-
relation with other parameters such as chlorophyl-a (chl-a) and sea surface temperature (SST).
The present study aims to integrate satellite data, along with in-situ observations to bring forth in-
novative approaches on how DO can be estimated and monitored on large scale near aquaculture
facilities. In this context we exploited daily CMEMS data (chl-a and SST) along with in-situ data
(DO) to train a support vector regression (SVR) model. Our in-situ dataset included daily DO mea-
sures from Agrilia fish farm in Lesvos for the year 2021. The accuracy of our model was tested us-
ing the value of Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). Our prelimi-
nary results indicate that our model performs well locally with promising scalability, which paves
the way for the development of real-time monitoring systems for aquaculture.

1. Introduction

Oxygen is, along with temperature, one of the most critical environmental parameters affecting the physiology and performance
of marine organisms since it is requisite for aerobic metabolism. Consequently, the concentration of dissolved oxygen (DO) in the wa-
ter is a monitoring parameter of great importance for finfish aquaculture as it directly affects the survival, growth, food intake, and
health of the farmed fish (Oldham et al., 2019), (Burt et al., 2012). For an aquaculture cage in particular, the systematic and continu-
ous monitoring of DO constitutes a necessity because the environmental conditions at the rearing sites are outside human control (as
opposed to land-based production systems) and are therefore prone to fluctuations that may threaten production.

Traditionally, DO has been monitored with in-situ measurements using sensors either manually or, more recently, with semi-
automated and automated systems (Parra et al., 2018). While such modes of DO monitoring are simple and have been effective for the
empirically-driven practices of the past, the rapid expansion of aquaculture towards precise, data-driven management (precision
farming) necessitates the development and implementation of advanced systems that utilize automation and modern technologies to-
wards forecasting and real-time monitoring (O'Donncha and Grant, 2020), (Raju and Varma, 2017). Of particular importance is the

* Corresponding author.
E-mail address: achatz@marine.aegean.gr (A. Chatziantoniou).

https://doi.org/10.1016/j.rsase.2022.100865
Received 8 July 2022; Received in revised form 20 October 2022; Accepted 27 October 2022

RemoteSensingApplications:SocietyandEnvironment28(2022)100865Availableonline7November20222352-9385/©2022TheAuthors.PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-nc-nd/4.0/).A. Chatziantoniou et al.

possibility of forecasting the oxygen concentration in the farm depending on the site-specific characteristics of the farming area and
its surroundings. For this information, in situ sensors are not particularly efficient as they cannot provide the required area coverage.
Furthermore, organized zones of aquaculture activity with several farms installed have similar needs and, large scale monitoring is es-
sential for forecasting. A promising field that may provide useful tools in that context is remote sensing.

Remote sensing is widely used for the detection of optically active parameters such as chlorophyl-a (chl-a), total suspended mat-
ter, and temperature. Satellite sensors are able to detect parameters that affect the optical properties of water at specific wavelengths
(e.g. chl-a). Therefore, it is unlikely to record the concentration of DO directly from the reflection values of the satellite sensors. How-
ever, research has shown that it can be estimated indirectly because of its correlation with other parameters, such as temperature and
chl-a (Guo et al., 2021), (Kim et al., 2020).

DO generally exhibits a negative correlation with sea temperature (Matear and Hirst, 2003). As the temperature of water in-
creases, the solubility of oxygen decreases. Therefore, seasonal variations of DO concentration can be observed in surface waters in
winter and early spring when there is a peak and, in the summer, where the concentration reaches the lowest point. Especially in the
Mediterranean studies have shown that solubility due to temperature is the main driving force of DO concentrations in surface waters
(Mavropoulou et al., 2020).

Another major oceanographic parameter that greatly affects the levels of DO is the primary production. In remote sensing, pri-
mary production is usually quantified by chl-a concentration that acts as an index of phytoplankton abundance in surface waters (Guy
et al., 1993), (Lewis et al., 2016). In the daytime, due to photosynthesis, phytoplankton releases oxygen and as such, there is a posi-
tive correlation between chlorophyll concentration and DO. This is particularly evident in the productive water layer, the depth of
which varies between the surface and the thermocline and between seasons and phytoplankton species. Oxygen levels are higher in
surface waters because that is where the ocean-atmosphere gas exchange occurs and lower at depths below 200m because that is
where the euphotic zone generally ends and oxygen absorption due to organic matter decomposition starts. On the other hand, re-
search has shown that high concentrations of phytoplankton can have a reverse effect (Wang et al., 2019). During night-time, when
there is an absence of light, phytoplankton absorbs oxygen and, in case of high abundance, it can even cause anoxic conditions in the
water. In these cases, the surrounding environment deteriorates with a negative impact on larger organisms, such as fish. In the case
of aquaculture farms where fish are in high concentrations the impact may be worse.

Knowing the above theoretical mechanisms, several researchers have tried to develop models based on the correlation of DO with

several environmental parameters, such as sea surface temperature (SST) and chl-a, to estimate its concentration and distribution.

Karakaya and Evrendilek (2011) developed multiple regression models to estimate water parameters (turbidity, DO, nitrite nitro-
gen, silicate, biological oxygen demand, chl-a) using Landsat 7 (ETM+) data. They used 18 Landsat 7 images and field measurements
from 16 stations on approximately same dates. Their results were very promising (R2 = 0.81), however, the developed methodology
is based on local measurements and cannot be generalized in other study areas.

Another interesting approach published by Batur's and Maktav's (Batur and Maktav, 2019), attempts to combine machine learning
and regression techniques (Response Surface Regression -RSR, Multiple Linear Regression - MLR, Artificial Neural Network - ANN,
Support Vector Machines - SVM), using satellite data (Landsat-8, Sentinel-2, Goturk 2) and field measures for the estimation of DO.
Their results indicated that RSR performed better than the other three methods (MLR, ANN, SVM) with R2 equal to 0.89.

The methods mentioned perform well locally but are difficult to generalize. In this context, Kim et al. (2020) tried to overcome
this challenge by correlating DO with parameters that can be directly measured from satellite sensors (SST, chl-a) using multiple re-
gression (MLR) to create a linear relation between the parameters. Pearson correlation analysis showed that DO is highly correlated
with SST and chl-a. Stepwise multiple regression was then used to develop a linear relation among DO, SST and chl-a. The proposed
model was then applied to MODIS and VIIRS products to observe the spatial and temporal changes in DO in the Saemangeum offshore
areas, Yellow Sea. The results showed a strong correlation between measured and predicted values of DO (R2 = 0.801) and the study
showed the potential for monitoring DO from satellite sensors.

Similarly, Guo et al. (2021) developed a generalized approach for the estimation of DO, based on Support Vector Regression
(SVR). Besides estimating DO and comparing several different methods, they also investigated the correlation of DO with other para-
meters (air temperature, incident shortwave radiation flux density, precipitation, nutrients). They exploited Landsat images for years
2000–2018 and daily MODIS data. From the comparison among the four different kernels (linear, polynomial, sigmoid, radial basis)
radial basis function (RBF) performed best. They also compared SVR to random forest (RF) and multiple regression (MLR), and ac-
cording to their results SVR outperformed the other two methods.

So far literature has highlighted the contribution of remote sensing and machine learning in the estimation of DO; however, the
challenges of coastal zones and aquaculture processes have not been addressed yet. While previous research has been successful in es-
timating DO in the water, the sparsity of data, the spatial resolution, and the scope of the existing studies does not fully account for
the importance of daily and reliable data for meeting aquaculture needs at the coastal zone. In this context, the purpose of our study
was to develop a methodology for the estimation of DO in coastal areas with aquaculture facilities, based on daily CMEMS data and
machine learning techniques.

2. Methods and data

2.1. Study site

The test site is located at the South-Eastern part of Lesvos Island (Agrilia), in North Aegean Sea (Fig. 1). The North Aegean is char-
acterized by lower salinity values (37–39 psμ) than the South Aegean (>38.5 psμ) (Zervakis and Georgopoulos, 2002) due to the Dar-
danelles Strait which inputs low salinity flow of water to the plateau of Lemnos. At the same time, studies have shown that the fresh

RemoteSensingApplications:SocietyandEnvironment28(2022)1008652A. Chatziantoniou et al.

Fig. 1. The study site is located at the South-Eastern part of Lesvos Island (Agrilia).

waters of the strait directly affect the seasonal circulation patterns due to the buoyancy of the water in Aegean (Androulidakis and
Kourafalou, 2011). North Aegean is generally characterized as an oligotrophic sea, due to a lack of phosphorus (Krom et al., 1991).
The capacity of the farm in the studied area is 380T per year and the main fish farmed are the European sea bass (Dicentrarchus
labrax) and the gilthead sea bream (Sparus aurata). The unit consists of circular cages of 10m–20 m m diameter. Water temperature in
the surrounding area ranges between 14 °C to 24 °C and the salinity is constant at 39 psμ. The average depth in the farming area is ap-
proximately 50m.

2.2. Satellite data

Most recent satellite sensors offer a wide range of data products useful for estimating water quality parameters at large scale tem-
porally. However, they are not suitable to be adopted as a standalone solution in real case scenarios due to their inability to collect
data under heavy cloud coverage.

Copernicus Marine Environment Monitoring Service (CMEMS)1 provides regular and systematic biogeochemical and physical in-
formation on the marine. In the framework of our study, we exploited Level-4, daily, gap-free satellite observations for chl-a concen-
tration and SST from multi-platform observations. We use CMEMS data to describe environmental conditions and study their correla-
tion to the concentration of DO. Knowing this relation, in-situ observations of DO are used to train a machine learning regression
model.

2.3. In-situ data

Our in-situ dataset includes field measures of DO and SST from Agrilia fish farm in Lesvos, collected for the year 2021. DO is mea-
sured daily (8:00am - 10:00am) using Oxy Guard scavenging packet. The 80% of the dataset was used as training sample and the re-
maining 20% was used as test sample.

2.4. Methodology

Regression analysis is widely used for prediction and forecasting, where its use has substantial overlap with the field of machine
learning. Regression methods are used to estimate the relation between a dependent variable and one or more independent variables
(features). In this study our aim is to estimate the concentration of DO in relation to chl-a and SST. All the parameters are described in
continuous values, so we selected the implementation of a regression model instead of classification. Commonly used regression mod-
els include Simple Linear Regression, Polynomial Regression and Logistic Regression. For the present study, we developed an ap-
proach for DO estimation based on a Support Vector Regression machine learning model, using CMEMS data and in-situ observations.
For every set of coordinates an array was created including the values of chl-a and SST, as well as the values of one, two and three
days prior to the sampling.

Support Vector Regression (SVR) uses the same principles as SVMs but returns continuous values instead of classified. SVR has
been proven to be successful in solving linear and nonlinear problems and perform sufficiently with limited datasets (Guo et al.,
2021). Support Vector Machines is a nonlinear and non-parametric large margin supervised machine learning classifier implementing
Vapnik's structural risk minimization principle (Vapnik, 1995). Most linear regression methods are based on the minimization of the
sum of squared errors. In SVR the objective is to handle the error in constraints, giving the flexibility to choose our tolerance, find the
appropriate hyperplane and define the acceptable error margins (ε). Essentially, the hyperplane is the decision surface that describes

1 https://marine.copernicus.eu/.

RemoteSensingApplications:SocietyandEnvironment28(2022)1008653A. Chatziantoniou et al.

the optimal values. Altering the maximum ε allows to achieve the desired accuracy to our model. The slack variables ξ allow some
training errors, guaranteeing robustness to noise and outliers. The objective function and the constraints are described by the follow-
ing equations (1) and (2):

MIN

1
2

w

2 + C

‖

‖

n

∑
i=1 |

𝜉

|


yi

− wixi


 ≤ 𝜀 + 𝜉

(1)

(2)

where yᵢ is the target, wᵢ is the coefficient, and xᵢ is the predictor (feature). C corresponds to a user selected parameter to control the
complexity of the model, acting as a trade-off parameter between nonlinearity and number of training errors.

To represent more complex hyperplane shapes than the linear methods, the techniques can be extended by using kernel functions
(Chatziantoniou et al., 2017). The most common kernels include polynomial kernel, radial basis function (RBF), and sigmoid kernel.
In this study, RBF kernel was used due to its promising capabilities (Guo et al., 2021).

SVR is simple structured and supported by several programming languages. For the implementation of the model in our study we
used the scikit-learn library (v.0.18.1) in Python 3.4. The evaluation of the model was conducted using the residuals and two statisti-
cal indices, namely, mean absolute error (MAE), root mean squared error (RMSE). MAE calculates the precision expressing the aver-
age distance between the estimated and the real values, and is described by equation (3). RMSE describes the standard deviation of
the residuals (equation (4)).

MAE +

n

|
|

∑
i=1

yi

− x
|
|n

n

RMSE = 





i=1

yi


2

− xi
n

(3)

(4)

where yᵢ is the predicted values and xᵢ the measured values.

Additionally, in order to evaluate the fitness of our model, R2 was also calculated. R2 is widely used in remote sensing classifica-
tion studies, however it is not recommended for evaluating regression models as it only expresses how well the regression line approx-
imates the real data point without considering all parameters.

The initial dataset included four columns (dates, DO in-situ, latitude and longitude). Using the dates and the coordinates as pri-
mary key another 8 columns were added with the values of chl-a and SST from CMEMS for each date and the previous 3 days (chl,
chld-1, chld-2, chld-3, sst, sstd-1, sstd-2, sstd-3). After removing the empty entries, the dataset was divided in training and testing sample
(80%–20%). The results were used to calculate the Mean Absolute Error (MAE) and produce the residuals’ plots, correlation chart and
time series. In Fig. 2 a graphical representation of the approach is presented.

Fig. 2. Flowchart of the implemented methodology.

RemoteSensingApplications:SocietyandEnvironment28(2022)1008654A. Chatziantoniou et al.

3. Results

3.1. Temporal and spatial variability

The data collected from CMEMS (chl-a, SST) and the estimated DO were used to create daily maps for examining the spatial distri-
bution of the aforementioned parameters. The maps represent the concentration of chl-a, sst and DO in the surrounding area with spa-
tial resolution of 1 km.

The following maps present the prevailing conditions of SST, chl-a (Fig. 3, Fig. 4) and DO (Fig. 4) in the surrounding sea area of
Lesvos for 12/03/2022. SST ranges between 14 °C - 16 °C and exhibit the lowest values near the north-east part of the island (14 °C),
while they gradually ascend towards the south-western part (up to 16 °C). This gradient is related to the upwelling processes near the
coastal region of western Lesvos, affecting the water circulation of the area (Androulidakis et al., 2017). A similar inverse pattern is
observed in the concentration of chl-a, however the values range between 0.2 and 1 mg m−3. Higher values are observed in the north-
eastern part of the island, near the coastline and inside the gulf of Gera. Overall, the concentration does not exceed 0.6–0.7 mg m−3
across the whole studied area.

The concentration of DO was estimated in relation to SST and chl-a. Consequently, the spatial distribution as presented in Fig. 5
follows the same pattern. Higher concentration is observed in the north-eastern waters, near the coastline and within the gulf of Gera,
presenting an obvious negative correlation with SST and a weaker positive correlation with chl-a.

Examining the timeseries of the SVR results, no significant seasonal variability was detected. The DO concentration varied from 7
to 7.8 ppm across the year with four major drops below 6.5 ppm. Highest values were detected in the winter and spring months and
the lowest during summer and fall. The highest values were detected in the winter and spring months and the lowest during summer
and fall. According to Souvermezoglou et al. (2014)), North Aegean surface layers are highly influenced by the influx waters of the
Black Sea through the Dardanelles Strait. These waters, compared to the Aegean, are rich in nutrients but have a high seasonal vari-
ability (Krom et al., 1991). Specifically, in winter and spring phosphate concentrations can be more than doubled in relation to au-
tumn. These nutrients are directly correlated to phytoplankton abundance which again is one of the main driving forces of oxygen
generation and release in the surface water layers.

In relation to the in-situ measurements, the DO seasonal variability can be tracked through both SST and chl-a (Fig. 6). This is es-
pecially true from January through September, when the negative correlation with SST and the positive with chl-a is clearly high-
lighted. In winter, lower temperatures in combination with high phytoplankton concentration allows bigger oxygen production with
a higher level of retention form the water column. On the other hand, in the summer the reduction of the inflow of inland waters lim-

Fig. 3. The spatial distribution of SST around Lesvos Island for four representative dates (fall, winter, spring, summer).

RemoteSensingApplications:SocietyandEnvironment28(2022)1008655A. Chatziantoniou et al.

Fig. 4. The spatial distribution of CHL-a around Lesvos Island for four representative dates (fall, winter, spring, summer).

its the nutrient concentration in the water column with a direct impact on phytoplankton abundance. Furthermore, the heated surface
has a limited capacity for oxygen retention. According to these results it would be expected that in the fall, when the temperatures
start to drop and chl-a concentration rises, the DO would also rise, but this behaviour is not present. Instead, the DO levels remain
similar to those in the summer months.

DO presented weak correlation with both chl-a and SST. DO and chl-a had a positive trend on the scale of 0.17 and DO and SST a
stronger negative correlation of −0.39 (Table 1). These results are in agreement with the theoretical mechanisms of DO concentration
in water as cooler waters can retain more oxygen molecules compared to warmer and phytoplankton releases oxygen in the water col-
umn during the day.

3.2. Model performance

The model's accuracy and precision were examined based on the MAE and RMSE indices. The model produced results with a MAE
of 0.11 and RMSE of 0.13 (Table 2). The rating stands close the decimal precision of the in-situ measurements which had a decimal
precision of one. An error of 0.11 can be considered acceptable for most real-life applications as meaningful fluctuations of DO.

Accuracy can be explored with the residual plot in Fig. 3. The residuals present an even distribution around 0, showcasing high ac-
curacy. There is no visible fluctuation around the 0 axis that could hint to a different model response based on the DO levels. Constant
variation of residuals means that the rate of error also remains constant on both ends of the value spectrum and that the model has a
low variation of resulting errors. Similar conclusions are extracted by the density plot (Fig. 7), where the residuals present a normal
distribution around the mean. There is no significant deviation on either side of the histogram that could point to unbalanced results,
and the bias is around the value of 0.1, close the MAE results.

4. Discussion and conclusions

The present study was aiming at the development of a methodology for the estimation of DO near aquaculture facilities. In this
context we exploited daily CMEMS data (chl-a and SST) along with in-situ data (DO) to train an SVR model. The accuracy of our
model was tested using the value of Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), as well as the residuals’ plot.
The most common used error metrics for evaluating a regression model are MAE and RMSE. Both metrics are describing the dis-
tance between the actual and the predicted values and are measured in the same units as the output variable, making the interpreta-
tion of loss easy. Our model performed well with MAE of 0.11 and RMSE of 0.13, and the residuals were evenly distributed around 0.
Our results showed high precision and accuracy. We have chosen to use MAE and RMSE indices to validate our model as they give as a
clearer view of the error and distribution of the residuals. On the contrary, R2 was poor (0.32) compared to other studies. For example

RemoteSensingApplications:SocietyandEnvironment28(2022)1008656A. Chatziantoniou et al.

Fig. 5. The spatial distribution of DO around Lesvos Island for four representative dates (fall, winter, spring, summer).

Guo et al. (2021) reached a score of 0.94 using a similar approach in inland waters for a long term analysis. R2 is generally used in
similar studies to examine the fitness of the model instead of the performance, and it is not representing of the magnitude and direc-
tion of error. R2 creates a baseline model to compare the trained model and is a good measure to determine how well the model fits
the dependent variables, however it does not give any information about the distribution of the residuals. For this reason, MAE and
RMSE are considered to be more appropriate to validate the performance of regression models as they give information about the
closeness of the prediction to the actual values. In this context we do not consider the poor value of R2 to be overall disappointing for
our results.

The timeseries analysis highlighted some extreme values during the summer, however they are not considered critical to the farm
as the saturation of oxygen is greater than 80%. The values of chl-a and DO present small changes during the year (range <1 unit)
and they do not appear to have significant correlation (0.17), but taking into consideration both the temporal and the spatial distribu-
tion we can observe a positive trend connecting the two variables. On the contrary, SST ranges from 16 °C to 26 °C and the correlation
with both chl-a and DO is stronger but negative (−0.67 and −0.39 respectively). This inverse correlation has also been reported by
Kim et al. (2020) who performed a multiple linear regression for a long term analysis with correlation coefficients ranging from
−0.743 to −0.792.

The method we chose to use in our study (SVR) has also been used with promising results in the studies of Batur and Maktav
(2019) and Guo et al. (2021) and outperformed several other approaches (Linear Regression, Multiple Linear Regression, Random
Forests). Guo et al., 2021 ((Guo et al., 2021)) also suggest this method over others based on its low complexity which makes it easy to
be adopted by several programming language, and the ability to solve linear and nonlinear problems, even with limited datasets. Both
studies also report the promising scalability and generalizability of SVR in comparison to simple and multiple linear regression mod-
els.

Our results show a promising approach for estimating DO at aquaculture sites, which paves the way for the development of real-
time monitoring systems for aquaculture. The methodology was successful at correlating DO with SST and chl-a, while the precision
of the estimates was also high when compared with field data. Τhe method was able to depict not only shifts in the seasonal patterns
of DO but also to detect sudden drops in concentration in at least four occasions during the summer (Fig. 6). While the drops in the an-
alyzed time-series are of minor practical interest because they are relatively small and thus, don't constitute a concern for fish health
(saturation remained >80%), the capability of the method to realistically capture them is reflective of its potential as a monitoring
tool. Abrupt changes in DO typically occur in the summer, as seen here, during heatwaves or low circulation periods leading to hy-

RemoteSensingApplications:SocietyandEnvironment28(2022)1008657A. Chatziantoniou et al.

Fig. 6. Seasonal variability of DO (1), SST (2) and chl-a (3), along with the boxplots which show the distribution of their values.

Table 1
Correlation between chl-a, SST and DO.

SST
DO
CHL

Table 2
Model performance results.

MAE

0,11

SST

1
−0,39
−0,66

DO

1
0,17

CHL

1

RMSE

0,13

R2

0,32

poxic events. Severe hypoxic events can be detrimental to the fish as they cause increased mortalities and substantial energetic costs
related to their stress response (Wade et al., 2019), (Vikeså et al., 2017). Therefore, the usefulness of a monitoring tool for DO is
largely associated with its accuracy at capturing theses rare but life-threating, for the fish, events.

Another advantage of using this method for the estimation of DO is that it increases the spatial scale at which monitoring can oc-
cur. While in-situ sensors are paramount for precise measurements within a single cage of a farm, a remote sensing approach offers a
better representation of the oxygen conditions, and thus, potential dangers, at a larger area. Considering that aquaculture farms are
often aggregated within the limited coastal space of suitable farming areas, either as single operations or as an organized industrial
park, it is imperative for the aquaculture producers to monitor the DO at a higher spatial scale. The same applies to administrative au-
thorities that may be interested in the supervision of zones of organized aquaculture activity at a regional level.

Our preliminary results are promising and indicate correlation between SST, chl-a and DO. The predicted and the measured values
differ less than 3% in most cases. The lack of extreme incidents during the study period and the low variability of the values in the

RemoteSensingApplications:SocietyandEnvironment28(2022)1008658A. Chatziantoniou et al.

Fig. 7. Density plot presenting the residuals distribution around 0.

area makes the prediction more challenging, since the model is only trained for a limited range of values. This is considered to be a
weakness of this study, as we have noticed that when the values exceed the normal range, the differences between the predicted and
measured values are higher. In order to overcome this challenge, we are planning to expand our study to more sites with different pre-
vailing conditions to feed our model with more data. Increasing the dataset to include more cases is essential for proper training of the
model and, consequently, for improving our results.

Funding

This research has been co-financed by the European Regional Development Fund of the European Union and Greek national funds
through the Operational Program Competitiveness, Entrepreneurship, and Innovation, under the call RESEARCH – CREATE – INNO-
VATE (project code: T2EDK-02687).

Author agreement statement

We the undersigned declare that this manuscript is original, has not been published before and is not currently being considered

for publication elsewhere.

We confirm that the manuscript has been read and approved by all named authors and that there are no other persons who satis-
fied the criteria for authorship but are not listed. We further confirm that the order of authors listed in the manuscript has been ap-
proved by all of us.

We understand that the Corresponding Author is the sole contact for the Editorial process. He/she is responsible for communicat-

ing with the other authors about progress, submissions of revisions and final approval of proofs.

Ethical Statement for Solid State Ionics

Hereby, I/Andromachi Chatziantoniou/consciously assure that for the manuscript/Dissolved Oxygen estimation in Aquaculture

sites using remote sensing and machine learning/the following is fulfilled:

1) This material is the authors' own original work, which has not been previously published elsewhere.
2) The paper is not currently being considered for publication elsewhere.
3) The paper reflects the authors' own research and analysis in a truthful and complete manner.
4) The paper properly credits the meaningful contributions of co-authors and co-researchers.
5) The results are appropriately placed in the context of prior and existing research.
6) All sources used are properly disclosed (correct citation). Literally copying of text must be indicated as such by using quotation

marks and giving proper reference.

7) All authors have been personally and actively involved in substantial work leading to the paper, and will take public

responsibility for its content.

The violation of the Ethical Statement rules may result in severe consequences.
To verify originality, your article may be checked by the originality detection software iThenticate. See also http://

www.elsevier.com/editors/plagdetect.

I agree with the above statements and declare that this submission follows the policies of Solid State Ionics as outlined in the Guide

for Authors and in the Ethical Statement.

Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to

influence the work reported in this paper.

RemoteSensingApplications:SocietyandEnvironment28(2022)1008659A. Chatziantoniou et al.

Data availability

Data will be made available on request.

Acknowledgments

We would like to express our appreciation to Avramar SA, for their contribution to this study by providing in-situ data and consul-

tation.

References

Androulidakis, Y.S., Kourafalou, V.H., 2011. Evolution of a buoyant outflow in the presence of complex topography: the Dardanelles plume (North Aegean Sea). J.

Geophys. Res. Ocean. 116 (4), 1–24. https://doi.org/10.1029/2010JC006316.

Androulidakis, Y.S., Krestenitis, Y.N., Psarra, S., 2017. Coastal upwelling over the north Aegean Sea: observations and simulations. Continent. Shelf Res. 149, 32–51.

https://doi.org/10.1016/J.CSR.2016.12.002.

Batur, E., Maktav, D., 2019. Assessment of surface water quality by using satellite images fusion based on PCA method in the Lake Gala, Turkey. IEEE Trans. Geosci.

Rem. Sens. 57 (5), 2983–2989. https://doi.org/10.1109/TGRS.2018.2879024.

Burt, K., et al., 2012. Environmental conditions and occurrence of hypoxia within production cages of Atlantic salmon on the south coast of Newfoundland. Aquacult.

Res. 43 (4), 607–620. https://doi.org/10.1111/J.1365-2109.2011.02867.X.

Chatziantoniou, A., Petropoulos, G.P., Psomiadis, E., 2017. Co-Orbital Sentinel 1 and 2 for LULC mapping with emphasis on wetlands in a mediterranean setting based

on machine learning. Rem. Sens. 9 (12). https://doi.org/10.3390/rs9121259.

Guo, H., Huang, J.J., Zhu, X., Wang, B., Tian, S., Xu, W., Mai, Y., 2021. A generalized machine learning approach for dissolved oxygen estimation at multiple

spatiotemporal scales using remote sensing. Environ. Pollut. 288, 117734. https://doi.org/10.1016/j.envpol.2021.117734.

Guy, R.D., Fogel, M.L., Berry, J.A., 1993. Photosynthetic fractionation of the stable isotopes of oxygen and carbon. Plant Physiol. 101 (1), 37–47. https://doi.org/

10.1104/PP.101.1.37.

Karakaya, N., Evrendilek, F., 2011. Monitoring and validating spatio-temporal dynamics of biogeochemical properties in Mersin Bay (Turkey) using Landsat ETM+.

Environ. Monit. Assess. 181 (1–4), 457–464. https://doi.org/10.1007/S10661-010-1841-5.

Kim, Y.H., Son, S., Kim, H.C., Kim, B., Park, Y.G., Nam, J., Ryu, J., 2020. Application of satellite remote sensing in monitoring dissolved oxygen variabilities: a case

study for coastal waters in Korea. Environ. Int. 134, 105301. https://doi.org/10.1016/j.envint.2019.105301.

Krom, M.D., Kress, N., Brenner, S., Gordon, L.I., 1991. Phosphorus limitation of primary productivity in the eastern Mediterranean Sea. Limnol. Oceanogr. 36 (3),

424–432. https://doi.org/10.4319/lo.1991.36.3.0424.

Lewis, K.M., Mitchell, B.G., van Dijken, G.L., Arrigo, K.R., 2016. Regional chlorophyll a algorithms in the Arctic Ocean and their effect on satellite-derived primary

production estimates. Deep Sea Res. Part II Top. Stud. Oceanogr. 130, 14–27. https://doi.org/10.1016/J.DSR2.2016.04.020.

Matear, R.J., Hirst, A.C., 2003. Long-term changes in dissolved oxygen concentrations in the ocean caused by protracted global warming. Global Biogeochem. Cycles 17

(4), 1125. https://doi.org/10.1029/2002GB001997. Dec.

Mavropoulou, A.M., Vervatis, V., Sofianos, S., 2020. Dissolved oxygen variability in the mediterranean sea. J. Mar. Syst. 208 (May). https://doi.org/10.1016/

j.jmarsys.2020.103348.

Oldham, T., Nowak, B., Hvas, M., Oppedal, F., 2019. Metabolic and functional impacts of hypoxia vary with size in Atlantic salmon. Comp. Biochem. Physiol. A. Mol.

Integr. Physiol. 231, 30–38. https://doi.org/10.1016/J.CBPA.2019.01.012.

O’Donncha, F., Grant, J., 2020. Precision aquaculture. IEEE Internet Things Mag 2 (4), 26–30. https://doi.org/10.1109/IOTM.0001.1900033.
Parra, L., Lloret, G., Lloret, J., Rodilla, M., 2018. Physical sensors for precision aquaculture: a review. IEEE Sensor. J. 18 (10), 3915–3923. https://doi.org/10.1109/

JSEN.2018.2817158.

Raju, K.R.S.R., Varma, G.H.K., 2017. Knowledge based real time monitoring system for aquaculture using IoT. In: Proc. - 7th IEEE Int. Adv. Comput. Conf. IACC 2017.

pp. 318–321. https://doi.org/10.1109/IACC.2017.0075.

Souvermezoglou, E., Krasakopoulou, E., Pavlidou, A., 2014. Temporal and spatial variability of nutrients and oxygen in the North Aegean Sea during the last thirty

years. Mediterr. Mar. Sci. 15 (4), 805–822. https://doi.org/10.12681/mms.1017.

Vapnik, V.N., 1995. The Nature of Statistical Learning Theory. Springer, New York, NY. New York.
Vikeså, V., Nankervis, L., Hevrøy, E.M., 2017. Appetite, metabolism and growth regulation in Atlantic salmon (Salmo salar L.) exposed to hypoxia at elevated seawater

temperature. Aquacult. Res. 48 (8), 4086–4101. https://doi.org/10.1111/ARE.13229. Aug.

Wade, N.M., Clark, T.D., Maynard, B.T., Atherton, S., Wilkinson, R.J., Smullen, R.P., Taylor, R.S., 2019. Effects of an unprecedented summer heatwave on the growth
performance, flesh colour and plasma biochemistry of marine cage-farmed Atlantic salmon (Salmo salar). J. Therm. Biol. 80, 64–74. https://doi.org/10.1016/
J.JTHERBIO.2018.12.021.

Wang, C., Pawlowicz, R., Sastri, A.R., 2019. Diurnal and seasonal variability of near-surface oxygen in the Strait of Georgia. J. Geophys. Res. Ocean. 124 (4),

2418–2439. https://doi.org/10.1029/2018JC014766. Apr.

Zervakis, V., Georgopoulos, D., 2002. Hydrology and circulation in the north aegean (eastern mediterranean) throughout 1997 and 1998. Mediterr. Mar. Sci. 3 (1),

5–19. https://doi.org/10.12681/mms.254.

RemoteSensingApplications:SocietyandEnvironment28(2022)10086510