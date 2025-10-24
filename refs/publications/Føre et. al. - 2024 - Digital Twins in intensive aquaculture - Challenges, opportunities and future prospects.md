Contents lists available at ScienceDirect

Computers and Electronics in Agriculture

journal homepage: www.elsevier.com/locate/compag

Review article

Digital Twins in intensive aquaculture — Challenges, opportunities and
future prospects
Martin Føre a,∗, Morten Omholt Alver a, Jo Arve Alfredsen a, Adil Rasheed a, Thor Hukkelås a,
Hans V. Bjelland b, Biao Su b, Sveinung J. Ohrem b, Eleni Kelasidi b, Tomas Norton c,
Nikos Papandroulakis d
a Department of Engineering Cybernetics, NTNU, Trondheim, Norway
b Department of Aquaculture Technology, SINTEF Ocean, Trondheim, Norway
c Animal and Human Health Engineering (A2H), KU Leuven, Belgium
d Institute of Marine Biology, Biotechnology and Aquaculture, Hellenic Centre of Marine Research, Heraklion Crete, Greece

A R T I C L E I N F O

A B S T R A C T

Keywords:
Digital twin
Marine fish farming
Precision farming
Modelling

Digital Twin technology has emerged to become a key enabling technology in the ongoing transition into
Industry 4.0. A Digital Twin is in essence a digital representation of an asset that provides better insight
into its dynamics by combining a priori knowledge of the system through mathematical models with online
data acquired from sensors and instruments deployed in or at the physical asset. While the technology is
seeing increased use across several different industrial, governmental and research sectors, and across scientific
disciplines, its application within aquaculture is still in its infancy. However, due to the rapid ongoing
development in technological methods in aquaculture, an increasing number of the building blocks required to
make a Digital Twin for aquaculture purposes are becoming available. We set out to explore these possibilities
by first defining a Digital Twin — what components it should contain, how it should be constructed, and
outlining the capability levels of a finished Digital Twin.

Our next step was then to explore the state-of-the-art within the different required components and
enabling technologies within aquaculture, thereby identifying the current foundation for developing Digital
Twin technology in this sector. Following this, we developed concrete case studies that elaborate upon how
we by combining existing and developing new technological tools could envision developing Digital Twins
for three application areas of high industrial relevance, namely oxygen conditions in sea-cages, fish growth in
sea-cages and in-cage robotics and vehicle operations. In conclusion, we present our thoughts on the potential
of Digital Twin technology in being a key component in ushering in Industry 4.0 in aquaculture, and outline
a pathway on the way onward towards achieving this goal.

1. Introduction

The concept of Digital Twins has gained a strong following, and
been proposed as an emerging disruptive technology in several in-
dustrial fields (Rasheed et al., 2020). A Digital Twin offers a digital
representation of a real-world system or asset of interest that merges
mathematical models (knowledge based and data driven models) of
that system with real-time data from the system (VanDerHorn and
Mahadevan, 2021). By capitalising on the symbiosis of these compo-
nents, Digital Twins typically offer capabilities within describing and
predicting system dynamics, and monitoring and estimating system
states that are difficult to observe directly. If elements from decision
support and risk analysis are also included, these capabilities may be

further expanded to also include the ability to diagnose challenges
arising in the system and prescribe/recommend solutions to these.
Provided that the Digital Twin’s representation of the system/asset
is sufficiently complete and computationally tractable, Digital Twins
can also be a tool for realising closed-loop autonomous control of the
system/asset.

While the capabilities of Digital Twins developed and applied in
many fields are increasing rapidly (Rasheed et al., 2020; VanDerHorn
and Mahadevan, 2021), there have been few attempts at using Digital
Twin technology for aquaculture applications. One of the main reasons
for this is probably that intensive aquaculture is a comparatively young
industry. Most early R&D efforts in aquaculture have accordingly had
to focus on solving the concrete biological challenges of underwater

∗ Corresponding author.

E-mail address: Martin.fore@ntnu.no (M. Føre).

https://doi.org/10.1016/j.compag.2024.108676
Received 20 September 2023; Received in revised form 19 January 2024; Accepted 23 January 2024

ComputersandElectronicsinAgriculture218(2024)108676Availableonline1February20240168-1699/©2024TheAuthor(s).PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).M. Føre et al.

animal production. However, many of these challenges have now been
overcome, and the industry is at a point where the focus should be
shifted to developing farm management practices to better monitor
and control the fish production. Developing such new farming practices
requires insight into the inner dynamics of the biological and physical
processes involved in fish farming, and the ability to continuously
monitor these. This is difficult to achieve in aquaculture as one of the
major challenges endemic to this industry is that most of the system
dynamics occur under water, rendering them difficult to observe and
safely access by humans. Digital Twin technology provides a potential
solution to this challenge. Considering the current and projected growth
of aquaculture, and its expected importance as a future provider of
human sustenance, it is important that the potential to create useful
Digital Twins for aquaculture is explored, and that a roadmap for
achieving this and thus reaping the benefits of doing so, is established.

1.1. Intensive fish farming

Aquaculture is one of the key providers of food for human consump-
tion, and fish farming is believed to be a crucial protein source for the
growing world population. This trend is also seen in global numbers for
aquaculture finfish production, which increased from 38 to almost 60
million tonnes between 2010 and 2020 (FAO, 2022). Fish farming can
roughly be divided into two different production paradigms: extensive
and intensive fish farming. While extensive fish farming is mainly based
on the natural environment at the site providing for all the needs
of the fish, intensive fish farming is focused on actively controlling
the culture conditions, feed delivery in particular. Better control leads
to improved end product quality, faster growth and more predictable
growth trajectories, all of which contribute to a better ability to deliver
fish to the market in accordance with customer needs and desires.
Better control over rearing conditions also improves the farmer’s ability
to manage industrial challenges associated with important areas such as
fish welfare, Health, Safety and Environment (HSE) and environmental
impacts (Føre et al., 2018).

The most common form of intensive fish farming in Europe is cage
based farming, where the fish are contained within net enclosures
suspended from plastic/polyester collars floating at the surface (McIn-
tosh et al., 2022). Cage based farming has grown rapidly in recent
years, both in terms of gross tonnage and local farm scales (McIntosh
et al., 2022). For instance, a typical salmon farm may today contain
as many as 10–15 cages, each measuring circumferences up to 200 m
and depths down to 50 m and containing up to 200 000 individual
fish. Although at relative smaller scales, the situation is similar in the
Mediterranean Sea with cages of 120–160 m in circumference, depths
from 30 to 50 m containing 150 000 to 200 000 individuals. While
these numbers and scales are indicative of industrial success, they also
impose increased challenges in monitoring the cultured animals during
production (Føre et al., 2018). This is an action that is required of any
form of animal husbandry, in many countries even by law (Medaas
et al., 2021). Moreover, the sheer spatial extent of fish farms limits the
ability to monitor all elements of the production system and actively
control the production through low-level control actions such as using
mechanised feeding systems to deliver feed.

Although the general principles of cage based farming are still
similar to that applied decades ago, external processes have stimulated
technological development in both farming structures and practices.
One such external process was an arrangement recently hosted by the
Norwegian government where experimental salmon production permits
were offered to companies that wish to develop new production con-
cepts for salmon (Moe Føre et al., 2022). To qualify for these permits,
the industry needed to demonstrate that their concept is different
from conventional production forms and that it contributes to solving
specific industrial challenges such as avoiding parasites or reducing nu-
trient release to the environment, or can be applied in areas previously
unsuitable for fish farming. This has led to the emergence of a myriad

of different novel production concepts that all have their particular
properties, and distinguish themselves from conventional cage based
farming in design, operational aspects or both. In many countries, there
are also strong incentives to locate sea-based farming further from
shore, both due to conflicting claims from other industries near the
coastline, such as capture fisheries and recreation and tourism, and due
to the shortage of near-shore sites suitable for fish production (Bjelland
et al., 2015; Morro et al., 2022). Furthermore, new systems in the form
of multiuse offshore concepts for combined installations for energy
harvesting and aquaculture are also gaining interest as a result of EU
policies (e.g., Papandroulakis et al., 2017).

Together, these trends steer production forms toward bigger and/or
more complex production units (McIntosh et al., 2022; Moe Føre et al.,
2022) that are often placed at more inaccessible locations with harsher
environments (Morro et al., 2022). Maintaining intensive fish farming
as a viable industry also in the future thus calls for new solutions
for better monitoring and controlling the biological production in fish
farms. These solutions must be founded in technological approaches.

1.2. Precision fish farming meets digital twins

The main intention of proposing the Precision Fish Farming (PFF)
concept was to establish a framework for how technology and au-
tomation can be introduced into fish farming practices to better cope
with present and future challenges (Føre et al., 2018). PFF seeks to
link technology and automation principles with the practical aspects
of aquaculture operations, and as such serves as a common arena for
the worlds of research and industry, and can also be generalised to
non-fish aquatic species. Using the framework, researchers can thus
communicate their results and findings in a setting that allows industry
to better relate these to their needs and challenges, and hence easier
adopt them into new solutions in the future. Conversely, PFF can also
be used as a tool for industry to communicate their needs and chal-
lenges to research communities in a format that is easier to translate
into concrete research activities. This dual purpose enables a better
harmonisation between technological research and development and
how operations are conducted at fish farms, which is of key importance
since any new technology needs to be accepted by the farmers who are
responsible for day to day farm management.

Industrial operations in aquaculture are complex as they contain
biological and technological elements, and are often conducted in
submerged and flexible structures in an exposed sea-environment. A
key element in PFF has therefore been to devise a system for break-
ing aquaculture operations down into distinct phases (Fig. 1). This
simplifies technology adaptation as it is then possible to fit specific
technological solutions with the simpler sub-operations in each phase
instead of trying to do so for the entire process at once.

Several scientific studies on technological development towards
aquaculture operations have sought to explore the dimensions proposed
in PFF. Some of these have expanded along the Observe direction in
seeking to develop new smart sensors to quantify various properties
related to the fish, e.g., by using machine vision to recognise individual
fish by automatically analysing their iris (Schraml et al., 2020) or
skin dot patterns (Cisar et al., 2021) and also individual or group fish
motion (Georgopoulou et al., 2021). Other approaches include those
that combine sensors in networks to acquire a more complete picture of
the situation in the farm. This has thus far been done for pond culture,
either through integrated networks of stationary (Komarudin et al.,
2021) or mobile (Ouyang et al., 2021) sensors. Others have proposed
to combine sensor data with mathematical models in an Internet of
Things (IoT) platform as tools for better interpretation, presentation
and refinement of the measurement data (O’Donncha and Grant, 2019)
or even using satellite data (Chatziantoniou et al., 2022). Modelling
was also the focus of the study conducted by Royer et al. (2021) who
developed and validated a model describing the oxygen dynamics in a
raceway for trout production. More recently, there have been similar

ComputersandElectronicsinAgriculture218(2024)1086762M. Føre et al.

Fig. 1. The Precision Fish Farming concept with the four phases.
Source: Reproduced with permission from Føre et al. (2018).

studies of oxygen dynamics in large ocean based farms (Alver et al.,
2022), and that have been used to assess potential effects of cage size
on oxygen dynamics (Alver et al., 2023). Although there have been
fewer studies targeting the Decide and Act phases, there are examples
where decision support systems have been applied to an aquaculture
setting (e.g., Mathisen et al., 2016, 2021), as well as an increasing
body of research aimed at aquaculture robotics (Kelasidi and Svendsen,
2022).

These and other ongoing studies illustrate that the PFF approach is
being applied either directly or indirectly today. Recent efforts have
also taken the next step in seeking to merge the worlds of modelling
and instrumentation to better observe and assess structural dynamics
at a commercial fish farm Su et al. (2023). However, there have been
few concrete attempts at doing similar exercises that also includes the
biological processes in aquaculture production units, and most of these
have so far been focused on organisms for first-feeding with simple
life cycles (Alver et al., 2010) or early life stages in fish. Digital Twin
technology could be a key element in serving this need.

Assimilation of real-time sensor data into mathematical models is a
core element in the Digital Twin concept, where the aim is to create a
virtual representation of a physical asset (Rasheed et al., 2020). Digital
Twin technology is being applied within an increasing number of
different industrial segments, a trend that has been stimulated by recent
advances in enabling technologies such as mathematical modelling,
artificial intelligence, and data processing capabilities and visualisation
methods. This has also spawned new initiatives aimed at achieving
technological convergence between these fields, and since this includes
data assimilation into mathematical models, the Digital Twin concept
emerges as a natural framework for making the next steps on the path
towards closed loop control of fish farming through PFF.

Additional insight into the benefits and opportunities of adapting
Digital Twins to animal production can be gained by looking to ter-
restrial livestock production. The concept Precision Livestock Farming
(PLF), which serves a similar purpose for this industry as PFF does in
fish farming, was established in the early 2000’s (Berckmans, 2017).
PLF was founded in the idea that improved control of livestock pro-
duction (and the benefits thereof) is possible through the intelligent
application of technology. This includes the use of sensors to monitor
behavioural, physiological and environmental indicators, mathematical
models that synthesise existing knowledge on the animal/farm dynam-
ics, and the combination of these to better describe the animal state
(production, motivation, stress and wellbeing) under terrestrial farming
conditions. Recent advances in fields such as Machine Learning (ML)
and Artificial Intelligence (AI) and increased availability of sensors has
improved the precision of these applications, and hence their potential
applications. This expanded space of opportunities has also spawned an
increased interest in the development and application of Digital Twin
technology in the agricultural community, particularly to facilitate
early identification of issues in animal groups or single animals, as
well as assess the impact of these issues (Schleich et al., 2017; Jones
et al., 2020). While some recent literature have provided an overview
on the possibilities for using Digital Twins in the farm operation
management (Verdouw et al., 2021), these are still explorative studies
and use-cases focusing on parts of digital twin. Completely integrated
Digital Twins have yet to be developed for agriculture mainly due to
the inherent diversity in the production systems and complex responses
of the animals to their environment and management (Neethirajan and
Kemp, 2021). These elements will also be relevant for aquaculture,
adding to the challenge of developing Digital Twin technology for this
sector.

ComputersandElectronicsinAgriculture218(2024)1086763M. Føre et al.

1.3. Motivation and research questions

The aim of this study was to explore the possibilities and potential
challenges of creating Digital Twins for cage based aquaculture in light
of the current state-of-the-art, and their potential for future use in
fish farming operations. An operational Digital Twin could serve as a
platform that:

• Facilitates seamless combination of real-time sensors and predic-
tive models enabling insight into the state and dynamics of the
fish population, and potentially projection into the future;

• Is a framework for virtual prototyping of new technologies, oper-

ational methods and instruments;

• Can be used to aggregate and operationalise system knowledge,
and whose completeness will grow with our increased insight into
the system;

• Enables the use of experience gained from one generation of fish

farms to develop next generation fish farms;

• Enables real-time visualisation, monitoring and optimal control.
• Supports operations planning at different time horizons by allow-

ing different scenarios to be evaluated;

A successful realisation of a Digital Twin for aquaculture would also
open for harvesting the added values of Digital Twins described by
Rasheed et al. (2020).

The main research questions we sought to answer in our study were:

1. Is it possible to define a Digital Twin concept for aquaculture
applications that enables the exploitation of the advantages of
this emerging technology?

2. Which tools and components needed to this end are already
available through the current state-of-the-art within aquaculture
technology?

3. What are the major knowledge gaps we need to fill to realise

Digital Twins in this field?

4. Is it possible through concrete case studies to highlight the way

onward toward achieving this goal?

1.4. Methodology and outline of study

Section 2 is largely dedicated to our addressing research question
1. We first surveyed the scientific literature to identify the components
required to create a Digital Twin that would fulfil the six roles a digital
twin may serve that are listed above.

Searches combining "digital twin" with other keywords including
"definition", "challenges" and "values" returned several thousand sources
seeking to define a Digital Twin. Since it is very difficult to condense
thousands of different approaches into one definition, we thus had to
select a set of studies whose concepts had enough common denomi-
nators to be feasible to combine. By synthesising the contents from
the resulting six studies, we then outlined a possible structure for a
Digital Twin for aquaculture, highlighting the different required tools
and components.

We also described the different capability levels and concluded our
survey of research question 1 by identifying specific applications of
Digital Twins in aquaculture and related segments such as agriculture
and hydroponics/aquaponics (Section 3.1). This was done through
literature searches using "digital twin" together with either "aqua-
culture"/"fish farming", "agriculture", or "hydroponics"/"aquaponics".
While these searches returned thousands of studies, not all of these
reflected a full Digital Twin implementation. Of the 13 studies that did,
we selected those found most relevant for demonstrating the Digital
Twin development and use in these sectors.

