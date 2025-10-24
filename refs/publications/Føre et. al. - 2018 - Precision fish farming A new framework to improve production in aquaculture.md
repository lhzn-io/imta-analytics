b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

Available online at www.sciencedirect.com
ScienceDirect

j o u r n a l h o m e p a g e : w w w . e l s e v i e r . c o m / l o c a t e / i s s n / 1 5 3 7 5 1 1 0

Special Issue: Engineering Advances in Precision Livestock Farming

Review

Precision ﬁsh farming: A new framework to
improve production in aquaculture

, Kevin Frank a, Tomas Norton c, Eirik Svendsen a,

Martin Føre a,b,*
Jo Arve Alfredsen b, Tim Dempster d, Harkaitz Eguiraun e,f, Win Watson g,
Annette Stahl b, Leif Magne Sunde a, Christian Schellewald a,
Kristoffer R. Skøien b, Morten O. Alver a,b, Daniel Berckmans c

a SINTEF Ocean, 7465 Trondheim, Norway
b NTNU Department of Engineering Cybernetics, 7491 Trondheim, Norway
c KU Leuven, M3-BIORES, Kasteelpark Arenberg 30, bus 2456, 3001 Leuven, Belgium
d School of BioSciences, University of Melbourne, Victoria 3010, Australia
e Research Center for Experimental Marine Biology and BiotechnologydPlentziako Itsas Estazioa (PIE), University of
the Basque Country UPV/EHU, 48620 Plentzia, Spain
f Dept. of Graphic Design & Engineering Projects, Faculty of Engineering of Bilbao, University of the Basque Country
UPV/EHU, 48013 Bilbao, Spain
g University of New Hampshire, Department of Biological Sciences, Rudman Hall, Durham, NH 03824, USA

a r t i c l e i n f o

Article history:

Published online 14 November 2017

Keywords:

Precision Livestock Farming

Fish farming

Atlantic salmon

Technology

Modelling

Sensors

Aquaculture production of ﬁnﬁsh has seen rapid growth in production volume and economic

yield over the last decades, and is today a key provider of seafood. As the scale of production

increases, so does the likelihood that the industry will face emerging biological, economic and

social challenges that may inﬂuence the ability to maintain ethically sound, productive and

environmentally friendly production of ﬁsh. It is therefore important that the industry as-

pires to monitor and control the effects of these challenges to avoid also upscaling potential

problems when upscaling production. We introduce the Precision Fish Farming (PFF) concept

whose aim is to apply control-engineering principles to ﬁsh production, thereby improving
the farmer's ability to monitor, control and document biological processes in ﬁsh farms. By
adapting several core principles from Precision Livestock Farming (PLF), and accounting for

the boundary conditions and possibilities that are particular to farming operations in the

aquatic environment, PFF will contribute to moving commercial aquaculture from the

traditional experience-based to a knowledge-based production regime. This can only be

achieved through increased use of emerging technologies and automated systems. We have

also reviewed existing technological solutions that could represent important components in

future PFF applications. To illustrate the potential of such applications, we have deﬁned four

case studies aimed at solving speciﬁc challenges related to biomass monitoring, control of

feed delivery, parasite monitoring and management of crowding operations.
© 2017 The Authors. Published by Elsevier Ltd on behalf of IAgrE. This is an open access
article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

* Corresponding author.

E-mail address: Martin.Fore@sintef.no (M. Føre).
https://doi.org/10.1016/j.biosystemseng.2017.10.014
1537-5110/© 2017 The Authors. Published by Elsevier Ltd on behalf of IAgrE. This is an open access article under the CC BY license (http://
creativecommons.org/licenses/by/4.0/).

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

177

Introduction: a technological journey from

1.
terrestrial animal production to intensive ﬁsh
farming

1.1.

Modern intensive ﬁsh farming

Modern intensive ﬁsh aquaculture comprises all life stages of
the ﬁsh from brood-stock/eggs to fully-grown adults. The
hatchery phase is typically conducted in indoor tanks, where
one is able to control the environmental conditions and other
external factors affecting the ﬁsh. While some species are
raised in tanks all the way to marketable size, most industri-
ally farmed ﬁnﬁsh species are transferred to outdoor ponds or
sea-cages for the ﬁnal ongrowing phase. This is because the
volume of water required by a ﬁsh depends strongly on its
size, and a gradual scaling of the production unit volume as
the ﬁsh grow is easier to facilitate in the sea or ponds than in
indoor tanks. Sea-based ﬁsh farming also exposes ﬁsh to
natural ﬂuctuations in important features of the production
environment (e.g. water ﬂow, temperature and light in-
tensity). Although this limits the farmer's ability to control the
production conditions, and increases the chance that
stressors such as pollutants, pathogens and parasites are
introduced into the population, the simplicity and cost-
effectiveness of open systems makes this approach more
competitive today (Iversen, Andreassen, Hermansen, Larsen,
& Terjesen, 2013).

Currently, Atlantic salmon (Salmo salar L.) are the most
signiﬁcant farmed sea-based ﬁnﬁsh species with more than
2.3 Mt produced globally in 2014 (FAO, 2016). In Norwegian
salmon production, ongrowth is conducted in ﬂexible sea-
cages located in sheltered coastal areas, or at locations more
exposed to environmental forces (Bjelland et al., 2015, pp.
1e10). As with many other industries, salmon farming has
sought to reap the beneﬁts of economies of scale, meaning
that both farm size and the size of individual cages has
increased with the intent of producing more ﬁsh per
employee, leading to increased proﬁtability (Hallam, 1991). As
a result, production cages at current Norwegian salmon farms
often have a circumference of up to 157 m, contain a volume of
approximately 40,000 m3, and hold up to 200,000 individual
ﬁsh. Considering that a typical ﬁsh farm consists of 8e16
separate cages, this means that each farming crew (typically
5e10 people in total) may be responsible for several million
animals, amounting to a biomass of up to 15,000 t. Sea-based
production of salmon is therefore a very large-scale intensive
form of seafood production.

Much of the human historical knowledge on animal hus-
bandry has been built on a direct relationship between farmer
and animal. However, such relationships are not possible to
establish with a population consisting of millions of individual
animals living under water, making it almost impossible to
evaluate the animals and collect information on the status of
the population through direct observation. This challenge will
be further ampliﬁed by the present trend towards moving
aquaculture operations to more environmentally exposed
areas, which will render the farms less accessible to farmers
(Bjelland et al., 2015, pp. 1e10). Due to these factors, a regime
based on direct observation alone may be insufﬁcient to

acquire the levels of knowledge, monitoring and control
required to tackle the challenges of modern ﬁsh farming.
Instead, what is required for modern large-scale ﬁsh farming
are technological tools that enable remote monitoring of large
populations of ﬁsh in a manner that yields data that can be
used to adjust and modify day-to-day operations to optimise
the growth and survival of the ﬁsh. The idea of applying such
principles to commercial ﬁsh production may be traced back
to the original thoughts and philosophies of Jens Glad Balchen
(Balchen, 1979).

1.2.

Precision Livestock Farming

Livestock production is the second largest supplier of food for
human consumption behind vegetable/cereal agriculture.
Although there have been several initiatives concerning auto-
mated sensing and detection of farm animal responses (e.g.
Van der Stuyft, Schoﬁeld, Randall, Wambacq, & Goedseels,
1991; Maatje, De Mol, & Rossing, 1997), and mathematical
modelling of animal behavioural and physiological dynamics
(e.g. Bastianelli & Sauvant, 1997; Kristensen & Kristensen, 1998)
in the 80's and 90's, the ﬁrst conceptual framework of Precision
Livestock Farming (PLF) was not established until the turn of
the millennium by Berckmans (2004). While the general prin-
ciple of using technology and automation to improve precision
in industrial production is directly transferrable from the pro-
cess and manufacturing industries to PLF, the transition of
focus from inert products to live animals introduces the
following additional complications that need to be taken into
account when developing PLF methods:

(cid:1) Observation and monitoring is more challenging, as ani-
mals at times exhibit complex behaviour that may be
difﬁcult to observe and interpret.

(cid:1) Animals may move and are not always willing or able to
cooperate with the farmer, making the implementation of
automated actions more difﬁcult.

(cid:1) In addition to covering the basal requirements for survival,
animal needs are also linked with their ability to exhibit
certain behaviours, and maintain a certain perceived
quality of life, or welfare.

Berckmans (2004) stated three distinct conditions that a
system would need to fulﬁl if it was to achieve sufﬁcient levels
of monitoring and control to be considered a PLF system:

1) Animal variables (i.e. parameters related to the behavioural
or physiological state of the animal) need to be measured
continuously with cost-effective robust sensor technology,
2) a reliable model for predicting (expectation of) how Animal
variables will dynamically vary in response to external
factors at any moment must be available, and

3) predictions and on-line measurements are integrated in an
analysing algorithm for automatic monitoring and/or
control.

PLF methods are often deﬁned using a common terminol-
ogy denoting the different components in a PLF-system
(Table 1).

178

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

Technological advances over the last decades have enabled
the development of several PLF methods and application areas,
including the use of modern sensor technologies to monitor
animal variables (e.g. Darr & Epperson, 2009; Tebot et al., 2009),
using methods from information technology and modelling to
synthesise and combine different types of data (e.g. Milner-
Gulland, Kerven, Behnke, Wright, & Smailov, 2006; Terrasson,
Llaria, Marra, & Voaden, 2016), and the application of control
theory to increase the level of autonomy (see Johnson et al.,
2011 on different autonomy levels) of the production process
(Frost et al., 2003). While most of these applications have arisen
from research activities, the long-term goal of PLF is to provide
industrial methods and tools that contribute to improving
animal health and welfare while increasing productivity, yield
and environmental sustainability. This is generally achieved
through the combination of hardware and intelligent software
(Berckmans, 2014). Examples of successful PLF applications in
the livestock production industry include the automated
monitoring of pig health through cough analysis with micro-
phones (Berckmans, Hemeryck, Berckmans, Vranken, & van
Waterschoot, 2015), the utilisation of automated milking ro-
bots on cows (John et al., 2016), and the use of computer vision
methods to automatically monitor real time positions of ani-
mals (Sloth & Frederiksen, 2015).

Aquaculture ﬁsh production faces many of the same chal-
lenges as modern terrestrial meat production, and some as-
pects of PLF can therefore be adapted directly to intensive ﬁsh
farming. However, aquaculture also faces additional chal-
lenges that add to the complexity of the farming operations:

(cid:1) The feed consumed by the ﬁsh in ﬁsh farms is exclusively
provided by the farmer, leading to a strong dependency on
farming management.

(cid:1) Feeding and most other operations are enacted on the
entire cage population, as opposed to on individual or
small group levels.

(cid:1) The number of individual animals in ﬁsh farms (millions)
exceeds what is common in most terrestrial livestock
farms.

(cid:1) The ﬁsh live in a complex 3D environment and all farming
operations associated with the ﬁsh are at least partly

conducted in the subsurface environment, which is
generally more challenging than terrestrial farming.

(cid:1) The exposure of the ﬁsh to external stressors such as
pathogens/diseases (McVicar, 1987), parasites (Grimnes &
Jakobsen, 1996), chemical pollutants (e.g. Brodin, Fick,
Jonssom, & Klaminder, 2013) and microplastics (Wright,
Thompson, & Galloway, 2013) is largely determined by
the ambient environmental conditions and outside of
human control.

1.3.

Scope of this study

We have developed the Precision Fish Farming (PFF) concept
that is based on PLF and hence accommodates the features
therein, while also addressing the additional challenges of
farming animals in water. In this article, we will present the
PFF framework by ﬁrst deﬁning the boundary conditions and
possibilities of precision farming in the aquatic environment,
then deﬁning the PFF concept in brief terms, and then going
through the status of PFF today, within the framework of
research and industry. Following this, we will address the
potential industrial impacts of PFF exempliﬁed by four speciﬁc
case studies, before we conclude and recommend future
research directions we deem important for the continued
development of the PFF concept. We will primarily use ex-
amples related to Atlantic salmon farming, because this is a
segment of industrial ﬁsh farming that has a high technology
level, is under rapid development, and hence will be very
receptive with respect to PFF-methods. However, we believe
that the applications of PFF we suggest will be transferrable to
other aquatic farmed species.

