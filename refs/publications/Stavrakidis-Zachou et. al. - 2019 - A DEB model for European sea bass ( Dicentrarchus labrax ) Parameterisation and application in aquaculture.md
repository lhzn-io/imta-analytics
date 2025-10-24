1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

A DEB model for European sea bass (Dicentrarchus labrax):
parameterisation and application in aquaculture

Orestis Stavrakidis-Zachoua,b, Nikos Papandroulakisa, Konstadia Likab,∗

aInstitute of Aquaculture, Hellenic Centre for Marine Research, AquaLabs, 71500 Gournes, Heraklion, Greece
bDepartment of Biology, University of Crete, 71003 Heraklion, Greece

Abstract

The framework provided by the Dynamic Energy Budget (DEB) theory allows the quantiﬁca-
tion of metabolic processes and the associated biological rates that are of interest for aquacul-
ture, such as growth and feeding. The DEB parameters were estimated for farmed European
sea bass (Dicentrarchus labrax), a species of major importance for the Mediterranean aquacul-
ture, using zero- and uni-variate literature data and achieving an overall good ﬁt. The obtained
parameter set was used to validate the model on sites representatively covering the geographic
distribution of the aquaculture activity in Greece via comparison of model predictions to ob-
servations. Inter-individual variability of farmed ﬁsh was introduced through: 1) an individual
initial weight and 2) a factor that acts as an individual-speciﬁc multiplier for some of the model
parameters and produces scatter in maximum size, and age and size at puberty. Growth of E.
sea bass was adequately predicted by the model while feeding tended to be underestimated,
particularly during the period following the summer months when warmer temperatures pro-
mote high growth rates. The results suggest robustness of the model since it is able to simulate
growth and food intake in several independent aquaculture production units, using a common
parameter set. The accuracy of growth predictions supports the applicability of the model in
variable environmental conditions in the context of climate change. Reconstruction of the feed-
ing history from growth data revealed variations in the scaled functional response ( f ), i.e., the
feeding rate as fraction of maximum possible one of an individual of a given size, through-
out the production cycle. However, model simulations with constant f result in reasonably
good predictions for growth and feeding in variable environmental conditions. Tendency of the
model to underestimate the feeding process revealed both model weaknesses associated with
higher temperatures as well as irregularities in the feeding protocols applied at the farm level.
Our work demonstrates the capacity and potential of DEB theory for further development of
tools that contribute to the assessment and improvement of feeding practices in aquaculture.

Keywords: DEB parameter estimation, interval estimates, inter-individual variability,
Dicentrarchus labrax, European sea bass, aquaculture

1. Introduction

European sea bass (Dicentrarchus labrax) is a species of high importance in aquaculture.
It was the ﬁrst non-salmonid marine ﬁsh to be commercially farmed in Europe and to date,

∗Coresponding author. Fax: +30 2810 394408
Email address: lika@uoc.gr (Konstadia Lika)

Preprint submitted to Journal of Sea Research

March 20, 2020

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

it is the most commercially important ﬁsh produced in the Mediterranean areas with Greece,
Turkey, Spain and Egypt being the biggest producers. Including Turkey, which is currently
a leading country in E. sea bass farming, the total production of the species in Europe has
increased exponentially in the last decades with production reaching 158,479 tonnes in 2015
(FEAP, 2016). However, to what extent this trend will continue and how changes such as rising
temperatures will aﬀect production remains uncertain.

Rising temperatures constitute the principal characteristic of climate change and the poten-
tial implications of this trend on ﬁsh, ﬁsheries, aquaculture and the dependent communities in
the Mediterranean as well as the rest of Europe have been recognized (Brugre, 2015; Hollowed
et al., 2013; Peck et al., 2013; Rosa et al., 2012). For E. sea bass in particular, temperature
plays an important role in growth, maturation, gonad diﬀerentiation, mortality and behaviour.
Although some traits such as protein utilization seem to be enhanced by lower temperatures
(Peres and Oliva-Teles, 1999), growth, food intake, nitrogen excretion and oxygen consump-
tion rates tend to increase with temperature, reaching maximum values at 26-27oC beyond
which point they exhibit slight decrease (Person-Le Ruyet et al., 2004). Higher temperatures
promote white muscle growth by increasing both the number and size of muscle cells, but the
eﬀect diﬀers between life stages, as shown for eleutheroembryos and larvae (Alami-Durante
et al., 2006), which indicates that acquiring information for the whole production cycle is crit-
ical. Experimental work based on the metabolic activity of E. sea bass at temperatures ranging
from 7 to 30oC, has provided insight regarding the width of the thermal window of the species
(Claireaux et al., 2006; Ozolina et al., 2016; Person-Le Ruyet et al., 2004) while it appears
that E. sea bass is able to withstand maximum critical temperatures of 33oC for short periods
(Ozolina et al., 2016) .

It is evident that despite the large volume of literature regarding the species, signiﬁcant
knowledge gaps exist with respect to its response to prolonged exposure to elevated temper-
atures as well as the thermal eﬀects on growth at both boundaries of the temperature tolerance
range. Due to the economic importance of the species it is imperative that the impact of climate
change on the future production of the species be assessed. This highlights the necessity for the
development of a model that is able to quantify changes in processes that are relevant for the
species culture, such as growth and food utilization, under various dietary and environmental
regimes throughout the production cycle.

In ﬁnﬁsh aquaculture, various modelling approaches have been used to describe growth.
Traditionally, empirical models have been used to study aquaculture production due to their
simplicity and their ability to link environmental parameters to state variables using relatively
small sets of data without representing the underlying biological processes (Lupatsch et al.,
2001; Tveters and Tveters, 2010). Classical bioenergetic models have also been extensively
used and they are characterized by intermediate complexity while identifying and estimating
a small number of key parameters based on data such as growth and respiration (Libralato
and Solidoro, 2008; Piedecausa et al., 2010). Typically, “classical” bioenergetic models use
one state variable to characterize the state of an individual, they are parameter-rich, they do
not capture the full cycle of the individual in a single modeling framework and they require
additional assumptions to relate parameters for diﬀerent species (Nisbet et al., 2012). Dynamic
Energy Budget (DEB) theory on the other hand, is a theory that provides the conceptual and
quantitative framework to study the whole life cycle of an individual while making explicit use
of energy and mass balances (Kooijman, 2010a). Its applicability in studying growth, feeding or
the eﬀects of phenomena like climate change lies in its capacity to capture metabolic processes
as a function of temperature and food availability in a dynamic way for the entire life cycle
2

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

of the species in question. DEB models have been successfully used in aquaculture to study
bivalves (Guyondet et al., 2010; Sar´a et al., 2012) and ﬁsh such as the Atlantic salmon (Salmo
salar) (Fore et al., 2016), the blueﬁn tuna (Thunnus orientalis) (Jusup et al., 2011) the white
seabream (Diplodus sargus) and the gilthead seabream (Sparus aurata) (Serpa et al., 2013).

In this study a DEB model for E. sea bass was developed with the aim to mechanistically
describe the processes of growth and food consumption for the whole life cycle of the species
with focus on the stages pertinent to aquaculture while accounting for temperature changes.
Using literature data the DEB parameters were estimated and their uncertainty was assessed.
The model provides quantiﬁcation of metabolic rates that can be used to assess the response
of E. sea bass to changing environmental conditions, namely temperature and feeding, in the
context of climate change. Furthermore, it introduces a novel method of addressing inter-
individual variability. Finally, validation of the model using aquaculture production data aimed
at increasing the robustness of the generated predictions.

2. Materials and methods

2.1. Model description

DEB theory is a powerful theoretical framework for modeling the metabolic dynamics of an
individual organism through its entire life cycle. Based on physiological rules for the uptake
of food by the organism and its use for maintenance, growth and maturation or reproduction,
the theory allows for modelling the processes of feeding, digestion, maintenance, maturation,
growth, reproduction and aging. A Holling type II functional response relationship is assumed
to exist between food density and feeding rate ( ˙pX). The scaled functional response f , i.e., feed-
ing rate as fraction of maximum possible one of an individual of a given size, is a quantiﬁer of
food availability and takes values between 0 (starvation) and 1 (feeding ad libitum). However,
due to the asymptotic nature of the functional response, slight changes in f may translate to
large changes in food availability at high food levels. Energy from food is extracted by the
organism and added to the reserve via the process of assimilation ( ˙pA). Subsequent mobiliza-
tion ( ˙pC) of the reserve allows for growth ( ˙pG), which is the increase in structural biomass,
maintenance ( ˙pS ), and development or reproduction ( ˙pR). A constant fraction κ of the mobi-
lized reserve is allocated to somatic functions, which include somatic maintenance and growth,
while the remaining 1 − κ fraction is used for development and reproduction, after subtraction
of costs related to maturity maintenance ( ˙pJ).