Section 3 presents our findings when addressing research question
2, and was thus broken down into subsections targeting each of the
main components required to create a Digital Twin for aquaculture.
For each component, we first conducted a literature survey where we

used keywords that were specific to both the application (‘‘aquaculture’’
or ‘‘fish farming’’) and related to the component type (e.g., ‘‘sensors’’,
‘‘computer vision’’, ‘‘modelling’’). We then did the same with a wider
application (e.g., ‘‘fish monitoring’’, ‘‘wild fish’’, ‘‘fisheries’’) to also
capture publications that were relevant although they were applied
to other fields. In cases where the relevant publications exceeded a
number that was practical to include in the manuscript, studies were
selected based on (1) relevance for the aquaculture industry, (2) the
quality of the results, and (3) publication year (newer publications
being favoured).

The last two research questions (3 and 4) are largely addressed
in Section 4, where we present possible Digital Twin setups for three
case studies. The case studies are based on specific industrial chal-
lenges in aquaculture we believe can be partly solved through Digital
Twin technology. The first of these was aimed at how Digital Twins
can improve monitoring of oxygen conditions in sea-cages. This is
an increasingly important industrial topic since the intensification of
production and increase in farm/cage scale may increase both the
risk and consequences of hypoxia events (Remen et al., 2013). In
the second case study, the potential of using Digital Twins to get
better real-time inputs on fish growth and biomass development in
commercial cages was explored. The rationale behind this choice is that
biomass development is the supremely most important process in any
aquaculture production, and that improved control over this process
can have very large impacts in production efficiency and precision.
While the first two case studies primarily highlighted the potential
of Digital Twins in improving monitoring and control of aquaculture
facilities, the third case study was more aimed towards technology
development. Recent industrial trends have tended toward increased
use of robotics and autonomous vehicles in aquaculture, particularly
when considering moving production to less accessible and exposed
locations (Bjelland et al., 2015). The third case outlines how a Digital
Twin could be used as both a virtual test bench for developing new
technologies, and as a monitoring tool during autonomous or remotely
piloted vehicle operations in fish farms.

Each study is described by first providing the industrial background
and motivation, and then iterating through the main components re-
quired to create the Digital Twin. This entails both including existing
tools and components that could have a role, and highlighting the
knowledge gaps that need to be filled to create the Digital Twin. The
case studies also represent potential pathways to developing Digital
Twins for aquaculture. In the final conclusion, we provide our thoughts
on the current status and future prospects on achieving the vision of
acquiring Digital Twins for aquaculture.

2. Defining a digital twin — main properties, necessary compo-
nents and enabling technologies

Our definition of Digital Twin is in line with those provided by
Rasheed et al. (2020) and VanDerHorn and Mahadevan (2021), and
the outline of the various properties and elements in Digital Twins will
hence be made in accordance with their perspectives.

2.1. Digital twin components

A Digital Twin is defined as a virtual representation of a physical
asset enabled through data and simulators for visualising, predicting,
monitoring, optimising and controlling system states, and improved
decision making (Rasheed et al., 2020). The overarching aims of setting
up a Digital Twin may in generic terms be to acquire a tool that enables
(1) better real-time remote control, maintenance and optimisation; (2)
increased safety in both material and humane aspects; (3) improved
knowledge and insight into dynamic processes.

Fig. 2 illustrates the main concepts of Digital Twins, fusing real time
monitoring of the system states with mathematical models, and also
incorporate some of their main end impacts. This view harmonises with

ComputersandElectronicsinAgriculture218(2024)1086764M. Føre et al.

Fig. 2. Conceptual description of a Digital Twin setup.

the Digital Twin concepts proposed within other fields in several other
recent studies (San et al., 2021; Elfarri et al., 2023; Stadtmann et al.,
2023a,b). The physical asset is here the fish farm (upper right hand
corner). Historical farm management data and data obtained through
instrumentation deployed in the farm are used together with existing
system knowledge to build the mathematical models describing the
process. These data are also assimilated into the Digital Twin using
data assimilation methods, thereby providing the link between the
predictive models and the real asset. In sum, this provides the core of
the Digital Twin implementation as implied in the left side of the figure.
The main direct uses of the Digital Twin are applications of the
Digital Twin as a decision and policy making tool (upper left corner), or
as a component in achieving the ability to assert optimal control of the
process (top centre of the figure). In these cases, the Digital Twin needs
to be in real-time or close to real-time contact with the physical asset
to exploit the online data stream from this. Digital siblings (bottom
of the figure), are not based on direct interaction with the asset, but
rather represent purely hypothetical scenarios using the Digital Twin
to explore the impact of situations or conditions on the asset without
having to expose the asset to these. This enables risk free exploration
of possible scenarios, which in an aquaculture setting could entail the
ability to explore how expanding the farm with more cages, outbreaks
of disease or challenging weather conditions may affect production
without having to experience this in the real asset.

2.1.1. Instrumentation and data

The nature of the instrumentation (i.e., type of instrument, spatial
and temporal distribution, sampling rates) needed to construct a Digital
Twin will depend on the asset being studied, and needs to be designed
such that it provides sufficient data to allow estimation of the system
state with acceptable accuracy. The optimal setup for maximising the
ability to capture the dynamics of the asset depends on both the asset
and the purpose/aim of the Digital Twin. Conversely, a Digital Twin
can also be used to optimise the instrumentation design by providing
inputs on how many sensors/measurement points will be necessary to
achieve good estimation of system states.

2.1.2. Models
Knowledge based models. Knowledge based models (KBM) are the most
common tools for operationalising existing a priori knowledge, and

there are several types of such models that could prove relevant for
quantifying the dynamics in aquaculture production facilities. KBMs are
built by synthesising knowledge on the system and its dynamics into
mathematical equations that subsequently can be used to predict the
responses of the system when subjected to a set of appropriate inputs.
Due to their foundation in system knowledge, KBMs will often have a
more clear cut line between measured data and the analysis of these.

Data driven models.
In cases where the existing knowledge on system
dynamics, components or elements is insufficient to develop KBMs,
Data Driven Models (DDMs) may offer an attractive alternative. De-
veloping DDMs requires datasets describing the set of known system
inputs and the corresponding system outputs these will elicit. Methods
from Artificial Intelligence (AI) and Machine Learning (ML) are then
used to identify input/output transformations, enabling the prediction
of system responses given a set of known inputs and initial/boundary
conditions. Such models range from interpretable data driven mod-
els to pure black box input/output representations. While black box
models are usually pure implementations of methods from AI and ML,
interpretable models are usually also subjected to rules, limitations
and boundaries defined for the asset at hand. Examples of such rules
could be that the parameters of a neural network are found through
evaluation against outputs that are required to adhere to periodic
boundary conditions defined by the physics of a system or rules based
on the physical properties of the system (for instance that the dissolved
oxygen content of sea-water has an upper limit depending on factors
such as temperature and local primary production).

2.1.3. Synthesising components into a digital twin

While instrumentation will handle the flow of data from the real
asset to the Digital Twin in either real time or periodically, the use
of KBMs and DDMs could be considered to serve a common purpose
by adapting a Hybrid Modelling Approach (von Rueden et al., 2020).
KBMs are then used to represent the part of the system dynamics
known to science and that can be properly described by mathematical
relations, while data driven elements are used to describe the remaining
dynamics. This concept is central in Big data cybernetics, where the
aim is to combine sophisticated mathematical models and Big data
processing methods into a more robust and complete foundation for
introducing feedback control of a system or asset of interest (Rasheed
et al., 2019).

ComputersandElectronicsinAgriculture218(2024)1086765M. Føre et al.

Fig. 3. Capability levels of Digital Twin.

2.2. Capability levels

The realism and completeness of the models and the degree of cov-
erage achieved through instrumentation determine how close a Digital
Twin resembles the asset it is intended to mimic. This also has a strong
impact upon the capabilities of the Digital Twin, i.e., what it could
potentially be used for. Based on the potential application of Digital
Twin technology, it is possible to identify six distinct capability levels:
0-standalone, 1-descriptive, 2-diagnostic, 3-predictive, 4-prescriptive,
and 5-autonomous (see Fig. 3).

Standalone digital twins. Standalone Digital Twins are categorised by
being created solely based on existing knowledge on the system dy-
namics and hence do not have a link with the real asset/process in
focus. As such, they may be considered purely model based precursors
to Digital Twins of a system rather than proper Digital Twins (Jones
et al., 2020; VanDerHorn and Mahadevan, 2021). This means that
standalone Digital Twins can be constructed on the proposed specifi-
cation of the asset before it is realised. One of their main values is that
they can be used for preliminary cost–benefit analyses (profit margin,
ecological/environmental impact assessment) of the asset before it is
built.

Descriptive digital twin. Descriptive Digital twins utilise both real time
or periodic data from instrumentation and models to provide a digital
representation of the present state of the asset. They can therefore give
a deeper insight into the inner workings of the farms at the required
granularity. Descriptive Digital Twins can be used to visualise even
those aspects of the asset which are not obvious to the naked eye.
Their main value is that they keep all stakeholders (even those having
no access to the physical farm) updated in real-time resulting in more
informed decision making.

Diagnostic digital twin.
If a descriptive Digital Twin is sufficiently ac-
curate, it can be extended to become a diagnostic Digital Twin able
to provide features such as fault detection and provide some degree of
decision support. This requires that the Digital Twin is set up to explore,
compute and assess the potential fault states and potential decision
criteria.

Predictive digital twin. Although standalone, descriptive and diagnostic
Digital Twins have their described benefits, neither of these have the
ability to provide well founded insights into the future. This can only be
achieved if the fidelity of the Digital Twin can be sufficiently increased
by integrating data streams and models more tightly, and validating
the outputs. The results of this process may be called a predictive
Digital Twin, and requires that data streams are assimilated into the
mathematical models using e.g., linear/nonlinear estimation methods.
Predictive Digital Twins retain all the properties of the lower capability
levels and can thus project the present as well as any past state into
the future, a capability that is valuable for e.g., predictive maintenance
or/and asset optimisation.

Autonomous digital twin. The final step on the capability scale entails
equipping the Digital Twin and the physical asset with bi-directional
communication. The physical asset can then update its Digital Twin
in real-time and in turn the Digital Twin can be set up to control the
asset towards an optimal set point by closing the loop and applying
model-based feedback control principles, in what can be referred to as
an autonomous Digital Twin.

3. State of the art for digital twin technology in aquaculture

In this section, we will outline the state of the art within Digital
Twin technology applied to aquaculture. We will first highlight a few
scientific contributions that have aspired to at least partially fulfil the
aims of Digital Twins in aquaculture, and then look deeper into the
state-of-the-art within the main sub-components required to realise
Digital twins, namely instrumentation, knowledge based modelling and
data-driven models.

3.1. Digital twin concepts

Although Digital Twins have been identified as part of the solution
to achieving precision farming, they have yet to become established
tools in agriculture practices (Pylianidis et al., 2021). Applications in
aquatic farming are even less mature than those in terrestrial agri-
culture. However, the industrial awareness of and interest in Digital
Twins for aquaculture is increasing as seen in initiatives highlighting
future possibilities (e.g., Ramos, 2021), or developments aimed at end
products for the farming industry (e.g., Berthelsen, 2017; Russel, 2021;
DNV GL, 2021). In research, there are also initiatives aimed at land-
based production that are interesting for the discussion on Digital
Twins for aquaculture, particularly those focused on intensive fish
production through raceway systems (Lima et al., 2022) or recirculating
aquaculture systems (RAS) (e.g., Zhabitskii et al., 2021). Others again
have sought to develop Digital Twins for aquaponics/hydroponics that
focused mainly on food production in the aquatic environment and less
on intensive animal production (e.g., Ahmed et al., 2019; Sreedevi and
Kumar, 2020; Ghandar et al., 2021).

There have also been some research initiatives on Digital Twins
for cage based fish farming, most of which have focused on using the
concept to monitor farm structural dynamics better. While some of
these are mainly exploratory on the modelling side (e.g., Staalesen,
2019), others have sought to implement data assimilation methods for
fusing model outputs with real-time sensor data (e.g., SINTEF Ocean,
2020; Su et al., 2023).

3.2. Instrumentation and observation

Prescriptive digital twin. The next step capability level is the prescrip-
tive Digital Twin which also incorporates methods for making rec-
ommendations based on what if ? / risk assessment and uncertainty
quantification based on the outputs of the Digital Twin.

These abilities are highly desirable for decision support systems.

Instrumentation will always be a key component in a Digital Twin
since it enables real-time tracking of the dynamics and states of the
process. To capture the full system dynamics in aquaculture, it is
thus necessary to apply instrumentation to monitor both the animal
population and the physical structures and environment at the site.

ComputersandElectronicsinAgriculture218(2024)1086766M. Føre et al.

Fig. 4. Illustration of different methods for observing fish in sea-cages.
Source: Reproduced from Føre et al. (2018).

3.2.1. Animal monitoring

Fish in aquaculture production facilities may be monitored either at
group or individual level using different types of technologies (Fig. 4).
These two fundamentally different approaches to animal monitoring
are largely complementary and can hence often be combined to acquire
a holistic picture of animal states. However, for some applications, a
purely individual or group focus may be sufficient.

Group level. The aquaculture industry has used technological solutions
such as biomass frames to monitor size distributions in fish groups (e.g.,
Folkedal et al., 2012) for decades. While such solutions are likely to
be important industrial tools also in the future, ongoing developments
within enabling technologies are opening new avenues and possibilities
for how the states of farmed fish groups can be objectively monitored.
Machine vision coupled with subsurface cameras is the most common
method for collecting group level data on fish in aquaculture fish
farms, spanning a wide variety of specific applications (e.g., Zion,
2012; Saberioon et al., 2017). Some existing applications such as the
assessment of fish swimming activity (e.g., Kolarevic et al., 2016;
Georgopoulou et al., 2021), size (e.g., Hao et al., 2015; Voskakis et al.,
2021), health condition (e.g., Jopling et al., 2021) and feeding activ-
ity (e.g., Måløy et al., 2019) may have particular importance for Digital
Twin development as they provide data on some of the most crucial
underlying biological processes at fish farms. Industry is also starting
to pick up on the utility of machine vision in aquaculture (Stavelin
et al., 2021), and several companies are now offering solutions that
claim to enable quantifying such values, meaning that these methods
are approaching industrial applicability. Some camera based systems
also provide lice estimates as one of the outputs automatically derived
from video footage.

The other main category of technologies for fish monitoring on
group level are acoustic methods, that may again be divided into
active and passive methods. Active methods are typically based on
emitting acoustic pulses with known spectral characteristics, and then
analysing the return pulses caused by reflections from objects within
the observed volume. The complexity of the resulting data depends
on the device type, ranging from basic 1D density distributions from
echo sounders (e.g., Johansson et al., 2006), through 2D swimming
speeds and fish sizes from splitbeam sonars (e.g., Arrhenius et al., 2000;
Knudsen et al., 2004), to complete volumetric distributions and mea-
surements using multibeam and high-frequency imaging sonars (e.g.,
Zhang et al., 2014; Cotter and Polagye, 2020,

for wild fish).

Studies have also shown that it is possible to gain information on
fish through passive acoustic monitoring (PAM), particularly during
specific activities such as feeding (Kasumyan, 2008; Rountree et al.,
2018; Rosten et al., 2023). Although passive monitoring is at a much
earlier developmental stage than active methods, it has promise for fu-
ture developments as it can be applied both omnidirectionally or aimed
at specific areas using beam shaping methods (Chiariotti et al., 2019).
While there are fewer industrial applications based on hydroacoustic
methods than for cameras, there are companies delivering solutions
for monitoring specific operations such as feeding or complete systems
monitoring.

In addition to the technological approaches mentioned above, regu-
lar observations that are a part of the everyday farm management such
as lice counts and mortality assessments can provide useful information
on the state of the fish population. While these are usually acquired
through manual inspection, their outcomes are typically inserted into a
centralised control system and will as such be available for monitoring
and/or control applications albeit not in real-time.

Individual level. Camera imaging and hydroacoustic methods can also
provide instantaneous data on individual fish, e.g., by assessing indi-
vidual swimming speed (Arrhenius et al., 2000; Georgopoulou et al.,
2021) or individual fish sizes (Knudsen et al., 2004; Difford et al.,
2020; Voskakis et al., 2021). Such information can provide insight
into individual variations at that specific point in time, which can
be useful information for understanding the dynamics observed at
group level. However, these methods can generally not provide long-
term data series for specific individuals, as they do not distinguish
which individuals are currently being observed. Although individual
identification can be achieved, at least for salmonids, by automatically
recognising unique features such as dot patterns (Stien et al., 2017;
Cisar et al., 2021), it is difficult to trace specific individuals over time
using such methods as they target sub-volumes in the cage, usually from
a static position.