Adapting precision farming to the aquatic

2.
environment: boundary conditions and
possibilities

Over the millennia that terrestrial livestock farming has been
a part of human culture, the interaction between man and
animal has produced a vast body of veterinary, ethological
and physiological knowledge on farm animals. Through such

Table 1 e Some of the main terms used to deﬁne PLF methods and that hence form the foundation of the PFF terminology.

Term

Complex, Individual and Time-variant (CIT) system

Bio-response
Animal variable

Feature variable

Target variable

Gold standard

Explanation

A complex, individually different and time-variant system. Applies to all
living organisms, including animals (Berckmans, 2004; 2013).
The biological response of an animal when exposed to external stimuli.
Any parameter related to the behavioural or physiological state of the
animal, e.g. weight, activity, feed intake (Berckmans, 2004). Typically
acquired in the ﬁeld.
Variable that may be calculated based on measured Animal variables and
that describes the bio-response of interest (Berckmans, 2013; Norton &
Berckmans, 2017).
Variable that is derived from Feature variables and that relates to the ﬁnal
objective of the PLF method (Norton & Berckmans, 2017). Target variables
are used as foundations for making management decisions.
Reliable and/or generally accepted method of measuring or observing
Target variables (Norton & Berckmans, 2017). Gold standards may be
expensive, complex and difﬁcult to assess, but are necessary to verify that a
PLF method provides reliable outputs.

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

179

Fox, & Guiroy,

2004), health/survival

knowledge, humans have been able to identify how observ-
able traits and bio-responses exhibited by animals may be
linked with management outcomes such as growth (e.g.
Tedeschi,
(e.g.
Berckmans et al., 2015) and milk production (e.g. John et al.,
2016). This process is analogous to the system identiﬁcation
methods used in control engineering to determine relation-
ships between system inputs and system outputs when
lacking a complete mechanistic description of key sub-
(cid:1)
Astr€om & Eykhoff, 1971). Establishing an under-
systems (
standing of such relationships is a prerequisite for being able
to derive the sequence from an observed bio-response,
through Animal and Feature variables, to Target variables
that lies at the core of the PLF concept. Moreover, a thorough
understanding of the system dynamics is also key in identi-
fying possible Gold Standards to validate such methods.

Direct man and animal interaction is more difﬁcult in ﬁsh
farming than in its terrestrial counterpart, and the population
sizes in ﬁsh aquaculture make interactions with speciﬁc in-
dividuals very difﬁcult. Furthermore, intensive cage-based
ﬁsh farming has a comparatively shorter industrial history
(decades) than terrestrial livestock production (millennia). As
a result, knowledge about the bioprocesses occurring in in-
dustrial ﬁsh farming is very limited compared with terrestrial
farming; this makes proper system identiﬁcation a more
challenging task. Moreover, it means that the identiﬁcation of
both relationships between bio-responses and Target vari-
ables and proper Gold Standards will often be more difﬁcult
and likely to be based on a weaker foundation in a ﬁsh farming
situation.

In addition to inﬂuencing the knowledge foundation for
deriving PFF methods,
the aforementioned factors also
complicate the operational aspects of implementing such
methods. For instance, it is generally challenging to continu-
ously monitor animals and achieve sufﬁcient information for
PFF applications in the aquatic environment. While such in-
formation may be obtained using direct observation or low-
end technological equipment on land, more advanced tech-
nical solutions are required to achieve a similar knowledge
basis in ﬁsh farms, where one needs to cope with the unfor-
giving conditions of the subsurface environment at increas-
ingly exposed sites, and the large number of animals at each
farm. Moreover, the establishment of Gold Standards may be
complicated by the difﬁculties in directly interacting with in-
dividuals. Many Gold Standards used in terrestrial farming
require veterinarians or farmers to directly observe and/or
interact with the animals, an ability that may be rendered
near impossible in commercial ﬁsh farms. In spite of all these
challenges, the technologies used today by farmers to observe
the ﬁsh represent good foundations for developing future PFF
applications, and often entail already established technical
infrastructures
for communication and power supply.
Furthermore, since farmers are already accustomed to
employing technical solutions in their everyday work tasks,
the introduction of new technology based upon PFF methods
will not represent a completely new concept.

As ﬁsh farms increase in size and complexity, the size and
designs of ﬁsh cages evolve, and new location types are taken
into use (e.g. Bjelland et al., 2015, pp. 1e10), more sophisti-
cated technological solutions will be required to provide

sufﬁcient knowledge and information to monitor and/or
control the biological production process. Furthermore, a side
effect of the increases in scale occurring within the industry is
that risks associated with day-to-day operations are also
increasing (Kalogerakis et al., 2015). Larger structures sustain
larger loads, making handling and manipulation of structural
components such as the net or sinker tubes more precarious
activities (Lader, Dempster, Fredheim, & Jensen, 2008). In the
event of component breakdown during such operations, the
forces released in modern ﬁsh farms are more likely to cause
serious injuries than was the case decades ago. Moreover,
with larger populations in each cage, potential negative con-
sequences of suboptimal animal handling such as escapes
(Jensen, Dempster, Thorstad, Uglem, & Fredheim, 2009) and
impaired welfare (Pettersen et al., 2014) will also increase.
Using technology to automate or otherwise increase the se-
curity of such operations could thus lead to vast improve-
ments in risk mitigation around commercial ﬁsh farms, which
might be one of the most important outcomes of using the PFF
approach.

In addition, the Norwegian government presently has an
arrangement where salmon production companies are awar-
ded new ﬁsh production permits (so-called development
permits) if they develop new concepts for sustainable pro-
duction of salmon. How the ﬁsh will respond to and grow in
new and untested production concepts is largely unknown.
Furthermore, many of these concepts include larger ﬁsh
populations being kept in each production unit (i.e. cages or
tanks). Although such concepts also include increasing the
volumes of the production units accordingly to achieve com-
parable stocking densities to those commonly used today, the
surface area of the cage facing the upstream current does not
scale with the same factor. For example, if the population and
correspondingly the production unit volume is upscaled by a
factor of ﬁve, the upstream facing cage area will scale by a
factor of less than three. As a consequence, the water ex-
change rate does not scale properly with the population (Lader
et al., 2008). This may lead to hypoxic conditions in the cage as
the oxygen consumption of the ﬁsh may then exceed the ox-
ygen replenishment through incoming water. Poor dissolved
oxygen conditions reduce the appetite and subsequent growth
rates of ﬁsh (Remen, Sievers, Torgersen, & Oppedal, 2016).
This development emphasises the need for better methods to
manage and monitor the populations in commercial ﬁsh
production systems. We thus argue that the potential indus-
trial impact of PFF may equal or even exceed that of PLF.

3.

Precision Fish Farming (PFF)

Precision Fish Farming and the different elements of

3.1.
the ﬁsh farming process

The overarching aims of Precision Fish Farming (PFF) are to: 1)
improve accuracy, precision and repeatability in farming op-
erations; 2) facilitate more autonomous and continuous
biomass/animal monitoring; 3) provide more reliable decision
support and; 4) reduce dependencies on manual labour and
subjective assessments, and thus improve staff safety.
Through these means, PFF will improve animal health and

180

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

welfare while increasing the productivity, yield and environ-
mental sustainability in commercial intensive aquaculture.
To help in deﬁning PFF, it is useful to envision ﬁsh farming as
several cyclical operational processes realised in four phases
where bio-responses in the cage are observed (Observe phase)
and interpreted (Interpret phase), resulting in a foundation for
making decisions (Decide phase) on which actions to enforce
(Act phase) that in turn elicit a bio-response in the ﬁsh (Fig. 1).
Similar cyclic concepts have been used to describe processes
and products in other manufacturing industries, one of the
most notable examples of which is the Plan-Do-Check-Act
(PDCA) philosophy (Deming & Edwards, 1982) that has been
popular within e.g. the automotive industry (Rother, 2010).
This approach also resembles the OODA (Observe, Orient,
Decide, Act) cycle, which is a concept for decision making in
military strategy (Boyd John, 1987).

Today, most tasks pertaining to the different phases are
conducted manually (i.e. close to the centre in Fig. 1). First, the
farmer observes the ﬁsh via direct visual observation or with
data acquisition tools such as cameras, the outcome of which
is qualitative or quantitative information on the bio-responses
of the ﬁsh. The farmer then uses primarily subjective experi-
ence to interpret this information, yielding a perception of the
current state and condition of the ﬁsh. These interpretations
are then used as a foundation for making decisions concern-
ing farming operations and management, which are then put
into action by manually induced actions on the cage. Such
decisions may be made based on the estimated present states
or expected future states of the system, representing manual

Fig. 1 e A cyclical representation of PFF where operational
processes are considered to consist of four phases:
Observe, Interpret, Decide and Act. The inner cycle
represents the present state-of-the-art in industry, with
manual actions and monitoring, and experience-based
interpretation and decision-making. The outer cycle
illustrates how the introduction of PFF may inﬂuence the
different phases of the cycle. Figure credits: Andreas
Myskja Lien, SINTEF Ocean.

versions of the feedback and feed-forward principles in con-
trol engineering respectively.

Methods and tools for ﬁsh farming that apply technological
solutions and/or automation principles to one, several or all
the different phases of farming operations may be considered
PFF approaches. The ultimate result of applying PFF to a
particular operation will therefore be that the elements in that
operation belonging to the different phases of ﬁsh farming
operations are shifted from an experience-based to a
knowledge-based regime (i.e. by moving from the centre to-
wards the outer edge in Fig. 1).

Status of Precision Fish Farming in present industry

3.2.
and research

Although the PFF concept has not previously been deﬁned,
many technological research efforts and equipment
in-
novations for the ﬁsh aquaculture industry can be considered
tools or components for developing PFF methods, and in a few
cases are already PFF methods in their own right. Here, we
provide an overview of the present status in this area,
covering both industrial applications and research activities.
Most relevant methods or concepts included here address a
single phase in ﬁsh farming operations (Fig. 1), hence a status
will be given separately for each phase.

3.2.1. Observe: Animal variables describing bio-responses
inability to use direct observation to make
The general
representative assessments of individual and population
states under water in ﬁsh farms means that ﬁsh farmers
already depend on using technological solutions to monitor
their animals. Submerged cameras are the most common
tools found on ﬁsh farms today, and are used to observe the
ﬁsh during production, with operators manually, and subjec-
tively, analysing behaviour. Camera systems are useful plat-
forms for automated ﬁsh monitoring by applying computer
vision algorithms to the video stream. The possibilities within
computer vision techniques are expanding rapidly, both due
to the development of enabling hardware such as camera and
computer technology, and to the increased application of
these technologies within the consumer electronics market.
Computer vision methods can quantify several different An-
imal variables in a ﬁsh farm setting, including clustering and
movement (e.g. Eguiraun, L(cid:3)opez-de-Ipi~na, & Martinez, 2014),
skin status (e.g. Wallat, Luzuriaga, Balaban, & Chapman,
2002), ﬁsh size (e.g. Hao, Yu, & Li, 2016), sea-lice infestation
levels (e.g. Tillett, Bull, & Lines, 1999) and behavioural changes
due to exposure to chemicals (e.g. Eguiraun, & Martinez,
2015b; Eguiraun, Lopez de Ipi~na, & Martinez, 2016). In addi-
tion, computer vision methods could monitor important
properties of the physical environment, such as feed pellet
quantities (Skøien, Alver, & Alfredsen, 2014), and behavioural
expressions observable above the water line such as surface
activity (Jovanovi(cid:3)c, Risojevi(cid:3)c, Babi(cid:3)c, Svendsen, & Stahl, 2016).
While the variation in technologies used to observe live ﬁsh
in industry is limited, the methodological diversity within
research is large, as researchers are constantly looking into
new methods for collecting scientiﬁc data. In addition to
cameras, active hydroacoustic devices are the most common
technological tools used to study ﬁsh in aquaculture research.

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