An individual is described by four state variables: structure (V), energy reserve (E), re-
production buﬀer (ER) and maturity (EH), the latter deﬁned as the cumulative investment to
maturation. The state variables, the energy ﬂuxes and the dynamics of the standard DEB model
are summarized in Table 1. The DEB parameters are presented in Table 2. For a more com-
prehensive description of the DEB theory and a full list of the equations and the nomenclature
used we refer to (Kooijman, 2010a).

The standard DEB model includes three life stages (embryos, juveniles and adults) and as-
sumes isomorphic growth over all life stages. Isomorphy implies that surface area is propor-
tional to structural volume to the power 2/3. Most species with larvae phase, however, show
metabolic acceleration during the early developmental stages, which frequently is followed
by morphological metamorphosis (Kooijman, 2014). Metabolic acceleration means that tem-
porarily the isomorphic individual switches to the V1-morphic mode, meaning that the surface
area grows proportionally to structural volume. The extended DEB models that include various
forms of metabolic acceleration are classiﬁed as a-models (Marques et al., 2018a). When accel-
eration occurs between birth and metamorphosis the model is named “abj” model. Metabolic
3

Table 1: Energy ﬂuxes linked to metabolic processes, state variables, and dynamics of the standard DEB. Brackets
[] indicate quantities expressed per unit of structural volume and braces {} per unit of structural surface area.

Metabolic process
Assimilation

Mobilization

Somatic maintenance
Maturity maintenance
Growth
Maturation/reproduction

˙pA = { ˙pAm} f L2(EH ≥ Eb
H)

˙pC = E

˙v[EG]L2 + ˙pS
[EG]L3 + κE
˙pS = [ ˙pM]L3 + { ˙pT }L2
˙pJ = ˙kJEH
˙pG = κ ˙pC − ˙pS
˙pR = (1 − κ) ˙pC − ˙pJ

State variables
V
L
E
EH
ER

Structural body volume
Volumetric structural length: V 1/3
Energy in reserve
Energy investment into maturation
Energy investment to reproduction

d

Dynamics
dt V = ˙pG
[EG]
dt E = ˙pA − ˙pC
dt EH = ˙pR(EH < E p
H)
dt ER = κR ˙pR(EH ≥ E p
H)

d

d

d

4

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

acceleration accommodates the observed change of shape and the empirical observation that
length increases approximately exponentially with age during the early juvenile stage for most
ﬁsh species. The abj-DEB model has been previously used to model the anchovy Engraulis
encrasicolus, the zebraﬁsh Danio rerio, the Paciﬁc blueﬁn tuna, Thunnus orientalis and many
Mediterranean Perciformes (Pecquerie et al., 2009; Augustine et al., 2011; Jusup et al., 2011;
Lika et al., 2014). The abj-model was also used in this study for the E. sea bass, Dicentrarchus
labrax.

H for hatching, Eb

In the present study we assume ﬁve life stages (embryo, pre-larvae, larvae, juvenile and
adult), with stage transitions occurring when the cumulative investment into maturation, EH,
exceeds certain thresholds: Eh
H for
puberty. The structural volume at this events has values Vh, Vb, V j and Vp, respectively. Birth
in the DEB context marks the start of exogenous feeding and metamorphosis the completeness
of morphological metamorphosis. Puberty is deﬁned as the time when development ceases and
allocation to reproduction commences. The stage of interest for aquaculture is the production
stage which covers parts of the juvenile and adult stages and relates to the on-growing phase of
the species culture. The on-growing phase commences with the transfer of juveniles to marine
cages and ends at harvest.

H for metamorphosis, and E p

H for birth, E j

According to abj-model assumptions, between birth and metamorphosis the individual fol-
lows the rules for V1-morphy. Since V1-morphy only concerns the relationship between sur-
face area and structural volume, changes in shape aﬀect only the speciﬁc maximum assimilation
rate, { ˙pAm}, and the energy conductance, ˙v, via the acceleration factor sM: sM{ ˙pAm} and sM ˙v.
The acceleration factor equals one for embryos and pre-larvae, (V/Vb)1/3 for larvae (early ju-
veniles) and (V j/Vb)1/3 for juveniles and adults. Consequently, the dynamics (Table 1) will
change via the ﬂuxes ˙pA and ˙pC.

A fundamental concept of DEB theory is that all organic compounds, food (X), faeces (P),
structure (V) and reserves (E), are mixtures of polymers such as lipids, proteins and carbohy-
drates and each of them is represented as a “generalized compound” with ﬁxed stoichiometry.
The composition of a generalized compound is expressed as the relative abundance of hydro-
gen (H), oxygen (O) and nitrogen (N) relative to carbon (C). Thus, for example, a molecule of
reserve has the formula CHnHE OnOE NnNE , where n∗E are the stoichiometric coeﬃcients, e.g. nNE
represents the molar N:C ratio of reserve. Each generalized compound has speciﬁed chemical
potential (µ∗), speciﬁc density (d∗), and molecular weight (w∗). Table 2 gives the values of
those auxiliary parameters that are relevant to this study.

The abstract state variables of reserves and structure can be linked to commonly measured
quantities which in this case are length and mass. Total length, which is a measurable length
for a ﬁsh, is related to the structural length (L) with the shape factor (δM) given by

Lw = L/δM

(1)

Body mass of an individual has contributions from structure (V), reserve (E) and (for reproduc-
ing adults) energy reserve for reproduction (ER). Mass quantiﬁed as wet weight (Ww) is given
by

Ww = dVwV + (E + ER)

wEw
µE

(2)

where dVw is the speciﬁc density of wet structure (g/cm3), wEw the molecular weight of wet
reserve (g/mol) and µE the chemical potential of reserve (J/mol) (see for details Kooijman
(2010b, Comments on section 3.2.1)). The dry- over wet-weight ratio of structure and reserve
5

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

= dVd
dVw

and wEd
wEw

is wVd
, respectively. If we assume that dVd
(i.e., the water content
wVw
dVw
of reserve equals that of structure) and dVw = dEw = 1 g/cm3 (i.e., the speciﬁc densities of wet
structure and reserves equals that of water, which hold approximately), equation (2) becomes

= dEd
dEw

= dEd
dEw

Ww = dVwV + (E + ER)

wEddVw
µEdVd

(3)

Mass ﬂuxes of organic (food, faeces, reserves and structure) and mineral (e.g., CO2, nitroge-
nous waste) compounds can be written as weighted sum of three basic ﬂuxes: assimilation ( ˙pA),
dissipation ( ˙pD) and growth ( ˙pG) (Kooijman, 2010a, Chapter 4). Dissipation excludes assimi-
lation and somatic growth overheads and amounts to ˙pD = ˙pS + ˙pJ + (1 − κR) ˙pR for adults or
˙pD = ˙pS + ˙pJ + ˙pR for the non-reproductive stages. For the non-reproductive stages, the energy
invested to maturation is excreted into the environment in the form of heat and metabolites and
does not contribute to the total weight.

Speciﬁcally, the feeding rate, ˙JX, in g/d, is given by

˙JX = wXd
κXµX

˙pA

(4)

where wXd is the molecular weight of dry food (g/mol), µX the chemical potential of food
(J/mol), and κX the conversion eﬃciency of food into assimilated energy. Equation (4) gives
the feeding rate in dry mass of food. To convert it into wet mass, ˙JX must be multiplied by dXw
,
dXd
where dXd is the speciﬁc density of dry food (g/cm3) and dXw of wet, which is taken, as above,
approximately equal to 1 g/cm3.

The rate of nitrogenous waste, in the form of ammonia, is given by

˙JNH

= ηNA ˙pA + ηND ˙pD + ηNG ˙pG

(5)

where the weight coeﬃcients follow from mass conservation: ηNA = nNX
κXµX
and ηNG = nNE
µE

− nNV dVd
[EG]wVd

.

− nNE
µE

− nNPκP
κXµP

, ηND = nNE
µE