Other monitoring methods, such as biosensors and telemetry, are
designed specifically to produce individual histories of data (Thorstad
et al., 2013). These methods require that the fish are first captured
in the cage, and then anaesthetised. The fish are then equipped with
electronic devices called tags either through surgical implantation or
external attachment before being released back into the cage again.
Suboptimal tag deployment may perturb a fish to the extent that they
exhibit behavioural and physiological changes (Georgopoulou et al.,
2022), potentially even leading to mortality (Macaulay et al., 2021),

ComputersandElectronicsinAgriculture218(2024)1086767M. Føre et al.

implying the need for proper interpretation of the dataset and expertise
in fish handling and surgery (Jepsen et al., 2002). While these concerns
render biosensors and telemetry a more complicated tool for industrial
deployment, placing the equipment on or in the animal opens for the
measurement of several parameters that are not possible to observe
through optical or acoustic means (Endo and Wu, 2019; Brijs et al.,
2021). Parameters that can be measured using commercially available
tags range from behavioural traits such as activity (Føre et al., 2011;
Kolarevic et al., 2016) and depth dynamics/positioning (Føre et al.,
2017; Stockwell et al., 2021) to physiological parameters such as heart
rate (Brijs et al., 2018; Hvas et al., 2020; Rosell Moll et al., 2021)
and even gastrointestinal blood flows (Brijs et al., 2019). Moreover,
the ongoing rapid developments in the fields of biosensor technology
and microelectronics has led to the emergence of increasingly complex
concepts able to measure hitherto unmeasurable parameters such as
movement speed through mini-Doppler shifts (Hassan et al., 2020)
and glucose and cholesterol (Endo and Wu, 2019). Coupled with the
inherent ability to generate individual data histories, this expanding
multitude of available data types implies that electronic tags can be a
potent tool for obtaining information on individual sentinel fish in both
research and potentially industrial applications (Føre et al., 2017).

3.2.2. Physical monitoring

The physical conditions of interest at a site can often be divided
between those pertaining to the dynamics of the farm construction and
those of the production environment.

Structural dynamics. Maintaining the structural integrity of the cages
in a fish farm is the foremost measure in preventing escapes (Moe Føre
and Thorvaldsen, 2021). Moreover deformations and movements in the
various farm components may have an impact on the fish. It is thus
important to monitor the movements and, if possible, deformations of
the production units to get a full picture of the conditions affecting the
fish. Some novel fish farming concepts are rigid structures (e.g., Ocean
Farm 1, Salmar; Preline, Lerøy) whose dynamics can be estimated using
data from sensors such as accelerometers, gyros and IMUs together
with geometric considerations. However, most farms are still based
on gravity type cages that are flexible and largely follow rather than
resist water motions. Due to their flexibility, the full dynamics of such
structures are notoriously difficult to monitor using available sensors.
One of the few properties of gravity cages that can be reliably moni-
tored with sensors are the gross loads acting on the structure. This has
been done using load cells mounted between the cage and the mooring
system, either in stationary farms (e.g., Fredriksson et al., 2003), or by
towing or pushing cages at predetermined speeds using a ship (e.g.,
Gansel et al., 2018). The structural dynamics can also be monitored
with a higher resolution through position sensors mounted strategically
on the net structure, thereby obtaining the 3D position of these points
in the net, which in turn are used to extrapolate the shape of the
full net structure using mathematical models (e.g., Haugaløkken et al.,
2018; Su et al., 2021). Structural monitoring can also include direct
observations of net integrity, i.e., measurements aimed at detecting
if there is damage to the net. This has previously mainly been done
using solutions based on computer vision (e.g., Zacheilas et al., 2021;
Madshaven et al., 2022) attached to mobile platforms that patrol the
inner perimeter of the cage (e.g., Livanos et al., 2018; Amundsen et al.,
2022).

Environment. Environmental monitoring is the most common type of
monitoring in fish farming, partly due to governmental requirements to
measure currents at a site before farm establishment, but also because
fish farmers are seeing an increasing need to continuously monitor
factors important for fish growth and welfare. This is also reflected
within science, as studies aiming to explore fish responses toward
cage operations and management (e.g., Oppedal et al., 2001; Føre
et al., 2011; Erikson et al., 2016) often require environmental data as
auxiliary sources of information. Some studies even aim specifically

on studying variations in environmental factors (e.g., Burke et al.,
2021), or how such variations impact fish behaviour (e.g., Johans-
son et al., 2006; Oppedal et al., 2011), growth (e.g., Cuenco et al.,
1985; Solstorm et al., 2018) and welfare (e.g., Jónsdóttir et al., 2019).
The most common instruments used for environmental monitoring in
aquaculture are commercial off the shelf (COTS) sensors designed for
long term monitoring of variables such as temperature (e.g., Johansson
et al., 2006), oxygen (e.g., Solstorm et al., 2018) and salinity (e.g.,
Oppedal et al., 2019). Other environmental features such as wave spec-
tra and water current require more complex instruments like Acoustic
Doppler Current Profilers (ADCPs) or Acoustic Wave and Current Pro-
filers (AWACs). Although such devices are usually more costly than
conventional sensors, they are seeing increased use in research (e.g.,
Fredriksson et al., 2007; Michelsen et al., 2019), and are even included
as permanent instruments in some of the more recently developed
farming concepts for production further from shore. Environmental
monitoring has recently been realised by using satellite data comple-
mented with data from drones (Chatziantoniou et al., 2022) thereby
providing data describing the conditions in a larger area than a cage
or a farm, an approach that is of particular interest when organised
aquaculture parks are operating or for monitoring HAB events (Nichols
and Hogan, 2022). In this way, the monitoring of a larger area may
provide insight on possible interactions between farms, particularly if
coupled with hydrodynamic/oceanographic models.

3.3. Knowledge based models

Knowledge based models are likely to form the backbone of digital
twins for aquaculture as they aggregate existing system knowledge. The
idea of developing mathematical models for predicting the dynamics
of farmed fish populations has existed for decades (Balchen, 1979).
These early initiatives did not proceed beyond the theoretical level
as their realisation requires a technological level that did not exist in
the 70’s. However, as the availability and capacity of computational
resources and other technological tools has increased in time, so have
the possibilities and opportunities within mathematical modelling and
simulation of increasingly complex systems. Although this has resulted
in a large body of predictive models seeking to represent various sides
of the dynamics of fish farms and the processes therein, aquaculture
production facilities are inherently interdisciplinary systems and need
to be treated as such. Successfully developing a Digital Twin that
captures the full system dynamics in a fish farm will therefore require
a combination of models able to predict the biological (e.g., behaviour,
growth, welfare), physical (e.g., structural, hydrodynamic) and en-
vironmental dynamics at the site. We will in the following outline
the current status on knowledge based modelling in fish farming,
where theory and knowledge on fish and fish farming systems is
synthesised into predictive models, first covering models aimed at the
biological aspects (i.e., fish behaviour and growth) and then those
replicating physical/environmental dynamics. Fig. 5 describes four con-
crete examples of models within these categories aimed at aquaculture
applications.

3.3.1. Biological models
Behavioural models. Unlike simpler organisms such as zooplankton
(e.g., Alver et al., 2006) or fish larvae (Lika and Papandroulakis, 2005),
adult fish have explicit behaviours that are important components in
how they cope and interact with the culture conditions, assimilate
nutrition and develop in the production unit. Models portraying fish
behaviour will therefore be crucial elements in the development of
a Digital Twins of fish farming operations. Although the potential
importance of behavioural modelling in controlling fish production was
first implied in the 70’s (e.g., Balchen, 1979, 2000), there have been
few attempts at creating generic models for portraying the behavioural
dynamics in farmed fish populations. This may be due to the difficulty
of finding sufficient high quality data to develop and verify reliable and

ComputersandElectronicsinAgriculture218(2024)1086768M. Føre et al.

Fig. 5. Examples of Knowledge based models aimed at aquaculture processes. (a) individual based fish behaviour model simulating movements in sea-cage (simulation based on
the model presented by Føre et al., 2009); (b) Finite Element Model representing net cage deformations (reproduced with permission from Moe et al., 2010); (c) advection–diffusion
type model used to simulate oxygen flow and depletion in sea-cages of various sizes (reproduced from Alver et al., 2023); (d) (c) oceanographic model used to simulate distribution
f particulate matter from fish farms in larger spatial scales (reproduced from Broch et al., 2020).

realistic predictive models. Attempts have been made at synthesising
knowledge based on echo sounder observations in sea-cages into an
individual based model of salmon behaviour (Fig. 5a, Føre et al., 2009).
These models provide insight into the dynamics of vertical distributions
and group migration patterns in salmon, but not other elements such as
how realistic the horizontal distribution patterns or individual response
patterns are. Further development of such models to also cover these
aspects will probably require the use and assimilation of data from
other sources, such as biosensors/telemetry and cameras, that have
both been in rapid development in later years.

through manual

Growth models. Fish growth is easier to objectively quantify than be-
haviour, and can be assessed either
sampling
(e.g., comparing individual fish weight at different times), or by using
technological tools specifically designed to estimate fish size. More-
over, since fish growth is intrinsically linked with the economic profit
of a farming operation, the industry has practised growth tracking
throughout the history of aquaculture. This has resulted in a data and
knowledge base available for the development of fish growth models
that is considerably more concise and comprehensive than that for
developing behaviour models. From this base, it has been proven pos-
sible to develop models describing how farmed fish growth is affected
by feeding methods (e.g., Cho and Bureau, 1998) and environmental
features such as temperature and oxygen (e.g., Cuenco et al., 1985;
Björnsson et al., 2007; Stavrakidis-Zachou et al., 2019; Stavrakidis-
Zachou et al., 2021). The approaches applied to model growth in
farmed fish range from early attempts on basic curve fitting between
fish weight and age (e.g., Chen et al., 1992), to more knowledge
based approaches seeking to replicate the internal energetics of the
organism (e.g., Kooijman, 2000; Nisbet et al., 2012; Nobre et al., 2019).

3.3.2. Physical and environmental models
Fluid–structure interaction. Although basic physical relationships and
equations can be used to predict the hydrodynamic forces acting on
individual cage components, modelling a full cage system comprised
by interconnected components requires data for development and sub-
sequent validation. Sea-cages have therefore received much attention
from engineers and researchers seeking to map their hydrodynamic
interactions with the environment (as reviewed by Klebert et al., 2013)
Although some studies have also been conducted in full-scale fish
farms (e.g., Fredriksson et al., 2003; Lader et al., 2008), most of this
data and knowledge has been obtained through scaled down studies in
laboratories where it is possible to monitor and control both conditions
and structural responses with high accuracy (Moe-Føre et al., 2016;
Dong et al., 2019). When scaled up accordingly, it is possible to use
the outcomes from such studies to describe the expected system dy-
namics, and hence the responses and tolerance of the structure towards
environmental factors. This has led to a vast body of knowledge on the
dynamic interaction of flexible sea-cages that has in turn been used to
derive different models describing the loads and deformations exhibited
by cages and their sub-systems when subjected to environmental forces
like currents and waves (Fig. 5b, e.g., Tsukrov et al., 2003; Moe et al.,
2010; Dong et al., 2010). Other studies have also looked into how
cage structures in turn affect the ambient and cage-internal environ-
ment (e.g., Klebert and Su, 2020), either by full Computational Fluid
Dynamics (CFD) analyses (e.g., Winthereig-Rasmussen et al., 2016),
or by ‘‘line-of-sight’’-based approaches to predict shadow effects (e.g.,
Løland, 1993; Endresen et al., 2013).

Cage environment models. Models that seek to describe the dynam-
ics behind particle movement and distribution in volumes have also
several applications in modelling the dynamics in aquaculture produc-
tion units. These models can either be based on generic modelling

ComputersandElectronicsinAgriculture218(2024)1086769M. Føre et al.

paradigms like CFD or be custom made frameworks designed to model
specific phenomena, and have previously been used to simulate the feed
distribution in fish farms in 2D (Alver et al., 2004) and 3D (Alver et al.,
2016), and particle removal from production units (e.g., Klebert et al.,
2018). Although it is difficult to assess the accuracy of such models
in full-scale aquaculture situations, a recent study used an advection–
diffusion based model to simulate oxygen distribution in sea-cages, and
validated it using measurement data from a large rigid sea-cage (Fig. 5c,
Alver et al., 2022, 2023).

Ambient environment models. When modelling the cage environment, it
is also necessary to identify methods for representing the dynamics in
the ambient environment both close to or far from the fish farm as these
can provide the boundary conditions for the models simulating the in-
cage dynamics. There are several different oceanographic models (e.g.,
Slagstad and McClimans, 2005; Shchepetkin and McWilliams, 2005;
Urke et al., 2021) that fit the purpose of estimating the physical
and chemical conditions in regions of various sizes and resolutions.
Such models have been used for purposes ranging from forecasting
oceanographic conditions (e.g., Slagstad et al., 2011), through data
assimilation (e.g., Moore et al., 2011), to multi-scale modelling in
conjunction with CFD (Fig. 5d, e.g., Broch et al., 2020). While oceano-
graphic models can provide inputs on currents, nutrient flows and other
physical/chemical properties, a Digital Twin will also need some way
of assessing the local effects of waves, particularly when considering
operations in more exposed areas (Bjelland et al., 2015). This role could
be fulfilled by models designed to predict coastal wave generation (e.g.,
Sukhinov et al., 2013), or by combining models relating wind and
waves (e.g., Chalikov, 1978) with farm wind exposure analyses (e.g.,
Lader et al., 2017).

3.4. Data driven models

More recently, data-driven modelling has become increasingly pop-
ular due to the abundance of big data, easy-to-use machine learning
libraries, cheap computational infrastructure, and readily available
training resources. These models are built on the assumption that
data represents both known and unknown physics. With enough data,
data-driven models can learn the underlying physics on their own,
resulting in models that achieve super human-level performance in
tasks previously deemed impossible for computers.

Any data-driven model can be put in one of the six categories. These

models in the context of aquaculture is explained below:

3.4.1. Supervised linear models

These models are trained with labelled data, where the target vari-
able is known. Linear regression and logistic regression are examples
of this type of model. They are simple and efficient and can be used
for tasks such as prediction, classification, and feature selection. In
a comparatively early study, Palomares and Pauly (1989) developed
a regression model able to predict food consumption in marine fish,
while a more recent study by Sara et al. (2009) demonstrated the utility
of such models in describing and predicting growth and feed intake
in marine prawns. While these studies were not aimed at cultured
animals, they illustrate the potential usefulness of such models also in
aquaculture.

3.4.2. Unsupervised linear models

These models are trained with unlabelled data, where the target
variable is unknown. Principal component analysis (PCA) and linear
discriminant analysis (LDA) are examples of this type of model, and can
be used for tasks such as dimensionality reduction, feature extraction,
and clustering. There have been previous studies using such methods
towards aquaculture applications, exemplified by Simonnet-Laprade
et al. (2021) who demonstrated strategies for the characterisation of
chemical contaminant mixtures in the contest of fish contaminant using
PCA and LDA.

3.4.3. Supervised non-linear models

Models belonging to this class are trained with labelled data, are
more flexible than linear models, and include well-known approaches
such as decision trees, support vector machines (SVMs), and random
forests. Such models can capture complex relationships between the
features and the target variable, and have often been used in combi-
nation with cameras and other machine vision components (Saberioon
et al., 2017). In a recent study, Palaiokostas (2021) assessed SVM,
and various tree based methods in terms of their efficiency to predict
disease resistance in both simulated and real-life aquaculture datasets,
also considering the computational cost associated with the training of
different models.

3.4.4. Unsupervised non-linear models

These models are trained with unlabelled data, are more flexible
than unsupervised linear models and include notable model types
such as Self-organising maps (SOMs) and K-Nearest Neighbour. Unsu-
pervised non-linear models can be used for tasks such as clustering,
anomaly detection, and data compression. Example applications from
aquaculture include Russo et al. (2010) who utilised SOM to study of
skeletal anomalies and meristic counts in gilthead seabream, and Iswari
et al. (2017) who demonstrated a fish freshness classification method
based on applying k-Nearest Neighbour to fish images.

3.4.5. Supervised deep learning

