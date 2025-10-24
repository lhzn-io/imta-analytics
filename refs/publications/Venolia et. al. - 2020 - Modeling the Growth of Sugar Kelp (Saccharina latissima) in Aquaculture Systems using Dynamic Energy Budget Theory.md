Version of Record: https://www.sciencedirect.com/science/article/pii/S0304380020302222
Manuscript_8d6e84a37e110aa97536c9917c4e0643

1

2

3

4

5

6

7

8

9

Modeling the Growth of Sugar Kelp (Saccharina latissima) in Aquaculture Systems using

Dynamic Energy Budget Theory

Celeste T. Venoliaa, Romain Lavaudb, Lindsay A. Green-Gavrielidisc,d, Carol Thornberc, and

Austin T. Humphriesa,e*

a Department of Fisheries, Animal and Veterinary Sciences, University of Rhode Island,

10

Kingston, Rhode Island

11

12

b Institut des Sciences de la Mer, Université du Québec à Rimouski, Rimouski, QC, Canada

13

14

c Department of Natural Resources Science, University of Rhode Island, Kingston, Rhode Island

15

16

d Present address: Department of Biology and Biomedical Sciences, Salve Regina University,

17

Newport, RI, USA

18

19

e Graduate School of Oceanography, University of Rhode Island, Narragansett, Rhode Island

20

21

* Corresponding Author.

Email Address: humphries@uri.edu (Austin Humphries)

22

23

1

© 2020 published by Elsevier. This manuscript is made available under the Elsevier user license
https://www.elsevier.com/open-access/userlicense/1.0/

24

Keywords

25

Macroalgae; food production; bioenergetics; synthesizing units; Rhode Island

2

26

Abstract

27

Aquaculture is an industry with the capacity for further growth that can contribute to

28

sustainable food systems to feed an increasing global population. Sugar kelp (Saccharina

29

latissima) is of particular interest for farmers as a fast-growing species that benefits ecosystems

30

as a primary producer. However, as a new industry in the U.S., farmers interested in growing S.

31

latissima lack data on growth dynamics. To address this gap, we calibrated a Dynamic Energy

32

Budget (DEB) model to data from the literature and field-based growth experiments in Rhode

33

Island (U.S.A.). Environmental variables forcing model dynamics include temperature,

34

irradiance, dissolved inorganic carbon concentration, and nitrate and nitrite concentration. The

35

modeled estimates for field S. latissima blade length were accurate despite underestimation of

36

early season growth. In some simulations, winter growth was limited by the rate at which the

37

light-dependent reaction of photosynthesis, the first step of carbon assimilation, was performed.

38

Nitrogen (N) reserves were also an important limiting factor especially later in the spring season

39

as irradiance increased, although the low resolution of N forcing concentrations might restrict the

40

model accuracy. Since this model is focused on S. latissima grown in an aquaculture setting with

41

winter and spring growth, no specific assumptions were made to include summer growth patterns

42

such as tissue loss or reproduction. The results indicate that this mechanistic model for S.

43

latissima captures growth dynamics and blade length at the time of harvest, thus it could be used

44

for spatial predictions of S. latissima aquaculture production across a range of environmental

45

conditions and locations. The model could be a particularly useful tool for further development

46

of sustainable ocean food production systems involving seaweed.

47

3

48

1.  Introduction

49

Aquaculture is currently the fastest growing food production sector in the world and is

50

likely to become the main seafood supply in the future (FAO, 2018). In open systems of fed

51

species, aquaculture activities can cause concentrated fluxes of feces and feed wastage leading to

52

eutrophication (Wu, 1995) and alteration of food webs (Herbeck et al., 2013). Open aquaculture

53

systems composed of species that do not require supplemental feed or nutrients (i.e., primary

54

producers and filter feeders) avoid these harms and instead can provide important ecosystem

55

services such as removing dissolved organic and inorganic nutrients (Alleway et al., 2019).

56

Seaweeds are of particular interest as they mitigate hypoxia from terrestrial food production

57

systems and even protect shorelines through dampening of wave energy (Duarte et al., 2017).

58

Outside of these ecosystem services, growing seaweed has been proposed as a way to engage a

59

wider public audience with climate change via offsetting carbon emissions (Froehlich et al.,

60

2019). Seaweed aquaculture has the potential to generate net positive environmental and social

61

impacts, but this industry has been traditionally concentrated in Asian countries (FAO, 2018).

62

The U.S. does not produce enough aquatic plants to even register in the global production

63

statistics (< 0.1%; FAO, 2018). In the Northeast U.S., sugar kelp (Saccharina latissima) is a

64

local species of recent interest for food, biofuel, bioremediation, and pharmaceutical products

65

(Forbord et al., 2012). In a single season of aquaculture growth, S. latissima blades can grow up

66

to 60-140 cm depending on the water depth, planting time, and nutrient availability (Handå et al.,

67

2013). Oysters, however, are the most widely aquacultured species in coastal areas of the U.S

68

(NMFS, 2018). The Eastern oyster (Crassostrea virginica) mostly grows during the summer

69

months when water temperatures are above 15 (cid:176) C and is in a state of relative dormancy in the

70

winter (Dame, 1972). It has been suggested that cultivation of S. latissima could complement

4

71

oyster farming because of the differences in growing season with kelp growing mainly when

72

water temperatures are below 15 (cid:176) C. Therefore, kelp could provide an additional source of

73

income without interfering with oyster production. This new industry, however, would benefit

74

from production estimates in order to assess the biological and economic sustainability of S.

75

latissima farming.

76

Bioenergetic models can provide such production estimates by studying energy fluxes

77

and usage between the environment and the organism and within the organism. They constitute

78

useful tools in the early development of an aquaculture activity to: assess the carrying capacity of

79

a system before installing new farms (Grant et al., 2007; Filgueira et al., 2014), estimate

80

production and feeding ration (Cho and Bureau, 1998), or to optimize integrated multi-trophic

81

aquaculture (IMTA) systems (Ren et al., 2012). Forcing variables in bioenergetic modelling

82

frameworks are of prime importance as they define the system response. In the case of S.

83

latissima, blade growth is mainly influenced by irradiance, temperature, and nutrient

84

concentration (Boden, 1979). Other factors such as wave action (Buck and Buchholz, 2005) and

85

ambient light regime (Gerard, 1988) may also determine growth dynamics. In a simple predictive

86

model, Petrell et al. (1993) estimated growth of S. latissima using a linear relationship with

87

dissolved inorganic nitrogen concentration and a temperature correction. This model required an

88

assumption that nitrogen dynamics are always limiting growth, thus ignoring the potential

89

influence of irradiance. While integrating photosynthetic processes into a model can be

90

challenging, mechanistic approaches may be more suited to capture the physiological response to

91

environmental variability, especially in a changing environment (Denny and Helmuth, 2009).

92

Dynamic energy budget (DEB) theory provides a sound mechanistic basis for

93

understanding an organism’s energetics, which is used to model the flow of mass and energy

5

94

through an organism from uptake to usage for maintenance, growth, reproduction, or excretion

95

(Kooijman, 2010). This theory of metabolic organization provides a framework to examine the

96

interactive effects of environmental nutrient concentrations and irradiance on an organism

97

through parallel systems of nitrogen (N) and carbon (C) dynamics. Modeling autotrophs is a less

98

common direction for the application of DEB theory. Thus, multiple reserves are necessary to

99

accurately model matter and energy dynamics because of the different nutrient uptake pathways

100

(Kooijman, 2010). Autotroph DEB models have been constructed for microalgae (Lorena et al.,

101

2010, Livanou et al., 2019), phytoplankton-zooplankton interactions (Poggiale et al., 2010),

102

calcification of a coccolithophore (Muller and Nisbet, 2014), and recently the macroalga Ulva

103

lactuca (Lavaud et al., 2020). Broch and Slagstad (2012) were the first to develop a dynamic

104

bioenergetic model for S. latissima, borrowing concepts from DEB theory with the aim of

105

creating a tool for optimizing aquaculture production of Norwegian S. latissima. These authors

106

based their model structure on a Droop’s cell quota model completed by numerous empirical and

107

allometric relationships to simulate growth of S. latissima, but this simplification did not increase

108

parsimony (i.e., reduce the number of model parameters). Using a DEB framework, however,

109

ensures theoretical coherence (i.e., mechanistic description of metabolic processes) and ease of

110

model transference to other regions through less re-calibration.

111

Our objective with this study is to develop a bioenergetic model for S. latissima growth

112

using the mechanistic properties of DEB theory. Specifically, we aim to calibrate the macroalga

113

DEB model presented by Lavaud et al. (2020) to field data on kelp from Rhode Island (U.S.A.).

114

The application of this model to another species from a different environment constitutes an

115

important step in the validation of this model structure. The resulting model allows for growth

6

116

predictions based on environmental inputs and has the potential to support the sustainable

117

aquaculture industry, particularly with regard to site selection.