181

The most frequent application of this technology has been the
use of echo sounders to obtain echograms describing the
vertical ﬁsh distribution and schooling density in the cage
(Oppedal, Dempster, & Stien, 2011), which are Animal vari-
ables that may be used to quantify the bio-response of ﬁsh to
(e.g. Bui, Oppedal, Korsøen, Sonny, &
some treatment
Dempster, 2013; Johansson et al., 2006; Oppedal, Juell, &
Johansson, 2007). While conventional echo sounders are
limited to producing echograms, more advanced hydro-
acoustic devices are already in use within other marine in-
dustry segments, and could obtain additional Animal
variables from caged ﬁsh populations. For instance, split-
beam sonars can estimate swimming speeds and directions
of individual ﬁsh within their sonar beam (e.g. Arrhenius,
Benneheij, Rudstam, & Boisclair, 2000; Huse & Ona, 1996;
Knudsen, Fosseidengen, Oppedal, Karlsen, & Ona, 2004),
while multibeam sonar systems can produce data on the 3D
distribution and movements of the ﬁsh (e.g. Melvin, 2016;
Tenningen, Macaulay, Rieucau, Pe~na, & Korneliussen, 2016).
In addition, sonar based systems may be used to assess indi-
vidual ﬁsh sizes, given that it is possible to establish a rela-
tionship between the target strength (TS) of the ﬁsh and its
mass or length (Knudsen et al., 2004; Soliveres et al., 2017).
Passive hydrophones have also been used to provide infor-
mation on Animal variables related to the behaviour of several
ﬁsh species including salmonids by recording the sounds
emitted or generated by the ﬁsh (Kasumyan, 2008; 2009).
Considering that hydroacoustic devices (unlike cameras) are
impervious to visibility conditions, this group of technologies
could provide a useful foundation for PFF methods designed to
acquire behaviour-related Animal variables for farmed ﬁsh
populations.

Despite the considerable population sizes featured in
modern ﬁsh farming, indicators of individual ﬁsh behaviour
may prove equally important in ﬁsh farming as population or
group level Animal variables. Acoustic ﬁsh telemetry is a
method for remote sensing where individual ﬁsh are equipped
with electronic transmitters containing sensors that measure
some property in or near the ﬁsh, and that transmit raw or
post-processed data wirelessly to submerged stationary
receiver units using acoustic signals (i.e. sound waves). This
technology is widely used for wild ﬁsh research (e.g. Finstad,
Økland, Thorstad, Bjørn, & McKinley, 2005; Hedger et al.,
2011; Urke, Kristensen, Ulvund, & Alfredsen, 2013), but is
also seeing increased usage within aquaculture-related
research (e.g. Baras & Lagard(cid:4)ere, 1995; Rillahan, Chambers,
Howell, & Watson, 2009). Animal variables observed using
this technology in a culture setting include individual depth
movements (e.g. Føre, Alfredsen, & Gronningsater, 2011; Føre,
Frank, Dempster, Alfredsen, & Høy, 2017), 3D-positions (e.g.
Rillahan et al., 2009; Ward, Føre, Howell, & Watson, 2012),
swimming activity levels (e.g. Kolarevic et al., 2016), muscle
activity levels (e.g. Cooke, Thorstad, & Hinch, 2004) and
respiration rates/feed intake (e.g. Alfredsen, Holand, Solvang-
Garten, & Uglem, 2007). The deployment of acoustic telemetry
systems requires handling of the ﬁsh that often includes
surgery, and hence has a certain risk of inﬂuencing the states
of the ﬁsh, and the bio-responses they exhibit. However, at
present, acoustic telemetry is the only viable technique for
obtaining continuous data series from individual ﬁsh in

commercial sea-cages, making this technology an attractive
candidate for future PFF methods. Furthermore, while other
methods for subsurface ﬁsh observation (e.g. cameras and
sonars) are largely limited to deriving behaviour-based Ani-
mal variables, acoustic telemetry may be used to monitor ﬁsh
physiology (e.g. heart rate, blood composition) since the
transmitters units are placed in or on the ﬁsh.

Farming operations at sea are subject to natural conditions
at the site, as ﬁsh kept in sea-cages are exposed to conditions
strongly inﬂuenced by the ambient environment (e.g. weather,
water currents, sea states, temperatures, oxygen saturation,
light levels and pollutants). Since many of these factors affect
the growth, development and welfare of ﬁsh, data on the local
ambient environment is important when selecting farming
sites for salmon production. Furthermore, farmers increas-
ingly want to monitor such conditions at their site also during
production, as this information may be used as a foundation
for making decisions concerning farm management, such as
avoiding net manipulations when currents are strong, or
reducing feeding when temperature decreases. Such data will
be useful auxiliary data for deriving PFF methods, as it is often
necessary to view an observed Animal variable relative to
prevailing environmental conditions to derive desired Feature
variables. For instance, temperature and light strongly affect
the vertical movements of salmon (Johansson et al., 2006).
Evaluating the levels of these factors is critical when seeking
Feature variables that are based on depth movements, such as
responses to feeding events (Føre et al., 2011).

Table 2 Summarises some of the most common sensors
and monitoring methods used to observe salmon in sea-cages
today, including both industrially applied systems and solu-
tions primarily used in research. Figure 2 illustrates how a
selection of these systems would be applied in a commercial
cage.

Interpret: Feature variables from animal variables

3.2.2.
In the ﬁsh farming industry, the interpretation of animal ob-
servations is mainly conducted by individual farmers based
on personal experience. Although ongoing innovations aspire
to automate this process (e.g. systems for remote feeding
operations that aggregate and present relevant data from
different sources), the existing industrial foundation for
automated interpretation of Feature variables is less estab-
lished than it is for the acquisition of Animal variables.
However, this also means that the unreleased potential for
developing new PFF methods in this area is considerable.

As production from the cage-based ﬁsh farming industry
has increased, so has the extent of the research into obtaining
a better understanding of the processes occurring in farmed
populations. Aggregated knowledge on the different sub-
mechanisms and bioprocesses occurring in commercial sea-
cages is therefore rapidly expanding. However, before this
knowledge can be put to use for decision support on a cage
level, it needs to be structured to provide information relevant
for the processes occurring in the cage. Mathematical
modelling of systems dynamics is a tool commonly used for
such inference, structuring and aggregating knowledge by
synthesising information from different subsystems into a
complete system representation. A mathematical model of a
dynamic system can often predict how the system will

182

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

Table 2 e Sensor systems and monitoring methods commonly used to observe Animal variables in aquaculture industry
and research, and some properties of these systems.

Sensor type

Sonar

Sensor
implementation

Single beam sonar
Split-beam sonar

Multibeam sonar

Hydroacoustic
Telemetry
Passive

hydroacoustic
sensing

Camera

Individual ﬁsh tags

Hydrophone

Surface camera
Feeding camera
(submerged)

Stereo camera
(submerged)

Hyperspectral
imager
Multispectral imager

Animal variables

Information level

Sensing range

Biomass depth distribution within beam
Biomass depth distribution
Movement dynamics (position, speed) within beam
Biomass depth distribution
Movement dynamics (position, speed) within entire
cage volume
Feed pellet detection
E.g. depth, position, acceleration and spatial
orientation
Sound emitted from ﬁsh population, general
soundscape

Surface activity (jumping/splashing)
Sea-lice count
Skin characteristics (scratches, wounds)
Behavioural characteristics (e.g. systematic vs.
chaotic swimming patterns, normal vs. unexpected
behaviour)
Species identiﬁcation
Sea-lice count
Skin characteristics (scratches, wounds)
Behavioural characteristics (e.g. systematic vs.
chaotic swimming patterns, normal vs. unexpected
behaviour)
Species identiﬁcation
Swimming speed and direction
Size estimation
Skin spectral characteristics
Sea-lice detection and -count
Detection of spectral signatures
Sea-lice count

Group
Individual based group

1 - 200 m
1 - 200 m

Group

1 - 200 m

Individual history

0 - 1000 m

Group

0 - 50 m

Group
Individual based group

0.5e30 m
0.5e25 m

Individual based group

0.5e25 m

Individual based group

0.5e25 m

Individual based group

0.5e25 m

Fig. 2 e Illustration of how four systems based on different monitoring principles could be deployed in a commercial cage to
observe the ﬁsh. While the surface camera (1), underwater stereo video camera (2) and sonar system (3) produce data on the
ﬁsh within a sub-volume in the cage (delimited by dashed lines for each system), the acoustic telemetry system (4) may
collect data on the individual ﬁsh carrying acoustic transmitters irrespective of their location in the cage.

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

183

respond given a speciﬁc set of inputs, and may estimate fea-
tures of the system that are difﬁcult or impossible to measure
directly. In aquaculture research, mathematical models exist
to estimate ﬁsh growth (e.g. Bar, Sigholt, Shearer, & Krogdahl,
2007; Dumas, France, & Bureau, 2010; Føre et al., 2016; Olsen &
Balchen, 1992) and behaviour (Føre, Dempster, Alfredsen,
Johansen, & Johansson, 2009). Such models are good candi-
dates as a foundation for PFF-methods aimed at interpreta-
tion, as they could predict or estimate properties of the ﬁsh
based on measured inputs. These inputs will often include
various types of auxiliary data (e.g. environmental measure-
ments, feed delivery and feeding schedules) required to drive
the model dynamics, but may also include measured Animal
variables that the model could then convert into Feature
variables more useful for decision support. For instance, a
recent study sought to estimate the economic yield of a pro-
duction operation by combining a model of sea bream growth
with temperature as input with simulations of sales plans and
strategies (Estruch, Mayer, Roig, & Jover, 2017). Another
example of such use of mathematical models could be to use a
mathematical model to estimate Feature variables such as the
feeding activity of the ﬁsh, the distribution of waste material
in the water, or vertical ﬁsh swimming speeds based on Ani-
mal variables such as vertical distribution obtained with an
echo sounder as input. Mathematical models representing
elements of the environment in production units also exist,
covering subjects such as spatial and temporal feed distribu-
tion in sea-cages (Alver, Alfredsen, & Sigholt, 2004; Alver et al.,
2016). If provided with sufﬁciently good input data, such
models could estimate Feature variables not directly associ-
ated with the ﬁsh but
rather with the production
environment.

for a wide range of

The use of mathematical models to estimate unobserved
states in complex systems has a long history within control
engineering, and is realised by including the mathematical
model into an observer structure, either based on statistical
methods such as Kalman ﬁltering (Brown & Hwang, 1997) or
by using non-linear observer methods (Fossen, 2002). Such
applications allow the combination of existing knowledge
(through mathematical models) with real-time data from
sensors to provide better estimates than it is possible to obtain
with either sensors or models alone. Estimation techniques
are useful
industrial applications,
including vessel guidance and navigation (e.g. Fossen & Perez,
2009), oil and gas production (e.g. Geir, Mannseth, & Vefring,
2002) and the automotive industry (e.g. Wenzel, Burnham,
Blundell, & Williams, 2007), and are well-established
methods in all of these ﬁelds. Since caged ﬁsh production is
a predominantly biological process, it is more difﬁcult to
measure the different states and processes directly than in
more technically-oriented industries. By this reasoning, it is
likely that extensive use of estimators based on mathematical
models will be necessary components when deriving the PFF
methods of the future, as precision farming will require a
better foundation for information than is available through
present monitoring methods.

3.2.3. Decide: Target variables from feature variables
All important decisions in present day ﬁsh aquaculture are
made by humans based on the interpretation of observations

