Contents lists available at ScienceDirect

Coastal Engineering

journal homepage: www.elsevier.com/locate/coastaleng

Aquaculture farms as nature-based coastal protection: Random wave
attenuation by suspended and submerged canopies
Longhuan Zhu a,∗, Kimberly Huguenard a, Qing-Ping Zou b, David W. Fredriksson c, Dongmei Xie d
a Department of Civil and Environmental Engineering, University of Maine, Orono, ME, 04469-5711, USA
b The Lyell Centre for Earth and Marine Science and Technology, Institute for Infrastructure and Environment, Heriot-Watt University, Edinburgh, UK
c Department of Naval Architecture and Ocean Engineering, U.S. Naval Academy, Annapolis, MD, 21402, USA
d College of Harbour, Coastal and Offshore Engineering, Hohai University, Nanjing, 210098, China

A R T I C L E I N F O

A B S T R A C T

Keywords:
Wave attenuation
Random waves
Suspended canopy
Vegetation
Aquaculture farm
Natural coastal defense

As the frequency and intensity of storms increase, a growing need exists for resilient shore protection techniques
that have both environmental and economic benefits. In addition to producing seafood, aquaculture farms
may also provide coastal protection benefits either alone or with other nature-based structures. In this paper,
a generalized three-layer frequency dependent theoretical model is derived for random wave attenuation due
to presence of biomass within the water column. The biomass can be characterized as submerged, emerged,
suspended and floating canopies that can consist of natural aquatic vegetation with potential aquaculture
systems of kelp or mussels. The present analytical solutions can reduce to the solutions by Mendez and
Losada (2004), Chen and Zhao (2012) and Jacobsen et al. (2019) for submerged rigid aquatic vegetation.
The present theoretical model incorporates the motion of these canopies using a cantilever-beam model for
slender components and a buoy-on-rope model for elements with concentrated mass and buoyancy. Analytical
results are compared with existing laboratory and field datasets for submerged and suspended canopies. The
theoretical model was then used (in a case study at a field site in Northeastern US) to investigate the capacity
of suspended mussel farms with submerged aquatic vegetation (SAV) to dissipate wave energy during a recent
storm event. Compared to a dense SAV meadow in shallower water, the suspended aquaculture farms more
effectively attenuate random waves with a smaller peak period and the higher frequency components of wave
spectrum. The performance of suspended aquaculture farms is less affected by water level changes due to
tides, surge and sea level rise, while the wave attenuation performance of SAV decreases with increasing
water level due to decreased wave motion near the sea bed. Incorporating suspended aquaculture farms
offshore significantly enhance the coastal protection effectiveness of SAV-based living shorelines and extend
the wave attenuation capacity over a wider wave period and water level range. The combination of suspended
aquaculture farms and traditional living shorelines provides a more effective nature-based coastal defense
strategy than the traditional living shorelines alone.

1. Introduction

level are likely to occur (Izaguirre et al., 2011; Tebaldi et al., 2012;

Approximately 40% of the world’s population lives within 100
kilometers of the coast (MEA, 2005; Ferrario et al., 2014), and 71% of
the coastal population lives within 50 kilometers of an estuary (UNEP,
2006). While coastal communities benefit from proximity to seascapes,
they are more vulnerable to natural coastal hazards and extreme events
from the sea. For example, from 1900 to 2017, 197 hurricanes with 206
landfalls in the USA caused about 2 trillion USD damage (normalized
to 2018 value by considering the effects of inflation, wealth, and
population), or annually about 17 billion USD (Weinkle et al., 2018).
Due to climate change, more frequent and severe storms and rising sea

Ondiviela et al., 2014).

To mitigate storm damage, hard structures such as seawalls, break-

waters, and bulkheads have been used as coastal defenses. These struc-

tures, however, may aggravate land subsidence due to soil drainage,

inhibit natural accumulation of sediments by tides and waves, adversely

impact water quality, and cause coastal habitat loss (Syvitski et al.,

2009; Currin et al., 2010; Pace, 2011; Temmerman et al., 2013; Sutton-

Grier et al., 2015). Additionally, these conventional hard engineering

defenses are also seriously challenged due to their continual and costly

∗ Corresponding author.

E-mail address:

longhuan.zhu@maine.edu (L. Zhu).

https://doi.org/10.1016/j.coastaleng.2020.103737
Received 12 October 2019; Received in revised form 27 May 2020; Accepted 30 May 2020

CoastalEngineering160(2020)103737Availableonline2June20200378-3839/©2020ElsevierB.V.Allrightsreserved.L. Zhu et al.

Fig. 1. Canopy classification (from left to right): suspended aquaculture farms, floating
wetlands, submerged plants, and emergent plants (figure credit: Yu-Ying Chen).

maintenance, as well as their reconstruction and reinforcement to keep
up with increasing flood risk are becoming unsustainable (Temmerman
et al., 2013). Natural and nature-based infrastructure may be a viable
alternative to hardened shoreline protection system with added eco-
nomic and ecological benefits and ability to adapt to sea level rise and
climate change (Borsje et al., 2011; Gedan et al., 2011; Temmerman
et al., 2013).

As an example of nature-based infrastructure, living shorelines in-
cluding a variety of wetland plants, aquatic vegetation, kelp beds and
oyster reefs have become a complement to hardened shoreline stabi-
lization. Unlike many hardened coastal protection techniques, living
shorelines can mitigate storm damage and erosion while enhancing pro-
ductive habitat, improving water quality, producing food and adapting
to rising sea level (Currin et al., 2010; Scyphers et al., 2011; Davis et al.,
2015; Bilkovic et al., 2016; Gittman et al., 2016; Saleh and Weinstein,
2016; Vuik et al., 2016; Moosavi, 2017; Leonardi et al., 2018; Möller,
2019). The protection of coastal ecosystems by wave attenuation is
more effective in areas with relatively small tidal ranges (Bouma et al.,
2014). Living shorelines at exposed, high-energy sites require structure
such as breakwater or sill offshore to damp incident wave energy to
sustain health growth of the living organisms (McGehee, 2016).

Aquaculture systems may also act as nature-based infrastructure
to attenuate wave energy and produce food at the same time. For
example, Plew et al. (2005) observed that a 650 m × 2450 m mussel
farm reduced wave energy by approximately 5%, 10%, and 17% at
wave frequencies of 0.1, 0.2, and 0.25 Hz, respectively at low sea state.
It was found that densely grown kelp may have advantageous wave
attenuation characteristics (Mork, 1996). For instance, Mork (1996)
observed a 70% to 85% wave energy reduction across a 258 m long
kelp bed (dominated by Laminaria hyperborea) with the highest wave
attenuation observed during low tide. Unlike the natural kelp beds
rooted at the seabed, cultivated kelp is suspended near the surface
from a longline (Peteiro and Freire, 2013; Peteiro et al., 2016; Walls
et al., 2017; Campbell et al., 2019; Grebe et al., 2019; Zhu et al.,
2019), as shown on Fig. 1. Near surface cultivated kelp may damp
more wave energy than bottom-rooted kelp since the wave motion
decreases towards the bottom. Kelp can also absorb carbon to mitigate
climate change impacts and reduce nutrients to improve water quality,
therefore, increase the growth rate of marine species (Duarte et al.,
2017; Campbell et al., 2019). Other environmental benefits of kelp and
seaweed farming include recycling inorganic nutrients and preventing
eutrophication conditions (Yang et al., 2015; Stévant et al., 2017; Xiao
et al., 2017; Campbell et al., 2019).

Both mussels and kelp are often farmed near the surface on a
horizontal type mooring system (Fig. 1). The wave attenuation char-
acteristics of these aquaculture farms can be modeled in a similar way
as natural, bottom-rooted submerged and emergent canopies such as
kelp forests, seagrasses and salt marshes. In this study, the aquaculture
structures are treated as suspended canopies according to the classi-
fication shown on Fig. 1. The classification is based on the vertical

position in the water column and the ‘‘plant’’ height relative to the
water depth (e.g., Plew, 2011; Huai et al., 2012; Chen et al., 2016;
Zhu and Zou, 2017). The horizontal mussel and kelp farms shown
on Fig. 1 are placed at an elevation with optimum light, temperature
and nutrient conditions within the water column to achieve maximum
growth. Fig. 1 also shows a row of nature-based floating wetlands and
natural submerged and emergent plants.

Extensive studies have been dedicated to better understanding and
predicting wave attenuation by submerged and emergent vegetation
as reviewed later in Section 2.1. To model the wave attenuation by
suspended canopies, Plew et al. (2005) developed a two-layer analytical
solution for a floating longline mussel farm based on energy conserva-
tion equation with linear wave theory (Dalrymple et al., 1984). They
represented random wave conditions using root-mean square wave
height and peak wave period. Zhu and Zou (2017) extended the two-
layer solution by Kobayashi et al. (1993) for submerged vegetation
to a generalized three-layer theoretical solution for suspended and
submerged vegetation. Zhu and Zou (2017) found that the wave atten-
uation by a submerged canopy decreases while the wave attenuation by
a floating canopy increases with increasing wave frequency. The wave
attenuation by a suspended canopy first increases and then decreases
with increasing wave frequency. Combining an OpenFOAM (Higuera
et al., 2013) hydrodynamics model with an immersed element vege-
tation model, Chen and Zou (2019) observed a strong jet formed at
the top of a submerged flexible canopy in the opposite direction as the
wave. Using a SWASH (Simulating WAves till SHore, Zijlema et al.,
2011) model, Chen et al. (2019) investigated the wave-driven circu-
lation cell induced by suspended canopies and found that the vertical
position of the canopy also has significant effects on the wave-driven
current in the canopy. Recently, SWASH was improved by Suzuki et al.
(2019) to consider the drag of horizontal vegetation stems, vegetation
canopy porosity and vegetation inertia, which can influence the wave
dissipation. The effects of vegetation porosity on wave dissipation is of
importance for dense vegetation. As time domain numerical models,
OpenFOAM and SWASH are able to simulate waves with arbitrary
frequency shape. However, the existing analytical models developed
for suspended canopies in single characteristic frequency waves still
need to be extended to frequency dependent models for random waves,
which are a better representation of field conditions.

The objective of this study is to develop a generalized three-layer
frequency dependent theoretical model for random wave attenuation
by submerged and suspended canopies. The analytical wave attenua-
tion model is coupled with cantilever-beam and buoy-on-rope vegeta-
tion models to consider the motion of canopies with different type com-
ponents. The coupled flow and vegetation model is validated with lab-
oratory experimental datasets for submerged canopies (Jacobsen et al.,
2019) and laboratory and field datasets for suspended canopies (Sey-
mour and Hanes, 1979). The validated coupled model is then ap-
plied in the field near Saco, Maine in the Northeastern USA to in-
vestigate the potential of a mussel farm to damp storm during the
January 2015 North American blizzard. The effectiveness of using a
suspended aquaculture farm alone and in combination with submerged
aquatic vegetation (SAV) close to shore for wave attenuation is also
investigated.

2. Theory

2.1. Background on analytical wave attenuation models

Theoretical models have been developed to study the wave attenua-
tion characteristics of submerged and emergent canopies by Dalrymple
et al. (1984) and Kobayashi et al. (1993). Both studies represented the
canopy as arrays of rigid, homogeneous cylinders subject to monochro-
matic wave action. Assuming the wave energy loss as the work per-
formed by the drag of vegetation, Dalrymple et al. (1984) obtained
the wave decay coefficient by solving the energy conservation equation

CoastalEngineering160(2020)1037372L. Zhu et al.

using linear wave theory. By solving the linearized incompressible Eu-
ler equations with assumptions of exponentially decayed wave height
along the canopy and linearized drag, Kobayashi et al. (1993) obtained
the same wave decay coefficient as Dalrymple et al. (1984). The wave
decay coefficient is an explicit function of hydrodynamic conditions
and canopy characteristics including blade length, width, and canopy
density (defined as blade number per unit area).

Both these analytical solutions have been widely used for calculat-
ing wave attenuation by submerged vegetation. The solution by Dal-
rymple et al. (1984) was modified by Mendez and Losada (2004) to
consider random non-breaking and breaking waves propagating over a
mildly sloped vegetation seabed by using the unmodified Raleigh dis-
tribution method and assuming a narrow-banded wave spectrum. The
modification developed by Mendez and Losada (2004) has been imple-
mented in the SWAN (Simulating WAves Nearshore) model by Suzuki
et al. (2012), and the MDO (Mellor–Donelan–Oey) wave model for
wind-generated waves and swells in deep and shallow waters by Mar-
sooli et al. (2017). Recently, Losada et al. (2016) extended Mendez
and Losada (2004) solution for combined wave and currents. The
solution by Mendez and Losada (2004) was also used by Garzon et al.
(2019) to analyze the wave attenuation by Spartina Saltmarshes in the
Chesapeake Bay under storm surge conditions. These models based on
the Mendez and Losada (2004) approach are limited to ideal narrow-
banded waves. If applied to wide-banded waves, the Mendez and
Losada (2004) based models would overestimate the dissipation for the
wave components with higher frequency than the characteristic peak
frequency and underestimate the dissipation for the wave components
with lower frequency than the characteristic peak frequency (Jacobsen
et al., 2019).

√

To investigate the spectral distribution of energy dissipation, Chen
and Zhao (2012) developed two analytical frequency dependent wave
attenuation models for random waves and rigid vegetation by im-
plementing the energy dissipation of random waves in Hasselmann
and Collins (1968) and the joint distribution of wave heights and
wave periods proposed by Longuet-Higgins (1983). To derive the wave
attenuation solution based on the random waves in Hasselmann and
Collins (1968), Chen and Zhao (2012) used the root mean square
velocity to linearize the drag force following Madsen et al. (1988) such
2𝜎𝑢, where 𝑢 is the horizontal wave velocity and 𝜎𝑢 is the
that |𝑢| ≈
standard deviation of 𝑢. Recently, Jacobsen et al. (2019) obtained a
frequency distributed wave dissipation model by linearizing the drag
force such that |𝑢| ≈
8∕𝜋𝜎𝑢 estimated from 270,000 numerical cases
under JONSWAP spectrum so the linearization-induced mean error
|
|𝑢|∕
|
|
|
8∕𝜋𝜎𝑢 by minimizing the mean square of the dif-
same result |𝑢| ≈
ference between the nonlinear drag and linearized drag for 𝑢 in normal
distribution. The Borgman (1967) method for the drag linearization can
also be used for other probability distributions of 𝑢.

is less than 0.01%. Borgman (1967) obtained the

8∕𝜋𝜎𝑢

|
|
|
|
√

(√

− 1

√

)

Since most vegetation are flexible, the wave-induced motion of
vegetation would reduce the relative velocity between wave-induced
flow and vegetation and therefore the drag force, yielding less wave
attenuation than rigid vegetation (Mullarney and Henderson, 2010; van
Veelen et al., 2020). To consider the effects of vegetation motion, one
common practice is using a reduced bulk drag coefficient (e.g., Paul
and Amos, 2011; Jadhav et al., 2013; Pinsky et al., 2013; Anderson
and Smith, 2014; Hu et al., 2014; Zeller et al., 2014; Möller et al.,
2014; Losada et al., 2016; Wu et al., 2016; Marsooli et al., 2017;
Nowacki et al., 2017; Garzon et al., 2019; van Veelen et al., 2020). The
bulk drag coefficient should be dependent on the Cauchy number (𝐶𝑎)
incorporating the blade flexural rigidity related to vegetation motion.
However, most of the empirical formulas in literature for the bulk
drag coefficient of flexible vegetation are expressed as a function of
Reynolds number (𝑅𝑒) or Keulegan–Carpenter number (𝐾𝐶) without
incorporating the blade flexural rigidity. Consequently, the empirical
formulas of bulk drag coefficient have different expressions for vege-
tation with different flexural rigidities for the same set of 𝑅𝑒 and 𝐾𝐶

numbers. This introduces uncertainty in modeling wave attenuation by
flexible vegetation. To apply the original (unreduced) drag coefficient
as previous studies and incorporate the effects of blade motion at the
same time, Luhar et al. (2017) proposed a reduced, effective blade
length instead of a reduced drag coefficient to incorporate the effects
of blade motion. The empirical formula for the effective blade length is
dependent on blade flexural rigidity, therefore, can be readily applied
to vegetation of various flexural rigidities. The formula for the effective
blade length was recently modified by considering the effects of rigid
sheath of seagrass (Lei and Nepf, 2019b) and applied to combined
waves and currents conditions (Lei and Nepf, 2019a). These empirical
approaches do not need to resolve blade motion and therefore improve
the computational efficiency by reducing the iterative computation for
coupling wave and vegetation motion. These approaches, however,
require numerous datasets to derive the formulas for bulk drag co-
efficient and effective blade length. If the blade motion is directly
resolved by the model, then the original unreduced drag coefficient
and blade length can be used directly without modification. Therefore,
the number of experiments and model runs to calibrate the bulk drag
coefficient and the uncertainty associate with the bulk drag coefficient
are reduced.