Supervised Deep learning models are trained with labelled data and
complex architectures. Convolutional neural networks (CNNs) for im-
age recognition, recurrent neural networks (RNNs) for natural language
processing, and fully connected deep neural networks for regression
and classification tasks are prominent examples of models belonging
to this class. Deep learning models can achieve state-of-the-art perfor-
mance in many tasks and are highly flexible. Some recent examples
belonging to this category include the use of neural networks to predict
feed intake in rainbow trout based on water temperature, oxygen,
average weight and number of fish (Chen et al., 2020), and the use
of Q-learning to track fish growth trajectories (Chahid et al., 2022).
Moreover, Måløy et al. (2019) and Måløy (2020) used deep learning
methods to derive behavioural parameters from video footage and echo
sounder data collected from farmed salmon.

3.4.6. Unsupervised deep learning

These models are trained with unlabelled data and complex archi-
tectures. Generative adversarial networks (GANs) for image synthesis
and unsupervised feature learning and autoencoders for data com-
pression and anomaly detection are examples of this type of model.
Unsupervised deep learning models can be used for tasks such as
unsupervised feature learning, anomaly detection, and generative mod-
elling.

4. Concept studies

The preceding literature review shows that many of the components
required to design a Digital Twin of an aquaculture fish farm exist.
However, to achieve this goal, we need to combine these components
into a complete solution that maintains the properties we require from
a proper Digital Twin. In this section, we will illustrate this by out-
lining three concrete cases that are founded in published experimental
studies. For each case, we will first describe elements within the three
main component classes (i.e., knowledge based models, real-time data
collection systems and data driven models) needed to build the Digital
Twin for that case. We will then suggest how these elements can be
integrated into a common system, before finally suggesting potential
industrial applications for the resulting Digital Twin.

ComputersandElectronicsinAgriculture218(2024)10867610M. Føre et al.

Fig. 6. Components that could be components in a Digital Twin aimed at concept 1. (a) instrumentation package to collect data on e.g., oxygen and current conditions in
the cage volume (Reproduced with permission from Alver et al., 2022); (b) mathematical individual based model of fish behaviour (simulation based on Føre et al., 2009); (c)
advection–diffusion models for simulating the distribution and depletion of oxygen through the cage volume (Reproduced with permission from Alver et al., 2022).

4.1. Concept 1: Oxygen conditions in sea-cages

4.1.1. Background

Fish farmers have a strong motivation to avoid hypoxia events
(e.g., Remen et al., 2013) where dissolved oxygen levels drop to a level
that can cause stress and other welfare-compromising effects (Remen
et al., 2012), potentially even increasing the likelihood of disease out-
breaks and acute mortality (e.g., Abdel-Tawwab et al., 2019). Whereas
terrestrial farming operations can ensure sufficient oxygen through
active ventilation, the higher density of water and size of the volumetric
flow through a cage, which depends on a variable current speed,
renders this more challenging in fish farming. Moreover, the nominal
oxygen concentration in water (less than 1%) is much lower than in
air (about 20%), and is also very sensitive to water temperature. These
effects imply that it is important to monitor dissolved oxygen levels
in fish farming, both to provide decision support for the farmer, and
to serve as a foundation for future solutions for improving the oxygen
conditions in sea-cages. A Digital Twin reflecting the distribution of
dissolved oxygen in sea-cages is a potential first step in achieving
this level of control. In a recent study, a mathematical model of how
dissolved oxygen propagates through the production volume of a large-
scale rigid cage structure (Ocean Farm 1, Fig. 6) was presented and
validated (Alver et al., 2022), and has been further used to analyse
how cage size affects oxygen levels in sea cages (Alver et al., 2023).
This model can form the basis for the Digital Twin concept outlined in
the following.

4.1.2. Knowledge based models

Alver et al. (2022) (Fig. 6a, c) compared their model predictions
with data series collected for low, moderate and high current speeds

by oxygen sensors placed at 12 m depths at four positions along the
outer perimeter of the cage. Although this validation proved the model
able to predict most of the dynamics in dissolved oxygen levels within
the cage, the study also identified some potential future expansions
that could improve its performance in generic cases, several of which
were associated with the oxygen consumption of the fish. One key
element was that the distribution of the fish within the volume was
represented by qualitative assumptions on how the fish distribute in
response to feeding. A more advanced behavioural model for reflecting
the movements and distribution of fish could contribute to increasing
the realism in this aspect. This could be done by integrating the oxygen
model with existing models of fish behaviour in sea-cages (Fig. 6b,
e.g, Føre et al., 2009, 2016), if these models were first calibrated to
the structural properties and environment of the asset targeted by the
Digital Twin.

4.1.3. Real-time data collection

The dataset used by Alver et al. (2022) featured data collected using
hard-wired oxygen and temperature probes and current profilers placed
outside the cage (Fig. 6 a), and feed delivery signals from the farm
management system. Although this provided a sufficiently good picture
of the oxygen dynamics in the cage, a higher resolution and hence
precision could be obtained by also collecting oxygen data and current
data from the volume inside the cage. This could enable both a more
thorough validation of the model, and provide a better foundation for
assimilating current and oxygen data with the model. There were also
12 scientific echo sounders (EK80, Kongsberg Maritime) deployed at
the site during the trials that can provide echograms describing the
distribution of the fish, and split-beam functionality that can be used
to assess individual fish size (Knudsen et al., 2004) and swimming

ComputersandElectronicsinAgriculture218(2024)10867611M. Føre et al.

speeds (Arrhenius et al., 2000). While these data were not employed
by Alver et al. (2022) as their analyses would be a considerable research
task in itself, a future Digital Twin of this system could benefit from also
exploiting these data types to better describe fish distribution and sizes.

4.1.4. Data-driven models

While the inter-calibration between the oxygen probes used by Alver
et al. (2022) could be categorised as a form of machine learning,
it is possible that data-driven models could serve a bigger purpose
by portraying some of the elements that are less clearly defined in
the knowledge based models. Considering the large amounts of data
produced by hydroacoustic systems, it would be particularly relevant
to look at such methods for analysing fish distributions and responses
toward the prevailing conditions in the cage. Previous work on this area
has resulted in methods able to classify different types of fish behaviour
and even detect disease outbreaks by applying deep learning methods
to hydroacoustic data collected from sea-cages (Måløy, 2020). Similar
methods could also be used as a means to develop data-driven models
able to predict fish distribution based on a set of input parameters
(e.g., temperature, feeding, light).

4.1.5. Module integration

The first integration step required to develop the Digital Twin for
this case would be to facilitate a real-time link between the sensors and
the mathematical model. For the instruments already attached to the
cage structure (i.e., oxygen probes, temperature sensors, echo sounders)
the main technical task would be to provide a communication link
for forwarding the data streams from these to the computer running
the model. Successful integration would also require the development
of an interface for assimilating the data into the model. Temperature
and current measurements, as well as oxygen measurements outside
of the farm representing ambient conditions, could be used in real-
time to provide appropriate input values to the oxygen model. Data
from oxygen sensors within the model domain could be used directly
by comparison to predicted values at matching positions, using an
Ensemble Kalman Filter (Evensen et al., 2009) or other approaches to
compute model corrections.

Echo sounder data would require more extensive processing and
translation before being assimilated into the model. This would entail
both the synthesis of data from all 12 echo sounders into a common
dataset, and deriving fish distribution estimates from this. The resulting
datastream could then be both assimilated into the knowledge based
behavioural model and be used to train the data driven model of fish
distribution. These models could then be set up in the cascade structure
proposed in the Big data cybernetics approach (Rasheed et al., 2020).
This would effectively exploit real-time data, knowledge based mod-
elling and data driven models to acquire a better estimate of dissolved
oxygen distribution in sea-cages. Finally, developing a human machine
interface to present and visualise the twinned cage oxygen conditions
to the user would finalise the Digital Twin for their application.

4.1.6. Industrial applications

The most apparent benefit of achieving a fully functional Digital
Twin of the oxygen distribution in sea-cages is that it will provide
farmers with a more complete picture of the oxygen situation in a sea-
cage than possible through either measurements or model simulations
alone. This can in turn be used as a means for decision support to
ensure that cage management practices or operations do not lead to the
fish being too exposed to hypoxic conditions. One example where this
could be applied is feeding, as feeding activity is a key factor behind
both the consumption of and requirement for oxygen in fish (Forsberg,
1997). The farm used in the study by Alver et al. (2022) is equipped
with 16 individual feeding points, and in cases where oxygen levels
are low, it could be beneficial to suspend feeding or only deliver
feed through the feeding points that are upstream from the midpoint
of the cage to prevent feeding under sub-optimal oxygen conditions.

Digital Twins could also have a role in counteracting hypoxic situations
after they have arisen. Active oxygenation of an entire full-scale sea-
cage is unrealistic, as this would require oxygenation equipment of
a scale that is practically and economically unfeasible to use in a
production situation. The placement of the oxygenation diffusors used
by the industry must therefore be chosen with care. A Digital Twin
could predict the most strategic diffusor placement, and monitor the
impact of the operation so that the placement can be optimised. Such
Digital Twins would perhaps be even more relevant when considering
closed containment systems, a type of systems that comprises both land-
based recirculation aquaculture systems (RAS) and closed/semi-closed
marine systems. Since these are systems that are designed to operate
with little or no exchange of water with the surroundings, it is even
more crucial to maintain close control over the developments in oxygen
concentration and distribution inside the production system to avoid
unfavourable conditions.

4.2. Concept 2: fish growth in sea-cages

4.2.1. Background

The biomass is the most important parameter for fish farmers, as
it both conveys how they best can manage farm operations such as
feeding, and enables them to assess the future crop value. Estimating
the size distribution of the fish is also crucial for value assessment,
as the fish are sold not as a bulk but according to size classes. The
precision of such applications could be further improved if one was
able to also quantify the number of individual fish in the cage. Previous
studies have sought to explore how the current state-of-the-art can
be used to improve feeding efficiency in salmon farming. However,
a Digital Twin merging relevant mathematical models and real-time
data from available sensors and instruments could provide the means
to achieving a better overview of these parameters.

4.2.2. Knowledge based models

Føre et al. (2016) (Fig. 7d) sought to simulate the growth process
in full-scale sea-cages by combining a behavioural model (Føre et al.,
2009) with an energetic model (Kooijman, 2000) and a feed distribu-
tion model (Fig. 7c, Alver et al., 2016). While the model was originally
developed for simulating Atlantic salmon, its modular design allowed
for easy adaptation to other species by adapting the behavioural and/or
energetic modules to other species (e.g., Stavrakidis-Zachou et al.,
2019). The model was run using the feed delivery regime and envi-
ronmental data series measured at the site during a long term growth
experiment as input. Its outputs in the form of growth data were
then compared with growth data collected through periodic manual
samples and automated measurements using a biomass frame. The
model proved able to track the growth of the fish relatively closely
in the first half of the experiment, implying that it captured most of
the growth dynamics for salmon under normal conditions. However,
midway through the experiment, the fish contracted Pancreas Disease
(PD), the effect of which was clearly seen as a reduction in growth. The
model was not able to predict the growth accurately in this period,
and since it operated with the same feeding rates and environmental
conditions as at the experimental site, this deviation probably arose
because the model had no means of representing the effects of disease.
While it is unclear if this growth deficit was due to reduced feed intake
or a direct physiological response in the fish, expanding the model
with the ability to simulate how pathogens or parasites affect fish
growth would add to the realism of the model and hence an eventual
digital twin based upon it. These models cover most of the important
components to represent fish growth and typically rely on a limited
number of forcing variables such as temperature and feeding regime.
Their accuracy could be improved by including more detailed models
of the environment such as dissolved oxygen (Alver et al., 2022), pH,
salinity, turbidity and water currents, and how the fish respond to
these.

ComputersandElectronicsinAgriculture218(2024)10867612M. Føre et al.

Fig. 7. Components that could be components in a Digital Twin aimed at concept 2. (a) computer vision methods to automatically estimate surface distribution of pellets (right)
by analysing aerial photos of the cage surface (left) (Reproduced with permission from Lien et al., 2019); (b) telemetry methods to measure individual fish depth movements
before, during and after feeding period (marked by grey bars) (Reproduced with permission from Føre et al., 2011); (c) advection–diffusion models for simulating the distribution
of feed pellets in the cage volume (Reproduced with permission from Alver et al., 2016); (d) growth models able to estimate and predict individual fish growth (Reproduced with
permission from Føre et al., 2016).

4.2.3. Real-time data collection

4.2.4. Data-driven models

The automated data sources used in the original study (i.e., feeding
signals, environmental sensors, biomass frames) would probably be
useful when designing the Digital Twin. Additional insight could be
obtained by using behavioural data from devices such as cameras (e.g.,
An et al., 2021), echo sounders (e.g., Bjordal et al., 2020) or teleme-
try (Fig. 7b, e.g., Føre et al., 2011) to tune or correct the feeding
behaviour of the fish. From a holistic point of view, echo sounders could
also have a potential in providing data describing the total biomass in
the system and how this biomass is spatially distributed. This would
require that the device could observe the entire cage volume, and
more refined technologies/processing methods than extant today, but
could become a reality in the future due to ongoing developments
within both hydroacoustic technologies and use of these in cages.
Precision could be further improved by expanding these setups, by
e.g., measuring environmental data with a higher spatial resolution
or trying to better quantify feed distribution (Fig. 7a, e.g.,
Lien
et al., 2019) and loss (e.g., Skøien et al., 2014). The data on fish
sizes could probably likewise be improved by increased resolution,
e.g., by placing several biomass frames/sensors at different depths or
using stereoscopic camera systems (Voskakis et al., 2021). This could
potentially compensate for eventual measurement errors due to size-
dependent vertical stratification in the fish distribution, as has been
observed in salmon cages (Folkedal et al., 2012). Moreover, since
elevated and/or prolonged swimming activity may have impacts on
fish growth (Waldrop et al., 2018; Hvas et al., 2021), data describing
the water movements induced by currents and waves would be useful
inputs for better predicting fish growth in sea-cages. Such data would
be particularly interesting for operations in more exposed and ener-
getic environments (Bjelland et al., 2015; Jónsdóttir et al., 2019), and
can be collected by a wide variety of commercially available devices
(e.g., Acoustic Doppler Current Profilers, Acoustic Wave And Current
Profilers).

Fish farming companies and fish feed producers routinely run feed-
ing trials and experiments to e.g., explore new feed types, resulting in
datasets describing both the weight development and the driving fac-
tors behind this process over time. Such datasets are usually restricted
from public access as they may feature information that can divulge the
effects of e.g., feed composition or feed delivery methods on growth
and hence profitability that are proprietary to the owner of the data.
However, if these data were made sufficiently anonymous and cleaned
of eventual details that could reveal company secrets, and then were
made available for science, they could be a foundation for developing
accurate data-driven models of fish growth that could be used as a
component in a Digital Twin aimed at fish growth (Aunsmo et al.,
2014). Data-driven models could also serve a purpose in providing a
means for modelling features not captured by the knowledge based
growth models such as disease effects. One of the main shortcomings of
the model used in the original study was its inability to represent the
growth effects induced by the onset of disease. Using the dataset that
describes the difference between the expected (i.e., model predictions)
and actual (i.e., growth measurements) growth in that trial, it could
be possible to set up and train a data driven model able to predict the
effects of PD on fish growth. If similarly detailed growth data could
also be collected for cases where fish are subject to other disease and
parasite outbreaks, repeating this exercise could result in a collection
of data driven models able to predict the effects of such events on fish
growth. Such models would also be useful and interesting results in
themselves.

4.2.5. Module integration

Since the instruments required to achieve a minimum of data cov-
erage for this case are mostly commercial products that often feature
interfaces for external communication, their integration with models
would mainly entail a setup of reliable communication channels for
transferring their data to databases available to the simulation models
and assimilation schemes. Data driven models of disease effects could

ComputersandElectronicsinAgriculture218(2024)10867613M. Føre et al.

Fig. 8. Case 3: An example of an advanced starting point for a full Digital Twin for in-cage robotics and vehicle operations (SINTEF, 2023). This example showcases various
components of a Digital Twin application, including a description of the setup of sensors for monitoring the fish (upper left) and the cage structure and physical conditions (upper
right), an online digital rendition of the situation in the cage (lower left), and data histories from instruments over time (lower right).

