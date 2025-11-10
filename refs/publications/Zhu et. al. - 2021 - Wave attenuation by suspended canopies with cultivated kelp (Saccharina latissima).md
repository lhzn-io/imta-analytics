Contents lists available at ScienceDirect

Coastal Engineering

journal homepage: www.elsevier.com/locate/coastaleng

Wave attenuation by suspended canopies with cultivated kelp (Saccharina
latissima)
Longhuan Zhu a,∗, Jiarui Lei b, Kimberly Huguenard a, David W. Fredriksson c
a Department of Civil and Environmental Engineering, University of Maine, Orono, ME, 04469, USA
b Department of Civil and Environmental Engineering, Massachusetts Institute of Technology, Cambridge, MA, 02139, USA
c Department of Naval Architecture and Ocean Engineering, U.S. Naval Academy, Annapolis, MD, 21402, USA

A R T I C L E I N F O

A B S T R A C T

Keywords:
Wave attenuation
Kelp
Saccharina latissima
Bulk drag coefficient
Effective blade length
Suspended canopies

Many kelp aquaculture farms consist of moored arrays of long horizontal lines that grow kelp near the
water surface. Most kelp farms are deployed in the same direction of wave propagation. However, with
numerous longlines of densely grown kelp, these farms may have the potential to attenuate waves if installed
perpendicular to the direction of wave propagation. In this application, the kelp farm may serve as a form of
nature-based coastal protection. To assess this potential, a set of 1:10 scale physical model experiments were
conducted to measure the wave attenuation of a suspended kelp model. The model was scaled based on the
morphological and mechanical properties of the cultivated Saccharina latissima (sugar kelp) from Saco Bay,
Maine, USA. Experimental results demonstrated that suspended blades have asymmetric oscillatory motions
with more bending in the opposite direction of wave propagation. Due to severe asymmetric blade motion
in large waves, the suspended blade could roll over the attached line following the wave orbital motion.
The results also showed that suspended kelp farms in the designed configuration with 20 longlines of 1-
m-long blades and 100 blades/m have the potential attenuating wave energy by up to 33.7% under the
experimental wave conditions. Based on the experimental data, empirical formulas were developed for the
bulk drag coefficient (𝐶𝐷𝐵) and effective blade length (𝑙𝑒) of suspended kelp canopies for wave attenuation.
To predict wave attenuation under a wider range of conditions and to identify the key parameters affecting
wave attenuation, a numerical model was developed that could resolve blade motion. The benefits of resolving
blade motion were to improve the model accuracy and reduce the number of experiments needed for obtaining
𝐶𝐷𝐵 or 𝑙𝑒, which is required in the conventional wave attenuation models based on the rigid blade assumption.
The results indicate that (i) the wave energy dissipation ratio (𝐸𝐷𝑅 defined as the ratio of the dissipated wave
energy to the incident wave energy) of suspended kelp farms decreases with increased water depth, (ii) 𝐸𝐷𝑅
is not sensitive to wave height, (iii) 𝐸𝐷𝑅 first increases and then decreases with wavelength, and (iv) 𝐸𝐷𝑅
increases with blade size, kelp vertical position, plant density, and the number of longlines. Therefore, the
technique to improve the wave attenuation capacity of suspended kelp farms for nature-based coastal defense
is to install the kelp farms in shallower water, expand the farm size by adding more longlines, locate the kelp
in a higher position of the water column, grow the kelp more densely, and choose the kelp species with more
rigid, wider, and longer blades/biomass.

1. Introduction

Kelp is considered one of many types of brown macroalgae sea-
weeds that contribute to coastal ecosystems by providing food, shelter,
and enhanced oxygen habitats for fish and marine animals. Kelp also
provides services such as recycling inorganic nutrients, preventing
eutrophication, reducing carbon dioxide concentration, and potentially
mitigating ocean acidification (Duarte et al., 2017; Stévant et al., 2017;

Xiao et al., 2017; Campbell et al., 2019; Bricknell et al., 2020). Further-
more, the existence of kelp can physically influence the environmental
hydrodynamics. For example, Macrocystis pyrifera (giant kelp) forests
can significantly reduce currents (Jackson, 1997; Gaylord et al., 2007;
Rosman et al., 2007) and internal wave amplitudes (Jackson, 1984;
Rosman et al., 2007) off west coast of California, USA. However, no
significant (surface) wave attenuation was observed over M. pyrifera
forests by Elwany et al. (1995), which is likely due to the compliant

∗ Corresponding author.

E-mail address:

longhuan.zhu@maine.edu (L. Zhu).

https://doi.org/10.1016/j.coastaleng.2021.103947
Received 8 September 2020; Received in revised form 19 April 2021; Accepted 20 June 2021

CoastalEngineering168(2021)103947Availableonline21June20210378-3839/©2021ElsevierB.V.Allrightsreserved.L. Zhu et al.

nature of the kelp, the sparse canopy density (∼ 0.1 plants/m2) and the
limited canopy height related to the water depths (typical averages of
10 m). Similar results are also observed for highly flexible Nereocystis
luetkeana bull kelp,Gaylord et al. (2003) and deeply submerged Ecklonia
radiata (< 10% of the water column, Morris et al., 2019). However,
Laminaria hyperborea (tangle) with 25 plants/m2 in shallow water (5
m) have been observed to reduce wave energy by 70%–85% over a
distance of 258 m (Mork, 1996).

Unlike wild kelp that grows on the seafloor, kelp aquaculture farms
that float may also have the potential to dissipate wave energy, es-
pecially since surface wave energy is concentrated near the surface.
Furthermore, many kelp aquaculture farms are densely seeded to max-
imize economic output. With densely cultivated kelp, suspended farms
may provide more favorable wave attenuation than naturally occurring
kelp beds containing a sparse plant density.

Wave attenuation theories for submerged canopies including wild
kelp beds have been developed by Dalrymple et al. (1984) and
Kobayashi et al. (1993) by assuming rigid kelp and vegetation subject
to monochromatic wave action. These wave attenuation models were
then extended for flexible vegetation (Asano et al., 1992; Méndez et al.,
1999; Mullarney and Henderson, 2010; Riffe et al., 2011; Luhar et al.,
2017; Lei and Nepf, 2019b; Zhu et al., 2020a), random waves (Mendez
and Losada, 2004; Chen and Zhao, 2012; Jacobsen et al., 2019; Zhu
et al., 2020a), and combined waves and currents (Hu et al., 2014;
Losada et al., 2016; Chen et al., 2018; Yin et al., 2020). To analyze
the effects of blade motion on wave attenuation, Asano et al. (1992)
and Méndez et al. (1999) simplified the blade motion as an oscillator
with one degree of freedom by assuming blade deflection is linearly
distributed along the blade length and averaging the deflection along
the length. To obtain the depth dependent blade deflection, Rosman
et al. (2013) discretized the blade into segments and solved the force
balance equations for each segments by assuming negligible bending
momentum and shear stresses between adjacent segments. To obtain
the analytical solutions for blade motion considering bending momen-
tum and shear stresses, Mullarney and Henderson (2010), Riffe et al.
(2011), and Henderson (2019) modeled the blade as a continuous
cantilever beam by using Euler–Bernoulli techniques and ignoring the
blade inertia and inertia forces.Recently, Zhu et al. (2020a, 2021)
extended the analytical solutions for blade motion by incorporating
the inertia forces for both chromatic wave and random waves. These
analytical solutions are achieved by assuming a small deflection to
linearize the blade curvature. To consider the nonlinear blade curvature
(geometric nonlinearity) in large blade motion, numerical methods are
often used (e.g., Zeller et al., 2014; Luhar and Nepf, 2016; Chen and
Zou, 2019; Zhu et al., 2020b). Recently, Zhu et al. (2020b) used a
cable model to capture the asymmetric ‘‘whip-like’’ blade motion and
proposed mechanisms for the asymmetric blade motion in symmetric
waves.

The wave attenuation theories developed by Dalrymple et al. (1984)
and Kobayashi et al. (1993) were then extended to floating and sus-
pended canopies by Plew et al. (2005) and Zhu and Zou (2017),
respectively. Zhu and Zou (2017) showed that the suspended and float-
ing canopies can reduce more wave energy than submerged canopies
in the same conditions because wave orbital velocities decrease to-
ward the bottom, especially for shorter waves. However, these ap-
proaches assumed a rigid canopy component without motion, which
may overestimate the wave attenuation. Recently, Zhu et al. (2020a)
extended the wave attenuation methods to be frequency dependent
for random waves and incorporated the motion of the flexible canopy
component. Compared to nearshore submerged aquatic vegetation
(SAV), suspended aquaculture structures are less affected by water level
changes since suspended aquaculture structures float near the water
surface (Zhu et al., 2020a). In one case study, Zhu et al. (2020a) demon-
strated that the implementation of aquaculture structures offshore can
extend the wave attenuation capacity of SAV-based living shorelines
over wider ranges of wave frequency and water level. With numerical

techniques, such as the SWASH (Simulating WAves till SHore, Zijlema
et al., 2011) model, Chen et al. (2019) investigated the wave-driven
circulation cell induced by suspended canopies and found that the
vertical position of the canopy also has significant effects on the wave-
driven current in the canopy. Although these studies have provided
important insight into the wave attenuation potential of suspended
aquaculture farms, experimental research to quantify the performance
of suspended kelp aquaculture structures is still needed.

Research to examine the hydrodynamic characteristics of kelp
blades in steady flow was conducted by Buck and Buchholz (2005). In
their study, the drag characteristics of both a single and an aggregate
of Saccharina latissima (sugar kelp) blades were investigated with tow
tests in still water. The results showed sheltering interactions among
the blades so that the drag force of an aggregate of kelp blades cannot
be estimated by simply superimposing the drag of individual blades.
Vettori and Nikora (2019) investigated the turbulent flow interaction
with single blades of S. latissima in an open-channel flume and showed
enhanced turbulence in blade wakes. At low current speeds, the flap-
ping motion of kelp blades of S. latissima, M. pyrifera, and N. luetkeana
can significantly enhance the nutrient flux to the blade surface (Huang
et al., 2011). Using polyethylene to model S. latissima, Vettori and
Nikora (2018) found that the model kelp blades increase the turbulence
intensity and reduce the mean longitudinal velocity. By comparing
the hydrodynamic performance of S. latissima with the performance
of the model blades, Vettori et al. (2020) showed that the model
blades replicated many aspects of S. latissima blade dynamics, although
the drag force and reconfiguration were underestimated. To avoid the
dynamic similarity issues, Fredriksson et al. (2020) conducted full-scale
model experiments to understand the hydrodynamics of an aggregate
of model S. latissima blades in steady flow. Fredriksson et al. (2020)
showed a threshold for reconfiguration as the tow speed at which the
horizontal component of tangential drag was equal or exceeded the
horizontal component of the normal drag. To build upon this work,
it is important to examine the dynamics of suspended kelp blades in
waves and the value of suspended kelp aquaculture structures for wave
attenuation in a laboratory environment. Appropriate parameters from
these experiments are essential for modeling wave attenuation with
canopy models.

The objective of this study is to quantify the wave attenuation
capacity of suspended kelp canopies with a scaled physical model in
a set of laboratory experiments. To predict wave attenuation under a
wider range of conditions, a simple numerical model was developed
based on the blade dynamic model in Zhu et al. (2020b). This model
was also used to perform dynamic similarity analysis in preparation
for the model tests. The physical model kelp material was chosen from
the measured morphological and mechanical properties of cultivated
S. latissima from Saco Bay, Maine in the USA considering dynamic
similarity. The motions of both a single and an aggregate of blades were
recorded to analyze the blade dynamics with focus on the mechanisms
for observed roll-up and roll-over of suspended blades. The horizontal
forces on unsheltered single blades and sheltered blades were mea-
sured to examine the differences. The wave height evolution along the
suspended canopy was also measured to investigate wave attenuation
performance. With the experimental results, bulk drag coefficient and
effective blade length estimates for the suspended canopy were devel-
oped. The numerical model was compared with the datasets and then
used to investigate the potential of using suspended kelp aquaculture
structures as nature-based coastal protection.

2. Theory

2.1. Blade dynamics and dynamical similarity

The dynamics of kelp blades in waves can be described using the
cable model in Zhu et al. (2020b) by representing the structure as
a cantilever beam discretized as blade segments (𝑑𝑠). The velocity

CoastalEngineering168(2021)1039472L. Zhu et al.

Fig. 1. Sketch for the coordinate systems. The global Cartesian reference frame is (𝑥, 𝑧) with 𝑥 = 0 at the leading edge of the canopy and 𝑧 = 0 at the still water level (SWL). A
local Lagrangian coordinate system at a distance of 𝑠 along the blade length (𝑙) is (⃗𝑡, ⃗𝑛) with the angle of 𝜙 between the horizontal line and the blade tangential direction (⃗𝑡). The
suspended blade is fixed at the upper end with distance of 𝑑1 below the SWL. The canopy length is 𝐿𝑣. The water depth is ℎ.

components of the blade segment are defined using a local Lagrangian
coordinate system (⃗𝑡, ⃗𝑛) along the blade length with ⃗𝑡 representing the
blade-tangential direction and ⃗𝑛 as the blade-normal direction (Fig. 1).
The velocity components in the blade-tangential direction (𝑢) and
normal direction (𝑤) are a function of the distance (𝑠) along the blade
length (𝑙) from the fixed end with time (𝑡). The wave velocity field
(𝑈 , 𝑊 ) is defined using global Cartesian coordinates (𝑥, 𝑧), where the
horizontal coordinate 𝑥 is positive in the direction of wave propagation
with 𝑥 = 0 at the leading edge of the kelp canopy and the vertical
coordinate 𝑧 is positive upward with 𝑧 = 0 at the still water level
(SWL). The angle of the tangential direction (⃗𝑡) relative to the horizontal
direction (𝑥) is 𝜙. Thus, the points in the Lagrangian coordinate system
(⃗𝑡, ⃗𝑛) can be obtained by rotating the global Cartesian coordinates (𝑥, 𝑧)
counterclockwise by 𝜙. In the procedure, a set of normalized variables
were applied to the governing equations in Zhu et al. (2020b) and
described as,

̂𝑠 =

𝑠
𝑙

, ̂𝑡 = 𝑡𝜔, ̂𝑢 =

𝑢
𝑙𝜔

,

̂𝑤 =

𝑤
𝑙𝜔

,

̂𝑇 =

𝑇 𝑙2
𝐸𝐼

,

̂𝑈 =

𝑈
𝑈𝑚

, and ̂𝑊 =

𝑊
𝑈𝑚

,

(1)

where 𝑇 is the effective tension of the blade, 𝐸 is the bending elastic
modulus, 𝐼 = 𝑏𝑑3∕12 is the second moment of the cross-section area of
the blade with 𝑏 the blade width and 𝑑 the blade thickness, 𝜔 = 2𝜋∕𝑇𝑤
is the wave angular frequency with 𝑇𝑤 the wave period, and 𝑈𝑚 is
the magnitude of the horizontal wave orbital velocity. Therefore, the
dimensionless governing equations for the blade motion are given by

+

𝜕 ̂𝑇
𝜕 ̂𝑠

𝜕2𝜙
𝜕 ̂𝑠2

+ 𝐵 sin 𝜙

𝜕𝜙
𝜕 ̂𝑠
1
𝐶𝑓 2(1 + 𝛿)𝐶𝑎 ∣ −𝐿 ̂𝑢 + ̂𝑈 cos 𝜙 + ̂𝑊 sin 𝜙 ∣ (−𝐿 ̂𝑢 + ̂𝑈 cos 𝜙 + ̂𝑊 sin 𝜙)
2

+

+2𝜋

𝐶𝑎𝛿
𝐾𝐶

[

(

−𝜌′𝐿

)

𝜕 ̂𝑢
𝜕̂𝑡

− ̂𝑤

𝜕𝜙
𝜕̂𝑡

+

𝜕 ̂𝑈
𝜕̂𝑡

cos 𝜙 +

𝜕 ̂𝑊
𝜕̂𝑡

]

sin 𝜙

= 0,

(2)

−

+

+ ̂𝑇

𝜕𝜙
𝜕 ̂𝑠

+ 𝐵 cos 𝜙

𝜕3𝜙
𝜕 ̂𝑠3
1
𝐶𝑑𝑖𝐶𝑎 ∣ −𝐿 ̂𝑤 − ̂𝑈 sin 𝜙 + ̂𝑊 cos 𝜙 ∣ (−𝐿 ̂𝑤 − ̂𝑈 sin 𝜙 + ̂𝑊 cos 𝜙)
2