To resolve the blade motion, Asano et al. (1992) simplified the
blade motion as an oscillator with one degree of freedom by assum-
ing blade deflection is linearly distributed along the length and also
averaging deflection along the length. This method was then extended
to consider irregular waves, wave reflection, and evanescent modes
by Méndez et al. (1999) for submerged vegetation. To analyze the
depth dependence of the blade deflection as well as its effects on wave
dissipation, Mullarney and Henderson (2010) modeled the blade as a
continuous beam with Euler–Bernoulli techniques, where the governing
equation for the blade motion is simplified as a balance between the
flexural rigidity-induced restoring force and the drag force, assuming
the inertia force and buoyancy are negligible. Recently, Henderson
(2019) extended this model by including buoyancy but still neglected
the inertia force, therefore the model is valid only for blades with
small cross sectional area. In addition, the mass of vegetation influences
the natural frequency of the vegetation and further impacts the blade
motion as well as the resonant conditions. To fully consider the grav-
ity, buoyancy, structural damping, bending stiffness, virtual buoyancy,
friction, drag and inertia forces, numerical models are often used to
simulate the blade dynamics (e.g., Zeller et al., 2014; Zhu and Chen,
2015; Luhar and Nepf, 2016; Leclercq and de Langre, 2018; Zhu et al.,
2018; Chen and Zou, 2019; Zhu et al., 2020). Recently, Zhu et al.
(2020) used a cable model to capture the asymmetric ‘‘whip-like’’ blade
motion and proposed mechanisms for the asymmetric blade motion in
symmetric waves.

To derive a generalized wave attenuation model for suspended
and submerged canopies, the water column is divided into 3 layers
with model set-up in Section 2.2. The effects of canopy motion are
incorporated by resolving the motion of individual canopy component
using a cantilever-beam model or a buoy-on-rope model based on the
type of the canopy component in Section 2.3. These two structural
dynamics models consider inertia force and are therefore applicable
for large diameter structure such as mussel droppers. The frequency
dependent theoretical wave attenuation model incorporating canopy
motion is developed in Section 2.4.

2.2. Model set-up

The mathematical approach is based on the three-layer model set-
up shown on Fig. 2. As shown on Fig. 2, the horizontal coordinate,
𝑥, is positive in the direction of wave propagation (assumed to be
perpendicular to the coast), with 𝑥 = 0 at the leading edge of the
canopy. The horizontal length of the canopy is defined as 𝐿𝑣 such that
𝑥 = 𝐿𝑣 at the end of the canopy. The vertical coordinate, 𝑧, is positive
upward with 𝑧 = 0 at the still water level (SWL).

CoastalEngineering160(2020)1037373L. Zhu et al.

Fig. 2. Definition sketch of variables and coordinate system for the three-layer
theoretical model of waves propagating over a canopy. The coordinate system (𝑥, 𝑧)
with the origin at the leading edge of the canopy (𝑥 = 0) and the still water level
(SWL, 𝑧 = 0), where 𝑥 is positive in the wave propagation direction from left to right
and 𝑧 is positive upward. The water column is divided into three layers by the canopy.
The thicknesses of layer 1, 2, and 3 are denoted as 𝑑1, 𝑑2, and 𝑑3, respectively. The
canopy length is 𝐿𝑣. The water depth from the SWL is defined as ℎ = 𝑑1 + 𝑑2 + 𝑑3.

The water column is divided into three layers with Layer 1 above
the canopy, Layer 2 within the canopy, and Layer 3 below the canopy.
The initial static thicknesses for each layer are denoted by 𝑑1, 𝑑2, 𝑑3,
respectively. The thickness of Layer 2 (𝑑2) also named the canopy
height, is defined as the average submerged length of the canopy
components. The water depth from the SWL is defined as ℎ = 𝑑1 +
𝑑2 + 𝑑3, where the seafloor is located at 𝑧 = −ℎ and assumed to be
horizontal. This generalized three-layer model can be used to analyze
the wave attenuation characteristics of the following four types of
≠ 0 and 𝑑3 = 0), (2) emergent
canopy configurations: (1) submerged (𝑑1
≠ 0 and
(𝑑1 = 0 and 𝑑3 = 0), (3) suspended in the water column (𝑑1
𝑑3

≠ 0), and (4) floating on the surface (𝑑1 = 0 and 𝑑3
At many sites, sea surface profiles are better represented by random
waves, which can be formulated as a superposition of monochromatic
waves with a set of random phases. Thus, the water elevation can be
expressed as

≠ 0).

𝜂 =

∞
∑

𝑖=1

𝑎𝑖 cos

(𝑘𝑖𝑥 − 𝜔𝑖𝑡 + 𝜓𝑖

) ,

(1)

where 𝑡 is time, 𝑎𝑖 is the wave amplitude, 𝑘𝑖 is the wave number,
𝜔𝑖 is the angular frequency and 𝜓𝑖 is the random phase of the 𝑖th
monochromatic wave component. As a sum of infinite independent ran-
dom variables, the water elevation tends toward a normal distribution
according to the central limit theorem. Assuming that the random phase
is distributed uniformly on (0, 2𝜋), the water elevation is normally
distributed with a zero mean (⟨𝜂⟩ = 0, where ⟨ ⟩ indicates expected
⟨𝜂2⟩
value) and a variance of 𝜎2
0 𝑆𝜂𝜂(𝜔, 𝑥)𝑑𝜔,
where 𝑆𝜂𝜂(𝜔, 𝑥) is the wave spectrum. For the convenience of expres-
sion, the index of summation 𝑖 is omitted and 𝜔 is used to indicate the
summation such that

𝑖 ∕2 = ∫ ∞

= ∑∞

𝑖=1 𝑎2

𝜂 =

𝜂 =

∑

𝜔

𝑎(𝑘𝑥 − 𝜔𝑡 + 𝜓).

(2)

According to linear wave theory (Dean and Dalrymple, 1991), the wave
number and angular frequency satisfy the dispersion relation, 𝜔2 =
𝑔𝑘 tanh 𝑘ℎ, where 𝑔 is the gravitational acceleration. The wave orbital
velocity (𝑢) at a given level 𝑧 is then written as

𝑢 =

∑

𝜔

𝑎𝜔𝛤 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓),

(3)

where 𝛤 = cosh 𝑘(ℎ + 𝑧)∕ sinh 𝑘ℎ when 𝑧 ≤ 𝜂 and 𝛤 = 0 when 𝑧 > 𝜂.

Fig. 3. Sketch for the cantilever-beam model and buoy-on-rope model for different
species.

2.3. Models for the motion of canopy components

The wave-induced motion of a canopy component is simulated by
different models depending on the morphology and physical properties
of the species. In this paper, we introduce cantilever-beam and buoy-
on-rope models. The cantilever-beam model is applicable for slender
species such as vegetation blades, kelp blades, and mussel droppers
(Fig. 3). The buoy-on-rope model is applicable for species with concen-
trated mass and buoyancy supported by a tethered stipe whose mass
and stiffness can be ignored, e.g., the bull kelp, Nereocystis luetkeana
(Fig. 3).

2.3.1. Cantilever-beam model

The individual component of the canopies such as seagrass meadow,
kelp forest and mussel farms is modeled as a slender cantilever beam
(Fig. 3), referred as a blade hereinafter. A typical blade having the av-
eraged geometrical and physical properties of the canopy components
is used to represent the canopy components. To simulate the large-
amplitude deflection of a flexible blade, Zhu et al. (2020) introduced
a cable model that can capture the asymmetric ‘‘whip like’’ motion
of a flexible blade (Luhar and Nepf, 2016). To obtain the analytical
solution for the horizontal displacement (𝜉) of the blade, the governing
equations in Zhu et al. (2020) are linearized by assuming a small-
amplitude motion such that the vertical displacement of the blade is
negligible. The horizontal displacement, 𝜉(𝑠, 𝑡) is a function of time
𝑡 and the distance 𝑠 along the blade length from the fixed end. The
relation between the local coordinate 𝑠 and the global coordinate 𝑧 is
given by
{

blade fixed at the bottom end,

blade fixed at the tip end.

(4)

𝑧 =

− 𝑑1 − 𝑑2 + 𝑠,
− 𝑑1 − 𝑠,

Neglecting tension and buoyancy, the linearized governing equation is
given by

𝜌𝑣𝐴𝑐

̈𝜉 + 𝐸𝐼𝜉′′′′ = 𝜌𝑤𝐴𝑐 ̇𝑢 +

1
2

𝐶𝑑 𝜌𝑤𝑏|𝑢 − ̇𝜉|(𝑢 − ̇𝜉) + 𝐶𝑚𝜌𝑤𝐴𝑐 ( ̇𝑢 − ̈𝜉),

(5)

where the dot ( ̇ ) indicates derivative with respect to 𝑡, the prime (′)
indicates derivative with respect to 𝑠, 𝜌𝑤 is the water density, 𝜌𝑣 is
the blade mass density, 𝑏 is the projected blade width, 𝐴𝑐 is the blade
cross sectional area, 𝐸 is the Young’s modulus of the blade, 𝐼 is second
moment of the blade cross sectional area, 𝐶𝑑 is the drag coefficient and
𝐶𝑚 is the added mass coefficient. The terms on the right-hand side of
(5) are virtual buoyancy, drag and added mass force per unit length
modified from the Morison formula (Morison et al., 1950). To obtain
an analytical solution to (5), the nonlinear drag 1∕2𝐶𝑑 𝜌𝑤𝑏|𝑢 − ̇𝜉|(𝑢− ̇𝜉) is
linearized as 𝑐(𝑢− ̇𝜉), where the linearization coefficient (𝑐) is calculated
using the Borgman (1967) method. Substituting (3) into (5) yields

CoastalEngineering160(2020)1037374(7)

(8)

(9)

L. Zhu et al.

𝑚 ̈𝜉 + 𝑐 ̇𝜉 + 𝐸𝐼𝜉′′′′ =

∑

𝜔

] ,
𝑎𝜔𝛤 [𝑐 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝜔𝑚𝐼 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓)

(𝜌𝑣 + 𝐶𝑚𝜌𝑤

(6)
) 𝜌𝑤𝐴𝑐 . The boundary
where 𝑚 =
conditions for a cantilever beam are given by 𝜉(0, 𝑡) = 0, 𝜉′(0, 𝑡) = 0,
𝜉′′(𝑙, 𝑡) = 0 and 𝜉′′′(𝑙, 𝑡) = 0. Using a normal mode approach (Rao, 2007),
the solution for the blade displacement is obtained in Appendix as

) 𝐴𝑐 and 𝑚𝐼 =

(
1 + 𝐶𝑚

𝜉 =

∑

𝜔

] ,
𝑎𝛤 [𝛾𝑠 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝛾𝑐 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓)

where 𝛾𝑠 and 𝛾𝑐 are the transfer functions given by

𝛾𝑠 =

and

𝛾𝑐 =

𝜔
𝛤

∞
∑

𝑛=1

𝜙𝑛

𝜔𝐼𝑛
(𝜆2

𝑛 − 𝜔2)
(𝜆2
𝑛 − 𝜔2)2
+

− 𝐷𝑛2𝜁𝑛𝜆𝑛𝜔
2𝜁𝑛𝜆𝑛𝜔)2
(

𝜔
𝛤

∞
∑

𝑛=1

𝜙𝑛

𝑛 − 𝜔2)
(𝜆2
𝑛 − 𝜔2)2
+

𝐷𝑛
(𝜆2
cos 𝜇𝑛𝑙 + cosh 𝜇𝑛𝑙) (
(

+ 𝜔𝐼𝑛2𝜁𝑛𝜆𝑛𝜔
2𝜁𝑛𝜆𝑛𝜔)2
(

,

+

sin 𝜇𝑛𝑠 − sinh 𝜇𝑛𝑠)

sin 𝜇𝑛𝑙 + sinh 𝜇𝑛𝑙)
(
where 𝜙𝑛 =
cosh 𝜇𝑛𝑠 − cos 𝜇𝑛𝑠)
(
is the 𝑛th normal mode of the cantilever beam with
𝜇𝑛 being the 𝑛th solution of 1 + cos 𝜇𝑙 cosh 𝜇𝑙 = 0, 𝜆𝑛
=
√
𝑛𝑑𝑠∕ ∫ 𝑙
∫ 𝑙
𝜇2
0 𝐸𝐼𝜙2
𝑛𝑑𝑠 is the 𝑛th natural frequency of the blade,
𝑛
0 𝑐𝛤 𝜙𝑛𝑑𝑠∕ ∫ 𝑙
2𝜁𝑛𝜆𝑛 = ∫ 𝑙
0 𝑚𝜙2
0 𝑐𝜙2
𝑛𝑑𝑠 and 𝐼𝑛 =
∫ 𝑙
0 𝑚𝐼 𝛤 𝜙𝑛𝑑𝑠∕ ∫ 𝑙
𝑛𝑑𝑠. Since 𝛤 is expressed in terms of 𝑧 and 𝜙𝑛 is
expressed in terms of 𝑠, the relation between 𝑠 and 𝑧 in (4) is required
to calculate the integral ∫ 𝑙

0 𝑚𝜙2
𝑛𝑑𝑠∕ ∫ 𝑙
0 𝑚𝜙2

𝑛𝑑𝑠, 𝐷𝑛 = ∫ 𝑙

0 𝑚𝜙2

0 𝛤 𝜙𝑛𝑑𝑠.

The relative velocity of flow to blade 𝑢𝑟 = 𝑢 − 𝜉 is given by
∑

1 + 𝛾𝑠

cos(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝛾𝑐 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓)

𝑎𝜔𝛤 [(

] .

)

𝑢𝑟 =

(10)

𝜔

According to the central limit theorem, the relative velocity also asymp-
totically approaches a normal distribution with zero mean (⟨𝑢𝑟⟩ = 0)
and the variance
∞
⟨𝑢2
𝑟

𝑆𝜂𝜂(𝜔, 𝑥)𝑑𝜔.

𝜔2𝛤 2 [(

1 + 𝛾𝑠

+ 𝛾 2
𝑐

(11)

)2

=

⟩

]

𝜎2
𝑢𝑟

= ∫

0

displacement of the buoy and the fluid velocity at the buoy center is
used to calculate the forces. The governing equation for buoy-on-rope
model is given by
(𝜌𝑤 − 𝜌𝑣
𝑅

𝜉 = 𝜌𝑤𝑉 ̇𝑢 (𝑧𝑐

𝜌𝑣𝑉 ̈𝜉 +

[𝑢 (𝑧𝑐

𝑢 (𝑧𝑐

) 𝑉 𝑔

− ̇𝜉]

+

)

)

)

− ̇𝜉|
|
|

1
2
+ 𝐶𝑚𝜌𝑤𝑉 [ ̇𝑢 (𝑧𝑐

𝐶𝑑 𝜌𝑤𝐴𝑝
− ̈𝜉] ,
)

|
|
|

(14)

where 𝑅 is the length of the tethered rope, 𝑉 is the volume of the
buoy with projected area of 𝐴𝑝. Similarly, the nonlinear drag force
1∕2𝐶𝑑 𝜌𝑤𝐴𝑝
, where
𝐶 is obtained using the Borgman (1967) method. Substituting (3) into
(14) yields

is linearized as 𝐶 [𝑢 (𝑧𝑐

[𝑢 (𝑧𝑐

− ̇𝜉|
|
|

𝑢 (𝑧𝑐

− ̇𝜉]

− ̇𝜉]

|
|
|

)

)

)

𝑀 ̈𝜉 + 𝐶 ̇𝜉 + 𝐾𝜉 =

∑

𝜔

𝑎𝜔𝛤 (𝑧𝑐

] ,
) [𝐶 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝜔𝑀𝐼 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓)

(15)

where 𝑀 = (𝜌𝑣 + 𝐶𝑚𝜌𝑤)𝑉 , 𝐾 = (𝜌𝑤 − 𝜌𝑣)𝑉 𝑔∕𝑅, and 𝑀𝐼 = (1 + 𝐶𝑚)𝜌𝑤𝑉 .
The solution for (15) is