potentially be implemented as a module in the knowledge based growth
model to account for such effects. In its most basic form, this could
be done by simply scaling the growth rate of the fish directly in
accordance with the output from the model. Although this approach
could be sufficient to compensate for the shortcomings of the mathe-
matical model on this area, it would not reveal the specific reason for
the growth reduction during disease outbreaks. This could potentially
be explored further by trying to identify what specific mechanisms
(e.g., reduced appetite, increased energy expenditure) in the growth
process are actually causing the growth deficit seen during disease.
Ideally, this endeavour would entail conducting specific laboratory and
field experiments on pathogen–host interactions and disease effects
on metabolism to unravel the biochemical pathways that explain the
observed growth deficit. In turn, this could contribute to the integration
of these mechanisms into the growth models by the addition of disease-
related knowledge based modules or the adjustment of appropriate
model parameters. Considering the theoretical and practical challenges,
such as data availability, in developing truly knowledge based models
for diseases, one possible indirect way to include such effects could
be to run simulations with the knowledge based model where the
growth reduction is introduced through different model components.
For instance, such effects could be introduced as reduced feed intake or
direct reduction in metabolism due to increased energetic maintenance
needs related to the immune response of the fish rather than as a
direct factor on growth rate. Although this is a manual approach that
would not transform the data driven model entirely into a knowledge
based representation, it could be a step towards better understanding
the growth dynamics in fish. Devising a human–machine interface that
presents the estimated growth data in a good manner to the user would
finalise this Digital Twin. This interface could possibly also contain
options for visualising the growth together with chosen features of the
production environment such that the user can highlight relationships
between these and the growth.

4.2.6. Industrial applications

A Digital Twin describing fish growth in sea-cages could foremost
provide the farmer with a better overview of the properties of the

biomass and its daily development, which is important information
when assessing feeding efficiency and the effects of environmental
conditions, as well as planning of the future marketing of the fish.
This information can also be crucial from a decision support viewpoint,
as knowing the total biomass and size distribution in a cage can be
important both in determining a suitable feeding plan and for critical
operations such as crowding. Moreover, in predicting the expected
growth rate and being able to compare this with real-time data, the
Digital Twin could also provide a method for early detection and
warning of undetected disease outbreaks and other unwanted effects.
If the model is also equipped with models that account for the effects
of different diseases/parasites, it could even potentially suggest the
specific cause behind the growth reduction. Finally, if the Digital Twin
is properly validated against real situations, it could also be used to
close the loop of cage-based fish production. By providing feedback
control signals on growth and spatial feed distribution, one could ac-
tively control farm management operations such as feeding. This would
be a step towards enabling fish farms to operate autonomously without
human intervention, a feature that could be particularly beneficial
for farming operations at more exposed sites (Bjelland et al., 2015).
Although this may lie some years further into the future than the other
potential applications, a similar approach has previously been used for
autonomous control of rotifer cultures (Alver et al., 2010).

4.3. Concept 3: in-cage robotics and vehicle operations

4.3.1. Background

More extensive use of advanced robotics in industrial production is
an important step in achieving the automation aims proposed in the
Industry 4.0 paradigm (Vaidya et al., 2018). This notion has also been
transferred to the aquaculture industry, where there is an increasing
interest in using robotics to replace manual labour, particularly for
Dull, Dirty, Dangerous, Distant and Dear (5 D’s) jobs. Such jobs are
even more challenging at more exposed or offshore locations, where
there is also a higher demand for robotics and automation as human
presence is more difficult due to the harsher environmental condi-
tions (Bjelland et al., 2015). Digital Twins seeking to mimic robotics

ComputersandElectronicsinAgriculture218(2024)10867614M. Føre et al.

operations in flexible sea-cages can prove to be key components in
developing and testing operations with remote piloted/unmanned ve-
hicles and/or robotic manipulators (e.g., net inspections with an ROV,
as shown in Fig. 8). The use of robotic platforms for autonomous and
continuous high-quality data collection in sea-cages has been explored
by Rundtop and Frank (2016) and Kelasidi et al. (2022) through full
scale trials studying in-cage navigation with an ROV using different
sensor solutions, and by Livanos et al. (2018) in a simpler approach
using off-the-shelf equipment while developing appropriate algorithms.
This type of research has been stimulated by currently increasing
industrial trends on adapting robotic solutions to aquaculture, and
investigating their autonomous capabilities in relevant applications in
sea-based and land-based fish farms. The relevance of this research
and potential industrial applications of robotic system were recently
reviewed by Kelasidi and Svendsen (2022). Expanding this study with
knowledge based and data driven models would introduce predictive
powers and utilise existing knowledge, representing a solid foundation
for developing a Digital Twin for this case.

4.3.2. Knowledge based models

In addition to describing the vehicle dynamics (e.g., Ohrem et al.,
2021), a mathematical model base for a Digital Twin for this purpose
would need to define several aspects of the spatial dynamics facing a
vehicle or robot inside a cage. This includes the cage structure (e.g.,
Moe et al., 2010; Kristiansen and Faltinsen, 2015) and its interactions
with the environment (e.g., Klebert and Su, 2020), as well as the move-
ments of the fish (e.g., Føre et al., 2009). Su et al. (2019) synthesised
all these elements (i.e., marine environment, fish, cage and vehicle
operations) by using a module based modelling framework (Reite et al.,
2014). Although the resulting model could be used to simulate the
spatial dynamics in a sea-cage, there are still limitations related to its
ability to reflect the full system dynamics. While some of these are
possible to derive from existing knowledge, other aspects are less well-
known by science and hence difficult to model. One such aspect is
how fish respond to the presence and movements of a vehicle or robot,
which is a key question to answer before one can fully exchange human
intervention with robotics at fish farms (Kruusmaa et al., 2020).

4.3.3. Real-time data collection

The most essential real-time element needed for this application is
the ability to detect the position and movement of the vehicle, and
its proximity to other objects in the cage. Ultra Short Baseline (USBL)
and Doppler Velocity Log (DVL) devices were tested for this purpose
by Rundtop and Frank (2016) and Amundsen et al. (2022), and are
suitable candidates for the future development of a Digital Twin. Such
systems could also be complemented by pressure sensors, providing
a better estimate of depth, and current (ADCP) or wave profilers
(AWAC) to assess hydrodynamics and hydraulics at the site. Acoustic
positioning systems could also be used to measure the positions and
velocities of structural components at the farm, and could in combi-
nation with mathematical models, even estimate the deformations of
flexible components like net structures (Su et al., 2021). Recent studies
have also shown that it is possible to utilise autonomous underwater
vehicles (Kelasidi et al., 2022) to collect data for in-cage navigation
through camera based solutions (Schellewald et al., 2021). Cameras can
also be used to automatically collect data on biofouling levels (Gansel
et al., 2017), and fish behaviour/movements (e.g., Saberioon et al.,
2017; Måløy et al., 2019), which would be useful for assessing the
structural motions/deformations and fish distributions, respectively.
Moreover, acoustic devices such as echo sounders or sonars would be
useful sources of information on fish distribution and movement, and
could be fitted onto the vehicles.

4.3.4. Data-driven models

Assuming that vehicle position and movement is known, and that
the vehicle has some method of quantifying the movements of nearby
fish, it could be possible to design a data driven model able to predict
fish responses based on vehicle motions. This could eventually be
complemented with Guidance Navigation and Control (GNC) data (Fos-
sen, 1999) from the vehicle to also analyse if accelerations have an
effect, and fish data from auxiliary systems such as stationary sonars.
Extension of vehicle models themselves and/or adaptation of hybrid
type of methods incorporating structure and fish models (e.g., reaching
the formulation of fish–machine interaction concept) could also benefit
farm automation through Digital Twin concepts.

4.3.5. Module integration

A setup such as the one used by Su et al. (2021) could repre-
sent a starting point for developing a Digital Twin in this field (see
e.g., Fig. 8). As for the other two cases, this would require enabling
the real-time transfer of data from the cage to the model, which would
mainly be a technical task (e.g., based on the emerging IoT tech-
nologies). Furthermore, the system model would need to be expanded
with models of the vehicle and the fish at the site, and potentially
be equipped with possibilities for dynamic model adjustments based
on measurements of e.g., fouling level and current speeds. A data
driven model able to predict fish responses to vehicle manoeuvres
could be incorporated as a distinct module in the fish model, and
be used to perturb the fish behaviour accordingly when a vehicle is
nearby. However, if sufficient data could be collected on this aspect,
the data driven model could also be used to derive a knowledge
based mathematical model of this particular dynamics. This could be
done by running simulations of the cases for which there is data, and
experiments with various parameter settings to see if it is possible to
reproduce the responses. Under the assumption that the simulated fish
have a similar set of perception abilities as real fish, this could result
in a better understanding in how fish perceive and respond to vehicles
in the cage. These elements could then be linked with an interface
providing a view of the outputs form the navigation system, sensors,
cameras and models.

4.3.6. Industrial applications

A Digital Twin able to reflect the kinematics and dynamics of
vehicle operations within a sea-cage could represent a means for an
operator to have a better overview of the situation in the cage while
conducting real operations. This can be of great help when operating
the vehicle, as it would then be easier to orient and conduct operations
more precisely, and possibly preempt and avoid unwanted events such
as collisions with the net or fish. The Digital Twin could also be
used as a basis for a simulator system for training personnel in using
underwater vehicles/robots at fish farms. Candidates could then exploit
the predictive powers of the models featured in the Digital Twin, and
conduct the preliminary stages of training in a purely virtual environ-
ment, thereby both reducing the risk and cost at training new operators.
As an extension of this, a Digital Twin within this sphere could also be
used as a virtual laboratory to test new control approaches in a realistic,
albeit purely digital environment. This would allow developing and
testing methods/approaches considered too risky to prototype and test
in real fish farms, and could hence expand the control system toolbox
available for automating fish farm operations. Although this application
would only use the simulator part of the Digital Twin, it illustrates that
this technology could also be crucial tools in developing the methods
needed to enable unmanned fish farm operations in the future.

ComputersandElectronicsinAgriculture218(2024)10867615M. Føre et al.

5. Conclusion and future work

5.1. Digital twins in aquaculture: More fish on the double or double the
trouble?

Digital Twin technology has arisen to become a key enabling tech-
nology in the realisation of the aims of the Industry 4.0 paradigm
of increased digitisation and smarter automation. Several industrial
(e.g., manufacturing, process technology, transportation, energy pro-
duction) and societal (e.g., health care, meteorology, education) seg-
ments are already using Digital Twins (Rasheed et al., 2020). However,
there is still a vast potential in the application of this technology to
new areas, particularly where there are applications that require the
combination of models and data streams founded in different scientific
disciplines. The marine environment is one such area, and several
bodies including the European Research Council (ERC) have recently
highlighted the development of Digital Twins of the ocean as a key
strategic research direction. This has spawned several ongoing research
activities aiming to build Digital Twins of the oceans or parts of the
ocean by e.g., combining real-time marine and maritime data with
oceanographic models. However, although most applications within
aquaculture are inherently of a trans-disciplinary nature, there have
been few attempts at developing complete Digital Twin solutions for
aquaculture purposes. We therefore set out to examine the potential
of developing Digital Twins for this sector in light of the current
state-of-the-art and probable future developments.

One important aspect we did not cover in detail in the case studies is
the digitisation footprint of the proposed applications, which refers to
the assessment of the data storage requirements of applications within
digitisation in agriculture (Marinello et al., 2019). This concept has
recently been used to explore the development in storage requirements
for a 22 ha field over two decades, and how this is expected to develop
in the future (Kayad et al., 2022). Similar considerations will also
be needed for aquaculture applications for the industry to assess the
technical requirements for storage capacity (and possibly processing
power) associated with running a Digital Twin for a farming site. It
would then make sense to consider the digitisation footprint per unit
weight produced (e.g., per tonne) rather than per unit area, as the
production yield in aquaculture is less tightly linked with area than
in agriculture. At present, the level of development within Digital
Twins for aquaculture is too immature, and the industrial application
of such solutions too sparse, to conduct assessments at a similar level
of detail as Kayad et al. (2022). However, it is possible to make some
general approximations based on the components required for such
solutions. The mathematical models proposed in the three case studies
would contribute to the digitisation footprint as they would require
both storage space and memory when continuously running, and the
scale of this requirement depends on the model type. For instance, the
requirements for individual based models would mainly depend on the
number of individuals simulated, while the footprint of Eulerian type
models (such as feed distribution and oxygen models) would mainly
depend on the spatial extent and resolution of the modelled area.
This implies that a trade-off between the extent of the digitisation
footprint and the fidelity of the models would be a necessary element
in the design of a Digital Twin for aquaculture. The data collection
schemes proposed in the case studies would likewise contribute to the
footprint as some monitoring methods such as active acoustics and
camera based solutions tend to generate large amounts of data (often
several gigabytes per day, depending on sampling frequency). However,
this footprint could be severely reduced by processing and interpreting
the data before storage and use in the Digital Twin. For instance,
storing time series describing e.g., the spatial distribution with a lower
resolution in time and space than that used by the echo sounders
rather than raw acoustic data would reduce the data size by orders of
magnitude. Similarly, time series describing e.g., the swimming speed
or wound frequency over time derived using computer vision would

require significantly lower storage space than raw camera footage. Such
pre-processing before storage and assimilation into the Digital Twin
would also reduce the load on the communication channel between the
farm and the Digital Twin. Moreover, storing and using processed data
from such sources also makes more sense from a practical perspective,
as raw data would be harder and less useful to assimilate into the
Digital Twin than interpretations of these data that contain information
about core aspects in the dynamics described by the Digital Twin.

To conclude this segment, we review the research questions posed

initially in this study:

Research question 1.
: by reviewing similar initiatives in other sectors,
the approach described in Section 2 seems like a promising candidate
for implementing a Digital Twin for aquaculture purposes. The selection
of components required and the capability levels identified for the
chosen approach appears to be sufficient to fulfil the potential roles
of a Digital Twin in aquaculture. This is further illustrated through the
case studies in Section 4 as these illustrate how Digital Twin technology
can be used to address concrete industrial challenges.

Research question 2.
: the current state of the art contains several of
the components needed to reach the goal of achieving a Digital Twin
for aquaculture. As highlighted in the literature surveys presented in
Section 3, there exist several sensor technologies and instruments for
acquiring data from fish in aquaculture. While some of these have yet
to be applied to aquaculture, their proof of concept for fish in other
settings (e.g., wild fish, fisheries) show that they can be used to provide
insights into the dynamics of farmed fish. We also identified several
knowledge based models describing various aspects of the processes
in aquaculture facilities. While most of these models are standalone
in the sense that they do not combine aspects from different domains
(e.g., biology and structural dynamics), their integration is an ongoing
process as evident from recently published studies.

Research question 3.
: both the literature survey and the case studies
highlight that there are several knowledge gaps that need to be filled
before we can claim that a full fledged Digital Twin for aquaculture is
possible. However, some of these can possibly be patched temporarily
through the application of hybrid analysis methods where data driven
modelling approaches are used to fill in the gaps where knowledge
based models are not sufficient or do not have the sufficiently fidelity.

Research question 4.
: the case studies presented in Section 4 de-
scribe potential pathways toward creating Digital Twins for aqua-
culture. While these do not cover all potential application areas for
Digital Twins in aquaculture, our intention was to provide a relevant
subset of such applications to illustrate how it could be done. The
approach we used to explore the case studies can also be considered a
possible first step in developing Digital Twins for specific applications
in aquaculture. By systematically identifying existing components and
knowledge gaps before starting Digital Twin development, it is likely
that the outcome will become more valuable in the end.

5.2. The way onward

A natural track for the way onward in the realisation of Digital
Twin technology in aquaculture will be to focus on the knowledge
gaps identified above, i.e., the development of missing components,
integration of components, and continued validation of these to ensure
sufficient fidelity. This suggests that the path towards achieving Digital
Twins in aquaculture will be incremental rather than disruptive, in that
we can build new solutions on past results and achievements. In parallel
with these scientific advances, new innovations in aquaculture tech-
nology utilise and build on such results. These industrial developments
will likely support further research by raising the industry’s awareness
and interest in the approach and providing richer datasets through
improved and more comprehensive sensor use. Since most research and
innovation processes are incremental by nature, a shift to focusing on

ComputersandElectronicsinAgriculture218(2024)10867616M. Føre et al.