of the ﬁsh and other cage processes based on personal expe-
rience, and the use of protocols, legislation and recommen-
dations on farm management. This will probably still be the
case in the near future for ﬁsh farming operations, as making
the “right” decision is a complex task that is difﬁcult to assign
to computer-based systems without running a risk of un-
foreseen and potentially undesirable side effects (e.g. sub-
optimal feeding due to limited data on ﬁsh responses). How-
ever, when ﬁsh farming operations are moved to more
exposed and remote areas, limited human access will increase
the need for autonomy in central tasks such as feeding
(Bjelland et al., 2015, pp. 1e10). Limited human presence also
means that decision-making processes need to be at least
partly automated. Although there exist no systems for auto-
mated decision making or decision support that are operative
within the aquaculture industry, advances in artiﬁcial intel-
ligence and information technology have led to the develop-
ment of Decision Support Systems (DSS). A DSS is a computer
tool that for a given situation or problem combines inputs (e.g.
from sensors or mathematical models) and historical user
experiences (i.e. from similar situations or problems previ-
ously experienced)
into compound output values. These
output values are used by the DSS as a foundation on which to
suggest an appropriate decision, and are in fact Target vari-
ables within the PLF/PFF terminology. DSS methods are used
in several industries, including oil and gas (e.g. Gundersen,
Sørmo, Aamodt, & Skalle, 2012), ﬁnance (e.g. Ravisankar,
Ravi, Rao, & Bose, 2011) and medicine (e.g. Montani et al.,
2003).

An example of research that aspires to go in the direction of
DSS for ﬁsh farming is found in the proposed concept of using
the ﬁsh as biological warning systems (BWS) for monitoring
seafood safety (Eguiraun, Izagirre, & Martinez, 2015a). Fish
would be monitored online using technological methods (e.g.
computer vision) to detect atypical behaviour or responses in
the ﬁsh that imply that the animals are affected by external
perturbations, possibly indicating e.g. the presence of noxious
substances. Another example of DSS-oriented research in ﬁsh
farming is given by Føre, Dempster, Alfredsen, and Oppedal
(2013) who used a mathematical model to predict how vary-
ing the depth of submerged artiﬁcial lights could be used to
steer the swimming depth of salmon. Combined with online
proﬁling of the temperature gradient at a site, such a model
could be used to suggest light placement depths with the
intent of optimising the thermal history of the ﬁsh, leading to
improved conditions for optimising ﬁsh growth. Controlling
ﬁsh swimming depth is also a strategy to prevent sea-lice in-
festations by selecting the light placement depths such that
the ﬁsh are steered away from the depth ranges in which the
majority of the sea-lice reside (Frenzl et al., 2014). This would
require indications of when the densities of copepodites in the
water are high, and at which depths (e.g. Oppedal et al., 2017).
Such methods could also be combined with automatically
submersible cages or other actions.

3.2.4. Act: manipulating system and eliciting desired bio-
responses
Most actions that incite bio-responses at ﬁsh farms are
manually controlled, and often include the manual operation
of mechanical equipment (e.g. winches, cranes, crowding nets

184

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

and ropes). The task of converting a speciﬁc decision into the
proper control signals or physical actions that elicit the
desired response is assigned to a human operator. An
important exception from this is the centralised feeding sys-
tems employed at most commercial ﬁsh farms. These systems
are designed to convert decision level inputs such as cage
speciﬁc feeding rates and feeding time schedules into the
electrical signals (e.g. blower frequency, feed sluice opening
rate and feed hose selector) required for the feeding process to
achieve the desired system response.

In earlier days, most of the necessary underwater actions
at ﬁsh farms were conducted by divers. Today it has become
common to use Remotely Operated Vehicles (ROVs) for such
tasks, greatly reducing the risks of personnel
injuries.
Although ROVs are most often controlled by human pilots,
recent research has demonstrated the possibility of using
acoustic positioning methods (Rundtop & Frank, 2016) and
computer vision-based systems (Duda, Schwendner, Stahl, &
Rundtop, 2015, pp. 1e6) to improve the navigation of ROVs
in and around cages, increasing the precision in remote op-
erations. The use of this type of technology could also be
extended to Autonomous Underwater Vehicles (AUVs) that
move without human interference, and that could in turn be
equipped to conduct minor repairs and other underwater
tasks autonomously. AUVs have been used for different pur-
poses within several industries, including hydrographic sur-
veys, inspections and prospecting for oil and gas applications,
ship hull inspections and military applications (Nicholson &
Healey, 2008).

3.2.5. Closed loop Precision Fish Farming applications
At present, there exist no examples of systems that may be
branded closed-loop PFF-applications in farm-based ﬁsh
aquaculture, encompassing the span from observing Animal
variables to actuation that elicits a bio-response in the ﬁsh.
However, as the general level of technology in the world in-
creases, the equipment commercially available to the ﬁsh
farming industry also becomes more technically advanced
and better able to handle more complex tasks. For instance,
devices such as biomass frames (e.g. the VAKI Biomass Daily
system, Pentair Aquatic Eco-systems Inc.) may be argued to
cover both the Observe and Interpret phases in the farming
cycle (Fig. 1), as they optically scan the ﬁsh, estimate indi-
vidual volumes based on the scanning data, and then estimate
weight distributions based on these numbers. However, there
are few examples of solutions that seek also to cover the
Decide and Act phases, which often entail human interven-
tion. This aspect is also reﬂected in the fact that the number
and diversity of systems pertaining to each of the different
phases as outlined above is higher for Observe and Interpret
than for the other two.

However, there are examples of such initiatives within
research on live feed production, where different cybernetic
methods (i.e. mathematical modelling, sensor technology and
automated control) have been successfully applied to auto-
matically control feeding, and hence culture growth (Alver,
Alfredsen, & Øie, 2007; Alver, Alfredsen, Øie, Storøy, & Olsen,
2010). Although this industrial segment differs greatly from
cage-based ﬁsh farming in both scale and facilities, both are
focused on the husbandry of live aquatic animals, and since

such methods are possible to develop for live feed production,
similar approaches may apply to farm-based ﬁsh production.
This potential is even greater for land-based production of ﬁsh
in onshore tanks, where the ability to control core aspects of
the production environment (e.g. temperature, oxygen, ﬂow)
is substantially higher than for cage-based production.

3.2.6. Challenges for industrialisation
Many of the technology principles that are potential tools in
the realisation of industrial PFF applications have been used
industrially and commercially in other market segments, and
several have also seen some use within aquaculture. Howev-
er, for many of these, there exist speciﬁc technical challenges
related to the basic physics of the subsurface environment,
properties pertaining to the selected sensing methods, or
limitations of communication protocols when used in a ﬁsh
farm setting. These challenges need to be overcome before a
full step towards commercial exploitation in aquaculture is
possible. Potential methods to handle such challenges may
range from the implementation of new product features,
through adjustment of system settings, to more strategic
equipment placement (Table 3).

Potential industrial applications of

4.
Precision Fish Farming

reducing ﬁsh losses (e.g.

To be of industrial value, a PFF method must positively affect
the day-to-day farming situation. PFF methods must therefore
be evaluated to test their contributions to improving ﬁsh
welfare and health,
through
handling, escapes and disease), improving production efﬁ-
ciency and product quality, and/or reducing environmental
impacts of the farming operation, prior to launching innova-
tive actions with the intent of commercialisation. Although it
would be more practical to conduct proof of concept studies
for PFF methods in controlled laboratory conditions, demon-
strating their effects under full scale farming conditions is
critical, as culture scale effects modify ﬁsh performance
(cid:1)
Asga˚ rd, & Terjesen, 2017; Føre et al.,
(Espmark, Kolarevic,
2016). Furthermore, as ﬁsh farming operations are primarily
conducted outdoors, any piece of equipment or system
located at the farming site will be exposed to the elements. PFF
methods should thus be tested for durability to prevent
equipment malfunction when used on commercial sites.

To illustrate the implementation of PFF methods, we
outline four concrete examples of PFF applications that are
realistic to implement given present technology readiness
levels, and could have a large impact within industrial ﬁsh
farming. The cases cover important areas in the salmon in-
dustry, ranging from biomass monitoring and feeding to
parasite management. Moreover, the examples illustrate how
PFF principles can be applied to continuous (i.e. throughout
the production cycle), regular (i.e. daily) or transient (i.e. oc-
casionally, on demand) time scales.

4.1.

Case 1: automated biomass monitoring

Cage population properties such as total biomass, number of
ﬁsh and ﬁsh size distribution in a cage are key inputs to many

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

185

Table 3 e Technology principles that are industrially applied in other segments, and the main challenges of introducing
these to industrial aquaculture.

Present industrial
applications

Main challenges in transfer to
industrial aquaculture

Suggested remedies

Technology
principle

Sonar

Acoustic telemetry

tags

Passive acoustics

Computer vision

Remote controlled or

autonomous
vehicles (ROV/
AUV)

Observers (Kalman

ﬁltering, nonlinear
observers)

Seismic surveys,
stock assessment in
ﬁsheries

Fish conservation
and ecology studies
in relation to
hydroelectric dams

Difﬁcult to capture behavioural details on
high density populations
Complex datasets that may be difﬁcult to
visualise in relevant manners
Complex and time consuming tag
deployment through surgery

Low bandwidth of acoustic
communications channel
Difﬁcult to ensure that tagged ﬁsh are
representative for the population

Terrestrial livestock
production
Medicine, robotics,
manufacturing and
mass- production

Oil and gas,
shipping, military

Limited knowledge on relation between
sound and Animal variables of salmon
High turbidity caused by e.g. feed particles
or net cleaning particles
Suboptimal lighting conditions during
winter/at night-time
Risk of hitting structures/ﬁsh while
navigating cage volume

Vessel GNC, oil and
gas, automotive

Risk of ﬁsh responding to presence of
vehicle
Insufﬁcient reliability and quality in
sensor data

Decision Support
Systems (DSS)

Oil and gas, ﬁnance,
medicine

Lack of mechanistic mathematical models
of biological dynamics
Insufﬁcient reliability and quality in
sensor data

Difﬁculties obtaining detailed descriptions
of user experiences

Use higher acoustic frequencies for higher spatial
resolution
Develop visualisation concepts customised to
applications (e.g. feeding)
Enable more efﬁcient and simple tagging by e.g.
miniaturising tag sizes or using other principles
such as oral tagging
Improved communication protocols based on e.g.
chirp/sweep signals and TDMA principles
Increase percentage monitored ﬁsh through
more efﬁcient tagging methods and higher
bandwidth
Long term monitoring in parallel with other
systems to generate new knowledge
Strategic camera placement during feeding/
cleaning operations
UV lights invisible to ﬁsh

Equip vehicle with acoustic/computer vision
based navigation means, giving input to adaptive
mission planning systems
Incorporate control system features enabling the
vehicle to adapt to ﬁsh responses
Using more sensors and higher sampling rates
than deemed necessary from a theoretical
viewpoint
Use system identiﬁcation principles to derive
input/output relations
Increase robustness of instruments and
communication channels to prolonged
submersion in sea water
Introduce routines for systematic registration of
metadata during farm operations

important decisions in the salmon production process,
including the determination of medicinal dosages, assign-
ment of proper feed rations and estimation of total production
yield when selling the ﬁsh before slaughter. Although systems
exist to estimate individual ﬁsh sizes and ﬁsh size distribution
(e.g. biomass frames, stereo vision systems), these only pro-
vide data relevant for their location in the cage, and hence
cannot deliver representative data for the entire cage popu-
lation (Folkedal et al., 2012). This means that decisions where
the total biomass, biomass distribution or number of ﬁsh in a
cage are used as inputs partly need to rely on experience-
based estimates provided by farmers rather than on a
knowledge-based, objective source.