𝜉 =

∑

𝜔

] ,
𝑎𝛤 [𝛾𝑠 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝛾𝑐 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓)

where 𝛾𝑠 and 𝛾𝑐 are the transfer functions given by

𝛾𝑠 =

and

𝛾𝑐 =

) 𝜔

𝛤 (𝑧𝑐
𝛤 𝑀

𝜔𝑀𝐼

(𝜆2 − 𝜔2)

− 𝐶(2𝜁𝜆𝜔)

(𝜆2 − 𝜔2)2

+ (2𝜁𝜆𝜔)2

) 𝜔

𝛤 (𝑧𝑐
𝛤 𝑀

𝐶 (𝜆2 − 𝜔2)
(𝜆2 − 𝜔2)2

+ 𝜔𝑀𝐼 (2𝜁𝜆𝜔)

,

+ (2𝜁𝜆𝜔)2

(16)

(17)

(18)

√

𝐾∕𝑀 and 2𝜁𝜆 = 𝐶∕𝑀. Similarly, the relative velocity
where 𝜆 =
𝑢𝑟 = 𝑢 − ̇𝜉 asymptotically approaches a normal distribution with zero
mean and the variance 𝜎2
in a similar expression as (11) except for the
𝑢𝑟
transfer functions 𝛾𝑠 and 𝛾𝑐, which are calculated using (17) and (18).
Thus, the linearization coefficient (𝐶) is given by

𝐶 =

1
2

𝐶𝑑 𝜌𝑤𝐴𝑝

√

8
𝜋

𝜎𝑢𝑟

,

(19)

Hence, the probability density function of 𝑢𝑟 is given by

)