Digital Twin development is therefore unlikely to entail a substantial
change in how these processes are conducted in science and industry.
This is also reflected in the three concrete concepts we highlight in
this study, as most of the components proposed for the Digital Twins
in those areas already exist in some form. The concepts also illustrate
some potential industrial benefits to introducing Digital Twins in these
areas, and it is clear that similar benefits could be achieved in other
areas within aquaculture. However, it is also important to keep in mind
that the three case studies presented here mostly rely upon the abilities
of Digital Twins considered to be at the predictive capability level. With
time, it is likely that needs for Digital Twins at higher capability levels
be required also in aquaculture, e.g., to achieve autonomous production
in areas and situations that render human presence at the farm difficult.
The main conclusion of this study is that the technological level
within aquaculture is sufficiently high to warrant starting the work
on adapting Digital Twins. Furthermore, given the potential benefits,
this is a path the scientific community and industry alike should start
following. This requires that research and development processes are
adjusted to not only focus on their specific goals, but also on how the
outcomes will fit in a holistic Digital Twin solution down the line. If
we can integrate this vision into the future of research and innovation
in aquaculture, it is likely that the future will see us able to harvest the
benefits of Digital Twin technology also within this sector.

CRediT authorship contribution statement

Martin Føre: Writing – review & editing, Writing – original draft,
Project administration, Methodology, Investigation, Conceptualization.
Morten Omholt Alver: Writing – review & editing, Writing – original
draft, Investigation, Conceptualization. Jo Arve Alfredsen: Writing –
review & editing, Writing – original draft, Investigation. Adil Rasheed:
Writing – review & editing, Writing – original draft, Methodology,
Investigation, Conceptualization. Thor Hukkelås: Writing – review &
editing, Investigation. Hans V. Bjelland: Writing – review & edit-
ing, Investigation. Biao Su: Writing – review & editing, Investigation.
Sveinung J. Ohrem: Writing – review & editing, Investigation. Eleni
Kelasidi: Writing – review & editing, Investigation. Tomas Norton:
Writing – review & editing, Investigation, Conceptualization. Nikos
Papandroulakis: Writing – review & editing, Investigation.

Declaration of competing interest

This work has been conducted by the authors through their posi-
tions at their respective institutions and all funding used to cover the
expenses and time has been acquired from governmental agencies. We
declare that we have no economic interests, patents or copyrights that
are relevant for this publication.

Data availability

No data was used for the research described in the article.

Acknowledgements

Føre

Martin

from
Salmar ASA/Salmar Aker Ocean AS. This work was partly funded by
the Research Council of Norway (RCN) project: CHANGE (no. 313737).

acknowledges

financial

support

the

References

Abdel-Tawwab, M., Monier, M.N., Hoseinifar, S.H., Faggio, C., 2019. Fish response to
hypoxia stress: growth, physiological, and immunological biomarkers. Fish Physiol.
Biochem. 45 (3), 997–1013.

Ahmed, A., Zulfiqar, S., Ghandar, A., Chen, Y., Hanai, M., Theodoropoulos, G.,
2019. Digital twin technology for aquaponics: Towards optimizing food production
with dynamic data driven application systems. In: Asian Simulation Conference.
Springer, pp. 3–14.

Alver, M.O., Alfredsen, J.A., Øie, G., Storøy, W., Olsen, Y., 2010. Automatic control of

growth and density in rotifer cultures. Aquac. Eng. 43 (1), 6–13.

Alver, M.O., Alfredsen, J.A., Olsen, Y., 2006. An individual-based population model for

rotifer (Brachionus plicatilis) cultures. Hydrobiologia 560 (1), 93–108.

Alver, M.O., Alfredsen, J.A., Sigholt, T., 2004. Dynamic modelling of pellet distribution

in Atlantic salmon (Salmo salar L.) cages. Aquacult. Eng. 31, 51–72.

Alver, M.O., Føre, M., Alfredsen, J.A., 2022. Predicting oxygen levels in Atlantic salmon

(Salmo salar) sea cages. Aquaculture 548, 737720.

Alver, M.O., Føre, M., Alfredsen, J.A., 2023. Effect of cage size on oxygen levels
in Atlantic salmon sea cages: A model study. Aquaculture 562, 738831. http:
//dx.doi.org/10.1016/j.aquaculture.2022.738831.

Alver, M.O., Skøien, K.R., Føre, M., Aas, T.S., Oehme, M., Alfredsen, J.A., 2016.
Modelling of surface and 3D pellet distribution in Atlantic salmon (Salmo salar
L.) cages. Aquac. Eng. 72, 20–29.

Amundsen, H.B., Caharija, W., Pettersen, K.Y., 2022. Autonomous ROV inspections
of aquaculture net pens using DVL. IEEE J. Ocean. Eng. 47 (1), 1–19. http:
//dx.doi.org/10.1109/JOE.2021.3105285.

An, D., Hao, J., Wei, Y., Wang, Y., Yu, X., 2021. Application of computer vision
in fish intelligent feeding system—A review. Aquacult. Res. 52 (2), 423–437.
http://dx.doi.org/10.1111/are.14907.

Arrhenius, F., Benneheij, B.J., Rudstam, L.G., Boisclair, D., 2000. Can stationary bottom
split-beam hydroacoustics be used to measure fish swimming speed in situ? Fish.
Res. 45 (1), 31–41.

Aunsmo, A., Krontveit, R., Valle, P.S., Bohlin, J., 2014. Field validation of growth
models used in Atlantic salmon farming. Aquaculture 428–429, 249–257. http:
//dx.doi.org/10.1016/j.aquaculture.2014.03.007.

Balchen, J.G., 1979. Modeling, prediction, and control of fish behavior. In: Control and

Dynamic Systems, vol. 15, Elsevier, pp. 99–146.

Balchen, J.G., 2000. Thirty years of research on the application of cybernetic methods

in fisheries and aquaculture technology.

Berckmans, D., 2017. General introduction to precision livestock farming. Animal Front.

7 (1), 6–11. http://dx.doi.org/10.2527/af.2017.0102.

Berthelsen, K., 2017. Ocean Farm 1 becomes a floating laboratory. https://www.

fishfarmingexpert.com/article/ocean-farm-1-becomes-a-floating-laboratory/.
(Accessed 05 October 2021).

Bjelland, H.V., Føre, M., Lader, P., Kristiansen, D., Holmen,

I.M., Fredheim, A.,
Grøtli, E.I., Fathi, D.E., Oppedal, F., Utne, I.B., et al., 2015. Exposed aquaculture
in Norway. In: OCEANS 2015-MTS/IEEE Washington. IEEE, pp. 1–10.

Bjordal, Å., EJuell, J., Lindem, T., Fernö, A., 2020. Hydroacoustic monitoring and
feeding control in cage rearing of Atlantic salmon (Salmo salar L.). In: Fish Farming
Technology. CRC Press, pp. 203–208.

Björnsson, B., Steinarsson, A., Árnason, T., 2007. Growth model for Atlantic cod (Gadus
morhua): Effects of temperature and body weight on growth rate. Aquaculture 271
(1–4), 216–226.

Brijs, J., Føre, M., Gräns, A., Clark, T., Axelsson, M., Johansen, J., 2021. Bio-sensing
technologies in aquaculture: how remote monitoring can bring us closer to our
farm animals. Phil. Trans. R. Soc. B 376 (1830), 20200218.

Brijs, J., Sandblom, E., Axelsson, M., Sundell, K., Sundh, H., Huyben, D., Broström, R.,
Kiessling, A., Berg, C., Gräns, A., 2018. The final countdown: Continuous physi-
ological welfare evaluation of farmed fish during common aquaculture practices
before and during harvest. Aquaculture 495, 903–911. http://dx.doi.org/10.1016/
j.aquaculture.2018.06.081.

Brijs, J., Sandblom, E., Axelsson, M., Sundell, K., Sundh, H., Kiessling, A., Berg, C.,
Gräns, A., 2019. Remote physiological monitoring provides unique insights on
the cardiovascular performance and stress responses of freely swimming rainbow
trout in aquaculture. Sci. Rep. 9 (1), 9090. http://dx.doi.org/10.1038/s41598-019-
45657-3.

Broch, O.J., Klebert, P., Michelsen, F.A., Alver, M.O., 2020. Multiscale modelling of
cage effects on the transport of effluents from open aquaculture systems. PLoS One
15 (3), e0228502.

Burke, M., Grant, J., Filgueira, R., Stone, T., 2021. Oceanographic processes control
dissolved oxygen variability at a commercial Atlantic salmon farm: Application of
a real-time sensor network. Aquaculture 533, 736143.

Chahid, A., N’Doye, I., Majoris, J.E., Berumen, M.L., Laleg-Kirati, T.M., 2022. Fish
growth trajectory tracking using Q-learning in precision aquaculture. Aquaculture
550, 737838. http://dx.doi.org/10.1016/j.aquaculture.2021.737838.

Chalikov, D., 1978. The numerical simulation of wind-wave interaction. J. Fluid Mech.

87 (3), 561–582.

Chatziantoniou, A., Charalampis Spondylidis, S., Stavrakidis-Zachou, O., Papan-
droulakis, N., Topouzelis, K., 2022. Dissolved oxygen estimation in aquaculture
sites using remote sensing and machine learning. Remote Sens. Appl. Soc. Environ.
28, 100865. http://dx.doi.org/10.1016/j.rsase.2022.100865.

Chen, Y., Jackson, D., Harvey, H., 1992. A comparison of von Bertalanffy and
polynomial functions in modelling fish growth data. Can. J. Fish. Aquat. Sci. 49
(6), 1228–1235.

Chen, L., Yang, X., Sun, C., Wang, Y., Xu, D., Zhou, C., 2020. Feed intake prediction
model for group fish using the MEA-BP neural network in intensive aquaculture.
Inf. Process. Agric. 7 (2), 261–271.

Chiariotti, P., Martarelli, M., Castellini, P., 2019. Acoustic beamforming for noise source
localization – Reviews, methodology and applications. Mech. Syst. Signal Process.
120, 422–448. http://dx.doi.org/10.1016/j.ymssp.2018.09.019.

ComputersandElectronicsinAgriculture218(2024)10867617M. Føre et al.

Cho, C.Y., Bureau, D.P., 1998. Development of bioenergetic models and the Fish-PrFEQ
software to estimate production, feeding ration and waste output in aquaculture.
Aquat. Living Resour. 11 (4), 199–210.

Georgopoulou, D.G., Fanouraki, E., Voskakis, D., Mitrizakis, N., Papandroulakis, N.,
2022. European seabass show variable responses in their group swimming features
after tag implantation. Front. Animal Sci. 3.

Cisar, P., Bekkozhayeva, D., Movchan, O., Saberioon, M., Schraml, R., 2021. Computer
vision based individual fish identification using skin dot pattern. Sci. Rep. 11 (1),
1–12.

Georgopoulou, D.G., Stavrakidis-Zachou, O., Mitrizakis, N., Papandroulakis, N.,
2021. Tracking and analysis of the movement behavior of European seabass
(Dicentrarchus Labrax) in aquaculture systems. Front. Animal Sci. 2.

Cotter, E., Polagye, B., 2020. Automatic classification of biological targets in a tidal
channel using a multibeam sonar. J. Atmos. Ocean. Technol. 37 (8), 1437–1455.
http://dx.doi.org/10.1175/JTECH-D-19-0222.1.

Ghandar, A., Ahmed, A., Zulfiqar, S., Hua, Z., Hanai, M., Theodoropoulos, G., 2021. A
decision support system for urban agriculture using digital twin: A case study with
aquaponics. IEEE Access 9, 35691–35708.

Cuenco, M.L., Stickney, R.R., Grant, W.E., 1985. Fish bioenergetics and growth in
aquaculture ponds: II. Effects of interactions among, size, temperature, dissolved
oxygen, unionized ammonia and food on growth of individual fish. Ecol. Model.
27 (3–4), 191–206.

Difford, G.F., Boison, S.A., Khaw, H.L., Gjerde, B., 2020. Validating non-invasive growth
measurements on individual Atlantic salmon in sea cages using diode frames.
Comput. Electron. Agric. 173, 105411.

DNV GL, 2021. Nautical Site

(NSIM). https://www.dnv.
com/services/nautical-site-information-models-nsim--86364. (Accessed 05 October
2021).

Information Models

Dong, G.H., Tang, M.F., Xu, T.J., Bi, C.W., Guo, W.J., 2019. Experimental analysis of
the hydrodynamic force on the net panel in wave. Appl. Ocean Res. 87, 233–246.
Dong, G.H., Xu, T.J., Zhao, Y.P., Li, Y.C., Gui, F.K., 2010. Numerical simulation of
hydrodynamic behavior of gravity cage in irregular waves. Aquac. Eng. 42 (2),
90–101.

Elfarri, E.M., Rasheed, A., San, O., 2023. Artificial intelligence-driven digital twin of
a modern house demonstrated in virtual reality. IEEE Access 11, 35035–35058.
http://dx.doi.org/10.1109/ACCESS.2023.3265191.

Endo, H., Wu, H., 2019. Biosensors for the assessment of fish health: A review. Fish.

Sci. 85 (4), 641–654. http://dx.doi.org/10.1007/s12562-019-01318-y.

Endresen, P.C., Føre, M., Fredheim, A., Kristiansen, D., Enerhaug, B., 2013. Numerical
modeling of wake effect on aquaculture nets. In: International Conference on
Offshore Mechanics and Arctic Engineering, Vol. 55355. American Society of
Mechanical Engineers, p. V003T05A027.

Erikson, U., Gansel, L., Frank, K., Svendsen, E., Digre, H., 2016. Crowding of Atlantic

salmon in net-pen before slaughter. Aquaculture 465, 395–400.

Evensen, G., et al., 2009. Data Assimilation: The Ensemble Kalman Filter, vol. 2,

Springer.

Hao, M., Yu, H., Li, D., 2015. The measurement of fish size by machine vision-a
review. In: International Conference on Computer and Computing Technologies in
Agriculture. Springer, pp. 15–32.

Hassan, W., Føre, M., Pedersen, M.O., Alfredsen, J.A., 2020. A new method for
measuring free-ranging fish swimming speed in commercial marine farms using
Doppler principle. IEEE Sens. J. 20 (17), 10220–10227. http://dx.doi.org/10.1109/
JSEN.2020.2991294.

Haugaløkken, B.O.A., Sandøy, S.S., Schjølberg, I., Alfredsen, J.A., Utne, I.B., 2018.
Probabilistic localization and mapping of
flexible underwater structures using
octomap. In: European Control Conference 2018. Limassol, Cyprus, Institute of
Electrical and Electronics Engineers (IEEE), pp. 268–275. http://dx.doi.org/10.
23919/ECC.2018.8550498.

Hvas, M., Folkedal, O., Oppedal, F., 2020. Heart rate bio-loggers as welfare indicators
in Atlantic salmon (Salmo Salar) aquaculture. Aquaculture 529, 735630. http:
//dx.doi.org/10.1016/j.aquaculture.2020.735630.

Hvas, M., Folkedal, O., Oppedal, F., 2021. Fish welfare in offshore salmon aquaculture.

Rev. Aquac. 13 (2), 836–852.

Iswari, N.M.S., Wella, Ranny, 2017. Fish freshness classification method based on fish
image using K-nearest neighbor. In: 2017 4th International Conference on New
Media Studies. CONMEDIA, pp. 87–91. http://dx.doi.org/10.1109/CONMEDIA.
2017.8266036.

Jepsen, N., Koed, A., Thorstad, E.B., Baras, E., 2002. Surgical implantation of telemetry
transmitters in fish: How much have we learned? Hydrobiologia 483 (1), 239–248.
http://dx.doi.org/10.1023/A:1021356302311.

Johansson, D., Ruohonen, K., Kiessling, A., Oppedal, F., Stiansen, J.E., Kelly, M.,
Juell, J.E., 2006. Effect of environmental factors on swimming depth preferences
of Atlantic salmon (Salmo salar L.) and temporal and spatial variations in oxygen
levels in sea cages at a fjord site. Aquaculture 254 (1–4), 594–605.

FAO, 2022. Food and Agriculture Organization of the United Nations: Aquaculture
production: quantities 1950–2019. Available from http://www.fao.org/fishery/en.
(Accessed 25 April 2022).

Jones, D., Snider, C., Nassehi, A., Yon, J., Hicks, B., 2020. Characterising the digital
twin: A systematic literature review. CIRP J. Manuf. Sci. Technol. 29, 36–52.
http://dx.doi.org/10.1016/j.cirpj.2020.02.002.

Folkedal, O., Stien, L.H., Nilsson, J., Torgersen, T., Fosseidengen, J.E., Oppedal, F.,
2012. Sea caged Atlantic salmon display size-dependent swimming depth. Aquat.
Living Resour. 25 (2), 143–149.

Jónsdóttir, K.E., Hvas, M., Alfredsen, J.A., Føre, M., Alver, M.O., Bjelland, H.V.,
Oppedal, F., 2019. Fish welfare based classification method of ocean current speeds
at aquaculture sites. Aquac. Environ. Interact. 11, 249–261.