+𝐶𝑚2𝜋

𝐶𝑎𝛿
𝐾𝐶
[

[

−𝐿

𝜕 ̂𝑤
𝜕̂𝑡
𝜕 ̂𝑤
𝜕̂𝑡

(

+

𝜕
𝜕̂𝑡

]
− ̂𝑈 sin 𝜙 + ̂𝑊 cos 𝜙)
(
)

+ ̂𝑢

𝜕𝜙
𝜕̂𝑡

−

𝜕 ̂𝑈
𝜕̂𝑡

sin 𝜙 +

𝜕 ̂𝑊
𝜕̂𝑡

+2𝜋

𝐶𝑎𝛿
𝐾𝐶

−𝜌′𝐿

]
cos 𝜙

= 0,

𝜕 ̂𝑢
𝜕 ̂𝑠
and
𝜕 ̂𝑤
𝜕 ̂𝑠

+ ̂𝑤

𝜕𝜙
𝜕 ̂𝑠

−

1
12

𝛿2𝑆2 𝜕 ̂𝑇
𝜕̂𝑡

= 0,

− ̂𝑢

𝜕𝜙
𝜕 ̂𝑠

+

𝜕𝜙
𝜕̂𝑡

= 0.

The dimensionless parameters governing the blade dynamics include
the aspect ratio,

𝛿 = 𝑑∕𝑏,

the slenderness,

𝑆 = 𝑏∕𝑙,

the length ratio,

𝐿 = 𝑙∕𝐴𝑤,

the Keulegan–Carpenter number,

𝐾𝐶 = 𝑈𝑚𝑇𝑤∕𝑏,

the density ratio,

𝜌′ = 𝜌𝑣∕𝜌,

the buoyant parameter,

𝐵 = (𝜌 − 𝜌𝑣)𝑔𝑏𝑑𝑙3∕𝐸𝐼 = (1 − 𝜌′)𝐶𝑎∕𝐹 2
𝑟 ,

and the Cauchy number,

𝐶𝑎 = 𝜌𝑏𝑈 2

𝑚𝑙3∕𝐸𝐼,

(6)

(7)

(8)

(9)

(10)

(11)

(12)

where 𝜌𝑣 is the blade mass density, 𝜌 is the water density, 𝑔 is the
gravitational acceleration, 𝐴𝑤 = 𝑈𝑚∕𝜔 is the wave orbital excursion,
and 𝐹𝑟 = 𝑈𝑚∕
𝑔𝑏 is the Froude number. In (2), the friction coefficient
is (Abdelrhman, 2007; Zeller et al., 2014)

√

𝐶𝑓 = 0.074𝑅𝑒−1∕5

(13)

with the Reynolds number 𝑅𝑒 = 𝑈𝑚𝑏∕𝜈 and 𝜈 the fluid kinematic
viscosity. In (3), the drag coefficient is

𝐶𝑑𝑖 = max(10𝐾𝐶 −1∕3, 1.95)

(3)

and the added mass coefficient is

𝐶𝑚 = min(𝐶𝑚1, 𝐶𝑚2)

with 𝐶𝑚1 =