118

119

2.  Methods

120

121

2.1  Dynamic Energy Budget model assumptions

122

The S. latissima model is based on a DEB model developed for sea lettuce by Lavaud et

123

al. (2020). The core structure of the S. latissima model tracks the uptake of carbon (C) and

124

nitrogen (N), their assimilation into specific reserves and allocation to growth or maintenance or

125

their excretion (Figure 1). The variables that depict the state of the model are the mass of

126

structure

 (in mol V, moles of structure), Nitrogen reserve density

 (in mol N per mol V),

(cid:1)(cid:2)

(cid:3)(cid:4)(cid:5)

127

and Carbon reserve density

 (in mol C per mol V). The code for this model is freely

(cid:3)(cid:4)(cid:6)
available at https://github.com/CVenolia/SugarKelpDEB.

A core assumption of DEB theory, strong homeostasis, maintains that reserve and

128

129

130

structure have constant chemical compositions (Kooijman, 2010). This does not mean that there

131

are always constant amounts of reserve and structure; rather, the amount of carbon, nitrogen,

132

hydrogen, and oxygen relative to each other within specific reserves or structures remains

133

constant.

134

Two substrates and associated reserves were considered in this S. latissima model: C and

135

N (nitrate and nitrite, collectively); other potential nutrients such as phosphorous or potassium

136

were dismissed based on the fact that in regions where nitrogen is not abundant year-round,

137

nitrogen availability is what drives accelerated growth in winter and early spring (Gagné et al.,

138

1982). Adding further reserves to the model would increase complexity by increasing the number

7

139

of state variables and parameters with potentially little to no increase in accuracy. On the C side

140

of the model, since S. latissima and other algae use carbonic anhydrase to assimilate bicarbonate

141

and convert it into carbon dioxide (Axelsson et al., 2000), we assumed that assimilating carbon

142

dioxide directly was identical to assimilating carbon dioxide that was formed extracellularly

143

from bicarbonate through a carbon concentrating mechanism.

144

Another assumption of this DEB model is that S. latissima is a V1-morph. In DEB

145

theory, V1-morphs are organisms whose surface area is proportional to volume (Kooijman,

146

2010). S. latissima grows as a sheet in both length and width directions at the meristematic blade

147

region near the stipe (Sjøtun, 1993). Variation in blade thickness over an individual blade and

148

through time does not have a substantial impact on the surface area to volume ratio (Vettori and

149

Nikora, 2017) to preclude the V1-morph assumption. Drag from water speed has been found to

150

impact blade morphology (Buck and Buchholz, 2005) but this difference in appearance should

151

not affect the surface area to volume ratio either.

152

Other assumptions were grounded in the fact that this model was used to determine

153

aquaculture production, which is currently limited in time to November-May. Energy was not

154

used for reproduction or maturity in this model, a simplification that allows for a more

155

parsimonious model. There is evidence suggesting that kelp produces inhibitors that minimize

156

the formation of reproductive tissue during the rapid growth phase (Buchholz and Lüning, 1999,

157

Lüning et al., 2000). Moreover, only a small subset of blades show reproductive development by

158

the time the aquaculture harvest occurs in spring, towards the end of the first period of rapid

159

growth. Furthermore, the aquaculture season of S. latissima is set up to maximize growth while

160

minimizing loss or degradation of tissues due to various stresses. Apical frond loss in kelp is

161

correlated with temperature stress and wave action (Krumhansl et al., 2014), mechanical stress of

8

162

biofouling (Brown et al., 1997), and overall blade length (Sjøtun, 1993). A tissue loss function

163

would be necessary to accurately model S. latissima growth year-round, however, the exact

164

mechanism for this loss remains context-specific in the literature. Aquaculture farmers generally

165

harvest kelp before biofouling begins, which maximizes harvestable blade length and product

166

quality. Photoinhibition may occur in S. latissima when high light conditions are combined with

167

high temperature conditions (Heinrich et al., 2012), but since we limit the application of our

168

model to winter-spring seasons, photoinhibition was not accounted for. Photorespiration was not

169

included either to simplify model dynamics (Kooijman, 2010).

170

171

2.2 Model structure

172

All the equations for this model are based on and detailed in Lavaud et al. (2020; Table

173

1). S. latissima blade length (

) was calculated via total dry weight (

) using an allometric

174

relationship proposed by Gevaert et al. (2001; Table 1). The change in the three state variables

(cid:7)(cid:8)

(cid:9)(cid:10)

175

(reserve density of C and N and mass of structure) over time is described by differential

176

equations that where solved using the deSolve package (Soetaert et al., 2010) in R (R Core

177

Team, 2019).

178

179

2.3  Model calibration

180

The parameters of the S. latissima DEB model were manually calibrated to fit

181

simultaneously a combination of literature data and field data collected for this study (Table 2).

182

Root mean square error (RMSE) was used as a measure of spread in the residuals for assessing

183

the quality of model predictions compared to each observation data set.

184

9

185

186

2.3.1. Literature data

Information about the locations where literature studies were conducted was also

187

included because there are multiple ecotypes of S. latissima (Gerard, 1988), which may influence

188

their physiological response (Table 3). Due to a lack of local information on certain aspects of S.

189

latissima life history traits, this model was calibrated with data across multiple ecotypes of S.

190

latissima. The Arrhenius relationship parameters were estimated using a least squared non-linear

191

regression on compiled physiological rates from the literature. Prior to the estimation, each data

192

set was standardized by dividing by the averaged value found at the reference temperature (Table

193

3). The nitrate and nitrite uptake parameters,

 maximum volume specific nitrogen

194

assimilation and

 half-saturation concentration for NO3

- and NO2

- uptake, were calibrated

195

using nitrate uptake data from Espinoza and Chapman (1983). To match the dimensions used by

(cid:15)(cid:16)

(cid:11)(cid:12)(cid:4)(cid:5)(cid:13)(cid:14)

196

these authors (µmol N–1 gDW

–1 h–1) the volume-specific modeled N uptake was multiplied by

197

198

 (structural mass divided by dry weight). Photosynthesis parameters,

 photosynthetic

(cid:1)(cid:2) (cid:9)(cid:10)⁄
unit (PSU) density,

(cid:22)(cid:23)

 specific photon arrival cross section,

(cid:18)(cid:19)(cid:20)(cid:21)
 binding probability of a photon to

 (cid:25)(cid:12) (cid:23)

199

a free light synthesizing unit, and

 dissociation rate of photosynthetic products, were calibrated

using oxygen production data from Johansson and Snoeijs (2002).

(cid:26)(cid:12) (cid:23)

Appropriate literature data for calibrating several model parameters were not available.

200

201

202

For instance, air-based carbon dioxide uptake data for S. latissima (Ní Longphuirt et al., 2013)

203

were examined to estimate dissolved inorganic carbon uptake but ultimately were rejected due to

204

likely dissimilarity to submerged uptake. Carbon uptake parameters, maintenance rates, the yield

205

factor of C reserve and the rejection flux were estimated during model testing so as to result in

206

predicted length within the observed range in length data (Table 2). Other parameters such as the

207

reserve turnover rates are difficult to compare to measurable physiological data, so these

10

208

parameters were set based on previously assumed values by Lorena et al. (2010) and Lavaud et

209

al. (2020).

210

211

212

2.3.2. Field data

S. latissima was grown at four oyster farm sites from fall to spring in both 2017-2018

213

(Year 1) and 2018-2019 (Year 2). S. latissima seed was raised in aquaria from harvested local

214

reproductive S. latissima tissue collected at Ft. Wetherill, RI, following the methods of Redmond

215

et al. (2014), and seed lines were attached to ropes held in place by moorings at each of the

216

farms. The growing sites were split between Narragansett Bay and Pt. Judith Pond, RI (Figure 2).

217

Longlines of S. latissima were placed in duplicates at a depth of 1 m at all the growing sites. S.

218

latissima growth, measured as length and width (cm), was monitored every 20-85 days using a

219

subset of individuals harvested from the longline. The variability in monitoring timing was

220

largely driven by the availability of farmers to assist with logistics as well as weather conditions.

221

Temperature data were collected every fifteen minutes at each site using HOBO®

222

pendant loggers. Water samples were collected when S. latissima growth measurements were

223

taken to determine the concentrations of nitrate and nitrite. In year 1, nitrate and nitrite

224

concentrations were measured using a LACHAT Flow Injection Autoanalyzer (LACHAT, 2008,

225

method detection limit 0.3 µM). In year 2, nitrate and nitrite concentrations were determined

226

using an Astoria Pacific Model 303A Segmented Continuous Flow Autoanalyzer (Astoria-

227

Pacific Inc, Clackamas, OR; Eaton et al., 1998, method detection limit 1.43 µM). Because

228

Narragansett Bay S data were below the method detection limit for the analysis done in year 2,

229

we replaced them with data from the nearby University of Rhode Island Graduate School of

11

230