Due to their importance in central farm management de-
cisions, the ability to predict and quantify such population
properties in sea-cages has become a “holy grail” in the
salmon farming industry. One way of applying the PFF prin-
ciples to this challenge is to ﬁrst identify the relevant Feature
variables. Feature variables in this case could be the total
biomass in the cage, the total number of ﬁsh in the population
and the individual size distribution of
the population.
Although recent studies have demonstrated the potential of
using sonar-based solutions to monitor individual ﬁsh mass
(Soliveres et al., 2017), no existing technological solutions for

salmon farming are able to provide data on all these Feature
variables directly. It is therefore necessary to develop solu-
tions that derive such data by combining data on different
Animal variables, possibly obtained with several different
technologies. One possible selection of Animal variables for
this purpose could be vertical distribution (sonar) and point
measurements of individual size distribution (biomass frames
and stereo vision systems). These variables could be com-
bined into a variable estimating the size distribution of the
population, by using echograms from the sonar to determine
the vertical distribution of biomass in the cage and biomass
frames and/or stereo vision systems placed at different depths
to observe vertical variations in individual ﬁsh size. However,
although this scheme would provide new knowledge on
population-wide variations in size and vertical variations in
biomass properties that are useful properties in their own
right, no combination of these two Animal variables can be
used to estimate the total number of ﬁsh or biomass in the
cage directly. One way of achieving such knowledge could be
to combine the incoming Animal variable data streams with
mathematical models of the behavioural and growth dy-
namics of salmon (e.g. Føre et al., 2016, Fig. 3) in an estimator
structure, such as a Kalman ﬁlter. If the model is fed sufﬁ-
ciently detailed data on the external factors tied to the

186

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

activity of the ﬁsh, and adjust the feeding rates accordingly if
they interpret the ﬁsh to be less responsive towards the feed
or otherwise indicate lowered appetite. Although this im-
proves the association between feed delivery and the biolog-
ical processes in the cage, the interpretation of the ﬁsh
responses is experience-based, and hence depends on the
experience and skills of the individual farmer. This method
has been demonstrated to occasionally lead to good growth
rates and feed conversion factors (i.e. kg ﬁsh produced per kg
feed), but the outcomes will vary much between operators and
sites. Furthermore, for locations in remote or exposed (with
regards to wind, current and waves) locations it may not be
possible for personnel to be present every day. For such lo-
cations, fully automated or remotely controlled feeding is
crucial for farm operation.

(of

Better precision and monitoring tools in feed delivery to
salmon cages would improve the predictability and observ-
ability of feed consumption in the ﬁsh population, which in
turn could enable reductions in production costs and envi-
ronmental impacts while improving growth. This could be
solved by applying the principles of PFF to shift feeding
management
from comprising largely experience-driven
processes to become a more knowledge-driven procedure.
Suitable Animal variables for this application could be vertical
distribution and movement
individual ﬁsh and ﬁsh
groups), and individual swimming behaviour (e.g. speed and
direction), both of which are inﬂuenced by the feeding moti-
vation of the ﬁsh (Oppedal et al., 2011). Available technologies
to observe such variables include sonars (vertical distribution,
e.g. Bjordal, Juell, Lindem, & Femo, 1993, p. 203; the CageEye
system, Lindem Data Acquisition AS), computer vision tech-
niques (swimming speed, direction and acceleration through
optical ﬂow and motion pattern analysis techniques, e.g.
Stahl, 2009; Stahl & Aamo, 2011; Stahl et al., 2012) and acoustic
telemetry (depth movements and activity levels, e.g. Føre
et al., 2011, Fig. 4). Although it is possible to derive Feature
variables reﬂecting the appetite or feeding motivation of the
ﬁsh based on the data provided by each of these technologies
alone, it is possible that a more reliable and precise indicator
would combine information gained from several technologies.
Moreover, the importance of efﬁcient feed use for the overall
proﬁtability of any salmon farming enterprise renders the
extra investments required to achieve a Feature variable that
combines several Animal variables from different sources
worthwhile, granted that the increased precision leads to
improved proﬁts or reduced negative externalities. Such
compound Feature variables could, for instance, combine the
occurrence of shifts in the vertical distribution towards/away
from the feeding area with increases/decreases in individual
variability in swimming direction.

To design an automated algorithm (e.g. a DSS) that uses
selected Feature variables to provide advice on whether or not
the present feeding regime should be adjusted requires that
datasets for the chosen Feature variables be collected for both
feeding and non-feeding periods. The algorithm could then
compare present trends and state values of the Feature vari-
ables to those previously observed during different phases of
feeding (i.e. beginning, midway through and towards the end
of the feeding period), and while feed is unavailable to identify
which state the ﬁsh are in with regards to feeding response.

Fig. 3 e Example of comparison between numerical model
output (solid line) and experimental data obtained with
biomass frame and manual sampling (circles). The grey
dashed line marks the onset of PD-disease in the cage.
Figure is modiﬁed from Føre et al. (2016).

(e.g.

environmental
temperature levels, sea-states) and
management-related (e.g. feed delivery rate) states in the cage
that inﬂuence ﬁsh growth, it can estimate the growth dy-
namics in the cage. By adjusting the estimated size distribu-
tion and vertical distributions based on the monitored Animal
variables, the estimator structure will ensure that the popu-
lation size and dynamics outputs from the estimator adhere to
both the historical knowledge included in the model and the
real-time data obtained from the sensors. Although this
approach is sensitive to both measurement errors and inac-
curacies in model equations and parameters, estimates will
probably be more reliable than those gained from standalone
model simulations.

Since several of the monitoring and simulation tools
required in the Observe and Interpret phases for this case
study already exist, achieving a closed loop PFF application
would primarily require more research into new methods to
integrate data from different sources with simulation data.
However, as Feature variables describing aspects of the
biomass contain information that is relevant for a wide vari-
ety of farming applications, it does not make sense to link
these to speciﬁc Target variables.

4.2.

Case 2: automated feeding strategies and control

The objectives of feeding processes in commercial salmon
sea-cages are to ensure that every ﬁsh is provided with sufﬁ-
cient feed to maintain desired growth rates, and keep feed loss
to the environment at a minimum. Since these two aims often
conﬂict (i.e. overfeeding may give good growth rates but may
result in more feed spillage and vice versa for underfeeding),
this is an everyday trade-off in the industry that has conse-
quences for both ﬁsh welfare and farm economy. Feed cost
accounts for about 50% of total production costs from egg to
marketable ﬁsh and thus is the most signiﬁcant single
expense in salmon production. Feeding strategies in salmon
production are largely based on feeding tables that suggest
feed amounts as a function of population size and tempera-
ture. In addition, farmers tend to use submerged cameras
aimed at the feeding area to manually monitor the feeding

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

187

Fig. 4 e Example data from acoustic telemetry describing the vertical positioning (a, b) and vertical movement speeds (c, d) of
two individual ﬁsh during feeding. Grey bars denote feeding periods. Figure is modiﬁed from Føre et al. (2011).

This would represent the Target variable of this application
upon which the decisions of whether feeding rates should be
kept constant, reduced or increased to best accommodate the
ﬁsh are made. The Target variable could also include inputs
from mathematical models that predict the spatial and tem-
poral distribution of feed pellets (Alver et al., 2016) and/or
sonar solutions able to detect uneaten pellets in the water
column (Llorens, P(cid:3)erez-Arjona, Soliveres, & Espinosa, 2017).
This could improve the quality of the decision making process
by also accounting for the physical and hydrodynamic aspects
of feed distribution in cages.

Since automated feeding systems are used throughout the
salmon industry today, the ﬁnal stage of PFF applications
aimed at feeding operations simply entails feeding the output
from the automated decision making algorithm into the
feeding system. As these systems typically rely on human
operators, the required inputs are in forms (e.g. feed amount
per time unit, total feed amounts) that are simple to derive
from Target variables. Considering that many of the sensor
solutions required to collect data relevant for this case study
in the Observe phase exist, obtaining a closed loop application
would therefore primarily require research into new methods
to assimilate data from different sources into compound
Feature variables, and new algorithms to derive the proper

Target variables from these. With the development of more
complex feeding systems, feed placement could also be opti-
mised spatially, based on derived Feature variables. Depend-
ing on the present location of ﬁsh within the sea cage,
direction and speed of the water ﬂow, feed could then be
placed further upstream to reduce feed loss and increase
availability for the ﬁsh (Skøien, 2017).

Case 3: automated monitoring of sea-lice levels in

4.3.
salmon farms

Norwegian salmon farms are legally required to regularly
report sea-lice levels in their cages. Sea-lice levels are
assessed manually by counting the number of lice attached to
a selection of individual ﬁsh retrieved from approximately
half the cages on the site, and then ﬁnding the average value
of the individual counts. If the average sea-lice number per
ﬁsh exceeds the legal limit, the farmer must promptly delouse
the farm. Apart from being labour intensive and costly, the
louse assessment process impacts some ﬁsh as they have to
be captured, handled and sedated prior to the actual counting.
Manual counting is also subject to variable weather conditions
and subjective bias, while small stages of sea-lice are difﬁcult
to see and hence assumed to be strongly underestimated in

188

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

these counts. Furthermore, the fact that the ﬁsh need to be
captured to contribute to the dataset raises the question of
representability; are 10e20 individual ﬁsh retrieved near the
surface representative of the full population kept in the cage?
As recent data suggests that salmon with more sea-lice swim
deeper (Bui, Oppedal, Stien, & Dempster, 2016), present
counting methods are likely to underestimate lice levels.

Considering the costs and labour associated with sea-lice
counting, and the potential consequences of having inaccu-
rate lice counts, this operation is a good candidate for auto-
mation through PFF methods. The ﬁrst step would be to
identify Animal variables that may serve as a foundation for
acquiring the desired Feature variable - sea-lice infestation
levels. With the precondition that ﬁsh handling should be
avoided, variables observable through optical methods appear
best suited. For instance, Furevik, Bjordal, Huse, and Fern€o
(1993) found that lice infestation levels could be expressed in
the jumping frequency of salmon in sea-cages, a behavioural
trait automatically detectable using computer vision methods
(Jovanovi(cid:3)c et al., 2016, Fig. 5). This approach is attractive as it
applies video recorded using elevated cameras, making the
acquisition of useful and affordable camera solutions easier
than in the subsurface environment. Underwater video re-
cordings and computer vision might also detect sea-lice
directly. This could be done using spectral analysis to distin-
guish between sea-lice and salmon skin (Tillett et al., 1999) or
hyperspectral analyses to detect changes in skin texture and
colour caused by louse infestation (Nolan, Reilly, & Bonga,
1999). While these methods would probably require more
expensive equipment, they are more direct approaches to the
problem rather than using surface activity as a proxy measure.
This principle is used to detect sea-lice in the commercially
available Stingray system (Stingray Marine Solutions AS).

An automated algorithm constantly evaluating the esti-
mated sea-lice numbers (Feature variable) against the legally
set maximum limits for sea-lice infestation could then be set
to alert the farmer when the detections approach levels that
require action (Target variable). The Feature variable of this
application could be combined with a mathematical model of
louse population dynamics (e.g. Stien, Bjørn, Heuch, & Elston,

2005) in an estimator structure to better predict population
dynamics and enable better planning of delousing operations.
Since contemporary approaches to remove sea-lice from
salmon vary greatly in delousing principle (e.g. chemical,
freshwater, thermal, mechanical), equipment selection (e.g.
pump types, presence of skirts) and ﬁsh manipulation
methods (e.g. crowding, use of dip nets, well boats), an auto-
mated Action based on the Target variable could be difﬁcult to
derive at present. However, given the costs of sea-lice to both
ﬁsh and farmers, just the ability to monitor sea-lice infesta-
tion levels automatically and continuously would be highly
useful. The Gold Standard required to validate this method
could be obtained by conducting manual sea-lice assessments
in parallel with the applications of the technology. Assuming
the transition from Feature variable to Target variable is set by
legal limits, the main research challenges in deriving closed
loop PFF applications for this case study would lie in devel-
oping robust and representative methods to assess lice
numbers based on the aforementioned existing sensor sys-
tems, and in adapting different delousing procedures to the
resulting Target variable.

