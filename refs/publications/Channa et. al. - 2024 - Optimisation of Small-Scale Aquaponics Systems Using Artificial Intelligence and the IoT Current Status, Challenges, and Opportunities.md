Review
Optimisation of Small-Scale Aquaponics Systems Using
Artificial Intelligence and the IoT: Current Status, Challenges,
and Opportunities

Abdul Aziz Channa 1,*, Kamran Munir 1

, Mark Hansen 1

and Muhammad Fahim Tariq 2

1 Computer Science Research Centre (CSRC), School of Computing and Creative Technologies, College of Arts,

Technology and Environment, University of the West of England (UWE), Bristol BS16 1QY, UK;
kamran2.munir@uwe.ac.uk (K.M.); mark.hansen@uwe.ac.uk (M.H.)
SciFlair, Ltd., Unit 18, Apex Court, Woodlands Lane, Bradley Stoke, Bristol BS32 4JT, UK; fahim@sciflair.com

2

* Correspondence: abdul2.channa@live.uwe.ac.uk

Abstract: Environment changes, water scarcity, soil depletion, and urbanisation are making it harder
to produce food using traditional methods in various regions and countries. Aquaponics is emerging
as a sustainable food production system that produces fish and plants in a closed-loop system.
Aquaponics is not dependent on soil or external environmental factors. It uses fish waste to fertilise
plants and can save up to 90–95% water. Aquaponics is an innovative system for growing food and
is expected to be very promising, but it has its challenges. It is a complex ecosystem that requires
multidisciplinary knowledge, proper monitoring of all crucial parameters, and high maintenance
and initial investment costs to build the system. Artificial intelligence (AI) and the Internet of Things
(IoT) are key technologies that can overcome these challenges. Numerous recent studies focus on
the use of AI and the IoT to automate the process, improve efficiency and reliability, provide better
management, and reduce operating costs. However, these studies often focus on limited aspects
of the system, each considering different domains and parameters of the aquaponics system. This
paper aims to consolidate the existing work, identify the state-of-the-art use of the IoT and AI,
explore the key parameters affecting growth, analyse the sensing and communication technologies
employed, highlight the research gaps in this field, and suggest future research directions. Based on
the reviewed research, energy efficiency and economic viability were found to be a major bottleneck
of current systems. Moreover, inconsistencies in sensor selection, lack of publicly available data, and
the reproducibility of existing work were common issues among the studies.

Keywords: aquaponics; AgriTech; sustainable farming; Internet of Things; artificial intelligence;
big data

1. Introduction

Traditional farming methods are facing increasing threats from extreme weather
events, resource scarcity, and urbanisation. These challenges are jeopardising food security,
causing a shift towards more sustainable and resilient agricultural practices. Extreme
weather events, like droughts, floods, and heatwaves, are causing widespread crop damage
and yield losses. In 2018, heatwaves alone led to multiple crop failures and up to 50%
yield reductions in central and northern Europe [1], highlighting the vulnerability of
traditional farming systems to climate change. The escalating demand for food, coupled
with urbanisation, is putting further strain on agricultural resources. Urban populations are
projected to increase by about 50% by 2045 [2], and there is growing pressure to produce
more food from a shrinking land base. This is further intensified by the depletion of water
resources, deforestation, soil degradation, and greenhouse gas emissions associated with
conventional farming practices [3]. There is a need to find new ways of food production
that are more efficient, rely on fewer natural resources, and are resilient to climate change.

Citation: Channa, A.A.; Munir, K.;

Hansen, M.; Tariq, M.F. Optimisation

of Small-Scale Aquaponics Systems

Using Artificial Intelligence and the

IoT: Current Status, Challenges, and

Opportunities. Encyclopedia 2024, 4,

313–336. https://doi.org/

10.3390/encyclopedia4010023

Academic Editors: Ping-Feng Pai,

Milva Pepi and Raffaele Barretta

Received: 3 October 2023

Revised: 26 January 2024

Accepted: 2 February 2024

Published: 8 February 2024

Copyright: © 2024 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

Encyclopedia 2024, 4, 313–336. https://doi.org/10.3390/encyclopedia4010023

https://www.mdpi.com/journal/encyclopedia

Encyclopedia 2024, 4

314

Aquaponics has emerged as one of the potential alternatives to overcome these
challenges. It is a sustainable and innovative agricultural system that combines aquaculture
(raising fish and other aquatic organisms) and hydroponics (growing plants without soil).
In an aquaponics system, the nutrient-rich water from the fish tanks is used to fertilise the
plants, and the plants help purify the water for the fish. This symbiotic relationship allows
aquaponics systems to produce both fish and vegetables with significantly less water and
land compared to traditional agriculture. Additionally, food can be grown indoors in a
fully controlled environment, making it more resilient to climate change.

Despite its many benefits, aquaponics is a complex ecosystem with many critical
parameters that must be closely monitored and maintained, such as dissolved oxygen
(DO), ammonia, pH, temperature, and exposure to sunlight. Manually monitoring
and maintaining all of these parameters is complicated, time-consuming, and requires
multidisciplinary expert knowledge. However, the IoT and AI can help overcome these
challenges by automating the monitoring and control process, analysing sensor data,
and identifying patterns and trends that would be difficult or impossible for humans
to detect. This could lead to the development of new and innovative ways to optimise
aquaponics systems.

Recent studies have demonstrated the use of AI and machine learning to address
various aspects of aquaponics systems. For example, Abbasi et al. [4] used machine
learning algorithms to identify Foliage Chlorosis in lettuce, John and Mahalingam [5] tested
the use of the You Only Look Once (YOLO) algorithm to detect excessive fish feed in a
tank, and Karimanzira and Rauschenbach [6] used a convolutional neural network (CNN)
to estimate plant growth parameters and a Long Short-Term Memory (LSTM) network
to detect anomalies in the system. However, the majority of the AI-related literature on
aquaponics focuses on visual observations using machine vision and image processing,
whereas the use of data from IoT sensors remains largely unexplored.

Moreover, existing research on the use of the IoT for aquaponics often focuses on
limited parameters. For instance, Wijayanto et al. [7] monitored pH, temperature, water
level, and electrical conductivity but overlooked DO and other elements. Murakami and
Yamamoto [8] detected DO but overlooked nitrate and solar radiation. There was no clear
explanation about the parameter selection and use of sensors, suggesting that researchers
are choosing sensors based on availability rather than on a thorough understanding of the
needs of aquaponics systems. According to Yanes et al. [9], current aquaponics systems
are still in their primitive stage, and not all the parameters of aquaponics have been
thoroughly researched.

A comprehensive review is needed to consolidate the existing work on aquaponics,
identify the crucial parameters to monitor, and survey the state-of-the-art AI and IoT
technologies and sensing solutions available on the market.

1.1. Contributions

While there are several review papers on aquaponics, none of them provide an
exhaustive evaluation of the current state-of-the-art use of AI and the IoT in this field.
This paper aims to fill this gap by compiling and comparing the current literature. This
review will cover the following key areas:

1.
2.
3.
4.

5.

The key parameters that need to be monitored in aquaponics systems.
The sensors available for acquiring farm data.
The AI and ML algorithms used to optimise aquaponic processes and management.
The IoT systems and communication technologies used for remote monitoring
and control.
The research gaps and new opportunities in this field.

Encyclopedia 2024, 4

315

1.2. Scope and Boundaries

The scope and boundaries of this study can be summarised as follows:

1.

The scope of this study is mainly limited to small-scale experimental aquaponics
systems within the academic domain. Commercial aquaponics systems, in contrast,
exhibit significant variability in their technical specifications due to regional
requirements, climate conditions, and resource availability. In addition, technical
details about integrating AI and IoT technologies within commercial aquaponics
systems appear to be limited in the public domain. Consequently, the comprehensive
evaluation of commercial systems, particularly in relation to AI and IoT integration,
proved challenging and, as a result, was excluded from the scope of this study.
2. Although commercial systems are excluded from this review, their fundamentals and
operational theories are the same. Therefore, the knowledge acquired from this review
can be applied to commercial systems.
This study is primarily focused on single-recirculation coupled aquaponics systems.
While the identified IoT and AI technologies are applicable to both coupled and
decoupled systems, optimising decoupled systems may require a separate study due
to their distinct requirements. We have only included decoupled systems to provide a
thorough overview of aquaponics systems.
This review only covers the technical aspects of aquaponics related to the integration
of AI and the IoT. It does not delve into mechanical, chemical, biological, ecological,
or any other domain.

3.

4.

1.3. Paper Organisation

This paper begins with a comprehensive literature review. Section 2 describes the
methodology and search criteria used to select papers for review. Section 3 provides a brief
introduction to typical aquaponics systems, their types, and grow techniques. Section 4
reviews the use of the IoT and AI in the existing literature, discusses the key parameters that
need to be monitored, and surveys the progress of AI solutions for aquaponics. Section 5
outlines the research gaps and opportunities in the field. Finally, Section 6 concludes this
review by identifying key research areas for future work.

2. Search Criteria and Methodology

This review is based on a comprehensive search of aquaponics publications on the
Scopus database to synthesise the current knowledge of aquaponics systems and evaluate
the use of the IoT and AI. All the papers published until August 2023 were searched in the
Scopus database.

The initial search of the database using the keyword “aquaponics” resulted in
1176 records, whereas another search using “aquaponic” yielded 842 records. To cover
both keywords, a third search was performed with an asterisk at the end of the keyword
(aquaponic*), yielding 1405 results. To narrow down the search results, all aquaponics
publications with specific keywords were filtered using advanced queries. The included
keywords were ‘internet of things’, ‘machine learning’, ‘smart’, and ‘intelligent’. Moreover,
two additional keywords with an asterisk, “optim*” and “automat*”, were used to cover any
keyword that started with “opti” or “automat”, such as optimal, optimisation, optimisation,
automates, or automation. Publications that were not in the English language were
excluded from the results.