Oceanography to better reflect reality; samples were run on an Astoria Analyzer (Reed and

231

Oviatt, 2020, method detection limit of 0.1 µM).

232

233

2.4. Model forcing

234

The S. latissima model was forced with temperature, irradiance, dissolved inorganic

235

carbon (DIC) concentration, and nitrate and nitrite concentration data on an hourly time step.

236

Temperature recorded at fifteen-minute intervals at each site was averaged on an hourly basis.

237

Due to difficulties with biofouling on irradiance loggers, we used radiative forcing from the

238

North American Regional Reanalysis (Mesinger et al., 2006) to estimate photosynthetically

239

active radiation (PAR, mol γ m–2 h–1 or E m–2 h–1) using this equation:

, with

 the net shortwave radiation (W m–2) at the water surface

PAR  =  NSW ∗ PAR#$%& ∗

240

241

(*+ ∗ ,)

C ∗ e
calculated from downward shortwave flux minus upward shortwave flux,

∗ 3600

12(cid:9)

 the fraction of

242

the incident flux useable for photosynthesis (dimensionless),

3456789
 a conversion factor (m mol γ s–1

243

244

W–1),

 extinction coefficient (m–1),
;
hour. We used a value of 4.56 m mol γ s–1 W–1 for C (Mõttus et al., 2011), a

(cid:26)

 line depth (m), and 3600 to convert from per second to per

 of 0.43

:

245

(Mõttus et al., 2011), a

 of 0.46 m–1 from past work in Narragansett Bay (Ullman & Codiga,

(cid:26)

246

2010), and a

 of 1 m as kelp lines were held at a depth of a minimum of 1 m. We used linear

247

;

interpolation to create an hourly forcing from source data every three hours (Figure 3). All sites

3456789

248

had the same base irradiance forcing in one year using this method. DIC concentration data were

249

not collected in this study, so this forcing was estimated from other sources. The Pt. Judith Pond

250

sites were held at a constant DIC value of 1.836 10–3 mol DIC L–1 based on U.S. Environmental

251

Protection Agency data from Ninigret Pond (J. Grear, unpublished data). The Narragansett Bay

252

sites were held at a constant DIC value of 1.956 10–3 mol DIC L–1 based on data from Brenton

12

253

Point (Segarra, 2002). Nitrate and nitrite concentrations were also linearly interpolated on an

254

hourly basis. State variable initial conditions were estimated based on approximate length and

255

weight at planting of the kelp blades (

 = 0.00164 gDW). Reserve densities had to be assumed

256

but their impact on end results is limited to the first few days of the simulation. Initial

was

(cid:1)(cid:2)

257

set at 0.002 mol C mol V–1 and

 at 0.01 mol N mol V–1 in year 1 and 0.01 and 0.09,

(cid:3)(cid:4)(cid:6)

258

respectively, in year two.

(cid:3)(cid:4)(cid:5)

259

260

2.5  Sensitivity Analyses

261

To determine how each DEB parameter influenced simulation outputs, we analyzed the

262

local sensitivity of the three state variables to model parameters using an L1 summary value of

263

sensitivity from the R package FME (Soetaert and Petzoldt, 2010). The larger the L1 metric a

264

parameter has the greater the sensitivity of the state variables to that parameter.

265

266

3.  Results

267

268

3.1  Model calibration: Literature data

269

The Arrhenius relationship fit to the compiled literature data (Table 3) reflected

270

maximum physiological rates at temperatures around 13 °C (Figure 4). The lower boundary of

271

the temperature tolerance range in the Arrhenius relationship was 0 °C, and the upper boundary

272

was 13.39 °C. The rather low value for the upper boundary indicates that the optimum

273

temperature is close to the upper limit of the tolerance range for this species. However, the shape

274

of the curve past this point implies that the effects of high temperatures on the metabolism of

13

275

sugar kelp appear gradually with increasing temperature. The adjusted R-squared for this

276

relationship was 0.55 (p-value = 2.74 * 10–11).

277

Using the nitrate uptake data from Espinoza and Chapman’s (1983) St. Margaret’s Bay

278

site (Nova Scotia, Canada) provided estimates of maximum volume specific nitrate and nitrite

279

assimilation of 1.5 * 10–4 mol N mol V–1 h–1 and a half-saturation concentration of 2.5 * 10–6 mol

280

NO3

– and NO2

– L–1 (Figure 5). The fit for the data collected at 18 °C was slightly better with a

281

RMSE of 0.374 µmol N gDW

–1 h–1 than the 9 °C data at 0.504 µmol N gDW

–1 h–1.

282

For the oxygen production data (Johansson and Snoeijs, 2002) used to calibrate the

283

photosynthesis parameters, the values that had the lowest error around the data were a PSU

284

density

 = 0.05 mol PSU mol V–1, specific photon arrival cross section

of 1 m2 mol PSU–

(cid:18)(cid:19)(cid:20)(cid:21)

(cid:22)(cid:23)

285

1, a binding probability of a photon to a free light synthesizing unit

 = 0.5 (dimensionless), and

286

a dissociation rate of photosynthesis products

 = 0.075 mol γ mol PSU–1 h–1 (Figure 5). The

resulting RMSE for this data set was 0.54 mg O2 gDW

(cid:26)(cid:12) (cid:23)

287

–1 h–1. The maximum oxygen production

(cid:25)(cid:12) (cid:23)

288

rate of the model was approximately 4.95 mg O2 gDW

–1 h–1 (Figure 5).

289

290

3.2  Model calibration: Field data

291

In year 1, the maximum water temperature recorded at the sites was 16.7 °C in November

292

and the minimum temperature was –1.72 °C in January (Figure 6). For year 2, the maximum

293

temperature was 15.28 °C in May and the minimum temperature was –1 °C in January.

294

Temperature changes were consistent across all four sites for both years.

295

The nitrate and nitrite concentration forcing variable had a lower resolution than the

296

temperature forcing because of the linear interpolation between the N measurements (Figure 6).

297

The mean N concentration at the Pt. Judith Pond sites was 4.42 * 10–6 mol NO3

– and NO2

– L–1 (±

14

298

2.76 * 10–6) and 2.20 * 10–6 mol NO3

– and NO2

– L–1 (± 2.99 * 10–6) at the Narragansett Bay sites

299

in year 1. For year 2, the mean N concentration at the Pt. Judith Pond sites was 1.01 * 10–6 mol

300

NO3

– and NO2

– L–1 (± 2.11 * 10–6) and 1.87 * 10–6 mol NO3

– and NO2

– L–1 (± 2.97 * 10–6) at the

301

Narragansett Bay sites.

302

303

3.3  Predicted growth and model dynamics

304

S. latissima grew quickly with mean elongation across all sites studied of 0.87 ± 0.63 cm

305

d–1 in year 1 and 1.18 ± 0.62 cm d–1 in year 2 (Figure 7). End of season blade length varied, but

306

no clear trend based on sites was observed (Table 4). The S. latissima DEB model generally

307

underestimated growth observed in the early parts of the season (planting to end of March) but

308

accurately predicted the length at harvest within one standard deviation of the observed mean

309

length for the majority of sites (Figure 7). An exception to this trend was the first S. latissima

310

line planted at Pt. Judith Pond South in year 1 for which final length was overestimated. The

311

RMSEs for the model length prediction to the field length data ranged widely from 4.01 to 53.94

312

cm (Figure 7). Examining the reject fluxes from the growth SU indicate that the C reserve

313

(carbohydrates) limited model growth after planting for greatly variable time spans across the

314

sites, seasons, and lines (Figure 8). A growth limitation by C reserve may result from low C

315

assimilation due to a low specific relaxation rate. Temperature seemed to be the main factor

316

controlling C assimilation, as indicated by the greater similarity of the shape of the temperature

317

correction to that of C assimilation than the shape of the seasonal trend of irradiance (Figure 9).

318

N limitation seemed to have a strong role in controlling modeled S. latissima growth dynamics

319

overall due to the proportion of time C was rejected from the growth SU.

15

320

3.4  Sensitivity Analysis

321

The parameters with the largest effects (>9000 L1 summary value of sensitivity

,
B(cid:4)C

322

functions) on the state variables were

,

,

,

,

,

,

,

, and

323

(Figure 10). The parameters

,

<=

<(cid:13), <?
 and

<(cid:13)?

<@
 had a moderate effect with L1 values ranging

ADEFD

A(cid:4)(cid:6)(cid:2)

<(cid:13)@

A(cid:23)D

(cid:22)(cid:23)

(cid:25)(cid:12) (cid:23)
between 3000-7000. Finally, some parameters showed small but non-zero effects on the state

G(cid:12)(cid:4)(cid:6)(cid:13)(cid:14)

(cid:18)(cid:19)(cid:20)(cid:21)

324

325

variables, including:

,

A(cid:4)(cid:5)(cid:2)

(cid:26)(cid:4)D(cid:12)

,
(cid:26)(cid:4)(cid:16)