Føre, M., Alfredsen, J.A., Gronningsater, A., 2011. Development of two telemetry-
based systems for monitoring the feeding behaviour of Atlantic Salmon (Salmo
Salar L.) in aquaculture sea-cages. Comput. Electron. Agric. 76 (2), 240–251.
http://dx.doi.org/10.1016/j.compag.2011.02.003.

Føre, M., Alver, M., Alfredsen, J.A., Marafioti, G., Senneset, G., Birkevold, J.,
Willumsen, F.V., Lange, G., Espmark, Å., Terjesen, B.F., 2016. Modelling growth
performance and feeding behaviour of Atlantic salmon (Salmo salar L.)
in
commercial-size aquaculture net pens: Model details and validation through
full-scale experiments. Aquaculture 464, 268–278.

Jopling, J.K., Pridgen, B.C., Yeung, S., 2021. Setting assessment standards for artificial
intelligence computer vision wound annotations. JAMA Netw. Open 4 (5), e217851.
Kasumyan, A., 2008. Sounds and sound production in fishes. J. Ichthyol. 48 (11),

981–1030.

Kayad, A., Sozzi, M., Paraforos, D.S., Rodrigues, Jr., F.A., Cohen, Y., Fountas, S.,
Francisco, M.J., Pezzuolo, A., Grigolato, S., Marinello, F., 2022. How many
gigabytes per hectare are available in the digital agriculture era? A digitization
footprint estimation. Comput. Electron. Agric. 198, 107080. http://dx.doi.org/10.
1016/j.compag.2022.107080.

Føre, M., Dempster, T., Alfredsen, J.A., Johansen, V., Johansson, D., 2009. Modelling
of Atlantic salmon (Salmo salar L.) behaviour in sea-cages: A Lagrangian approach.
Aquaculture 288, 196–204.

Kelasidi, E., Su, B., Caharija, W., Føre, M., Pedersen, M.O., Frank, K., 2022. Autonomous
monitoring and inspection operations with UUVs in fish farms. IFAC-PapersOnLine
55 (31), 401–408. http://dx.doi.org/10.1016/j.ifacol.2022.10.461.

Føre, M., Frank, K., Dempster, T., Alfredsen, J.A., Høy, E., 2017. Biomonitoring using
tagged sentinel fish and acoustic telemetry in commercial salmon aquaculture: A
feasibility study. Aquac. Eng. 78, 163–172. http://dx.doi.org/10.1016/j.aquaeng.
2017.07.004.

Føre, M., Frank, K., Norton, T., Svendsen, E., Alfredsen, J.A., Dempster, T., Eguiraun, H.,
Watson, W., Stahl, A., Sunde, L.M., Schellewald, C., Skøien, K.R., Alver, M.O.,
Berckmans, D., 2018. Precision fish farming: a new framework to improve
production in aquaculture. Biosyst. Eng. 173, 176–193.

Forsberg, O., 1997. The impact of varying feeding regimes on oxygen consumption and
excretion of carbon dioxide and nitrogen in post-smolt Atlantic salmon Salmo salar
L.. Aquacult. Res. 28 (1), 29–41.

Fossen, T.I., 1999. Guidance and Control of Ocean Vehicles (Doctors thesis). University
of Trondheim, Norway, Printed by John Wiley & Sons, Chichester, England, ISBN:
0 471 94113 1.

Fredriksson, D.W., DeCew, J.C., Tsukrov, I., Swift, M., Irish, J.D., 2007. Development
of large fish farm numerical modeling techniques with in situ mooring tension
comparisons. Aquac. Eng. 36 (2), 137–148.

Fredriksson, D.W., Swift, M.R., Irish, J.D., Tsukrov, I., Celikkol, B., 2003. Fish cage
and mooring system dynamics using physical and numerical models with field
measurements. Aquac. Eng. 27 (2), 117–146.

Gansel, L., Bloecher, N., Floerl, O., Guenther, J., 2017. Quantification of biofouling
on nets: a comparison of wet weight measurements and optical (image analysis)
methods. Aquac. Int. 25 (2), 679–692.

Kelasidi, E., Svendsen, E., 2022. Robotics for sea-based fish farming. In: Zhang, Q. (Ed.),
Encyclopedia of Smart Agriculture Technologies. Springer International Publishing,
Cham, pp. 1–20. http://dx.doi.org/10.1007/978-3-030-89123-7_202-1.

Klebert, P., Lader, P., Gansel, L., Oppedal, F., 2013. Hydrodynamic interactions on net

panel and aquaculture fish cages: A review. Ocean Eng. 58, 260–274.

Klebert, P., Su, B., 2020. Turbulence and flow field alterations inside a fish sea cage

and its wake. Appl. Ocean Res. 98, 102113.

Klebert, P., Volent, Z., Rosten, T., 2018. Measurement and simulation of the three-
dimensional flow pattern and particle removal efficiencies in a large floating closed
sea cage with multiple inlets and drains. Aquac. Eng. 80, 11–21.

Knudsen, F., Fosseidengen, J., Oppedal, F., Karlsen, Ø., Ona, E., 2004. Hydroacoustic
monitoring of fish in sea cages: target strength (TS) measurements on Atlantic
salmon (Salmo salar). Fisheries research 69 (2), 205–209.

Kolarevic, J., Aas-Hansen, Ø., Espmark, Å., Baeverfjord, G., Terjesen, B.F., Damsgård, B.,
2016. The use of acoustic acceleration transmitter tags for monitoring of Atlantic
Salmon swimming activity in recirculating aquaculture systems (RAS). Aquac. Eng.
72–73, 30–39. http://dx.doi.org/10.1016/j.aquaeng.2016.03.002.

Komarudin, M., Septama, H., Yulianti, T., Yudamson, A., Hendri, J., Arafat, M., 2021.
Multi node sensors for water quality monitoring towards precision aquaculture. In:
IOP Conference Series: Earth and Environmental Science, vol. 739, (no. 1), IOP
Publishing, 012026.

Kooijman, S.A.L.M., 2000. Dynamic Energy and Mass Budgets in Biological Systems.

Cambridge University Press.

Gansel, L.C., Oppedal, F., Birkevold, J., Tuene, S.A., 2018. Drag forces and deformation
of aquaculture cages—Full-scale towing tests in the field. Aquac. Eng. 81, 46–56.

Kristiansen, T., Faltinsen, O.M., 2015. Experimental and numerical study of an
aquaculture net cage with floater in waves and current. J. Fluids Struct. 54, 1–26.

ComputersandElectronicsinAgriculture218(2024)10867618M. Føre et al.

Kruusmaa, M., Gkliva, R., Tuhtan, J.A., Tuvikene, A., Alfredsen, J.A., 2020. Salmon
behavioural response to robots in an aquaculture sea cage. Royal Soc. Open Sci. 7
(3), 191220. http://dx.doi.org/10.1098/rsos.191220.

Lader, P., Dempster, T., Fredheim, A., Jensen, Ø., 2008. Current induced net deforma-
tions in full-scale sea-cages for Atlantic salmon (Salmo salar). Aquac. Eng. 38 (1),
52–65.

Lader, P., Kristiansen, D., Alver, M., Bjelland, H.V., Myrhaug, D., 2017. Classification
of aquaculture locations in Norway with respect to wind wave exposure. In:
International Conference on Offshore Mechanics and Arctic Engineering, Vol.
57724. American Society of Mechanical Engineers, p. V006T05A005.

Lien, A.M., Schellewald, C., Stahl, A., Frank, K., Skøien, K.R., Tjølsen, J.I., 2019.
Determining spatial feed distribution in sea cage aquaculture using an aerial camera
platform. Aquac. Eng. 87, 102018.

Lika, K., Papandroulakis, N., 2005. Modeling feeding processes: A test of a new model
for sea bream (Sparus Aurata) larvae. Can. J. Fish. Aquat. Sci. 62 (2), 425–435.
http://dx.doi.org/10.1139/f04-198.

Lima, A.C., Royer, E., Bolzonella, M., Pastres, R., 2022. Digital twins for land-based
aquaculture: A case study for rainbow trout (Oncorhynchus Mykiss). Open Res.
Eur. 2 (16), 16.

Livanos, G., Zervakis, M., Chalkiadakis, V., Moirogiorgou, K., Giakos, G., Papan-
droulakis, N., 2018. Intelligent navigation and control of a prototype autonomous
underwater vehicle for automated inspection of aquaculture net pen cages. In: 2018
IEEE International Conference on Imaging Systems and Techniques. IST, IEEE, pp.
1–6.

Løland, G., 1993. Current forces on, and water flow through and around, floating fish

farms. Aquac. Int. 1 (1), 72–89.

Macaulay, G., Warren-Myers, F., Barrett, L.T., Oppedal, F., Føre, M., Dempster, T.,
2021. Tag use to monitor fish behaviour in aquaculture: A review of benefits,
problems and solutions. Rev. Aquac. 13 (3), 1565–1582. http://dx.doi.org/10.
1111/raq.12534.

Neethirajan, S., Kemp, B., 2021. Digital livestock farming. Sens. Bio-Sens. Res. 32,

100408.

Nichols, D., Hogan, T., 2022. Remote sensing technologies to monitor harmful algal

blooms in offshore aquaculture. World Aquac. 21.

Nisbet, R.M., Jusup, M., Klanjscek, T., Pecquerie, L., 2012. Integrating dynamic energy
budget (DEB) theory with traditional bioenergetic models. J. Exp. Biol. 215 (6),
892–902.

Nobre, A.M., Valente, L.M., Conceição, L., Severino, R., Lupatsch, I., 2019. A bioen-
ergetic and protein flux model to simulate fish growth in commercial farms:
Application to the gilthead seabream. Aquac. Eng. 84, 12–22.

O’Donncha, F., Grant, J., 2019. Precision aquaculture. IEEE Internet Things Mag. 2 (4),

26–30. http://dx.doi.org/10.1109/IOTM.0001.1900033.

Ohrem, S.J., Amundsen, H.B., Kelasidi, E., 2021. Control-oriented modeling of an
underwater biofouling prevention robot. In: 2021 20th International Conference
on Advanced Robotics. ICAR, IEEE, pp. 1121–1128.

Oppedal, F., Bui, S., Stien, L.H., Overton, K., Dempster, T., 2019. Snorkel technology
to reduce sea lice infestations: Efficacy depends on salinity at the farm site, but
snorkels have minimal effects on salmon production and welfare. Aquac. Environ.
Interact. 11, 445–457. http://dx.doi.org/10.3354/aei00321.

Oppedal, F., Dempster, T., Stien, L.H., 2011. Environmental drivers of Atlantic salmon
behaviour in sea-cages: A review. Aquaculture 311 (1), 1–18. http://dx.doi.org/10.
1016/j.aquaculture.2010.11.020.

Oppedal, F., Juell, J.E., Tarranger, G., Hansen, T., 2001. Artificial light and season
affects vertical distribution and swimming behaviour of post-smolt Atlantic salmon
in sea cages. J. Fish Biol. 58 (6), 1570–1584.

Ouyang, B., Wills, P.S., Tang, Y., Hallstrom, J.O., Su, T.C., Namuduri, K., Mukherjee, S.,
Rodriguez-Labra, J.I., Li, Y., Den Ouden, C.J., 2021. Initial development of the
Hybrid Aerial Underwater Robotic System (HAUCS): Internet of Things (IoT) for
aquaculture farms. IEEE Internet Things J. 8 (18), 14013–14027. http://dx.doi.org/
10.1109/JIOT.2021.3068571.

Madshaven, A., Schellewald, C., Stahl, A., 2022. Hole detection in aquaculture net cages
from video footage. In: Fourteenth International Conference on Machine Vision, Vol.
12084. ICMV 2021, SPIE, pp. 258–267.

Palaiokostas, C., 2021. Predicting for disease resistance in aquaculture species using
machine learning models. Aquac. Rep. 20, 100660. http://dx.doi.org/10.1016/j.
aqrep.2021.100660.

Måløy, H., 2020. EchoBERT: A transformer-based approach for behavior detection in

echograms. IEEE Access 8, 218372–218385.

Måløy, H., Aamodt, A., Misimi, E., 2019. A spatio-temporal recurrent network for
salmon feeding action recognition from underwater videos in aquaculture. Comput.
Electron. Agric. 167, 105087.

Marinello, F., Bramley, R., Cohen, Y., Fountas, S., Guo, H., Karkee, M., Martínez-
Casasnovas, J., Paraforos, D., Sartori, L., Sorensen, C., et al., 2019. Agriculture
and digital sustainability: a digitization footprint. In: Precision Agriculture’19.
Wageningen Academic Publishers, pp. 4–18.

Mathisen, B.M., Bach, K., Aamodt, A., 2021. Using extended siamese networks to pro-
vide decision support in aquaculture operations. Appl. Intell. 51 (11), 8107–8118.
http://dx.doi.org/10.1007/s10489-021-02251-3.

Mathisen, B.M., Haro, P., Hanssen, B., Björk, S., Walderhaug, S., 2016. Decision
support systems in fisheries and aquaculture: A systematic review. arXiv preprint
arXiv:1611.08374.

McIntosh, P., Barrett, L.T., Warren-Myers, F., Coates, A., Macaulay, G., Szetey, A.,
Robinson, N., White, C., Samsing, F., Oppedal, F., Folkedal, O., Klebert, P.,
Dempster, T., 2022. Supersizing salmon farms in the coastal zone: A global analysis
of changes in farm technology and location from 2005 to 2020. Aquaculture 553,
738046. http://dx.doi.org/10.1016/j.aquaculture.2022.738046.

Medaas, C., Lien, M.E., Gismervik, K., Kristiansen, T.S., Osmundsen, T., Størkersen, K.V.,
Tørud, B., Stien, L.H., 2021. Minding the gaps in fish welfare: The untapped
potential of fish farm workers. J. Agric. Environ. Ethics 34 (5), 29. http://dx.doi.
org/10.1007/s10806-021-09869-w.

Michelsen, F.A., Klebert, P., Broch, O.J., Alver, M.O., 2019. Impacts of fish farm
structures with biomass on water currents: A case study from Frøya. J. Sea Res.
154, 101806.

Moe, H., Fredheim, A., Hopperstad, O.S., 2010. Structural analysis of aquaculture net

cages in current. J. Fluids Struct. 26 (3), 503–516.

Moe-Føre, H., Lader, P., Lien, E., Hopperstad, O., 2016. Structural response of high

solidity net cage models in uniform flow. J. Fluids Struct. 65, 180–195.

Moe Føre, H., Thorvaldsen, T., 2021. Causal analysis of escape of Atlantic salmon and
rainbow trout from Norwegian fish farms during 2010–2018. Aquaculture 532,
736002. http://dx.doi.org/10.1016/j.aquaculture.2020.736002.

Moe Føre, H., Thorvaldsen, T., Osmundsen, T.C., Asche, F., Tveterås, R., Fagertun, J.T.,
Bjelland, H.V., 2022. Technological
innovations promoting sustainable salmon
(Salmo Salar) aquaculture in Norway. Aquac. Rep. 24, 101115. http://dx.doi.org/
10.1016/j.aqrep.2022.101115.

Moore, A.M., Arango, H.G., Broquet, G., Powell, B.S., Weaver, A.T., Zavala-Garay, J.,
2011. The Regional Ocean Modeling System (ROMS) 4-dimensional variational data
assimilation systems: Part I–System overview and formulation. Prog. Oceanogr. 91
(1), 34–49.

Morro, B., Davidson, K., Adams, T.P., Falconer, L., Holloway, M., Dale, A., Aleynik, D.,
Thies, P.R., Khalid, F., Hardwick, J., et al., 2022. Offshore aquaculture of finfish:
Big expectations at sea. Rev. Aquac. 14 (2), 791–815. http://dx.doi.org/10.1111/
raq.12625.

Palomares, M.L., Pauly, D., 1989. A multiple regression model for prediction the food
consumption of marine fish populations. Mar. Freshwater Res. 40 (3), 259–273.
http://dx.doi.org/10.1071/mf9890259.

Papandroulakis, N., Thomsen, C., Mintenbeck, K., Mayorga, P., Hernández-Brito, J.J.,
2017. The EU-project ‘‘TROPOS’’. In: Aquaculture Perspective of Multi-Use Sites in
the Open Ocean: The Untapped Potential for Marine Resources in the Anthropocene.
Springer International Publishing, pp. 355–374.

Pylianidis, C., Osinga, S., Athanasiadis, I.N., 2021. Introducing digital twins to agricul-
ture. Comput. Electron. Agric. 184, 105942. http://dx.doi.org/10.1016/j.compag.
2020.105942.