Metabolic rates depend on temperature. For a species-speciﬁc range of temperatures, the
temperature eﬀect is quantiﬁed by the Arrhenius relationship (Kooijman, 2010a). For the
species-speciﬁc Arrhenius temperature TA, the rate of a physiological process ˙k at tempera-
ture T is given by

˙k(T ) = ˙k1 exp

(cid:33)

(cid:32)

TA
T1

−

TA
T

(6)

where ˙k1 is the rate at a chosen reference temperature, here T1 = 293K. The reduction of rates
at low and high temperatures is modeled based on the idea that metabolic rates are controlled
by enzymes that catalyze reactions and that they have inactive conﬁgurations outside the tem-
perature tolerance range (Kooijman, 2010a). The rates of enzyme deactivation at the lower (TL)
and upper (TH) boundaries of the tolerance range are taken to depend on temperature in a way
similar to the reaction that is catalyzed by the enzyme, but with diﬀerent Arrhenius tempera-
tures, TAL and TAH, respectively. Therefore, the reduction of physiological rates is quantiﬁed
by multiplication of the rate with the fraction s(T )/s(T1) of the enzyme catalyzing the reaction
that is in active state at temperature T , where

(cid:32)

s(T ) =

1 + exp (

TAL
T

−

TAL
TL
6

) + exp (

TAH
TH

−

TAH
T

(cid:33)−1
)

201

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

231

232

233

234

235

236

237

238

239

240

241

242

243

244

245

2.2. Data

Information on the physiology, morphology and life history of the European sea bass was
taken both from published literature (Lika et al., 2014; Papandroulakis et al., 2014; Person-
Le Ruyet et al., 2004; Zanuy and Carrillo, 1985) and the Hellenic Centre for Marine Research
(HCMR). Several observations were incorporated into the parameter estimation including both
uni-variate and zero-variate data. Zero-variate data, which comprise of single data points,
regarding age, length and wet weight at hatch, birth, metamorphosis, puberty and ultimate
size were included, taken from HCMR, Fishbase (http://www.fishbase.org/summary/
Dicentrarchus-labrax/) and published literature (Lika et al., 2014). The uni-variate data
consisted of: 1) weight-at-age for the on-growing stage (cage stage) at variant temperatures
(Papandroulakis et al., 2014), 2) length- and weight-at-age for the larvae development (Lika
et al., 2015), 3) feeding rates as a function of wet weight at variant temperatures (digitized
from Zanuy and Carrillo (1985)), 4) reproduction rates as a function of wet weight (Mayer
et al., 1990) and 5) Total Ammonia Nitrogen (TAN) excretion rates at various temperatures
(Person-Le Ruyet et al., 2004). Larvae and on-growing rearing data from HCMR concerned
animals produced via the semi-intensive Mesocosm methodology which is known to promote
fast larvae and early juvenile growth rates (Papandroulakis et al., 2014) and the on-growing
phase took place in the cage farm of the Institute at Souda Bay (west Crete).

For the validation of the model, data on growth performance of E. sea bass (weight-time
and feed consumption) were obtained from various commercial farms covering the 2005-2015
period. Average feeding rates were then calculated as the amount of cumulative feed pro-
vided per cage divided by the number of ﬁsh and the number of days between weight mea-
surements. Temperature data were also provided by the farms and were given as monthly aver-
age Sea Surface Temperatures (SST) for the duration of the on-growing period. Temperatures
were recorded with traditional in-situ sensors below the conductive laminar sub-layer, where
daily changes are minimal and diurnal ﬂuctuations are considered negligible (Kawai and Wada,
2007). Since temperature eﬀects on growth are of particular interest for aquaculture, we used
datasets from farms located in three areas which constitute important centres of aquaculture
activity and cover representative parts of the geographical distribution of the industry in the
country. In order to preserve farm anonymity the areas were characterized as “East”, “West”
and “South”, comprising of grid cells with central geographic coordinates “38.72N, 25.81E”,
“39.85N, 20.19E” and “35.70N, 24.69E”, respectively, and approximate dimensions of 50×100
km. Eight data sets were used in total, two from each region and two from commercial farms
of unknown geographical origin.

2.3. Parameter estimation