,

, and

 (Figure 10).

HDEF(cid:14)

(cid:26)(cid:12) (cid:23)

326

327

4.  Discussion

328

Aquaculture development represents a key role in expanding U.S. sustainable food

329

production and macroalgae can provide high returns when the proper growth conditions exist.

330

Understanding and predicting the growth dynamics of S. latissima can provide the aquaculture

331

industry with a powerful predictive tool for estimating production potential. This model is the

332

first attempt to apply Dynamic Energy Budget (DEB) theory to a macroalga of the order

333

Laminariales. The process-based model presented in this study allowed us to better understand

334

growth limitations as they relate to the behavior of the model.

335

336

4.1  Growth Limitation

337

In several model simulations, predictions of early S. latissima growth seemed to indicate

338

a limitation in carbon (C) assimilation due to a low modeled specific relaxation rate,

, by

339

photosynthetic SU2 processing the light-dependent reactions of photosynthesis. There is some

(cid:11)(cid:12)(cid:23)

340

evidence that a lack of C reserve occurs in the field during winter due to lower irradiance; S.

341

latissima individuals older than a year were shown to have a decrease in blade C content mid-

342

winter suggesting consumption of stored carbohydrates (Sjøtun, 1993). New sporophytes would

16

343

not have this carbohydrate pool to draw upon and would exclusively depend on photosynthesis to

344

acquire C. The decrease in C content observed by Sjøtun (1993) suggests that C dynamics may

345

be limiting S. latissima growth, but substrate limitation was not directly examined by this author.

346

In simulations where irradiance was the initial limiting factor for growth, the early season model

347

underestimation of field growth may reflect an outsized impact of the temperature correction of

348

 on the specific relaxation rate,

, in comparison to irradiance. As with many DEB parameters,

(cid:26)(cid:12) (cid:23)

 (cid:11)(cid:12)(cid:23)

349

 is difficult to estimate directly based on empirical data and our assumption of dependence on

(cid:26)(cid:12) (cid:23)
temperature as in other algae (Kooijman, 2010; Lavaud et al., 2020) may not be as relevant to S.

350

351

latissima. As ocean temperature seasonal trends trail behind irradiance changes (Brady-Campbell

352

et al., 1984), S. latissima’s early season growth could be driven by this early season increase in

353

irradiance rather than water temperature change. More data are necessary to confirm why the S.

354

latissima DEB model underestimates winter growth.

355

Other than an increase in irradiance, day length could also impact seasonal growth

356

patterns. Broch and Slagstad’s (2012) S. latissima model used the rate of change of day length in

357

a photoperiodic effect function to mimic growth seasonality. These authors relied on the

358

hypothesis that S. latissima is a “seasonal anticipator” with endogenous circadian rhythms (Kain,

359

1989). Seasonal anticipators are posited to grow strategically in response to a trigger. Other kelps

360

such as Laminaria hyperborea and Laminaria digitata have been shown to have free-running

361

seasonal growth patterns, which suggests control by endogenous circadian rhythms (Schaffelke

362

and Lüning, 1994). Species-specific evidence for this circadian hypothesis is lacking including

363

the mechanism for what would trigger S. latissima’s photoperiodic response. If this is the case,

364

substrate uptake or reserve mobilization parameters may be adjusted in the model in response to

365

a trigger to temporarily favor early winter growth.

17

366

Another possible reason for underestimation of early season C dynamics may be a lack of

367

energy gain at night. S. latissima’s carbon dioxide exchange rate is not closely correlated with

368

irradiance because carbon dioxide uptake by the alga continues into the dark (Mortensen, 2017).

369

On average, 11% of S. latissima’s carbon fixation happens in the dark (Kremer and Markham,

370

1979). The linkage between the light-dependent and light-independent reactions is modeled in

371

our study as an immediate transference. In other words, when there is no irradiance input, the

372

assimilation of carbohydrates to the C reserve is zero. However, adding this layer of

373

physiological accuracy could reduce model efficiency without increasing predictive capacity.

374

 In some instances, N was the limiting factor to growth, as shown by more rejected C by

375

the growth SU, for example, in Pt. Judith Pond sites in Dec and Jan of year 1, resulting in lower

376

predicted length as compared to field observations. The low resolution of N forcing could limit

377

our interpretation of the results, but our N data show general agreement with long-term

378

monitoring at the University of Rhode Island Graduate School of Oceanography (Reed and

379

Oviatt, 2020). The seasonal dynamics of N in Narragansett Bay matches that of many sites

380

around New England with higher concentrations of N in the October-March and reduced summer

381

N concentrations (Townsend 1991, Reed and Oviatt, 2020). Nitrogen has been well-documented

382

as a major force limiting primary production across the ocean (Duce et al., 2008). N limitation of

383

S. latissima growth may be a reasonable expectation later in the year as inorganic N availability

384

is thought to facilitate late winter and early spring S. latissima growth (Ahn et al., 1998).

385

To increase the ability to accurately understand growth limitation with this DEB model,

386

localized N uptake data in response to changing N concentrations would be useful. Ecotypic

387

differences in N nutrition have been observed both in Nova Scotia (Canada, Espinoza and

388

Chapman, 1983) and when comparing Long Island Sound (New York) kelps with kelps from

18

389

Maine (Gerard, 1997). In this study, Espinoza and Chapman’s (1983) N uptake data from St.

390

Margaret’s Bay was chosen for calibration over their Bay of Fundy data because the April-

391

November seasonal depletion of nitrate was more similar to Narragansett Bay conditions than the

392

year-round nitrate replete conditions of the Bay of Fundy. Kelp individuals from St. Margaret’s

393

Bay also had greater nitrate accumulation ability (Espinoza and Chapman, 1983). The seasonal

394

dissolved inorganic nitrogen patterns were comparable for the Long Island Sound and Maine

395

kelps that Gerard (1997) analyzed, but the Long Island Sound plants (geographically closer to

396

our kelp from Narragansett Bay) accumulated larger N reserves, which allowed for a ramping up

397

of photosynthetic component production. Such ability to store nitrogen over winter months has

398

been documented (Nielsen et al., 2014) and may explain the observed pattern of C reserve

399

limitation in our model. Year-long simulations would most likely provide different conclusions

400

when N availability in the environment decreases (Reed and Oviatt, 2020).

401

The chemical composition of available N for assimilation may have an effect on N

402

limitation. Nitrate was the primary N source used in this model primarily due to lack of complete

403

ammonium data to include in the forcing. Including ammonium, however, may allow for more

404

accurate predictions of growth dynamics as ammonium has been hypothesized to be a more

405

efficient N source for macroalgae especially in low light conditions because it may be

406

assimilated passively through diffusion (Harrison and Hurd, 2001). One argument for leaving out

407

ammonium is to simplify dynamics, as a different substrate composition would require another

408

reserve pool, although pools of different N forms may be combined and uptake rates for different

409

N sources averaged. Another reason is that S. latissima has been shown to have a higher

410

maximum uptake of nitrate compared to ammonium: ammonium saturation was observed at

411

concentrations of 10 μM whereas nitrate saturation was not observed until 30 μM (Ahn et al.,

19

412

1998). The greater variation in nitrate uptake could cause nitrate to have a more important role in

413

shaping S. latissima growth dynamics. The caveat to using these rates to understand dynamics

414

broadly is that kelp individuals used in this study came from ammonium rich and nitrate poor

415

habitat (Ahn et al., 1998), which may have some effect on the reported uptake rates.

416

417

4.2 Sensitivity Analysis

418

The high sensitivity of the state variables to the temperature related parameters is a

419

logical outcome of the central role of temperature in DEB theory. Since the temperature

420

correction is applied to such a large number of rates in the organism, the high sensitivity to these

421

values is reasonable. It is also an argument for caution in regional calibration of the Arrhenius

422

relationship. The sensitivity of the S. latissima model to the fraction of rejection flux

423

incorporated back in i-reserve (

) contrasts with the lack of sensitivity of Lorena et al. (2010)’s

424

microalgae model to the same parameter. Different metabolic pathways, storage capacities, and

B(cid:4)C

425

efficiencies might be responsible for these differences between a phytoplankton species and a

426

macroalgae. More experimental work focusing on the dynamics of internal and external N

427

concentration in controlled settings should help confirm the calibration of this parameter. The

428

sensitivity of the model to the yield factor of C reserve on photons and on CO2 (

 and

ADEFD
respectively), reflects the generality of photosynthesis reactions; a change in these parameters

A(cid:23)D

429

430

would involve important modifications of the physiological processes involved in

431

photosynthesis. Since these processes are well known and established, it reinforces our

432

confidence in the model. The high sensitivity of the model to the yield factor of C reserve to

433

structure (

 in comparison to the small but nonzero impact of the yield factor of N reserve to

434

structure (

) might be reflective of the greater amount of C reserve required by the chemical

A(cid:4)(cid:6)(cid:2))