After refinement through a search query, a total of 479 results were returned, which
were further evaluated by carefully checking the abstract of each paper. The papers that
clearly focused on state-of-the-art aquaponics systems and their optimisation techniques,
key parameters, and optimal ranges, as well as the use of the IoT and AI, were retained for
full-text eligibility checks, leaving a total count of 198. After a full-text review, 45 papers
were selected for inclusion in this article. Thirty of the selected papers mainly focused on
the use of AI and the IoT in aquaponics systems, whereas the remaining papers covered

Encyclopedia 2024, 4

316

the basics of aquaponics systems, the key parameters to monitor, and their optimal ranges
to maintain. A diagram of the paper selection method can be seen in Figure 1.

Figure 1. Flow diagram of paper selection method—adapted from PRISMA flow diagram www.
prisma-statement.org/PRISMAStatement/FlowDiagram.

3. Aquaponics Systems

Growing plants and fish in integrated aquaculture systems dates back 2000 years to
the early development of agriculture in China [10]. Modern aquaponics systems were
first introduced by Dr James Rakocy and his team during the 1980s at the University of
the Virgin Islands in the USA [11]. Aquaponics systems can be categorised into coupled
aquaponics systems (CASs) and decoupled aquaponics systems (DASs), both of which are
discussed in the following sections. For a quick overview, a block diagram is shown in
Figure 2.

Encyclopedia 2024, 4

317

Figure 2. Block diagram for coupled and decoupled aquaponics systems.

3.1. Coupled Aquaponics Systems

Coupled aquaponics systems comprise a single loop where water flows in one direction
only, moving from a fish tank to the plants and then returning to the fish tank. Plants and
fish share the same water, and the waste produced by the fish is directly used as nutrients for
the plants. A typical example of a coupled aquaponics system is the aquaponics system at
the UVI (University of the Virgin Islands) [11]. The majority of the reviewed publications in
this study tended towards CASs due to their simplicity and ease of setup and maintenance.
However, one potential issue observed with CASs is that it is challenging to optimise the
environment for both fish and plants due to the nature of a single recirculating system and
different water quality requirements for both fish and plants [12].

3.2. Decoupled Aquaponics Systems

In DASs, fish and plant systems are separated, and water is not directly circulated
from the fish tank to the hydroponics unit. Instead, it is first treated to remove any solid
waste and excess nutrients before being supplied as needed. A decoupled system allows
for greater control over the water quality in each unit. For example, the fish tank can
be maintained at a different pH or temperature than the hydroponics unit, making it
possible to maintain optimal conditions for both plants and fish. Kloas et al. [13] proposed
a double-recirculation aquaponics system (DRAP), which is a type of decoupled system
that provides optimum conditions for two components by separating plant and fish growth
cycles. Using two independent recirculating units, the water circulation is separated by a
one-way valve. The nutrient-rich water is supplied to the hydroponics part according to
the plant’s specific needs.

In another study, Suhl et al. [14] compared the performance of a DRAP with that
of a conventional hydroponics system by growing tomatoes and found a 40% higher
yield with the DRAP. A DRAP offers greater flexibility over the hydroponics part of the
system. The water can be supplemented to increase nutrient concentration and achieve
optimal plant growth. An experiment conducted by Delaide et al. [15] demonstrated a 39%
increase in the growth rate of lettuce with a supplemented aquaponic solution. A DAS can

Encyclopedia 2024, 4

318

provide independent regulation of water chemistry for each component. Monsees et al. [12]
demonstrated a 36% higher fruit yield with more effective management of fertilisers and
pH levels using a DAS.

Despite the apparent benefits of DASs, this article mainly focuses on coupled
aquaponics systems due to their easier setup and the vast number of related publications.
DASs are comparatively complex systems and require a high initial investment. Therefore,
they are often appropriate for large-scale commercial setups.

3.3. Hydroponics—Grow Techniques for Plants

Aquaponics is the combination of aquaculture and hydroponics to produce fish
and vegetables in a sustainable manner. Fish are generally grown in a simple tank that
is sufficient to accommodate the densities of fish proportional to crop size. However,
in hydroponics, three techniques have been widely discussed in the literature for growing
plants [16,17]: deep water culture (DWC), the nutrient film technique (NFT), and media
beds. Each has its advantages and disadvantages, which are explained in the following
sections. Commercial setups often combine these techniques to obtain all the benefits
of each.

3.3.1. Media-Based Systems

These systems use large trays or boxes filled with solid growth media, such as gravel,
expanded clay pebbles, or stones, to provide support for plants and serve as a biofilter
for converting fish waste into plant nutrients [16]. They use flood and drain cycles to
ensure adequate aeration and supply nutrients to plant roots. This is the ideal technique for
beginners and is comparatively more fault-tolerant [17]. Media-based systems provide good
support to plant roots, natural filtration, and a large area for bacterial growth. Depending
on which media are used, they can become very heavy, be labour labour-intensive to
construct and maintain, and may not be suitable for large-scale setups [18].

3.3.2. Nutrient Film Technique

In NFT systems, horizontal pipes are used to grow plants. Small holes are drilled into
the pipes to support plants and keep their roots inside. A continuous stream of nutrient-rich
shallow water is pumped from the fish tank, and the plants absorb the nutrients they need
for growth before the water is returned to the tank. This technique uses the least amount of
water, allows for easy harvesting, and is most suitable for rooftops because it is lightweight
and does not use soil [17]. However, this technique requires careful monitoring and
management to ensure that the water and nutrient levels are maintained within the optimal
range for plant growth. Water quality issues can quickly escalate if the water circulation is
interrupted for any reason, such as power failure or clogging of pipes with debris [18].

3.3.3. Deep Water Culture

In the DWC technique, plants are generally grown on a floating polystyrene sheet over
a water bed [16]. Small holes are made in the sheets to support plants and keep their roots
in water. The nutrient-rich water is typically recirculated from a fish tank or other nutrient
source, and an air pump is used to provide oxygen to the roots of the plants. The roots of
the plants grow down into the water, absorbing the nutrients they need for growth. DWC
is a cost-effective technique that allows for easy harvesting and planting and a high density
of plants to be grown in a small space, but it requires more complex filtration methods and
is unsuitable for large plants [18]. Moreover, the roots of the plants can become tangled
and overcrowded if the plants are not spaced properly or if they grow too large for the size
of the tank or tray. This can lead to a reduction in plant growth and can also increase the
risk of disease and pest infestations [17].

Encyclopedia 2024, 4

319

3.4. System Sizes of Domestic and Commercial Systems

The design and size of aquaponics systems vary greatly depending on production
requirements and specific needs, ranging from small-scale domestic systems to large-scale
commercial setups. Commercial systems are typically designed to meet the demand for
fresh produce in local shops and supermarkets. On the other hand, domestic systems can
allow each home to achieve self-sustainability and produce its own food. According to
Palm et al. [10], these systems have the potential to become an integral part of future homes
and smart cities.

Aquaponics is a versatile system that can be adopted for domestic and commercial
needs. Domestic aquaponics systems typically involve cultivating fish and plants in
closed-loop systems, typically consisting of a single fish tank, such as an aquarium, and a
small hydroponics unit with a maximum area below 50 m2 [19]. Commercial systems are
relatively complex to build, requiring a dedicated mechanical filter for solid separation and
a biofilter for the nitrification and growth of bacteria. Water flows from the fish tank to the
solid separator, then to the biofilter, and from the biofilter to plants. Finally, the water from
plants is dumped into a sump, and from there, it is pumped back to the fish tank. The sizes
of both domestic and commercial systems, their required site area, and their mechanical
complexity can be seen in Table 1.

Table 1. Sizes of aquaponics systems for domestic and commercial setups.

Aquaponics System

Market

Site Area

Domestic systems

Small-scale
commercial
Medium-scale
commercial
Large-scale
commercial

Home use or direct
sales

Below 50 m2

Retail or wholesale

50 to 100 m2

Wholesale

Wholesale

100 to 500 m2

Above 500 m2

Mechanical
Complexity

Low

Medium

High

High

4. Use of the IoT and AI in Aquaponics

Aquaponics is a complex ecosystem, and manually monitoring and maintaining each
parameter is a difficult task for cultivators. The IoT and AI can greatly increase the efficiency
of aquaponic farms by eliminating operational complexities, enabling process automation,
and ensuring stable operation [8]. Recent research has trended toward automation to
optimise processes such as climate control, anomaly detection, and remote access with the
goal of reducing operational costs and making aquaponics more sustainable. The Scopus
database reveals an upward trend in the use of the IoT and AI in aquaponics systems.
Figure 3 shows the total number of publications on aquaponics involving the IoT and AI
for each year based on the following search term:

TITLE-ABS-KEY (( aquaponic*) AND (“IoT” OR “internet of things” OR “artificial intelligence”
OR “AI” OR “machine learning” OR “smart” OR “intelligent”)) AND (LIMIT-TO (LANGUAGE ,
“English”)).

Various electronic sensors were used in the reviewed studies to monitor farm
parameters, the most common of which were water and air temperature, humidity, pH,
DO, light intensity, and ultrasonic level sensors to monitor water level and plant height.
Sensor data were used to control farm environments, including climate control (lighting,
heating, and cooling), aerator control, water pumps, and automated fish feeders. However,
not all studies provided complete control of the farm environment, with many limited to
one or two control elements.

Encyclopedia 2024, 4

320

Figure 3. Number of publications in Scopus from 2016 to August 2023 discussing the use of the IoT
and AI in aquaponic systems.

The use of Arduino-based microcontrollers and Raspberry PI hardware was common
among the reviewed papers, where control logic was implemented locally, and cloud
connectivity was used for remote monitoring of farm health and to switch some actuators
via a web interface.

Table 2 outlines the key sensing and control elements used in recent publications.

Table 2. Use of sensing and control elements in recent publications.

Sensors

s
d

i
l
o
S
d
e
v
l
o
s
s
i
D

l
a
t
o
T

y
t
i
n
i
l
a
S
r
e
t
a
W

a
i
n
o
m
m
A

e
t
i
r
t
i

N

e
t
a
r
t
i

N

x

x

x

x

x

x

x

y
t
i
v
i
t
c
u
d
n
o
C

l
a
c
i
r
t
c
e
l
E

x

x

x

x

x

n
e
g
y
x
O
d
e
v
l
o
s
s
i
D

x

x

x