𝑝 (𝑢𝑟

=

1
√

2𝜋

𝜎

𝑢𝑟

𝑢2
𝑟
2𝜎2
𝑢𝑟 .

−
𝑒

which is obtained iteratively using the same procedure for the
cantilever-beam model.

(12)

2.4. Solutions for random wave attenuation

Using the Borgman (1967) method, the linearization coefficient (𝑐) is
obtained by minimizing the mean square difference between the non-
)
)2 𝑝 (𝑢𝑟
linear and linearized drag so that 𝜕 ∫ ∞
−∞
𝑑𝑢𝑟∕𝜕𝑐 = 0, yielding

(
𝑢𝑟|
1∕2𝐶𝑑 𝜌𝑤𝑏 |
|
|

𝑢𝑟 − 𝑐𝑢𝑟

𝑐 =

1
2

𝐶𝑑 𝜌𝑤𝑏

𝑟 𝑝 (𝑢𝑟
∫ ∞
𝑢2
𝑢𝑟|
−∞ |
|
|
𝑟 𝑝 (𝑢𝑟
∫ ∞
−∞ 𝑢2

) 𝑑𝑢𝑟
) 𝑑𝑢𝑟

=

1
2

𝐶𝑑 𝜌𝑤𝑏

√

8
𝜋

𝜎𝑢𝑟

.

(13)

The linearization coefficient can be obtained iteratively through the
following procedure. Starting from a static blade, an initial 𝑐 is cal-
culated from Eq. (13) with (11) by assuming 𝛾𝑠 = 0 and 𝛾𝑐 = 0. Once
the blade displacement is obtained, 𝑐 can be recalculated from (13) and
(11) with (8) and (9). Using the new value of 𝑐, the blade displacement
can be updated. The procedure is repeated until a convergent solution
is achieved.

2.3.2. Buoy-on-rope model

The bull kelp (Nereocystis luetkeana) is used as an example to
describe the buoy-on-rope model (Denny et al., 1997), which is also
used for other species such as Macrocystis pyrifera (Utter and Denny,
1996). The pneumatocyst (the ball-shape ‘‘float’’ structure) of Nere-
ocystis luetkeana is modeled as a buoy and the stipe is modeled as
a rope (Fig. 3). Therefore, the canopy component is modeled as a
buoy attached to seabed by a thin, straight, non-buoyant rope. The
inertia, drag and buoyancy act at the buoy center, 𝑧𝑐 = −𝑑1 − 𝑑2∕2,
where the canopy height 𝑑2 is the diameter of the buoy. The horizontal

Following Dalrymple et al. (1984), Kobayashi et al. (1993), and
Mendez and Losada (2004), the wave attenuation is assumed to come
from the work of the canopy-induced drag force. The inertia force has
a negligible contribution to wave attenuation since the mathematical
expectation of the work due to the inertia force is zero because the
relative acceleration and the relative velocity are out of phase in
linear waves. The vertical frictional force is assumed negligible when
compared with the horizontal drag force. The wave reflection from
the canopy is also assumed negligible since the wave reflection has
limited contributions to the wave attenuation for both submerged veg-
etation (Mendez and Losada, 2004) and suspended canopies (Seymour
and Hanes, 1979). Some wave energy is converted into the kinematic
and potential energy of the canopy at the beginning. However, once
the canopy motion becomes steady, the energy needed to maintain
the steady motion can be assumed negligible because the structural
damping of the canopy components is negligible (Asano et al., 1992;
Méndez et al., 1999). Lacking data, the velocity reduction in the
canopy (Lowe, 2005), the sheltering effects (Raupach and Thom, 1981;
Abdelrhman, 2007; Etminan et al., 2019), and the porosity effects (Mei
et al., 2011; Nepf, 2011; Liu et al., 2015; Arnaud et al., 2017; Suzuki
et al., 2019) are not considered. Using the linearized drag force, the
energy conservation equation can be written as

∞

𝜕
𝜕𝑥 ∫
0

𝜌𝑤𝑔𝑆𝜂𝜂(𝜔, 𝑥)𝑐𝑔𝑑𝜔 = − ∫

⟨

−𝑑1

𝑁

1
2

𝐶𝑑 𝜌𝑤𝑏

√

⟩

8
𝜋

𝜎𝑢𝑟

𝑢2
𝑟

𝑑𝑧,

(20)

−𝑑1−𝑑2

CoastalEngineering160(2020)1037375L. Zhu et al.

where 𝑐𝑔 = (𝜔∕𝑘)(1 + 2𝑘ℎ∕ sinh 2𝑘ℎ)∕2 is the group velocity and 𝑁
is the number of canopy components per unit horizontal area (also
referred to as the canopy density). Substituting (11) into (20) yields
the transmitted wave spectrum at distance 𝑥 in relation to the incident
wave spectrum at 𝑥 = 0,

𝑆𝜂𝜂(𝜔, 𝑥) = 𝑆𝜂𝜂(𝜔, 0)𝑒−2𝛽(𝜔)𝑥,

(21)

where the frequency dependent decay coefficient (𝛽) is given by

𝛽(𝜔) =

√
2
√

2𝑁𝑘2 sinh2 𝑘ℎ
𝜋𝜔(2𝑘ℎ + sinh 2𝑘ℎ)

−𝑑1

∫

−𝑑1−𝑑2

𝐶𝑑 𝑏𝜎𝑢𝑟

𝛤 2 [(

1 + 𝛾𝑠

]

)2

+ 𝛾 2
𝑐

𝑑𝑧.

(22)

The transfer functions 𝛾𝑠 and 𝛾𝑐 are selected based on the structural
dynamics model used for the canopy motion. To evaluate the effect of
the canopies on wave attenuation, the wave spectral dissipation ratio
(𝑆𝐷𝑅) and wave energy dissipation ratio (𝐸𝐷𝑅) are used and defined
as

𝑆𝐷𝑅 = 1 −

and

𝐸𝐷𝑅 = 1 −

)

(𝜔, 𝐿𝑣
𝑆𝜂𝜂
𝑆𝜂𝜂(𝜔, 0)

) 𝑑𝜔
(𝜔, 𝐿𝑣
∫ ∞
0 𝑆𝜂𝜂
∫ ∞
0 𝑆𝜂𝜂(𝜔, 0)𝑑𝜔

,

respectively.

3. Model-data comparison

3.1. Submerged canopy

(23)

(24)

The model results were first compared with the laboratory exper-
iments by Jacobsen et al. (2019) for a submerged canopy consisting
of artificial vegetation. The wave conditions were based on a single
peaked JONSWAP spectrum with a peak enhancement factor 𝛾 = 3.3
and peak wave period 𝑇𝑝 = 1.15 s. The incident significant wave height
at the leading edge of the canopy was 𝐻𝑠0 = 3.7 cm. The water depth
was ℎ = 0.685 m.

The artificial vegetation was made of 4 mm-wide polypropylene
blades with 𝜌𝑣 ≈ 920 kg/m3 and 𝐸 ≈ 0.3 GPa (Ghisalberti and Nepf,
2002). Four blades were taped to a 6 mm-diameter PVC dowel and
60 mm above the bed. The canopy was 7.5 m long with a density of
566 dowels/m2 therefore 2264 blades/m2. The blade length was 20, 40,
and 60 cm such that 𝑑2∕ℎ = {0.38, 0.67, 0.96}. The blade thickness was
0.12, 0.2, 0.5 and 1.0 mm for the 20 cm-long blade and 0.5 mm for the
other blades. More details of the experiments can be found in Jacobsen
et al. (2019).

Based on the datasets for rigid flat plates in oscillatory flows (Keule-
gan and Carpenter, 1958; Sarpkaya and O’Keefe, 1996) with 1.7 ≤
𝐾𝐶 ≤ 118.2, Luhar and Nepf (2016) derived the drag coefficient and
added mass coefficient,

𝐶𝑑 = max(10𝐾𝐶 −1∕3, 1.95)

and

𝐶𝑚 = min(𝐶𝑚1, 𝐶𝑚2),

(25)

(26)

{ 1 + 0.35𝐾𝐶 2∕3, 𝐾𝐶 < 20,
1 + 0.15𝐾𝐶 2∕3, 𝐾𝐶 ≥ 20

and 𝐶𝑚2 = 1 + (𝐾𝐶 −
where 𝐶𝑚1 =
18)2∕49 as described in Luhar (2012). Eqs.(25) and (26) are robust in
calculating the hydrodynamic forces acting on flexible blades in regular
waves (Zhu et al., 2020). To apply (25) and (26) to random waves, the
𝐾𝐶 number is calculated using the significant relative velocity (2𝜎𝑢𝑟
)
as 𝐾𝐶 = 2𝜎𝑢𝑟

𝑇𝑝∕𝑏.

The vegetation blade is modeled as a cantilever beam so that the
wave attenuation model incorporating the cantilever beam model is
used to calculate the wave decay coefficient, 𝛽. The model results using
frequency dependent 𝐶𝑑 and 𝐶𝑚 in (25) and (26) as well as constant

𝐶𝑑 = 1.95 and 𝐶𝑚 = 1 are compared with the datasets of Jacobsen
et al. (2019) on Fig. 4. It is noted that 𝐶𝑑 = 1.95 is the minimum drag
coefficient for (25).

The model results are in a good agreement with the data with
the root-mean-square-error (RMSE) of about 0.002 for the 20 cm-long
blades (𝑙∕ℎ = 0.38) with thickness 𝑑 ≤ 0.5 mm (Fig. 4a–c). For the
thickest blades with 𝑑 = 1 mm, the decay coefficient is slightly overesti-
mated for the lower frequency wave components (𝑓 < 0.8 Hz) resulting
in a larger RMSE of 0.0032 (Fig. 4d). One possible reason is that the
drag coefficient calculated using Eq. (25) might be overestimated for
the thicker blades whose thickness–width ratio has reached 0.25 and
much larger than the thickness–width ratio (< 0.1) of the experimental
plates for the formula (25). The thicker blades are expected to have a
smaller drag coefficient due to increased Reynolds number. Thus, the
model results can be improved by using a smaller drag coefficient. For
instance, the RMSE for the 1 mm-thick blades is reduced to 0.0016 by
using 𝐶𝑑 = 1.95 (Fig. 4d).

For the longer blades that are nearly emergent (𝑙∕ℎ ≥ 0.67), the
model results calculated with frequency dependent hydrodynamic coef-
ficients underestimate the observation with RMSE=0.0046 and 0.0073
for 𝑙 = 40 cm (𝑙∕ℎ = 0.67) and 60 cm (𝑙∕ℎ = 0.96), respectively,
as shown on Fig. 4(e and f) possibly due to the simplification of
the cantilever beam model. Neglecting the large deflection-induced
geometrical non-linearity, net buoyancy, and the net buoyancy-induced
tension would underestimate the restoring capacity of the blades. Thus,
the simplified model may overestimate the blade motion resulting in
a smaller wave attenuation. This underestimation of wave attenuation
is more obvious for longer blades because the effects of the large
deflection-induced geometrical non-linearity, the net buoyancy and the
net buoyancy-induced tension are more significant for longer blades.
Compared to the shorter blade (𝑙 = 20 cm), the longer blade (𝑙 ≥ 40
cm) is more flexible, therefore, the blade motion follows the flow
more closely so that the relative velocity between the longer blade
and flow is smaller, resulting in a larger 𝐶𝑑 . Therefore, using a smaller
𝐶𝑑 = 1.95 enhances the underestimation as indicated by RMSE=0.0055
and 0.0177 for the 𝑙 = 40 cm (𝑙∕ℎ = 0.67) and 60 cm (𝑙∕ℎ = 0.96),
respectively on Fig. 4(e and f). A more precise formula for the hydrody-
namic coefficients in random waves is desired for the nearly emergent
canopies with 𝑙∕ℎ ≥ 0.67. However, the hydrodynamic coefficients in
(25) and (26) as well as the constant hydrodynamic coefficients work
well for the submerged vegetation (𝑙∕ℎ ≤ 0.38) with a small RMSE of
about 0.002.

3.2. Suspended canopy

The model results were also compared with the laboratory and field
experiments by Seymour and Hanes (1979) for a suspended canopy
consisting of spherical buoys. The field experiments for a suspended
canopy consisting of arrays of tethered sphere buoys (Fig. 5) were
conducted in San Diego Bay, California, USA. The half-scale model tests
for the field experiments were conducted in the 40-m long Wind Wave
Channel at the Hydraulics Laboratory of Scripps Institution of Oceanog-
raphy (Seymour and Hanes, 1979). The properties of the canopies in the
laboratory and field experiments are shown in Table 1.

For the laboratory experiments, the incident significant wave height
was 0.069–0.176 m and the peak frequency was 0.19–0.883 Hz. For the
field experiments, two storms were observed on Jan 22, 1976 and Feb
9, 1976. The measured significant wave height was 0.17–0.44 m. The
drag coefficient and added mass coefficient for the tethered spheres are
assumed as 𝐶𝑑 = 0.5 and 𝐶𝑚 = 0.5, respectively.

The calculated transmitted wave spectrum and spectral dissipation

ratio (𝑆𝐷𝑅) are shown on Fig. 6.

The calculated transmitted wave spectrum follows the shape of the
incident wave spectrum. The 𝑆𝐷𝑅 for the suspended canopy first in-
creases and then decreases with increasing wave spectrum as expected.

CoastalEngineering160(2020)1037376L. Zhu et al.

Fig. 4. Comparisons of calculated frequency (𝑓 ) dependent wave decay coefficient (𝛽) by the present model and the data (black dotted lines) from Jacobsen et al. (2019). The
model results using frequency dependent and constant drag coefficient (𝐶𝑑 ) and added mass coefficient (𝐶𝑚) are denoted by red solid and blue dashed lines, respectively. The
submerged canopies with blade lengths (𝑙) of 20, 40 and 60 cm and thicknesses (𝑑) of 0.12, 0.20, 0.5 and 1.0 mm are subjected to random waves of JONSWAP spectrum with
peak enhancement factor 𝛾 = 3.3, peak wave period 𝑇𝑝 = 1.15 s (vertical dashed black line) and incident significant wave height of 3.7 cm at a water depth ℎ = 0.685 m with
normalized blade length (𝑙∕ℎ) of 0.38 (a–d), 0.67 (e) and 0.96 (f). The canopy density is 566 shoots/m2(2264 blades/m2).

Table 1
Properties for the suspended canopies consisting of sphere components in the laboratory
and field experiments (Seymour and Hanes, 1979).

In the lab
(half scale)

In the field
(full scale)

Sphere mass density [kg/m3]
Sphere diameter [cm]
Depth of sphere center [cm]
Effective tether length [cm]
Sphere spacing (along canopy length) [cm]
Sphere spacing (along canopy width) [cm]
Canopy width (perpendicular to wave direction) [m]
Canopy length (along wave direction) [m]
Water depth [m]

40
15.8
7.36 − 15.24
83.8
31.6
31.6
2.39
23
1.78

85
29.2
21.9
168.0
58.41
58.41
46
6
8

Fig. 5. Sketch of the suspended canopy consisting of sphere components according to
the description of Seymour and Hanes (1979).

The comparison between the calculated and measured energy dissi-
pation ratio (𝐸𝐷𝑅) is shown on Fig. 7. Good agreement (RMSE=0.073)
between model and data indicates that the present generalized ana-
lytical solutions are also applicable to suspended aquaculture farms
with simple structures in other forms, such as cylinders, as long as the
appropriate hydrodynamic coefficients are available.

4. Case study at the field site

The present frequency dependent theoretical model is now applied
to analyze the wave attenuation capacity of suspended aquaculture
farms at a field site and compared with that of submerged aquatic
vegetation, as well as a combination of these two nature-based shore
protection schemes.

The study site (42◦28′2′′N, 70◦21′2′′W) is located at Saco Bay, Maine,
USA as shown on Fig. 8 with a water depth of about 10.6 m. The
January 2015 North American blizzard was a powerful and destructive
extratropical storm that swept across the Saco Bay and along the
coast of the Northeastern United States in January of 2015. To assess
coastal flood risk and sea level rise effects during this storm event, Xie
et al. (2019) constructed an integrated atmosphere-ocean-coast and
overtopping-drainage modeling framework based on the coupled tide,
surge and wave model, SWAN+ADCIRC. The wave spectrum and water
level conditions output from the SWAN+ADCIRC model (Xie et al.,
2019) are used to drive the present theoretical model. The canopies
are oriented to be parallel to the dominant wave direction so that the
present 1-D solutions can be applied.

CoastalEngineering160(2020)1037377L. Zhu et al.

Fig. 6. Comparisons between calculated and measured transmitted wave spectrum (𝑆𝜂𝜂 ) as well as spectral dissipation ratio (𝑆𝐷𝑅) versus wave frequency (𝑓 ) for suspended
canopies with spheres in (a) laboratory and (b) field experiments by Seymour and Hanes (1979). The incident significant wave height is 𝐻𝑠0 and the peak period is 𝑇𝑝.

hydrodynamic performances to the actual droppers. In this study, the
geometric and physical properties of the cylinders are based on the
measurements of the live droppers at the University of New Hamp-
shire nearshore multi-trophic aquaculture site in the Gulf of Maine,
USA (Knysh et al., 2020). The measured dropper diameter was 0.13
m, mass per unit length was 7.53 kg/m, and flexural rigidity was 0.79
N/m2 on July 3 (Knysh et al., 2020), which was about 160 days (years
are not considered) after the January 2015 North American blizzard
arrived at the study site. The geometrical properties of the droppers
in January were estimated by assuming a growth rate of 7.5% per 40
days (Lauzon-Guay et al., 2006; Gagnon and Bergeron, 2017), which
indicates that the diameter of the mussel dropper in January was about
75% of that in July. Therefore, the cylinder diameter was taken as
𝑏 = 0.10 m, the mass per unit length was assumed as 𝜌𝑣𝐴𝑐 = 4.46 kg/m,
and the flexural rigidity was assumed as 𝐸𝐼 = 0.28 N/m2. The cylinders
are assumed to be submerged half meter below the water surface so
that 𝑑1 = 0.5 m. The length of the mussel dropper is assumed as 𝑙 = 8
m following Plew et al. (2005) and Stevens et al. (2007) for a similar
water depth. A sparse configuration with 0.06 droppers/m2 (Plew et al.,
2005; Gagnon and Bergeron, 2017) and a dense configuration with
0.125 droppers/m2 (e.g., mussel droppers are 0.5 m apart and the
longline interval is about 16 m) are compared. Following Plew et al.
(2009), Dewhurst (2016) and Knysh et al. (2020), the drag coefficient
and added mass coefficient are assumed as 𝐶𝑑 = 1.3 and 𝐶𝑚 = 1,
respectively, which are also comparable to the values in Raman-Nair
and Colbourne (2003), Raman-Nair et al. (2008), Stevens et al. (2008),
Plew et al. (2009), Gagnon and Bergeron (2017) and Landmann et al.
(2019).

The SAV is modeled as a rectangular plate based on the properties
of Zostera marina, which is a common SAV in the Gulf of Maine,
USA (Mattila et al., 1999; Gaeckle and Short, 2002; Beal et al., 2004;
Neckles et al., 2005; Beem and Short, 2009; Newell et al., 2010). The
length of Zostera marina ranges from 10 to 150 cm and the shoot density
is about 50–1100 shoots/m2 with 3 − 7 blades per shoot (Abdelrhman,
2007; Beem and Short, 2009; Boström and Bonsdorff, 1997; Gaeckle
and Short, 2002; Mattila et al., 1999; Ondiviela et al., 2014). In
January, however, the averaged blade length of Zostera marina is about
16 cm (Gaeckle and Short, 2002; Ondiviela et al., 2014). Thus, the SAV
blade length is assumed as 16 cm. The corresponding blade width and
thickness as well as the sheath length and width are estimated using

Fig. 7. Comparisons between the calculated and measured wave energy dissipation
ratio (𝐸𝐷𝑅) for laboratory (blue + ) and field experiments (red ×) by Seymour and
Hanes (1979).

Fig. 8. The study site at Saco Bay, Maine, USA (Sources: Esri, GEBCO, NOAA, National
Geographic, DeLorme, HERE, Geonames.org, and other contributors).

4.1. Properties for the mussel farm and submerged aquatic vegetation

The mussel farm is simplified as arrays of cylinders which repre-
sent the mussel droppers. The cylinders have similar mechanical and

CoastalEngineering160(2020)1037378L. Zhu et al.

Table 2
Properties of the mussel farm and submerged aquatic vegetation (SAV) meadow.

Canopy component
Component properties

Mussel farm

Mussel dropper
Length: 8 m
Diameter: 0.10 m
𝐸𝐼 = 0.28 N/m2
𝜌𝑣𝐴𝑐 = 4.46 kg/m

Canopy density

Drag coefficient (𝐶𝑑 )
Added mass coefficient (𝐶𝑚)

Sparse: 0.060 droppers/m2
Dense: 0.125 droppers/m2
1.3
1

SAV

Zostera marina
Blade length: 0.16 m
Blade width: 3.7 mm
Blade thickness: 0.11 mm
Young’s modulus: 0.26 GPa
Mass density: 700 kg/m3
Sheath length: 8 cm
Sheath width: 3.4 mm
Sparse: 200 shoots/m2 (1000 blades/m2)
Sparse: 400 shoots/m2 (2000 blades/m2)
1.95
1

Fig. 9. Time evolution of (a) tide, storm tide and storm surge during the January 2015 North American blizzard, (b) significant wave height 𝐻𝑠0 and the corresponding peak
wave period 𝑇𝑝, (c) and (d) calculated wave energy dissipation ratio (𝐸𝐷𝑅) by the suspended mussel farm (thick blue lines) and submerged aquatic vegetation (SAV, thin red
lines) using the wave spectrum data. The canopy lengths are 𝐿𝑣 = 100 m in (c) and 𝐿𝑣 = 200 m in (d). The canopy densities are shown in the legend. (For interpretation of the
references to color in this figure legend, the reader is referred to the web version of this article.)

the empirical formula provided by Abdelrhman (2007), which yields
a blade width of 3.7 mm, blade thickness of 0.11 mm, sheath length
of 8 cm and sheath width of 3.4 mm. Following Abdelrhman (2007),
the mass density is assumed 𝜌𝑣 = 700 kg/m3. The Young’s modulus
is assumed 𝐸 = 0.26 GPa for the blades based on the measurements
by Fonseca et al. (2007). The sheath is considered rigid following Lei
and Nepf (2019b). A sparse SAV meadow with 200 shoots/m2 and a
dense meadow with 400 shoots/m2 are used in the study to investigate
the variation of wave attenuation with vegetation density. The number
of blades per shoot is assumed to be 5 so that there are 1000 blades/m2
for the sparse configuration and 2000 blades/m2 for the dense configu-
ration. Due to small blade width and large significant wave height and
peak period in a storm event, the calculated 𝐾𝐶 number is greater than
135, yielding a constant drag coefficient of 1.95 based on Eq. (25). The
data comparison in Section 3.1 has shown that 𝐶𝑑 = 1.95 and 𝐶𝑚 = 1

work well for submerged vegetation with 𝑙∕ℎ < 0.38 (Fig. 4). Therefore,
the drag coefficient and added mass coefficient are assumed 𝐶𝑑 = 1.95
and 𝐶𝑚 = 1, respectively, for this case study. The properties of the
mussel farm and SAV meadow are summarized in Table 2. In this study,
both mussel droppers and SAV are modeled as cantilever beams.

4.2. Mussel farm and SAV at the same water depth

The time evolution of tide, storm tide, storm surge at the study
site during the January 2015 North American blizzard is given by the
SWAN+ADCIRC model (Xie et al., 2019) and shown on Fig. 9(a). The
tidal range is around 3.3 m and the largest storm surge is about 0.8
m at the study site. The incident significant wave height (𝐻𝑠0) and
corresponding peak wave period (𝑇𝑝) for every 30 min are shown on
Fig. 9(b). At the study site during the storm, the significant wave height
reached 3.6 m with peak wave periods ranging from 5.2 s to 13.5 s.

CoastalEngineering160(2020)1037379L. Zhu et al.

Fig. 10. Comparisons of wave spectrum (𝑆𝜂𝜂 ) and wave spectral dissipation ratio (𝑆𝐷𝑅) versus wave frequency (𝑓 ) between the suspended mussel farm and submerged aquatic
vegetation (SAV) with different canopy densities (shown in legend) at 10:00 UTC (a), 16:00 UTC (b), and 22:00 UTC (c) on Jan 27. The canopy length is 200 m for both canopies.
The incident significant wave height and peak period are denoted by 𝐻𝑠0, and 𝑇𝑝, respectively.

The wave attenuation by the mussel farm and SAV at the same
still water depth of 10.6 m during the storm is calculated with the
wave spectral data from the SWAN+ADCIRC model. The calculated
wave energy dissipation ratio (𝐸𝐷𝑅) is shown on Fig. 9(c and d). The
𝐸𝐷𝑅 of both SAV and mussels increases with incident significant wave
height. However, the 𝐸𝐷𝑅 decreases with water level resulting in an
oscillating wave attenuation with the same period of the tidal cycle.
This periodic behavior is more obvious for SAV because the mussels
are less influenced by the tidal change since the mussels can move up
and down with the buoys. The largest wave attenuation value occurs at
the highest wave height during low tide. The larger (𝐿𝑣 = 200 m) and
denser (0.125 droppers/m2) mussel farm provides a more pronounced
wave attenuation with 𝐸𝐷𝑅 up to 0.32 (Fig. 9d), which is a bit more
than that of the same size (𝐿𝑣 = 200 m) but sparse (200 shoots/m2)
SAV with 𝐸𝐷𝑅 up to 0.26. However, for the denser (400 shoots/m2)
SAV with the same size (𝐿𝑣 = 200 m), the 𝐸𝐷𝑅 can reach to 0.45. For
the shorter period waves with 𝑇𝑝 < 9 s as shown on Fig. 9(c and d), the
mussel farm can damp more wave energy than the same size SAV since
SAV at the ocean bottom has little effect on wave attenuation for short
period waves whose energy is concentrated near the ocean surface.

The comparisons for the selected wave spectrum as well as the
associated spectral dissipation ratio (𝑆𝐷𝑅) at 10:00 UTC (high tide
with 𝐻𝑠0 = 2.9 m and 𝑇𝑝 = 9.2 s), 16:00 UTC (low tide with 𝐻𝑠0 = 3.5
m and 𝑇𝑝 = 13.5 s), and 22:00 UTC (high tide with 𝐻𝑠0 = 3.5 m
and 𝑇𝑝 = 13.5 s) on Jan 27 are shown on Fig. 10. The 𝑆𝐷𝑅 of the
suspended mussel farm increases with wave frequency until reaching
the maximum value, while the 𝑆𝐷𝑅 of SAV decreases with wave
frequency. As a result, the suspended mussel farm shows the advantage
of reducing higher frequency (shorter period) wave components over
SAV. For example on Fig. 10(a2) with smaller 𝐻𝑠0 and 𝑇𝑝, the 𝑆𝐷𝑅 of
the dense suspended mussel farm (0.125 droppers/m2) is larger than

that of dense SAV (400 shoots/m2) for 𝑓 > 0.12 Hz (wave period 𝑇 < 8.3
s) and sparse SAV (200 shoots/m2) for wave frequency 𝑓 > 0.055 Hz
(𝑇 < 18 s). The 𝑆𝐷𝑅 of the sparse suspended mussel farm (0.06
droppers/m2) is larger than that of the dense SAV for wave frequency
𝑓 > 0.16 Hz (𝑇 < 6.25 s) and sparse SAV for 𝑓 > 0.12 Hz (𝑇 < 8.3𝑠). As
𝐻𝑠0 and 𝑇𝑝 increases, the threshold value of the wave frequency where
the 𝑆𝐷𝑅 of suspended mussel farm is larger than that of SAV increases
to 𝑓 > 0.167 Hz (𝑇 < 6 s) for the dense mussel farm and the dense SAV,
𝑓 > 0.1 Hz (𝑇 < 10 s) for the dense mussel farm and the sparse SAV,
𝑓 > 0.21 Hz (𝑇 < 4.8 s) for the sparse mussel farm and the dense SAV,
and 𝑓 > 0.17 Hz (𝑇 < 5.9 s) for the sparse mussel farm and the sparse
SAV as shown on Fig. 10(b2). For the same 𝐻𝑠0 and 𝑇𝑝 at high tide, the
𝑆𝐷𝑅 of both the mussel farm and SAV decreases due to the increase
of water level. The threshold value of the wave frequency where the
𝑆𝐷𝑅 of suspended mussel farm is larger than that of SAV decreases to
𝑓 > 0.147 Hz (𝑇 < 6.8 s) for the dense mussel farm and the dense SAV,
𝑓 > 0.095 Hz (𝑇 < 10.5 s) for the dense mussel farm and the sparse
SAV, 𝑓 > 0.18 Hz (𝑇 < 5.5 s) for the sparse mussel farm and the dense
SAV, and 𝑓 > 0.15 Hz (𝑇 < 6.7 s) for the sparse mussel farm and the
sparse SAV as shown on Fig. 10(c2).

4.3. Mussel farm and SAV at different water depths

The previous section shows the advantages of suspended mussel
farms on damping high frequency wave energy over SAV at the same
water depth. Usually, SAV colonizes in shallower water as shown on
Fig. 1. To compare the performances of the suspended mussel farm
and the shallow water SAV meadow, the water depth for SAV is set
at 6 m so that maximum 𝐻𝑠0∕ℎ = 0.79 to avoid wave breaking.
The water depth for the suspended mussel farm keeps the same at
10.6 m. The wave shoaling is incorporated using shoaling coefficient

CoastalEngineering160(2020)10373710L. Zhu et al.

Fig. 11. (a) Comparisons of wave energy dissipation ratio (𝐸𝐷𝑅) between the suspended mussel farm and submerged aquatic vegetation (SAV). The canopy densities are 0.125
droppers/m2 for the suspended mussel farm and 200 shoots/m2 (1000 blades/m2) for the SAV meadow, respectively. The canopy length is 100 m for the SAV meadow. The canopy
length for the mussel farm is shown in the legend. (b1, c1, d1) The incident wave spectrum (𝑆𝜂𝜂 ) and (b2, c2, d2) Comparisons of wave spectral dissipation ratio (𝑆𝐷𝑅) versus
wave frequency (f) at 10:00 UTC (A), 16:00 UTC (B) and 22:00 UTC (C) on Jan 27. The incident significant wave height and peak wave period are denoted by 𝐻𝑠0, and 𝑇𝑝,
respectively.

𝐾𝑠(𝜔) = √𝑐𝑔𝑑 (𝜔)∕𝑐𝑔𝑠(𝜔) (Dean and Dalrymple, 1991), where 𝑐𝑔𝑑 (𝜔)
and 𝑐𝑔𝑠(𝜔) are the wave group speed at deeper and shallower water
depths, respectively. Correspondingly, 𝐸𝐷𝑅 and 𝑆𝐷𝑅 are calculated
using the shoaled wave energy and wave spectrum. The canopy density
is set as 200 shoots/m2 (1000 blades/m2) for SAV meadow and 0.125
droppers/m2 for the mussel farm. The canopy length for SAV meadow
is set as 𝐿𝑣 = 100 m. For the mussel farm, two canopy lengths of 100
m and 200 m are designed for comparison.

The wave attenuations of SAV and mussel farms as well as their
combinations are shown on Fig. 11. The wave attenuation by SAV
decreases dramatically with increasing water level while the suspended
mussel farm is less affected by the water level change. For example
(Fig. 11a), the 𝐸𝐷𝑅 of SAV decreases by 49% from 0.51 at low tide
(Jan 27 16:00 UTC) to 0.26 at high tide (Jan 27 22:00 UTC) with
water level increment of 2.5 m while the 𝐸𝐷𝑅 of the suspended mussel
farm decreases by 29%. The combination of the suspended mussel farm
and SAV provides a larger wave attenuation, especially for smaller
significant wave period and low tide (Fig. 11a). For example at 10:00
UTC on Jan 27 with 𝑇𝑝 = 9.2 s and 𝐻𝑠0 = 2.9 m, the 𝐸𝐷𝑅 of SAV and
a large mussel farm (𝐿𝑣 = 200 m) is 0.37, which is 1.5 times of the
𝐸𝐷𝑅 = 0.15 of SAV. Adding a small mussel farm (𝐿𝑣 = 100 m) to SAV
can also favorably improve the 𝐸𝐷𝑅 of SAV to 0.27 by 80%. As 𝐻𝑠0 and
𝑇𝑝 increases to 𝐻𝑠0 = 3.5 m and 𝑇𝑝 = 13.5 s, the improvements of the
wave attenuation of SAV by adding mussel farms are reduced because
the mussel farm is more effective for reducing shorter period waves.
However, the improvements still can reach up to 31% by adding a small
mussel farm and 54% by adding a large mussel farm. The improvements
of combined SAV and mussels hold for wave energy at all frequencies
by taking the advantage of the canopy density of SAV and the vertical
position of the suspended mussel as shown on Fig. 11(b2, c2 and d2).

5. Discussion

5.1. Wave attenuation characteristics of suspended aquaculture farms and
SAV

Wave attenuation occurs through the drag force which is deter-
mined by the horizontal wave orbital velocity. In shallow water waves,
the amplitude of the horizontal wave orbital velocity is almost uniform
with depth. Thus, the vertical position of the canopy has little effect
on attenuating shallow water waves. Taking the advantages of canopy
density, SAV can dissipate more wave energy than suspended mussel
farms for long period waves. However, the wave attenuation of SAV is
influenced by changes of water level. In shallow water, the wave at-
tenuation of SAV decreases dramatically during high tide, storm surge,
or storm tide (tide plus storm surge), which highlights the weakness of
SAV in protecting coastlines during large storm tide conditions. This
implies that severe erosion by storms may occur during high storm
tide levels (in addition, higher waves may arrive at the shore without
breaking during high tide). Therefore, living shorelines represented by
SAV would be less effective during extreme events.

Suspended aquaculture farms can work as living breakwaters to
protect the coast due to their capacity for wave attenuation. The wave
attenuation capacity of suspended aquaculture farms is mainly dictated
by the canopy density and the size (length) in the wave direction.
Unlike SAV, which is limited by water depth due to light and nutrients,
the vertical locations of suspended aquaculture farms can be adjusted
to optimize their growth. Consequently, there is no depth restriction
for suspended farms and they can be quite large, e.g., the suspended
mussel aquaculture farm off Gouqi Island in East China Sea has an area

CoastalEngineering160(2020)10373711L. Zhu et al.

Fig. 12. Relationship between the present solutions (22), (28), (29) and previous solutions by Chen and Zhao (2012), Jacobsen et al. (2019), and Mendez and Losada (2004),
where 𝛾𝑠 and 𝛾𝑐 are the transfer function for the motion of canopy component, 𝑑3 is the thickness of the gap between the canopy and sea bed, 𝑢 is the horizontal wave velocity
and 𝜎𝑢 is the stand deviation of 𝑢.

of about 8 km2 (Lin et al., 2016). In theory, the size of suspended aqua-
culture farms can be designed to achieve optimal wave attenuation. For
example, for the incident significant wave height (𝐻𝑠0) to be reduced
to the transmitted significant wave height (𝐻𝑠𝑇 ) that will allow the
living shorelines to thrive and mitigate coastal erosion, the size of the
aquaculture farms can be designed as

𝐻𝑠0
𝐻𝑠𝑇

,

(27)

) ln

𝐿𝑣 >

is the critical angular frequency such that ∫ ∞

1
𝛽 (𝜔𝑐
0 𝑆𝜂𝜂(𝜔, 0)
where 𝜔𝑐
𝑒−2𝛽(𝜔)𝐿𝑣 𝑑𝜔 = 𝑒−2𝛽(𝜔𝑐)𝐿𝑣 ∫ ∞
0 𝑆𝜂𝜂(𝜔, 0)𝑑𝜔. The existence of 𝜔𝑐 is guar-
anteed according to the mean value theorem for definite integrals. For
narrow-banded waves, 𝜔𝑐 can be approximated using the peak wave
angular frequency, 𝜔𝑐 ≈ 𝜔𝑝 = 2𝜋∕𝑇𝑝. The external factors such as the
water depth and the vertical position of aquaculture farms should also
be considered during the design. For places that are not suitable to
establish living shorelines, such as low-nutrient seabeds, the suspended
aquaculture farms offer a viable alternative to SAV for nature-based
coastal defense.

This work has shown that suspended aquaculture farms can supple-
ment SAV in wave attenuation. Suspended aquaculture farms attenuate
shorter peak period waves and high frequency wave components more
than SAV. Hence, adding suspended aquaculture farms to SAV-based
living shorelines can compensate for the limitations of SAV for at-
tenuating shorter period waves (such as boat wake) and enhance the
wave attenuation capacity of SAV-based living shorelines for a wider
range of wave frequency. The wave attenuation by SAV decreases
during high tide or storm surge due to the increase in water level. The
water level, however, has fewer influences on suspended aquaculture
farms since they are located near the surface and move up and down
with water level. Therefore, suspended aquaculture farms can enhance
the wave attenuation capacity of SAV-based living shorelines during
extreme events. The combination of suspended aquaculture farms and
traditional living shorelines (such as SAV) is therefore a desirable
nature-based coastal defense strategy.

5.2. Simplified analytical solutions

The generalized three-layer frequency dependent theoretical wave
attenuation model developed in this paper is applicable to analyze
the wave attenuation capacity of submerged, emerged, suspended,
and floating canopies for random waves including narrow-banded and
wide-banded wave conditions. The present analytical model provided
a more precise consideration of the blade motion by incorporating
the effects of inertia (neglected in Mullarney and Henderson, 2010;
Henderson, 2019) and the mode shape (not considered in Asano et al.,
1992; Méndez et al., 1999).

The present model can reduce to previous models for submerged
rigid vegetation without motion by setting the transfer functions 𝛾𝑠 and
𝛾𝑐 as 0. Therefore, the decay coefficient 𝛽 in (22) reduces to the solution
for rigid blades and given by

𝛽𝑅(𝜔) =

√
2

2𝑁𝑘2

√

𝜋𝜔(2𝑘ℎ + sinh 2𝑘ℎ)

−𝑑1

∫

−𝑑1−𝑑2

𝐶𝑑 𝑏𝜎𝑢[cosh 𝑘(ℎ + 𝑧)]2𝑑𝑧,

(28)

𝑢 = ∫ ∞

0 [𝜔 cosh 𝑘(ℎ + 𝑧)∕ sinh 𝑘ℎ]2𝑆𝜂𝜂(𝜔, 0)𝑑𝜔. If 𝑑3 = 0, the
where 𝜎2
solution in (28) reduces to the solution by Jacobsen et al. (2019)
for submerged rigid vegetation. In this model, the nonlinear drag is
linearized using the Borgman (1967) method such that |𝑢| ≈
8∕𝜋𝜎𝑢.
If using the root mean square velocity to linearize the drag force
following Madsen et al. (1988) such that |𝑢| ≈
2𝜎𝑢, the solution
reduces to the Hasselmann and Collins (1968) based solution in Chen
and Zhao (2012) for submerged rigid vegetation. For idealized narrow-
banded waves such that 𝑆𝜂𝜂 ≈ 0 when 𝜔 ≠ 𝜔𝑝, the damping coefficient
in (28) can be further simplified as

√

√

𝐶𝑑 𝑏𝑁𝑘𝑝𝐻𝑟𝑚𝑠0

𝛽𝑅𝑁 =

12

×

1
√

𝜋
9 sinh 𝑘𝑝

(𝑑2 + 𝑑3

)

− 9 sinh 𝑘𝑝𝑑3 + sinh 3𝑘𝑝
sinh 2𝑘𝑝ℎ + 2𝑘ℎ)
(

sinh 𝑘𝑝ℎ

(𝑑2 + 𝑑3

)

− sinh 3𝑘𝑝𝑑3

,

(29)

√

8 ∫ ∞

where 𝐻𝑟𝑚𝑠0 =
0 𝑆𝜂𝜂(𝜔, 0)𝑑𝜔 is the root mean square incident
wave height and 𝑘𝑝 is the peak wave number calculated by solving
𝜔2
𝑝 = 𝑔𝑘𝑝 tanh 𝑘𝑝ℎ. For bottom-rooted rigid vegetation such that 𝑑3 = 0,
𝛽𝑅𝑁 in (29) reduces to the solution of Mendez and Losada (2004). The
relationship between the present and previous models are shown on
Fig. 12.

6. Conclusions

A generalized three-layer frequency-dependent theoretical model
for the wave attenuation by submerged and suspended canopies sub-
jected to random waves was derived and validated with laboratory
and field data. This model incorporates the motion of canopies using
a cantilever-beam model for slender canopy components and a buoy-
on-rope model for canopy components with concentrated mass and
buoyancy. This frequency-dependent solution was used to demonstrate
the shoreline protection capability of suspended mussel farms alone
and in combination with submerged aquatic vegetation (SAV) to damp
wave energy at a field site in Saco Bay, Maine, USA during a Jan-
uary 2015 Blizzard. The results showed that both suspended mussel
farms and SAV have the potential to damp wave energy considerably
during storm events. Suspended mussel farms are more effective at

CoastalEngineering160(2020)10373712L. Zhu et al.

damping shorter waves and high frequency wave components of the
wave spectrum while dense SAV colonized in shallower water have
the advantages of damping longer waves and lower frequency wave
components more effectively. However, the wave attenuation of SAV
in shallow water decreases dramatically at the peak of storm tide due
to increased water level, which decreases the wave motion reaching the
ocean bottom. In contrast, suspended aquaculture farms can move up
and down with water level change and are less affected by water level
change. As a consequence, the combination of suspended aquaculture
farms and traditional SAV-based living shorelines provide an optimized
nature-based shore protection scheme that can damp more wave energy
for a wider wave frequency and water level range.

The research of wave attenuation by suspended and floating
canopies is still in its infancy. More laboratory and field experiments
data for the hydrodynamic properties of suspended aquaculture farms
(e.g., mussels and kelp) as well as wave attenuation are desirable. The
present theoretical model assumed the blade motion as a linear vibra-
tion with small-amplitude. However, as long as the nonlinear effects
of large-amplitude blade motion is negligible, the present theoretical
model remains valid. In addition, the bottom friction, bedforms, bottom
slope as well as wave-driven currents, wave and current conditions may
also be significant for certain types of bottom rooted vegetation (e.g.,
Jensen et al., 1989; Myrhaug, 1995; Zou, 2004; Zou and Hay, 2003;
Smyth and Hay, 2002; Maza et al., 2019; Abdolahpour et al., 2017;
van Rooijen et al., 2020). Therefore, it is worthwhile to investigate
the nonlinear effects of large-amplitude blade motion on the wave
damping capacity of suspended canopies as well as the effects of bottom
properties and wave–current conditions in the future work.

CRediT authorship contribution statement

Longhuan Zhu: Conceptualization, Methodology, Software, Valida-
tion, Formal analysis, Investigation, Data curation, Writing - original
draft, Writing - review & editing, Visualization. Kimberly Huguenard:
Conceptualization, Writing - review & editing, Supervision, Project ad-
ministration, Funding acquisition. Qing-Ping Zou: Conceptualization,
Writing - review & editing, Supervision, Funding acquisition. David
W. Fredriksson: Writing - review & editing. Dongmei Xie: Resources,
Data curation, Writing - review & editing.

Declaration of competing interest

The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.

Acknowledgments

This work was completed as part of the PhD research of Longhuan
Zhu who is supported by National Science Foundation, USA award
#IIA-1355457 to Maine EPSCoR at the University of Maine. The authors
benefited from discussions with Zhilong Liu and Haifei Chen. The
authors wish to thank Stephen Cousins and Shane Moeykens at the
University of Maine Advanced Research Computing for the computa-
tional support. The authors would like to thank Niels G. Jacobsen for
sharing the data used on Fig. 4. The authors would also like to thank
the anonymous reviewers for constructive comments that helped to
improve this manuscript greatly.

Appendix. Normal mode solutions for blade displacements in ran-
dom waves

The governing equation (6) for the blade displacement in random

waves is given by

𝑚 ̈𝜉 + 𝑐 ̇𝜉 + 𝐸𝐼𝜉′′′′ =

∑

𝜔

]
𝑎𝜔𝛤 [𝑐 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝜔𝑚𝐼 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓)

(A.1)

with the boundary conditions 𝜉(0, 𝑡) = 0, 𝜉′(0, 𝑡) = 0, 𝜉′′(𝑙, 𝑡) = 0, and
𝜉′′′(𝑙, 𝑡) = 0 for a cantilever beam. The solution of (A.1) can be written
as the linear superposition of components of different frequencies

𝜉 = 𝛴𝜔𝜉𝜔,

where 𝜉𝜔 is the solution of

(A.2)

𝑚 ̈𝜉𝜔 + 𝑐 ̇𝜉𝜔 + 𝐸𝐼𝜉′′′′

] .
𝜔 = 𝑎𝜔𝛤 [𝑐 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝜔𝑚𝐼 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓)

(A.3)

According to normal mode approach (Rao, 2007), the solution of (A.3)
can be assumed as a linear superposition of the normal modes of the
cantilever beam as

𝜉𝜔 =

∑

𝑛

𝜙𝑛(𝑠)𝑞𝑛(𝑡),

(A.4)

where 𝜙𝑛(𝑠) is the 𝑛th normal mode and 𝑞𝑛 is the 𝑛th generalized
coordinate or modal participation coefficient. The normal modes for
a cantilever beam are found from the equation

𝜙′′′′ − 𝜇4𝜙 = 0

(A.5)

with boundary conditions 𝜙(0) = 0, 𝜙′(0) = 0, 𝜙′′(𝑙) = 0, and 𝜙′′′(𝑙) = 0.
Solving (A.5) yields the 𝑛th normal mode,
sin 𝜇𝑛𝑠 − sinh 𝜇𝑛𝑠)