A(cid:4)(cid:5)(cid:2)

20

435

composition of the structure. This greater proportion of C may also be the reason the majority of

436

the impactful parameters are related to C dynamics. The state variables had a small sensitivity to

437

reserve turnover parameters, which calibration may be challenging due to the difficulty to relate

438

these abstract parameters to observed data. It is, therefore, encouraging that the sensitivity to

439

these values was low. This analysis should increase our overall confidence in the values of the

440

calibrated parameters and the reliability of the model as the most sensitive parameters are those

441

in which we can have highest assurance.

442

443

4.3  Model Application

444

Limitations to broader geographic use of this parameter set center around the plasticity of

445

S. latissima and the existence of ecotypes in this species. The differentiation of ecotypes occurs

446

when individuals have an acclimation range related to their habitat of origin (Gerard, 1988). For

447

instance, S. latissima individuals from New York have been shown to have a different

448

physiological response to temperature in a lab setting than individuals from Maine (Gerard,

449

1988). In the context of this study, Narragansett Bay (RI, U.S.A.) is located towards the southern

450

boundary of S. latissima distribution range (Taylor, 1972); kelps from this location likely have

451

different physiological rates than in northern neighboring states. The existence of multiple

452

ecotypes of this species suggests that some parameters, such as the temperature parameters or

453

maximum assimilation rates of substrates, require regional adjustment, particularly in the Arctic.

454

Additionally, the model assumption regarding the proportionality of surface area to volume

455

impedes prediction of blade shape plasticity, which is a characteristic of S. latissima related to

456

drag (Buck and Buchholz, 2005). Since the blade thickness and amount of blade ruffling could

457

impact the relationship between surface area and volume, some adjustments to the model may be

21

458

warranted in regions where blade plasticity results in thicker thalli as the surface area to volume

459

relationship would be impacted. Determining a mechanism for how blade type changes in

460

response to hydrodynamic conditions would provide a clearer picture of overall growth

461

dynamics.

462

Further research on the mechanisms for frond loss, blade plasticity, and regional

463

parameter information have the potential to improve this DEB model. A better understanding of

464

the physiological cause for apical frond loss would allow this process to be included in

465

mechanistic models in a more meaningful way than modeling erosion as a response to one

466

correlated variable such as length or age. Aging mechanisms within DEB theory (Kooijman,

467

2010), based on the production of harmful compounds may also be of interest to model frond

468

loss. Finally, underwater carbon dioxide uptake data and more regionally appropriate oxygen

469

production data in response to variable irradiance would be useful to better calibrate parameters

470

linked to S. latissima photosynthesis.

471

Our model establishes a baseline for S. latissima DEB parameters and further testing of

472

the model equations from Lavaud et al. (2020). This tool facilitates analyzing local growth

473

limitations as they relate to modeled responses to changing environmental conditions. Our S.

474

latissima DEB model is a first step towards estimating kelp aquaculture production in the U.S.A.

475

In future work, this S. latissima DEB model could be coupled with a DEB model for C. virginica

476

(Lavaud et al., 2017) and the Regional Ocean Modeling System (ROMS) with a Carbon Silicate

477

Nitrogen Ecosystem (CoSiNE) model (Chai et al, 2009) to predict growth potential at sites in the

478

Northeastern U.S.A. Supporting macroalgae aquaculture is an important avenue to work towards

479

the vital goals of feeding a growing human population and while combatting climate change.

480

22

481

482

Acknowledgements

483

This study would not have been possible without the valuable contributions of the aquaculture

484

farmers working with us to grow kelp for two years: Cindy and John West of Moonstone

485

Oysters, Russ and Thomas Blank of Rome Point Oyster Farm, Trip Whilden of Wickford Oyster

486

Co, and Perry Russo of Matunuck Oyster Farm. Dave Ullman and Chris Kincaid provided

487

assistance in the initial project development. Thomas Guyondet facilitated collaborations around

488

this project. Dawn Outram at the Marine Science Research Facility at URI’s Narragansett Bay

489

Campus and Kelly Addy conducted water analyses. Candace Oviatt and Laura Reed shared their

490

nitrogen data, which is funded by EPA, NOAA-CHRP and RI DEM. T. Ben-Horin provided

491

assistance collecting reproductive kelp. J. Barnes, A. Barry, R. Derouin, E. Ferrante, I. Gray, K.

492

Hannibal, C. Jenkins, A. Mauk, L. Sebesta, and A. Wetzel provided lab and field assistance. S.

493

McWilliams, D. Ullman, M. Gomez-Chiarri, L. Josephs, and K. Gorospe provided feedback on

494

previous versions of the manuscript.

495

496

Funding: This work is supported by the National Oceanic and Atmospheric Administration

497

Saltonstall-Kennedy grant [17GAR008], NSERC grant [497065-2016], the National Science

498

Foundation under EPSCoR Cooperative Agreement #OIA-165522 and the U.S. Department of

499

Agriculture’s National Institute of Food and Agriculture, Hatch Formula project 1011478.

500

23

501

References

502

Ahn, O., Petrell, R. J., & Harrison, P. J. (1998). Ammonium and nitrate uptake by Laminaria

503

saccharina and Nereocystis luetkeana originating from a salmon sea cage farm. Journal of

504

Applied Phycology, 10(4), 333-340.

505

Alleway, H. K., Gillies, C. L., Bishop, M. J., Gentry, R. R., Theuerkauf, S. J., & Jones, R.

506

(2019). The ecosystem services of marine aquaculture: Valuing benefits to people and nature.

507

BioScience, 69(1), 59-68.

508

Axelsson, L., Mercado, J., & Figueroa, F. (2000). Utilization of HCO3

− at high pH by the brown

509

macroalga Laminaria saccharina. European Journal of Phycology, 35(1), 53-59.

510

Boden, G. T. (1979). The effect of depth on summer growth of Laminaria saccharina

511

(Phaeophyta, Laminariales). Phycologia, 18(4), 405-408.

512

Bolton, J. J., & Lüning, K. (1982). Optimal growth and maximal survival temperatures of

513

Atlantic Laminaria species (Phaeophyta) in culture. Marine Biology, 66(1), 89-94.

514

Brady-Campbell, M. M., Campbell, D. B., & Harlin, M. M. (1984). Productivity of kelp

515

(Laminaria spp.) near the southern limit in the northwestern Atlantic Ocean. Marine Ecology

516

Progress Series, 18(1), 79-88.

517

Broch, O. J., & Slagstad, D. (2012). Modelling seasonal growth and composition of the kelp

518

Saccharina latissima. Journal of Applied Phycology, 24(4), 759-776.

519

Brown, M. T., Nyman, M. A., Keogh, J. A., & Chin, N. K. M. (1997). Seasonal growth of the

520

giant kelp Macrocystis pyrifera in New Zealand. Marine Biology, 129(3), 417-424.

521

Buchholz, C., & Lüning, K. (1999). Isolated, distal blade discs of the brown alga Laminaria

522

digitata form sorus, but not discs, near to the meristematic transition zone. Journal of Applied

523

Phycology, 11(6), 579.

24

524

Buck, B. H., & Buchholz, C. M. (2005). Response of offshore cultivated Laminaria saccharina

525

to hydrodynamic forcing in the North Sea. Aquaculture, 250(3-4), 674-691.

526

Chai, F., G. Liu, H. Xue, L. Shi, Y. Chao, C.-M. Tseng, W.-C. Chou, and K.-K. Liu (2009).

527

Seasonal and interannual variability of carbon cycle in South China Sea: A three-dimensional

528

physical-biogeochemical modeling study, Journal of Oceanography, 65, 703-720.

529

Cho, C. Y., & Bureau, D. P. (1998). Development of bioenergetic models and the Fish-PrFEQ

530

software to estimate production, feeding ration and waste output in aquaculture. Aquatic Living

531

Resources, 11(4), 199-210.

532

Dame, R. F. (1972). The ecological energies of growth, respiration and assimilation in the

533

intertidal American oyster Crassostrea virginica. Marine biology, 17(3), 243-250.

534

Davison, I. R. (1987). Adaptation of photosynthesis in Laminaria saccharina (Phaeophyta) to

535

changes in growth temperature. Journal of Phycology, 23, 273-283.

536

Davison, I. R., & Davison, J. O. (1987). The effect of growth temperature on enzyme activities in

537

the brown alga Laminaria saccharina. British Phycological Journal, 22(1), 77-87.

538

Denny, M., & Helmuth, B. (2009). Confronting the physiological bottleneck: a challenge from

539

ecomechanics. Integrative and Comparative Biology, 49(3), 197-201.

540

Duarte, C. M., Wu, J., Xiao, X., Bruhn, A., & Krause-Jensen, D. (2017). Can seaweed farming

541

play a role in climate change mitigation and adaptation? Frontiers in Marine Science, 4, 100.

542

Duce, R. A., LaRoche, J., Altieri, K., Arrigo, K. R., Baker, A. R., Capone, D. G., ... & Geider, R.