{

1 + 0.35𝐾𝐶 2∕3, 𝐾𝐶 < 20
1 + 0.15𝐾𝐶 2∕3, 𝐾𝐶 ≥ 20

(14)

(15)

and 𝐶𝑚2 = 1 + (𝐾𝐶 − 18)2∕49

(4)

(5)

(Luhar, 2012; Luhar and Nepf, 2016). The formulas for 𝐶𝑑𝑖 and 𝐶𝑚
are obtained from the experiments by Keulegan and Carpenter (1958)
and Sarpkaya and O’Keefe (1996) for rigid plates in oscillatory flow
with 𝐾𝐶 from 1.7 to 118.2. It is noted that the drag coefficient 𝐶𝑑𝑖
is for an individual blade in oscillatory flow and hereinafter referred

CoastalEngineering168(2021)1039473L. Zhu et al.

to as ‘‘individual drag coefficient’’ to distinguish from the ‘‘bulk drag
coefficient’’ defined in Section 2.2.

The dynamic similarity for the blade motion requires the same
dimensionless parameters in (6) to (12) for the model and the full-
scale prototype. The aspect ratio (𝛿), slenderness (𝑆), and length ratio
(𝐿) represent the geometrical property and the 𝐾𝐶 number represent
the inertia property of fluid. The similarity for 𝛿, 𝑆, 𝐿, and 𝐾𝐶
can be satisfied by Froude similarity criteria (including geometrical
similarity). The density ratio 𝜌′, buoyant parameter 𝐵, and Cauchy
number 𝐶𝑎 represent the blade material properties. However, they are
not independent as 𝐵 = (1 − 𝜌′)𝐶𝑎∕𝐹 2
(11). Therefore, two of the
𝑟
following parameters: 𝜌′, 𝐵, and 𝐶𝑎 are the required criteria to select
the material to fabricate the model blades. In a similar approach, Fryer
et al. (2015) used 𝜌′ and 𝐶𝑎 as the similarity criteria to fabricate the
model kelp blade for Macrocystis with a silicone-based polymer.

In this study, the blade is fixed and suspended at the upper end
(𝑠 = 0) with tangential direction downward such that 𝜙 = 3𝜋∕2 for
the initial static state (Fig. 1). Thus, the boundary conditions are set as
̂𝑤 = 0, and 𝜙 = 3𝜋∕2 at the fixed end with ̂𝑠 = 0, as well as
̂𝑢 = 0,
̂𝑇 = 0, 𝜕𝜙∕𝜕 ̂𝑠 = 0, and 𝜕2𝜙∕𝜕 ̂𝑠2 = 0 at the free end with ̂𝑠 = 1. The
relationships between 𝑠 and (𝑥, 𝑧) are

𝑠

cos 𝜙𝑑𝑠

𝑥 = ∫

0

and

𝑧 = −𝑑1 + ∫

𝑠

0

sin 𝜙𝑑𝑠,

(16)

(17)

where 𝑑1 is the distance from the upper fixed end of the blade to SWL
(Fig. 1). Eqs. (16) and (17) are required to calculate the blade posture
and convert the flow velocity from global Cartesian coordinates to local
Lagrangian coordinates. Solving the blade dynamical equations (2) to
(5) with boundary conditions yields the blade velocity (𝑢, 𝑤), effective
tension (𝑇 ), and direction angle (𝜙). The shear force along the blade
can be obtained by

𝑄 = 𝐸𝐼

𝜕2𝜙
𝜕𝑠2

.

(18)

Details of numerically solving the nonlinear partial differential equa-
tions are referred to Zhu et al. (2020b).

2.2. Wave attenuation

For linear waves, the wave orbital velocities are expressed as (Dean

and Dalrymple, 1991)

𝑈 =

and

𝑊 =

𝐻
2

𝜔

cosh 𝑘(ℎ + 𝑧)
sinh 𝑘ℎ

cos(𝑘𝑥 − 𝜔𝑡)

𝐻
2

𝜔

sinh 𝑘(ℎ + 𝑧)
sinh 𝑘ℎ

sin(𝑘𝑥 − 𝜔𝑡),

(19)

(20)

where 𝐻 is the wave height, ℎ is the water depth, and 𝑘 = 2𝜋∕𝜆 is
the wave number with 𝜆 being the wavelength and determined by the
dispersion equation 𝜔2 = 𝑔𝑘 tanh 𝑘ℎ.

Wave energy dissipation is assumed to be the work of canopy
drag following Zhu et al. (2020a) for which the conservation equation
becomes
𝜕𝐸𝑐𝑔
𝜕𝑥

𝐶𝑑𝑖𝜌𝑏|𝑈𝑅|𝑈 2

𝑅𝑑𝑠,

𝑁𝛼𝜖

(21)

𝑙

1
2

= − ∫
0

As the sheltering effects are considered using the factor 𝛼𝜖, the relative
velocity 𝑈𝑅 is therefore calculated using the blade normal velocity 𝑤
of an unsheltered single blade and the incident wave orbital velocity
(𝑈 , 𝑊 ) without modifications for sheltering effects. Solving (21) with
(22) yields the transmitted wave height 𝐻(𝑥) at distance 𝑥 in relation
to the incident wave height 𝐻0 at 𝑥 = 0,
𝐻(𝑥)
𝐻0
where the wave decay coefficient (𝑘𝐷) is expressed as

1
1 + 𝑘𝐷𝐻0𝑥

(23)

=

,

𝑘𝐷 =

8𝛼𝜖𝑏𝑁𝑘2 sinh2 𝑘ℎ
𝜔3(2𝑘ℎ + sinh 2𝑘ℎ) ∫

𝐻 3
0

𝑙

0

𝐶𝑑𝑖|𝑈𝑅|𝑈 2

𝑅𝑑𝑠.

For a rigid blade with (𝑢, 𝑤) = 0 and 𝜙 = 3𝜋∕2, (24) becomes

𝑘𝐷,𝑅 =

=

8𝛼𝜖 𝑏𝑁𝑘2 sinh2 𝑘ℎ
𝜔3(2𝑘ℎ + sinh 2𝑘ℎ) ∫

𝐻 3
0
𝛼𝜖 𝐶𝑑𝑖𝑏𝑁𝑘
9𝜋

𝑙

0

𝐶𝑑𝑖|𝑈 |𝑈 2𝑑𝑠

⋅

9 sinh 𝑘(ℎ − 𝑑1) − 9 sinh 𝑘(ℎ − 𝑑1 − 𝑙) + sinh 3𝑘(ℎ − 𝑑1) − sinh 3𝑘(ℎ − 𝑑1 − 𝑙)
sinh 𝑘ℎ(2𝑘ℎ + sinh 2𝑘ℎ)

.

(24)

(25)

For a sparse canopy with 𝛼𝜖 = 1, (25) reduces to the solution by Zhu and
Zou (2017), which can be further reduced to the solutions of Dalrymple
et al. (1984) and Kobayashi et al. (1993) for bottom-rooted vegetation
with 𝑑1 = ℎ − 𝑙.

Solution (24) for the wave decay coefficient 𝑘𝐷 of flexible blades
is an implicit expression that requires calculating the relative velocity
𝑈𝑅 between blades and waves by resolving the blade motion. Thus,
solving (24) is computationally expensive. However, for rigid blades,
(24) reduces to an explicit expression, i.e., (25), which is very easy to
calculate. In order to obtain a similar explicit expression as (25) for flex-
ible blades, the bulk drag coefficient and effective blade length methods
with a rigid blade assumption are used. The assumption of rigid blades
can overestimate the wave attenuation for flexible blades. To reduce the
overestimation, the bulk drag coefficient (𝐶𝐷𝐵) is therefore defined as a
reduced drag (𝐶𝐷𝐵 < 𝐶𝑑𝑖) such that ∫ 𝑙
0 𝐶𝐷𝐵|𝑈 |𝑈 2𝑑𝑠,
yielding

0 𝐶𝑑𝑖|𝑈𝑅|𝑈 2

𝑅𝑑𝑠 = ∫ 𝑙

𝑘𝐷 =

=

=

8𝛼𝜖 𝑏𝑁𝑘2 sinh2 𝑘ℎ
𝜔3(2𝑘ℎ + sinh 2𝑘ℎ) ∫
𝐻 3
0
8𝛼𝜖 𝑏𝑁𝑘2 sinh2 𝑘ℎ
𝜔3(2𝑘ℎ + sinh 2𝑘ℎ) ∫

0

0

𝐻 3
0
𝛼𝜖 𝐶𝐷𝐵 𝑏𝑁𝑘
9𝜋

𝑙

𝑙

𝐶𝑑𝑖|𝑈𝑅|𝑈 2

𝑅𝑑𝑠

𝐶𝐷𝐵 |𝑈 |𝑈 2𝑑𝑠

(26)

⋅

9 sinh 𝑘(ℎ − 𝑑1) − 9 sinh 𝑘(ℎ − 𝑑1 − 𝑙) + sinh 3𝑘(ℎ − 𝑑1) − sinh 3𝑘(ℎ − 𝑑1 − 𝑙)
sinh 𝑘ℎ(2𝑘ℎ + sinh 2𝑘ℎ)

.

Similarly, the effective blade length (𝑙𝑒) is defined as a reduced blade
length (𝑙𝑒 < 𝑙) such that ∫ 𝑙

𝐶𝑑𝑖|𝑈 |𝑈 2𝑑𝑠, yielding

0 𝐶𝑑𝑖|𝑈𝑅|𝑈 2

𝑅𝑑𝑠 = ∫ 𝑙𝑒

0

𝑘𝐷 =

=

=

8𝛼𝜖 𝑏𝑁𝑘2 sinh2 𝑘ℎ
𝜔3(2𝑘ℎ + sinh 2𝑘ℎ) ∫
𝐻 3
0
8𝛼𝜖 𝑏𝑁𝑘2 sinh2 𝑘ℎ
𝜔3(2𝑘ℎ + sinh 2𝑘ℎ) ∫

0

0

𝐻 3
0
𝛼𝜖 𝐶𝑑𝑖𝑏𝑁𝑘
9𝜋

𝑙

𝑙𝑒

𝐶𝑑𝑖|𝑈𝑅|𝑈 2

𝑅𝑑𝑠

𝐶𝑑𝑖|𝑈 |𝑈 2𝑑𝑠

⋅

9 sinh 𝑘(ℎ − 𝑑1) − 9 sinh 𝑘(ℎ − 𝑑1 − 𝑙𝑒) + sinh 3𝑘(ℎ − 𝑑1) − sinh 3𝑘(ℎ − 𝑑1 − 𝑙𝑒)
sinh 𝑘ℎ(2𝑘ℎ + sinh 2𝑘ℎ)

.

(27)

where 𝐸 = 𝜌𝑔𝐻 2∕8 is the local wave energy per unit horizontal area,
𝑐𝑔 = 𝜔(1+2𝑘ℎ∕ sinh 2𝑘ℎ)∕2𝑘 is the wave group velocity, 𝑁 is the canopy
≤ 1
density defined as the number of blades per unit horizontal area, 𝛼𝜖
is a factor to consider the sheltering effects between blades with 𝛼𝜖 = 1
for no sheltering, and 𝑈𝑅 is the relative velocity normal to the blade
with

𝑈𝑅 = −𝑤 − 𝑈 sin 𝜙 + 𝑊 cos 𝜙.

(22)

The bulk drag coefficient and effective blade length methods are com-
putationally efficient by removing the computation requirements for
blade motion. Additionally, the explicit expression is easier to ana-
lyze the characteristics of wave attenuation. However, the empirical
values of 𝐶𝐷𝐵 and 𝑙𝑒 need to be determined from detailed laboratory
experiments. Some empirical formulas for 𝐶𝐷𝐵 (e.g., Kobayashi et al.,
1993; Mendez and Losada, 2004; Augustin et al., 2009; Bradley and
Houser, 2009; Sánchez-González et al., 2011; Jadhav et al., 2013;

CoastalEngineering168(2021)1039474L. Zhu et al.

Anderson and Smith, 2014; Ozeren et al., 2014; Chen et al., 2018; van
Veelen et al., 2020) and 𝑙𝑒 (e.g., Luhar et al., 2017; Lei and Nepf,
2019a,b) have been developed for submerged canopies. However, a
need exists to develop 𝐶𝐷𝐵 and 𝑙𝑒 formulas of suspended canopies for
wave attenuation applications.

To quantify the wave attenuation through a canopy with length of
𝐿𝑣, wave transmission ratio (𝐻𝑇 𝑅) and wave energy dissipation ratio
(𝐸𝐷𝑅) are often used. The wave transmission ratio is defined as the
ratio of the wave height at the ending edge of the canopy to the incident
wave height and given by

𝐻𝑇 𝑅 =

𝐻(𝐿𝑣)
𝐻(0)

=

1
1 + 𝑘𝐷𝐻0𝐿𝑣

.

(28)

The wave energy dissipation ratio is defined as the ratio of the dissi-
pated wave energy to the incident wave energy and given by

𝐸𝐷𝑅 =

𝐻(0)2 − 𝐻(𝐿𝑣)2
𝐻(0)2

= 1 − 𝐻𝑇 𝑅2 = 1 −

1
(1 + 𝑘𝐷𝐻0𝐿𝑣)2

.

(29)

3. Experiments

3.1. Measurements for cultivated S. latissima

The model kelp material is selected based on the properties of the
S. latissima cultivated on a 60 m kelp aquaculture longline in Saco
Bay, Maine, USA. S. latissima is one of the most extensively farmed
kelp species in Maine and in the USA (Augyte et al., 2017; Breton
et al., 2018; Sappati et al., 2019; Grebe et al., 2019; Mao et al., 2020;
Grebe et al., 2021). Two sets of kelp samples were collected from two
nonadjacent 10 cm regions of the longline on May 17, 2018, with 43
(0.689 kg) and 38 (0.683 kg) samples, respectively. Therefore, the aver-
aged plant density and yield were about 405 plants/m and 6.86 kg/m.
The kelp samples were stored in seawater. The morphological and
mechanical properties of the kelp samples were measured within 24 h
after collection to minimize the effects of kelp deterioration.

S. latissima consists of holdfast, stipe and blade (Fig. 2a). Compared
to the dimensions of kelp blade, the holdfast and stipe are small and
difficult to match in the physical model. To illustrate this characteristic,
consider the 1.90 m-long kelp on Fig. 2a as an example, the stipe length
is 15 cm and 8.6% of the blade length at 175 cm. The diameter of the
stipe is 5.8 mm and 4.5% of the blade width at 130.4 mm. In a 1:10
physical model, the model stipe diameter is less than 0.58 mm. Thus,
the holdfast and stipe are not geometrically modeled in this study.
However, the rigid holdfast and stipe are important to fix the blade and
therefore affect the blade bending. To model the effects of the holdfast
and stipe, the fixed base of the model blade is designed such that the
ratio of the length of the fixing base to the length of the flexible part of
the model blade is 5.2%, which is comparative to the ratio of the stipe
length to the blade length in the field (e.g., 8.6% for the S. latissima
sample on Fig. 2).

The kelp blade morphological characteristics were measured from
77 samples using a ruler for the blade length, a caliper for the blade
width and a micrometer for the blade thickness. The blade width was
determined by taking the average from three positions: near the stipe,
in the middle and near the tip. Thickness values were obtained along
the blade width at intervals of 1.27 cm (0.5 in) with at least five
positions.

The mass density and bending elastic modulus were measured from
41 rectangular specimens cut out from 6 to 9 different positions along
the blade length of 6 blades. Since the kelp tissue started to degrade
and die after cuts were made, the measurements for each specimen
were completed within 2 min, and the measurements for one whole
kelp blade sample were completed within 1 h. The specimens were cut
out from the center part of the blade where the blade thickness varies
slightly with an averaged standard deviation of less than 0.5% of the
averaged thickness. Thus, the cross section can be considered as a rect-
angular section and the volume of the specimen can be calculated using

the averaged thickness, width and length. The mass of the specimen
was measured using a digital balance scale with the precision of 0.1
mg. To control the effects of the wetness of the specimen, the specimen
was placed between two layers of a paper towel to reduce the seawater
attached on the specimen surface. The specimen was still wet, but not
dripping during the measurements. Due to the loss of surface water and
kelp degradation, the measured mass values decreased by 4% during
the course of the experiment. The averaged mass value was used in
this study.

The bending elastic modulus of the kelp blade was measured using
the cantilever beam bending test (Fig. 2b). Four bending tests were
conducted for each specimen with measurements taken on both ends
and both sides, for 164 tests. For each bending test, a photo of the
bending blade was taken to record the blade posture. The blade posture
was extracted using ImageJ (a Java-based image processing program,
Schneider et al., 2012; Liang et al., 2017). Given a value of 𝐸, solving
(2) and (3) by setting 𝑢 = 0, 𝑤 = 0, and 𝜌 = 0 with boundary conditions
yields 𝜙, which can be used to calculate the blade posture with (16)
and (17). The measured 𝐸 is set as the value with which the calculated
blade posture fits best with the measured blade posture (Fig. 2c).
The calculated blade postures compared well with the measured blade
postures, with 𝑅2 > 0.95 for 160 tests and 𝑅2 = 0.88, 0.89, 0.92, and
0.93 for the other 4 tests.

3.2. Experimental design

The laboratory experiments were conducted in the 24 m-long,
38 cm-wide, and 60 cm-high wave flume in the Nepf Environmental
Fluid Mechanics Lab at Massachusetts Institute of Technology in August
2018. The model experiments were designed at a scale of 1:10 to match
the dimensions of the wave flume. The wave conditions were designed
based on Froude similarity. The model kelp blade was made to satisfy
the similarity for (6) to (12).

In the physical model experiments, the holdfast, stipe, the ruffle of
the kelp blade, and the variance of thickness were too small to scale so
that the kelp was modeled as a rectangular flat plate with a constant
thickness. The material selected for modeling kelp blades was silicon
film with 𝜌𝑣 = 1.20 g/cm3, 𝐸 = 2.04 MPa, and 𝑑 = 0.10 mm. The model
kelp was designed as a 10.16 cm (4 in) long and 0.95 cm (3/8 in) wide
rectangular plate. The fixed part of the blade was 𝑙𝑟 = 0.5 cm so that
the flexible part of the blade was 𝑙𝑓 = 9.66 cm with 𝑙𝑟∕𝑙𝑓 = 5.2%. It
is noted that the fixed part of the blade is to model the effects of kelp
stipe and the flexible part of the blade is to model the kelp blade. Thus,
the corresponding full-scale kelp blade was 96.6 cm long, 9.5 cm wide
and 1.0 mm thick. To satisfy dynamical similarity, the mass density and
bending elastic modulus of the full scale kelp blade were designed as
𝜌𝑣 = 1.23 g/cm3 and 𝐸 = 21.0 MPa, such that
(𝜌′)𝑀
(𝜌′)𝐹

(𝐶𝑎)𝑀
(𝐶𝑎)𝐹

(𝐵)𝑀
(𝐵)𝐹

(𝐿)𝑀
(𝐿)𝐹

(𝛿)𝑀
(𝛿)𝐹

= 1,

= 1,

= 1,

= 1,

= 1,

(𝐾𝐶)𝑀
(𝐾𝐶)𝐹

= 1, and

(𝑆)𝑀
(𝑆)𝐹

= 1,

(30)

where the subscript ( )𝑀 denotes the dimensionless parameter for
the model and ( )𝐹 denotes the dimensionless parameter for the full
scale prototype. The properties of the full-scale model blade will be
compared with the measurements for S. latissima blade in Section 4.1.
A kelp farm includes numerous kelp plants attached to a horizontal
rope. In this laboratory experiment, the horizontal rope was modeled
using a rigid stainless steel welding rod with a diameter of 0.89 mm
(0.035 in). For each model longline, 31 aggregates of model kelp blades
with 10 blades for each aggregate were fixed to the model longline
(Fig. 3a).

The plant density for the model longline was 10 plants/cm equiv-
alent to 100 plants/m for the full scale, which was less than the
measured values at 405 plants/m in this study. The rod was mounted to
a stainless steel frame attached to the flume walls (Fig. 3b). The model

CoastalEngineering168(2021)1039475L. Zhu et al.

Fig. 2. (a) Saccharina latissima sample with bending elastic modulus (𝐸) at three positions along the blade length. (b) Bending test for a specimen. (c) Comparison between the
measured and calculated blade postures. The measured 𝐸 is the value with which the calculated blade posture has the largest 𝑅2 compared with the data. Photo credit: Yu-Ying
Chen.

Fig. 3. Photos of (a) a model kelp longline and (b) the model kelp farms with waves propagating from left to right (see video S2 for the video in the supplementary materials).
Sketches of (c) the side view of the wave flume showing the setup of model kelp farms and wave gauges and (d) the front view of section A-A showing the setup of load cells.

kelp farm consisted of 20 model sections with a distance of 20 cm apart
in the flume. Thus, the total canopy length was 𝐿𝑣 = 3.8 m equivalent

to 38 m in the full scale. The canopy density 𝑁 was 5263 plants/m2.

CoastalEngineering168(2021)1039476L. Zhu et al.

Three vertical positions of the model kelp farm beneath the SWL with
𝑑1 = 6, 11, and 16 cm were compared in the experiments.

A set of experiments were then conducted to investigate the dynam-
ics of a single blade and a blade in the canopy with a water depth of
40 cm. The suspended blade was fixed at 11 cm below the SWL. The
wave height ranged from 1.4 cm to 6 cm with 4 wave periods of 0.8 s, 1
s, 1.4 s, and 2 s. The blade motion was recorded by a Canon 5D Mark III
camera for 10 wave periods at 50 frames per second. The videos were
processed using MATLAB R2019b.

After the blade dynamics were investigated, another set of exper-
iments was then conducted to assess the wave attenuation. As the
suspended blades were observed to roll over the attached rod in large
wave heights, the largest wave heights were set at 3.8 cm to prevent
the blade roll over the attachment in the wave attenuation experiments.
For the wave attenuation experiments, the incident wave height was
𝐻𝐼0 = 1.8–3.8 cm, wave period was 𝑇𝑤 = 0.8–2 s, water depth was
ℎ = 30–40 cm, and wavelength was 𝜆 = 103–369 cm with 𝜆∕ℎ = 2.7–10.9,
𝐻𝐼0∕ℎ = 0.05–0.11, 𝑙𝑓 ∕ℎ = 0.24–0.32, and 𝑑1∕ℎ = 0.2–0.4. The canopy
covered 1 to 3.7 wavelengths. Thus, for the equivalent full-scale model,
the waves were 18 cm to 38 cm in height with period of 2.6 to 6.3 s
in 3 to 4 m-deep water. To calculate 𝑅𝑒, 𝐾𝐶, 𝐶𝑎, and 𝐿, as well as the
hydrodynamic coefficients 𝐶𝑓 , 𝐶𝑑𝑖, and 𝐶𝑚, the horizontal wave orbital
velocity at the fixed end of the flexible part of the blade was used,
yielding 𝑅𝑒 = 406–861, 𝐾𝐶 = 4.4–18.8, 𝐶𝑎 = 9667–43406, 𝐿 = 3.4–14.4,
𝐶𝑓 = 0.02, 𝐶𝑑𝑖 = 3.8–6.1, and 𝐶𝑚 = 1–2.5. A total of 14 cases were run
with the detailed characteristics shown in Table 1.

3.3. Wave decay measurements

The wave decay experiment setup is shown on Fig. 3. During the
tests, the wave height was measured using two resistance-type wave
gauges with one permanently mounted at 50 cm before the canopy
and the other moving along the canopy to measure the wave height
evolution for each case. The fixed wave gauge provided a reference
measurement to show that the wave conditions were steady throughout
one case. The movable wave gauge collected data along the canopy at
an interval of 5 cm or up to 15 cm depending on the wavelength (with
at least 20 horizontal positions for one wavelength). At each horizontal
position, the wave gauge measured the water elevation at 1000 Hz for
1 min (including 30 to 74 wave periods).

The wave reflection ratio of the flume is estimated at 7% (Lei and
Nepf, 2019b), yielding an oscillating wave height along the canopy
(Fig. 4). Assuming that the incident wave height and reflected wave
height decay follow (23) at the same decay coefficient 𝑘𝐷 along the
canopy, a local wave height in the canopy can be obtained by (31)
given in Box I (with derivation in Appendix A). In (31), 𝐻𝐼0 is the
incident wave height at 𝑥 = 0, 𝐻𝑅𝐿𝑣
is the reflected wave height at
𝑥 = 𝐿𝑣, and 𝜖 is the phase lag. The spatial oscillation period of the
wave height is 1/2 wavelength as shown in the term cos(2𝑘𝑥 + 𝜖).
Eq. (31) provided a good fit (𝑅2 > 0.99) for the incident wave height
and decay coefficient with the nonlinear regression model ‘fitnlm’ in
MATLAB R2019b as shown on Fig. 4. The flume bottom and walls as
well as the kelp supporting frames can also induce wave decay (Fig. 4).
According to Madsen et al. (1988), the wave energy dissipation by the
friction of the flume bottom and walls is proportional to the cubic
of the maximum orbital velocity near the bottom and walls with a
similar expression to the wave energy dissipation by vegetation in (21),
yielding the same wave height transmission in (23) but with a different
wave decay coefficient due to the flume bottom and walls. Therefore,
the wave decay coefficient over the wave flume without kelp can be
also fitted using (31). Since this study focuses on the wave attenuation
due to kelp canopies, the wave decay coefficient due to the flume
bottom and walls as well as the kelp supporting frames is subtracted
from the measured wave decay coefficient for the kelp canopy in the
following analysis.

The model kelp farms consisted of 20 rows (rods) of blades. The rods
were 20 cm apart, which was more than four times of the amplitude
of the blade deflection. For each row, 31 aggregates of blades were
attached separately with 1 aggregate/cm (Fig. 3a). For each aggregate,
10 blades were mounted together so that the front blades sheltered
the blades behind them. The sheltering effects between rods were not
considered in this study. However, the sheltering effects between the
blades in the same aggregate were significant and considered using
a sheltering factor. The sheltering effects for the drag force can be
considered using the force ratio of the sheltered and unsheltered blades
given by

𝛼𝐹 =

𝐹𝑥,𝑟𝑚𝑠
𝛽𝑛𝑓𝑥,𝑟𝑚𝑠

,

(32)

where 𝐹𝑥,𝑟𝑚𝑠 is the root-mean-square (RMS) of the measured horizontal
force on one row of aggregates of sheltered blades, 𝑓𝑥,𝑟𝑚𝑠 is the RMS of
the measured horizontal force on one row of unsheltered single blades,
and 𝛽𝑛 is the ratio of the number of sheltered blades to the number of
unsheltered blades, i.e., the number of blades in one aggregate. It is
noted that the wave energy dissipation is proportional to 𝑈 3
𝑅 in (21)
while the drag force is proportional to 𝑈 2
𝑅. Therefore, the sheltering
factor 𝛼𝜖 used in the calculation of the wave attenuation is defined as
𝛼𝜖 = 𝛼3∕2
𝐹

(33)

with the force ratio 𝛼𝐹 given by (32). To measure the total horizontal
force on one row of blades, two submerged load cells were mounted to
both ends of the rod (Fig. 3d) and recorded at 2000 Hz for 1 min at the
same time. The total force is the sum of the forces at both ends. Similar
to the measurement of 𝑘𝐷, the measured ‘‘forces’’ without kelp were
subtracted from the measured forces with kelp under the same wave
conditions. In this study, 𝑓𝑥,𝑟𝑚𝑠 was measured for 30 isolated blades
on one rod and 𝐹𝑥,𝑟𝑚𝑠 was measured for 30 aggregates of 10 sheltered
blades, i.e., totally 300 blades on one row. Therefore, 𝛽𝑛 was 10 in this
study.

4. Results

4.1. Morphological and mechanical properties of S. latissima compared with
the model blade

To evaluate the design of model kelp blade, the results section be-
gins with understanding the morphological and mechanical properties
of real cultivated S. latissima in Saco Bay, Maine of the USA. The kelp
blade length (𝑙𝑓 ) showed a quasi-linear relationship with the averaged
blade width (𝑏) as

𝑏 = (0.090 ± 0.003)𝑙𝑓 + 1.4 ± 0.2,

(34)

with 𝑅2 = 0.90 (Fig. 5a), where 𝑙𝑓 and 𝑏 are in cm. The blade width has
the following relation with the maximum thickness (𝑑max) at the center
of the blade width,

𝑑max = (0.040 ± 0.007)𝑏 + 0.39 ± 0.08,

(35)

with 𝑅2 = 0.75 (Fig. 5b), where 𝑑max is in mm while 𝑏 is in cm. The
blade thickness (𝑑) showed a normal-like distribution along the blade
width following

(

)2

𝑠𝑏∕𝑏
0.118±0.003

− 1
2

= (0.797 ± 0.011)𝑒

𝑑
𝑑max
with 𝑅2 = 0.94 (Fig. 5c), where 𝑠𝑏 is the distance from the center of the
blade width toward the blade edge.

+ 0.203 ± 0.011,

(36)

The bending elastic modulus increases along the blade length from
near the stipe to near the tip (Fig. 2a). As more mature elements of the
blade are near the tip, 𝐸 is expected to relate to the maturity of the
kelp tissue. The relation between 𝐸 and 𝑑max is

𝐸 = (2.3 ± 1.2)𝑑16±7

max + 5.5 ± 0.7,

(37)

CoastalEngineering168(2021)1039477L. Zhu et al.

Table 1
Wave conditions and hydrodynamic coefficients for the model kelp canopy in the experiments. In this table, 𝑑1 is the vertical location of the longlines from the still water level,
ℎ is the water depth, 𝑇𝑤 is the wave period, 𝐻𝐼0 is the incident wave height, 𝜆 is the wavelength, 𝑈𝑚 is the magnitude of the horizontal wave orbital velocity at the fixed end
of the blade, 𝑙𝑓 is length of the flexible part of the blade, 𝐿𝑣 is the canopy length, 𝑅𝑒 is the Reynolds number, 𝐾𝐶 is the Keulegan–Carpenter number, 𝐶𝑎 is the Cauchy number,
𝐿 is the length ratio, 𝐶𝑑𝑖 is the individual drag coefficient, 𝐶𝑓 is the friction coefficient, and 𝐶𝑚 is the added mass coefficient.

Case
#

𝑑1
[cm]

ℎ
[cm]

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

11
6
11
6
11
11
16
11
16
11
11
6
16
11

40
30
40
30
40
40
40
40
40
40
40
30
40
40

𝑇𝑤
[s]

1.4
2.0
1.4
1.4
1.0
2.0
2.0
2.0
1.4
1.4
1.0
0.8
0.8
0.8

𝐻𝐼0
[cm]

𝜆
[cm]

𝑈𝑚
[cm/s]

1.8
2.9
2.4
2.9
3.1
3.5
3.8
3.7
3.2
3.2
3.6
3.2
3.2
3.2

246
326
246
221
146
369
369
369
246
246
146
103
107
107

4.3
8.2
5.7
8.2
6.8
8.4
8.7
9.0
7.0
7.6
7.9
9.0
5.1
6.6

𝑙𝑓 ∕ℎ

𝐿𝑣∕𝜆

𝑑1∕ℎ

𝜆∕ℎ

𝐻𝐼0∕ℎ

𝑅𝑒

𝐾𝐶

𝐶𝑎

𝐿

𝐶𝑑𝑖

𝐶𝑓

0.24
0.32
0.24
0.32
0.24
0.24
0.24
0.24
0.24
0.24
0.24
0.32
0.24
0.24

1.5
1.2
1.5
1.7
2.6
1.0
1.0
1.0
1.5
1.5
2.6
3.7
3.6
3.6

0.28
0.20
0.28
0.20
0.28
0.28
0.40
0.28
0.40
0.28
0.28
0.20
0.40
0.28

6.1
10.9
6.1
7.4
3.7
9.2
9.2
9.2
6.1
6.1
3.7
3.4
2.7
2.7

0.05
0.10
0.06
0.10
0.08
0.09
0.09
0.09
0.08
0.08
0.09
0.11
0.08
0.08

406
783
545
778
646
798
831
855
669
719
754
861
483
632

6.4
17.3
8.6
12.2
7.1
17.6
18.3
18.8
10.5
11.3
8.3
7.9
4.4
5.8

9667
35 894
17 360
35 383
24 407
37 217
40 419
42 773
26 192
30 272
33 252
43 406
13 642
23 369

10.0
3.7
7.4
5.2
9.0
3.6
3.5
3.4
6.0
5.6
7.7
8.1
14.4
11.0

5.4
3.9
4.9
4.3
5.2
3.8
3.8
3.8
4.6
4.5
4.9
5.0
6.1
5.6

0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02

𝐶𝑚

2.2
1.0
2.5
1.7
2.3
1.0
1.0
1.0
2.1
1.9
2.4
2.4
1.9
2.1

Fig. 4. Measured (red circles for that without kelp and blue triangles for that with kelp) and fitted (solid lines, 𝑅2 = 0.99) wave heights (𝐻) normalized by the incident wave
height (𝐻𝐼0) along the model kelp farms for Case 4. The calculated incident wave height decay with fitted 𝐻𝐼0 and 𝑘𝐷 is denoted by dashed lines. The red thin lines are for the
case without kelp while the blue thick lines are for the case with kelp. The horizontal distance is normalized by the canopy length as 𝑥∕𝐿𝑣.

√
√
√
√
√

(

𝐻(𝑥) =

𝐻𝐼0
1 + 𝑘𝐷𝐻𝐼0𝑥

)2

[

+

𝐻𝑅𝐿𝑣
1 + 𝑘𝐷𝐻𝑅𝐿𝑣

(𝐿𝑣 − 𝑥)

]2

+ 2

𝐻𝐼0
1 + 𝑘𝐷𝐻𝐼0𝑥

𝐻𝑅𝐿𝑣
1 + 𝑘𝐷𝐻𝑅𝐿𝑣

(𝐿𝑣 − 𝑥)

cos(2𝑘𝑥 + 𝜖),

(31)

Box I.

with 𝑅2 = 0.41 (Fig. 5d), where 𝑑max is in mm and 𝐸 is in MPa. The mea-
sured 𝐸 from all specimens ranges from 2.7±1.4 to 22±6 MPa (Fig. 5d).
The measurements in Vettori and Nikora (2017) and Fredriksson et al.
(2020) with 4 ± 3 MPa and 1.3 ± 0.4 MPa, respectively, are also in this
range.

The measured mass density of S. latissima is 1.05 ± 0.03 g/cm3,
which is smaller than the measurement in Fredriksson et al. (2020)
with 1.3 ± 0.3 g/cm3, but comparable to the value of 1.09 ± 0.09 g/cm3
in Vettori and Nikora (2017). The difference may be caused by the
‘‘wetness’’ of the kelp sample since the measured mass of wetter kelp
is larger, resulting in a larger mass density. The measurements are

summarized in Table 2 along with the measurements from published
literature.

The designed properties of the full-scale model kelp blade are also
shown in Table 2 to compare with the measurements in this study and
from published literature. Based on the measurements, for a given kelp
blade length 𝑙𝑓 = 96.6 cm, the expected blade width is 𝑏 = 10.1 ± 0.5
cm using (34), the maximum blade thickness is 𝑑𝑚𝑎𝑥 = 0.79 ± 0.17 mm
using (35), and the bending elastic modulus is 𝐸 = 5.6 ± 0.8 MPa using
(37). The designed width (𝑏 = 9.5 cm) of the full-scale model blade is
slightly smaller than the calculated averaged width (𝑏 = 10.1±0.5 cm) of
S. latissima with the same blade length, while the maximum thickness

CoastalEngineering168(2021)1039478L. Zhu et al.

Fig. 5. Morphological and mechanical properties of S. latissima. (a) Relation between the averaged blade width (𝑏) and the blade length (𝑙𝑓 ). (b) Relation between the maximum
thickness (𝑑max) and the averaged blade width. (c) The distribution of the normalized blade thickness (𝑑∕𝑑max) along the normalized distance (𝑠𝑏∕𝑏) from the blade center. (d)
Bending elastic modulus (𝐸).

Table 2
Morphological and mechanical properties of cultivated S. latissima and model kelp blades.

Study site

Model kelp blade (scale 1:10)
Designed full-scale kelp blade
Measured values in this study

Saco, Maine, US

Fredriksson et al. (2020)
Vettori and Nikora (2017)
Augyte et al. (2017)

Maine, US
Loch Fyne, Scotland, UK
Bristol, Maine, US

Peteiro and Freire (2013)

Sorrento, Maine, US

Ares, Spain
Sada, Spain

aCalculated 𝑏 using (34) for the given 𝑙𝑓 = 96.6 cm.
bCalculated 𝑑max using (35) for given 𝑏 = 10.1 ± 0.5 cm.
cCalculated 𝐸 using (37) for given 𝑑 = 0.79 ± 0.17 mm.
dNarrow-bladed kelp.

Mass
density
𝜌𝑣 [g/cm3]

1.2
1.23
1.05 ± 0.03

1.3 ± 0.3
1.09 ± 0.09
–
–
–
–
–
–

Elastic
modulus
𝐸 [MPa]

2.04
21.0
5.6 ± 0.8c
(2.7 ± 1.4 − 22 ± 6)
1.3 ± 0.4
4 ± 3
–
–
–
–
–
–

Blade
length
𝑙𝑓 [cm]

9.66
96.6
96.6
(3 − 177.7)
Up to 300
15 − 65
220.4d
56.9
147.4d
71.4
152.9
123.2

Blade
width
𝑏 [cm]

0.95
9.5
10.1 ± 0.5a
(1 − 18.5)
–
3.6 − 13.1
4.67d
8.72
2.76d
7.38
12.1
11.4

Maximum
blade thickness
𝑑max [mm]

Blades
per meter
[m−1]

0.10
1.0
0.79 ± 0.17b
(0.44 − 1.08)
0.4 ± 0.1
0.42 − 1.8
–
–
–
–
–
–

1000
100
405

–
–
330d
–
400d
–
745
728

(𝑑max = 1.0 mm) is slightly larger than that (𝑑max = 0.79 ± 0.17 mm)
of the real S. latissima. However, the designed dimensions of the full
scale kelp blade are within the range of the measurements as shown in
Table 2. The designed mass density (𝜌𝑣 = 1.23 g/cm3) of the full-scale
model blade is larger than the measured value of 1.05 ± 0.03 g/cm3,
but comparable to the measurement in Fredriksson et al. (2020) with
1.3±0.3 g/cm3 for cultivated S. latissima in Maine. The designed bending
elastic modulus 𝐸 = 21.0 MPa of the full-scale model kelp blade is large
but still within the range of the measurements (2.7 ± 1.4 to 22 ± 6 MPa).

The designed plant density 100 plants/m is smaller than the measured
value of 405 plants/m.

4.2. Wave-induced motion of suspended blades

To understand the wave-induced dynamics of suspended blades as
well as the sheltering effects among blades, the motion of a single
suspended blade is compared with that of an aggregate of suspended
blades on Fig. 6 (with video S3 in the supplementary materials), where

CoastalEngineering168(2021)1039479L. Zhu et al.

Fig. 6. Postures for (a and c) a single blade and (b and d) a row of blades in waves with wave heights of (a and b) 1.5 cm and (c and d) 2.8 cm, respectively. The wave period
(𝑇𝑤) is 1.4 s and water depth is 40 cm. The blade is fixed at 11 cm below the still water level. The waves propagate from left to right. The left four columns show the blade
posture at one phase. The fifth column shows the blade postures for 12 phases in one wave period with the black line indicates the posture at 𝑡 = 0 and 𝑡 = 𝑇𝑤 while the gray
lines indicate the postures at other phases. In (b5) and (d5), the red dotted lines indicate the postures of one representative blade in an aggregate of blades. See video S3 for the
video in the supplementary materials.

the waves propagate from left to right with a period of 1.4 s at 40 cm
water depth. Due to high flexibility, the blade shows a higher-mode
(≥ 3) motion (Fig. 6a and c) with large asymmetry (Fig. 6a5 and
c5). Unlike bottom-fixed vegetation inclining to the wave propagation
direction (Zhu et al., 2020b), the suspended blade fixed at the upper
end inclines to the opposite direction of wave propagation. For waves
propagating to the right, the action of the vertical wave orbital velocity
on the blade provides clockwise momentum that drives the bottom-
fixed blade also to the right (Zhu et al., 2020b) but drives the suspended
blade to the left. The asymmetry of blade motion increases with blade
deflection and wave height (Fig. 6a and c). More information about the
mechanisms and properties of asymmetric blade motion in waves can
be found in Zhu et al. (2020b).

The motion of the blade in an aggregate of blades shows a smaller-
amplitude motion than a single blade in the same wave conditions
(e.g., Fig. 6a and b). This is caused by the sheltering from neighboring
blades in the same aggregate, which reduces the flow velocity to

the sheltered blades. Therefore, the deflection of a sheltered blade
is smaller than that of an unsheltered single blade. Accordingly, the
motion asymmetry of the sheltered blade is also smaller than that of
the unsheltered single blade (e.g., Fig. 6a and b).

The blade was observed to wrap up and roll over the attached line
when the wave height exceeded a critical value (Fig. 7 with video S4
in the supplementary materials). The unsheltered single blade rolled
over when the wave height reached 2.8 cm for 𝑇𝑤 = 2 s, 3.3 cm for
𝑇𝑤 = 1.4 s (Fig. 7), 3.7 cm for 𝑇𝑤 = 1 s, and 3.5 cm for 𝑇𝑤 = 0.8 s. Due
to sheltering effects, the threshold values increased for the sheltered
blades in an aggregate, especially for the blade in the center of the
aggregate that was sheltered by more blades.

The roll-over motion of the suspended blade results from the asym-
metric blade motion driven by the wave orbital motion. When the
wave height increases to a critical value, the asymmetry of the blade
motion becomes so large that the blade is almost horizontal, providing
conditions for the onset of rolling over.

CoastalEngineering168(2021)10394710L. Zhu et al.

Fig. 7. Postures for a single blade in waves with wave height of 3.3 cm. The wave period (𝑇𝑤) is 1.4 s and water depth is 40 cm. The blade is fixed at 11 cm below the still
water level. The waves propagate from left to right. The black line indicates the posture at the end of the given time (𝑡) while the gray lines indicate the previous postures in that
wave period. The blade starts to wrap up and roll over the attached line in the 18th wave period (c) and continue to roll over the attached line again until reaching a steady
state after 26 wave periods (k–p). See video S4 for the video in the supplementary materials.

To demonstrate the mechanisms that drive the suspended blade to
roll over the attached line, the blade motion (Fig. 7) at representative
phases is analyzed with the corresponding wave orbital motion (Fig. 8).
As shown on Fig. 8, the blade is almost horizontal at the 17th period.
At time 𝑡 = 17.25𝑇𝑤 (Fig. 8c), the wave orbital velocity points upward
and drives the blade to bend upward and exceeds where the fixed end
is located. After 𝑡 = 17.5𝑇𝑤, the wave orbital velocity points to the right
and drives the blade to the right (Fig. 8e) to pass over the attachment
(Fig. 8f). Then at 𝑡 = 17.75𝑇𝑤 (Fig. 8g), the wave orbital velocity points
downward and drives the blade downward. Therefore, the portion of
the blade that passed over the attachment moves down below the
attachment. Although the wave orbital velocity changes direction back
toward after 𝑡 = 17.75𝑇𝑤, the blade does not unravel due to the
presence of the longline (Fig. 8h). After 𝑡 = 18.375𝑇𝑤, the restoring
force induced by the second curvature of the blade acts clockwise in
the same direction of the wave orbital motion. Thus, the blade passes
the longline in a shape like a ‘‘fly casting loop’’ (Fig. 8l to p). The whole
blade rolls over the longline by the 18th period. In the following time,

the blade rolls over the blade again (Fig. 7) until reaching a steady
state.

4.3. Horizontal force and wave attenuation

The measured force ratio 𝛼𝐹 , sheltering factor 𝛼𝜖, wave decay coeffi-
cient 𝑘𝐷, wave transmission ratio (𝐻𝑇 𝑅), and wave energy dissipation
ratio (𝐸𝐷𝑅) are listed in Table 3. As 𝛼𝐹 and 𝛼𝜖 are expected to be less
than 1, the values 𝛼𝐹 = 1.536 and 𝛼𝜖 = 1.904 for Case 12 are so large
that they may be not correct. Additionally, removing these single values
would not significantly impact the mean values of 𝛼𝐹 and 𝛼𝜖. Thus, they
were not used in this study. The rest measured 𝛼𝐹 ranging from 0.506
to 1.031 with the mean value 𝛼𝐹 = 0.724 and 𝛼𝜖 ranging from 0.360
to 1.047 with the mean value 𝛼𝜖 = 0.630 were used in the numerical
calculations for 𝐹𝑥,𝑟𝑚𝑠 and 𝑘𝐷.

To obtain the numerical simulations for 𝐹𝑥,𝑟𝑚𝑠 and 𝑘𝐷, the input
wave field (𝑈 , 𝑊 ) were estimated using linear wave theory (19) and
(20), which provided a good approximation with 𝑅2 = 0.91 for the
waves in the flume of this study (Luhar and Nepf, 2016), especially

CoastalEngineering168(2021)10394711L. Zhu et al.

Fig. 8. Suspended blade postures with flow field. The waves propagate from left to right with wave height of 3.3 cm and wave period 𝑇𝑤 = 1.4 s at water depth of 40 cm. The
flow field is calculated using linear wave theory (Dean and Dalrymple, 1991). The blade is fixed at 11 cm below the still water level. The blade starts to roll over the longline
at time 𝑡 = 17.5𝑇𝑤 for this case (e). The shaded regions indicate the position of the supporting frame. The part of the blade in the shaded region was plotted using a smoothing
curve that connect the visible blade segments. This does not impact the analysis on the mechanisms for the rolling over of suspended blades. See video S4 for the video in the
supplementary materials.

for small-amplitude waves. Since the blade included a rigid part (𝑙𝑟)
and a flexible part (𝑙𝑓 ), the computation for 𝑘𝐷 (24) was split into
two parts, i.e., the wave decay coefficient 𝑘𝐷𝑟 for the rigid part as
an integral over [0, 𝑙𝑟], and the wave decay coefficient 𝑘𝐷𝑓 for the
flexible part as an integral over [𝑙𝑟, 𝑙] according to the property of
the integral. The integral over [0, 𝑙𝑟] for the rigid part was reduced
to (25) with 𝑙 = 𝑙𝑟 while the integral over [𝑙𝑟, 𝑙] for the flexible part
was still (24) with 𝑙 = 𝑙𝑓 . As the rigid parts of the blades in the same
aggregate were fixed together, the rigid parts in the same aggregate
were considered as one element such that the canopy density for the
rigid parts was 526.3 elements/m2 (i.e., 526.3 aggregates/m2) and the
sheltering effects among the elements were negligible. Thus, 𝑘𝐷𝑟 was
calculated using (25) with 𝑙 = 𝑙𝑟, 𝑁 = 526.3 m−2, 𝛼𝜖 = 1, and 𝐶𝑑𝑖 in
Table 1 calculated using (14). For the flexible part, the blade motion
was obtained by solving the blade dynamical equations (2) to (5) with
(𝑈 , 𝑊 ) and the corresponding initial and boundary conditions, yielding

the blade velocity (𝑢, 𝑤) and direction angle 𝜙. In the computation
for the blade motion, the used friction coefficient 𝐶𝑓 , drag coefficient
𝐶𝑑𝑖, and added mass coefficient 𝐶𝑚 are shown in Table 1, which
were calculated using (13), (14), and (15) with the magnitude of the
horizontal wave orbital velocity at the fixed end of the flexible part
of the blade. With the blade normal velocity 𝑤 and the wave orbital
velocity (𝑈 , 𝑊 ), the relative velocity 𝑈𝑅 between the blade and the
flow was obtained using (22). Then 𝑘𝐷𝑓 was calculated using (24) with
the calculated 𝑈𝑅, 𝑙 = 𝑙𝑓 , 𝑁 = 5263 m−2, 𝛼𝜖 = 0.630, and 𝐶𝑑𝑖 in Table 1
calculated using (14). Finally, the wave decay coefficient 𝑘𝐷 for the
kelp canopy was obtained by 𝑘𝐷 = 𝑘𝐷𝑟 + 𝑘𝐷𝑓 .

Similarly, the computation for 𝐹𝑥,𝑟𝑚𝑠 was also split into two pro-
cesses, i.e., the drag force for the rigid part and the horizontal force for
the flexible part. With the directional angle 𝜙 obtained from solving
the governing equations (2) to (5) for blade motion, the shear force
at the fixed end of the flexible part of the blade 𝑄(𝑠 = 0) (which is

CoastalEngineering168(2021)10394712L. Zhu et al.

Table 3
Measurements for the 1:10 scale model experiments and projections to the full scale prototype. In this table, 𝑑1 is the vertical location of the longlines from the still water level,
ℎ is the water depth, 𝑇𝑤 is the wave period, 𝐻𝐼0 is the incident wave height, 𝑘𝐷 is the wave decay coefficient, 𝛼𝐹 is the force ratio, 𝛼𝜖 is the sheltering factor, 𝐶𝐷𝐵 is the bulk
drag coefficient, 𝑙𝑓 ,𝑒 is the effective blade length for the flexible part of the blade (𝑙𝑓 ), 𝐻𝑇 𝑅 is the wave height transmission ratio, and 𝐸𝐷𝑅 is the wave energy dissipation
ratio.

Case

Experiments (1:10)

Projections to full scale

𝛼𝐹

𝛼𝜖

𝐶𝐷𝐵

𝑙𝑓 ,𝑒∕𝑙𝑓

𝐻𝑇 𝑅

𝐸𝐷𝑅

#

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

𝑑1
[cm]

ℎ
[cm]

11
6
11
6
11
11
16
11
16
11
11
6
16
11

40
30
40
30
40
40
40
40
40
40
40
30
40
40

𝑇𝑤
[s]

1.4
2.0
1.4
1.4
1.0
2.0
2.0
2.0
1.4
1.4
1.0
0.8
0.8
0.8

𝐻𝐼0
[cm]

𝑘𝐷
[m−2]

𝑑1
[m]

ℎ
[m]

1.8
2.9
2.4
2.9
3.1
3.5
3.8
3.7
3.2
3.2
3.6
3.2
3.2
3.2

1.22
0.85
0.85
1.00
1.18
0.52
0.38
0.37
0.62
0.71
1.04
1.87
0.46
0.96

1.1
0.6
1.1
0.6
1.1
1.1
1.6
1.1
1.6
1.1
1.1
0.6
1.6
1.1

4
3
4
3
4
4
4
4
4
4
4
3
4
4

𝑇𝑤
[s]

4.5
6.3
4.5
4.5
3.2
6.3
6.3
6.3
4.5
4.5
3.2
2.6
2.6
2.6

𝐻𝐼0
[m]

0.18
0.29
0.24
0.29
0.31
0.35
0.38
0.37
0.32
0.32
0.36
0.32
0.32
0.32

𝑘𝐷
[m−2]

0.0122
0.0085
0.0085
0.0100
0.0118
0.0052
0.0038
0.0037
0.0062
0.0071
0.0104
0.0187
0.0046
0.0096

0.506
0.966
0.511
0.845
0.575
0.675
1.031
0.512
0.823
0.713
0.986
1.536
0.633
0.632

0.360
0.950
0.365
0.776
0.436
0.555
1.047
0.367
0.747
0.602
0.979
1.904
0.504
0.502

0.55
0.20
0.37
0.22
0.57
0.22
0.17
0.15
0.33
0.31
0.50
0.41
0.55
0.53

0.085
0.046
0.063
0.042
0.072
0.053
0.042
0.036
0.062
0.057
0.066
0.043
0.050
0.051

0.92
0.91
0.93
0.90
0.88
0.94
0.95
0.95
0.93
0.92
0.87
0.81
0.95
0.89

15.0%
16.3%
14.0%
18.6%
22.9%
12.5%
10.1%
9.6%
13.8%
15.4%
23.5%
33.7%
10.4%
19.9%

also the total horizontal force) was calculated using (18). Considering
sheltering effects, the total horizontal force on one row of 30 aggregates
of 10 sheltered blades was

𝐹𝑥,𝑟𝑚𝑠 =

√

1
𝑇𝑤

∫

0

𝑇𝑤

[ 1
2

𝑛𝐶𝑑𝑖𝜌𝑏𝑙𝑟|𝑈 |𝑈 + 𝛼𝐹 𝛽𝑛𝑛𝑄(𝑠 = 0)

]2

𝑑𝑡

(38)

with 𝑛 = 30, 𝛽𝑛 = 10, and 𝛼𝐹 = 0.724.

The numerically calculated 𝐹𝑥,𝑟𝑚𝑠 for a row of blades and 𝑘𝐷 for the
canopy are compared with the measurements on Fig. 9. The calculated
𝐹𝑥,𝑟𝑚𝑠 and 𝑘𝐷 have shown a good agreement with the measured data
with normalized root-mean square-errors (NRMSE) of 0.40 (Fig. 9a)
and 0.23 (Fig. 9b), respectively. The numerical model overestimated
𝐹𝑥,𝑟𝑚𝑠 by 1% while underestimated 𝑘𝐷 by 10% (calculated using the
slope of the linear fitting line on Fig. 9), indicating that the constant
hydrodynamic coefficients, mean 𝛼𝐹 , and mean 𝛼𝜖 are appropriate to
predict the total horizontal force and wave attenuation in this study.

The designed model kelp canopy can reduce up to 33.7% of the
wave energy when the canopy occupied a larger portion of the water
column (𝑙∕ℎ = 0.34), was located at higher position (𝑑1∕ℎ = 0.20),
covered more wavelengths (𝐿𝑣∕𝜆 = 3.7) and featured larger amplitude
waves (𝐻𝐼0∕ℎ = 0.11) as shown in Table 3.

The measured wave energy dissipation ratio (𝐸𝐷𝑅) for the sus-
pended model kelp canopy in different wave conditions and with
different canopy vertical positions are shown on Fig. 10 as a function
of the dimensionless parameters, 𝜆∕ℎ, 𝐻𝐼0∕ℎ, 𝑙∕ℎ, and 𝑑1∕ℎ. The nu-
merically calculated 𝐸𝐷𝑅 using (29) is also shown on Fig. 10 to help
analyze the trend of 𝐸𝐷𝑅. It is noted that 𝐸𝐷𝑅 first increases with 𝜆∕ℎ
and then decreases with 𝜆∕ℎ (Fig. 10a) showing a different behavior
from submerged canopies, of which the wave attenuation capacity in-
creases with wavelength (e.g., Fig. 6c in Luhar et al., 2017). The 𝐸𝐷𝑅 is
not sensitive to 𝐻𝐼0∕ℎ. For example on Fig. 10b, 𝐸𝐷𝑅 increases a little
by 3% from 0.150 to 0.154 when 𝐻𝐼0∕ℎ increases dramatically by 77%
from 0.046 to 0.081. The 𝐸𝐷𝑅 increases with 𝑙𝑓 ∕ℎ (Fig. 10c). As the
water depth decreases, the canopy occupies more of the water column
so that 𝐸𝐷𝑅 increases. The results also demonstrate that moving the
canopy upward (reducing 𝑑1∕ℎ) can improve the wave attenuation
(Fig. 10d) as expected.

4.4. Bulk drag coefficient and effective blade length

For convenience in implementing the wave attenuation model into
large scale models and to improve computational efficiency, empirical
formulas for the bulk drag coefficient and the effective blade length of
the suspended canopy for wave attenuation were developed based on
the datasets. For the blade with rigid part (𝑙𝑟) and flexible part (𝑙𝑓 ), the

wave decay coefficient 𝑘𝐷 can be split into two parts as 𝑘𝐷 = 𝑘𝐷𝑟 + 𝑘𝐷𝑓
with 𝑘𝐷𝑟 for the rigid part and 𝑘𝐷𝑓 for the flexible part of the blade.
The 𝑘𝐷𝑟 for the rigid part is calculated using (25) with 𝑙 = 𝑙𝑟 and 𝐶𝑑𝑖
calculated using (14). The measured 𝑘𝐷𝑓 is obtained by subtracting 𝑘𝐷𝑟
from the measured 𝑘𝐷. With measured 𝑘𝐷𝑓 , the bulk drag coefficient
(𝐶𝐷𝐵,𝑓 ) for the flexible part of the blade is solved from (26), and the
effective blade length (𝑙𝑓 ,𝑒) is solved from (27) with 𝐶𝑑𝑖 calculated using
(14). The calculated 𝐶𝑑𝑖 are shown in Table 1.

For unsteady flow, 𝐶𝐷𝐵,𝑓 is better fitted as a function of 𝐾𝐶 than
𝑅𝑒. The fitted relation between 𝐶𝐷𝐵,𝑓 and 𝐾𝐶 for the suspended model
kelp canopy is

𝐶𝐷𝐵,𝑓 = (3.6 ± 0.7)𝐾𝐶 −1.02±0.10,

(39)

with 𝑅2 = 0.92 (Fig. 11a). With the bulk drag coefficient 𝐶𝐷𝐵,𝑓 ,
the wave decay coefficient 𝑘𝐷𝑓 for the flexible part can therefore be
calculated directly using (26) without calculating the blade motion.

Based on the scaling analysis with linear blade motion, Luhar and
Nepf (2016) argued that 𝑙𝑓 ,𝑒 is proportional to (𝐶𝑎𝐿)−0.25. Follow-
ing Luhar and Nepf (2016), the best fit for 𝑙𝑓 ,𝑒 is

𝑙𝑓 ,𝑒
𝑙𝑓

= (1.11 ± 0.08)(𝐶𝑎𝐿)−0.25,

(40)

with 𝑅2 = 0.06 (Fig. 11b). With the effective blade length 𝑙𝑓 ,𝑒, the wave
decay coefficient 𝑘𝐷𝑓 for the flexible part can therefore be calculated
directly using (27) with 𝐶𝑑𝑖
in (14) without calculating the blade
motion.

To evaluate the performance of the fitted formulas for 𝐶𝐷𝐵,𝑓 and
𝑙𝑓 ,𝑒, the calculated 𝑘𝐷𝑓 using (26) with fitted 𝐶𝐷𝐵,𝑓 in (39) and using
(27) with fitted 𝑙𝑓 ,𝑒 in (40) are compared with the measured 𝑘𝐷𝑓 as
well as the numerically calculated 𝑘𝐷𝑓 using (24) as shown on Fig. 11c.
The NRMSE for the calculated 𝑘𝐷𝑓 with fitted 𝐶𝐷𝐵,𝑓 is 0.08, which
is smaller than the calculations with fitted 𝑙𝑓 ,𝑒 (NRMSE = 0.13). The
improved performance of the bulk drag coefficient method is due to the
better fit for 𝐶𝐷𝐵,𝑓 as a function of 𝐾𝐶 with a larger 𝑅2 = 0.92 than the
effective blade length method (𝑅2 = 0.06), which fits 𝑙𝑓 ,𝑒 as a function
of 𝐶𝑎𝐿. Both the bulk drag coefficient and the effective blade length
methods have shown a smaller NRMSE than that of the numerical
calculations without fitting (NRMSE = 0.27). This indicates that the
simplified methods using the bulk drag coefficient and effective blade
length that are fitted with experiments are successful for considering
the influences of blade motion on wave attenuation. In fact, they
performed even better than the numerical methods (24) that resolves
the blade motion. This is because the values of 𝐶𝐷𝐵,𝑓 and 𝑙𝑓 ,𝑒 are
derived from empirical fits to the data that they are used to predict. Ad-
ditionally, the fitted values incorporated all the uncertainties, such as

CoastalEngineering168(2021)10394713L. Zhu et al.

Fig. 9. Comparisons for the measured and calculated (a) horizontal force (𝐹𝑥,𝑟𝑚𝑠) for a row of 30 aggregates of 10 sheltered blades and (b) wave decay coefficient (𝑘𝐷). The
vertical error bars indicate two standard deviations (2𝜎) for the measurements while the horizontal bars indicate the computation uncertainty induced by using the minimum and
maximum force ratio 𝛼𝐹 and sheltering factor 𝛼𝜖 . The normalized root mean square error (NRMSE) for the calculated values is shown in the legend. The black lines are the linear
fit for the calculated 𝐹𝑥,𝑟𝑚𝑠 and 𝑘𝐷 with expressions and 𝑅2 nearby.

Fig. 10. Measured and calculated wave energy dissipation ratio (𝐸𝐷𝑅) for the suspended model kelp canopy as a function of (a) 𝜆∕ℎ, (b) 𝐻𝐼0∕ℎ, (c) 𝑙∕ℎ, and (d) 𝑑1∕ℎ. The water
depth is ℎ, the wavelength is 𝜆, the incident wave height is 𝐻𝐼0, the blade length is 𝑙, and the vertical distance from the longline to the still water line is 𝑑1. The measured
𝐸𝐷𝑅 is denoted by black crosses with the corresponding case numbers nearby while the calculated 𝐸𝐷𝑅 using the averaged sheltering factor is denoted by red lines. In (a), the
upper red line indicates the calculations for Case 8 and 11 with 𝐻𝐼0∕ℎ = 0.09 while the lower red line indicates the calculations for Case 10 and 14 with 𝐻𝐼0∕ℎ = 0.08. They are
presented together in (a) since their 𝐻𝐼0∕ℎ are close and have no significant influences on 𝐸𝐷𝑅.

the velocity reduction in the canopy (Lowe, 2005), that the numerical
methods did not consider.

5. Discussion

The blade roll-over phenomenon is expected to influence wave
attenuation, therefore, understanding the wave induced dynamics is
important to assess if this is anticipated in the field. Additionally, it is
critical to analyze if simplified methods (i.e. the bulk drag coefficient

and effective blade length) can be used to enhance computational
efficiency in wave attenuation simulations. Before kelp farms can be
implemented as nature-based coastal protection measures, it is essential
to identify the key parameters affecting wave attention.

5.1. Roll-over of suspended flexible blades

The suspended blade fixed at the upper end exhibited different
dynamics compared to the submerged blade fixed at the sea floor. The

CoastalEngineering168(2021)10394714L. Zhu et al.

Fig. 11. (a) Measured bulk drag coefficients (𝐶𝐷𝐵,𝑓 ) for the flexible part of the blade as a function of Keulegan–Carpenter number (𝐾𝐶). (b) Measured effective blade length (𝑙𝑓 ,𝑒)
for the flexible part (𝑙𝑓 ) of the blade as a function of the product of Cauchy number (𝐶𝑎) and length ratio (𝐿). In (a) and (b), the black line indicates the fitting formula with
expression and 𝑅2 nearby. (c) Comparisons between the measured wave decay coefficient 𝑘𝐷𝑓 for the flexible part of the blade and the calculations using (24) with 𝐶𝑑𝑖 calculated
from (14) (denoted by magenta open circles), using (26) with fitted 𝐶𝐷𝐵,𝑓 (denoted by red ×), and using (27) with fitted 𝑙𝑓 ,𝑒 (denoted by blue +). The normalized root mean
square error (NRMSE) is shown in the legend.

differences are represented by the opposite asymmetric motion and roll-
over property of the suspended blade. The opposite asymmetric motion
of suspended blades is mainly induced by the asymmetric action of the
vertical wave orbital velocity. In waves propagating to the right as an
example, the wave orbital motion provides a clockwise momentum that
drives bottom-fixed blade to incline to the right while drives top-fixed
blades to incline to the left. Similarly, the rolling over motion of the
suspended blades also results from the interaction of the blade with
wave orbital motion. The blade motion is driven by the wave orbital
motion. For a long flexible blade in transitional and deep water waves,
the blade motion is asymmetric (Zhu et al., 2020b). When the wave
height increases to a critical value, the asymmetry becomes so large
that the blade is almost horizontal, providing conditions for the onset
of rolling over.

For aquaculture farms, the blades are closely seeded as an aggre-
gate. The sheltering effects and blade–blade interaction may inhibit
the rolling over cycle by cycle. In the experiments, only waves were
considered. In the field, the strong background currents can streamline
the blade and therefore inhibit rolling over. However, the rolling over
can still happen for sparsely seeded kelp in large wave conditions.
The blade roll-over induces a large curvature resulting in a large inner
stress that increases the risk of blade breakage. Long-term roll-over is
expected to also impact kelp growth and morphology. The blade roll-
over reduces canopy height and increase blade–blade sheltering and
interaction, which may decrease wave attenuation. However, the roll-
over effects may reduce the blade motion amplitude and move the
lower part of the blade upward that may enhance wave attenuation.
The roll-over effects are still unclear that warrant further investigation
in the future.

5.2. Methods to predict wave attenuation

The aquaculture kelp blades are seeded closely together on the long-
line for economic benefits. High plant density (e.g., 745/m in Peteiro
and Freire, 2013) is also beneficial for wave attenuation. However, the
sheltering effects from neighboring blades and the blade–blade inter-
action present uncertainties for wave attenuation prediction. A simple
sheltering factor defined in (33) is acceptable since the numerical
calculations with the sheltering factor present a small NRMSE of 0.23

(Fig. 9b). As the plant density and blade configurations influence the
sheltering effects, a more sophisticated sheltering factor as a function
of plant density and blade properties as well as wave conditions is
warranted.

Compared to the numerical wave decay coefficient calculated with
(24), the bulk drag coefficient and effective blade length methods have
improved the calculations by reducing the NRMSE by 70% and 52%,
respectively. The improvements are attributed to the fits for 𝐶𝐷𝐵,𝑓 and
𝑙𝑓 ,𝑒 based on the data that are being predicted. The bulk drag coeffi-
cient and effective blade length methods are simple and convenient to
implement into large-scale models. Although the bulk drag coefficient
and effective blade length methods could provide favorable results with
fitted 𝐶𝐷𝐵 and 𝑙𝑒, physical experiments are required to calibrate 𝐶𝐷𝐵
and 𝑙𝑒. Thus, the numerical solution (24) could be an alternative when
reliable 𝐶𝐷𝐵 and 𝑙𝑒 are not available.

5.3. Suspended kelp aquaculture farms as nature-based coastal protection

The model kelp canopy has shown the capacity for wave attenuation
in the laboratory experiments. Though, this anticipated wave attenua-
tion is overestimated because the model blade thickness is 𝑑 = 𝑑max
as constant while the thickness of real kelp reduces towards the blade
edge (Fig. 5c). Based on the thickness distribution in (36), the second
momentum of the cross section of S. latissima is

𝐼 = ∫

1
2

𝑑max

− 1
2

𝑑max

2 ∣ 𝑠𝑏 ∣ 𝑦2𝑑𝑦 ≈

0.2𝑏 𝑑3
12

max

,

(41)

indicating that the flexural rigidity of the real S. latissima blade is
only 20% of the same wide plate but with the maximum thickness. To
reduce the overestimation and obtain more reliable results for the wave
attenuation in the field, an effective blade width 𝑏𝑒 = 0.2𝑏 is used in
the following discussion. By removing the overestimation due to using
maximum thickness, the wave energy dissipation ratio (EDR) drops
from 10% to 1.5% (Fig. 12a) for Case 6 in Table 3. In addition, the
bending elastic modulus (𝐸) of the full scale model blade is designed
as 21.0 MPa, which is near the largest measured 𝐸. The measured
𝐸 ranges from 2.7 ± 1.4 to 22 ± 6 MPa (Table 2) and varies along
the blade length (Fig. 2a). For the given blade thickness of 0.79 mm,
the expected bending elastic modulus is 𝐸 = 5.6 MPa based on (37).

CoastalEngineering168(2021)10394715L. Zhu et al.

Fig. 12. (a) Effects of the bending elastic modulus (𝐸) and the length (𝑙) of the blade as well as number of plants per meter on the wave energy dissipation ratio (EDR) of
suspended kelp aquaculture farms. Wave attenuation as a function of the number of kelp longlines with (b) 100 plants/m and (c) 400 plants/m with 𝑙 = 0.1 (square), 1 (triangle),
2 (circle) m and 𝐸 = 1 (blue), 5 (cyan), 21 (orange) MPa. The water depth is 4 m, wave height is 0.35 m, and wave period is 6.3 s. The kelp longline is 1.1 m beneath the
still water line. The blade thickness is 𝑑 and the maximum thickness is 𝑑max. (For interpretation of the references to color in this figure legend, the reader is referred to the web
version of this article.)

However, the numerical results show that 𝐸 has a small influence on
wave attenuation (Fig. 12). For example in Case 6, the EDR reduces
from 1.5% to 1.4% by 6.7% when 𝐸 decreases from 21 MPa to 5 MPa
by 76% (Fig. 12a).

The plant density is 100 plants/m for the model kelp longline, which
is smaller than the measured value of 405 plants/m. In fact, the plant
density can be as large as 745 plants/m (Peteiro and Freire, 2013),
which can significantly enhance the wave attenuation. Assuming the
measured sheltering factor 𝛼𝜖 is applicable for larger plant density, the
simulated EDR for Case 6 increases to 5.5% with 400 plants/m and
to 9.4% with 700 plants/m with effective blade width 𝑏𝑒 = 0.2𝑏 and
𝐸 = 5 MPa (Fig. 12a). As the growth of kelp, the blade length increases
yielding larger wave attenuation. For instance with 400 plants/m and
𝐸 = 5 MPa, the EDR increases from 5.5% to 15.7% when the blade
length grows from 1 m to 2 m. The increase of EDR is even more
significant (25.2%) for a greater plant density of 700 plants/m.

The wave attenuation of suspended aquaculture kelp is dependent
on the growth of kelp including the blade size and plant density,
where a denser longline with longer kelp yields more wave attenuation.
Another important parameter determining the wave attenuation of a
suspended kelp farm is the number of longlines. For the suspended kelp
farm with 200 longlines with 100 plants/m in the same conditions with
Case 6, the EDR are 13.0% for 1 m-long blades with 𝐸 = 5 MPa and
33.2% for 2 m-long blades with 𝐸 = 5 MPa (Fig. 12b). If the plant
density increases to 400 plants/m as measured in this study, the EDR
increase to 40.0% and 72.1% (Fig. 12c), respectively. The vertical posi-
tion of kelp in the water column also influences the wave attenuation.
Generally, the higher location in the water column results in larger

wave attenuation. However, the vertical position also influences the
growth of kelp due to the depth distribution of light, temperature, and
nutrient (Graham et al., 2007; Bekkby et al., 2019), which should be
considered in the application of suspended kelp aquaculture farms for
wave attenuation.

𝑚 𝐻0 ∝ 𝐻 −1.02

The wave attenuation capacity of suspended kelp aquaculture farms
is also dependent on the wave conditions, especially the water depth
and wavelength. Although (29) shows that 𝐸𝐷𝑅 is dependent on 𝑘𝐷𝐻0,
𝐸𝐷𝑅 is not certainly significantly influenced by 𝐻0. Noted that 𝑘𝐷𝐻0 ∝
𝐶𝐷𝐵𝐻0 ∝ 𝐾𝐶 −1.02𝐻0 ∝ 𝑈 −1.02
≈ 1 based on the
bulk drag coefficient method with 𝑘𝐷 in (26), 𝐶𝐷𝐵 in (39), 𝐾𝐶 in (9),
and 𝑈 in (19). Therefore, the wave attenuation is not sensitive to the
incident wave height, which is also demonstrated in the experiments
as shown on Fig. 10b. However, the wave attenuation can be improved
significantly by locating the suspended kelp farms in shallower water
such that the kelp blade occupies a larger fraction of the water column,
especially for shallow water waves. In shallow water waves (𝑘ℎ < 0.1𝜋),
the wave decay coefficient 𝑘𝐷 in (26) is reduced to

𝐻0 = 𝐻 −0.02

0

0

𝑘𝐷 =

𝛼𝜖𝐶𝐷𝐵𝑏𝑁𝑙
3𝜋ℎ2

,

(42)

indicating that 𝑘𝐷 increases quadratically with decreasing water depth
in shallow water waves. The water depth is also an important factor
for kelp growth. Furthermore, the wave attenuation of suspended kelp
farms increases with wavelength and then decreases with wavelength,
indicating that the suspended kelp farms do not perform well for very
short waves and very long waves. This is because in very short waves,
the wave kinematic energy concentrates on the water particles above

CoastalEngineering168(2021)10394716L. Zhu et al.

the kelp canopy and in very long waves, the canopy length covers few
wavelength.

Overall, the wave attenuation effectiveness of suspended kelp farms
can be improved by installing the kelp farms in shallower water,
expanding the farm size by adding more longlines, and locating the
kelp in a higher position of the water column. Choosing the kelp species
with more rigid, wider, and longer blades/biomass and growing the
kelp more densely can further improve the wave attenuation.

5.4. Limitations

This preliminary study has proposed simple methods to quantify the
wave attenuation of suspended kelp aquaculture structures. However,
there are still some limitations of these methods due to the complexity
of the kelp morphology and flow environment in the field. The kelp
blade morphology is more flat in exposed sites and more ruffled in
sheltered sites (Koehl et al., 2008). The ruffle and thickness variance
of the blade may impact the hydrodynamic coefficients. Like kelp
stipe and holdfast, these small morphological features cannot be fully
considered in the downscaled model and the effects of these small
morphological features on wave attenuation are unclear. In the field,
there would be a background current in addition to waves that may
have significant influences on the wave attenuation, which is not con-
sidered in the current study. When the current exceeds a critical value,
the kelp becomes streamlined so that the drag force decreases and
the friction dominates (Fredriksson et al., 2020), after which a smaller
wave attenuation is anticipated. At this point, the energy conservation
equation (21) should be modified by using friction rather than the nor-
mal drag. Gaylord et al. (2003) observed that the alongshore currents
decrease the wave attenuation of Nereocystis luetkeana. However, the
reconfiguration of kelp in waves and currents can enhance the survival
rate and reduce the effects of wave attenuation service on the biomass
productivity (Gerard, 1987). Lastly, the kelp longline mooring system
and the motion of the longline were not considered due to the small
width of the flume, which may lead to overestimation of the wave
attenuation.

energy dissipation ratio (𝐸𝐷𝑅) of suspended kelp farms decreases with
increased water depth, (ii) 𝐸𝐷𝑅 is not sensitive to wave height, (iii)
𝐸𝐷𝑅 first increases and then decreases with wavelength, and (iv)
𝐸𝐷𝑅 increases with blade size, kelp vertical position, plant density,
and the number of longlines. Therefore, the technique to improve the
wave attenuation capacity of suspended kelp aquaculture farms for
nature-based coastal defense is to install the kelp farms in shallower
water, expand the farm size by adding more longlines, locate the
kelp in a higher position of the water column, grow the kelp more
densely, and choose the kelp species with more rigid, wider, and longer
blades/biomass.

The results of this study also produced empirical formulas for the
bulk drag coefficient and effective blade length of suspended kelp
canopy for wave attenuation applications. These expressions could be
implemented in large-scale wave models to examine the role of kelp
farms as nature-based coastal protection measures on coastal morphol-
ogy, inner shelf circulation and material transport. Though this study
focused on waves without currents, a natural extension of this work
would be to include background currents, which likely streamline the
kelp blades and influence the wave attenuation performance.

CRediT authorship contribution statement

Longhuan Zhu: Conceptualization, Methodology, Software, Valida-
tion, Formal analysis, Investigation, Resources, Data curation, Writing
– original draft, Writing - review & editing, Visualization. Jiarui Lei:
Methodology, Writing - review & editing. Kimberly Huguenard: Su-
pervision, Resources, Writing - review and editing. David W. Fredriks-
son: Resources, Writing - review & editing.

Declaration of competing interest

The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.

6. Conclusions

Acknowledgments

Wave attenuation by suspended kelp canopies was investigated
using a set of physical model experiments having dynamic similarity
with cultivated S. latissima from an aquaculture site in Saco Bay, Maine
of the USA. The yield of the kelp farm was 6.86 kg/m with 405
plants/m. The cultivated S. latissima had a length of 3–177.7 cm, width
of 1–18.5 cm, thickness of 0.44–1.08 mm, mass density of 1.05 g/cm3,
and elastic modulus of 2.7–22 MPa. The model kelp farm was configured
to have 20 grow lines of 1-m-long blades and 100 blades/m with an
orientation normal to the direction of waves. The experimental results
demonstrated that in this configuration, a suspended kelp farm could
attenuate wave energy by 16.3%, 18.6%, 23.5%, and 33.7% for 6.3 s,
4.5 s, 3.2 s, and 2.6 s waves, respectively, in water depth of 3–4 m.
The physical model results also showed that the motion of suspended
blades was asymmetric, similar to bottom-fixed blades, but yielded
a blade inclination that opposed the direction of wave propagation.
In waves propagating to the right, the clockwise motion of water
particles induces a clockwise momentum that drives the blades to bend
clockwise around the fixed end. As suspended blades are fixed at the top
end, the clockwise bending of suspended blades results in an inclination
to the left. In contrast, the bottom-fixed blade inclines to the right.
In large waves, this strong asymmetric motion promoted a roll over
motion of the suspended blades.

To predict wave attenuation under a wider range of conditions
and to identify the key parameters affecting wave attenuation, a nu-
merical model was developed that could resolve blade motion. The
numerical model showed good agreement with the experiments with
a slight underestimation of 10%. The results indicate that (i) the wave

This work was completed as part of the PhD research of Longhuan
Zhu who was supported by National Science Foundation, USA award
#IIA-1355457 to Maine EPSCoR at the University of Maine. The authors
gratefully acknowledge the assistance of the Advanced Computing
Group of the University of Maine System in producing the numerical
data. Longhuan Zhu would like to sincerely thank Heidi Nepf for
supporting the experiments and discussions at MIT, Neil Fisher and
Allen Treadwell for assisting designing and manufacturing the kelp
supporting frames, Adam St. Gelais and Kathryn Johndrow for assisting
collecting S. latissima samples from the kelp longline of the University
of New England, Kathryn Johndrow for measuring the blade length
and width of kelp samples. Longhuan Zhu would also like to thank Yu-
Ying Chen for assisting to measure the morphological and mechanical
properties of S. latissima and his colleagues in the coastal research
group of the University of Maine and friends for help in preparing
model kelp longlines. All data generated or analyzed during this study
are included in this manuscript. The raw data are available from the
authors upon reasonable request. Finally, the authors would like to
thank the anonymous reviewer for constructive comments that really
helped to improve this manuscript greatly.

Appendix A. Wave height fitting along a canopy with reflective
waves

Assuming the incident wave height (𝐻𝐼0) and reflective wave height
) decay at the same decay coefficient 𝑘𝐷 following (23), the