sin 𝜇𝑛𝑙 + sinh 𝜇𝑛𝑙)
(

𝜙𝑛 =

+

cos 𝜇𝑛𝑙 + cosh 𝜇𝑛𝑙) (
(
cosh 𝜇𝑛𝑠 − cos 𝜇𝑛𝑠) ,
(
×

where 𝜇𝑛 is the 𝑛th solution of

1 + cos 𝜇𝑙 cosh 𝜇𝑙 = 0.

(A.6)

(A.7)

Using (A.5) associated with the boundary conditions, the normal modes
are proved to satisfy the orthogonality conditions,

{

𝑙

∫
0

𝐺(𝑠)𝜙𝑛𝜙𝑚𝑑𝑠 =

∫ 𝑙
0 𝐺(𝑠)𝜙2
0,

𝑛𝑑𝑠,
𝑛 ≠ 𝑚,

𝑛 = 𝑚,

(A.8)

where 𝐺(𝑠) is an arbitrary function. Substituting (A.4) into (A.3) yields

∑

∑

∑

𝑛

𝑚

𝜙𝑛 ̈𝑞𝑛 + 𝑐

𝜙𝑛 ̇𝑞𝑛 + 𝐸𝐼
=𝑎𝜔𝛤 [𝑐 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝜔𝑚𝐼 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓)
] .
Multiplying (A.9) by 𝜙𝑚 and integrating from 0 to 𝑙 result in

𝑛

𝑛

𝜙′′′′
𝑛 𝑞𝑛

(A.9)

(

𝑙

∑

∫

0
𝑙

𝑛

[

𝑙

𝑚𝜙𝑛𝜙𝑚𝑑𝑠 ̈𝑞𝑛 + ∫
0

𝑐𝜙𝑛𝜙𝑚𝑑𝑠 ̇𝑞𝑛 + ∫

)

𝐸𝐼𝜙′′′′

𝑛 𝜙𝑚𝑑𝑠𝑞𝑛

𝑙

0

=𝑎𝜔

∫

0

𝑐𝛤 𝜙𝑚𝑑𝑠 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝜔 ∫
0

𝑙

]
𝑚𝐼 𝛤 𝜙𝑚𝑑𝑠 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓)

.

(A.10)

Substituting (A.5) into (A.10) and using the orthogonality conditions
(A.8) yield

̈𝑞𝑛 + 2𝜁𝑛𝜆𝑛 ̇𝑞𝑛 + 𝜆2

] ,
𝑛𝑞𝑛 = 𝑎𝜔 [𝐷𝑛 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝜔𝐼𝑛 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓)