Ramos,

L., 2021. How Digital Twin could double down farm efficiency.

https://www.aquaculturenorthamerica.com/how-digital-twin-could-double-down-
farm-efficiency/. (Accessed 05 October 2021).

Rasheed, A., San, O., Kvamsdal, T., 2019. Hybrid analysis and modeling as an
enabler for big data cybernetics. In: Proceedings of the 32nd Nordic Seminar on
Computational Mechanics. Oulu, Finland, pp. 24–25.

Rasheed, A., San, O., Kvamsdal, T., 2020. Digital twin: Values, challenges and enablers
from a modeling perspective. IEEE Access 8, 21980–22012. http://dx.doi.org/10.
1109/ACCESS.2020.2970143.

Reite, K.J., Føre, M., Aarsæther, K.G., Jensen, J., Rundtop, P., Kyllingstad, L.T.,
Endresen, P.C., Kristiansen, D., Johansen, V., Fredheim, A., 2014. FHSIM — Time
Domain Simulation of Marine Systems. In: International Conference on Offshore
Mechanics and Arctic Engineering. In: Ocean Engineering, vol. 8A, http://dx.doi.
org/10.1115/OMAE2014-23165, p. V08AT06A014.

Remen, M., Oppedal, F., Imsland, A.K., Olsen, R.E., Torgersen, T., 2013. Hypoxia
tolerance thresholds for post-smolt Atlantic salmon: Dependency of temperature
and hypoxia acclimation. Aquaculture 416–417, 41–47. http://dx.doi.org/10.1016/
j.aquaculture.2013.08.024.

Remen, M., Oppedal, F., Torgersen, T., Imsland, A.K., Olsen, R.E., 2012. Effects of
cyclic environmental hypoxia on physiology and feed intake of post-smolt Atlantic
salmon: Initial responses and acclimation. Aquaculture 326–329, 148–155. http:
//dx.doi.org/10.1016/j.aquaculture.2011.11.036.

Rosell Moll, E., Piazzon de Haro, M.C., Sosa, J., Ferrer, M., Cabruja, E.,
Vega Martínez, A., Calduch Giner, J., Sitja-Bobadilla, A., Lozano, M., Montiel-
Nelson, J.A., et al., 2021. Smart Biosensing Device for Tracking Fish Behaviour.
Universidade do Algarve.

Rosten, C.M., Mathiassen, J.R., Volent, Z., 2023. Acoustic environment of aquaculture
net-pens varies with feeding status of Atlantic salmon (Salmo salar). Aquaculture
563, 738949. http://dx.doi.org/10.1016/j.aquaculture.2022.738949.

Rountree, R.A., Juanes, F., Bolgan, M., 2018. Air movement sound production by
alewife, white sucker, and four salmonid fishes suggests the phenomenon is
widespread among freshwater fishes. PLoS One 13 (9), e0204247. http://dx.doi.
org/10.1371/journal.pone.0204247.

Royer, E., Faccenda, F., Pastres, R., 2021. Estimating oxygen consumption of rainbow
trout (Oncorhynchus Mykiss) in a raceway: A precision fish farming approach.
Aquac. Eng. 92, 102141. http://dx.doi.org/10.1016/j.aquaeng.2020.102141.

ComputersandElectronicsinAgriculture218(2024)10867619M. Føre et al.

Rundtop, P., Frank, K., 2016. Experimental evaluation of hydroacoustic instruments
for ROV navigation along aquaculture net pens. Aquac. Eng. 74, 143–156. http:
//dx.doi.org/10.1016/j.aquaeng.2016.08.002.
Russel, G., 2021. R3-IoT: Digital platform is

to revolutionise aquaculture.

set

https://www.thenational.scot/news/19281879.new-digital-platform-will-
revolutionise-aquaculture/. (Accessed 05 October 2021).

Russo, T., Prestinicola, L., Scardi, M., Palamara, E., Cataudella, S., Boglione, C., 2010.
Progress in modeling quality in aquaculture: An application of the self-organizing
map to the study of skeletal anomalies and meristic counts in Gilthead Seabream
(Sparus Aurata, L. 1758). J. Appl. Ichthyol. 26 (2), 360–365. http://dx.doi.org/10.
1111/j.1439-0426.2010.01435.x.

Saberioon, M., Gholizadeh, A., Cisar, P., Pautsina, A., Urban, J., 2017. Application of
machine vision systems in aquaculture with emphasis on fish: State-of-the-art and
key issues. Rev. Aquac. 9 (4), 369–387. http://dx.doi.org/10.1111/raq.12143.
San, O., Rasheed, A., Kvamsdal, T., 2021. Hybrid analysis and modeling, eclecticism,
and multifidelity computing toward digital twin revolution. GAMM-Mitt. 44 (2),
e202100007. http://dx.doi.org/10.1002/gamm.202100007.

Sara, J.R., Gous, R.M., Bureau, D.P., 2009. Describing growth and predicting feed intake
in the marine prawn Fenneropenaeus indicus: Part I: Theoretical and practical
aspects of measuring and predicting genetic parameters. Aquaculture 287 (3),
402–413. http://dx.doi.org/10.1016/j.aquaculture.2008.10.057.

Schellewald, C., Stahl, A., Kelasidi, E., 2021. Vision-based pose estimation for au-
IFAC-PapersOnLine 54 (16),

tonomous operations in aquacultural
438–443. http://dx.doi.org/10.1016/j.ifacol.2021.10.128.

fish farms.

Schleich, B., Anwer, N., Mathieu, L., Wartzack, S., 2017. Shaping the digital twin for
design and production engineering. CIRP Ann. 66 (1), 141–144. http://dx.doi.org/
10.1016/j.cirp.2017.04.040.

Schraml, R., Hofbauer, H., Jalilian, E., Bekkozhayeva, D., Saberioon, M., Cisar, P.,
Uhl, A., 2020. Towards fish individuality-based aquaculture. IEEE Trans. Ind.
Inform. 17 (6), 4356–4366. http://dx.doi.org/10.1109/TII.2020.3006933.

Shchepetkin, A.F., McWilliams, J.C., 2005. The regional oceanic modeling system
(ROMS): A split-explicit,
topography-following-coordinate oceanic
model. Ocean Model. 9 (4), 347–404. http://dx.doi.org/10.1016/j.ocemod.2004.
08.002.

free-surface,

Simonnet-Laprade, C., Bayen, S., Le Bizec, B., Dervilly, G., 2021. Data analysis strategies
for the characterization of chemical contaminant mixtures. Fish as a case study.
Environ. Int. 155, 106610. http://dx.doi.org/10.1016/j.envint.2021.106610.

SINTEF,

2023. HAVOPERA. Available

from http://www.sintef.no/laboratorier/

havopera. (Accessed 30 June 2023).

SINTEF Ocean, 2020. RACE digital cage. https://www.sintef.no/en/projects/2020/race-

digital-cage/. (Accessed 05 October 2021).

Skøien, K.R., Alver, M.O., Alfredsen, J.A., 2014. A computer vision approach for
detection and quantification of feed particles in marine fish farms. In: 2014 IEEE
International Conference on Image Processing. ICIP, IEEE, pp. 1648–1652.

Slagstad, D., Ellingsen, I.H., Wassmann, P., 2011. Evaluating primary and secondary
production in an Arctic Ocean void of summer sea ice: An experimental simulation
approach. Prog. Oceanogr. 90 (1), 117–131. http://dx.doi.org/10.1016/j.pocean.
2011.02.009.

Slagstad, D., McClimans, T.A., 2005. Modeling the ecosystem dynamics of the Barents
sea including the marginal ice zone: I. Physical and chemical oceanography. J.
Mar. Syst. 58 (1), 1–18. http://dx.doi.org/10.1016/j.jmarsys.2005.05.005.

Solstorm, D., Oldham, T., Solstorm, F., Klebert, P., Stien, L.H., Vågseth, T., Oppedal, F.,
2018. Dissolved oxygen variability in a commercial sea-cage exposes farmed
Atlantic salmon to growth limiting conditions. Aquaculture 486, 122–129. http:
//dx.doi.org/10.1016/j.aquaculture.2017.12.008.

Sreedevi, T., Kumar, M.S., 2020. Digital twin in smart farming: A categorical literature
review and exploring possibilities in hydroponics. In: 2020 Advanced Computing
and Communication Technologies for High Performance Applications. ACCTHPA,
IEEE, pp. 120–124.

Staalesen, K., 2019. Exploring the Digital Twin Concept for a Rigid Aquaculture

Cage (Master’s thesis). NTNU.

Stadtmann, F., Rasheed, A., Kvamsdal, T., Johannessen, K.A., San, O., Kölle, K.,
Tande, J.O., Barstad, I., Benhamou, A., Brathaug, T., Christiansen, T., Firle, A.L.,
Fjeldly, A., Frøyd, L., Gleim, A., Høiberget, A., Meissner, C., Nygård, G., Olsen, J.,
Paulshus, H., Rasmussen, T., Rishoff, E., Scibilia, F., Skogås, J.O., 2023a. Digital
twins in wind energy: Emerging technologies and industry-informed future direc-
tions. IEEE Access 11, 110762–110795. http://dx.doi.org/10.1109/ACCESS.2023.
3321320.

Stadtmann, F., Wassertheurer, H.A.G., Rasheed, A., 2023b. Demonstration of a stan-
dalone, descriptive, and predictive digital twin of a floating offshore wind turbine.
In: ASME 2023 42nd International Conference on Ocean, Offshore and Arctic
Engineering. American Society of Mechanical Engineers Digital Collection, http:
//dx.doi.org/10.1115/OMAE2023-103112.

Stavelin, H., Rasheed, A., San, O., Hestnes, A.J., 2021. Applying object detection to
marine data and exploring explainability of a fully convolutional neural network
using principal component analysis. Ecol. Inform. 62, 101269. http://dx.doi.org/
10.1016/j.ecoinf.2021.101269.

Stavrakidis-Zachou, O., Papandroulakis, N., Lika, K., 2019. A DEB model for European
sea bass (Dicentrarchus Labrax): Parameterisation and application in aquaculture.
J. Sea Res. 143, 262–271. http://dx.doi.org/10.1016/j.seares.2018.05.008.

Stavrakidis-Zachou, O., Papandroulakis, N., Pavlidis, M., Lika, K., 2021. Preliminary
dynamic energy budget models for studying the thermal tolerance of E. seabass
and meagre. In: Aquaculture Europe 2021. Madeira, Portugal, EAS, pp. 1244–1245.
Stien, L.H., Nilsson, J., Bui, S., Fosseidengen, J.E., Kristiansen, T.S., Øverli, Ø.,
Folkedal, O., 2017. Consistent melanophore spot patterns allow long-term indi-
vidual recognition of Atlantic salmon Salmo salar. J. Fish Biol. 91 (6), 1699–1712.
http://dx.doi.org/10.1111/jfb.13491.

Stockwell, C.L., Filgueira, R., Grant, J., 2021. Determining the effects of environmen-
tal events on cultured Atlantic salmon behaviour using 3-dimensional acoustic
telemetry. Front. Animal Sci. 2, http://dx.doi.org/10.3389/fanim.2021.701813.
Su, B., Bjørnson, F.O., Tsarau, A., Endresen, P.C., Ohrem, S.J., Føre, M., Fagertun, J.T.,
Klebert, P., Kelasidi, E., Bjelland, H.V., 2023. Towards a holistic digital twin
solution for real-time monitoring of aquaculture net cage systems. Mar. Struct.
91, 103469. http://dx.doi.org/10.1016/j.marstruc.2023.103469.

Su, B., Kelasidi, E., Frank, K., Haugen, J., Føre, M., Pedersen, M.O., 2021. An integrated
approach for monitoring structural deformation of aquaculture net cages. Ocean
Eng. 219, 108424. http://dx.doi.org/10.1016/j.oceaneng.2020.108424.

Su, B., Reite, K.J., Føre, M., Aarsæther, K.G., Alver, M.O., Endresen, P.C., Kris-
tiansen, D., Haugen, J., Caharija, W., Tsarau, A., 2019. A multipurpose framework
for modelling and simulation of marine aquaculture systems. In: International
Conference on Offshore Mechanics and Arctic Engineering, Vol. 58837. American
Society of Mechanical Engineers, p. V006T05A002.

Sukhinov, A.I., Chistyakov, A.E., Timofeeva, E.F., Shishenya, A.V., 2013. Mathematical
model for Calculating Coastal wave processes. Math. Models Comput. Simul. 5 (2),
122–129. http://dx.doi.org/10.1134/S2070048213020087.

Thorstad, E.B., Rikardsen, A.H., Alp, A., Økland, F., 2013. The use of electronic tags
in fish research–an overview of fish telemetry methods. Turk. J. Fish. Aquat. Sci.
13 (5), 881–896.

Tsukrov, I., Eroshkin, O., Fredriksson, D., Swift, M.R., Celikkol, B., 2003. Finite element
modeling of net panels using a consistent net element. Ocean Eng. 30 (2), 251–270.
http://dx.doi.org/10.1016/S0029-8018(02)00021-5.

Urke, H., Daae, K., Viljugrein, H., Kandal,

I., Staalstrøm, A., Jansen, P., 2021.
Improvement of aquaculture management practice by integration of hydrodynamic
modelling. Ocean & Coastal Management 213, 105849. http://dx.doi.org/10.1016/
j.ocecoaman.2021.105849.

Vaidya, S., Ambad, P., Bhosle, S., 2018. Industry 4.0 – A glimpse. Procedia Manuf.
20, 233–238. http://dx.doi.org/10.1016/j.promfg.2018.02.034, 2nd International
Conference on Materials, Manufacturing and Design Engineering (iCMMD2017),
11-12 December 2017, MIT Aurangabad, Maharashtra, INDIA.

VanDerHorn, E., Mahadevan, S., 2021. Digital twin: Generalization, characterization
and implementation. Decis. Support Syst. 145, 113524. http://dx.doi.org/10.1016/
j.dss.2021.113524.

Verdouw, C., Tekinerdogan, B., Beulens, A., Wolfert, S., 2021. Digital twins in smart
farming. Agric. Syst. 189, 103046. http://dx.doi.org/10.1016/j.agsy.2020.103046.
von Rueden, L., Mayer, S., Sifa, R., Bauckhage, C., Garcke, J., 2020. Combining
machine learning and simulation to a hybrid modelling approach: Current and
future directions. In: Advances in Intelligent Data Analysis XVIII: 18th International
Symposium on Intelligent Data Analysis, IDA 2020, Konstanz, Germany, April
27–29, 2020, Proceedings 18. Springer, pp. 548–560.

Voskakis, D., Makris, A., Papandroulakis, N., 2021. Deep learning based fish length
estimation. An application for the mediterranean aquaculture. In: OCEANS 2021:
San Diego–Porto. IEEE, pp. 1–5.

Waldrop, T., Summerfelt, S., Mazik, P., Good, C., 2018. The effects of swimming
exercise and dissolved oxygen on growth performance, fin condition and precocious
maturation of early-rearing Atlantic salmon Salmo salar. Aquacult. Res. 49 (2),
801–808.

Winthereig-Rasmussen, H., Simonsen, K., Patursson, Ø., 2016. Flow through fish
farming sea cages: Comparing computational fluid dynamics simulations with scaled
and full-scale experimental data. Ocean Eng. 124, 21–31. http://dx.doi.org/10.
1016/j.oceaneng.2016.07.027.

Zacheilas, T., Moirogiorgou, K., Papandroulakis, N., Sotiriades, E., Zervakis, M.,
Dollas, A., 2021. An FPGA-based system for video processing to detect holes in
aquaculture nets. In: 2021 IEEE 21st International Conference on Bioinformatics
and Bioengineering. BIBE, IEEE, pp. 1–6.

Zhabitskii, M., Andryenko, Y., Malyshev, V., Chuykova, S., Zhosanov, A., 2021. Digital
transformation model based on the digital twin concept for intensive aquaculture
production using closed water circulation technology. In: IOP Conference Series:
Earth and Environmental Science, vol. 723, (no. 3), IOP Publishing, 032064.
Zhang, H., Wei, Q., Kang, M., 2014. Measurement of swimming pattern and body length
of cultured Chinese sturgeon by use of imaging sonar. Aquaculture 434, 184–187.
http://dx.doi.org/10.1016/j.aquaculture.2014.08.024.

Zion, B., 2012. The use of computer vision technologies in aquaculture – A review.
Comput. Electron. Agric. 88, 125–132. http://dx.doi.org/10.1016/j.compag.2012.
07.010.

ComputersandElectronicsinAgriculture218(2024)10867620