x

x

x

x

.

p
m
e
T
r
e
t
a
W

H
p

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x = used.

Controls

T
o
I

I

A

Publication

w
o
l
F

l
e
v
e
L

.

p
m
e
T
r
i
A

i

y
t
i
d
m
u
H

t
h
g
i
L

n
o
i
s
i
V
e
n
i
h
c
a
M

g
n
i
t
a
e
H

g
n
i
t
h
g
i
L

p
m
u
P
r
e
t
a
W

r
e
d
e
e
F

- -

-

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

Mansor et al. [20]

Alselek et al. [21]

Wan et al. [22]

x

x

Reyes Yanes et al. [23]

Kodali and Sabu [24]

Murakami and Yamamoto
[8]

Wijayanto et al. [7]

Ntulo et al. [25]

x

John and Mahalingam [5]

x

x

Mahkeswaran and Ng [26]

Banjao et al. [27]

Concepcion II et al. [28]

Lauguico et al. [29]

Mandap et al. [30]

Jie Ong et al. [31]

Kyaw and Ng [32]

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

Encyclopedia 2024, 4

321

The complexity of aquaponics lies in the interdependent relationship among its core
components: fish, bacteria, plants, nutrient cycles, and system maintenance. Fish generate
nutrient-rich waste, primarily ammonia, which beneficial bacteria transform into nitrites
and then nitrates, serving as essential nutrients for plants [17]. These plants, in turn, filter
the water, creating a healthier environment for fish. Managing this relationship involves
maintaining a delicate balance of nutrient levels, water quality, and system functionality.
The IoT and AI can play a vital role in managing these interdependencies. IoT sensors
can continuously monitor crucial parameters like water quality pH, ammonia, nitrites,
nitrates, temperature, oxygen levels, and water flow rates. These real-time data are pivotal
for understanding the health of the system. For example, IoT sensors can promptly detect
an imbalance in nutrient levels or a fluctuation in water quality and alert operators to take
corrective actions.

The following section delves into the potential ways in which AI and the IoT can
manage these complexities, optimise aquaponics operations, and enhance their efficiency
over traditional aquaponics systems.

4.1. The Synergy of AI and the IoT in Revolutionising Aquaponics

The convergence of AI and the IoT holds immense potential for transforming
aquaponics systems and enhancing their efficiency, sustainability, and overall productivity.
By integrating these technologies, aquaponics operators can harness real-time data,
automate system control, optimise component performance, and make data-driven
decisions, leading to a more efficient, sustainable, and productive aquaponics system [33].

4.1.1. Real-Time Monitoring and Predictive Analytics

AI algorithms can analyse real-time data from IoT sensors to monitor critical
parameters such as water quality, nutrient levels, fish health, and plant growth indices [6,8].
This enables the early detection of potential issues, such as imbalances, contamination,
or disease outbreaks, allowing for proactive interventions to minimise disruptions and
maintain optimal system performance.

4.1.2. Remote Monitoring and Management

IoT-enabled remote monitoring provides aquaponics operators with the ability to
access and analyse system data from anywhere, enabling real-time adjustments and
interventions even when away from the site [34,35]. This promotes continuous optimisation
and ensures optimal system performance even from remote locations.

4.1.3. Automated System Control and Maintenance

IoT sensors can trigger automated tasks, such as adjusting water flow, aeration,
nutrient dosing, and filtration cycles, based on real-time data and AI-generated
recommendations [6,36]. This reduces manual labour requirements and ensures consistent
system performance, minimising the risk of human error.

4.1.4. Predictive Maintenance and Anomaly Detection

AI algorithms can analyse historical data and sensor readings to identify patterns
and predict potential breakdowns or malfunctions in system components [6,33]. This
enables proactive maintenance, preventing downtime and disruptions to production.
By anticipating failures, aquaponics operators can efficiently schedule maintenance tasks
and ensure uninterrupted operation.

4.1.5. Nutrient Management

Nutrient management is a crucial aspect of aquaponics, as it involves maintaining
the right balance of nutrients in the water to ensure healthy plant growth and fish health.
The use of AI and the IoT can help optimise nutrient management in aquaponics by
providing real-time data on water quality parameters such as pH, DO, ammonia, nitrate,

Encyclopedia 2024, 4

322

and nitrite. These data can be used to identify potential imbalances in these water quality
parameters, which can help efficiently manage the nutrients in the system [37].

4.1.6. Data-Driven Decision Making and Optimisation

AI-powered decision support systems can aggregate and analyse data from IoT
sensors [23], system performance logs, and market trends to provide actionable
insights for aquaponics operators. This facilitates data-driven decision making and the
optimisation of system operations, leading to improved resource utilisation, cost savings,
and increased productivity.

4.1.7. Optimising Fish Health and Feeding

AI coupled with IoT sensors offers continuous monitoring capabilities for crucial water
quality parameters such as temperature, dissolved oxygen (DO), pH, ammonia, nitrite,
and nitrate levels within the fish tank. These real-time data can serve as a valuable resource
for understanding fish health, facilitating the early detection of potential issues such as
ammonia or nitrite poisoning, as well as identifying signs of diseases or abnormalities
within the system [31,38]. In addition to functioning as early warning systems for fish
health, AI algorithms can also play a pivotal role in optimising feeding practices. By
leveraging machine vision, AI can analyse video streams and images from the fish tank
to track fish movement and behaviour, providing real-time estimations of feed intake
and fish growth rates. This capability assists in refining feeding schedules to ensure the
optimal quantity of food is dispensed, mitigating the risk of overfeeding and subsequent
waste generation. This precise feeding regimen not only safeguards water quality but also
sustains a healthy aquatic environment [31]. Furthermore, through the analysis of historical
feeding data, growth patterns, and nutritional content, machine learning algorithms can
help optimise feed formulations or dynamically adjust feeding schedules based on real-time
data. This adaptive approach ensures the provision of adequate nutrition to the fish while
minimising costs [33].

4.1.8. Optimising Filtration and Bioconversion

The use of AI and the IoT can enhance the efficiency of both mechanical filters and
biofilters in aquaponics. Mechanical filters are responsible for removing solid waste and
debris from the water, whereas biofilters provide a habitat for beneficial bacteria that
convert harmful ammonia and nitrite into less harmful nitrate [18]. For a healthy bacterial
colony, it is important to maintain adequate levels of pH, DO, water temperature, and UV
light [17]. IoT sensors can monitor these parameters in real time and ensure they remain
within their optimal ranges by alerting farmers of any deviations or suggesting they take
other corrective measures, such as activating aerators to increase DO levels or heaters to
increase temperature [35]. The key indicators of bacterial activity are the ammonia and
nitrite levels; they should always be under 1 mg/L in a balanced system [17]. IoT sensors
can monitor the ammonia and nitrate levels, identify changes in the nitrification rate, and
ensure they remain within their optimal ranges [21].

To ensure mechanical filter functionality, a flow-rate sensor can be used [32]. Typically,
a blockage would impact water flow, and AI algorithms can analyse historical flow-rate
data, identifying trends and deviations from established patterns. This analysis, in turn,
can detect potential blockages within the filter or performance degradation over time.
Additionally, a turbidity sensor mounted inside the filter tank can continuously monitor
water clarity. Increased turbidity levels indicate a rise in suspended solids, which could
result from filter clogging or excessive organic matter buildup. By analysing flow-rate and
turbidity data using ML algorithms, it is possible to determine the optimal time for filter
media replacement or cleaning [39].

Moreover, AI algorithms can analyse historical data from all these sensors and make
recommendations for bacterial management [6], such as dosing nitrifying bacteria cultures
to boost bacterial activity and address ammonia spikes, adding or removing specific

Encyclopedia 2024, 4

323

microbial strains to maintain a healthy and balanced community of microbes for effective
ammonia and nitrite conversion [40,41], and water recycling or periodic filter tank cleaning
to manage bacterial populations and prevent nitrite build-up.

These combined approaches optimise filtration and bioconversion by maintaining a

healthy aquaponics system and reducing human error.

4.1.9. Optimising Plant Growth

AI and IoT technologies can also be employed to optimise plant growth in aquaponics
systems [28]. By continuously monitoring plant health metrics, such as leaf nutrient
levels, chlorophyll content, and photosynthetic efficiency, AI algorithms can identify
potential growth limitations and suggest adjustments to nutrient dosing, light intensity,
and environmental conditions. For instance, AI can analyse leaf nutrient levels to detect
deficiencies or imbalances [37], prompting automated nutrient dosing adjustments to
ensure optimal nutrient availability for plant growth. Additionally, AI can monitor plant
photosynthetic efficiency, which reflects a plant’s ability to convert light energy into biomass.
By analysing photosynthetic efficiency data, AI can optimise the light intensity and spectral
distribution to maximise plant growth rates and yield. Furthermore, IoT sensors can track
plants’ water uptake and moisture levels in the growing media, allow control of water
circulation to ensure consistent water availability for plants and prevent water stress.

By harnessing the power of AI and the IoT, aquaponics can be transformed into
a highly efficient, sustainable, and productive form of agriculture, offering a promising
solution for addressing global food security challenges while minimising the environmental
impact [33].

4.2. IoT Sensors, Controllers, and Communication Technologies

To enable the IoT in aquaponics, three essential components need to be integrated:
sensors, controllers, and a network communication interface. There is a variety of
standalone sensors available in the industry that can be selected based on project
requirements. These sensors generate electrical signals that need to be translated by a
controller. A computer program inside the controller tells it what these electrical signals
mean, how to translate them, and what action needs to be taken next. For example, turning
off the water pump when the water tank is filled or activating aeration when the DO
level drops below a certain point. Together, they can perform various automation tasks
that are preprogrammed. However, without IoT connectivity, their data handling and AI
capabilities are very limited. The communication interface enables internet connectivity
in the controllers, which opens up many possibilities, including massive data handling
and storage capabilities using big data. It also enables the ability to remotely monitor and
control aquaponic farms, run complex AI algorithms, and train models, which were never
before possible.

4.2.1. Key Parameters and Electronic Sensors