(A.11)

where 2𝜁𝑛𝜆𝑛 = ∫ 𝑙
0 𝑐𝛤 𝜙𝑛𝑑𝑠∕ ∫ 𝑙
∫ 𝑙
0 𝑚𝜙2
solution for (A.11) is

𝑛𝑑𝑠∕ ∫ 𝑙
0 𝑐𝜙2
0 𝑚𝜙2
𝑛𝑑𝑠, and 𝐼𝑛 = ∫ 𝑙

∫ 𝑙
𝑛𝑑𝑠, 𝜆2
𝑛 = 𝜇4
0 𝐸𝐼𝜙2
𝑛
0 𝑚𝐼 𝛤 𝜙𝑛𝑑𝑠∕ ∫ 𝑙
0 𝑚𝜙2

𝑛𝑑𝑠∕ ∫ 𝑙
0 𝑚𝜙2
𝑛𝑑𝑠, 𝐷𝑛 =
𝑛𝑑𝑠. The steady state

𝑞𝑛 = 𝑎𝜔𝑄𝑠 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝑎𝜔𝑄𝑐 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓),

(A.12)

where

𝑄𝑠 =

𝜔𝐼𝑛
(𝜆2

𝑛 − 𝜔2)
(𝜆2
𝑛 − 𝜔2)2
+