(𝐻𝑅𝐿𝑣

CoastalEngineering168(2021)10394717L. Zhu et al.

𝜂 = 𝜂𝐼 + 𝜂𝑅

=

+

=

1
2

1
2

1
2

[

[

𝐻𝐼0
1 + 𝑘𝐷𝐻𝐼0𝑥

𝐻𝐼0
1 + 𝑘𝐷𝐻𝐼0𝑥

cos(𝑘𝑥 + 𝜖𝐼 ) +

sin(𝑘𝑥 + 𝜖𝐼 ) −

𝐻𝑅𝐿𝑣
1 + 𝑘𝐷𝐻𝑅𝐿𝑣
𝐻𝑅𝐿𝑣
1 + 𝑘𝐷𝐻𝑅𝐿𝑣

(𝐿𝑣 − 𝑥)

(𝐿𝑣 − 𝑥)

]

cos(𝑘𝑥 + 𝜖𝑅)

cos(𝜔𝑡)

]

sin(𝑘𝑥 + 𝜖𝑅)

sin(𝜔𝑡)

√
√
√
√
√

(

𝐻𝐼0
1 + 𝑘𝐷𝐻𝐼0𝑥

)2

[

+

𝐻𝑅𝐿𝑣
1 + 𝑘𝐷𝐻𝑅𝐿𝑣

(𝐿𝑣 − 𝑥)

]2

+ 2

𝐻𝐼0
1 + 𝑘𝐷𝐻𝐼0𝑥

𝐻𝑅𝐿𝑣
1 + 𝑘𝐷𝐻𝑅𝐿𝑣

(𝐿𝑣 − 𝑥)

cos(2𝑘𝑥 + 𝜖)

⋅ cos(𝜔𝑡 + 𝜓),

Box II.

√
√
√
√
√

(

𝐻(𝑥) =

𝐻𝐼0
1 + 𝑘𝐷𝐻𝐼0𝑥

)2

[

+

𝐻𝑅𝐿𝑣
1 + 𝑘𝐷𝐻𝑅𝐿𝑣

(𝐿𝑣 − 𝑥)

]2

+ 2

𝐻𝐼0
1 + 𝑘𝐷𝐻𝐼0𝑥

𝐻𝑅𝐿𝑣
1 + 𝑘𝐷𝐻𝑅𝐿𝑣

(𝐿𝑣 − 𝑥)

cos(2𝑘𝑥 + 𝜖).

Box III.

(A.3)

(A.4)

incident water elevation (𝜂𝐼 ) and reflective water elevation (𝜂𝑅) can
be expressed as
𝐻𝐼0
2

cos(𝑘𝑥 − 𝜔𝑡 + 𝜖𝐼 )

1
1 + 𝑘𝐷𝐻𝐼0𝑥

𝜂𝐼 =

(A.1)

and

𝜂𝑅 =

𝐻𝑅𝐿𝑣
2

1
1 + 𝑘𝐷𝐻𝑅𝐿𝑣

(𝐿𝑣 − 𝑥)

cos(𝑘𝑥 + 𝜔𝑡 + 𝜖𝑅),

(A.2)

respectively, where 𝜖𝐼 and 𝜖𝑅 are the incident wave phase and reflective
wave phase, respectively. Therefore, the combined water elevation
𝜂 can be expressed as (A.3) in Box II, where 𝜖 = 𝜖𝐼 + 𝜖𝑅, and

𝜓 = −

𝐻𝐼0[1+𝑘𝐷𝐻𝑅𝐿𝑣 (𝐿𝑣−𝑥)] sin(𝑘𝑥+𝜖𝐼 )−𝐻𝑅𝐿𝑣 (1+𝑘𝐷𝐻𝐼0𝑥) sin(𝑘𝑥+𝜖𝑅)
𝐻𝐼0[1+𝑘𝐷𝐻𝑅𝐿𝑣 (𝐿𝑣−𝑥)] cos(𝑘𝑥+𝜖𝐼 )+𝐻𝑅𝐿𝑣 (1+𝑘𝐷𝐻𝐼0𝑥) cos(𝑘𝑥+𝜖𝑅)

. Thus, the

wave height along the canopy can be obtained and given by (A.4) in
Box III.

Appendix B. Supplementary data

Supplementary material related to this article can be found online

at https://doi.org/10.1016/j.coastaleng.2021.103947.

References

Abdelrhman, M., 2007. Modeling coupling between eelgrass zostera marina and water
flow. Mar. Ecol. Prog. Ser. 338, 81–96. http://dx.doi.org/10.3354/meps338081,
URL: http://www.int-res.com/abstracts/meps/v338/p81-96/.

Anderson, M.E., Smith, J., 2014. Wave attenuation by flexible, idealized salt marsh
vegetation. Coast. Eng. 83, 82–92. http://dx.doi.org/10.1016/j.coastaleng.2013.10.
004, URL: https://linkinghub.elsevier.com/retrieve/pii/S0378383913001609.
Asano, T., Deguchi, H., Kobayashi, N., 1992. Interaction between water waves and
vegetation. In: Coastal Engineering Proceedings, Vol. 3. pp. 2710–2723, URL:
https://icce-ojs-tamu.tdl.org/icce/index.php/icce/article/view/4885.

Augustin, L.N.,

Irish, J.L., Lynett, P., 2009. Laboratory and numerical studies of
wave damping by emergent and near-emergent wetland vegetation. Coast. Eng.
56 (3), 332–340. http://dx.doi.org/10.1016/j.coastaleng.2008.09.004, URL: https:
//linkinghub.elsevier.com/retrieve/pii/S037838390800152X.

Augyte, S., Yarish, C., Redmond, S., Kim, J.K., 2017. Cultivation of a morphologically
distinct strain of the sugar kelp, saccharina latissima forma angustissima, from
coastal maine, USA, with implications for ecosystem services. J. Appl. Phycol. 29
(4), 1967–1976. http://dx.doi.org/10.1007/s10811-017-1102-x, URL: http://link.
springer.com/10.1007/s10811-017-1102-x.

Bekkby, T., Smit, C., Gundersen, H., Rinde, E., Steen, H., Tveiten, L., Gitmark, J.K.,
Fredriksen, S., Albretsen, J., Christie, H., 2019. The abundance of kelp is modified
by the combined impact of depth, waves and currents. Front. Mar. Sci. 6 (JUL),

475. http://dx.doi.org/10.3389/fmars.2019.00475, URL: https://www.frontiersin.
org/article/10.3389/fmars.2019.00475/full.

Bradley, K., Houser, C., 2009. Relative velocity of seagrass blades:

Implications
for wave attenuation in low-energy environments. J. Geophys. Res. 114 (F1),
F01004. http://dx.doi.org/10.1029/2007JF000951, URL: http://doi.wiley.com/10.
1029/2007JF000951.

Breton, T.S., Nettleton, J.C., O’Connell, B., Bertocci, M., 2018. Fine-scale population
genetic structure of sugar kelp, saccharina latissima (laminariales, phaeophyceae),
in eastern maine, USA. Phycologia 57 (1), 32–40. http://dx.doi.org/10.2216/17-
72.1, URL: https://www.tandfonline.com/doi/full/10.2216/17-72.1.

Bricknell, I.R., Birkel, S.D., Brawley, S.H., Van Kirk, T., Hamlin, H., Capistrant-Fossa, K.,
Huguenard, K., Van Walsum, G.P., Liu, Z.L., Zhu, L.H., Grebe, G., Taccardi, E.,
Miller, M., Preziosi, B.M., Duffy, K., Byron, C.J., Quigley, C.T., Bowden, T.J.,
Brady, D., Beal, B.F., Sappati, P.K., Johnson, T.R., Moeykens, S., 2020. Resilience
of cold water aquaculture: a review of likely scenarios as climate changes in the
gulf of maine. Rev. Aquac. raq.12483. http://dx.doi.org/10.1111/raq.12483, URL:
https://onlinelibrary.wiley.com/doi/abs/10.1111/raq.12483.

Buck, B.H., Buchholz, C.M., 2005. Response of offshore cultivated laminaria saccharina
to hydrodynamic forcing in the north sea. Aquaculture 250 (3–4), 674–691. http:
//dx.doi.org/10.1016/j.aquaculture.2005.04.062, URL: https://linkinghub.elsevier.
com/retrieve/pii/S0044848605003248.

Campbell,

I., Macleod, A., Sahlmann, C., Neves, L., Funderud, J., Øverland, M.,
Hughes, A.D., Stanley, M., 2019. The environmental risks associated with the
development of seaweed farming in europe - prioritizing key knowledge gaps.
Front. Mar. Sci. 6 (MAR), 107. http://dx.doi.org/10.3389/fmars.2019.00107, URL:
https://www.frontiersin.org/article/10.3389/fmars.2019.00107/full.

Chen, H., Liu, X., Zou, Q., 2019. Wave-driven flow induced by suspended and
submerged canopies. Adv. Water Resour. 123, 160–172. http://dx.doi.org/10.
1016/j.advwatres.2018.11.009, URL: https://linkinghub.elsevier.com/retrieve/pii/
S0309170818302574.

Chen, H., Ni, Y., Li, Y., Liu, F., Ou, S., Su, M., Peng, Y., Hu, Z., Uijttewaal, W.,
Suzuki, T., 2018. Deriving vegetation drag coefficients in combined wave-current
flows by calibration and direct measurement methods. Adv. Water Resour.
122, 217–227. http://dx.doi.org/10.1016/j.advwatres.2018.10.008, URL: https://
linkinghub.elsevier.com/retrieve/pii/S030917081830112X.

Chen, Q., Zhao, H., 2012. Theoretical models for wave energy dissipation caused by
vegetation. J. Eng. Mech. 138 (2), 221–229. http://dx.doi.org/10.1061/(ASCE)EM.
1943-7889.0000318, URL: http://ascelibrary.org/doi/10.1061/%28ASCE%29EM.
1943-7889.0000318.

Chen, H., Zou, Q.-P., 2019. EulerIan–Lagrangian flow-vegetation interaction model
using immersed boundary method and openfoam. Adv. Water Resour. 126, 176–
192. http://dx.doi.org/10.1016/j.advwatres.2019.02.006, URL: https://linkinghub.
elsevier.com/retrieve/pii/S0309170818306523.

Dalrymple, R.A., Kirby, J.T., Hwang, P.A., 1984. Wave diffraction due to areas of
energy dissipation. J. Waterw. Port Coast. Ocean Eng. 110 (1), 67–79. http:
//dx.doi.org/10.1061/(ASCE)0733-950X(1984)110:1(67), URL: http://ascelibrary.
org/doi/10.1061/%28ASCE%290733-950X%281984%29110%3A1%2867%29.
Dean, R.G., Dalrymple, R.A., 1991. Water Wave Mechanics for Engineers and Scientists.
In: Advanced Series on Ocean Engineering, vol. 2, WORLD SCIENTIFIC, Cambridge,
http://dx.doi.org/10.1142/1232.

CoastalEngineering168(2021)10394718L. Zhu et al.

Duarte, C.M., Wu, J., Xiao, X., Bruhn, A., Krause-Jensen, D., 2017. Can seaweed farming
play a role in climate change mitigation and adaptation?. Front. Mar. Sci. 4 (APR),
100. http://dx.doi.org/10.3389/fmars.2017.00100, URL: http://journal.frontiersin.
org/article/10.3389/fmars.2017.00100/full.

Elwany, M.H.S., O’Reilly, W.C., Guza, R.T., Flick, R.E., 1995. Effects of southern
california kelp beds on waves. J. Waterw. Port Coast. Ocean Eng. 121 (2), 143–
150. http://dx.doi.org/10.1061/(ASCE)0733-950X(1995)121:2(143), URL: http://
ascelibrary.org/doi/10.1061/%28ASCE%29WW.1943-5460.0000251.

Fredriksson, D.W., Dewhurst, T., Drach, A., Beaver, W., St. Gelais, A.T., Johndrow, K.,
Costa-Pierce, B.A., 2020. Hydrodynamic characteristics of a full-scale kelp model
for aquaculture applications. Aquac. Eng. 90, 102086. http://dx.doi.org/10.1016/
j.aquaeng.2020.102086.

Fryer, M., Terwagne, D., Reis, P.M., Nepf, H., 2015. Fabrication of flexible blade models
from a silicone-based polymer to test the effect of surface corrugations on drag and
blade motion. Limnol. Oceanogr.: Methods 13 (11), 630–639. http://dx.doi.org/10.
1002/lom3.10053, URL: http://doi.wiley.com/10.1002/lom3.10053.

Gaylord, B.P., Denny, M.W., Koehl, M.A., 2003. Modulation of wave forces on kelp
canopies by alongshore currents. Limnol. Oceanogr. 48 (2), 860–871. http://
dx.doi.org/10.4319/lo.2003.48.2.0860, URL: https://aslopubs.onlinelibrary.wiley.
com/doi/pdf/10.4319/lo.2003.48.2.0860.

Gaylord, B., Rosman, J.H., Reed, D.C., Koseff, J.R., Fram, J., Macintyre, S.,
Arkema, K.K., Mcdonald, C., Brzezinski, M.A., Largier, J.L., Monismith, S.G.,
Raimondi, P.T., Mardian, B., 2007. Spatial patterns of flow and their modification
within and around a giant kelp forest. Limnol. Oceanogr. 52 (5), 1838–1852, URL:
https://aslopubs.onlinelibrary.wiley.com/doi/pdf/10.4319/lo.2007.52.5.1838.
Gerard, V.A., 1987. Hydrodynamic streamlining of laminaria saccharina lamour. in
response to mechanical stress. J. Exp. Mar. Biol. Ecol. 107 (3), 237–244. http://
dx.doi.org/10.1016/0022-0981(87)90040-2, URL: https://linkinghub.elsevier.com/
retrieve/pii/0022098187900402.

Graham, M.H., Kinlan, B.P., Druehl, L.D., Garske, L.E., Banks, S., 2007. Deep-water
kelp refugia as potential hotspots of tropical marine diversity and productivity.
Proc. Natl. Acad. Sci. 104 (42), 16576–16580. http://dx.doi.org/10.1073/pnas.
0704778104, URL: http://www.pnas.org/cgi/doi/10.1073/pnas.0704778104.
Grebe, G.S., Byron, C.J., Brady, D.C., Geisser, A.H., Brennan, K.D., 2021. The nitrogen
bioextraction potential of nearshore saccharina latissima cultivation and harvest
in the western gulf of maine. J. Appl. Phycol. 1–17. http://dx.doi.org/10.1007/
s10811-021-02367-6, URL: http://link.springer.com/10.1007/s10811-021-02367-
6.

Grebe, G.S., Byron, C.J., Gelais, A.S., Kotowicz, D.M., Olson, T.K., 2019. An ecosystem
approach to kelp aquaculture in the americas and europe. Aquac. Rep. 15, 100215.
http://dx.doi.org/10.1016/j.aqrep.2019.100215, URL: https://linkinghub.elsevier.
com/retrieve/pii/S2352513419300134.

Henderson, S.M., 2019. Motion of buoyant, flexible aquatic vegetation under waves:
Simple theoretical models and parameterization of wave dissipation. Coast. Eng.
152, 103497. http://dx.doi.org/10.1016/j.coastaleng.2019.04.009, URL: https://
linkinghub.elsevier.com/retrieve/pii/S0378383918305349.

Hu, Z., Suzuki, T., Zitman, T., Uittewaal, W., Stive, M., 2014. Laboratory study on wave
dissipation by vegetation in combined current–wave flow. Coast. Eng. 88, 131–
142. http://dx.doi.org/10.1016/j.coastaleng.2014.02.009, URL: https://linkinghub.
elsevier.com/retrieve/pii/S0378383914000416.

Huang, I., Rominger, J., Nepf, H., 2011. The motion of kelp blades and the surface
renewal model. Limnol. Oceanogr. 56 (4), 1453–1462. http://dx.doi.org/10.4319/
lo.2011.56.4.1453, URL: http://doi.wiley.com/10.4319/lo.2011.56.4.1453.

Jackson, G.A., 1984.

Internal wave attenuation by coastal kelp stands.

J.
Phys. Oceanogr. 14 (8), 1300–1306. http://dx.doi.org/10.1175/1520-0485(1984)
014<1300:IWABCK>2.0.CO;2, URL: http://journals.ametsoc.org/doi/abs/10.1175/
1520-0485%281984%29014%3C1300%3AIWABCK%3E2.0.CO%3B2.

Jackson, G.A., 1997. Currents in the high drag environment of a coastal kelp
stand off california. Cont. Shelf Res. 17 (15), 1913–1928. http://dx.doi.org/10.
1016/S0278-4343(97)00054-X, URL: https://linkinghub.elsevier.com/retrieve/pii/
S027843439700054X.

Jacobsen, N., McFall, B., van der A, D., 2019. A frequency distributed dissi-
pation model
for canopies. Coast. Eng. 150, 135–146. http://dx.doi.org/10.
1016/j.coastaleng.2019.04.007, URL: https://linkinghub.elsevier.com/retrieve/pii/
S0378383918303892.

Jadhav, R.S., Chen, Q., Smith, J.M., 2013. Spectral distribution of wave energy
dissipation by salt marsh vegetation. Coast. Eng. 77, 99–107. http://dx.doi.org/10.
1016/j.coastaleng.2013.02.013, URL: https://linkinghub.elsevier.com/retrieve/pii/
S0378383913000537.

Keulegan, G.H., Carpenter, L.H., 1958. Forces on cylinders and plates in an oscillating
fluid. J. Res. Natl. Bur. Stand. 60 (5), 423–440, URL: https://nvlpubs.nist.gov/
nistpubs/jres/60/jresv60n5p423_A1b.pdf.

Kobayashi, N., Raichle, A.W., Asano, T., 1993. Wave attenuation by vegetation. J.
Waterw. Port Coast. Ocean Eng. 119 (1), 30–48. http://dx.doi.org/10.1061/(ASCE)
0733-950X(1993)119:1(30), URL: http://ascelibrary.org/doi/10.1061/%28ASCE%
290733-950X%281993%29119%3A1%2830%29.

Koehl, M.A.R., Silk, W.K., Liang, H., Mahadevan, L., 2008. How kelp produce blade
shapes suited to different
Integr. Comp. Biol.
48 (6), 834–851. http://dx.doi.org/10.1093/icb/icn069, URL:https://academic.oup.
com/icb/article-abstract/48/6/834/837623.

flow regimes: A new wrinkle.

Lei, J., Nepf, H., 2019a. Blade dynamics in combined waves and current. J. Fluids
Struct. 87, 137–149. http://dx.doi.org/10.1016/j.jfluidstructs.2019.03.020, URL:
https://linkinghub.elsevier.com/retrieve/pii/S0889974618306996.

Lei, J., Nepf, H., 2019b. Wave damping by flexible vegetation: Connecting individual
blade dynamics to the meadow scale. Coast. Eng. 147, 138–148. http://dx.doi.org/
10.1016/j.coastaleng.2019.01.008, URL: https://linkinghub.elsevier.com/retrieve/
pii/S0378383918300905.

Liang, B., Chaudet, P., Boisse, P., 2017. Curvature determination in the bending test
of continuous fibre reinforcements. Strain 53 (1), 1–12. http://dx.doi.org/10.1111/
str.12213, arXiv:NIHMS150003.

Losada, I.J., Maza, M., Lara, J.L., 2016. A new formulation for vegetation-induced
damping under combined waves and currents. Coast. Eng. 107, 1–13. http://dx.
doi.org/10.1016/j.coastaleng.2015.09.011, URL: https://linkinghub.elsevier.com/
retrieve/pii/S0378383915001684.

Lowe, R.J., 2005. Oscillatory flow through submerged canopies: 1. Velocity structure. J.
Geophys. Res. 110 (C10), C10016. http://dx.doi.org/10.1029/2004JC002788, URL:
http://doi.wiley.com/10.1029/2004JC002788.

Luhar, M., 2012. Analytical and Experimental Studies of Plant-Flow Interaction at
Multiple Scales (Thesis). Massachusetts Institute of Technology, URL: http://dspace.
mit.edu/handle/1721.1/78142.

Luhar, M., Infantes, E., Nepf, H., 2017. Seagrass blade motion under waves and its
impact on wave decay. J. Geophys. Res. Oceans 122 (5), 3736–3752. http://dx.doi.
org/10.1002/2017JC012731, URL: http://doi.wiley.com/10.1002/2017JC012731.
Luhar, M., Nepf, H., 2016. Wave-induced dynamics of flexible blades. J. Fluids Struct.
61, 20–41. http://dx.doi.org/10.1016/j.jfluidstructs.2015.11.007, URL: arXiv:1510.
01237.

Madsen, O.S., Poon, Y.-K., Graber, H.C., 1988. Spectral wave Attenuation by bot-
tom friction:
theory. Coast. Eng. Proc. 1 (21), 492–504. http://dx.doi.org/
10.1061/9780872626874.035, URL: https://journals.tdl.org/icce/index.php/icce/
article/view/4241.

Mao, X., Augyte, S., Huang, M., Hare, M.P., Bailey, D., Umanzor, S., Marty-Rivera, M.,
Robbins, K.R., Yarish, C., Lindell, S., Jannink, J.-L., 2020. Population genetics of
sugar kelp throughout the northeastern united states using genome-wide markers.
Front. Mar. Sci. 7, 694. http://dx.doi.org/10.3389/fmars.2020.00694, URL: https:
//www.frontiersin.org/article/10.3389/fmars.2020.00694/full.

Mendez, F.J., Losada, I.J., 2004. An empirical model to estimate the propagation
of random breaking and nonbreaking waves over vegetation fields. Coast. Eng.
51 (2), 103–118. http://dx.doi.org/10.1016/j.coastaleng.2003.11.003, URL: https:
//linkinghub.elsevier.com/retrieve/pii/S0378383903001182.

Méndez, F.J., Losada, I.J., Losada, M.A., 1999. Hydrodynamics induced by wind waves
in a vegetation field. J. Geophys. Res. 104 (C8), 18383–18396. http://dx.doi.org/
10.1029/1999JC900119, URL: http://doi.wiley.com/10.1029/1999JC900119.
Mork, M., 1996. The effect of kelp in wave damping. Sarsia 80 (4), 323–327. http://
dx.doi.org/10.1080/00364827.1996.10413607, URL: http://www.tandfonline.com/
doi/full/10.1080/00364827.1996.10413607.

Morris, R.L., Graham, T.D.J., Kelvin, J., Ghisalberti, M., Swearer, S.E., 2019. Kelp beds
as coastal protection: wave attenuation of ecklonia radiata in a shallow coastal bay.
Ann. Botany 125, 235–246. http://dx.doi.org/10.1093/aob/mcz127, URL: https:
//academic.oup.com/aob/advance-article/doi/10.1093/aob/mcz127/5551380.
Mullarney, J.C., Henderson, S.M., 2010. Wave-forced motion of submerged single-
stem vegetation. J. Geophys. Res. 115 (C12), C12061. http://dx.doi.org/10.1029/
2010JC006448, URL: http://doi.wiley.com/10.1029/2010JC006448.

Ozeren, Y., Wren, D.G., Wu, W., 2014. Experimental investigation of wave attenuation
through model and live vegetation. J. Waterw. Port Coast. Ocean Eng. 140 (5),
04014019. http://dx.doi.org/10.1061/(ASCE)WW.1943-5460.0000251, URL: http:
//ascelibrary.org/doi/10.1061/%28ASCE%29WW.1943-5460.0000251.

Peteiro, C., Freire, Ó., 2013. Biomass yield and morphological features of the seaweed
saccharina latissima cultivated at two different sites in a coastal bay in the atlantic
coast of Spain. J. Appl. Phycol. 25 (1), 205–213. http://dx.doi.org/10.1007/
s10811-012-9854-9, URL: http://link.springer.com/10.1007/s10811-012-9854-9.

Plew, D.R., Stevens, C., Spigel, R., Hartstein, N., 2005. Hydrodynamic implications of
large offshore mussel farms. IEEE J. Ocean. Eng. 30 (1), 95–108. http://dx.doi.org/
10.1109/JOE.2004.841387, URL: http://ieeexplore.ieee.org/document/1435580/.

Riffe, K.C., Henderson, S.M., Mullarney, J.C., 2011. Wave dissipation by flexible vege-
tation. Geophys. Res. Lett. 38 (18), n/a. http://dx.doi.org/10.1029/2011GL048773,
URL: http://doi.wiley.com/10.1029/2011GL048773.

Rosman, J.H., Denny, M.W., Zeller, R.B., Monismith, S.G., Koseff, J.R., 2013. Interaction
Insights from
of waves and currents with kelp forests (macrocystis pyrifera):
a dynamically scaled laboratory model. Limnol. Oceanogr. 58 (3), 790–802.
http://dx.doi.org/10.4319/lo.2013.58.3.0790, URL: http://doi.wiley.com/10.4319/
lo.2013.58.3.0790.

Rosman, J.H., Koseff, J.R., Monismith, S.G., Grover, J., 2007. A field inves-
tigation into the effects of a kelp forest
(macrocystis pyrifera) on coastal
hydrodynamics and transport. J. Geophys. Res. Oceans 112 (2), 1–16. http://
dx.doi.org/10.1029/2005JC003430, URL: https://agupubs.onlinelibrary.wiley.com/
doi/pdf/10.1029/2005JC003430.

Sánchez-González, J.F., Sánchez-Rojas, V., Memos, C.D., 2011. Wave attenuation due
to posidonia oceanica meadows. J. Hydraul. Res. 49 (4), 503–514. http://dx.doi.
org/10.1080/00221686.2011.552464, URL: http://www.tandfonline.com/doi/abs/
10.1080/00221686.2011.552464.

CoastalEngineering168(2021)10394719L. Zhu et al.

Sappati, P.K., Nayak, B., VanWalsum, G.P., Mulrey, O.T., 2019. Combined effects of
seasonal variation and drying methods on the physicochemical properties and
antioxidant activity of sugar kelp (saccharina latissima). J. Appl. Phycol. 31
(2), 1311–1332. http://dx.doi.org/10.1007/s10811-018-1596-x, URL: http://link.
springer.com/10.1007/s10811-018-1596-x.

Sarpkaya, T., O’Keefe, J.L., 1996. Oscillating flow about two and three-dimensional
bilge keels. J. Offshore Mech. Arct. Eng. 118 (1), 1–6. http://dx.doi.org/10.1115/
1.2828796, URL: https://asmedigitalcollection.asme.org/offshoremechanics/article/
118/1/1/434651/Oscillating-Flow-About-Two-and-ThreeDimensional.

Schneider, C.A., Rasband, W.S., Eliceiri, K.W., 2012. NIH Image to imagej: 25 years of
image analysis. Nature Methods 9 (7), 671–675. http://dx.doi.org/10.1038/nmeth.
2089, URL: http://www.nature.com/articles/nmeth.2089.

Stévant, P., Rebours, C., Chapman, A., 2017. Seaweed aquaculture in Norway: recent
industrial developments and future perspectives. Aquac. Int. 25 (4), 1373–1390.
http://dx.doi.org/10.1007/s10499-017-0120-7, URL: http://link.springer.com/10.
1007/s10499-017-0120-7.

van Veelen, T.J., Fairchild, T.P., Reeve, D.E., Karunarathna, H., Van Veelen, T.J.,
Fairchild, T.P., Karunarathna, D.E., 2020. Experimental study on vegetation flexi-
bility as control parameter for wave damping and velocity structure. Coast. Eng.
157, 103648. http://dx.doi.org/10.1016/j.coastaleng.2020.103648, URL: https://
linkinghub.elsevier.com/retrieve/pii/S0378383919300663.

Vettori, D., Nikora, V., 2017. Morphological and mechanical properties of blades of
saccharina latissima. Estuar. Coast. Shelf Sci. 196, 1–9. http://dx.doi.org/10.1016/
j.ecss.2017.06.033.

Vettori, D., Nikora, V., 2018. Flow–seaweed interactions: a laboratory study using blade
models. Environ. Fluid Mech. 18 (3), 611–636. http://dx.doi.org/10.1007/s10652-
017-9556-6, URL: http://link.springer.com/10.1007/s10652-017-9556-6.

Vettori, D., Nikora, V., 2019. Flow-seaweed interactions of saccharina latissima at a
blade scale: turbulence, drag force, and blade dynamics. Aquatic Sciences 81 (4),
61. http://dx.doi.org/10.1007/s00027-019-0656-x, URL: http://link.springer.com/
10.1007/s00027-019-0656-x.

Vettori, D., Vettori student, D., Nikora Professor, V., Nikora, V., 2020. Hydrodynamic
performance of vegetation surrogates in hydraulic studies: a comparative analysis of
seaweed blades and their physical models. J. Hydraul. Res. 58 (2), 248–261. http://
dx.doi.org/10.1080/00221686.2018.1562999, URL: https://www.tandfonline.com/
doi/full/10.1080/00221686.2018.1562999.

Xiao, X., Agusti, S., Lin, F., Li, K., Pan, Y., Yu, Y., Zheng, Y., Wu, J., Duarte, C.M., 2017.
Nutrient removal from chinese coastal waters by large-scale seaweed aquaculture.
Sci. Rep. 7 (1), 46613. http://dx.doi.org/10.1038/srep46613, URL: http://www.
nature.com/articles/srep46613.

Yin, Z., Wang, Y., Liu, Y., Zou, W., 2020. Wave attenuation by rigid emergent vegetation
under combined wave and current flows. Ocean Eng. 213, 107632. http://dx.
doi.org/10.1016/j.oceaneng.2020.107632, URL: https://linkinghub.elsevier.com/
retrieve/pii/S0029801820306338.

Zeller, R.B., Weitzman, J.S., Abbett, M.E., Zarama, F.J., Fringer, O.B., Koseff, J.R.,
2014. Improved parameterization of seagrass blade dynamics and wave attenuation
based on numerical and laboratory experiments. Limnol. Oceanogr. 59 (1), 251–
266. http://dx.doi.org/10.4319/lo.2014.59.1.0251, URL: http://doi.wiley.com/10.
4319/lo.2014.59.1.0251.

Zhu, L., Huguenard, K., Fredriksson, D.W., Lei, J., 2021.Wave attenuation by flexible
vegetation (and suspended kelp) with blade motion: Analytical solutions, Adv.
Water Resour., in revision.

Zhu, L., Huguenard, K., Zou, Q.-p., Fredriksson, D.W., Xie, D., 2020a. Aquaculture
farms as nature-based coastal protection: Random wave attenuation by sus-
pended and submerged canopies. Coast. Eng. 160, 103737. http://dx.doi.org/10.
1016/j.coastaleng.2020.103737, URL: https://linkinghub.elsevier.com/retrieve/pii/
S0378383919303990.

Zhu, L., Zou, Q., 2017. THREE-Layer analytical SOLUTION FOR WAVE attenuation
BY SUSPENDED and nonsUSpended vegetation CANOPY. Coast. Eng. Proc. 1
(35), 27. http://dx.doi.org/10.9753/icce.v35.waves.27, URL: https://icce-ojs-tamu.
tdl.org/icce/index.php/icce/article/view/8239.

Zhu, L., Zou, Q.-p., Huguenard, K., Fredriksson, D.W., 2020b. Mechanisms for the
asymmetric motion of submerged aquatic vegetation in waves: A consistent-
mass cable model. J. Geophys. Res. Oceans 125 (2), 1–31. http://dx.doi.org/
10.1029/2019JC015517, URL: https://onlinelibrary.wiley.com/doi/abs/10.1029/
2019JC015517.

Zijlema, M., Stelling, G., Smit, P., 2011. SWASH: An operational public domain code
for simulating wave fields and rapidly varied flows in coastal waters. Coast.
Eng. 58 (10), 992–1012. http://dx.doi.org/10.1016/j.coastaleng.2011.05.015, URL:
https://linkinghub.elsevier.com/retrieve/pii/S0378383911000974.

CoastalEngineering168(2021)10394720