543

J. (2008). Impacts of atmospheric anthropogenic nitrogen on the open ocean. science, 320(5878),

544

893-897.

545

Eaton, A. D., Clesceri L. S., Greenberg A. E., & Franson M. H. (1998) Standard methods for the

546

examination of water and wastewater. APHA, AWWA, and WEF, Washington, DC.

25

547

Espinoza, J., & Chapman, A. R. O. (1983). Ecotypic differentiation of Laminaria longicruris in

548

relation to seawater nitrate concentration. Marine Biology, 74(2), 213-218.

549

FAO. 2018. The State of World Fisheries and Aquaculture 2018 - Meeting the sustainable

550

development goals. Rome. Licence: CC BY-NC-SA 3.0 IGO.

551

Filgueira, R., Guyondet, T., Comeau, L. A., & Grant, J. (2014). A fully-spatial ecosystem-DEB

552

model of oyster (Crassostrea virginica) carrying capacity in the Richibucto Estuary, Eastern

553

Canada. Journal of Marine Systems, 136, 42-54.

554

Forbord, S., Skjermo, J., Arff, J., Handå, A., Reitan, K. I., Bjerregaard, R., & Lüning, K. (2012).

555

Development of Saccharina latissima (Phaeophyceae) kelp hatcheries with year-round

556

production of zoospores and juvenile sporophytes on culture ropes for kelp aquaculture. Journal

557

of Applied Phycology, 24(3), 393-399.

558

Fortes, M. D., & Lüning, K. (1980). Growth rates of North Sea macroalgae in relation to

559

temperature, irradiance and photoperiod. Helgoländer Meeresuntersuchungen, 34(1), 15.

560

Froehlich, H. E., Afflerbach, J. C., Frazier, M., & Halpern, B. S. (2019). Blue Growth Potential

561

to Mitigate Climate Change through Seaweed Offsetting. Current Biology, 29, 1-7.

562

Gagné, J. A., Mann, K. H., & Chapman, A. R. O. (1982). Seasonal patterns of growth and

563

storage in Laminaria longicruris in relation to differing patterns of availability of nitrogen in the

564

water. Marine Biology, 69(1), 91-101.

565

Gevaert, F., Davoult, D., Creach, A., Kling, R., Janquin, M. A., Seuront, L., & Lemoine, Y.

566

(2001). Carbon and nitrogen content of Laminaria saccharina in the eastern English Channel:

567

biometrics and seasonal variations. Journal of the Marine Biological Association of the United

568

Kingdom, 81(5), 727-734.

26

569

Gerard, V. A. (1988). Ecotypic differentiation in light-related traits of the kelp Laminaria

570

saccharina. Marine Biology, 97(1), 25-36.

571

Gerard, V. A. (1997). The role of nitrogen nutrition in high‐temperature tolerance of the kelp,

572

Laminaria saccharina (Chromophyta). Journal of Phycology, 33(5), 800-810.

573

Grant, J., Curran, K. J., Guyondet, T. L., Tita, G., Bacher, C., Koutitonsky, V., & Dowd, M.

574

(2007). A box model of carrying capacity for suspended mussel aquaculture in Lagune de la

575

Grande-Entrée, Iles-de-la-Madeleine, Québec. Ecological modelling, 200(1-2), 193-206.

576

Handå, A., Forbord, S., Wang, X., Broch, O. J., Dahle, S. W., Størseth, T. R., ... & Skjermo, J.

577

(2013). Seasonal-and depth-dependent growth of cultivated kelp (Saccharina latissima) in close

578

proximity to salmon (Salmo salar) aquaculture in Norway. Aquaculture, 414, 191-201.

579

Harrison, P. J., & Hurd, C. L. (2001). Nutrient physiology of seaweeds: application of concepts

580

to aquaculture. Cahiers de biologie marine, 42(1-2), 71-82.

581

Heinrich, S., Valentin, K., Frickenhaus, S., John, U., & Wiencke, C. (2012). Transcriptomic

582

analysis of acclimation to temperature and light stress in Saccharina latissima (Phaeophyceae).

583

PLoS One, 7(8), e44342.

584

Herbeck, L.S., Unger, D., Wu, Y., & Jennerjahn, T.C., (2013). Effluent, nutrient and organic

585

matter export from shrimp and fish ponds causing eutrophication in coastal and back-reef waters

586

of NE Hainan, tropical China. Continental Shelf Research 57, 92–104.

587

Johansson, G., & Snoeijs, P. (2002). Macroalgal photosynthetic responses to light in relation to

588

thallus morphology and depth zonation. Marine Ecology Progress Series, 244, 63-72.

589

Kain, J. M. (1989). The seasons in the subtidal. British Phycological Journal, 24(3), 203-215.

590

Kooijman, S. A. L. M. (2010). Dynamic energy budget theory for metabolic organisation.

591

Cambridge university press.

27

592

Kremer, B. P., & Markham, J. W. (1979). Carbon assimilation by different developmental stages

593

of Laminaria saccharina. Planta, 144(5), 497-501.

594

Krumhansl, K. A., Lauzon-Guay, J. S., & Scheibling, R. E. (2014). Modeling effects of climate

595

change and phase shifts on detrital production of a kelp bed. Ecology, 95(3), 763-774.

596

LACHAT (2008). QuikChem Method 31-107-04-1-A. LACHAT INSTRUMENTS, Loveland,

597

CO.

598

Lavaud, R., La Peyre, M. K., Casas, S. M., Bacher, C., & La Peyre, J. F. (2017). Integrating the

599

effects of salinity on the physiology of the eastern oyster, Crassostrea virginica, in the northern

600

Gulf of Mexico through a Dynamic Energy Budget model. Ecological Modelling, 363, 221-233.

601

Lavaud, R., Filgueira, R., Nadeau, A., Steeves, L., & Guyondet, T. (2020). A Dynamic Energy

602

Budget model for the macroalga Ulva lactuca. Ecological modelling, 418, 108922.

603

Livanou, E., Lagaria, A., Psarra, S., & Lika, K. (2019). A DEB-based approach of modeling

604

dissolved organic matter release by phytoplankton. Journal of sea research, 143, 140-151.

605

Lorena, A., Marques, G. M., Kooijman, S. A. L. M., & Sousa, T. (2010). Stylized facts in

606

microalgal growth: interpretation in a dynamic energy budget context. Philosophical

607

Transactions of the Royal Society B: Biological Sciences, 365(1557), 3509-3521.

608

Lüning, K., Wagner, A., & Buchholz, C. (2000). Evidence for inhibitors of sporangium

609

formation in Laminaria digitata (Phaeophyceae) during the season of rapid growth. Journal of

610

Phycology, 36(6), 1129-1134.

611

Mesinger, F., G. DiMego, E. Kalnay, K. Mitchell, and Coauthors, 2006: North American

612

Regional Reanalysis. Bulletin of the American Meteorological Society, 87, 343–360.

28

613

Mortensen, L. M. (2017). Diurnal carbon dioxide exchange rates of Saccharina latissima and

614

Laminaria digitata as affected by salinity levels in Norwegian fjords. Journal of Applied

615

Phycology, 29(6), 3067-3075.

616

Mõttus, Matti & Sulev, Madis & Frederic, Baret & Lopez-Lozano, R. & Reinart, Anu. (2011).

617

Photosynthetically Active Radiation: Measurement and Modeling. In R. Meyers (Ed.),

618

Encyclopedia of Sustainability Science and Technology (pp. 7970-8000). New York, NY:

619

Springer.

620

Muller, E. B., & Nisbet, R. M. (2014). Dynamic energy budget modeling reveals the potential of

621

future growth and calcification for the coccolithophore E miliania huxleyi in an acidified ocean.

622

Global change biology, 20(6), 2031-2038.

623

National Marine Fisheries Service (2018) Fisheries of the United States, 2017. U.S. Department

624

of Commerce, NOAA Current Fishery Statistics No. 2017 Available at:

625

https://www.fisheries.noaa.gov/feature-story/ fisheries-united-states-2017

626

Ní Longphuirt, S., Eschmann, C., Russell, C., & Stengel, D. B. (2013). Seasonal and species-

627

specific response of five brown macroalgae to high atmospheric CO2. Marine Ecology Progress

628

Series, 493, 91-102.

629

Nielsen, M.M., Krause-Jensen, D., Olesen, B., Thinggaard, R., Christensen, P.B. and Bruhn, A.,

630

(2014). Growth dynamics of Saccharina latissima (Laminariales, Phaeophyceae) in Aarhus Bay,

631

Denmark, and along the species’ distribution range. Marine biology, 161(9), 2011-2022.

632

Petrell, R. J., Tabrizi, K. M., Harrison, P. J., & Druehl, L. D. (1993). Mathematical model of

633

Laminaria production near a British Columbian salmon sea cage farm. Journal of Applied

634