− 𝐷𝑛2𝜁𝑛𝜆𝑛𝜔
2𝜁𝑛𝜆𝑛𝜔)2
(

(A.13)

CoastalEngineering160(2020)10373713L. Zhu et al.

and

𝑄𝑐 =

𝐷𝑛
(𝜆2

𝑛 − 𝜔2)
(𝜆2
𝑛 − 𝜔2)2
+

+ 𝜔𝐼𝑛2𝜁𝑛𝜆𝑛𝜔
2𝜁𝑛𝜆𝑛𝜔)2
(

.

(A.14)

Substituting (A.6) and (A.12) into (A.4) and the result into (A.2) yields
the blade displacement,

𝜉 =

∑

𝜔

] ,
𝑎𝛤 [𝛾𝑠 sin(𝑘𝑥 − 𝜔𝑡 + 𝜓) + 𝛾𝑐 cos(𝑘𝑥 − 𝜔𝑡 + 𝜓)

(A.15)

where the transfer functions 𝛾𝑠 and 𝛾𝑐 are given by

𝛾𝑠 =

and

𝛾𝑐 =

𝜔
𝛤

∞
∑

𝑛=1

𝜙𝑛

𝜔𝐼𝑛
(𝜆2

(𝜆2
𝑛 − 𝜔2)
𝑛 − 𝜔2)2
+

− 𝐷𝑛2𝜁𝑛𝜆𝑛𝜔
2𝜁𝑛𝜆𝑛𝜔)2
(

(A.16)

𝜔
𝛤

∞
∑

𝑛=1

𝜙𝑛

𝐷𝑛
(𝜆2

(𝜆2
𝑛 − 𝜔2)
𝑛 − 𝜔2)2
+

+ 𝜔𝐼𝑛2𝜁𝑛𝜆𝑛𝜔
2𝜁𝑛𝜆𝑛𝜔)2
(

.

(A.17)

References

Abdelrhman, M., 2007. Modeling coupling between eelgrass Zostera marina and water
flow. Mar. Ecol. Prog. Ser. 338, 81–96. http://dx.doi.org/10.3354/meps338081,
URL http://www.int-res.com/abstracts/meps/v338/p81-96/.

Abdolahpour, M., Hambleton, M., Ghisalberti, M., 2017. The wave-driven current in
coastal canopies. J. Geophys. Res. 122 (5), 3660–3674. http://dx.doi.org/10.1002/
2016JC012446, URL http://doi.wiley.com/10.1002/2016JC012446.

Anderson, M.E., Smith, J., 2014. Wave attenuation by flexible, idealized salt marsh
vegetation. Coast. Eng. 83, 82–92. http://dx.doi.org/10.1016/j.coastaleng.2013.10.
004, URL https://linkinghub.elsevier.com/retrieve/pii/S0378383913001609.
Arnaud, G., Rey, V., Touboul, J., Sous, D., Molin, B., Gouaud, F., 2017. Wave
propagation through dense vertical cylinder arrays:
Interference process and
specific surface effects on damping. Appl. Ocean Res. 65, 229–237. http://dx.doi.
org/10.1016/j.apor.2017.04.011, URL https://linkinghub.elsevier.com/retrieve/pii/
S0141118717300998.

Asano, T., Deguchi, H., Kobayashi, N., 1992. Interaction between water waves and
vegetation. In: Coast. Eng. Proc., Vol. 3. pp. 2710–2723, URL https://icce-ojs-
tamu.tdl.org/icce/index.php/icce/article/view/4885.

Beal, B.F., Vadas Sr., R.L., Wright, W.A., Nickl, S., 2004. Annual aboveground biomass
and productivity estimates for intertidal Eelgrass (Zostera marina L.) in Cobscook
Bay, Maine. Northeast. Nat. 11, 197–224, URL https://doi.org/10.1656/1092-
6194(2004)11[197:AABAPE]2.0.CO;2.

Beem, N.T., Short, F.T., 2009. Subtidal Eelgrass declines in the great bay Estuary, new
hampshire and maine, USA. Estuaries Coasts 32 (1), 202–205. http://dx.doi.org/
10.1007/s12237-008-9110-3, URL http://link.springer.com/10.1007/s12237-008-
9110-3.

Bilkovic, D.M., Mitchell, M., Mason, P., Duhring, K., 2016. The role of living shorelines
as estuarine habitat conservation strategies. Coast. Manage. 44 (3), 161–174.
http://dx.doi.org/10.1080/08920753.2016.1160201, URL http://www.tandfonline.
com/doi/full/10.1080/08920753.2016.1160201.

Borgman, L.E., 1967. Random hydrodynamic forces on objects. Ann. Math. Stat. 38 (1),
37–51. http://dx.doi.org/10.1214/aoms/1177699057, URL http://projecteuclid.
org/euclid.aoms/1177699057.

Borsje, B.W., van Wesenbeeck, B.K., Dekker, F., Paalvast, P., Bouma, T.J.,
van Katwijk, M.M., de Vries, M.B., 2011. How ecological engineering can
serve in coastal protection. Ecol. Eng. 37 (2), 113–122. http://dx.doi.org/
10.1016/j.ecoleng.2010.11.027, URL https://linkinghub.elsevier.com/retrieve/pii/
S0925857410003216.

Boström, C., Bonsdorff, E., 1997. Community structure and spatial variation of benthic
invertebrates associated with Zostera marina (L.) beds in the northern Baltic Sea.
J. Sea Res. 37 (1–2), 153–166. http://dx.doi.org/10.1016/S1385-1101(96)00007-X,
URL https://linkinghub.elsevier.com/retrieve/pii/S138511019600007X.

Bouma, T.J., van Belzen, J., Balke, T., Zhu, Z., Airoldi, L., Blight, A.J., Davies, A.J.,
Galvan, C., Hawkins, S.J., Hoggart, S.P., Lara, J.L., Losada,
I.J., Maza, M.,
Ondiviela, B., Skov, M.W., Strain, E.M., Thompson, R.C., Yang, S., Zanuttigh, B.,
Zhang, L., Herman, P.M., 2014. Identifying knowledge gaps hampering application
of intertidal habitats in coastal protection: Opportunities & steps to take. Coast.
Eng. 87, 147–157. http://dx.doi.org/10.1016/j.coastaleng.2013.11.014, URL https:
//linkinghub.elsevier.com/retrieve/pii/S037838391300197X.

Campbell,

I., Macleod, A., Sahlmann, C., Neves, L., Funderud, J., Øverland, M.,
Hughes, A.D., Stanley, M., 2019. The environmental risks associated with the
development of seaweed farming in Europe - prioritizing key knowledge gaps.
Front. Mar. Sci. 6 (MAR), 107. http://dx.doi.org/10.3389/fmars.2019.00107, URL
https://www.frontiersin.org/article/10.3389/fmars.2019.00107/full.

Chen, X., Chen, Q., Zhan, J., Liu, D., 2016. Numerical simulations of wave propa-
gation over a vegetated platform. Coast. Eng. 110, 64–75. http://dx.doi.org/10.
1016/j.coastaleng.2016.01.003, URL https://linkinghub.elsevier.com/retrieve/pii/
S0378383916000041.

Chen, H., Liu, X., Zou, Q., 2019. Wave-driven flow induced by suspended and
submerged canopies. Adv. Water Resour. 123, 160–172. http://dx.doi.org/10.
1016/j.advwatres.2018.11.009, URL https://linkinghub.elsevier.com/retrieve/pii/
S0309170818302574.

Chen, Q., Zhao, H., 2012. Theoretical models for wave energy dissipation caused by
vegetation. J. Eng. Mech. 138 (2), 221–229. http://dx.doi.org/10.1061/(ASCE)EM.
1943-7889.0000318, URL http://ascelibrary.org/doi/10.1061/%28ASCE%29EM.
1943-7889.0000318.

Chen, H., Zou, Q.-P., 2019. Eulerian–Lagrangian flow-vegetation interaction model
using immersed boundary method and OpenFOAM. Adv. Water Resour. 126, 176–
192. http://dx.doi.org/10.1016/j.advwatres.2019.02.006, URL https://linkinghub.
elsevier.com/retrieve/pii/S0309170818306523.

Currin, C., Chappell, W., Deaton, A., 2010. Developing alternative shoreline armoring
strategies : The living shoreline approach in North Carolina. In: Shipman, H.,
Dethier, M.N., Gelfenbaum, G., Fresh, K.L., Dinicola, R.S. (Eds.), Puget Sound
Shorelines and the Impacts of Armoring—Proceedings of a State of the Science
Workshop. US Geological Survey, pp. 91–102, URL http://aquaticcommons.org/
14844/.

Dalrymple, R.A., Kirby, J.T., Hwang, P.A., 1984. Wave diffraction due to areas of
energy dissipation. J. Waterw. Port Coast. Ocean Eng. 110 (1), 67–79. http:
//dx.doi.org/10.1061/(ASCE)0733-950X(1984)110:1(67), URL http://ascelibrary.
org/doi/10.1061/%28ASCE%290733-950X%281984%29110%3A1%2867%29.
Davis, J.L., Currin, C.A., O’Brien, C., Raffenburg, C., Davis, A., 2015. Living shorelines:
Coastal resilience with a blue carbon benefit. In: Li, B. (Ed.), PLoS One 10 (11),
e0142595. http://dx.doi.org/10.1371/journal.pone.0142595, URL https://dx.plos.
org/10.1371/journal.pone.0142595.

Dean, R.G., Dalrymple, R.A., 1991. Water Wave Mechanics for Engineers and Scientists.
In: Advanced Series on Ocean Engineering, vol. 2, (8), World Scientific, Cambridge,
085201. http://dx.doi.org/10.1142/1232, arXiv:1011.1669, J. Phys. A.

Denny, M.W., Gaylord, B.P., Cowen, E.A., 1997. Flow and flexibility II. The roles of
size and shape in determining wave forces on the bull kelp Nereocystis luetkeana.
J. Exp. Biol. 200 (24), 3165–3183, URL https://jeb.biologists.org/content/200/24/
3165.

Dewhurst, T., 2016. Dynamics of a Submersible Mussel Raft (Ph.D. thesis). University

of New Hampshire, URL https://scholars.unh.edu/dissertation/1380/.

Duarte, C.M., Wu, J., Xiao, X., Bruhn, A., Krause-Jensen, D., 2017. Can seaweed farming
play a role in climate change mitigation and adaptation? Front. Mar. Sci. 4 (APR),
100. http://dx.doi.org/10.3389/fmars.2017.00100, URL http://journal.frontiersin.
org/article/10.3389/fmars.2017.00100/full.

Etminan, V., Lowe, R.J., Ghisalberti, M., 2019. Canopy resistance on oscillatory flows.
Coast. Eng. 152, 103502. http://dx.doi.org/10.1016/j.coastaleng.2019.04.014, URL
https://linkinghub.elsevier.com/retrieve/pii/S0378383918302254.

Ferrario, F., Beck, M.W., Storlazzi, C.D., Micheli, F., Shepard, C.C., Airoldi, L., 2014.
The effectiveness of coral reefs for coastal hazard risk reduction and adaptation.
Nature Commun. 5 (1), 3794. http://dx.doi.org/10.1038/ncomms4794, URL http:
//www.nature.com/doifinder/10.1038/ncomms4794.

Fonseca, M.S., Koehl, M., Kopp, B.S., 2007. Biomechanical factors contributing to self-
organization in seagrass landscapes. J. Exp. Mar. Biol. Ecol. 340 (2), 227–246. http:
//dx.doi.org/10.1016/j.jembe.2006.09.015, URL https://linkinghub.elsevier.com/
retrieve/pii/S0022098106005399.

Gaeckle, J.L., Short, F.T., 2002. A plastochrone method for measuring leaf growth
in eelgrass, Zostera marina L.. Bull. Mar. Sci. 71 (3), 1237–1246, URL
https://www.ingentaconnect.com/content/umrsmas/bullmar/2002/00000071/
00000003/art00010.

Gagnon, M., Bergeron, P., 2017. Observations of the loading and motion of a submerged
mussel longline at an open ocean site. Aquac. Eng. 78, 114–129. http://dx.doi.org/
10.1016/j.aquaeng.2017.05.004, URL https://linkinghub.elsevier.com/retrieve/pii/
S0144860917300353.

Garzon, J.L., Maza, M., Ferreira, C.M., Lara, J.L., Losada, I.J., 2019. Wave attenuation
by spartina saltmarshes in the chesapeake bay under storm surge conditions. J.
Geophys. Res. 124 (7), 5220–5243. http://dx.doi.org/10.1029/2018JC014865, URL
https://onlinelibrary.wiley.com/doi/abs/10.1029/2018JC014865.

Gedan, K.B., Kirwan, M.L., Wolanski, E., Barbier, E.B., Silliman, B.R., 2011. The present
and future role of coastal wetland vegetation in protecting shorelines: answering
recent challenges to the paradigm. Clim. Change 106 (1), 7–29. http://dx.doi.org/
10.1007/s10584-010-0003-7, URL http://link.springer.com/10.1007/s10584-010-
0003-7.

Ghisalberti, M., Nepf, H.M., 2002. Mixing layers and coherent structures in vege-
tated aquatic flows. J. Geophys. Res. 107 (C2), 3011. http://dx.doi.org/10.1029/
2001JC000871, URL http://doi.wiley.com/10.1029/2001JC000871.

Gittman, R.K., Peterson, C.H., Currin, C.A., Joel Fodrie, F., Piehler, M.F., Bruno, J.F.,
2016. Living shorelines can enhance the nursery role of threatened estuarine
habitats. Ecol. Appl. 26 (1), 249–263. http://dx.doi.org/10.1890/14-0716, URL
http://doi.wiley.com/10.1890/14-0716.

Grebe, G.S., Byron, C.J., Gelais, A.S., Kotowicz, D.M., Olson, T.K., 2019. An ecosystem
approach to kelp aquaculture in the Americas and Europe. Aquac. Rep. 15,
100215. http://dx.doi.org/10.1016/j.aqrep.2019.100215, URL https://linkinghub.
elsevier.com/retrieve/pii/S2352513419300134.

Hasselmann, K., Collins, J., 1968. Spectral dissipation of finite-depth gravity waves
due to turbulent bottom friction. J. Mar. Res. 26 (1), 1–12, URL http://www.
journalofmarineresearch.org/.

CoastalEngineering160(2020)10373714L. Zhu et al.

Henderson, S.M., 2019. Motion of buoyant, flexible aquatic vegetation under waves:
Simple theoretical models and parameterization of wave dissipation. Coast. Eng.
152, 103497. http://dx.doi.org/10.1016/j.coastaleng.2019.04.009, URL https://
linkinghub.elsevier.com/retrieve/pii/S0378383918305349.

Losada, I.J., Maza, M., Lara, J.L., 2016. A new formulation for vegetation-induced
damping under combined waves and currents. Coast. Eng. 107, 1–13. http://dx.
doi.org/10.1016/j.coastaleng.2015.09.011, URL https://linkinghub.elsevier.com/
retrieve/pii/S0378383915001684.

Higuera, P., Lara, J.L., Losada, I.J., 2013. Realistic wave generation and active wave ab-
sorption for Navier–Stokes models. Coast. Eng. 71, 102–118. http://dx.doi.org/10.
1016/j.coastaleng.2012.07.002, URL https://linkinghub.elsevier.com/retrieve/pii/
S0378383912001354.

Hu, Z., Suzuki, T., Zitman, T., Uittewaal, W., Stive, M., 2014. Laboratory study on wave
dissipation by vegetation in combined current–wave flow. Coast. Eng. 88, 131–
142. http://dx.doi.org/10.1016/j.coastaleng.2014.02.009, URL https://linkinghub.
elsevier.com/retrieve/pii/S0378383914000416.

Huai, W., Hu, Y., Zeng, Y., Han, J., 2012. Velocity distribution for open channel flows
with suspended vegetation. Adv. Water Resour. 49, 56–61. http://dx.doi.org/10.
1016/j.advwatres.2012.07.001, URL https://linkinghub.elsevier.com/retrieve/pii/
S0309170812001893.

Izaguirre, C., Méndez, F.J., Menéndez, M., Losada,

I.J., 2011. Global extreme
wave height variability based on satellite data. Geophys. Res. Lett. 38 (10),
n/a–n/a. http://dx.doi.org/10.1029/2011GL047302, URL http://doi.wiley.com/10.
1029/2011GL047302.

Jacobsen, N., McFall, B., van der A, D., 2019. A frequency distributed dissi-
pation model
for canopies. Coast. Eng. 150, 135–146. http://dx.doi.org/10.
1016/j.coastaleng.2019.04.007, URL https://linkinghub.elsevier.com/retrieve/pii/
S0378383918303892.

Jadhav, R.S., Chen, Q., Smith, J.M., 2013. Spectral distribution of wave energy
dissipation by salt marsh vegetation. Coast. Eng. 77, 99–107. http://dx.doi.org/10.
1016/j.coastaleng.2013.02.013, URL https://linkinghub.elsevier.com/retrieve/pii/
S0378383913000537.

Jensen, B., Sumer, B.M., Fredsøe, J., 1989. Turbulent oscillatory boundary layers at
high reynolds numbers. J. Fluid Mech. 206, 265–297. http://dx.doi.org/10.1017/
S0022112089002302, URL https://www.cambridge.org/core/product/identifier/
S0022112089002302/type/journal_article.

Keulegan, G.H., Carpenter, L.H., 1958. Forces on cylinders and plates in an oscillating
fluid. J. Res. Natl. Bur. Stand. 60 (5), 423–440, URL https://nvlpubs.nist.gov/
nistpubs/jres/60/jresv60n5p423_A1b.pdf.

Knysh, A., Tsukrov, I., Chambers, M., Swift, M.R., Sullivan, C., Drach, A., 2020.
Numerical modeling of submerged mussel longlines with protective sleeves. Aquac.
Eng. 88, 102027. http://dx.doi.org/10.1016/j.aquaeng.2019.102027, URL https:
//linkinghub.elsevier.com/retrieve/pii/S0144860919301177.

Kobayashi, N., Raichle, A.W., Asano, T., 1993. Wave attenuation by vegetation. J.
Waterw. Port Coast. Ocean Eng. 119 (1), 30–48. http://dx.doi.org/10.1061/(ASCE)
0733-950X(1993)119:1(30), URL http://ascelibrary.org/doi/10.1061/%28ASCE%
290733-950X%281993%29119%3A1%2830%29.

Landmann, J., Ongsiek, T., Goseberg, N., Heasman, K., Buck, B., Paffenholz, J.-A.,
Hildebrandt, A., 2019. Physical modelling of blue mussel dropper lines for the
development of surrogates and hydrodynamic coefficients. J. Mar. Sci. Eng. 7 (3),
65. http://dx.doi.org/10.3390/jmse7030065, URL https://www.mdpi.com/2077-
1312/7/3/65.

Lauzon-Guay, J.S., Barbeau, M.A., Watmough, J., Hamilton, D.J., 2006. Model for
growth and survival of mussels Mytilus edulis reared in Prince Edward Is-
land, Canada. Mar. Ecol. Prog. Ser. 323, 171–183. http://dx.doi.org/10.3354/
meps323171, URL http://www.int-res.com/abstracts/meps/v323/p171-183/.
Leclercq, T., de Langre, E., 2018. Reconfiguration of elastic blades in oscillatory
flow. J. Fluid Mech. 838, 606–630. http://dx.doi.org/10.1017/jfm.2017.910, URL
https://www.cambridge.org/core/product/identifier/S0022112017009107/type/
journal_article.

Lei, J., Nepf, H., 2019a. Blade dynamics in combined waves and current. J. Fluids
Struct. 87, 137–149. http://dx.doi.org/10.1016/j.jfluidstructs.2019.03.020, URL
https://linkinghub.elsevier.com/retrieve/pii/S0889974618306996.

Lei, J., Nepf, H., 2019b. Wave damping by flexible vegetation: Connecting individual
blade dynamics to the meadow scale. Coast. Eng. 147, 138–148. http://dx.doi.org/
10.1016/j.coastaleng.2019.01.008, URL https://linkinghub.elsevier.com/retrieve/
pii/S0378383918300905.

Leonardi, N., Carnacina, I., Donatelli, C., Ganju, N.K., Plater, A.J., Schuerch, M., Tem-
merman, S., 2018. Dynamic interactions between coastal storms and salt marshes: A
review. Geomorphology 301, 92–107. http://dx.doi.org/10.1016/j.geomorph.2017.
11.001, URL https://linkinghub.elsevier.com/retrieve/pii/S0169555X17304579.
Lin, J., Li, C., Zhang, S., 2016. Hydrodynamic effect of a large offshore mussel
suspended aquaculture farm. Aquaculture 451, 147–155. http://dx.doi.org/10.
1016/j.aquaculture.2015.08.039, URL https://linkinghub.elsevier.com/retrieve/pii/
S0044848615301587.

Liu, P.L., Chang, C.-W., Mei, C.C., Lomonaco, P., Martin, F.L., Maza, M., 2015. Periodic
water waves through an aquatic forest. Coast. Eng. 96, 100–117. http://dx.doi.org/
10.1016/j.coastaleng.2014.11.002, URL https://linkinghub.elsevier.com/retrieve/
pii/S0378383914002002.

Longuet-Higgins, M.S., 1983. On the joint distribution of wave periods and amplitudes
in a random wave field. Proc. R. Soc. Lond. Ser. A Math. Phys. Eng. Sci.
389 (1797), 241–258. http://dx.doi.org/10.1098/rspa.1983.0107, URL http://rspa.
royalsocietypublishing.org/cgi/doi/10.1098/rspa.1983.0107.

Lowe, R.J., 2005. Oscillatory flow through submerged canopies: 1. Velocity structure. J.
Geophys. Res. 110 (C10), C10016. http://dx.doi.org/10.1029/2004JC002788, URL
http://doi.wiley.com/10.1029/2004JC002788.

Luhar, M., 2012. Analytical and Experimental Studies of Plant-Flow Interaction at
Multiple Scales (Ph.D. thesis). Massachusetts Institute of Technology, URL http:
//dspace.mit.edu/handle/1721.1/78142.

Luhar, M., Infantes, E., Nepf, H., 2017. Seagrass blade motion under waves and its
impact on wave decay. J. Geophys. Res. 122 (5), 3736–3752. http://dx.doi.org/
10.1002/2017JC012731, URL http://doi.wiley.com/10.1002/2017JC012731.
Luhar, M., Nepf, H., 2016. Wave-induced dynamics of flexible blades. J. Fluids Struct.
arXiv:1510.

61,
01237, URL https://linkinghub.elsevier.com/retrieve/pii/S0889974615002613.
Madsen, O.S., Poon, Y.-K., Graber, H.C., 1988. Spectral wave attenuation by bot-
tom friction: Theory. Coast. Eng. Proc. 1 (21), 492–504. http://dx.doi.org/
10.1061/9780872626874.035, URL https://journals.tdl.org/icce/index.php/icce/
article/view/4241.

http://dx.doi.org/10.1016/j.jfluidstructs.2015.11.007,

20–41.

Marsooli, R., Orton, P.M., Mellor, G., 2017. Modeling wave attenuation by salt marshes
in jamaica bay, new york, using a new rapid wave model. J. Geophys. Res. 122 (7),
5689–5707. http://dx.doi.org/10.1002/2016JC012546, URL https://onlinelibrary.
wiley.com/doi/abs/10.1002/2016JC012546.

Mattila, J., Chaplin, G., Eilers, M.R., Heck, K.L., O’Neal, J.P., Valentine, J.F., 1999.
Spatial and diurnal distribution of invertebrate and fish fauna of a Zostera marina
bed and nearby unvegetated sediments in Damariscotta River, Maine(USA). J.
Sea Res. 41 (4), 321–332. http://dx.doi.org/10.1016/S1385-1101(99)00006-4, URL
https://linkinghub.elsevier.com/retrieve/pii/S1385110199000064.

Maza, M., Lara, J.L., Losada, I.J., 2019. Experimental analysis of wave attenuation
and drag forces in a realistic fringe rhizophora mangrove forest. Adv. Water Re-
sour. 131, 103376. http://dx.doi.org/10.1016/j.advwatres.2019.07.006, URL https:
//linkinghub.elsevier.com/retrieve/pii/S0309170819302969.

McGehee, D., 2016. Design and monitoring of a small living shoreline scaled for private
properties on exposed, rapidly-eroding coasts. In: Crookston, B., Tullis, B. (Eds.),
Hydraulic Structures and Water System Management. 6th IAHR International Sym-
posium on Hydraulic Structures. Portland, OR, 27-30 June, pp. 488–497. http://
dx.doi.org/10.15142/T3530628160853, URL https://digitalcommons.usu.edu/ishs/
2016/Session6/2/.

MEA, 2005. Ecosystems and human well-being: current state and trends. Millennium
Ecosystem Assessment, Global Assessment Reports 1, Millennium Ecosystem Assess-
ment, URL https://www.millenniumassessment.org/documents/document.766.aspx.
pdf.

Mei, C.C., Chan, I.-C., Liu, P.L.-F., Huang, Z., Zhang, W., 2011. Long waves through
emergent coastal vegetation. J. Fluid Mech. 687, 461–491. http://dx.doi.org/
10.1017/jfm.2011.373, URL https://www.cambridge.org/core/product/identifier/
S0022112011003739/type/journal_article.

Mendez, F.J., Losada, I.J., 2004. An empirical model to estimate the propagation
of random breaking and nonbreaking waves over vegetation fields. Coast. Eng.
51 (2), 103–118. http://dx.doi.org/10.1016/j.coastaleng.2003.11.003, URL https:
//linkinghub.elsevier.com/retrieve/pii/S0378383903001182.

Méndez, F.J., Losada, I.J., Losada, M.A., 1999. Hydrodynamics induced by wind waves
in a vegetation field. J. Geophys. Res. 104 (C8), 18383–18396. http://dx.doi.org/
10.1029/1999JC900119, URL http://doi.wiley.com/10.1029/1999JC900119.
Möller, I., 2019. Applying uncertain science to nature-based coastal protection: Lessons
from shallow wetland-dominated shores. Front. Environ. Sci. 7, http://dx.doi.
org/10.3389/fenvs.2019.00049, URL https://www.frontiersin.org/article/10.3389/
fenvs.2019.00049/full.

Möller, I., Kudella, M., Rupprecht, F., Spencer, T., Paul, M., van Wesenbeeck, B.K.,
Wolters, G., Jensen, K., Bouma, T.J., Miranda-Lange, M., Schimmels, S., 2014. Wave
attenuation over coastal salt marshes under storm surge conditions. Nat. Geosci. 7
(10), 727–731. http://dx.doi.org/10.1038/ngeo2251, URL http://www.nature.com/
articles/ngeo2251.

Moosavi, S., 2017. Ecological coastal protection: Pathways to living shorelines. Procedia
Eng. 196 (2017), 930–938. http://dx.doi.org/10.1016/j.proeng.2017.08.027, URL
https://linkinghub.elsevier.com/retrieve/pii/S187770581733148X.

Morison, J., Johnson, J., Schaaf, S., 1950. The force exerted by surface waves on
piles. J. Pet. Technol. 2 (05), 149–154. http://dx.doi.org/10.2118/950149-G, URL
http://www.onepetro.org/doi/10.2118/950149-G.

Mork, M., 1996. The effect of kelp in wave damping. Sarsia 80 (4), 323–327. http://
dx.doi.org/10.1080/00364827.1996.10413607, URL http://www.tandfonline.com/
doi/full/10.1080/00364827.1996.10413607.

Mullarney, J.C., Henderson, S.M., 2010. Wave-forced motion of submerged single-
stem vegetation. J. Geophys. Res. 115 (C12), C12061. http://dx.doi.org/10.1029/
2010JC006448, URL http://doi.wiley.com/10.1029/2010JC006448.

Myrhaug, D., 1995. Bottom friction beneath random waves. Coast. Eng. 24 (3–4), 259–
273. http://dx.doi.org/10.1016/0378-3839(94)00023-Q, URL https://linkinghub.
elsevier.com/retrieve/pii/037838399400023Q.

CoastalEngineering160(2020)10373715L. Zhu et al.

Neckles, H., Short, F., Barker, S., Kopp, B., 2005. Disturbance of eelgrass Zostera
marina by commercial mussel mytilus edulis harvesting in Maine: dragging impacts
and habitat recovery. Mar. Ecol. Prog. Ser. 285, 57–73. http://dx.doi.org/10.3354/
meps285057, URL http://www.int-res.com/abstracts/meps/v285/p57-73/.

Nepf, H., 2011. Flow over and through biota.

In: Treatise on Estuarine and
Coastal Science, Vol. 2. Elsevier, pp. 267–288. http://dx.doi.org/10.1016/
B978-0-12-374711-2.00213-8, URL https://linkinghub.elsevier.com/retrieve/pii/
B9780123747112002138.

Newell, C.R., Short, F., Hoven, H., Healey, L., Panchang, V., Cheng, G., 2010.
The dispersal dynamics of juvenile plantigrade mussels (Mytilus edulis L.) from
eelgrass (Zostera marina) meadows in Maine, U.S.A.. J. Exp. Mar. Biol. Ecol.
394 (1–2), 45–52. http://dx.doi.org/10.1016/j.jembe.2010.06.025, URL https://
linkinghub.elsevier.com/retrieve/pii/S0022098110002388.

Nowacki, D.J., Beudin, A., Ganju, N.K., 2017. Spectral wave dissipation by submerged
aquatic vegetation in a back-barrier estuary. Limnol. Oceanogr. 62 (2), 736–
753. http://dx.doi.org/10.1002/lno.10456, URL http://doi.wiley.com/10.1002/lno.
10456.

Ondiviela, B., Losada, I.J., Lara, J.L., Maza, M., Galván, C., Bouma, T.J., van Belzen, J.,
2014. The role of seagrasses in coastal protection in a changing climate. Coast.
Eng. 87, 158–168. http://dx.doi.org/10.1016/j.coastaleng.2013.11.005, URL https:
//linkinghub.elsevier.com/retrieve/pii/S0378383913001889.

Pace, N.L., 2011. Wetlands or seawalls? adapting shoreline regulation to address sea
level rise and wetland preservation in the gulf of Mexico. J. Land Use Environ.
Law 26 (2), 327–363, URL https://www.jstor.org/stable/42842968.

Paul, M., Amos, C.L., 2011. Spatial and seasonal variation in wave attenuation over
Zostera noltii. J. Geophys. Res. 116 (C8), C08019. http://dx.doi.org/10.1029/
2010JC006797, URL http://doi.wiley.com/10.1029/2010JC006797.

Peteiro, C., Freire, Ó., 2013. Biomass yield and morphological features of the seaweed
saccharina latissima cultivated at two different sites in a coastal bay in the Atlantic
coast of Spain. J. Appl. Phycol. 25 (1), 205–213. http://dx.doi.org/10.1007/
s10811-012-9854-9, URL http://link.springer.com/10.1007/s10811-012-9854-9.

Peteiro, C., Sánchez, N., Martínez, B., 2016. Mariculture of

the Asian kelp
undaria pinnatifida and the native kelp Saccharina latissima along the At-
lantic coast of Southern Europe: An overview. Algal Res. 15, 9–23. http:
//dx.doi.org/10.1016/j.algal.2016.01.012, URL https://linkinghub.elsevier.com/
retrieve/pii/S2211926416300236.

Pinsky, M.L., Guannel, G., Arkema, K.K., 2013. Quantifying wave attenuation to inform
coastal habitat conservation. Ecosphere 4 (8), art95. http://dx.doi.org/10.1890/
ES13-00080.1, URL http://doi.wiley.com/10.1890/ES13-00080.1.

Plew, D.R., 2011. Depth-averaged drag coefficient

for modeling flow through
suspended Canopies. J. Hydraul. Eng. 137 (2), 234–247. http://dx.doi.org/
10.1061/(ASCE)HY.1943-7900.0000300, URL http://ascelibrary.org/doi/10.1061/
%28ASCE%29HY.1943-7900.0000300.

Plew, D.R., Enright, M.P., Nokes, R.I., Dumas, J.K., 2009. Effect of mussel bio-pumping
on the drag on and flow around a mussel crop rope. Aquac. Eng. 40 (2), 55–61.
http://dx.doi.org/10.1016/j.aquaeng.2008.12.003, URL https://linkinghub.elsevier.
com/retrieve/pii/S0144860908001076.

Plew, D.R., Stevens, C., Spigel, R., Hartstein, N., 2005. Hydrodynamic implications of
large offshore mussel farms. IEEE J. Ocean. Eng. 30 (1), 95–108. http://dx.doi.org/
10.1109/JOE.2004.841387, URL http://ieeexplore.ieee.org/document/1435580/.

Raman-Nair, W., Colbourne, B., 2003. Dynamics of a mussel longline system. Aquac.
Eng. 27 (3), 191–212. http://dx.doi.org/10.1016/S0144-8609(02)00083-3, URL
https://linkinghub.elsevier.com/retrieve/pii/S0144860902000833.

Raman-Nair, W., Colbourne, B., Gagnon, M., Bergeron, P., 2008. Numerical model
of a mussel
longline system: Coupled dynamics. Ocean Eng. 35 (13), 1372–
1380. http://dx.doi.org/10.1016/j.oceaneng.2008.05.008, URL https://linkinghub.
elsevier.com/retrieve/pii/S0029801808001212.

Rao, S.S., 2007. Vibration of Continuous Systems. John Wiley & Sons, Inc., Hobo-
ken, New Jersey, URL https://wp.kntu.ac.ir/hrahmanei/Adv-Vibrations-Books/
Continuous-Vibrations-Rao.pdf.

Raupach, M., Thom, A.S., 1981. Turbulence in and above plant canopies. Annu.
Rev. Fluid Mech. 13 (1), 97–129. http://dx.doi.org/10.1146/annurev.fl.13.010181.
000525, URL http://www.annualreviews.org/doi/10.1146/annurev.fl.13.010181.
000525.

van Rooijen, A., Lowe, R., Rijnsdorp, D., Ghisalberti, M., Jacobsen, N.G., McCall, R.,
2020. Wave driven mean flow dynamics in submerged canopies. J. Geophys. Res. 0–
3. http://dx.doi.org/10.1029/2019JC015935, URL https://onlinelibrary.wiley.com/
doi/abs/10.1029/2019JC015935.

Saleh, F., Weinstein, M.P., 2016. The role of nature-based infrastructure (NBI) in
coastal resiliency planning: A literature review. J. Environ. Manag. 183, 1088–1098.
http://dx.doi.org/10.1016/j.jenvman.2016.09.077, URL https://linkinghub.elsevier.
com/retrieve/pii/S0301479716307484.

Sarpkaya, T., O’Keefe, J.L., 1996. Oscillating flow about two and three-dimensional
bilge keels. J. Offshore Mech. Arct. Eng. 118 (1), 1–6. http://dx.doi.org/10.1115/
1.2828796, URL https://asmedigitalcollection.asme.org/offshoremechanics/article/
118/1/1/434651/Oscillating-Flow-About-Two-and-ThreeDimensional.

Scyphers, S.B., Powers, S.P., Heck, K.L., Byron, D., 2011. Oyster reefs as natural
breakwaters mitigate shoreline loss and facilitate Fisheries. In: Browman, H. (Ed.),
PLoS One 6 (8), e22396. http://dx.doi.org/10.1371/journal.pone.0022396, URL
https://dx.plos.org/10.1371/journal.pone.0022396.

Seymour, R.J., Hanes, D., 1979. Performance analysis of tethered float breakwater.
J. Waterw. Port Coast. Ocean Div. 105 (3), 265–280, URL https://cedb.asce.org/
CEDBsearch/record.jsp?dockey=0008922.

Smyth, C., Hay, A.E., 2002. Wave

J.
Phys. Oceanogr. 32 (12), 3490–3498. http://dx.doi.org/10.1175/1520-0485(2002)
032<3490:WFFINS>2.0.CO;2, URL http://journals.ametsoc.org/doi/abs/10.1175/
1520-0485%282002%29032%3C3490%3AWFFINS%3E2.0.CO%3B2.

friction factors

in nearshore

sands.

Stévant, P., Rebours, C., Chapman, A., 2017. Seaweed aquaculture in Norway: recent
industrial developments and future perspectives. Aquac. Int. 25 (4), 1373–1390.
http://dx.doi.org/10.1007/s10499-017-0120-7, URL http://link.springer.com/10.
1007/s10499-017-0120-7.

Stevens, C., Plew, D., Hartstein, N., Fredriksson, D., 2008. The physics of open-
water shellfish aquaculture. Aquac. Eng. 38 (3), 145–160. http://dx.doi.org/
10.1016/j.aquaeng.2008.01.006, URL https://linkinghub.elsevier.com/retrieve/pii/
S0144860908000071.

long-line mussel

Stevens, C.L., Plew, D.R., Smith, M.J., Fredriksson, D.W., 2007. Hydrodynamic
forcing of
J. Waterw. Port Coast.
Ocean Eng. 133 (3), 192–199. http://dx.doi.org/10.1061/(ASCE)0733-950X(2007)
133:3(192), URL http://ascelibrary.org/doi/10.1061/%28ASCE%290733-950X%
282007%29133%3A3%28192%29.

farms: Observations.

Sutton-Grier, A.E., Wowk, K., Bamford, H., 2015. Future of our coasts: The potential
for natural and hybrid infrastructure to enhance the resilience of our coastal
communities, economies and ecosystems. Environ. Sci. Pol. 51, 137–148. http:
//dx.doi.org/10.1016/j.envsci.2015.04.006, URL https://linkinghub.elsevier.com/
retrieve/pii/S1462901115000799.

Suzuki, T., Hu, Z., Kumada, K., Phan, L., Zijlema, M., 2019. Non-hydrostatic modeling
of drag, inertia and porous effects in wave propagation over dense vegetation fields.
Coast. Eng. 149, 49–64. http://dx.doi.org/10.1016/j.coastaleng.2019.03.011, URL
https://linkinghub.elsevier.com/retrieve/pii/S0378383917304179.

Suzuki, T., Zijlema, M., Burger, B., Meijer, M.C., Narayan, S., 2012. Wave dissipation
by vegetation with layer schematization in SWAN. Coast. Eng. 59 (1), 64–
71. http://dx.doi.org/10.1016/j.coastaleng.2011.07.006, URL https://linkinghub.
elsevier.com/retrieve/pii/S0378383911001347.

Syvitski, J.P.M., Kettner, A.J., Overeem, I., Hutton, E.W.H., Hannon, M.T., Braken-
ridge, G.R., Day, J., Vörösmarty, C., Saito, Y., Giosan, L., Nicholls, R.J., 2009.
Sinking deltas due to human activities. Nat. Geosci. 2 (10), 681–686. http://dx.
doi.org/10.1038/ngeo629, URL http://www.nature.com/articles/ngeo629.

Tebaldi, C., Strauss, B.H., Zervas, C.E., 2012. Modelling sea level rise impacts on
storm surges along US coasts. Environ. Res. Lett. 7 (1), 014032. http://dx.doi.org/
10.1088/1748-9326/7/1/014032, URL https://iopscience.iop.org/article/10.1088/
1748-9326/7/1/014032.

Temmerman, S., Meire, P., Bouma, T.J., Herman, P.M., Ysebaert, T., De Vriend, H.J.,
2013. Ecosystem-based coastal defence in the face of global change. Nature 504
(7478), 79–83. http://dx.doi.org/10.1038/nature12859, URL http://www.nature.
com/articles/nature12859.

UNEP, 2006. Marine and Coastal Ecosystems and Human Well-Being: A Synthesis Report
Based on the Findings of the Millennium Ecosystem Assessment. UNEP, p. 76, URL
https://www.millenniumassessment.org/documents/Document.799.aspx.pdf.

Utter, Denny, 1996. Wave-induced forces on the giant kelp Macrocystis pyrifera
(Agardh): field test of a computational model. J. Exp. Biol. 199, 2645–2654, URL
https://jeb.biologists.org/content/199/12/2645.short.

van Veelen, T.J., Fairchild, T.P., Reeve, D.E., Karunarathna, H., 2020. Experimental
study on vegetation flexibility as control parameter for wave damping and velocity
structure. Coast. Eng. 157, 103648. http://dx.doi.org/10.1016/j.coastaleng.2020.
103648, URL https://linkinghub.elsevier.com/retrieve/pii/S0378383919300663.
Vuik, V., Jonkman, S.N., Borsje, B.W., Suzuki, T., 2016. Nature-based flood protection:
The efficiency of vegetated foreshores for reducing wave loads on coastal dikes.
Coast. Eng. 116, 42–56. http://dx.doi.org/10.1016/j.coastaleng.2016.06.001, URL
https://linkinghub.elsevier.com/retrieve/pii/S0378383916301004.

Walls, A.M., Kennedy, R., Edwards, M., Johnson, M., 2017. Impact of kelp cultivation on
the ecological status of benthic habitats and Zostera marina seagrass biomass. Mar.
Pollut. Bull. 123 (1–2), 19–27. http://dx.doi.org/10.1016/j.marpolbul.2017.07.048,
URL https://linkinghub.elsevier.com/retrieve/pii/S0025326X1730629X.

Weinkle, J., Landsea, C., Collins, D., Musulin, R., Crompton, R.P., Klotzbach, P.J.,
Pielke, R., 2018. Normalized hurricane damage in the continental United States
1900–2017. Nature Sustain. 1 (12), 808–813. http://dx.doi.org/10.1038/s41893-
018-0165-2, URL http://www.nature.com/articles/s41893-018-0165-2.

Wu, W.-C., Ma, G., Cox, D.T., 2016. Modeling wave attenuation induced by the vertical
density variations of vegetation. Coast. Eng. 112, 17–27. http://dx.doi.org/10.
1016/j.coastaleng.2016.02.004, URL https://linkinghub.elsevier.com/retrieve/pii/
S0378383916300199.

Xiao, X., Agusti, S., Lin, F., Li, K., Pan, Y., Yu, Y., Zheng, Y., Wu, J., Duarte, C.M., 2017.
Nutrient removal from chinese coastal waters by large-scale seaweed aquaculture.
Sci. Rep. 7 (1), 46613. http://dx.doi.org/10.1038/srep46613, URL http://www.
nature.com/articles/srep46613.

Xie, D., Zou, Q.-P., Mignone, A., MacRae, J.D., 2019. Coastal flooding from wave
overtopping and sea level
rise adaptation in the northeastern USA. Coast.
Eng. 150, 39–58. http://dx.doi.org/10.1016/j.coastaleng.2019.02.001, URL https:
//linkinghub.elsevier.com/retrieve/pii/S0378383917305653.

CoastalEngineering160(2020)10373716L. Zhu et al.

Yang, Y., Chai, Z., Wang, Q., Chen, W., He, Z., Jiang, S., 2015. Cultivation of
seaweed Gracilaria in Chinese coastal waters and its contribution to environmental
improvements. Algal Res. 9, 236–244. http://dx.doi.org/10.1016/j.algal.2015.03.
017, URL https://linkinghub.elsevier.com/retrieve/pii/S2211926415000806.
Zeller, R.B., Weitzman, J.S., Abbett, M.E., Zarama, F.J., Fringer, O.B., Koseff, J.R., 2014.
Improved parameterization of seagrass blade dynamics and wave attenuation based
on numerical and laboratory experiments. Limnol. Oceanogr. 59 (1), 251–266.
http://dx.doi.org/10.4319/lo.2014.59.1.0251, URL http://doi.wiley.com/10.4319/
lo.2014.59.1.0251.

Zhu, L., Chen, Q., 2015. Numerical modeling of surface waves over submerged
flexible vegetation. J. Eng. Mech. 141 (8), A4015001. http://dx.doi.org/
10.1061/(ASCE)EM.1943-7889.0000913, URL http://ascelibrary.org/doi/10.1061/
%28ASCE%29EM.1943-7889.0000913.

Zhu, L., Huguenard, K., Fredriksson, D., 2018. Interaction between waves and hanging
highly flexible kelp blades. Coast. Eng. Proc. 1 (36), 31. http://dx.doi.org/10.9753/
icce.v36.papers.31, URL https://journals.tdl.org/icce/index.php/icce/article/view/
8427.

Zhu, L., Huguenard, K., Fredriksson, D.W., 2019. Dynamic analysis of longline aqua-
culture systems with a coupled 3D numerical model. In: The Twenty-Ninth (2019)
International Ocean and Polar Engineering Conference. the International Society
of Offshore and Polar Engineers (ISOPE), Honolulu, Hawaii, USA, pp. 1305–1310,
URL https://onepetro.org/conference-paper/ISOPE-I-19-235.

Zhu, L., Zou, Q., 2017. Three-layer analytical solution for wave attenuation by
suspended and nonsuspended vegetation canopy. Coast. Eng. Proc. 1 (35),
27. http://dx.doi.org/10.9753/icce.v35.waves.27, URL https://icce-ojs-tamu.tdl.
org/icce/index.php/icce/article/view/8239.

Zhu, L., Zou, Q.-P., Huguenard, K., Fredriksson, D.W., 2020. Mechanisms for the asym-
metric motion of submerged aquatic vegetation in waves: A consistent-mass cable
model. J. Geophys. Res. 125 (2), 1–31. http://dx.doi.org/10.1029/2019JC015517,
URL https://onlinelibrary.wiley.com/doi/abs/10.1029/2019JC015517.

Zijlema, M., Stelling, G., Smit, P., 2011. SWASH: An operational public domain code
for simulating wave fields and rapidly varied flows in coastal waters. Coast.
Eng. 58 (10), 992–1012. http://dx.doi.org/10.1016/j.coastaleng.2011.05.015, URL
https://linkinghub.elsevier.com/retrieve/pii/S0378383911000974.

Zou, Q., 2004. A simple model for random wave bottom friction and dissipation. J.
Phys. Oceanogr. 34 (6), 1459–1467. http://dx.doi.org/10.1175/1520-0485(2004)
034<1459:ASMFRW>2.0.CO;2, URL http://journals.ametsoc.org/doi/abs/10.1175/
1520-0485%282004%29034%3C1459%3AASMFRW%3E2.0.CO%3B2.

Zou, Q., Hay, A.E., 2003. The vertical structure of

the wave bottom boundary
layer over a sloping bed: Theory and field measurements. J. Phys. Oceanogr. 33
(7), 1380–1400. http://dx.doi.org/10.1175/1520-0485(2003)033<1380:TVSOTW>
2.0.CO;2, URL http://journals.ametsoc.org/doi/abs/10.1175/1520-0485%282003%
29033%3C1380%3ATVSOTW%3E2.0.CO%3B2.

CoastalEngineering160(2020)10373717