There are several key parameters that need to be monitored to ensure optimal growth
performance. The optimal ranges for these parameters can vary greatly depending on the
species of fish and plants in the system, as well as the specific design and setup of the
aquaponics system. To avoid system failures and achieve better efficiency, it is crucial to
regularly monitor the key parameters and ensure that they remain within the appropriate
range for the healthy growth of fish and plants in the system. The next sections discuss the
key parameters, the available sensors, and their optimal ranges as a general guideline.

4.2.2. Temperature and Humidity

All aspects of an aquaponics system are affected by temperature. The water
temperature is considered the most important parameter, as it greatly impacts the whole
process, fish health, and plant growth. The temperature requirements of plants and fish
vary greatly between species, but generally, plants can tolerate between 16 and 30 ◦C, cold

Encyclopedia 2024, 4

324

water fish between 10 and 18 ◦C, warm water fish between 22 and 32 ◦C, and nitrifying
bacteria between 14 and 34 ◦C [17,42]. To avoid any production issues, it is important to
choose a combination of plants and fish that matches their optimal temperature as closely
as possible. The ambient temperature of the farm’s location is also a key factor to consider,
as controlling the temperature is an energy-intensive operation that could lead to high
energy bills and thus make the business unprofitable.

Temperature and humidity can be easily monitored using basic electronic sensors.
Two types of sensors have been discussed in the studied literature: standalone sensors and
sensors that combine temperature and humidity sensing elements in a single unit. It has
been found that combined sensors are only suitable for monitoring air temperature and
humidity, whereas standalone sensors are suitable for monitoring water temperature due
to their ability to be submerged in the water.

The lack of consistency in the literature regarding the specific models of sensors used
could be due to the limited availability of some sensors or the numerous options that
perform similarly. Each study may have conducted experiments using the sensor that was
most easily accessible. The reviewed studies used various sensors, as detailed in Table 3.
The resolution and accuracy of each sensor differed. The sensors used by Murakami and
Yamamoto [8] appear to be the best due to their higher accuracy and reliability. The PT-1000
is widely used in industrial applications, and the SHT-31-D is from Sensirion, a reputable
manufacturer. However, the DS18B20 also seems to have the second-best accuracy and
resolution, with easy accessibility and a lower price tag.

Table 3. Use of temperature sensors in the reviewed studies.

Sensor

DHT11

Accuracy

Range

Resolution

References

±2 °C

0 to 50 °C

1 °C

Nagayo et al. [35]
Kodali and Sabu [24]
Yanes et al. [9]
Bolte et al. [43]
Ng and Mahkeswaran [44]
Murakami and Yamamoto [8]

PT-1000

±0.15 °C

−200 to +850 °C

-

Murakami and Yamamoto [8]

DS18B20

±0.5 °C

−55 to +125 °C

0.0625 °C

SHT-31-D

±0.2 °C

−40 to +125 °C

DHT22

±0.5 °C

−40 to +80 °C

0.01

0.01

Ghandar et al. [45]
Nagayo et al. [35]
Mandap et al. [30]
Khaoula et al. [34]
Yanes et al. [9]
Ng and Mahkeswaran [44]
Wijayanto et al. [7]
Mohd Ali et al. [46]
Reyes Yanes et al. [23]

Murakami and Yamamoto [8]

Mansor et al. [20]
Wijayanto et al. [7]
Ntulo et al. [25]
Reyes Yanes et al. [23]

LM35

±0.5 °C

−55 to +150 °C

-

Prabha et al. [47]

4.2.3. pH

pH (Potential of Hydrogen) is the measure of acidity or alkalinity of a solution. It is one
of the key parameters to maintain in an aquaponics system and can be described as a master
variable that affects several chemical and biological processes essential for plant growth. It
controls the nutrient availability to plants [48]. The pH scale is logarithmic, meaning that
a change of one pH unit represents a tenfold change in the hydrogen ion concentration.
For instance, a pH of 7 has ten times fewer hydrogen ions than a pH of 6, and a pH of 9 has

Encyclopedia 2024, 4

325

1000 times fewer hydrogen ions than a pH of 6. This significant decline in hydrogen ions
can significantly impact the survival of fish and plants. For optimum growth and better
nutrient uptake, most plants require a pH value between 6 and 6.5 [49]. Nitrifying bacteria
prefer the pH to be above 6. In an acidic environment, their ability to convert ammonia to
nitrate is reduced. This can lead to an increase in ammonia in the system, which can be
harmful to fish and plants. The optimum pH for nitrifying bacteria is above 7 [49], and the
efficiency of nitrification increases linearly by 13% with each unit of pH between a range of
5 and 9 [50]. The optimum level of pH for fish varies between fish species. According to
Goddek et al. [49], Tilapia fish achieve the best growth performance between a pH range
of 7.0 and 9.0, yet they can survive large fluctuations in the range of 3.7 to 11.0. Generally,
the optimum pH range for most fish is between 6 and 8.5 [42]. The monitoring of pH
has been broadly discussed in the reviewed papers. Wijayanto et al. [7] implemented an
IoT system for aquaponics, where a pH sensor was used to monitor the level of acidity in
the aquaponic water. The system was tested by artificially adding the alkaline and acidic
solutions with the help of peristaltic pumps. Jie Ong et al. [31] used a sensor to monitor
the pH level, which was reported to an online application. A variety of sensors have been
used, mostly with identical specifications, from low-end manufacturers targeting hobbyists
and enthusiasts. One of the better-quality sensors is from Atlas Scientific, which was used
in Murakami and Yamamoto [8]’s study. The specifications for both categories of sensors
are shown in Table 4.

Table 4. Use of pH sensors in the reviewed studies.

Sensor

Accuracy

Range

Resolution

References

DF Robot/Grove
pH probe

±0.1

0 to 14

0.15

Atlas Scientific
pH probe

±0.002

0 to 14

0.001

Khaoula et al. [34]
Ntulo et al. [25]
Udanor et al. [51]
Wijayanto et al. [7]
Mahkeswaran and Ng [26]
Jie Ong et al. [31]

Alselek et al. [21]
Murakami and Yamamoto [8]

4.2.4. Dissolved Oxygen

Oxygen is essential for all living things in aquaponics: fish, plants, and bacteria.
Dissolved oxygen is a relative measure of the oxygen concentration in the water, and it is
measured in milligrams per litre. It is the most critical parameter in aquaponics, which,
if disregarded, could have catastrophic results. If, for any reason, the DO level drops, fish
can die within hours, depending on the size of the tank and fish density. Particularly in
small aquaponics systems, if aeration is stopped, DO levels can quickly decrease due to a
limited time buffer. A pump or aerator failure is a common cause. Therefore, a drop in DO
must be detected as soon as possible, and countermeasures should be taken to avoid any
failures. According to Somerville et al. [17], the optimum level of DO for all organisms to
thrive is between 5 and 8 mg/litre.

In aquaponics systems, DO can be measured using three types of sensors:
polarographic, galvanic, and optical. Both polarographic and galvanic sensors are
electromechanical sensors that work by diffusing the dissolved oxygen from the water
sample. Electrical voltages are generated when the oxygen passes inside the sensor from a
membrane, causing a chemical reaction. Polarographic sensors require a constant voltage
to be applied, which must be polarised. In contrast, galvanic sensors are self-polarising,
reducing the warm-up time by 5–15 min. Optical sensors measure the DO concentration
in water based on the quenching effect. This process decreases the fluorescence intensity
of a given substance. A photodiode inside the sensor detects the quenched luminescence
and compares it against a reference value to calculate the DO concentration in the water.
The advantage of optical sensors is that they do not require frequent calibration and are not

Encyclopedia 2024, 4

326

dependent on the velocity of water flow, making them the preferred choice in commercial
setups. Many of the reviewed studies used electromechanical sensors. For example,
Udanor et al. [51] used a DF Robot DO sensor probe for Arduino. Mandap et al. [30] and
Murakami and Yamamoto [8] used the DO probe from Atlas Scientific, which is considered
to be a better-quality probe with a wider measurement range of 0–50 mg/L compared to
0–20 mg/L for the DF Robot probe.

There was no use of optical probes in the reviewed studies. This could be due to the
limited availability and higher cost of these probes, generally above GBP 500 at the time of
writing this paper.

4.2.5. Total Nitrogen: Ammonia, Nitrite, and Nitrate

Nitrogen is an essential water quality parameter in aquaponics systems. It enters
the system through fish feed as crude protein, and the fish utilise a portion for growth
while releasing the rest as waste. The waste consists primarily of ammonia and is expelled
through the gills and urine, with some unconsumed feed waste being converted into
ammonia by microbes. Bacteria in the system convert ammonia into nitrite and then
further into nitrate through a process called nitrification. Although nitrogen compounds
can be toxic to fish, they serve as a valuable nutrient source for plants and are the basis
of plant fertilisers. In a well-functioning aquaponics system with proper biofiltration,
ammonia and nitrite levels should be minimal, ideally close to zero or ranging from 0.25
to 1.0 mg/L. The bacteria in the biofilter should effectively convert ammonia and nitrite
into nitrate before any harmful buildup occurs. Fish can generally tolerate up to 300 mg/L,
but above 250 mg/L, plants will start accumulating excessive nitrate into their leaves,
which is unsafe for human health. The optimum nitrate level to maintain is between 5 and
150 mg/L [17]. The nitrification process is dependent on the water temperature, pH, and
DO levels. Optimal nitrification can be achieved when the temperature is between 25 ◦C
and 30 ◦C, pH is between 7 and 9, and DO levels are below 20 mg/L [16].

Generally, ammonia is measured manually using chemical tests, which is a
cumbersome process, especially in small-scale systems. It often requires colour comparison
with a reference chart by the human eye. The colours in the reference chart are generally
very close to each other and could easily deceive human judgement, resulting in incorrect
findings. Electronic sensors are available, but they are generally very expensive, often
costing thousands of pounds. This is likely the reason they were often not used in the
reviewed studies.

4.2.6. Water Level