Case 4: automated crowding control during

4.4.
delousing operations

The ability to delouse salmon cages efﬁciently when sea-lice
counts exceed legal limits is critical, as uncontrolled out-
breaks of sea-lice may lead to impaired ﬁsh welfare and
health, and have severe consequences for wild salmonids in
the environment near the farm. Common delousing methods
include immersing the ﬁsh in closed/semi-closed volumes
(either in the sea or in well boats) containing anti-louse
lump-
chemicals, the use of cleaner ﬁsh (e.g. wrasses,
suckers) that eat the sea-lice, and the application of medicated
feeds. However, as sea-lice infestation numbers have recently
increased, so has the intensity of the treatment regimes at
salmon farms. Farmed salmon populations are now subjected
to a larger number of treatments during their life cycle than
was the case a decade ago. An unfortunate side effect of this
development is that sea-lice populations frequently exposed

Fig. 5 e Example of automatic detection of surface activity in salmon cages using computer vision methods. Each red square
marks the detection of a splash be caused by ﬁsh. Reproduced from Jovanovi(cid:3)c et al. (2016) with permission of copyright
holder.

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

189

to medicinal treatments have undergone a survival-driven
genetic selection for resistance against these substances,
which in turn has rendered many of the previously most
efﬁcient anti-louse chemicals ineffective (Aaen, Helgesen,
Bakke, Kaur, & Horsberg, 2015). This has forced the industry
to search for alternative methods of treating their ﬁsh and it is
today common to use non-medicinal treatment methods such
as freshwater,
thermal or mechanical delousing. These
methods often require that the ﬁsh be ﬁrst crowded at higher
than normal densities, then pumped from the cage, through a
barge or ship that contains the system used for delousing, and
back into a different section of the cage or into a new cage.
When ﬁsh are crowded at very high concentrations, they may
experience impaired culture conditions that induce negative
effects such as hypoxia, mechanical damage, and increased
stress levels. Crowding may subject the ﬁsh to lowered wel-
fare and lead to detrimental health and increased mortality,
adding to the potential negative welfare impacts caused by
the delousing process. This is a considerable challenge for the
salmon industry.

A PFF application that automatically monitors the states of
the salmon before, during and after a delousing operation
would be a tool to reduce the risks associated with crowding of
farmed ﬁsh. This method could present alarm signals to the
farmer if the states of the ﬁsh imply that the crowding process
inﬂicts unacceptable stress levels or physical strains on the
ﬁsh. The ﬁrst step of developing the method would be to
identify which technologies to use in the Observe phase.
Submerged cameras coupled with computer vision algorithms
could detect motion-based Animal variables that hold infor-
mation about stress levels, such as swimming speeds and
respiration rates, and detect deviations in skin condition
implying damage or sores. Another alternative could be to use
sonar (e.g. Fig. 6). As for cameras, the information obtained via
sonar describes the responses of sub-groups in the popula-
tion. However, whereas the group size observable with optical

means is limited by visibility, sonars can cover larger sub-
volumes of the cage and provide data on larger groups of
ﬁsh (Table 2). Although the cost of this lies in the fact that the
level of detail in the resulting data is lower than when using
cameras, such systems can describe Animal variables such as
vertical movement and distribution patterns (e.g. Johansson
et al., 2006; Oppedal et al., 2007), and swimming speed and
direction for individuals when using split-beam technology
(Knudsen et al., 2004).

Another possible technology for this purpose is the wire-
less monitoring of individual ﬁsh through acoustic telemetry.
Although the ﬁsh need to be handled and subjected to surgery
when deploying telemetry transmitters, there are several
properties making telemetry attractive for this application.
First, while data from cameras and sonar describe ﬁsh states
on a group level, telemetry results in data histories for indi-
vidual ﬁsh, enabling a direct link to the states of the in-
dividuals that are the basic units of the ﬁsh population
system. Second, the detection range of acoustic telemetry
systems may extend from several 100 m to kilometres,
meaning that it is possible to obtain continuous datasets
spanning all stages of the process (i.e. crowding, delousing
and moving the ﬁsh to a new cage) without having to move the
acoustic receivers. In contrast, camera systems and sonar
need to be placed within the cage and removed during
delousing and crowding to avoid interference with cage
manipulation and other operations. Such systems will be less
able to capture responses during the operation and also have
to be moved to the new cage after transfer. Third, acoustic
transmitters may be equipped with a wide variety of different
sensors that are commercially available, enabling the direct
measurement of ﬁsh states to derive relevant Animal vari-
ables (e.g. accelerometers - activity levels, pressure sensors e
vertical movement speeds).

Irrespective of monitoring technology, a baseline dataset
describing the “non-stressed” states and response patterns of

Fig. 6 e Echogram obtained with a split-beam sonar system describing the changes in the vertical dynamics of salmon in a
commercial cage when the net bottom is raised from 18 m to 11 m (raising occurs around 04:37:00) during a crowding
operation. Unpublished data, SINTEF Ocean.

190

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

the ﬁsh is required to facilitate interpretation. The easiest way
to obtain such data is to monitor the ﬁsh for a period prior to
the operation using the same monitoring regime as planned
during crowding. Automated algorithms could then search for
deviations from the data values and trends seen for unper-
turbed ﬁsh in the non-crowding periods, and label these as
Feature variables that could imply increased stress levels. A
DSS could then evaluate these Feature variables against his-
torical data from previous delousing processes to provide a
recommendation of whether
the operation should be
continued, halted or aborted, which would be the Target
variable of the application. The historical data used as the
basis for the decision making process would need to include
datasets describing the same Animal and Feature variables as
those assembled by the chosen method, together with meta-
data/information describing the impact the operation had on
ﬁsh welfare and/or mortality for each particular operation.
Such datasets could also represent Gold Standards with which
the method can be validated.

For this application, it would also be possible to implement
a method for directly operating actuators based on the Target
variable. This could be realised using automatically controlled
winches to raise the net bottom during crowding (e.g. winches
from the Midgard system, Aqualine AS). These winches could
be programmed to follow a pre-deﬁned schedule of crowding
that gradually reduced the volume available for the ﬁsh. The
DSS could be set with the capability of overriding the winch
system, so that the crowding process is halted or reversed if
real time data implies a situation that may lead to impaired
welfare or increased mortality. This application would thus be
an example of a full closed loop PFF method. Considering the
commercial availability of relevant sensors for data collection
and winches for net actuation, the main research challenges of
achieving closed loop PFF would in this case pertain to deriving
the relationships between observable Animal variables and
Feature variables suitable for decision support, and building up
the necessary knowledge foundation for the DSS to operate on.

Conclusion and recommended future

5.
research efforts

Industrial ﬁsh farming is an important supplier of marine
protein for human consumption. The industry aspires to sup-
ply the increasing demand for seafood arising from the
growing world population. Due to factors such as increasing
scarcity of feed raw materials, limited availability of farming
locations suitable for today's technology level, increasing focus
and demands with respect to eco-friendliness, and space use
conﬂicts with other industries (e.g. ﬁsheries, oil and gas,
tourism, shipping), this challenge is probably not possible to
counter by simply upscaling production volumes and applying
present production regimes. Future methods for ﬁsh farming
will therefore need to be more advanced and smarter, in the
sense that the industry needs to shift from experience-driven
to knowledge-driven approaches to better optimise produc-
tion. The present trends within the industry of farms produc-
ing greater volumes, and production per worker increasing on
each ﬁsh farm, highlight the need to monitor and control the
production process. Exploitation of technological tools will be

central in addressing these challenges, and the Precision Fish
Farming concept seeks to harness this potential in represent-
ing a framework for the development of technologically foun-
ded methods for ﬁsh farming. PFF best practice requires that
methods be validated through Gold Standards before they are
released onto the market. At present, there are few regulations
on introducing new technologies for the ﬁsh farming market,
and no formal or legal requirements for validation prior to
release. Through scientiﬁc documentation, PFF will allow
greater conﬁdence in the usefulness and efﬁciency of
commercially available technologies.

Many components required to create PFF methods exist
today, either as commercially available solutions or as
research tools that can be converted into innovations. Pri-
marily, these solutions are aimed at the Observation phase of
ﬁsh farming operations (Fig. 1), meaning that they are
designed to produce data or information on the expressions of
bio-responses in the farmed ﬁsh. This is not surprising,
considering that the general challenges of observing animals
in the aquatic environment has been pushing the industry to
adapt new technologies to observe the ﬁsh. There are also
several candidate technologies for future innovations aimed
at the interpretation phase, primarily in the form of mathe-
matical models. Most of these are still research tools with
limited direct industrial applications, but models are likely to
become industrialised either on their own or as components
of a larger system. As production units increase in size, the
ability to monitor the states of the caged population through
sensors will decrease,
implying that estimation through
mathematical models may be necessary to make the states of
the system observable. There are fewer examples of estab-
lished methods or tools in the Decide and Act phases of ﬁsh
farming. This is mainly because the realisation of PFF
methods at these stages will require well-established tools for
the Observe and Interpret phases. Hence, as new tools and
innovations aimed at the ﬁrst two phases are realised, the
possibility of developing solutions extending all the way into
the Act phase will increase.

Continued research on technological applications within
all four phases of ﬁsh farming is necessary to realise the po-
tential of PFF in commercial aquaculture. One approach would
be to target this effort towards speciﬁc use cases, meaning
that the motivation is to solve concrete challenges within the
industry using a PFF approach. The case studies of sea-lice
counting and crowding control outlined in this study are ex-
amples of this. Such methods are more case-speciﬁc than
generic, are founded in applied research, and more likely to
have a strong industry appeal. Alternatively, each phase can
be targeted separately, to solve technical challenges such as
reﬁning sensor technologies for better observation of Animal
variables, industrialising mathematical models, developing
automated DSS methods and developing autonomous sys-
tems for cage manipulation. This will require a certain
amount of basic research to understand biological mecha-
nisms in the ﬁsh better, which may have a lower immediate
industrial appeal but stronger long-term effects in providing a
knowledge basis for the development of future methods.
Research in both these directions is necessary to usher in a
technologically oriented ﬁsh farming
new paradigm of
through the Precision Fish Farming concept.

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

191

Acknowledgements

This study is the result of a strategic collaborative effort be-
tween the participating institutions, and has not been funded
through external grants. We dedicate this work to the late
Professor Jens Glad Balchen (1926e2009) who ﬁrst established
the idea of applying cybernetic methods to the production and
capture of aquatic organisms.

r e f e r e n c e s

Aaen, S. M., Helgesen, K. O., Bakke, M. J., Kaur, K., &

Horsberg, T. E. (2015). Drug resistance in sea lice: A threat to
salmonid aquaculture. Trends in Parasitology, 31(2), 72e81.
Alfredsen, J. A., Holand, B., Solvang-Garten, T., & Uglem, I. (2007).
Feeding activity and opercular pressure transients in Atlantic
salmon (Salmo salar L.): Application to feeding management in
ﬁsh farming. Hydrobiologia, 582(1), 199e207.

Alver, M. O., Alfredsen, J. A., & Øie, G. (2007). Estimating larval
density in cod (Gadus morhua) ﬁrst feeding tanks using
measurements of feed density and larval growth rates.
Aquaculture, 268(1), 216e226.

Alver, M. O., Alfredsen, J. A., Øie, G., Storøy, W., & Olsen, Y. (2010).
Automatic control of growth and density in rotifer cultures.
Aquacultural Engineering, 43(1), 6e13.

Alver, M. O., Alfredsen, J. A., & Sigholt, T. (2004). Dynamic

modelling of pellet distribution in Atlantic salmon (Salmo salar
L.) cages. Aquacultural Engineering, 31(1), 51e72.