Phycology, 5(1), 1-14.

29

635

Poggiale, J. C., Baklouti, M., Queguiner, B., & Kooijman, S. A. L. M. (2010). How far details

636

are important in ecosystem modelling: the case of multi-limiting nutrients in phytoplankton–

637

zooplankton interactions. Philosophical Transactions of the Royal Society of London B:

638

Biological Sciences, 365(1557), 3495-3507.

639

Raven, J. A., Ball, L. A., Beardall, J., Giordano, M., & Maberly, S. C. (2005). Algae lacking

640

carbon-concentrating mechanisms. Canadian Journal of Botany, 83(7), 879-890.

641

R Core Team (2019). R: A language and environment for statistical computing. R Foundation for

642

Statistical Computing, Vienna, Austria. URL https://www.R-project.org/.

643

Redmond, S., L.A. Green, C. Yarish, J. Kim, & C.D. Neefus. 2014. New England seaweed

644

culture handbook: nursery systems. Connecticut Sea Grant College Program. CTSG-14-01. 92

645

pp. Available at: https://seagrant.uconn.edu/2014/01/01/new-england-seaweed-culture-

646

handbook-nursery-systems/

647

[dataset] Reed, Laura and Candace Oviatt. 2020. Graduate School of Oceanography Dock Data,

648

1977 to Present.

649

Ren, J. S., Stenton-Dozey, J., Plew, D. R., Fang, J., & Gall, M. (2012). An ecosystem model for

650

optimising production in integrated multitrophic aquaculture systems. Ecological Modelling,

651

246, 34-46.

652

Schaffelke, B., & Lüning, K. (1994). A circannual rhythm controls seasonal growth in the kelps

653

Laminaria hyperborea and L. digitata from Helgoland (North Sea). European Journal of

654

Phycology, 29(1), 49-56.

655

Schiener, P., Black, K. D., Stanley, M. S., & Green, D. H. (2015). The seasonal variation in the

656

chemical composition of the kelp species Laminaria digitata, Laminaria hyperborea, Saccharina

657

latissima and Alaria esculenta. Journal of Applied Phycology, 27(1), 363-373.

30

658

Segarra, K. E. A. 2002. Source Or Sink? Analysis of Narragansett Bay's carbon cycle. Brown

659

University. Center for Environmental Studies.

660

Sjøtun, K. (1993). Seasonal lamina growth in two age groups of Laminaria saccharina (L.)

661

Lamour. in western Norway. Botanica marina, 36(5), 433-442.

662

Soetaert, K., & Petzoldt, T. (2010). Inverse modelling, sensitivity and Monte Carlo analysis in R

663

using package FME. Journal of Statistical Software, 33(3), 1-28.

664

Soetaert, K., Petzoldt, T. R., & Setzer, W. (2010). Solving Differential Equations in R: Package

665

deSolve. Journal of Statistical Software, 33(9), 1-25. URL http://www.jstatsoft.org/v33/i09/ DOI

666

10.18637/jss.v033.i09

667

Taylor, W. R. (1972). Marine algae of the eastern tropical and subtropical coasts of the

668

Americas. University of Michigan.

669

Townsend, D. W. (1991). Influences of oceanographic processes on the biological productivity

670

of the Gulf of Maine. Reviews in Aquatic Sciences, 5(3), 211-230.

671

Ullman, D. S. & Codiga, D. L. (2010) Characterizing the Physical Oceanography

672

of Coastal Waters Off Rhode Island, Part 2: New Observations of Water Properties, Currents,

673

and Waves. Retrieved from https://www.seagrant.gso.uri.edu/oceansamp/pdf/appendix/03-

674

PhysOcPart2-OSAMP-UllmanCodiga2010.pdf

675

Vettori, D., & Nikora, V. (2017). Morphological and mechanical properties of blades of

676

Saccharina latissima. Estuarine, Coastal and Shelf Science, 196, 1-9.

677

Wu, R. S. S. (1995). The environmental impact of marine fish culture: towards a sustainable

678

future. Marine Pollution Bulletin, 31(4-12), 159-166.

31

679

Tables

680

Table 1. Model equations with environmental conditions: T = temperature (K), I = irradiance

681

(mol γ m–2 h–1), DIC = dissolved inorganic carbon (mol DIC L–1), and N = nitrate and nitrite

682

concentration (NO3

– and NO2

– L–1).

Equation

Description

IJ =  KLM N

JO
JP Q

JO
J R ST U KLM N

JOV
JP Q

JOV
JV R U KLM N

JOW
JW Q

JOW
JP RX ST U

Temperature correction

KLM N

JOV
J Q

JOV
JV R U  KLM N

JOW
JW Q

JOW
J RX

*T