In aquaponics, adequate water levels need to be maintained in the system, particularly
in the fish tank, so that fish can move freely and thrive. Water is typically consumed in
the system through evaporation and transpiration, or it is manually drained to remove
waste from the system. Water levels can be monitored in the system using basic float
switches or ultrasonic sensors. Ultrasonic distance sensors, such as the HC-SR04 from
Sparkfun, have often been discussed in the reviewed literature. They work by emitting
high-frequency sound waves beyond the range of human hearing. These waves propagate
through the air and reflect back when they encounter a surface, such as water. By measuring
the time it takes for the waves to travel to the water’s surface and return, the level of
water can be calculated. This method allows for accurate monitoring and measurement
of water levels in aquaponics. However, the HC-SR04 is not appropriate or reliable for
long-term use, particularly in commercial applications. Furthermore, the electronics are
not protected against water, and a few accidental splashes of water can easily damage
them. To ensure reliable operation, water-level sensors should be at least water-resistant or
ideally, IP68-rated. IP68 is an Ingress Protection (IP) rating for dust and water protection,
indicating that a device is dust-tight and can withstand temporary immersion in water up
to 1.5 m (4.9 feet) for 30 min.

Encyclopedia 2024, 4

327

4.2.7. Water Flow Rate

The flow rate is an important factor in maintaining the overall balance of an aquaponics
system. It influences the rate of nutrient cycling, oxygen availability, and waste removal.
A consistent flow rate in the system can help maintain stability and ensure that fish and
plants receive optimal conditions for growth. It is important to note that the ideal flow
rate varies depending on the size of the system, the specific fish and plant species, and the
design of the aquaponics setup. During the initial setup, the flow rate is typically set using a
manual valve, but adjustments may be required if changes in pressure are observed during
operation. While electronic sensors or water meters can be used to monitor flow rates, the
reviewed literature suggests that they are not commonly utilised in small-scale systems.
This may be due to the preference for manual observation, as flow rates tend to remain
relatively stable in a well-functioning system, thereby reducing complexity and cost.

4.2.8. Light Intensity

Light is the primary energy source for photosynthesis, and it is the process by which
plants convert light energy into chemical energy. Through photosynthesis, plants produce
sugars and other organic compounds necessary for their growth. Without adequate
light, plants may struggle to photosynthesise effectively, resulting in stunted growth or
even death.

When setting up an aquaponics system, it is essential to consider the lighting needs
of the plants being grown. Factors such as light intensity, duration, and spectrum should
be taken into account. The use of electronic sensors was widely observed in the reviewed
literature for detecting light intensity and controlling artificial light. For example, Nagayo
et al. [35] used an LDR (Light-Dependent Resistor) to automatically activate artificial grow
lights when it is dark, and Sunardi et al. [52] used an LDR to monitor solar lighting. Table 5
shows the types of sensors used in the various studies.

Table 5. Use of light-intensity sensors in the reviewed studies.

Sensor

Range

References

LDR (Photoconductive cell)

5 k to 100 k Ohms @
10 Lux

TLS2561 (Photojunction device)

0.1 Lux to 40,000 Lux

Ghandar et al. [45]
Nagayo et al. [35]
Sunardi et al. [52]
Prabha et al. [47]

Murakami and Yamamoto [8]
Mahkeswaran and Ng [26]

4.2.9. Total Dissolved Solids, Electrical Conductivity, and Salinity

Electrical conductivity (EC) is a measurement of the electrical charge that passes
through water in aquaponics systems, whereas Total Dissolved Solids (TDS) refers to the
measure of anything dissolved in the water, usually mineral salts. The more salt dissolved in
the water, the higher the electrical conductivity, making them highly correlated. Therefore,
TDS and salinity are often estimated from the EC in electronic sensors to reduce processing
time and hardware complexity.
It is recommended to maintain a TDS level between
200 and 400 ppm in aquaponics systems [49]. Salinity levels may vary depending on the
plant species, but it is generally advised to keep the water salinity below 1500 µS/cm [17].
Wijayanto et al. [7] used an EC sensor to detect TDS levels in aquaponic water.
The system was tested by dissolving a salt solution in the fish water until it reached
a set threshold. Another experiment by Mahkeswaran and Ng [26] used an EC sensor to
monitor the electrical conductivity of water and report it to a mobile-based GUI application.

4.3. Controllers—Microprocessor or Microcontroller

To process sensor data and perform any kind of automation in aquaponics,
a microcontroller or a microprocessor is required. The difference between a microcontroller

Encyclopedia 2024, 4

328

and a microprocessor is that a microcontroller contains a CPU (Central Processing Unit),
memory, and all I/O-related hardware in a single chip. In contrast, microprocessors often
contain a CPU only. Comparatively, the processing power of a microcontroller is very
limited; it is an inexpensive part, usually does not require an OS (Operating System)
to run, and is used in a range of applications from calculators to washing machines.
Almost all modern electrical appliances contain one or more microcontrollers. The use of
both microcontroller- and microprocessor-based systems was observed in the reviewed
works. Microcontroller-based systems were largely Arduino-based, such as Atmega,
ESP32, ESP8266, etc. Microprocessor-based systems included Raspberry Pi and other
SBCs (Single-Board Computers) like the NVIDIA Jetson Xavier, etc. Table 6 shows the
usage of controllers in the reviewed studies.

The use of Arduino-based microcontrollers and Raspberry PI hardware was most
common among the reviewed papers. Control logic was implemented locally, and the
cloud connectivity was used for remote monitoring of a farm’s health and to switch some
actuators via a web interface.

Table 6. Controllers used in the reviewed studies.

Controller

Atmega

ESP8266
ESP32

Raspberry Pi

ESP8266 + Raspberry Pi

Atmega + ESP32

Atmega + esp8266

Atmega + Raspberry Pi

Raspberry Pi + PIC32

MSP430 + ESP8266

Jetson Xavier + nRF52840

Usage

Reads sensor data and controls
actuators

sensor data,

Reads
controls
actuators, and provides cloud
connectivity

Reads
actuators,
applications

sensor data,
and

controls
runs web

ESP32 reads
sensor data and
controls actuators; Raspberry Pi for
analyses data and provides cloud
connectivity

Atmega reads sensor data; ESP32
provides cloud connectivity

Atmega reads sensor data and
controls
ESP8266
actuators;
provides cloud connectivity

References

Nagayo et al. [35]

Wan et al. [22]
Khaoula et al. [34]
Udanor et al. [51]
Kodali and Sabu [24]

Wijayanto et al. [7]

Ghandar et al. [45]

Mansor et al. [20]
Banjao et al. [27]
Ng and Mahkeswaran [44]

Ntulo et al. [25]
Ng and Mahkeswaran [44]

Atmega reads sensor data and
controls actuators; Raspberry Pi
runs web applications and provides
cloud connectivity

Mandap et al. [30]
Sunardi et al. [52]
Jie Ong et al. [31]
John and Mahalingam [5]

sensor data,

Processes
runs
pre-trained models, and controls
actuators

MSP430 microcontroller processes
sensor data; ESP8266 provides
cloud connectivity

nRF52840 reads sensor data and
provides Bluetooth connectivity;
image
Jetson Xavier processes
processing
runs ML
algorithms.

and

Dhal et al. [53]

Lee and Wang [54]

Murakami and Yamamoto [8]

Encyclopedia 2024, 4

329

The controller acts as the brain of the system. Electrical signals from all connected
sensors are transmitted to it, which are then processed according to the program running
inside, and automated decisions are made to activate or deactivate specific actuators.

Microprocessor-based systems were mostly used where image processing was required
or for running local app servers, data storage, and visualisation. For example, Murakami
and Yamamoto [8] used an NVIDIA Jetson Xavier NX to capture images from multiple
depth cameras and run ML algorithms to estimate growth. Mandap et al. [30] used
Raspberry Pi to run a local web server and database storage. John and Mahalingam [5]
used Raspberry Pi to capture images from a CMOS camera and detect fish feed in the
fish tank.

4.4. Communication Technologies to Enable the IoT

Any physical device that has a sensor attached to it and can transmit data to the
internet is referred to as an IoT device. All IoT devices must have some communication
interface that allows them to transmit and receive data from the internet. There are many
communication technologies available on the market, which can be categorised into two
types: ones that provide direct IP (Internet Protocol) connectivity, such as WiFi and cellular,
and ones that provide indirect connectivity with the help of gateways such as Zigbee,
LoRaWAN, LPWAN, etc. Table 7 shows the available technologies that can be used in
aquaponic farms.

Table 7. Available communication technologies.

Technology

Communication Range

Data Rate

Frequency

Power Consumption

WiFi

Up to 100 m

Up to 9.6 Gbits/s

2.5 GHz, 5 GHz, and
6 GHz

Higher

Cellular (GPRS)

-

Up to 171.2 Kbps

850/900/1800/1900 MHz

Higher

LoRaWAN

Up to 10 km

27 kbit/s

868 MHz, 900 MHz,
2.4 GHz

Sigfox

LTE-M

NB-IoT

Up to 40 km

100/ 600 bps

868 MHz, 902 Mhz

-

-

300/375 kbps

30/60 kbps (NB1) -
127/169 kbps (NB2)

-

-

Lower

Lower

Lower

Lower

Devices with indirect connectivity are generally ultra-low power; they can last on
coin cell batteries for years. However, their use in aquaponic studies is very limited.
Bolte et al. [43] designed a sensor node using LoraWAN for long-range transmission.
Murakami and Yamamoto [8] designed an aquaponics system where sensor data were
transmitted using Bluetooth. Despite the range of communication technologies available
on the market, the majority of experiments were conducted using WiFi connectivity. This is
probably due to the easy availability and lower cost of WiFi modules.

4.5. Use of AI in Aquaponics

In recent years, the use of machine learning and AI has become the focus of studies in
aquaponics to optimise plant growth and improve resource efficiency. Machine learning
algorithms can be used to analyse data from image sensors or sensors that measure
environmental factors such as temperature, pH, DO, and nutrient levels in the water.
By using these data, machine learning models can be trained to predict the optimal
conditions for plant growth in aquaponics, monitor the growth of fish and plants, or
identify problems in the system. In the studied literature, AI methods were effective at
visually classifying plant growth stages, estimating fish size, detecting nutrient deficiencies
and plant diseases, detecting anomalies, and optimising processes. This section discusses
the common applications of AI and ML in aquaponics. In essence, it is not meant to cover