Alver, M. O., Skøien, K. R., Føre, M., Aas, T. S., Oehme, M., &
Alfredsen, J. A. (2016). Modelling of surface and 3D pellet
distribution in Atlantic salmon (Salmo salar L.) cages.
Aquacultural Engineering, 72, 20e29.

Arrhenius, F., Benneheij, B. J., Rudstam, L. G., & Boisclair, D.

(2000). Can stationary bottom split-beam hydroacoustics be
used to measure ﬁsh swimming speed in situ? Fisheries
Research, 45(1), 31e41.

(cid:1)
Astr€om, K. J., & Eykhoff, P. (1971). System identiﬁcationda survey.

Automatica, 7(2), 123e162.

Balchen, J. G. (1979). Modeling, prediction, and control of ﬁsh

behavior. Control and Dynamic Systems, 15, 99e146.

Baras, E., & Lagard(cid:4)ere, J. P. (1995). Fish telemetry in aquaculture:

Review and perspectives. Aquaculture International, 3(2),
77e102.

Bar, N. S., Sigholt, T., Shearer, K. D., & Krogdahl,

(cid:1)
A. (2007). A
dynamic model of nutrient pathways, growth, and body
composition in ﬁsh. Canadian Journal of Fisheries and Aquatic
Sciences, 64(12), 1669e1682.

Bastianelli, D., & Sauvant, D. (1997). Modelling the mechanisms of

pig growth. Livestock Production Science, 51(1e3), 97e107.

Berckmans, D. (2004). Automatic on-line monitoring of animals by
precision livestock farming. In Proceedings of the ISAH conference
on animal production in Europe: The way forward in a changing
world (Vol. 1, pp. 27e31). Saint-Malo, France, October 11e13.

Berckmans, D. (2013). Basic principles of PLF: Gold standard,

labelling and ﬁeld data. In Proceedings of European conference of
precision livestock farming (pp. 21e29).

Berckmans, D. (2014). Precision livestock farming technologies for
welfare management in intensive livestock systems. Scientiﬁc
and Technical Review of the Ofﬁce International des Epizooties,
33(1), 189e196.

Berckmans, D., Hemeryck, M., Berckmans, D., Vranken, E., & van
Waterschoot, T. (2015). Animal sound… Talks! real-time
sound analysis for health monitoring in livestock. In Proc
animal environment and welfare (pp. 215e222).

Bjelland, H. V., Føre, M., Lader, P., Kristiansen, D., Holmen, I. M.,
Fredheim, A., et al. (2015 October). Exposed aquaculture in
Norway. In OCEANS'15 MTS/IEEE Washington. IEEE.

(cid:1)
A., Juell, J. E., Lindem, T., & Femo, A. (1993). Hydroacoustic

Bjordal,

monitoring and feeding control in cage rearing of Atlantic salmon
(Salmo salar L.). Fish Farming Technology.

Boyd John, R. (1987). A discourse on winning and losing (p. 1). Air

University document MU43947, brieﬁng.

Brodin, T., Fick, J., Jonssom, M., & Klaminder, J. (2013). Dilute

concentrations of a psychiatric drug alter behavior of ﬁsh from
natural populations. Science, 339, 814e815.

Brown, R. G., & Hwang, P. Y. (1997). Introduction to random signals
and applied Kalman ﬁltering: With MATLAB exercises and solutions.
Wiley.

Bui, S., Oppedal, F., Korsøen, Ø. J., Sonny, D., & Dempster, T.

(2013). Group behavioural responses of Atlantic salmon (Salmo
salar L.) to light, infrasound and sound stimuli. PloS One, 8(5).

Bui, S., Oppedal, F., Stien, L., & Dempster, T. (2016). Sea lice

infestation level alters salmon swimming depth in sea-cages.
Aquaculture Environment Interactions, 8, 429e435.

Cooke, S. J., Thorstad, E. B., & Hinch, S. G. (2004). Activity and

energetics of free-swimming ﬁsh: Insights from
electromyogram telemetry. Fish and Fisheries, 5(1), 21e52.
Darr, M., & Epperson, W. (2009). Embedded sensor technology for
real time determination of animal lying time. Computers and
Electronics in Agriculture, 66(1), 106e111.

Deming, W. E., & Edwards, D. W. (1982). Quality, productivity, and
competitive position (Vol. 183). Cambridge, MA: Massachusetts
Institute of Technology, Center for advanced engineering
study.

Duda, A., Schwendner, J., Stahl, A., & Rundtop, P. (2015 May).
Visual pose estimation for autonomous inspection of ﬁsh
pens. In OCEANS 2015-Genova. IEEE.

Dumas, A., France, J., & Bureau, D. (2010). Modelling growth and
body composition in ﬁsh nutrition: Where have we been and
where are we going? Aquaculture Research, 41(2), 161e181.
Eguiraun, H., Izagirre, U., & Martinez, I. (2015a). A paradigm shift
in safe seafood production: From contaminant detection to
ﬁsh monitoring - application of biological warning systems to
aquaculture. Trends in Food Science and Technology, 45, 104e115.
Eguiraun, H., L(cid:3)opez-de-Ipi~na, K., & Martinez, I. (2014). Application
of entropy and fractal dimension analyses to the pattern
recognition of contaminated ﬁsh responses in aquaculture.
Entropy, 16(11), 6133e6151.

Eguiraun, H., Lopez de Ipi~na, K., & Martinez, I. (2016). Shannon
entropy in a European seabass (Dicentrarchus labrax) system
during the initial recovery period after a short term exposure
to methylmercury. Entropy, 18(6), 209e219.

Eguiraun, H., & Martinez, I. (2015b). Evolution of Shannon entropy

in a ﬁsh system (European seabass, Dicentrarchus labrax)
during exposure to sodium selenite (Na2SeO3). In Proceedings
of the 2nd int. Electron. Conf. Entropy appl., 15e30 Nov. 2015;
sciforum electronic conference series (Vol. 2) (session Complex
Systems).

(cid:1)
A. M., Kolarevic, J.,

(cid:1)
Asga˚ rd, T., & Terjesen, B. F. (2017).

Espmark,

Tank size and ﬁsh management history matters in
experimental design. Aquaculture Research, 48(6), 2876e2894.
Estruch, V. D., Mayer, P., Roig, B., & Jover, M. (2017). Developing a
new tool based on a quantile regression mixed-TGC model for
optimizing gilthead sea bream (Sparus aurata L) farm
management. Aquaculture Research, 48(10), 1e12.

FAO. (2016). Aquaculture production: Quantities 1950-2014. Available
from: http://www.fao.org/ﬁshery/aquaculture/en [accessed
February 02 2017].

Finstad, B., Økland, F., Thorstad, E. B., Bjørn, P. A., &

McKinley, R. S. (2005). Migration of hatchery-reared Atlantic
salmon and wild anadromous brown trout post-smolts in a
Norwegian fjord system. Journal of Fish Biology, 66(1), 86e96.

192

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

Folkedal, O., Stien, L. H., Nilsson, J., Torgersen, T.,

Fosseidengen, J. E., & Oppedal, F. (2012). Sea caged Atlantic
salmon display size-dependent swimming depth. Aquatic
Living Resources, 25(2), 143e149.

Føre, M., Alfredsen, J. A., & Gronningsater, A. (2011). Development
of two telemetry-based systems for monitoring the feeding
behaviour of Atlantic salmon (Salmo salar L.) in aquaculture
sea-cages. Computers and Electronics in Agriculture, 76(2),
240e251.

Føre, M., Alver, M., Alfredsen, J. A., Maraﬁoti, G., Senneset, G.,

Birkevold, J., et al. (2016). Modelling growth performance and
feeding behaviour of Atlantic salmon (Salmo salar L.) in
commercial-size aquaculture net pens: Model details and
validation through full-scale experiments. Aquaculture, 464,
268e278.

Føre, M., Dempster, T., Alfredsen, J. A., Johansen, V., &

Johansson, D. (2009). Modelling of Atlantic salmon (Salmo salar
L.) behaviour in sea-cages: A Lagrangian approach.
Aquaculture, 288(3), 196e204.

Føre, M., Dempster, T., Alfredsen, J. A., & Oppedal, F. (2013).

Modelling of Atlantic salmon (Salmo salar L.) behaviour in sea-
cages: Using artiﬁcial light to control swimming depth.
Aquaculture, 388, 137e146.

Føre, M., Frank, K., Dempster, T., Alfredsen, J. A., & Høy, E. (2017).

Biomonitoring using tagged sentinel ﬁsh and acoustic
telemetry in commercial salmon aquaculture: A feasibility
study. Aquacultural Engineering, 78, 163e172. part B.

Fossen, T. I. (2002). Marine control systems: Guidance, navigation and
control of ships, rigs and underwater vehicles (1st ed.). Marine
Cybernetics AS.

Fossen, T. I., & Perez, T. (2009). Kalman ﬁltering for positioning
and heading control of ships and offshore rigs. IEEE Control
Systems, 29(6).

Frenzl, B., Stien, L. H., Cockerill, D., Oppedal, F., Richards, R. H.,
Shinn, A. P., et al. (2014). Manipulation of farmed Atlantic
salmon swimming behaviour through the adjustment of
lighting and feeding regimes as a tool for salmon lice control.
Aquaculture, 424, 183e188.

Frost, A. R., Parsons, D. J., Stacey, K. F., Robertson, A. P.,

Welch, S. K., Filmer, D., et al. (2003). Progress towards the
development of an integrated management system for broiler
chicken production. Computers and Electronics in Agriculture,
39(3), 227e240.
Furevik, D. M., Bjordal,

(cid:1)
A., Huse, I., & Fern€o, A. (1993). Surface

activity of Atlantic salmon (Salmo salar L.) in net pens.
Aquaculture, 110(2), 119e128.

Geir, Æ., Mannseth, T., & Vefring, E. H. (2002 January). Near-well
reservoir monitoring through ensemble Kalman ﬁlter. In SPE/
DOE improved oil recovery symposium. Society of Petroleum
Engineers.

Grimnes, A., & Jakobsen, P. J. (1996). The physiological effects of
salmon lice infection on post-smolt of Atlantic salmon. Journal
of Fish Biology, 48(6), 1179e1194.

Gundersen, O. E., Sørmo, F., Aamodt, A., & Skalle, P. (2012). A real-
time decision support system for high cost oil-well drilling
operations. AI Magazine, 34(1), 21e32.

Hallam, A. (1991). Economies of size and scale in agriculture: An
interpretive review of empirical measurement. Review of
Agricultural Economics, 155e172.

Hao, M., Yu, H., & Li, D. (2016). The measurement of ﬁsh size by

machine vision-a review. In Computer and computing
technologies in agriculture IX: 9th IFIP WG 5.14 international
conference, CCTA 2015, Beijing, China, September 27-30, 2015,
revised selected papers, Part II 9 (pp. 15e32). Springer
International Publishing.

Hedger, R. D., Uglem, I., Thorstad, E. B., Finstad, B.,

Chittenden, C. M., Arechavala-Lopez, P., et al. (2011).
Behaviour of Atlantic cod, a marine ﬁsh predator, during

Atlantic salmon post-smolt migration. ICES Journal of Marine
Science: Journal du Conseil, 2152e2162.

Huse, I., & Ona, E. (1996). Tilt angle distribution and swimming
speed of overwintering Norwegian spring spawning herring.
ICES Journal of Marine Science: Journal du Conseil, 53(5), 863e873.

Iversen, A., Andreassen, O., Hermansen, Ø., Larsen, T. A., &

Terjesen, B. F. (2013). Oppdrettsteknologi og konkurranseposisjon.
Noﬁma rapport 32/2013.

Jensen, Ø., Dempster, T., Thorstad, E. B., Uglem, I., & Fredheim, A.

(2009). Escapes of ﬁshes from Norwegian sea-cage
aquaculture: Causes, consequences and prevention.
Aquaculture Environment Interactions, 1(1), 71e83.
Johansson, D., Ruohonen, K., Kiessling, A., Oppedal, F.,