The parameter estimation procedure is presented in Marques et al. (2018b) and at the online
AmP manual (http://www.debtheory.org/wiki/). Parameters were estimated simultane-
ously from the aforementioned zero- and uni-variate data sets (1-5), on the basis of the minimi-
sation of the symmetric bounded loss function F = (cid:80)n
, where n is the number
i=1
of diﬀerent data sets, ni is the number of data-points of data set i, wi j’s are weight coeﬃcients,
di j’s are data-points, pi j’s are predicted values, di = n−1
j=1 di j is the mean value for dataset
i
i and pi = n−1
j=1 pi j is the mean predicted value for dataset i. All code, data and results are
i
downloadable from AmP (2018) Dicentrarchus labrax version 20180511, which in combina-
tion with the freely downloadable DEBtool at http://www.bio.vu.nl/thb/deb/deblab/,
allows repeatability of the computations.

(di j−pi j)2
+p2
i

j=1 wi j

(cid:80)ni

(cid:80)ni

(cid:80)ni

d2
i

7

246

247

248

249

250

251

252

253

254

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

292

Lack of information regarding metabolic rates at the very edges of the temperature tolerance
range does not allow estimation of all ﬁve temperature parameters. However, this information
is required to increase the applicability of the model in climate change-related studies. In order
to obtain a measure of the reduction of physiological rates at the upper and lower boundaries
of the tolerance range, we used pseudo-data to increase the identiﬁability of the temperature
parameters (TA, TH, TL, TAL and TAH). For the pseudo-data, we assumed near-zero values of the
TAN excretion rates (determined as 5% of the maximum value), at the upper, TH, and lower,
TL, temperatures of the positive rate range known from literature (280-306 K) (Freitas et al.,
2007; Ozolina et al., 2016).

Due to lack of detailed information some parameters could not be estimated and, therefore,
the values of the generalized animal were used (Kooijman, 2010a; Lika et al., 2011). These
values include: the maturity maintenance (˙kJ = 0.002 d−1), the reproduction eﬃciency (κR =
0.95), the defecation eﬃciency of food to faeces (κP = 0.1), the chemical potential parameters
(µV = 500 kJ/mol, µE = 550 kJ/mol, µX = 525 kJ/mol and µP = 480 kJ/mol) and the molecular
weights (wXd = wVd = wEd = 23.9 g/mol). Moreover, the speciﬁc cost for structure, which
is given by [EG] = µV dVd
, was ﬁxed to the value [EG] = 5230 J/cm3 by assuming a growth
κGwVd
eﬃciency of κG = 0.8. This value corresponds to a dry-weight over wet-weight ratio of structure
and reserve equal to 0.2 for ﬁsh (AmP, 2018), which implies that the speciﬁc density of dry
structure is dVd = 0.2 g/cm3, given that dVw = 1 g/cm3.

The conversion eﬃciency of food into assimilated energy was also ﬁxed to the value
κX = 0.68 (Lupatsch et al., 2001). Lupatsch et al. (2001) obtained this value using food with
composition that satisﬁes the protein and lipid requirements recommended by FAO for standard
feed formulation which is what the majority of farms use.

The overall goodness of ﬁt of the model is quantiﬁed with the Mean Relative Error (MRE)
and Symmetric Mean Squared Error (SMSE) (Marques et al., 2018a,b). The relative error (RE)
of each data set can also be computed. MRE can take values in the interval [0, ∞), while
SMSE has values in the interval [0, 1]. Values of MRE and SMSE close to 0 mean that the
model predictions are close to the data.

Uncertainty of the point estimates was assessed by computing the marginal conﬁdence in-
tervals, which may be comprised of more than one interval (conﬁdence sets), using the proﬁle
method (Marques et al., 2018b). The proﬁle method is a two-step procedure. In the ﬁrst step,
the proﬁle of the loss function for a parameter is obtained. In the second, which is the calibra-
tion step, the level of the loss function that corresponds to uncertainty is computed.

The proﬁle of the loss function, F, for the parameter of interest is obtained by ﬁxing the
parameter to a range of values around the parameter estimate that corresponds to the global
minimum, Fmin, of the loss function and estimate all the other parameters. Then, the corre-
sponding diﬀerence with the minimum of the loss function, F − Fmin, is plotted as function of
the parameter of interest (Figure 1, left).

For the calibration step, 1000 Monte Carlo data-sets were generated by adding centered
log-normally distributed scatter, with the same coeﬃcient of variation, to the predictions
for each data-point (zero- and uni-variate data). Since there is no information on scatter
for each of the data-points, the coeﬃcient of variation was set equal to the mean of the
absolute diﬀerence between observed and predicted values divided by the predicted value,
(cid:17)
cv = 1
, which for this study equals to 0.2. For each Monte Carlo sim-
n
ulation of the data-sets, we found the (global) minimum of the loss function. The cumulative
distribution of the diﬀerence X = F − F0 of the global minima, F, and the value in the absence
of scatter, F0, is used to ﬁnd the threshold value for the loss function that corresponds to a
8

|di j−pi j|
pi j

(cid:16) 1
ni

(cid:80)ni

(cid:80)n

j=1

i=1

293

294

295

296

297

298

299

300

301

302

303

304

305

306

307

308

309

310

311

312

313

314

315

316

317

318

319

320

321

322

323

324

325

326

327

328

329

330

331

332

333

334

335

336

337

338

given conﬁdence level. For example, for a conﬁdence level 0.9 the threshold value of the loss
function, Fc, was obtained from P(X ≤ Fc) = 0.9 or equivalently S (Fc) = P(X > Fc) = 0.1,
where S is the survivor function of the diﬀerence F − F0 (Figure 1, right). The marginal conﬁ-
dence set for the parameter of interest consists of all values of the parameter for which the loss
function is below the threshold value.

2.4. Model validation

DEB parameter values are individual-speciﬁc and are partly under genetic control. Genetic
variation is substantial in cultured populations, even in those originating from a limited num-
ber of broodstock individuals (Chistiakov et al., 2005). These genetic diﬀerences reﬂect in
phenotypic diﬀerences such as the ultimate size, and age and size at puberty, among others.
The model developed here introduces inter-individual variability through subdivision of the
population into a number of cohorts that diﬀer in parameter values and initial conditions. We
assume that the parameter values vary between individuals according to the covariation rules
which are applied among diﬀerent species (Kooijman, 2010a), but within a narrower range.
The parameter values, as discussed in (Kooijman, 2010a, Chapter 8), covary inter-speciﬁcally
in a particular way via the zoom factor, z, deﬁned as z = Lm/Lref
m , where Lm = κ{ ˙pAm}/[ ˙pM] is
= 1 cm is a reference maximum structural length. The
the maximum structural length and Lref
m
argument for the covariation of the primary parameters is that only parameters that relate to the
physical design of the organism depend on the maximum size of the organism. Including the
H and ¨ha. There-
aging module, only four parameters depend on physical design: { ˙pAm}, Eb
Am} = z{ ˙p1
fore, for two species, the physical design parameters relate to each other as: { ˙p2
Am},
= z¨h1
Eb
a.
H2
To introduce the inter-individual variability we assume a factor ζ, deﬁned as ζ = z/z0 =
Lm/L0
m are, respectively, the zoom factor and the maximum structural length
of the “reference” individual with the estimated parameter values (Table 2). Individuals relate
to the “reference” individual as: { ˙pAm} = ζ{ ˙p0
Am}, Eb
a. In-
dividuals were assigned diﬀerent values of the zoom factor z sampled randomly from a normal
distribution with mean z0 and standard deviation σ or, equivalently, assigned diﬀerent values
of the factor ζ sampled from a normal distribution with mean one and standard deviation σ/z0;
for either distribution the coeﬃcient of variation is cv = σ/z0. Therefore, a single parameter,
that acts as an individual-speciﬁc multiplier for some of the parameters, produces scatter which
can then be calibrated based on observations of inter-individual variability.

m, where z0 and L0

H0 and ¨ha = ζ ¨h0

H1 and ¨h2

H0, E p

H1, E p

= ζ3E p

= ζ3Eb

= z3E p

= z3Eb

H, E p

H2

H

H

a

Model validation was then performed via comparison of the model predictions to data ob-
tained from the farms. For each data set, the temperature data provided by the farms were used
as the forcing variable and population variability was introduced through the factor, ζ, and the
initial weight, W0, which was also considered to be normally distributed with mean the value
given by the ﬁrst weight measurement. For each data set, 500 Monte Carlo simulations were
performed. The values of the coeﬃcient of variation for ζ and W0 were, respectively, cv = 0.05
and cv = 0.2 and were based on empirical knowledge of the observed variability at common
market and stocking sizes. However, the realism of the variability generated here could not be
further evaluated due to the absence of reported variability for the farm data.

To investigate the variability in food intake throughout the production cycle, we used an ap-
proach that involves a dynamic reconstruction of the scaled functional response using reverse
modeling. Using the weight-time data and temperature data from the diﬀerent farms we back-
estimated the functional response, f . The estimation procedure is similar to that described in
section 2.3. The Nead-Melder simplex method was used to ﬁnd the minimum of the symmetric
9

339

340

341

342

343

344

345

346

347

348

349

350

351

352

353

354

355

356

357

358

359

360

361

362

363

364

365

366

367

368

369

370

371

372

373

374

375

376

377

378

379

380

381

382

383

bounded loss function and estimate values of the functional response at speciﬁed knots. Addi-
tionally, a ﬁlter was applied to prevent f from taking values outside the interval [ fmin, 1], where
fmin is the minimum scaled functional response that is required to reach puberty (Lika et al.,
2014). A cubic Hermite spline was used in order to interpolate between points. Similar ap-
proaches have been used to reconstruct f time series from temperature and growth trajectories
(Cardoso et al., 2006; Freitas et al., 2009; Lavaud et al., 2018; Pecquerie et al., 2012; Troost et
al., 2010).

3. Results

3.1. DEB parameters

The parameter estimates for the E. sea bass DEB model are given in Table 2 and the com-
puted 90% marginal conﬁdence intervals for parameters of interest in Table 3. An illustrative
example of the generated proﬁle of the loss function for the zoom factor, z, and the survivor
function of the loss function for parameter estimates for 1000 Monte-Carlo simulations is pre-
sented in Figure 1. This type of conﬁdence intervals can only provide a rough indication of the
uncertainty in parameter values. Parameters such as ˙v and z exhibited relatively narrow conﬁ-
dence intervals while κ showed the widest, suggesting that this parameter is not well identiﬁed
by the data. In general, the conﬁdence intervals were asymmetric around the point estimates.
The relative distance of the point estimate was smaller to the lower limit than to the upper limit
of the conﬁdence interval, with the exception of κ and δM. Moreover, while for most parameters
the distance between the point estimate and the upper limit was smaller than three times that of
the lower limit, for maturity thresholds it exceeded eight times.

The parameter estimation resulted in an acceptable goodness of ﬁt, quantiﬁed by the mean
relative error (MRE) of 0.1301 and the Symmetric Mean Squared Error (SMSE) of 0.1351,
giving an overall good match between predictions and observations (Figure 2 and Table 4).
For the growth data pertaining to the early developmental stages (Figure 2, b-c) we assumed
f =1, meaning ad libitum feeding, since intensive feeding protocols are applied at hatcheries to
ensure maximum growth. For the data sets referring to the production stage where feeding is
more variable, f was estimated from the data. This resulted in values of f =0.76, f =0.78 and
f =0.94 for Figures 2b, 2d and 2f respectively, which provide a representation of the average
feeding conditions throughout the production stage.

The model performed particularly well at predicting the growth pattern of E. sea bass with the
predicted growth curves accurately matching the observations (Figure 2, a-c). The model cap-
tured growth both quantitatively (relative errors between 0.06 and 0.11) and qualitatively since
seasonal growth changes due to temperature were accurately depicted. Predictions regarding
food intake, reproductive output and ammonia excretion were also fairly accurate (Figure 2,
d-f) with the relative errors being 0.14, 0.18 and 0.05, respectively.

Developmental aspects were also captured well by the model (Table 4). Speciﬁcally, the age
at metamorphosis, the life span, and the wet weight at puberty were most accurately captured,
whereas higher deviations were observed for length at hatch, ultimate wet weight, and age at
birth. Life history traits for which data were not available were predicted by the model. Namely,
the age at puberty was predicted at 723 days with the length at puberty being estimated at 53.4
cm.

3.2. Model validation

The validation of the model was performed by comparing the predictions of the model (wet
weight and feeding rate as functions of time) to data obtained from the farms (Figures 3 and 4).
10

Table 2: DEB parameter values of E. sea bass, corrected for the reference temperature of T=20oC. Brackets []
indicate quantities expressed per unit of structural volume and braces {} per unit of structural surface area.

Symbol
Core parameters
z
{ ˙pAm}
˙v
κ
κX
κP
[ ˙pM]
[EG]
Eh
H
Eb
H
E j
H
E p
H
¨ha
Temperature parameters
TA
TH
TL
TAH

TAL

Conversion parameters
δM
dVd
dXd
wXd, wVd, wEd
µX, µV , µE, µP
nNX, nNV , nNE, nNP

Value

Unit

Interpretation

2.45
85.44/585.85a,b
0.041/0.282a
0.56
0.68c
0.1c
19.60
5230c
0.14
1.61
526.16
2.51 106
1.55 10-9

7998
303
274
87590

22974

Zoom factor
Speciﬁc maximum assimilation rate
Energy conductance
Allocation fraction to soma
Digestion eﬃciency of food to reserves
Defecation eﬃciency of food to faeces

-
J cm-2 d-1
cm d-1
-
-
-
J cm-3 d-1 Volume-speciﬁc somatic maintenance rate
J cm-3
J
J
J
J
d-2

Speciﬁc costs for structure
Maturity threshold at hatching
Maturity threshold at birth
Maturity threshold at metamorphosis
Maturity threshold at puberty
Weibull aging acceleration

K
K
K
K

K

Arrhenius temperature
Higher bound of the tolerance range
Lower bound of the tolerance range
Arrhenius temp for the rate of decrease
at higher boundary
Arrhenius temp for the rate of decrease
at lower boundary

0.148
0.2c
0.2/0.9c
23.9c
525, 500, 550, 480c
0.15c

-
g cm-3
g cm-3
g mol-1
kJ mol-1
-

Shape coeﬃcient
Speciﬁc density of dry structure
Speciﬁc density of dry fresh/pelleted food
Molecular weight of dry mass
Chemical potentials
Molar N:C ratio of dry mass

a Values before/after acceleration.
b Derived from: { ˙pAm} = (z[ ˙pM])/(κLre f
c Fixed. See text for details.

m ) with Lre f

m = 1

Table 3: Point estimates (PE) and marginal Conﬁdence Intervals (CI) using the proﬁle method.

Parameter PE
˙v
κ
[ ˙pM]
Eh
H
Eb
H
E j
H
E p
H
¨ha
z
δM

0.041
0.56
19.60
0.14
1.61
5.26 102
2.56 106
1.55 10−9
2.45
0.148

CI
(0.018, 0.098)
(0.04, 0.89)
(11.52, 48.40)
(0.01,4.40 )
(0.16, 24.99 )
(0.55 102, 88.86 102)
(0.39 106, 24.44 106)
(0.09 10−9, 80.25 10−9)
(0.98, 4.69)
(0.071, 0.198)

11

Figure 1: Left: The proﬁle of the loss function for the zoom factor z. Right: the survivor function of F − F0 (the
diﬀerence of the minimum of the loss function for 1000 Monte-Carlo simulations minus the value in the absence
of scatter). A threshold value (indicated with the solid grey line) for the loss function for a speciﬁed uncertainty,
here 90%, was obtained from the survivor function plot (see text for details). The marginal conﬁdence interval was
obtained by selecting values for the parameter z (left plot) that have loss function values lower than the threshold
(horizontal grey line). In this case, the 90% marginal conﬁdence interval for z was (0.98, 4.69) (indicated with the
dotted grey lines).

Table 4: Comparison of model predictions with observed age, length and weight (where available) at hatch, birth,
metamorphosis and puberty for E. sea bass. Last column gives the relative error (RE) for each data-point.

Symbol (unit)
ah (d)
ah (d)
tb(d)
tb(d)
t j(d)
ap(d)
am(d)
Lh
w(cm)
Lb
w(cm)
L j
w(cm)
Lp
w(cm)
Li
w(cm)
W b
w(g)
W p
w(g)
W i
w(g)

Interpretation
Age at hatch
Age at hatch
Time since hatch at birth
Time since hatch at birth
Time since hatch at metam.
Age at puberty
Life span
Length at hatch
Length at birth
Length at metam.
Length at puberty
Ultimate total length
Weight at birth
Weight at puberty
Ultimate wet weight

T (oC) Observations Predictions RE
0.09
15
0.11
17
0.11
16
0.14
19
< 0.01
19
na
19
< 0.01
20
0.37
0.10
0.15
na
0.10
0.31
0.02
0.32

3.92
3.22
8.01
6.00
69.88
723
5472
0.22
0.50
3.40
53.38
113.6
57 10−5
711
6853

3.6
2.9
9
7
70
na
5475
0.35
0.55
4
na
103
43 10−5
700
10 103

12

Figure 2: Comparison of model predictions (solid lines) to observations (solid points): a. Weight-at-age at constant
temperature. b. Weight-at-age at variable temperature (broken line). c. Length-at-age. d. Food intake as function
of weight at variable temperatures (grey points). e. Reproduction rate as function of weight. f. Total Ammonia
Nitrogen excretion (TAN) rate as function of temperature (open circles denote pseudo-data).

13

384

385

386

387

388

389

390

391

392

393

394

395

396

397

398

399

400

401

402

403

404

405

406

407

408

409

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

For each data set, the temperature data provided by the farms were used as the forcing variable.
For all simulations, a constant functional response of f = 0.8 was assumed. This value was
chosen as being about the average of the f values estimated for the univariate data sets used
for parameterization. In reality, individual food intake exhibits a degree of daily ﬂuctuation
even under controlled conditions. Taking into account that farmed ﬁsh are traditionally fed
well in order to maximize growth, our results suggest that this assumption can provide a good
approximation of the feeding process. Moreover, the food given in the farms is in pelleted form
with the dry-to-wet ratio being around 0.9 (Yildiz et al., 2007), so we took dXd = 0.9 g/cm3.

Overall, the model performed well with considerable accuracy at predicting both growth and
food consumption for all data sets (Figures 3 and 4). With respect to predicting the evolution
of weight (Figures 3 and 4, a, c, e, g), the model can be characterized by high accuracy. Pre-
dictions (solid lines) matched the observations (points) in all eight datasets with high precision
and the small deviations from the empirical mean fell within the generated uncertainty (gray
shaded areas). The similarity between model predictions and observed growth in production
stages indicates that our model features the main mechanisms and eﬀects required to predict
the performance in production facilities.

Regarding food consumption (Figures 3 and 4, b, d, f, h), although the model generally cap-
tured the pattern of the feeding process, marked deviations were also recorded. In addition, the
goodness of ﬁt diﬀered between regions. Predictions of both sets originating from the South
region closely matched the observations while for the West region the model consistently under-
estimated the feeding process. Where diﬀerences between model predictions and observations
existed, predictions were always lower than the observations, thus showing the tendency of the
model to underestimate feeding rates. The highest diﬀerences were observed during the period
following the summer months when warmer temperatures promote high growth rates. This is
depicted on Figure 3-e where high underestimation of the feeding rates during the high summer
temperatures of the ﬁrst year coincides with underestimation of the growth rates, indicating that
the model predictive capacity is reduced towards the edges of the temperature tolerance range.
However, other datasets, such as the ones from the South region (Figure 3, e-h), suggested
that underestimation of feeding is not systematic since both growth and feeding rates are cap-
tured well even at temperatures approaching 28 oC. Therefore, the observed deviations may be
attributed to both model uncertainty and inconsistencies in the real data.

The reconstruction of the scaled functional response, f , was carried out for the three growth
data sets presented in Figures 4a, 4e and 4g. The reconstructed f trajectories are presented
in Figure 5. The results suggest that f varies throughout the production cycle with average
values f =0.71 (Figure 5a), f =0.76 (Figure 5b) and f =0.73 (Figure 5c). The temporal pattern
of the reconstructed f follows that of the growth rate (not shown), where the low values of f
correspond to low growth rates in the weight-data.

4. Discussion

The parameters of a DEB model for E. sea bass, a species of major importance for the
Mediterranean aquaculture, were estimated. The framework provided by the DEB theory al-
lowed the quantiﬁcation of processes that are of interest for aquaculture such as growth and
feeding. Moreover, the novel proﬁle method of Marques et al. (2018b) was applied to assess
the uncertainty of the estimated parameters. In general, the conﬁdence intervals were asymmet-
ric around the point estimates. Interestingly, the conﬁdence intervals for all maturity thresholds
were the most asymmetric ones, with the relative distance of the point estimate to the lower
limit much smaller than to the upper limit. This may indicate strong limitations with respect to
14

Figure 3: Wet weight (g), feeding rate (g/d) and temperature (oC) as a function of time (d) for two datasets of
unknown origin (a-d) and two from the West (e-h) Region: comparison of model predictions (solid lines) to
observations (points). Grey shaded areas indicate model uncertainty (500 Monte Carlo simulations) and broken
lines the temperature from each region. For all simulations, f = 0.8.

15

Figure 4: Wet weight (g), feeding rate (g/d) and temperature (oC) as functions of time (d) for two datasets from
the East (a-d) and two from the South (e-h) Region: comparison of model predictions (solid lines) to observa-
tions (points). Grey shaded areas indicate model uncertainty (500 Monte Carlo simulations) and broken lines the
temperature from each region. For all simulations, f = 0.8.

16

Figure 5: Reconstructed f trajectory from weight-time data from Figure 4a (a), Figure 4e (b) and Figure 4g (c).
Solid lines represent the smoothed trajectory through the estimated knot values (points) and broken lines denote
temperature.

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

reducing developmental time for various stages which in turn provides insight into the capacity
of aquaculture in selecting for those traits.

For all the regions that were investigated, the single estimated parameter set was capable of
reproducing the growth patterns with high accuracy. The growth rates for the eight production
sets that were used fell within the range reported for the species for temperate climates (L´opez-
Albors et al., 2008; Navarro-Martn et al., 2009; Samaras et al., 2017). Temperature between
production data-sets diﬀered not only due to the geographic distribution of the farms but also
due to the timing of stocking which may diﬀer among or within farms. The good performance
of the model for the wide range of temperatures forced in the simulations (14.1 – 27.9 oC) while
capturing the seasonal aspects of growth, highlights the generality and robustness of the devel-
oped model. Furthermore, it suggests satisfactory predictive capacity and applicability of the
model for studying implications of phenomena like climate change, at least for the temperature
range tested here.

Maintaining food availability at maximum (i.e., f close to 1) would theoretically allow max-
imization of growth for farmed species. However, in practice this is neither feasible nor ﬁ-
nancially viable due to the multi-factorial nature of ﬁsh biology and farm economics. In fact,
attempting to maintain f close to 1 would likely result in low assimilation eﬃciency and over-
feeding, and thus increased costs and lower overall proﬁtability (Jusup et al., 2014). Moreover,
lower feeding levels may be desirable due to the associated beneﬁts in immunology and overall
ﬁsh health (Miˇslov Jelavi´c et al., 2012).

Varying feeding protocols involving diﬀerences in food quality, feeding frequency, dura-
tion of feeding, and feeding techniques can alter the eﬃciency of food conversion (Kousoulaki
et al., 2015) and therefore, result in farm-speciﬁc f values. Moreover, feeding throughout the
production cycle is rarely constant since husbandry practice can modify feeding by including
days of starvation on the feeding schedule or prior to handling (vaccination, sampling, har-
vesting) or restricted rations under adverse rearing conditions (Kousoulaki et al., 2015; Leal
et al., 2011). The aforementioned changes in feeding protocols are often implemented at spe-
ciﬁc stages of the production cycle to accommodate size-dependent physiological changes of
the farmed ﬁsh. This may explain why discrepancies between observed and predicted feeding
rates were more pronounced at larger sizes. However, it is apparent from our simulations that
a constant functional response (here f = 0.8) that assumes well-fed ﬁsh can yield predictions
17

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

500

501

502

503

504

505

506

507

that match growth observations with reasonable accuracy. Therefore, a representative average
value for f can provide realistic output to be used for simulating future projections in aquacul-
ture. Other approaches such as trajectory reconstruction can be applied if the research focus is
oriented towards describing the temporal variations of the feeding process (Freitas et al., 2009;
Jusup et al., 2014; Pecquerie et al., 2012).

Reconstruction of the feeding trajectory for selected farms showed that the average feeding
conditions (quantiﬁed as f ) of those farms were close to the one we used for validation of the
model. Moreover, the reconstruction results suggested that food availability was highly vari-
able throughout the production cycle with oscillating patterns that have also been recorded for
other farmed ﬁsh (Jusup et al., 2014). Although the time of stocking, and therefore the tem-
perature pattern, diﬀered between the three production sets for which f was reconstructed, no
explicit correlation was detected between ﬂuctuations of f and time of stocking or seasonality.
This in turn indicates that the observed variability could be interpreted by irregularities in the
feeding scheme. Therefore, we conclude that attention should be given in establishing feeding
protocols that reduce the aforementioned oscillations in f , which would consequently increase
the predictability of production.

The boundaries of the temperature tolerance range for the species, and especially the higher
bound, constitute areas of scientiﬁc uncertainty since limited information is available in the lit-
erature regarding the eﬀect of extreme temperatures on metabolic rates (Claireaux et al., 2006;
Ozolina et al., 2016). The assumptions we used here to estimate the Arrhenius deactivation
rates at the edges of the temperature tolerance range constitute model weaknesses and more ex-
perimental work is required in order to decrease model uncertainty. Nevertheless, they provide
means of addressing thermal eﬀects on farmed E. sea bass at a wider temperature spectrum,
which is pertinent to climate change.

Inevitably, the model is expected to be more sensitive at high temperatures. Although not
evident for growth, validation showed tendency of the model to underestimate feeding rates,
which was more pronounced in higher temperatures. However, as discussed in section 3.2 this
was not consistent. Therefore, despite the model’s uncertainty associated with higher tempera-
tures, deviations between predictions and observations could also be attributed to the employed
feeding practices.

The model approximates the feeding process and predicts individual daily food intake. How-
ever, data originating from farms are not individual-based and rarely exhibit the same level of
precision. Feeding in ﬁsh farms is a relatively coarse process with the measured and reported
quantities relating to the total biomass of feed provided per cage rather than the actually quan-
tities consumed by the ﬁsh. Moreover, feeding in cage aquaculture is traditionally determined
by observation with indicators such as the decline of ﬁsh density at the surface denoting sati-
ation and the end of food supply. This approach however is not accurate and provision occurs
in excess with as much as 8% being lost depending on the species and the feed properties
(Garcia-Pineda et al., 2011).

Apart from environmental implications, the ﬁnancial aspect of overfeeding is the one most
important for aquaculture. Feeding represents the main expenditure in ﬁnﬁsh aquaculture and
can exceed 60% of the total production cost (Llorens et al., 2017), which renders the improve-
ment of food eﬃciency a priority for industrial aquaculture. Growth is known to decline at
temperatures above the optimal range due to loss of appetite (P¨ortner and Knust, 2007). There-
fore, overfeeding can be a pronounced event during summer months when feed provision is
not timely adjusted to the reduction of growth rates. Such a pattern is consistent with our vali-
dation results and suggests that the model developed here can provide means of assessing and
18

508

509

510

511

512

513

514

515

516

517

518

519

520

521

522

523

524

525

526

527

528

529

530

531

improving feeding practices at the farm level.

Technological advances, such as the development of image processing technology, have en-
abled underwater monitoring and allowed for automated feeding adjustments on-site which
reduce the quantity of uneaten pelleted food (Li et al., 2017). Nevertheless, accurate quantiﬁ-
cation of food requirements is needed to improve feeding practices in aquaculture. Extensive
work has been done regarding feeding, the digestibility of diﬀerent ingredients and waste pro-
duction in E. sea bass (Kousoulaki et al., 2015; Lupatsch et al., 2010, 2001; Omnes et al.,
2017; Piedecausa et al., 2010). However, the scope is often limited to experimental rather than
commercial diets, exhibits experimental duration limitations, and covers speciﬁc ranges of ﬁsh
sizes while quantiﬁcation of uneaten food remains challenging due to the extremely variable
nature of the feeding protocols employed. The holistic approach of the DEB framework which
can quantify metabolism throughout the production cycle of the farmed ﬁsh oﬀers means of
addressing some of those issues. The E. sea bass model developed here constitutes both an
explanatory and predictive tool for investigating future scenarios in the context of a changing
ocean while also contributing towards the assessment and improvement of feeding practices.

5. Conclusion

The energy-based framework of the DEB theory is able to quantify processes such as growth
and feeding throughout the life cycle of an organism as a function of constant parameters and
under changing environmental conditions. The dynamic nature of the model developed here
allows the prediction of growth and assessment of the farm-speciﬁc eﬃciency of the feeding
process under the variable temperature regimes of cage culture throughout the production cy-
cle. Moreover, discrepancies between observed and predicted feeding rates can be used to
inform management on the timely adjustments of feed quantities and thus contribute to the
improvement of the feeding process and reduction of production costs.

Acknowledgments

We are thankful to the Greek aquaculture producers for providing the production data used
for validation and P. Anastasiadis for assembling them. We further thank one anonymous ref-
eree and L. Pecquerie for their constructive comments and suggestions concerning the paper
and S. Augustine for providing the code for the reconstruction of the functional response. Fund-
ing was provided through the European Union Horizon 2020 Project ClimeFish 677039.

References

AmP. Add-my-Pet collection, online database of DEB parameters, implied properties and referenced underlying

data. http://www.bio.vu.nl/thb/deb/deblab/add_my_pet/ Last accessed: 2018/04/01..

Alami-Durante, H., Rouel, M., Kentouri, M., 2006. New insights into temperature-induced white muscle growth
plasticity during Dicentrarchus labrax early life: A developmental and allometric study. Marine Biology 149,
1551–1565.

Augustine, S., Gagnaire, B., Floriani, M., Adam-Guillermin, C., Kooijman, S. A. L. M., 2011. Developmental en-
ergetics of zebraﬁsh, Danio rerio. Comparative Biochemistry and Physiology. Part A, Molecular and Integrative
Physiology 159 (3), 275–283.

Brug`ere, C., 2015. Climate Change Vulnerability in Fisheries and Aquaculture: A synthesis of Six Regional

Studies. No. C1104 in FAO Fisheries and Aquaculture Circular. FAO, Rome.

Cardoso, J.F.M.F., Witte, J.I.J., van der Veer, H.W., 2015. Intra- and interspecies comparison of energy ﬂow in
bivalve species in Dutch coastal waters by means of the Dynamic Energy Budget (DEB) theory. Journal of Sea
Research 56 (2), 182-197.

19

Chistiakov, D. A., Hellemans, B., Haley, C. S., Law, A. S., Tsigenopoulos, C. S., Kotoulas, G., Bertotto, D.,
Libertini, A., Volckaert, F. A. M., 2005. A Microsatellite Linkage Map of the European Sea Bass Dicentrarchus
labrax L. Genetics 170 (4), 1821–1826.

Claireaux, G., Couturier, C., Groison, A.-L., 2006. Eﬀect of temperature on maximum swimming speed and
cost of transport in juvenile European sea bass (Dicentrarchus labrax). The Journal of Experimental Biology
209 (17), 3420–3428.

FEAP, 2016. European Aquaculture Production Report 2007-2015. Federation of European Aquaculture Produc-

ers. Prepared by the FEAP Secretariat.

Føre, M., Alver, M., Alfredsen, J. A., Maraﬁoti, G., Senneset, G., Birkevold, J., Willumsen, F. V., Lange, G.,
Espmark, s., Terjesen, B. F., 2016. Modelling growth performance and feeding behaviour of Atlantic salmon
(Salmo salar L.) in commercial-size aquaculture net pens: Model details and validation through full-scale
experiments. Aquaculture 464 (Supplement C), 268–278.

Freitas, V., Campos, J., Fonds, M., Van der Veer, H. W., 2007. Potential impact of temperature change on epiben-
thic predatorbivalve prey interactions in temperate estuaries. Journal of Thermal Biology 32 (6), 328–340.
Freitas, V., Cardoso, J. F. M. F., Santos, S., Campos, J., Drent, J., Saraiva, S., Witte, J. I., Kooijman, S. A. L. M.,
Van der Veer, H. W., 2009. Reconstruction of food conditions for Northeast Atlantic bivalve species based on
Dynamic Energy Budgets. Journal of Sea Research 62 (2), 75–82.

Garcia-Pineda, M., Sendra, S., Lloret, J., Lloret, G., Jan. 2011. Monitoring and control sensor system for ﬁsh

feeding in marine ﬁsh farms. IET Communications 5 (12),1682–1690.

Guyondet, T., Roy, S., Koutitonsky, V. G., Grant, J., Tita, G., 2010. Integrating multiple spatial scales in the
carrying capacity assessment of a coastal ecosystem for bivalve aquaculture. Journal of Sea Research 64, 341–
359.

Hollowed, A. B., Barange, M., Beamish, R. J., Brander, K., Cochrane, K., Drinkwater, K., Foreman, M. G. G.,
Hare, J. A., Holt, J., Ito, S.-i., Kim, S., King, J. R., Loeng, H., MacKenzie, B. R., Mueter, F. J., Okey, T. A.,
Peck, M. A., Radchenko, V. I., Rice, J. C., Schirripa, M. J., Yatsu, A., Yamanaka, Y., 2013. Projected impacts
of climate change on marine ﬁsh and ﬁsheries. ICES Journal of Marine Science 70 (5), 1023–1037.

Jusup, M., Klanjˇsˇcek, T., Matsuda, H., 2014. Simple measurements reveal the feeding history, the onset of repro-
duction, and energy conversion eﬃciencies in captive blueﬁn tuna. Journal of Sea Research 94 (Supplement
C), 144–155.

Jusup, M., Klanjˇsˇcek, T., Matsuda, H., Kooijman, S. A. L. M., 2011. A full lifecycle bioenergetic model for blueﬁn

tuna. PLoS ONE 6(7): e21903. https://doi.org/10.1371/journal.pone.0021903

Kawai, Y., Wada, A., 2007. Diurnal Sea Surface Temperature variation and its impact on the atmosphere and

ocean: A review. Journal of Oceanography 63, 721–744.

Kooijman, S. A. L. M., 2010a. Dynamic Energy Budget Theory for Metabolic Organisation. Cambridge University

Press.

Kooijman, S. A. L. M., 2010b. Dynamic Energy Budget Theory for Metabolic Organisation. Cambridge University

Press. Comments at http://www.bio.vu.nl/thb/research/bib/Kooy2010_c.pdf

Kooijman, S. A. L. M., 2014. Metabolic acceleration in animal ontogeny: An evolutionary perspective. Journal of

Sea Research 94 (Supplement C), 128–137.

Kooijman, S. A. L. M., Lika, K., 2014. Comparative energetics of the 5 ﬁsh classes on the basis of dynamic energy

budgets. Journal of Sea Research 94 (Supplement C), 19–28.

Kousoulaki, K., Sther, B.-S., Albrektsen, S., Noble, C., 2015. Review on European sea bass (Dicentrarchus labrax,
Linnaeus, 1758) nutrition and feed management: a practical guide for optimizing feed formulation and farming
protocols. Aquaculture Nutrition 21 (2), 129–151.

Lavaud R., Jolivet A., Rannou E., Jean F., Strand Ø., Flye-Sainte-Marie J., 2018. What can the shell tell about
the scallop? Using growth trajectories along latitudinal and bathymetric gradients to reconstruct physiological
history with DEB theory. Journal of Sea Research. doi:10.1016/j.seares.2018.04.001

Leal, E., Fern´andez-Durn, B., Guillot, R., R´ıos, D., Cerd´a-Reverter, J. M., 2011. Stress-induced eﬀects on feeding
behavior and growth performance of the sea bass (Dicentrarchus labrax): a self-feeding approach. Journal of
Comparative Physiology 181 (8), 1035–1044.

Li, D., Xu, L., Liu, H., 2017. Detection of uneaten ﬁsh food pellets in underwater images for aquaculture. Aqua-

cultural Engineering 78 (Part B), 85–94.

Libralato, S., Solidoro, C., 2008. A bioenergetic growth model for comparing Sparus aurata’s feeding experi-

ments. Ecological Modelling 214 (2), 325–337.

Lika K., Augustine S., Pecquerie L., Kooijman S.A.L.M., 2014. The bijection from data to parameter space with
the standard DEB model quantiﬁes the supply-demand spectrum. Journal of Theoretical Biology. 354:35–47.
Lika, K., Kearney, M. R., Freitas, V., van der Veer, H. W., van der Meer, J., Wijsman, J. W. M., Pecquerie, L.,
20

Kooijman, S. A. L. M., 2011. The covariation method for estimating the parameters of the standard Dynamic
Energy Budget model I: Philosophy and approach. Journal of Sea Research 66 (4), 270–277.

Lika, K., Kooijman, S. A. L. M., Papandroulakis, N., 2014. Metabolic acceleration in Mediterranean Perciformes.

Journal of Sea Research 94, 37–46.

Lika, K., Pavlidis, M., Mitrizakis, N., Samaras, A., Papandroulakis, N., 2015. Do experimental units of diﬀerent
scale aﬀect the biological performance of European sea bass Dicentrarchus labrax larvae?. Journal of Fish
Biology 86, 1271–1285.

Llorens, S., Prez-Arjona, I., Soliveres, E., Espinosa, V., 2017. Detection and target strength measurements of

uneaten feed pellets with a single beam echosounder. Aquacultural Engineering 78 (Part B), 216–220.

L´opez-Albors, O., Abdel, I., Periago, M. J., Ayala, M. D., Alc´azar, A. G., Graci´a, C. M., Nathanailides, C.,
V´azquez, J. M., 2008. Temperature inﬂuence on the white muscle growth dynamics of the sea bass Dicentrar-
chus labrax, L. Flesh quality implications at commercial size. Aquaculture 277 (1), 39–51.

Lupatsch, I., Kissil, G. W., Sklan, D., 2001. Optimization of feeding regimes for European sea bass Dicentrarchus

labrax: a factorial approach. Aquaculture 202 (3), 289–302.

Lupatsch, I., Santos, G. A., Schrama, J. W., Verreth, J. A. J., 2010. Eﬀect of stocking density and feeding level on
energy expenditure and stress responsiveness in European sea bass Dicentrarchus labrax. Aquaculture 298 (3),
245–250.

Mayer, I., Shackley, S. E., Witthames, P. R., 1990. Aspects of the reproductive biology of the bass, Dicentrarchus

labrax L. Fecundity and pattern of oocyte development. Journal of Fish Physiology 36, 141–148

Marques, G. M, Augustine, S., Lika, K., Pecquerie, L. Kooijman, S. A. L. M., 2018a. The AmP project: Com-
paring Species on the Basis of Dynamic Energy Budget Parameters. PLOS Computational Biology 14(5):
e1006100. https://doi.org/10.1371/journal.pcbi.1006100.

Marques, G. M, Lika, K., Augustine, S., Pecquerie, L. Kooijman, S. A. L. M., 2018b. Fitting Multiple Models to

Multiple Data Sets. Submitted to this special issue.

Miˇslov Jelavi´c, K., Stepanowska, K., Grubiˇsiˇc, L., Bubiˇc, T. ˇS., Kataviˇc, I., 2012. Reduced feeding eﬀects to the
blood and muscle chemistry of farmed juvenile blueﬁn tuna in the Adriatic Sea. Aquaculture Research 43 (2),
317-320.

Navarro-Mart´ın, L., Bl´azquez, M., Vi˜nas, J., Joly, S., Piferrer, F., 2009. Balancing the eﬀects of rearing at low
temperature during early development on sex ratios, growth and maturation in the European sea bass (Dicen-
trarchus labrax).: Limitations and opportunities for the production of highly female-biased stocks. Aquaculture
296 (3), 347–358.

Nisbet, R. M., Jusup, M., Klanjˇsˇcek, T., Pecquerie, L., 2012. Integrating dynamic energy budget (DEB) theory

with traditional bioenergetic models. The Journal of Experimental Biology 215, 892–902.

Omnes, M.-H., Le Goasduﬀ, J., Le Delliou, H., Le Bayon, N., Quazuguel, P., Robin, J. H., 2017. Eﬀects of
dietary tannin on growth, feed utilization and digestibility, and carcass composition in juvenile European sea
bass (Dicentrarchus labrax L.). Aquaculture Reports 6 (Supplement C), 21–27.

Ozolina, K., Shiels, H. A., Ollivier, H., Claireaux, G., 2016. Intraspeciﬁc individual variation of temperature tol-
erance associated with oxygen demand in the European sea bass (Dicentrarchus labrax). Conservation Physi-
ology 4 (1).

Papandroulakis, N., Lika, K., Kristiansen, T. S., Oppedal, F., Divanach, P., Pavlidis, M., 2014. Behaviour of
European sea bass, Dicentrarchus labrax L., in cages impact of early life rearing conditions and management.
Aquaculture Research 45 (9), 1545–1558.

Peck, M. A., Reglero, P., Takahashi, M., Catal´an, I. A., 2013. Life cycle ecophysiology of small pelagic ﬁsh and

climate-driven changes in populations. Progress in Oceanography 116 (Supplement C), 220–245.

Pecquerie, L., Fablet, R., De Pontual, H., Bonhommeau, S., Alunno-bruscia, M., Petitgas, P., A. L. M. Kooij-
man, S., 2012. Reconstructing individual food and growth histories from biogenic carbonates. Marine Ecology
Progress Series 447, 151–164.

Pecquerie, L., Petitgas, P., Kooijman, S. A. L. M., 2009. Modeling ﬁsh growth and reproduction in the context of
the Dynamic Energy Budget theory to predict environmental impact on anchovy spawning duration. Journal of
Sea Research 62 (2), 93–105.

Peres, H., Oliva-Teles, A., 1999. Inﬂuence of temperature on protein utilization in juvenile European sea bass

(Dicentrarchus labrax). Aquaculture 170 (3), 337–348.

Person-Le Ruyet, J., Mah´e, K., Le Bayon, N., Le Delliou, H., 2004. Eﬀects of temperature on growth and
metabolism in a Mediterranean population of European sea bass, Dicentrarchus labrax. Aquaculture 237 (1),
269–280.

Piedecausa, M. A., Aguado-Gim´enez, F., Cerezo-Valverde, J., Hern´andez-Llorente, M. D., Garc´ıa-Garc´ıa, B.,
2010. Simulating the temporal pattern of waste production in farmed gilthead seabream (Sparus aurata), Eu-
21

ropean sea bass (Dicentrarchus labrax) and Atlantic blueﬁn tuna (Thunnus thynnus). Ecological Modelling
221 (4), 634–640.

P¨ortner, H. O., Knust, R., 2007. Climate change aﬀects marine ﬁshes through the oxygen limitation of thermal

tolerance. Science 315 (5808), 95–97.

Rosa, R., Marques, A., Nunes, M., 2012. Impact of climate change in Mediterranean aquaculture. Reviews in

Aquaculture 4, 163–177.

Samaras, A., Pavlidis, M., Lika, K., Theodoridi, A., Papandroulakis, N., 2017. Scale matters: performance of
European sea bass, Dicentrarchus labrax, L. (1758), reared in cages of diﬀerent volumes. Aquaculture Research
48 (3), 990–1005.

Sar´a, G., Reid, G., Rinaldi, A., Palmeri, V., Troell, M., Kooijman, S. A. L. M., 2012. Growth and reproduction
simulation of candidate shellﬁsh species at ﬁsh cages in the southern mediterranean: Dynamic Energy Budget
(DEB) modelling for integrated multi-trophic aquaculture. Aquaculture 324-325, 259–266.

Serpa, D., Ferreira, P. P., Ferreira, H., da Fonseca, L. C., Dinis, M. T., Duarte, P., 2013. Modelling the growth of
white seabream (Diplodus sargus) and gilthead seabream (Sparus aurata) in semi-intensive earth production
ponds using the Dynamic Energy Budget approach. Journal of Sea Research 76 (Supplement C), 135–145.
Troost, T.A., Wijsman, J.W.M., Saraiva, S. and Freitas, V., 2010. Modelling shellﬁsh growth with dynamic en-
ergy budget models: an application for cockles and mussels in the Oosterschelde (Southwest Netherlands).
Philosophical Transactions of the Royal Society B: Biological Sciences 365(1557), 3567-3577.

Tveter˙as, S., Tveter˙as, R., 2010. The Global Competition for Wild Fish Resources between Livestock and Aqua-

culture. Journal of Agricultural Economics 61 (2), 381–397.

Yildiz, M., Sener, E., Timur, M. Eﬀects of variations in feed and seasonal changes on body proximate composition
of wild and cultured sea bass (Dicentrarchus labrax L.) . Turkish Journal of Fisheries and Aquatic Sciences 7,
45–51.

Zanuy, S., Carrillo, M., 1985. Annual cycles of growth, feeding rate, gross conversion eﬃciency and hematocrit
levels of sea bass (Dicentrarchus labrax L.) adapted to two diﬀerent osmotic media. Aquaculture 44 (1), 11–25.

22