Encyclopedia 2024, 4

330

all AI and ML research conducted in the aquaponics industry but rather give an idea of
current research interests. The AI methods used in the reviewed studies can be seen in
Table 8.

Table 8. Usage of AI methods in aquaponics.

Usage

AI Methods

Prediction of dissolved oxygen

Growth estimation of plant

Deep Convolutional Neural
Network (DCNN), K-Nearest
Neighbour (KNN), Support
Vector Machine
(SVM),
Decision Tree (DT)
LSTM, CNN, CNN-LSTM
Back Propagation (BP), CNN

Mask-RCNN
Artificial Neural Network
Latent Dirichlet
(ANN),
Allocation (LDA), Quantum
Support Vector Machine
(QSVM)
DCNN, KNN, SVM, DT

References

Taha et al. [55]

Barzegar et al. [56]
Ta and Wei [57]

Murakami and Yamamoto [8]
Concepcion II et al. [28]

Lauguico et al. [29]

Detection
deficiencies

of

nutrient

DCNN, KNN, SVM, DT

Taha et al. [55]

Detection of disease

YOLOv5s, Fast-RCNN

Abbasi et al. [36]

4.5.1. Prediction of Dissolved Oxygen

One of the important parameters that need to be monitored in aquaponics is the DO
level in the water, which is crucial for the health and growth of fish and plants. Machine
learning algorithms can help predict DO levels in aquaponics systems, making it easier
for farmers to maintain optimal DO levels. Various machine learning models, such as
LSTM and CNN, can be used. These models can use data such as water temperature,
pH levels, and EC to predict DO in the water. A study by Ta and Wei [57] proposed a
simplified reverse-understanding CNN model to predict DO. The results showed that
the accuracy of the model was adequate for use in commercial farms. Another study by
Barzegar et al. [56] tested various machine learning models, specifically CNN and LSTM,
to predict concentrations of DO in water. Time-series data of 1 year, which included water
temperature, pH, oxidation–reduction potential (ORP), electrical EC, and DO, were used
for model development. The findings indicated that the LTSM model performed better
compared to the CNN. However, a new approach using a coupled CNN-LSTM model
outperformed the standalone models.

4.5.2. Growth Estimation of Plants

One of the most common applications of ML in aquaponics was found to be the growth
estimation of plants and fish using vision-based systems. Various papers focused on plants,
specifically lettuce. Concepcion II et al. [28] used three ML approaches, namely LDA, ANN,
and QSVM, to identify the growth stage of lettuce. In the study, the LDA model was found
to be very unstable. The ANN achieved the highest accuracy of 90% during the training
phase but fell to 85% during testing. QSVM was shown to be the best-performing model,
with testing and training accuracies of 87.90% and 88.33%, respectively. Another study
by Murakami and Yamamoto [8] used a sensor network and two types of cameras for the
growth estimation of fish and plants. The environmental data were collected using an
air temperature and humidity sensor, illuminance sensor, pH sensor, water temperature
sensor, and dissolved oxygen sensor. Data were transmitted via Bluetooth low-energy
(BLE) wireless sensors to a Jetson Xavier NX. To capture plant images, a RealSense depth
camera D415 module was used, and a ZED Mini stereo camera was used to capture fish

Encyclopedia 2024, 4

331

images. Both cameras were directly connected to a Jetson Xavier board, and Mask-RCNN
was used to extract pixels from the captured images. The accuracy of the method was
evaluated using the RMSE (Root-Mean-Squared Error), and the average RMSE was 6.92%.
This indicates that the proposed method was sufficiently accurate to track changes in plant
growth conditions over time.

4.5.3. Nutrient Deficiencies

One of the challenges of aquaponics is ensuring that plants receive the necessary
nutrients for healthy growth. Nutrient deficiencies can lead to stunted growth, reduced
yield, and even death. Traditional methods of monitoring plant nutrition in aquaponics
involve manual testing of water quality and plant tissue samples, which can be
time-consuming and labour-intensive. Machine learning can be used to automate the
detection of nutrient deficiencies in aquaponics. By analysing data from sensors that
measure water quality and plant growth, machine learning algorithms can identify patterns
that indicate nutrient imbalances. For example, a machine learning model can be trained to
recognise when the levels of nitrogen, phosphorus, or potassium in the water are too low
or too high, based on their effects on plant growth.

Taha et al. [55] used deep CNNs to detect nutrient deficiencies in plants. The model
was evaluated using 3000 images of lettuce, and it successfully classified the images with
96.5% accuracy into four categories: (1) potassium deficiency, (2) nitrogen deficiency,
(3) phosphorous deficiency, and (4) full nutrition.

4.5.4. Disease Detection

Plant disease is a common problem that can destroy a whole crop. The early detection
of diseases is crucial for farmers, enabling them to take prompt action to prevent further
spread and minimise losses. Machine learning algorithms can aid in plant disease detection
by analysing various parameters, including plant growth patterns, leaf colour, and texture.
Abbasi et al. [36] evaluated YOLOv5s and Fast-RCNN to detect diseases in leafy greens.
The system works in three stages: first, it identifies the crop type; then, it checks whether it
is diseased or healthy; and finally, it identifies the disease. Both models were initialised
using transfer learning and then trained on datasets. In the experiment, the YOLOv5s
outperformed Fast-RCNN with a detection speed of 52.8 FPS and an mAP@0.5 of 82.13.

5. Research Gaps and Future Work

Despite the significant progress made in recent years, there are still many challenges
and research gaps present in the field of aquaponics. The following sections outline some
of these challenges to our understanding.

5.1. Energy Efficiency and Profitability

Energy efficiency is crucial in aquaponics, and one of the major issues is high energy
costs. In Europe and the UK, a large portion of the running costs may be attributed to
energy consumption. Specifically, in cold weather, climate control becomes an essential
requirement, and it is an energy-intensive operation.

The energy consumption of aquaponic farms can vary greatly depending on the
location of the farm, weather conditions, and selection of fish and plant combinations. One
small-scale aquaponic farm experiment conducted by Love et al. [58] in the USA reported
56 kWh of energy consumption to produce 1 kg of vegetables and 159kWh to increase the
weight of tilapia fish by 1 kg. Another experiment by Delaide et al. [59] in Belgium reported
84.5 kWh of electricity consumption to grow 1 kg of vegetables and 96.2 kWh to increase
tilapia weight by 1 kg. Considering the market prices of produce and the current energy
rates in the UK, the economic viability of aquaponics remains a challenge. Table 9 shows
the total cost to produce 1 kg of vegetables and fish. To make aquaponics a viable food
production system, energy consumption needs to be optimised. This can be achieved by

Encyclopedia 2024, 4

332

using renewable energy sources, finding ways to reduce energy usage, and developing
smart environmental control systems to optimise energy usage on farms.

Table 9. Cost to produce 1 kg of fish and vegetables.

Reference

Product

Love et al. [58]

Delaide et al. [59]

Vegetables
Fish

Vegetables
Fish

Total
Consumption

56 kWh
159 kWh

84.5 kWh
96.2 kWh

Cost/kWh

Total Cost

GBP 0.34 [60]

GBP 0.34 [60]

GBP 19.05
GBP 54.06

GBP 28.73
GBP 31.35

5.2. Anomaly Detection

Aquaponics systems are subject to environmental variability, such as changes in
temperature, pH, and nutrient levels. Building robust detection methods to distinguish
between normal fluctuations and genuine anomalies is a research challenge. Future research
should focus on combining data from multiple sources, such as water quality data, fish
behaviour data, and plant growth data, to develop reliable anomaly detection systems.
Additionally, real-time anomaly detection is crucial for preventing and mitigating issues
in aquaponics systems. Integrating anomaly detection into the local control systems of
aquaponics setups can help automate responses to anomalies.

By addressing these research gaps, scientists and engineers can develop more effective
and reliable anomaly detection systems for aquaponics. This will help aquaponic farmers
in identifying and mitigating problems early on, improving the productivity and efficiency
of their systems, and reducing the risk of losses.

5.3. System Design and Optimisation

There is a need for more research on how to design and optimise aquaponics systems
for different climates, fish and plant species, and production goals. AI and the IoT
could help analyse regional climate data, recommend the most productive fish–plant
pairings, and seamlessly fine-tune the operational parameters. This not only minimises
uncertainties for novice farmers but also avoids unexpected failures. Furthermore, the setup
of an automated aquaponic farm often involves the installation of multiple sensors and
actuators, coupled with the challenging task of configuring them to individual requirements.
Addressing this hardware complexity is another key area that needs improvement.
Introducing simplified control and monitoring systems could lower the entry barriers
for traditional farmers and encourage the adoption of cutting-edge technologies.

5.4. Lack of Data

One challenge with aquaponics is the lack of publicly available data. The training
process of an ML model heavily depends on large datasets and the selection of data. In most
of the reviewed studies, only a general description of the methodology used was provided,
and the datasets and codes used to train the ML models were excluded. This could be due
to the work being proprietary, but it restricts the work from being verified or reproduced,
which limits its adoptability by other researchers.

While many aquaponics systems already have electronic sensors installed, archiving
the raw data in its most detailed form in public repositories could help accelerate the
development of new intelligent systems.

5.5. Nutrient Management and Crop Variability

Understanding nutrient dynamics in aquaponics systems and optimising nutrient
delivery to different crop types remains a research challenge. Studying crop-specific
nutrient requirements and addressing potential nutrient imbalances can improve crop yield
and quality. Public repositories of sensor data from a variety of crops and regions across

Encyclopedia 2024, 4

333

the world could help in the study of nutrient dynamics and suggest nutrient supplements
in real time to maximise farm efficiency.

5.6. Interoperability and Standardisation

Despite the variety of sensors and actuators used in aquaponics systems, there are
no established standards defining how each component should work, what the most
important parameters are, the allowable tolerances for each sensor, or guidelines for dataset
selection. As a result, the selection of sensors and monitoring parameters in the reviewed
studies was found to be questionable or unjustified. It seems that researchers are selecting
sensors based on their personal preference or ease of use and programming them to meet
their individual needs. This can lead to the production of datasets or results that are
unique to their specific environment and sensor selection, making them less useful to
other researchers. Unless there are plug-and-play-type sensors that are easy to install and
interoperable among manufacturers, it would be difficult for a typical farmer or someone
with less technical knowledge to adapt or access modern technologies.