YZ[O = YZ[O\IJ

][^
][^ U _[

YI‘a   =   YI‘a\IJ

]bcI^
]bcI^ U _I

Yc =

defgch(cid:12) cic
ch(cid:12) cic
j(cid:12) cIJ

T U

Y‘a =

kl
 m

YcnV‘ao‘a

YZIO = p

T
YZIO\IJ

U

T
YI‘a/nI‘aI

U

T
Yc/ncI

Q

T
Yc/ncI U YI‘a/nI‘aI

*T
r

YZsI = \Zstj(cid:12) ZsIJ Q u(cid:12) v

u(cid:12) =

T
kl

wkl
wx

ks
YZs

  = yz{ tYZsI, YZskIJv

ks
YZs| =  YZsI Q YZs

ks
If     YZs

(cid:127)   YZskIJ

k
Yl

ks
= (cid:128) Yls
s

ks
= (cid:128) SNYZskIJ Q YZs

RnZsl

*T

X

s

32

Specific assimilation rate of N

Specific CO2 uptake rate from

photosynthetic SU1

Specific relaxation rate from photosynthetic

SU2

Oxygen production rate

Specific assimilation rate of C from

photosynthetic SU3

Specific catabolic flux of N or C reserve

Net specific growth rate

Specific maintenance flux from N or C

reserve

Specific growth flux from N or C reserve

Specific maintenance flux from structure

Yl| = (cid:129)(cid:128) p

s

YZs|
nZsl

*T

r

Q (cid:130)(cid:128)

s

YZs|
nZsl

*T

*T

(cid:131)

(cid:132)

k
= u(cid:12) U Yl

Gross specific growth rate

Specific flux of rejected C or N from growth

YZs(cid:133) = YZs| Q nZsl Yl|

SU

w
wx

w
wx

\Zs =   YZsO Q YZsI U (cid:134)ZsYZs(cid:133) Q   u(cid:12)  \Zs

kl = u(cid:12) kl

mw =(ol U \ZIoZI U \Z[oZ[)kl

T
T.(cid:141)(cid:142)(cid:143)

Vo = (cid:135)

mw
(cid:136). (cid:138)(cid:139) TP

*(cid:136)(cid:140)

683

Dynamics of the N or C reserve

Dynamics of structural mass

Whole S. latissima blade dry weight

Physical length

684

Table 2. S. latissima DEB model parameters and units resulting from fitting the model to the

685

compiled literature and field data.

Parameter  Parameter description

Parameter Units

Value

Source

Maximum volume specific

mol N mol V–1 h–1

1.5 * 10–

Fitted from data by Espinoza

nitrogen assimilation

4

and Chapman (1983)

Half-saturation concentration

mol NO3

– and NO2

– L–1

2.5 * 10–

Fitted from data by Espinoza

for NO3

– and NO2

– uptake

6

and Chapman (1983)

Maximum volume specific

mol CO2 mol V–1 h–1

0.0075

This study

CO2 uptake rate

Half-saturation concentration

mol CO2 L–1

4 * 10–7

This study

for CO2 uptake

Photosynthetic unit (PSU)

mol PSU mol V–1

0.5

Fitted from data by

density

Johansson and Snoeijs

(2002)

Binding probability of a photon

-

0.5

Fitted from data by

(cid:144)(cid:12)Z[O\

_[

YI‘a\

_I

defg

h(cid:12) c

33

to a free light SU

Johansson and Snoeijs

(2002)

Specific photon arrival cross

m2 mol PSU–1

1

Fitted from data by

section

Johansson and Snoeijs

(2002)

Dissociation rate of

mol γ mol PSU–1 h–1

0.075

Fitted from data by

photosynthetic products

Johansson and Snoeijs

(2002)

Yield of C reserve per photon   mol γ mol C–1

Yield of C reserve per CO2

mol CO2 mol C–1

10

1

Lavaud et al. (2020)

Lavaud et al. (2020)

Yield factor of photon to O2

mol O2 mol γ –1

0.125

Lavaud et al. (2020)

Maximum volume specific

mol C mol V–1 h–1

0.282

This study

carbon assimilation

N reserve turnover rate

C reserve turnover rate

h–1

h–1

0.04

Lavaud et al. (2020)

0.02

Lavaud et al. (2020)

Volume specific maintenance

mol N mol V–1 h–1

4 * 10–6

This study

cost paid by N reserve

Volume specific maintenance

mol C mol V–1 h–1

1 * 10–6

This study

cost paid by C reserve

Yield factor of N reserve to

mol N mol V–1

0.04

Lorena et al. (2010)

structure

Yield factor of C reserve to

mol C mol V–1

1

This study

structure

Fraction of rejection flux

-

0.9

This study

incorporated back in i-reserve

Arrhenius temperature

Reference temperature

K

K

6314.3

This study

293.15

This study

ic

j(cid:12) c

ncI

nI‘aI

nV‘a

YZIO\

j(cid:12) Z[

j(cid:12) ZI

YZ[k

YZIk

nZ[l

nZIl

(cid:134)Zs

JO

JP

34

Upper boundary of temperature

K

286.536

This study

tolerance

Lower boundary of

K

273.15

This study

temperature tolerance

Arrhenius temperature outside

K

18702

This study

TH

Arrhenius temperature outside

K

4391.9

This study

TL

Molar weight of structure

g mol V –1

29.89

C:H:O:N; 1: 1.33:1:0.04

Molar weight of C reserve

g C mol C–1

Molar weight of N reserve

g N mol N–1

Molar weight of O2

g O2 mol O2

–1

54

17

32

C:H:O:N; 1:2:1:0

C:H:O:N; 0:0:2.5:1

Periodic table

JW

JV

JOW

JOV

ol

oZI

oZ[

o‘a

686

687

Table 3. Data from literature and this study used to calibrate the S. latissima DEB model.

Reference

Location

Data

Experimental conditions

Time period

Espinoza and

Chapman (1983)

Johansson and Snoeijs

(2002)

*Davison (1987)

T = 9 and 18 °C

Discrete

[N] = from 2.5 to 88 * 10–6 M

measurements

Nova

Scotia,

Canada

NO3– uptake

(µg N gDW

–1 h–1)

Measured O2

NO3–

T = 14 °C

Discrete

measurements

Sweden

evolution (µmol

I = 0-900 µE m–2 s–1

O2 kg DW-1 s-1)

Photosynthesis

Germany

rates (µmol C

gWW

–1 h–1)

Specific growth

T = 0-30 °C with 5 °C intervals

Discrete

I = 200 µE m–2 s–1

measurements

*Fortes and Lüning

(1980)

Germany

rate

(% d–1)

T = 0, 5, 10, 15, and 20 °C

I = 70 µE m–2 s–1

7 days

35

Germany,

UK,

Specific growth

*Bolton and Lüning

T° = 0, 5, 10, 15, 20, and 23 °C

(1982)

France,

rate

and

(% d–1)

Norway

Relative growth

I = 50 µE m–2 s–1

7 days

*Davison and Davison

T = 0, 5, 10, 15 and 20 °C

Germany

rate

1 month

(1987)

(cm cm–1 month–1)

I = 60 µE m–2 s–1

T = 1.5-20 °C

[N] = 0-1 * 10–5 mol NO3

– and

Rhode

Blade length (cm)

NO2

– L–1

[C] = 1.836 * 10–3 mol DIC L–1

This study

Island,

and N:C ratio (mol

138- 172 days

USA

mol–1)

at Pt. Judith Pond sites and 1.956

* 10–3 mol DIC L–1 for

Narragansett Bay sites

I = 0-2 * 106 daily µE m–2 h–1

*Used only to build the Arrhenius relationship.

688

689

690

Table 4. Length of S. latissima blades in cm (± SD) at the end of the growing season in each site.

Site

Year 1

Year 2

Narragansett Bay North

67.9 (± 22.6)

50.5 (± 13.0)

Narragansett Bay South, Line 1

133.4 (± 78.8)

65.3 (± 22.5)

Narragansett Bay South, Line 2

73.2 (± 17.6)

20.0 (± 6.8)

Pt. Judith Pond North, Line 1

74.8 (± 18.3)

80.1 (± 23.1)

Pt. Judith Pond North, Line 2

81.0 (± 34.8)

46.9 (± 14.7)

Pt. Judith Pond South, Line 1

85.9 (± 37.1)

63.8 (± 26.3)

Pt. Judith Pond South, Line 2

87.3 (± 32.0)

47.1 (± 10.9)

36

691

Figures

692
693

Figure 1. S. latissima DEB model conceptual framework (adapted from Lavaud et al., 2020).

694

The large oval represents the algae and the surrounding area is its environment. Grey rounded

695

rectangles are the model forcing variables. White rectangles are the state variables of the model,

696

representing the main pools of mass in the modeled organism. Circles are synthesizing units,

697

processing key metabolic transformations. Dotted arrows represent fluxes of mass leaving the

698

main model system either through excretion or use in maintenance. Grey arrows depict where the

699

temperature correction is applied to a reaction.

37

Rhode Island

N

Atlantic Ocean

Point Judith Pond

700

&1º38'W

71º30'W

71º22'W

71º14'W

41º42'N

41º38'N

41º34'N

41º30'N

41º26'N

701

Figure 2. Map of growing sites (triangles) for S. latissima on Rhode Island oyster farms.

a)

)
1
–
h
2
–

m

γ
l
o
m

(

e
c
n
a
d
a
r
r
I

i

4

3

2

1

0

b)

4

3

2

1

0

702

N D J F M A M

N D J F M A M

703

Figure 3. Irradiance forcing used in all sites for year 1 (a) and year 2 (b) of the field study

704

converted from the radiative forcing from the North American Regional Reanalysis.

38

705

706

Figure 4. Arrhenius relationship for S. latissima estimated using multiple growth and

707

photosynthesis datasets from: Bolton and Lüning (1982; squares; orange for kelp from France,

708

yellow for Norway, purple for Germany, green for the UK), Fortes and Lüning (1980; blue

709

diamonds), Davison and Davison (1987; red asterisk), and Davison (1987 circles; blue for

710

sporophytes rearing temp 0 °C, orange for 5 °C, yellow for 10 °C, purple for 15 °C, and green

711

for 20 °C). The adjusted R-squared statistic for the fit of the curve to the data points is 0.551 (p-

712

value = 2.74 10–11).

39

713

714

Figure 5. Predicted (lines) and observed (points) a) N uptake from Espinoza and Chapman

715

(1983) at 9 °C (black circles) and 18 °C (grey diamonds) and b) Oxygen production from

716

Johansson and Snoeijs (2002).

40

717

718

Figure 6. Measured temperature (°C; a,b) and nitrate and nitrite concentrations (µmol L–1; c,d)

719

from year 1 (left panels) and year 2 (right panels). Narragansett Bay lines are in dark blue (North

720

site 1), purple (South site 1), and light blue (South site 2). Pt. Judith Pond lines are in orange

721

(North site 1), yellow (North site 2), brown (South site 1) and black (South site 2). Observed N

722

concentrations are indicated by black dots.

41

723

724

Figure 7. Saccharina latissima blade length (cm) during year 1 (top row) and year 2 (bottom

725

row). Dots and diamonds with error bars depict the mean observed length from the field data and

726

their standard deviation, respectively. Lines are the predicted length from the S. latissima DEB

727

model. Lines and dots in black are the first S. latissima line planted at a site, and lines and

728

diamonds in grey depict the second S. latissima line planted later in the year.

42

729

730

Figure 8. Rejected fluxes of C (a,b) and N (c,d) from the growth SU back to reserves at Pt.

731

Judith Pond in year 1 (left panels) and year 2 (right panels). Black is for the North S. latissima

732

line and the grey is for the South line on all plots.

43

r
o
t
c
a

f

n
o

i
t
c
e
r
r
o
c

e
r
u

t

a
r
e
p
m
e
T

1.50

1.25

1.00

0.75

0.50

a)

N D J F M A M

e

t

a
r

n
o

i
t

a
x
a
e
r

l

c
i
f
i
c
e
p
S

10–2
c)

)
1
–
h

1
–

V
l
o
m

γ
l
o
m

(

5

4

3

2

1

0

)
1
–
h

2
–

m

γ
l
o
m

(

e
c
n
a
d
a
r
r
I

i

)
1
–
h

1
–

V
l
o
m
C
o
m

l

(

b)

N D J F M A M

10–3
d)

4

3

2

1

0

5

4

3

2

1

0

e

t

a
r

n
o

i
t

a

l
i

i

m
s
s
a
C
c
i
f
i
c
e
p
S

733

N D J F M A M

N D J F M A M

734

Figure 9. Temperature correction factor (a), irradiance (b), specific relaxation rate from

735

photosynthetic SU2 (c) and carbon assimilation rate resulting from photosynthetic SU3 (d) at Pt.

736

Judith Pond during year 2. Black is for the North S. latissima line and the grey is for the South

737

line.

44

738

739

Figure 10. Graphic presentation of the results of the sensitivity analysis of the state variables

740

,

, and

 to model parameters as measured by the L1 sensitivity function.

\ZI

\Z[

kl

45