Stiansen, J. E., Kelly, M., et al. (2006). Effect of environmental
factors on swimming depth preferences of Atlantic salmon
(Salmo salar L.) and temporal and spatial variations in oxygen
levels in sea cages at a fjord site. Aquaculture, 254(1), 594e605.
John, A. J., Clark, C. E. F., Freeman, M. J., Kerrisk, K. L., Garcia, S. C., &
Halachmi, I. (2016). Review: Milking robot utilization, a successful
precision livestock farming evolution. Animal, 10(09), 1484e1492.

Johnson, M., Bradshaw, J. M., Feltovich, P. J., Hoffman, R. R.,

Jonker, C., van Riemsdijk, B., et al. (2011). Beyond cooperative
robotics: The central role of interdependence in coactive
design. IEEE Intelligent Systems, 26(3), 81e88.

Jovanovi(cid:3)c, V., Risojevi(cid:3)c, V., Babi(cid:3)c, Z., Svendsen, E., & Stahl, A.

(2016 May). Splash detection in surveillance videos of offshore
ﬁsh production plants. In Systems, signals and image processing
(IWSSIP), 2016 international conference on (pp. 1e4). IEEE.

Kalogerakis, N., Arff, J., Banat, I. M., Broch, O. J., Daffonchio, D.,

Edvardsen, T., et al. (2015). The role of environmental
biotechnology in exploring, exploiting, monitoring,
preserving, protecting and decontaminating the marine
environment. New Biotechnology, 32(1), 157e167.

Kasumyan, A. O. (2008). Sounds and sound production in ﬁshes.

Journal of Ichthyology, 48(11), 981e1030.

Kasumyan, A. O. (2009). Acoustic signaling in ﬁsh. Journal of

Ichthyology, 49(11), 963e1020.

Knudsen, F. R., Fosseidengen, J. E., Oppedal, F., Karlsen, Ø., &

Ona, E. (2004). Hydroacoustic monitoring of ﬁsh in sea cages:
Target strength (TS) measurements on Atlantic salmon (Salmo
salar). Fisheries Research, 69(2), 205e209.
(cid:1)
A., Baeverfjord, G.,

Kolarevic, J., Aas-Hansen, Ø., Espmark,

Terjesen, B. F., & Damsga˚ rd, B. (2016). The use of acoustic
acceleration transmitter tags for monitoring of Atlantic
salmon swimming activity in recirculating aquaculture
systems (RAS). Aquacultural Engineering, 72, 30e39.

Kristensen, T., & Kristensen, E. S. (1998). Analysis and simulation

modelling of the production in Danish organic and conventional
dairy herds. Livestock Production Science, 54(1), 55e65.

Lader, P., Dempster, T., Fredheim, A., & Jensen, Ø. (2008). Current
induced net deformations in full-scale sea-cages for Atlantic
salmon (Salmo salar). Aquacultural Engineering, 38(1), 52e65.
Llorens, S., P(cid:3)erez-Arjona, I., Soliveres, E., & Espinosa, V. (2017).

Detection and target strength measurements of uneaten feed
pellets with a single beam echosounder. Aquacultural
Engineering, 78, 216e220. part B.

Maatje, K., De Mol, R. M., & Rossing, W. (1997). Cow status

monitoring (health and oestrus) using detection sensors.
Computers and Electronics in Agriculture, 16(3), 245e254.

McVicar, A. H. (1987). Pancreas disease of farmed Atlantic salmon,
Salmo salar, in Scotland: Epidemiology and early pathology.
Aquaculture, 67(1e2), 71e78.

Melvin, G. D. (2016). Observations of in situ Atlantic blueﬁn tuna
(Thunnus thynnus) with 500-kHz multibeam sonar. ICES Journal
of Marine Science: Journal du Conseil, 73(8), 1975e1986.
Milner-Gulland, E. J., Kerven, C., Behnke, R., Wright, I. A., &

Smailov, A. (2006). A multi-agent system model of pastoralist
behaviour in Kazakhstan. Ecological Complexity, 3(1), 23e36.

b i o s y s t e m s e n g i n e e r i n g 1 7 3 ( 2 0 1 8 ) 1 7 6 e1 9 3

193

Montani, S., Magni, P., Bellazzi, R., Larizza, C., Roudsari, A. V., &

Stahl, A. (2009). Dynamic variational motion estimation and video

Carson, E. R. (2003). Integrating model-based decision support
in a multi-modal reasoning system for managing type 1
diabetic patients. Artiﬁcial Intelligence in Medicine, 29(1), 131e151.

Nicholson, J. W., & Healey, A. J. (2008). The present state of
autonomous underwater vehicle (AUV) applications and
technologies. Marine Technology Society Journal, 42(1), 44e51.
Nolan, D. T., Reilly, P., & Bonga, S. W. (1999). Infection with low

numbers of the sea louse Lepeophtheirus salmonis induces stress-
related effects in postsmolt Atlantic salmon (Salmo salar).
Canadian Journal of Fisheries and Aquatic Sciences, 56(6), 947e959.
Norton, T., & Berckmans, D. (2017). Developing precision livestock
farming tools for precision dairy farming. Animal Frontiers, 7(1),
18e23.

Olsen, O. A., & Balchen, J. G. (1992). Structured modeling of ﬁsh

physiology. Mathematical Biosciences, 112(1), 81e113.

Oppedal, F., Dempster, T., & Stien, L. H. (2011). Environmental

drivers of Atlantic salmon behaviour in sea-cages: A review.
Aquaculture, 311(1), 1e18.

Oppedal, F., Juell, J. E., & Johansson, D. (2007). Thermo-and
photoregulatory swimming behaviour of caged Atlantic
salmon: Implications for photoperiod management and ﬁsh
welfare. Aquaculture, 265(1), 70e81.

Oppedal, F., Samsing, F., Dempster, T., Wright, D. W., Bui, S., &
Stien, L. H. (2017). Sea lice infestation levels decrease with
deeper ‘snorkel’barriers in Atlantic salmon sea-cages. Pest
Management Science, 73, 1935e1943.

Pettersen, J. M., Bracke, M., Midtlyng, P. J., Folkedal, O., Stien, L. H.,
Steffenak, H., et al. (2014). Salmon welfare index model 2.0: An
extended model for overall welfare assessment of caged
Atlantic salmon, based on a review of selected welfare
indicators and intended for ﬁsh health professionals. Reviews
in Aquaculture, 6(3), 162e179.

Ravisankar, P., Ravi, V., Rao, G. R., & Bose, I. (2011). Detection of
ﬁnancial statement fraud and feature selection using data
mining techniques. Decision Support Systems, 50(2), 491e500.
Remen, M., Sievers, M., Torgersen, T., & Oppedal, F. (2016). The

oxygen threshold for maximal feed intake of Atlantic salmon
post-smolts is highly temperature-dependent. Aquaculture,
464, 582e592.

Rillahan, C., Chambers, M., Howell, W. H., & Watson, W. H. (2009).
A self-contained system for observing and quantifying the
behavior of Atlantic cod, Gadus morhua, in an offshore
aquaculture cage. Aquaculture, 293(1), 49e56.

Rother, M. (2010). Toyota kata. MacGraw Hill.
Rundtop, P., & Frank, K. (2016). Experimental evaluation of
hydroacoustic instruments for ROV navigation along
aquaculture net pens. Aquacultural Engineering, 74, 143e156.

inpainting with physical priors. Germany: University of
Heidelberg. Doctoral dissertation.

Stahl, A., & Aamo, O. M. (2011). A new framework for motion

estimation in image sequences using optimal ﬂow control. In
Informatics in control, automation and robotics (pp. 307e320).
Springer Berlin Heidelberg.

Stahl, A., Schellewald, C., Stavdahl, Ø., Aamo, O. M., Adde, L., &
Kirkerod, H. (2012). An optical ﬂow-based method to predict
infantile cerebral palsy. IEEE Transactions on Neural Systems and
Rehabilitation Engineering, 20(4), 605e614.

Stien, A., Bjørn, P. A., Heuch, P. A., & Elston, D. A. (2005).

Population dynamics of salmon lice Lepeophtheirus salmonis on
Atlantic salmon and sea trout. Marine Ecology Progress Series,
290, 263e275.

Tebot, I., Bonnet, J. M., Junot, S., Ayoub, J. Y., Paquet, C., & Cirio, A.
(2009). Roles of eating, rumination, and arterial pressure in
determination of the circadian rhythm of renal blood ﬂow in
sheep. Journal of Animal Science, 87(2), 554e561.

Tedeschi, L. O., Fox, D. G., & Guiroy, P. J. (2004). A decision support

system to improve individual cattle management. 1. A
mechanistic, dynamic model for animal growth. Agricultural
Systems, 79(2), 171e204.

Tenningen, M., Macaulay, G. J., Rieucau, G., Pe~na, H., &

Korneliussen, R. J. (2016). Behaviours of Atlantic herring and
mackerel in a purse-seine net, observed using multibeam
sonar. ICES Journal of Marine Science: Journal du Conseil, 74(1),
359e368.

Terrasson, G., Llaria, A., Marra, A., & Voaden, S. (2016 July).

Accelerometer based solution for precision livestock farming:
Geolocation enhancement and animal activity identiﬁcation.
In , Vol. 138, No. 1. IOP conference series: Materials science and
engineering (p. 012004). IOP Publishing.

Tillett, R. D., Bull, C. R., & Lines, J. A. (1999). An optical method for
the detection of sea lice, Lepeophtheirus salmonis. Aquacultural
Engineering, 21(1), 33e48.

Urke, H. A., Kristensen, T., Ulvund, J. B., & Alfredsen, J. A. (2013).
Riverine and fjord migration of wild and hatchery-reared
Atlantic salmon smolts. Fisheries Management and Ecology,
20(6), 544e552.

Van der Stuyft, E., Schoﬁeld, C. P., Randall, J. M., Wambacq, P., &

Goedseels, V. (1991). Development and application of
computer vision systems for use in livestock production.
Computers and Electronics in Agriculture, 6(3), 243e265.

Wallat, G. K., Luzuriaga, D. A., Balaban, M. O., & Chapman, F. A.
(2002). Analysis of skin color development in live goldﬁsh
using a color machine vision system. North American Journal of
Aquaculture, 64(1), 79e84.

Skøien, K. R. (2017). Feed distribution in large scale sea cage

Ward, D., Føre, M., Howell, W. H., & Watson, W. (2012). The

aquaculture, experiments, modelling and simulation. Norway:
Norwegian University of Science and Technology (NTNU).
Doctoral dissertation.

inﬂuence of stocking density on the swimming behavior of
adult Atlantic cod, Gadus morhua, in a near shore net pen.
Journal of the World Aquaculture Society, 43(5), 621e634.

Skøien, K. R., Alver, M. O., & Alfredsen, J. A. (2014 October). A

Wenzel, T. A., Burnham, K. J., Blundell, M. V., & Williams, R. A.

computer vision approach for detection and quantiﬁcation of
feed particles in marine ﬁsh farms. In Image processing (ICIP),
2014 IEEE international conference on (pp. 1648e1652). IEEE.

(2007). Kalman ﬁlter as a virtual sensor: Applied to automotive
stability systems. Transactions of the Institute of Measurement
and Control, 29(2), 95e115.

Sloth, K. H., & Frederiksen, D. (2015). Computer system for

Wright, S. L., Thompson, R. C., & Galloway, T. S. (2013). The

measuring real time position of a plurality of animals. US Patent
20,150,293,205.

Soliveres, E., Poveda, P., Estruch, V. D., P(cid:3)erez-Arjona, I., Puig, V.,
Ord(cid:3)o~nez, P., et al. (2017). Monitoring ﬁsh weight using pulse-
echo waveform metrics. Aquacultural Engineering, 77, 125e131.

physical impacts of microplastics on marine organisms: A
review. Environmental Pollution, 178, 483e492.