5.7. Parameter Prediction

To optimise the performance of an aquaponics system, real-time monitoring of key
parameters is essential. Sensors for basic parameters, such as temperature, light, and pH,
are readily available and affordable, but sensors for ammonia, nitrate, and nitrite are often
costly and difficult to obtain. It may be possible to use machine learning to predict these
parameters based on data from basic sensors, which would reduce the initial investment
and maintenance costs of aquaponics systems.

6. Conclusions

This study provides an up-to-date review of the work conducted on the optimisation
of small-scale aquaponics systems using artificial intelligence and the IoT. This review
focused on identifying key parameters and their optimal ranges, utilising electronic sensors,
and incorporating state-of-the-art IoT and AI technologies into aquaponics.

One of the major concerns identified in aquaponic farming is energy efficiency and
economic viability, particularly due to high energy costs. Current systems often prove
unprofitable, especially in cold weather conditions. For aquaponics to achieve success,
a reduction in energy costs is crucial. This could be attained by effectively managing
available resources. Renewable energy sources, such as solar and wind power, offer
promising solutions, as they have the potential to significantly decrease energy costs.
Furthermore, the IoT and AI can contribute to optimising the aquaponic process by
gathering more data for in-depth analysis and facilitating better decision making. Moreover,
aquaponics systems are susceptible to environmental variability, including fluctuations in
temperature, pH, and nutrient levels. Developing robust detection methods to distinguish
between normal variations and genuine anomalies poses a significant research challenge.
Future studies could explore the integration of data from various sources, such as
water quality, fish behaviour, and plant growth data, to create reliable anomaly detection
systems. Another challenge is the scarcity of publicly available data for training and testing
machine learning models, making it difficult to optimise systems or apply AI techniques to
a variety of crops. Additionally, interoperability and standardisation issues among sensors
and actuators create barriers for farmers and the general public to adopt these technologies.

Author Contributions: A.A.C. conceptualised this study and prepared the original draft. K.M.
and M.H. reviewed this manuscript and provided guidance and input on the overall research
direction. M.F.T. shared industry expertise, offering insights into the practical applications and
real-world implications of the research. All authors have read and agreed to the published version of
the manuscript.

Encyclopedia 2024, 4

334

Funding: This work was sponsored by the University of the West of England in collaboration with
the industry partner SciFlair, Ltd. under project id 7229864: Optimal Control of Aquaponic Farms for
Food Production Using IoT and AI.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Not applicable.

Conflicts of Interest: M Fahim Tariq, a co-author of this study, is the director of SciFlair, Ltd. Tariq
has no conflicts of interest to declare.

References

1.

Rampant Heatwaves Threaten Food Security of Entire Planet, Scientists Warn. Available online: https://www.theguardian.com/
environment/2023/jul/21/rampant-heatwaves-threaten-food-security-of-entire-planet-scientists-warn (accessed on 5 February
2024) .

2. World Bank. Urban Development; The World Bank: Washington, DC, USA, 2023. Available online: https://www.worldbank.org/

3.

4.

5.

6.

en/topic/urbandevelopment/overview (accessed on 5 February 2024) .
FAO. The Future of Food and Agriculture: Trends and Challenges; Food and Agriculture Organization of the United Nations: Quebec,
Canada, 2017; OCLC: ocn979567879.
Abbasi, R.; Martinez, P.; Ahmad, R. Automated Visual Identification of Foliage Chlorosis in Lettuce Grown in Aquaponic Systems.
Agriculture 2023, 13, 615.
John, J.; Mahalingam, P.R. Automated Fish Feed Detection in IoT Based Aquaponics System. In Proceedings of the 2021 8th
International Conference on Smart Computing and Communications (ICSCC), Kochi, Kerala, India, 1–3 July 2021; pp. 286–290.
[CrossRef]
Karimanzira, D.; Rauschenbach, T. An intelligent management system for aquaponics. At-Automatisierungstechnik 2021,
69, 345–350. [CrossRef]

[CrossRef]

7. Wijayanto, A.; Wardhana, K.; Aziz, A. Implementation of Internet of Things (IoT) for Aquaponic System Automation.

In
Proceedings of the the 2021 International Conference on Computer, Control, Informatics and Its Applications (IC3INA ’21),
Virtual/Online Conference, Indonesia, 5–6 October 2021 ; pp. 176–181. [CrossRef]

8. Murakami, R.; Yamamoto, H. Growth Estimation Sensor Network System for Aquaponics using Multiple Types of Depth
Cameras. In Proceedings of the 2022 International Conference on Artificial Intelligence in Information and Communication
(ICAIIC), Jeju Island, Republic of Korea, 21–24 February 2022; pp. 033–038. [CrossRef]
Yanes, A.R.; Martinez, P.; Ahmad, R. Towards automated aquaponics: A review on monitoring, IoT, and smart systems. J. Clean.
Prod. 2020, 263, 121571. [CrossRef]

9.

10. Palm, H.W.; Knaus, U.; Appelbaum, S.; Goddek, S.; Strauch, S.M.; Vermeulen, T.; Haissam Jijakli, M.; Kotzen, B. Towards
commercial aquaponics: A review of systems, designs, scales and nomenclature. Aquac. Int. 2018, 26, 813–842. [CrossRef]
11. Tokunaga, K.; Tamaru, C.; Ako, H.; Leung, P. Economics of Small-scale Commercial Aquaponics in Hawai‘i. J. World Aquac. Soc.

2015, 46, 20–32. [CrossRef]

12. Monsees, H.; Kloas, W.; Wuertz, S. Decoupled systems on trial: Eliminating bottlenecks to improve aquaponic processes. PLoS

ONE 2017, 12, e0183056. [CrossRef] [PubMed]

13. Kloas, W.; Groß, R.; Baganz, D.; Graupner, J.; Monsees, H.; Schmidt, U.; Staaks, G.; Suhl, J.; Tschirner, M.; Wittstock, B.; et al. A
new concept for aquaponic systems to improve sustainability, increase productivity, and reduce environmental impacts. Aquac.
Environ. Interact. 2015, 7, 179–192. [CrossRef]
Suhl, J.; Dannehl, D.; Kloas, W.; Baganz, D.; Jobs, S.; Scheibe, G.; Schmidt, U. Advanced aquaponics: Evaluation of intensive
tomato production in aquaponics vs. conventional hydroponics. Agric. Water Manag. 2016, 178, 335–344. [CrossRef]

14.

15. Delaide, B.; Goddek, S.; Gott, J.; Soyeurt, H.; Jijakli, M.H. Lettuce (Lactuca sativa L. var. Sucrine) Growth Performance in

Complemented Aquaponic Solution Outperforms Hydroponics. Water 2016, 8, 467. [CrossRef]

16. Yep, B.; Zheng, Y. Aquaponic trends and challenges—A review. J. Clean. Prod. 2019, 228, 1586–1599. [CrossRef]
17.

Somerville, C.; Cohen, M.; Pantanella, E.; Stankus, A.; Lovatelli, A. Small-Scale Aquaponic Food Production—Integrated Fish and
Plant Farming; Food and Agriculture Organization of the United Nations: Rome, Italy, 2014; ISBN 978-92-5-108532-5.

18. Aquaponics Food Production Systems: Combined Aquaculture and Hydroponic Production Technologies for the Future; Springer Nature:

Berlin/Heidelberg, Germany, 2019. [CrossRef]

19. de Vries, J.; Fleuren, R. A Spatial Typology for Designing a Local Food System. In Proceedings of the 7th International Aesop

Sustainable Food Planning Conference Proceedings, Torino, ME, USA, 7–9 October 2015.

20. Mansor, M.N.; Hasan, M.Z.; Kader, M.M.M.A.; Mustafa, W.A.; Saidi, S.A.; Jamlos, M.A.; Talib, N.A.A. Aquaponic Ecosystem

Monitoring with IOT Application. J. Adv. Res. Appl. Sci. Eng. Technol. 2023, 31, 345–357. [CrossRef]

21. Alselek, M.; Alcaraz-Calero, J.M.; Segura-Garcia, J.; Wang, Q. Water IoT Monitoring System for Aquaponics Health and Fishery

Applications. Sensors 2022, 22, 7679. [CrossRef]

Encyclopedia 2024, 4

335

22. Wan, S.; Zhao, K.; Lu, Z.; Li, J.; Lu, T.; Wang, H. A Modularized IoT Monitoring System with Edge-Computing for Aquaponics.

Sensors 2022, 22, 9260. [CrossRef]

23. Reyes Yanes, A.; Abbasi, R.; Martinez, P.; Ahmad, R. Digital Twinning of Hydroponic Grow Beds in Intelligent Aquaponic

Systems. Sensors 2022, 22, 7393. [CrossRef] [PubMed]

24. Kodali, R.K.; Sabu, A.C. Aqua Monitoring System using AWS. In Proceedings of the 2022 International Conference on Computer
Communication and Informatics (ICCCI), Hammamet, Tunisia, 28–30 September 2022; pp. 1–5, ISSN 2329-7190. [CrossRef]
25. Ntulo, M.P.; Owolawi, P.A.; Mapayi, T.; Malele, V.; Aiyetoro, G.; Ojo, J.S. IoT-Based Smart Aquaponics System Using Arduino Uno.
In Proceedings of the 2021 International Conference on Electrical, Computer, Communications and Mechatronics Engineering
(ICECCME), Mauritius, Mauritius , 7–8 October 2021; pp. 1–6. [CrossRef]

26. Mahkeswaran, R.; Ng, A.K. Smart and Sustainable Home Aquaponics System with Feature-Rich Internet of Things Mobile
Application. In Proceedings of the 2020 6th International Conference on Control, Automation and Robotics (ICCAR), Singapore,
20–23 April 2020; pp. 607–611, ISSN 2251-2446. [CrossRef]

27. Banjao, J.P.P.; Villafuerte, K.S.; Villaverde, J.F. Development of Cloud-Based Monitoring of Abiotic Factors in Aquaponics using
ESP32 and Internet of Things. In Proceedings of the 2020 IEEE 12th International Conference on Humanoid, Nanotechnology,
Information Technology, Communication and Control, Environment, and Management (HNICEM), Manila, Philippines, 3–7
December 2020; pp. 1–6. [CrossRef]

28. Concepcion, R.S., II; Alejandrino, J.D.; Lauguico, S.C.; Tobias, R.R.; Sybingco, E.; Dadios, E.P.; Bandala, A.A. Lettuce growth stage
identification based on phytomorphological variations using coupled color superpixels and multifold watershed transformation.
J. Adv. Intell. Inform. 2020, 6, 261. [CrossRef]

29. Lauguico, S.C.; Concepcion, R.I.S.; Alejandrino, J.D.; Tobias, R.R.; Dadios, E.P. Lettuce life stage classification from texture
attributes using machine learning estimators and feature selection processes. Int. J. Adv. Intell. Inform. 2020, 6, 173. [CrossRef]
30. Mandap, J.P.; Sze, D.; Reyes, G.N.; Matthew Dumlao, S.; Reyes, R.; Danny Chung, W.Y. Aquaponics pH Level, Temperature, and
Dissolved Oxygen Monitoring and Control System Using Raspberry Pi as Network Backbone. In Proceedings of the TENCON
2018—2018 IEEE Region 10 Conference, Jeju Island, Republic of Korea, 28–31 October 2018; pp. 1381–1386, ISSN 2159-3450.
[CrossRef]
Jie Ong, Z.; Keong Ng, A.; Ya Kyaw, T. Intelligent Outdoor Aquaponics with Automated Grow Lights and Internet of Things. In
Proceedings of the 2019 IEEE International Conference on Mechatronics and Automation (ICMA), Tianjin, China, 4–7 August
2019; pp. 1778–1783, ISSN 2152-744X. [CrossRef]

31.

32. Kyaw, T.Y.; Ng, A.K. Smart Aquaponics System for Urban Farming. Energy Procedia 2017, 143, 342–347. [CrossRef]
33. Mandal, A.; Ghosh, A.R. Role of artificial intelligence (AI) in fish growth and health status monitoring: A review on sustainable

aquaculture. Aquac. Int. 2023, 10, 1–30. [CrossRef]

34. Khaoula, T.; Abdelouahid, R.A.; Ezzahoui, I.; Marzak, A. Architecture design of monitoring and controlling of IoT-based

aquaponics system powered by solar energy. Procedia Comput. Sci. 2021, 191, 493–498. [CrossRef]

35. Nagayo, A.M.; Mendoza, C.; Vega, E.; Al Izki, R.K.S.; Jamisola, R.S. An automated solar-powered aquaponics system towards
agricultural sustainability in the Sultanate of Oman. In Proceedings of the 2017 IEEE International Conference on Smart Grid and
Smart Cities (ICSGSC), Singapore, 23–26 July 2017; pp. 42–49. [CrossRef]

36. Abbasi, R.; Martinez, P.; Ahmad, R. An ontology model to represent aquaponics 4.0 system’s knowledge. Inf. Process. Agric. 2022,

9, 514–532. [CrossRef]

37. Taha, M.F.; Abdalla, A.; ElMasry, G.; Gouda, M.; Zhou, L.; Zhao, N.; Liang, N.; Niu, Z.; Hassanein, A.; Al-Rejaie, S.; et al.
Using Deep Convolutional Neural Network for Image-Based Diagnosis of Nutrient Deficiencies in Plants Grown in Aquaponics.
Chemosensors 2022, 10, 45. [CrossRef]

38. Water Quality in Aquaponics—Go Green Aquaponics. Available online: https://www.gogreenaquaponics.com/blogs/news/

water-quality-in-aquaponics (accessed on 5 February 2024 ).

39. Kale, S.J.; Khandekar, M.A.; Agashe, S. Prediction of Water Filter Bed Backwash Time for Water Treatment Plant using Machine
In Proceedings of the 2021 IEEE 6th International Conference on Computing, Communication and

Learning Algorithm.
Automation (ICCCA), Arad, Romania, 17–19 December 2021; pp. 113–116, ISSN 2642-7354. [CrossRef]

40. Kasozi, N.; Abraham, B.; Kaiser, H.; Wilhelmi, B. The complex microbiome in aquaponics: Significance of the bacterial ecosystem.

Ann. Microbiol. 2021, 71, 1. [CrossRef]

41. Wright, R.J.; Gibson, M.I.; Christie-Oleza, J.A. Understanding microbial community dynamics to improve optimal microbiome

selection. Microbiome 2019, 7, 85. [CrossRef]

42. Yildiz, H.; Robaina, L.; Pirhonen, J.; Mente, E.; Domínguez, D.; Parisi, G. Fish welfare in aquaponic systems: Its relation to water

quality with an emphasis on feed and faeces-A review. Water 2017, 9, 13. [CrossRef]

43. Bolte, P.; Witkowski, U. Energy Self-Sufficient Sensor Node for Long Range Wireless Networks; IOP Publishing: Bristol, UK, 2020.

[CrossRef]

44. Ng, A.K.; Mahkeswaran, R. Fostering Computational Thinking and Systems Thinking through Aquaponics Capstone Projects. In
Proceedings of the 2021 IEEE International Conference on Engineering, Technology & Education (TALE), Wuhan, China, 5–8
December 2021; pp. 1039–1044, ISSN 2470-6698. [CrossRef]

45. Ghandar, A.; Ahmed, A.; Zulfiqar, S.; Hua, Z.; Hanai, M.; Theodoropoulos, G. A Decision Support System for Urban Agriculture

Using Digital Twin: A Case Study With Aquaponics. IEEE Access 2021, 9, 35691–35708. [CrossRef]

Encyclopedia 2024, 4

336

46. Mohd Ali, M.F.; Asrul Ibrahim, A.; Mohd Zaman, M.H. Optimal Sizing of Solar Panel and Battery Storage for A Smart Aquaponic
System. In Proceedings of the 2021 IEEE 19th Student Conference on Research and Development (SCOReD), Kota Kinabalu,
Malaysia, 23–25 February 2021; pp. 186–191, ISSN 2643-2447. [CrossRef]

47. Prabha, R.; Saranish, R.S.; Sowndharya, S.; Santhosh, A.; Varsha, R.; Sumathi, K. IoT Controlled Aquaponic System. In Proceedings
of the 2020 6th International Conference on Advanced Computing and Communication Systems (ICACCS), Coimbatore, India,
6–7 March 2020; pp. 376–379, ISSN 2575-7288. [CrossRef]

48. Penn, C.; Camberato, J. A critical review on soil chemical processes that control how soil ph affects phosphorus availability to

plants. Agriculture 2019, 9, 120. [CrossRef]

49. Goddek, S.; Delaide, B.; Mankasingh, U.; Ragnarsdottir, K.V.; Jijakli, H.; Thorarinsdottir, R. Challenges of Sustainable and

Commercial Aquaponics. Sustainability 2015, 7, 4199–4224. [CrossRef]

50. Villaverde, S.; García-Encina, P.A.; Fdz-Polanco, F. Influence of pH over nitrifying biofilm activity in submerged biofilters. Water

Res. 1997, 31, 1180–1186. [CrossRef]

51. Udanor, C.N.; Ossai, N.I.; Nweke, E.O.; Ogbuokiri, B.O.; Eneh, A.H.; Ugwuishiwu, C.H.; Aneke, S.O.; Ezuwgu, A.O.; Ugwoke,
P.O.; Christiana, A. An internet of things labelled dataset for aquaponics fish pond water quality monitoring system. Data Brief
2022, 43, 108400. [CrossRef] [PubMed]
Sunardi, A.; Suud, F.I.; Agus, N.W.; Gunawan, I. IoT Application on Aquaponics System Energy Optimization; IOP Publishing: Bristol,
UK, 2021. [CrossRef]

52.

53. Dhal, S.B.; Jungbluth, K.; Lin, R.; Sabahi, S.P.; Bagavathiannan, M.; Braga-Neto, U.; Kalafatis, S. A Machine-Learning-Based IoT
System for Optimizing Nutrient Supply in Commercial Aquaponic Operations. Sensors 2022, 22, 3510. [CrossRef] [PubMed]
54. Lee, C.; Wang, Y.J. Development of a cloud-based IoT monitoring system for Fish metabolism and activity in aquaponics. Aquac.

Eng. 2020, 90, 102067. [CrossRef]

55. Taha, M.; ElMasry, G.; Gouda, M.; Zhou, L.; Liang, N.; Abdalla, A.; Rousseau, D.; Qiu, Z. Recent Advances of Smart Systems and
Internet of Things (IoT) for Aquaponics Automation: A Comprehensive Overview. Chemosensors 2022, 10, 303. [CrossRef]
56. Barzegar, R.; Aalami, M.T.; Adamowski, J. Short-term water quality variable prediction using a hybrid CNN–LSTM deep learning

model. Stoch. Environ. Res. Risk Assess. 2020, 34, 415–433. [CrossRef]

57. Ta, X.; Wei, Y. Research on a dissolved oxygen prediction method for recirculating aquaculture systems based on a convolution

neural network. Comput. Electron. Agric. 2018, 145, 302–310. [CrossRef]

58. Love, D.C.; Uhl, M.S.; Genello, L. Energy and water use of a small-scale raft aquaponics system in Baltimore, Maryland, United

States. Aquac. Eng. 2015, 68, 19–27. [CrossRef]

59. Delaide, B.; Delhaye, G.; Dermience, M.; Gott, J.; Soyeurt, H.; Jijakli, M.H. Plant and fish production performance, nutrient mass
balances, energy and water use of the PAFF Box, a small-scale aquaponic system. Aquac. Eng. 2017, 78, 130–139. [CrossRef]
60. Energy Price Guarantee Up Until 30 June 2023, Available online: https://www.gov.uk/government/publications/energy-bills-

support/energy-price-guarantee-up-until-30-june-2023 (accessed on 5 February 2024) .

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

