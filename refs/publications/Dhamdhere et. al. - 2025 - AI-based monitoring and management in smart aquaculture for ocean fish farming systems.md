Applied Chemical Engineering (2025) Volume 8 Issue 3
doi: 10.59429/ace.v8i3.5746

ORIGINAL RESEARCH ARTICLE

ISSN: 2578-2010 (O)

AI-based monitoring and management in smart aquaculture for ocean
fish farming systems
Pramod Dhamdhere1, Swati Mukesh Dixit2,9, Manjusha Tatiya3, Babaso A. Shinde4, Jyoti Deone5, Anant
Kaulage6, Yogendra Patil1, Rupesh Gangadhar Mahajan7,9, Anant Sidhappa Kurhade8,9*, Shital Yashwant
Waware8,9

1 Department of Computer Engineering, Marathwada Mitramandal’s Institute of Technology, Lohgaon, Pune,411047,
Maharashtra, India
2 Department of Electronics and Telecommunication Engineering, Dr. D. Y. Patil Institute of Technology, Pimpri,
411018, Pune, India
3 Department of Artificial Intelligence and Data Science, Indira College of Engineering and Management, Indira
Chanakya Campus (ICC), Parandwadi, Pune - 410506, Maharashtra ,India
4 Department of Artificial Intelligence and Data Science, Marathwada Mitramandal’s Institute of Technology,
Lohgaon, Pune - 411047, Maharashtra, India
5 Department of Information Technology, D.Y. Patil Deemed to be University RAIT, Navi Mumbai,
Maharashtra 400706, India
6 Department of Computer Engineering, MIT Art, Design and Technology University, Loni Kalbhor, Pune,412201,
Maharashtra ,India
7 Department of Computer Engineering, Dr. D. Y. Patil Institute of Technology, Sant Tukaram Nagar, Pimpri, 411018,
Pune, Maharashtra, India.
8 Department of Mechanical Engineering, Dr. D. Y. Patil Institute of Technology, Sant Tukaram Nagar, Pimpri,
411018, Pune, Maharashtra, India.
9 School of Technology and Research, Dr. D. Y. Patil Dnyan Prasad University, Sant Tukaram Nagar, Pimpri, Pune,
411018, Maharashtra, India.

*Corresponding author: Anant Sidhappa Kurhade; a.kurhade@gmail.com

ARTICLE INFO

Received: 22 August 2025
Accepted:  10 September 2025
Available online: 17 September 2025

COPYRIGHT

Copyright © 2025 by author(s).
Applied Chemical Engineering is published by
Arts and Science Press Pte. Ltd. This work is
licensed under the Creative Commons
Attribution-NonCommercial 4.0 International
License (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/

ABSTRACT

 Background:  The  growing  global  demand  for  seafood  and  the
limitations  of  conventional  aquaculture  practices  have  highlighted  the  need
for  sustainable  and  efficient  alternatives.  Ocean-based  fish  farming  faces
challenges such as inconsistent water quality, delayed disease detection, and
inefficient feeding strategies. Artificial Intelligence (AI), integrated with the
Internet  of  Things  (IoT),  computer  vision,  and  machine  learning,  offers
opportunities to address these issues and advance smart aquaculture systems.
Methods: This review systematically synthesizes literature, industrial reports,
and case studies from leading aquaculture regions including Norway, Japan,
India,  and  Chile.  The  analysis  focuses  on  AI  applications  in  water  quality
monitoring,  fish  health  management,  feeding  optimization,  biomass
estimation,  and  decision  support.  The  study  also  evaluates  commercial
platforms  and  identifies  technical,  economic,  and  ethical  challenges,
alongside  emerging  research  directions.  Results:  AI-based  monitoring  and
management systems demonstrated significant improvements in aquaculture
practices.  Commercial  solutions  such  as  eFishery,  Aquabyte,  and  Aquaai
reported feed cost reductions of 15–30%, early disease detection leading to up

1

to 20% lower mortality rates, and more accurate biomass estimation exceeding 90% prediction accuracy. These outcomes
resulted  in  enhanced  yield,  cost  savings,  operational  efficiency,  and  compliance  with  environmental  standards.
Conclusion: AI technologies have shown transformative potential in achieving sustainable, climate-resilient aquaculture.
While challenges such as data scarcity, high setup costs, environmental variability, and ethical concerns persist, emerging
approaches—including  multimodal  AI,  digital  twins,  robotics,  and  explainable  AI—can  enhance  robustness  and
transparency. Future research should emphasize scalable, adaptive, and standardized AI frameworks to support global
seafood security and long-term sustainability in ocean-based fish farming.
Keywords:  Artificial  intelligence,  biomass  estimation,  disease  detection,  feed  optimization,  smart  aquaculture,  water

quality monitoring

1. Introduction

Increasing worldwide demand for seafood combined with the exhaustion of wild fish stocks has made
aquaculture an essential contributor to global food security. Of the proposed aquaculture systems, oceanic fish
farming—especially offshore or open-water farms—is a promising option for mass cultivation. Nevertheless,
these systems present several challenges including maintaining optimal water quality, monitoring fish health
status and feeding efficiency as well adapting to environmental changes in temperature or disease outbreaks.
Traditional  monitoring  can  be  labor-intensive,  ad  hoc  and  myopic  which  are  not  suited  to  the  dynamic
environment of open ocean aquaculture.

Recent developments in the field of artificial intelligence (AI) have led us to new possibilities on how we
can improve efficiency, precision and sustainability in our aquaculture practice. By applying AI methods like
machine  learning,  deep  learning  and  computer  vision,  smart  aquaculture  systems  can  automate  real-  time
monitoring  predictions  analytics  or  decision  making  [1].  Such  platforms  combine  data  from  multi-source
sensors, sub-sea camera and remote operated vehicles in order to enable timely interventions; efficient use of
resources through resource optimization algorithms together with as minimizing impact on the environment.
AI-enabled solutions have the potential to revolutionize aquaculture, aiding in data- driven applications leading
to  higher  productivity  levels  at  lower  costs  and  more  responsible  environmental  practices  [2,  3].  Real-time
monitoring  can  avoid  diseases  and  deaths  by  preventing  and  specifying  the  treatment  of  biomolecules  [4].
Combination of AI and IoT (the Internet of Things) is changing industries in terms of sustainability, efficiency,
innovation etc [3].

It is a revolution of the traditional fish farming, using IoT and big data analysis technology to remotely
operate with robotics control system that enabled by 5G/Cloud/AI technologies  [5]. This technology chain is
conducive to creating real-time data acquisition, quantitative regulation accuracy of decision-making means,
intelligent control mode and refined investment direction as well as personalized service content that have a
new  way  for  fish  farming  [6].  Integration  of  IoT  devices  as  sensors,  cameras  and  monitoring  systems  have
improved data collection from remote and dynamic aquaculture ecosystems  [1]. AI models can be used with
machine learning to analyze large amounts of data in order to optimize feeding strategies, monitor fish behavior
and forecast environmental impacts  [3]. In addition, drones, nano/micro sensors and bionic robots as well as
energy-efficient devices contribute towards increased productivity and sustainability of aquaculture  [6]. The
application  of  AI  technology  in  smart  cities  studies  Aquaculture  and  creates  the  means  to  in-service  such
aquaculture management, thus its use with AET to improve aqua farm productivity [7].

In this article, the utilization of AI methods and tools in developing aquaculture to close food supply-
demand gap was reviewed [8]. The review evaluates the contribution of AI in improving traceability, feeding
optimization,  disease  detection  and  growth  prediction  as  well  as  environmental  monitoring  and  market
information. The application of AI to aquaculture can help reduce human intervention in industry and increase
output  with  better  sustainability  [9].  The  targeted  introduction  of  AI  applications  into  various  aquaculture
processes is essential for delivering large productivity gains, increased operational sustainability and higher

2

efficiencies that will be required to meet growing global demand for seafood, while at the same time complying
with increasingly demanding environmental standards.

Figure 1. Conceptual Framework of Smart Aquaculture Using AI and IoT Technologies

Figure  1  shows  a  smart  aquaculture  system  with  AI-IoT  technologies,  where  data  from  underwater
sensors/cameras  and  remote  devices  are  fused  to  achieve  real-time  monitoring.  This  is  conducive  to  the
intelligent decision and data-driven management for the oceanic fish farming. Smart aquaculture involves the
use  of  sophisticated  digital  technologies—such  as  AI,  IoT  (Internet  of  Things),  edge  computing,  big  data
analytics and automation in combination—to optimize decision making based on real-time information within
an agricultural framework [10]. However, such systems aim to overcome the increasing demand for sustainable
and scalable solutions of truck farming that have also been developed with favorable growth conditions in
ocean-based environments where natural parameter fluctuate much more than inland system due to several
constraints[3]. AI in surveillance and management systems achieve functions including real-time environmental
monitoring,  automation  feeding  system  operation,  detection  of  fish  health  status  prediction  models  for  the
growth or disease  outbreak  [11].  In  this  context,  the  application  of AI  and  IoT  has  proven  effective  in  cage
culture facilities where continuous monitoring of fish health, survival rate as well as feed residuals is possible.

Central to smart aquaculture are networked equipment, underwater sensors and actuators, moving robots
(AUVs or drones), high-resolution video cameras for filming the aquatic environment and feeders [6]. These
are tools that monitor water temperature, dissolved oxygen levels, pH level of the waters, salinity to name a
few as well as monitoring fish behavior and feeding activity through sensors; hence providing you with every
single  information  about  your  livestock  (fish),  their  size  and  other  health  indexes.  AI-powered  algorithms
process this data, analyses the resulting information to provide actionable insights and even automate responses
while minimizing human intervention in routine monitoring activities [1].

Smart aquaculture farms are generally divided between onshore (land-based recirculating systems) and
offshore  (open-ocean  cages  or  net  pens).    Although  onshore  systems  can  better  implement  environmental
control, offshore ones can make the most of natural water exchange and be easily scaled up but with stronger
requirements to monitoring system because they are away from land where current, tide, storm should have
impact. In both environments, AI plays a very important role in supporting predictive management that can

3

help to decrease operational costs and reduce the number of fish destroyed while improving their welfare as
well as environmental compliance.

Aquaculture,  especially  marine  fish  farming  is  receiving  intense  pressure  to  feed  the  growing  world
population  and  now  in  need  of  more  sustainable  approach  [8].  Smart  aquaculture  with  the  combination  of
sophisticated technologies such as AI and IoT is a promising approach to transforming fish farming systems
[10]. With this method, the real-time monitoring, data-driven decision making and automated procedures which
improve productivity while decreasing environmental impact as well as improving fish welfare is achieved [12].
The anticipated growth in aquaculture production to almost 109 m tonns by 2030 further emphasizes the need
for  alternative  measures  [12].  Precision  aquaculture  systems  are  necessary  to  optimize  feeding  regimes  and
increase fish farming efficiency [13]. The adoption of a IoT solutions is revolutionizing conventional farming
approaches  facing  problems  related  to  pest  control  and  post-harvest  management  [14].  Aquaculture,  a  fast-
growing industry and an important contributor to global food security, requires novel strategies for improving
its efficiency and sustainability [15]. New friendly intensive breeding will be targeted nontoxic agents and non-
destructive products using antibiotics for the pro-biotic nature substances, immunocompetent to adjust with
physiological regulation cultured organisms [16]. Fish farming problems can be overcome using AI technologies
to achieve accurate, scalable and efficient solutions [10]. Automatic systems could be made used to manage for
a success of 70-80% which would also bring about an advantage in profit by 20–30% [17].

Designing and deploying AI systems for aquaculture necessitates a thorough understanding of the unique
challenges as well as opportunities in open ocean fish farming settings. For example, AI-based monitoring can
help to foster an optimal environment for fish growing which may increase production and profitability quite
considerably [5]. Generative AI is a disruptive force for aquaculture, as the industry turns towards a data-driven
decision  automation  and  digital  integration;  GAI  models  provide  new  opportunities  in  environmental
monitoring (e.g. detecting contamination or algal blooms), robotized processing plants design optimization
metrics development Flood management  [18]. It also enables from analysis in situ of the environmental and
biological parameters that influence aquaculture system performance. AI capabilities include optimization of
fish  feeding  by  real-time  monitoring  and  combining  an  understanding  of  the  behavior  of  the  fish  with
environmental conditions to avoid waste for feed while increasing growth rates [19]. Data from such sensors, as
well as cameras and others can be analyzed by AI algorithms to identify early signs of disease, predict growth
rates,  and  optimize  feeding  routines  [16].  Additionally,  AI  can  also  help  with  predictive  maintenance  of
aquaculture  machinery  to  prevent  down  times  and  reduce  operational  costs  [20].  When  deploying  AI-based
applications in aquaculture, it is necessary to address data privacy and security stakes as well as ethical issues.
AI has capacity to turn existing systems into extremely efficient and scalable frameworks [21].

The Precision Fish farming  concept applies control-engineering principles to enhance the supervision,
regulation and surveillance of biological operations within fish farms [22]. As production is up scaled, however
biological as well economic and social issues will more surely start to affect the ethical soundness, productive
viability and environmental beings of producing fish  [22]. Thus, the promotion of Integrated Farming System
technologies will increase yields and income by resource efficiencies and waste minimization  [23]. AI-based
methods in aquaculture have a wide variety of applications, from monitoring  fish  behavior and optimizing
feeding strategies to forecasting environmental conditions. An analysis of data from sensors and cameras is of
importance to achieve early disease detection in aquaculture using AI systems. These systems can detect subtle
alterations in fish behavior; for example, lower feeding activity or abnormal swimming patterns that might be
indicative  of  the  presence  of  disease.  The  early  recognition  of  such  changes  might  give  possibility  to  an
efficient intervention  and preventing  the spread  of diseases,  with following reduction  in mortality rate and
economic losses.

AI has also been applied to improve industries such as food quality control and supply chain optimization
[24]. Taking inspiration from our terrestrial agriculture, AI algorithms are able to calculate when it is the best

4

time for harvesting aquatic species, predict potential wasted based on growth and environmental conditions or
perceiver how healthy their  infrastructure waters are as in full rain  with a network of sensors mediated  by
advanced machine learning model.

More concretely, AI programs can crunch real-time data from sensors to calculate the most auspicious
time  for  harvesting  and  predict  potential  waste  using  variables  like  growth  progressions  or  water  quality;
ceaselessly  monitoring  aquaculture  conditions.  Figure  2  depicts  the  main  elements  of  smart-aquaculture,
showing how AI and IoT enable oceanic fish farming. It focuses on the monitoring in real time, intelligent
decision and data-driven management to improve productivity and sustainability.

Figure 2. Conceptual framework of smart aquaculture using AI and IoT technologies

The integration of AI and IoT allows automatic, real-time monitoring with intelligent analysis of animal
health status to enhance productivity, farm economy and animal welfare by reducing risks through machine
learning algorithms (ML)  [25]. In combination with artificial intelligence (AI)-based analysis, near real-time
data is collected then processed resulting in decision making based on the collection of hyper spectral and
multispectral imagery for optimal resource use as well as to combat minimizing environmental damage  [26].
This serves to improve even more the sustainability and efficiency of aquaculture farms  [28]. AI is currently
applied in many areas, such as food quality inspection and supply chain optimization [29]. AI algorithms may
also  assist  in  deciding  the  optimal  time  for  harvesting  aquatic  organisms,  predicting  potential  waste  by
combining  growth  trend  with  environmental  data  and  monitoring  continuously  and  on  a  network  basis  the
healthiness  of  an  ecosystem  thanks  to  sensors  field-pointed  based  measurements  together  with  advanced
machine learning models [21-31].

Combining such sensors with deep learning and AI algorithms provides the ability to quickly analyze

large datasets in real-time, discovering patterns, anomalies or trends [32].

By being able to handle large datasets, the AI models can unearth trends and patterns in water quality that
conventional techniques may miss  [33]. AI systems, by automatically controlling the levels of crucial water
quality parameters such as dissolved oxygen, pH, temperature and salinity to optimize conditions for fish health
and growth in an online mode [34].

5

In this work we review the status of AI technologies for smart ocean fish farming and their perspectives.
It concentrates on key applications including water quality monitoring, disease detection estimation of feed
and fish biomass. The contribution of the paper is, also, to survey recent advances for AI hardware and software
in IoT systems discuss implementations based on real world data – with a not negligible part being focused
onto  public  description  of  city  services  implemented  both  by  commercial  operators  than  local  government
bodies as well limitations achievements and research gaps. The aim is to develop a broader vision of how AI
can  transform  the  aquaculture  industry,  and  outline  potential  future  for  intelligent  and  sustainable  netwin
systems in ocean farming. Table 1 provides a brief summary of the major challenges encountered in ocean
fish farming and associated AI approaches/achievements that contribute to intelligent aquaculture systems.

Table 1. Summary of AI-Based smart aquaculture systems—Challenges, technologies, and expected outcomes

Focus Area

Key Challenges

AI-Based Solutions

Technologies
Involved

Expected Outcomes

Global Seafood Demand

Depletion of wild fish
stocks; inefficiency of
traditional farming

Predictive analytics
for resource planning
and management

Machine Learning, Big
Data, IoT

Increased production;
better food security

Monitoring & Health
Management

Manual, delayed fish
health monitoring;
disease outbreaks

Feeding Optimization

Feed wastage and cost
inefficiency

Environmental Control

Variability in open-
ocean conditions

System Integration &
Automation

Limited scalability of
traditional systems

Market Intelligence &
Sustainability

Lack of traceability,
harvest planning, and
ethical considerations

Real-time fish
behavior and disease
detection using
vision and sensors

Automated, adaptive
feeding schedules
based on fish
behavior and
environment

Continuous
monitoring and
predictive adjustment
of water parameters

AI-integrated control
systems for
autonomous and
remote aquaculture
operations

Smart decision
systems for market
data, traceability,
harvesting time, and
ethical resource
management

AI + Computer Vision
+ Underwater Sensors

Early intervention;
reduced mortality;
improved fish welfare

ML algorithms; Smart
Sensors; Automated
Feeders

Cost savings; enhanced
growth rates

IoT, Edge AI, Drones,
Autonomous Vehicles

Better environmental
compliance and
sustainability

Cloud computing,
Robotics, 5G, Edge
Computing

Labor reduction;
efficient large-scale
operations

Generative AI, Digital
Twins, AIoT, Cyber-
Physical Systems

Sustainable practices;
enhanced profitability;
minimized
environmental impact

2. Role of artificial intelligence in aquaculture

Artificial Intelligence (AI) significantly transforms contemporary aquaculture systems through intelligent
surveillance, prediction and automation over a range of fish farming procedures. In conventional culture the
tasks are carried out basically by manual labor and decisions in many cases take place reactively, causing lack
of efficiency action delays on critical issues or high costs. AI tackles some of these weaknesses by providing
tools that are data-driven and able to learn about patterns, identify anomalies and help optimize management
decisions as they’re made. Figure 3 depicts AI -Machine Learning (ML), Deep Learning (DL) and Computer
Vision (CV)-inclusion in aquaculture systems with data derived from camera, sensors, fish behavior. Moreover,
it also summarizes the stages in an AI lifecycle to data acquisition and pre-processing till model training for
smart fish farm management.

6

Figure 3. AI-Driven smart aquaculture: techniques, data sources, and lifecycle

2.1. Types of AI techniques used

There are many AI methods already used in aquaculture systems. Machine Learning (ML) can be applied
for  water  quality  prediction  [10,  11],  feed  optimization  [12]  and  disease  classification  by  training  with  record
historical data [1]. Deep Learning (DL) which is a subfield of ML technology has gain significant popularity in
the recent years for analyzing complex image and video data, e.g., fish detection  [2], behavior analysis  [6,8],
biomass estimation with CNNs [35]. Underwater cameras are combined with Computer Vision to observe fish
activity, detect stress behavior and measure the abundance of automatically counted individuals [36]. Moreover,
fuzzy logic controller are also adopted to deal with uncertain aquaculture environments and enables the rule-
based reasoning technique for regulating factors such as aeration or feeding in an imprecise conditions  [37].
Such AI techniques contribute to the less need of human effort for CSPTS and its efficiency.

2.1.1. Comparative discussion of AI approaches in aquaculture

Machine  Learning  (ML)  techniques  such  as  support  vector  machines,  random  forests,  and  regression
models  have  been  widely  applied  for  predicting  water  quality  trends,  classifying  disease  symptoms  from
tabular datasets, and optimizing feeding schedules. Their strengths lie in relatively low computational demand
and  interpretability,  which  makes  them  suitable  for  small-  to  medium-scale  farms.  Yet,  ML  models  often
struggle when handling high-dimensional or unstructured inputs such as video and sonar imaging.

Deep Learning (DL), especially Convolutional Neural Networks (CNNs) and Recurrent Neural Networks
(RNNs), offers clear advantages for processing complex image and temporal data. In aquaculture, CNN-based
models  have  achieved  high  accuracy  in  lesion  detection,  abnormal  behavior  recognition,  and  biomass
estimation  from  underwater  video  streams.  RNNs,  by  capturing  temporal  dependencies,  are  particularly
effective  for  predicting  fish  appetite  and  feeding  demand  based  on  behavioral  sequences.  The  challenge,
though, lies in their need for large annotated datasets and substantial computational resources, which may limit
adoption in resource-constrained farms.

7

Computer Vision (CV) serves as the practical interface for DL and ML models, translating underwater
images and video into analyzable features. CV-based disease detection enables real-time diagnosis from fish
skin discoloration or abnormal swimming patterns, while CV-guided feeding optimization adjusts feed supply
based on observed appetite and pellet wastage. While CV approaches are highly scalable in offshore cages
with dense populations, they are vulnerable to issues such as turbidity, lighting variability, and biofouling on
camera lenses.

Overall, ML provides accessible baseline models, DL drives accuracy in complex data environments, and
CV ensures real-time field applicability. A hybrid approach—leveraging ML for structured environmental data,
DL  for  unstructured  imaging  and  CV  for  operational  monitoring—appears  most  promising  for  robust,
multimodal aquaculture systems. This integration aligns with the identified research gap on multimodal AI
frameworks for sustainable and adaptive fish farming.

2.2. Data sources for AI models

The  application  of  AI  in  aquaculture:  Success  and  challenges  although  the  value  of  using  a  AI-based
system is well-recognized, its success will be highly reliant on achievement in data input. Today’s fish farms
use a variety of data sources including underwater sensors that measure the temperature, pH value and salinity
among other parameters, or even dissolved oxygen [1]. Imaging systems (e.g., HD cameras and sonar) collect
visual and acoustic information to track fish health, census populations, count dead biomass for commercial
landings in real time [2], detect when the fish are feeding etc. [38]. For the open-ocean, drones and Autonomous
Underwater Vehicles (AUVs) are becoming commonly used for remote monitoring, inspection of structures
and  habitats  [39].  These  devices  run  constantly,  wirelessly  feeding  data  to  onshore  or  cloud  systems  and
underpinning the real-time AI that is used for farm management.

2.3. AI lifecycle in aquaculture systems

The application of AI technologies in aquaculture generally embodies the life cycle and can be divided
into several stages. The first part, Data Collection is the step where raw data from sensors or cameras and even
actuators  are  gathered  [6].  Then,  the  data  is  pre-processed  (cleaning,  normalization  and  feature  extraction)
integrating it into an adequate format for modelling [40]. The processed dataset is utilized in the training phase
of  model  building  where  various  patterns,  relationships  are  learnt  by  algorithm  under  supervised  and
unsupervised  learning  [41].  Finally,  during  the  decision  support  stage,  that  same  trained  model  informs
predictions  and  automates  responses  (e.g.  modifying  feeding  rates  or  aeration)  in  addition  to  offering
suggestions/insights/alerts for operators [42]. Such a lifecycle supports the closed-loop nature of how AI systems
learn over time based on new data and improved system performance. Table 2 presents six main ingredients
of  AI-driven smart  aquaculture  systems  with  the  associated  technologies,  their  primary  roles  and  real-time
benefits. It highlights how AI supports sustainable and effective monitoring, feeding, health diagnosis of fish
populations and their local conditions in marine based aquaculture.

Table 2. Key components and functions of AI-Based smart aquaculture systems

Component

Technology Used

Primary Function

Benefit in
Aquaculture

Real-Time
Capability

Water Quality Monitoring

IoT Sensors + ML

Detect pH, DO,
temperature

Ensures healthy aquatic
habitat

Fish Health Assessment

Computer Vision +
CNN

Analyze fish behavior
and lesions

Early disease detection

Feeding Optimization

AI Algorithms +
Cameras

Auto-feed based on
fish appetite

Reduces feed waste

Environmental Prediction

Deep Learning
Models

Forecast weather and
water trends

Prepares farm for
disturbances

Yes

Yes

Yes

Yes

8

Component

Technology Used

Primary Function

Benefit in
Aquaculture

Real-Time
Capability

Waste and Contaminant
Detection

Image Processing +
Sensors

Identify pollutants and
debris

Maintains water
cleanliness

Central Decision System

AI Dashboard

Integrates all data and
alerts

Smart control and alerts

Yes

Yes

Table 2. (Continued)

3. AI applications in monitoring systems

Utilization  of  AI  in the  aquaculture  monitoring  system  makes  it  much  more  accurate  and  time  saving
especially  for  an  unfriendly  marine  environment.  AI  allows  round  the  clock,  real-time  tracking  of  living
conditions (e.g. water quality and fish health/condition), feeding regime used or biomass by using machine
learning-based  solutions  combined  with  deep  leaning  and  computer  vision.  These  applications  support
anticipatory  decisions  and  autonomous  operations,  thus  supporting  greater  productivity  and  sustainability.
Figure 4 provides a summary of the AI contribution in aquaculture monitoring by performing real time data
analysis for four main aspects, i.e., water quality management, fish health tracking and feed control together
with biomass estimation.

Figure 4. AI applications in aquaculture monitoring systems

3.1. Water quality monitoring

Good  water  quality  is  critical  for  fish  survival,  growth  and  system  stability  in  aquaculture.  Sensed
parameters  such  as  pH,  temperature,  DO  (dissolved  oxygen),  turbidity  and  ammonia  concentration  are
measured by a distributed sensor network in the AI-based monitoring systems [43]. These quantities can change
rapidly in ocean, such as tides and rain fall etc. Time series data from multiple sensors are processed using
machine  learning  algorithms  to  recognize  patterns,  trends  and  anomalies.  Sensor  fusion  methods  integrate
measurements of multiple sensors to enhance reliability and robustness [44]. The AI model is able to generate

9

alarms or drive controlling devices, e.g., aerators and water exchange pumps for environmental conditions that
are not desired in the aquatic environment.

3.2. Fish health and disease detection

Monitoring the health of fish plays a crucial role in smart aquaculture, especially for large-scale systems
that  cannot  be  easily  inspected  manually.  AI  allows  for  imaging-based  diagnosis  through  deep  learning,
particularly  CNNs  that  recognize  physical  symptoms  of  a  disease  such  as  lesions  or  discoloration  from
underwater  camera  feeds  [45].  Apart  from  visual  observation,  behavior  pattern  algorithms  that  analyses  the
movement data can be used to detect early signals of stress or disease (such as low activity levels, and non-
habitual very  rapid motions)  [46]. When these  models are linked to real-time  monitoring systems predictive
diagnostics and automated alerts can be produced, which could allow farmers to isolate affected fish or alter
environmental conditions before a disease becomes established.

3.3. Feed management and optimization

Feeding  is  one  of  the  most  important  tasks  in  aquaculture  and  misfeeding  can  cause  not  only  poor
economic profit but also water pollution. AI-based systems analyses live video feeds in real time and predictive
models—such  as  CNNs  or  RNNs—are  used  to  predict  feeding  demand  using  fish  behavior,  among  other
measurements [1]. These models enable to dynamically adapt the feeding schedule and ration according to the
actual appetite of fish [47]. AI contributes to time-based and dose-controlled feeding, which also affects the feed
conversion  ratio of those farmed  animals. These  systems  save  money, because  the best water is just never
wasted by overfeeding.

3.4. Fish biomass estimation and counting

Accurate biomass and counting of fish is an important step in determining growth, harvest scheduling, or
stocking  density.  Conventional  approaches  are  invasive  and  laborious,  yet  AI  can  provide  non-invasive
methods  through  sonar  data  camera  footage  as  well  as  computer  visions  models  [48].  Using  deep  learning
algorithms it is possible to process high resolution video feeds and count the number of fish, in a clustered
environment. More recently, AI has been employed with 3D imaging technology (stereo vision and structured
light scanning) to enhance the precision of biomass estimation by calculating fish volume/shape as it swims
through in real time  [36]. These methods allow prediction of growth rate and automatic harvesting schedule,
making it possible to control the farming more efficiently. Key AI applications in aquaculture: monitoring of
water quality, fish health, feed management and biomass estimation are summarized on the table 3. It indicates
artificial  intelligence  methods,  data  sources  and  end-users  advantages  that  are  key  to  encourage  real-time
decision-making, operational efficiency and sustainability in marine aquaculture.

Table 3. AI Applications in Aquaculture Monitoring Systems

Monitoring Area

AI Techniques
Used

Data Sources

Functionality

Key Benefits

Water Quality Monitoring

Machine Learning,
Sensor Fusion

pH, DO, Temp,
Ammonia Sensors

Detect anomalies,
trigger control actions

Stable environment,
reduced manual checks

Fish Health & Disease
Detection

Feed Management

Fish Biomass Estimation

Deep Learning
(CNN), Behavior
Recognition

CNN, RNN, Video
Analytics

Computer Vision,
3D Imaging, Deep
Learning

Underwater
Cameras,
Movement Data

Feeding Videos,
Historical Feed
Data

Identify diseases,
predict outbreaks

Early intervention, lower
mortality

Optimize feed
quantity & timing

Cost savings, minimal
waste

Sonar, 3D
Cameras, Video

Estimate weight,
count fish

Non-intrusive, harvest
planning

10

4. AI in decision support and farm management

Artificial intelligence in smart aquaculture Artificial Intelligence is also not restricted to surveillance and
detection  in  Smart  Aquaculture  systems;  it  further  involves  supporting  decisions  as  well  as  managing
operations. Using AI tools has the potential to make decisions quickly and based on up-to-date information by
synthesizing enormous amounts of environmental, biological, and operational data. These systems enable farm
operators to better  manage resources,  automate tasks and facilitate a proactive approach to dynamic ocean
processes. Using AI within management systems Adds transparency, traceability and sustains the process of
production.

4.1. Smart dashboards and visualization tools

Some of today's AI-driven aquaculture systems come equipped with intelligent dashboards that display
data in an easy to understand and user-friendly manner. The sensors data (censoring tension, spray factor and
weight) is processed through a server database architecture which compresses it to still graphical views of the
system  states  [50].  Charts  and  heat  maps  are  used  to  report  KPIs  such  as  water  quality,  fish  growth,  feed
consumption etc., while simple trend analyses demonstrate changes over time [51]. Through these dashboards,
farm managers can view ongoing operations in real-time, compare historical trends across time periods and
make informed decisions without actively possessing background knowledge of data analysis.

4.2. Real-Time farm control using AI-integrated platforms

By incorporating AI in the management of farms, farmers can control farms automatically and respond to
changes  occurring  about  it  or  system  errors  immediately.  For  instance,  if  AI  notices  a  sudden  decrease  in
dissolved oxygen levels it can instantly switch on the aerators or start water changes [52-54]. Such systems allow
remote monitoring and control which are particularly useful in offshore (and large scale) aquaculture farms
where only limited manual access is possible [55]. Through the use of feedback loops, a system adjusts various
parameters  (e.g.,  feeding  rate  lighting  or  circulation)  according  to  AI-based  recommendations  and  thereby
infinite conditions with minimal human intervention.

4.3. Risk analysis and forecasting

AI can improve resilience in aquaculture by providing predictive risk analytics [8]. With the utilization of
historical along real-time data, ML models can predict on event-based cases like algal blooms and outbursts
of  diseases  or  groups  die-offs  etc.  [53].  These  are  predictions  based  on  observed  relationships  between
environmental  cues  and  biological  responses  through  time.  High  biosecurity  standards  and  early  warning
mechanisms enable to take step decisions, for example with adjusting stocking rate, transferring cages or using
preventive treatments as such, AI enables great financial loss and fish welfare saving [56-62].

4.4. Supply chain integration and yield optimization

Outside  the  farm  gates,  AI  also  has  a  place  in  optimizing  the  wider  aquaculture  supply  chain,  from
planning  production  to  delivering  produce  to  market.  Predictive  models  aid  to  predict  harvest  date,  match
transportation scheduling and production in accordance with the market’s requirements [63-66]. AI solutions can
be connected to inventory systems, traceability platforms and QA protocols in order to guarantee compliance
as well as transparency  [67-70]. Additionally, yield optimization algorithms help to optimize stocking density
and feeding rates as well as harvesting policies in a way that maximizes output while reducing environmental
pollution  or  waste  of  resources.  Table  4  presents  a  summary  of  how  AI  facilitates  the  management  in  an
aquaculture  farm  via  smart  dashboards,  real-time  control,  risk  forecast  and  supply  chain  integration  by
improving automation and decision making as well as operational efficiency.

11

Table 4.  AI applications in decision support and farm management in aquaculture

Application Area

AI Techniques

Function

Data Sources

Automation/Control

Key Benefits

Smart Dashboards
& Visualization

Data
Aggregation,
Visualization
Algorithms

Real-Time Farm
Control

Rule-Based AI,
Control Systems

Risk Analysis &
Forecasting

Machine
Learning,
Predictive
Analytics

Display
KPIs and
trends

Adjust
aerators,
lights,
feeders

Forecast
algal
blooms,
diseases

Sensors, Cameras,
Feeding Logs

Manual Interpretation

Environmental &
Sensor Data

Automated Actions

Historical + Real-
Time Data

Alerts & Recommendations

Supply Chain
Integration

Optimization
Algorithms,
Predictive Models

Align
harvest &
logistics

Inventory, Market
Trends, Yield Data

Integrated Systems

Informed
decisions,
user-friendly
interface

Timely
response,
reduced
manual work

Early
mitigation,
improved
resilience

Market
alignment,
reduced waste

5. Case studies and commercial implementations

The real-world adoption of AI in aquaculture is growing steadily, with several countries and companies
demonstrating  measurable  improvements  in  productivity,  sustainability,  and  operational  efficiency.  This
section presents selected international case studies, reviews of industry-driven AI solutions, and comparative
insights into the outcomes before and after AI integration in fish farming systems.

5.1. Global examples from Norway, Japan, India, and Chile

Countries like Norway and Japan are at the forefront of smart aquaculture. Norway, a global leader in
salmon farming, has implemented AI-driven systems in open-sea cages to monitor water quality, detect sea
lice outbreaks, and optimize feeding using underwater cameras and predictive models. Companies collaborate
with  research  institutions  to  implement  digital  twins  and  automate  farm  operations  under  extreme  weather
conditions.

In Japan, AI technologies are being used to maintain the high quality of yellowtail and tuna farming.
Systems apply deep learning for visual monitoring and utilize sonar to estimate biomass. These developments
have supported sustainable production with reduced feed wastage and better stock control.

In India, several start-ups and research initiatives are applying AI and IoT in shrimp farming and inland
fisheries. Projects in coastal regions of Andhra Pradesh and Tamil Nadu use AI to predict pond water quality
and automate feed management, leading to improved yields and reduced disease risk.

Chile,  another  major  player  in  salmon  aquaculture,  has  deployed  AI-based  platforms  to  monitor  fish
behavior and optimize environmental conditions in fjord-based farms. Machine learning models are applied to
forecast algal blooms and avoid mass mortalities, which have historically affected the region’s aquaculture
operations.

5.2. Review of industry solutions: eFishery, Aquabyte, Aquaai

Several companies have emerged as pioneers in the commercial deployment of AI for aquaculture:

  E-Fishery (Indonesia) provides AI-powered smart feeders that adapt to fish behavior and feeding
patterns. Their systems collect real-time data to optimize feeding schedules, reduce costs, and prevent
overfeeding, particularly in catfish and tilapia farms.

12

  Aquabyte (Norway/USA) uses underwater cameras and deep learning to track individual fish health,
detect lice, and estimate biomass. Their platform helps salmon farmers reduce manual inspections
and adopt precision farming techniques.

  Aquaai (USA) has developed robotic fish equipped with sensors and cameras that swim inside cages
to monitor water parameters and fish welfare. These autonomous units mimic natural fish behaviour
and collect data with minimal disturbance.

Such  solutions  are  designed  for  plug-and-play  deployment  and  offer  cloud-based  analytics,  mobile

dashboards, and integration with existing farm infrastructure.

5.3. Comparative analysis of outcomes before and after AI adoption

Multiple  studies  and  farm-level  reports  have  shown  that  the  adoption  of  AI  leads  to  significant
improvements in aquaculture efficiency and sustainability. Before AI integration, fish farms commonly faced
issues such as inconsistent feeding, delayed detection of health problems, and optimized harvesting schedules.
After implementing AI-based systems, farms reported:

  Feed cost reduction by 15–30% due to precise feeding predictions

  Early disease detection, reducing mortality rates by up to 20%





Improved biomass estimation, resulting in better planning and higher yield accuracy

Increased traceability and compliance with environmental standards

These  comparisons  demonstrate  that  AI  not  only  improves  operational  performance  but  also  reduces
ecological impact and enhances data transparency, making it a critical enabler of next-generation aquaculture
practices.

Across documented implementations, AI adoption has yielded measurable technical benefits. For example,
feed efficiency improvements of 15–30% have been reported when adaptive feeding algorithms replace manual
schedules. Early disease detection using computer vision and deep learning has led to mortality rate reductions
of 10–20%, depending on species and farm conditions. Biomass estimation tools based on CNNs and sonar
integration have achieved prediction accuracies above 90%, enabling optimized harvest planning and reducing
waste. From an economic perspective, farms adopting AI-powered platforms such as eFishery and Aqua byte
have reported operational cost savings between 12–25% due to reduced labor, optimized feed use, and lower
loss from disease. These quantitative outcomes highlight the tangible technical and economic impact of AI
solutions, reinforcing their role in advancing sustainable aquaculture practices.

6. Challenges and limitations

Despite the promising advancements in AI-based smart aquaculture, several challenges and limitations
hinder  its  widespread  adoption,  particularly  in  open-ocean  environments.  These  issues  span  technical,
economic, environmental, and ethical domains, and need to be carefully addressed to ensure the long-term
success and scalability of intelligent aquaculture systems.

6.1. Data scarcity and inconsistency in offshore environments

A crucial obstacle in the application of AI to ocean fish farming is a lack of reliable, high-quality data. AI
models depend on a large amount of data in order to train and validate, but offshore sites are often subject to
frequent gaps due sensor failures, transmission breakdowns and power limitations. Challenging environmental
conditions  in  the  marine  environment  are  not  conducive  to  continuous  and  accurate  quantitative  data  on
variables of interest, such as fish activity, water chemistry and system performance. This lack of data results
in low relationship or generalization power for AI models, which may not adapt between different farms and
species.  There  are  numerous  examples  where  models,  trained  on  inshore  or  laboratory  datasets  do  not

13

generalize  well  for  offshore  conditions.  To  mitigate  these  limitations,  several  technical  strategies  can  be
employed. Redundancy in sensor networks ensures continuous monitoring by deploying multiple sensors for
the  same  parameter,  thereby  reducing  data  gaps  caused  by  failures  or  transmission  errors.  Sensor  fusion
techniques combine data from heterogeneous sources—such as sonar, optical cameras, and chemical probes—
to enhance reliability and compensate for individual sensor noise or drift. Moreover, synthetic data generation
methods,  including  physics-based  simulations  and  generative  adversarial  networks  (GANs),  can  augment
scarce  offshore  datasets  by  creating  realistic  training  samples  for  AI  models.  Together,  these  approaches
improve  model  robustness,  reduce  overfitting  to  limited  data,  and  enable  more  reliable  deployment  of  AI
systems in challenging offshore aquaculture environments.

6.2. High setup costs and maintenance issues

Operation  of  AI-based  systems  in  marine  aquaculture  requires  significant  investment  at  the  outset  for
hardware,  infrastructure  and  software  integration.  High-resolution  cameras,  underwater  sensors  and
autonomous vehicles are expensive to purchase or install in many cases) and technical know-how is needed.
In  addition,  the  operation  load  is  increased  by  keeping  these  systems  in  corrosive  saline  and  remote  sites.
Sensors calibration, battery changing, biofouling control and data transfer systems require maintenance which
may not be possible in the cases of small or medium fish farming production. Adoption of these technologies
is expensive and acts as a barrier, particularly for regions where aquaculture activities are fledgling.

6.3. Environmental factors: Tides, storms, and salinity variability

Cage systems in open sea are typically exposed to environmental factors like tide and surge, wave action
as  well  variable  salinities.  (These  also  have  negative  effects  on  fish  as  well,  but  they  can  distort  sensor
measurements  and  AIs  performance  too.)  Inclement  weather  can  throw  equipment  out  of  place,  knock
communications offline and stop data collection and system control in its tracks. Additionally, salinity and
temperature  are  not  homogeneous  in  the  deeper  water  layers  for  calibration  of  sensors  impacting  AV
predictions by AI. Approaches that do not accommodate this variability can result in either false positive alarms
or the failure to detect important events and, thus, may have limited practical utility.

Emerging  AI approaches offer new ways to manage such environmental variability. Physics-informed
neural networks (PINNs) integrate governing equations of fluid dynamics and environmental processes into
the  learning  framework,  allowing  predictions  that  remain  robust  even  under  sparse  or  noisy  sensor  data.
Similarly, hybrid AI–physics models combine machine learning with established hydrodynamic and ecological
models, improving the accuracy of forecasts for tides, salinity gradients, and storm impacts on cage stability.
These  methods  enable  more  reliable  predictions  in  dynamic  offshore  conditions,  where  purely  data-driven
models  may  fail.  By  embedding  physical  constraints  into  the  learning  process,  such  models  can  enhance
resilience,  reduce  false  alarms,  and  support  proactive  management  decisions  in  ocean-based  aquaculture
systems.

6.4. Ethical concerns and dependency on automation

As AI systems become more autonomous in making decisions, questions about over-reliance on fully-
automated decisions naturally follow. While critical judgments such as feeding, medicating or harvesting can
be delegated to algorithms without appropriate human supervision could produce unintended outcomes. For
example, an algorithm that is not functioning properly might underfeed fish or miss the early onset of a disease.
Moreover, the emerging automation would reduce jobs available for workers with traditional aquaculture tasks
which may create social issues in rural areas. The transparency and explainability of AI decisions, as well,
continues to be an issue however when trying to parse complex deep learning outputs that seem unmoored
from clear explanation.

14

To  address  this,  Explainable  AI  (XAI)  methods  are  increasingly  being  explored  in  aquaculture
applications. Techniques such as saliency mapping and Grad-CAM can visually highlight which parts of an
image influenced a CNN’s decision, making disease detection in fish more transparent to farmers. Similarly,
SHAP  (Shapley  Additive  Explanations)  and  LIME  (Local  Interpretable  Model-agnostic  Explanations)  can
identify how environmental parameters like dissolved oxygen or salinity contribute to predictive outcomes in
feed  optimization  or  mortality  risk  assessment.  By  embedding  such  interpretability  tools  into  aquaculture
dashboards,  operators  can  better  understand  model  reasoning,  validate  predictions  against  their  domain
knowledge,  and  maintain  human  oversight.  Incorporating  XAI  thus  reduces  blind  reliance  on  opaque
algorithms and supports more ethical, trustworthy, and accountable deployment of deep learning systems in
aquaculture.  Table  5  gives  Summary  of  main  challenges  that  prevent  A.I.  from  being  widely  adopted  in
offshore aquaculture classified into technical, economic, environmental and ethical issues. It details the reasons
for each problem, its effects and potential ways to address it.

Table 5. Challenges and Limitations in AI-Based Smart Aquaculture

Challenge Area

Subsection

Description

Underlying
Cause

Affected
Domain

Impact

Remarks

Data Issues

Data Scarcity
and
Inconsistency

Economic
Barriers

High Setup
Costs and
Maintenance

Environmental
Challenges

Tides, Storms,
and Salinity
Variability

Ethical and
Social Issues

Dependency on
Automation

Offshore
systems lack
consistent,
high-quality
datasets for
training AI
models.

High cost of
equipment and
maintenance
limits
scalability,
especially for
small farmers.

Weather
events and
ocean
variability
interfere with
AI system
reliability.

Automated
systems may
make flawed
decisions or
reduce human
employment.

Sensor
failures,
power issues,
dynamic
marine
conditions

Expensive
hardware,
harsh
environment
maintenance
needs

Natural ocean
disturbances
and sensor
calibration
issues

Lack of
human
oversight,
opaque AI
decision-
making

Technical

Poor model
generalization;
reduced
accuracy

Requires robust
data strategies
and
redundancy

Economic

Low adoption in
developing
regions

Subsidies or
cost-effective
models needed

Environmental

Inaccurate
readings;
equipment
damage

Design systems
for extreme
environments

Ethical/Social

Risk of error,
job displacement

Ensure
explainability
and hybrid
control models

7. Research gaps and future scope

While the integration of AI in smart aquaculture has shown considerable promise, several research gaps
still exist that limit the full realization of its potential. Addressing these gaps is essential to move from isolated
applications  toward  holistic,  adaptive,  and  intelligent  aquaculture  systems  that  are  scalable,  resilient,  and
environmentally  sustainable.  The  following  sub-sections  outline  the  key  areas  where  further  research  and
innovation are required.

7.1. Need for multimodal AI systems

Most  AI  applications  in  aquacultureally  employ  individual  data  sources,  such  as  visual  or  time-series
sensor  data.  Fal1:  However,  ocean  farming  is  a  complex  environment  where  physical  dynamics  influence
biological and environmental processes all at the same time. Multimodal AI systems that can read and correlate

15

different kinds of data, (e.g. images with sonar readings, chemical sensor outputs with weather forecasts), are
increasingly demanded in practice. Such systems would enable stronger and more context aware predictions,
increasing  the  robustness  of  decision-making  in  uncertain  and  varying  marine  conditions.  Investigating
multimodal fusion methods, cross-domain learning based on hybrid mounting and AI models is the cornerstone
to get this method working properly.

Deploying  multimodal  AI  in  offshore  aquaculture  also  presents  several  practical  challenges.  Data
synchronization across heterogeneous sources—such as cameras, sonar, and water-quality sensors—requires
precise temporal alignment, as delays or mismatches can degrade model accuracy. Bandwidth limitations in
remote marine environments constrain the real-time transfer of high-resolution video or sensor data to cloud
servers, often necessitating compression or selective transmission strategies. Moreover, computational load at
the edge is a critical factor, since running deep learning inference directly on offshore devices requires energy-
efficient hardware and optimized algorithms. Without addressing these constraints, multimodal frameworks
risk becoming impractical for continuous farm monitoring. Research on lightweight AI architectures, edge–
cloud hybrid models, and adaptive sampling strategies will be essential to overcome these technical hurdles
and unlock the full potential of multimodal systems in real-world aquaculture.

7.2. Integration of AI with digital twins and robotics

Another significant research frontier lies in the integration of AI with digital twin models and autonomous
robotics. A digital twin is a virtual replica of a physical aquaculture system that enables simulation, forecasting,
and real-time optimization. When combined with AI, digital twins can model fish behavior, environmental
changes, and equipment performance with high precision. Similarly, incorporating AI into robotic systems—
such as autonomous underwater vehicles (AUVs), robotic feeders, and cleaning drones—can support dynamic
adaptation and autonomous decision-making in complex underwater environments. Current research is limited
in this area, and developing coordinated frameworks that combine sensing, actuation, and virtual modelling
remains an open challenge.

In practical deployment, digital twins rely on continuous synchronization between physical systems and
their virtual replicas. AI models play a central role in this loop by processing incoming sensor data, calibrating
the  digital  twin  against  observed  states,  and  updating  simulation  parameters  in  real  time.  For  instance,
predictive  models  can  adjust  hydrodynamic  simulations  of  cage  environments  based  on  live  current  and
temperature  data,  ensuring  the  twin  reflects  evolving  conditions.  Model  calibration  and  validation  are
performed by comparing simulated outputs (e.g., fish growth curves, water quality predictions) with actual
farm  measurements,  thereby  refining both  the  AI  model  and  the  twin’s  fidelity.  Real-time  synchronization
allows proactive decision-making, such as adjusting feeding regimes or triggering maintenance alerts, before
deviations in the physical farm escalate. This iterative interplay between AI and digital replicas demonstrates
the potential of digital twins not only for forecasting but also for adaptive, closed-loop farm management in
offshore aquaculture.

7.3. Standardization of protocols and data formats

The lack of standardized protocols for data collection, labelling, storage, and sharing poses a barrier to
large-scale AI adoption in aquaculture. Presently, most farms operate in silos, using proprietary systems and
non-uniform sensor configurations. This fragmentation restricts the development of scalable AI models and
impedes collaboration across research and industry. There is a pressing need to define universal data formats,
benchmarking datasets, and interoperability standards for AI tools in aquaculture. Such standardization will
facilitate  model  validation,  reproducibility  of  results,  and  cross-farm  integration,  thereby  accelerating
innovation and regulatory acceptance.

16

Some  preliminary  steps  toward  standardization  are  already  emerging.  For  example,  the  International
Organization for Standardization (ISO) has developed guidelines related to aquaculture operations and data
handling,  such  as  ISO  12878  for  traceability  of  finfish  products,  which  could  be  extended  to  AI-driven
monitoring systems. In parallel, open-source benchmarking datasets are being curated by research groups in
Norway, Japan, and China, focusing on fish disease images, underwater behavior videos, and water quality
sensor streams. These resources enable reproducibility of AI models and provide a foundation for comparative
evaluation across research studies. Collaborative frameworks, such as the Global Aquaculture Alliance’s data-
sharing initiatives, also highlight the push toward interoperability. Incorporating these early standardization
efforts into future frameworks will help bridge the gap between experimental AI applications and industry-
wide deployment.

7.4. AI for sustainable and climate-resilient aquaculture

As  climate  change  continues  to  impact  ocean  ecosystems,  AI  can  serve  as  a  key  enabler  of  climate-
resilient  and  sustainable  aquaculture.  Predictive  analytics  can  forecast  temperature  anomalies,  disease
outbreaks,  or  harmful  algal  blooms,  helping  farms  prepare  for  environmental  stress.  AI  can  also  optimize
resource use—such as feed, water, and energy—thus reducing environmental footprint. However, research is
still limited in exploring how AI can be designed with sustainability goals in mind. Future studies should focus
on energy-efficient AI models, low-power hardware, and decision systems that promote biodiversity, reduce
waste, and support circular aquaculture economies.

8.  Conclusion

This review highlights the transformative role of artificial intelligence in modern ocean-based aquaculture.

AI technologies—including machine learning, computer vision, and deep learning—are instrumental in real-
time water quality monitoring, disease detection, feeding optimization, and biomass estimation. Commercial
implementations  like  eFishery,  Aquabyte,  and  Aquaai  demonstrate  measurable  benefits  in  yield,  cost-
efficiency, and sustainability. However, key challenges persist, such as data scarcity in offshore environments,
high setup and maintenance costs, environmental variability, and ethical concerns over automation. Notably,
research gaps remain in developing multimodal AI models, integrating AI with digital twins and robotics, and
establishing  standardized  data  protocols.  The  review  emphasizes  the  potential  of  AI  not  only  to  improve
productivity and reduce manual intervention but also to contribute to environmentally resilient and ethically
sound aquaculture systems. Moving forward, emphasis must be placed on developing scalable, adaptive, and
sustainable AI solutions tailored for dynamic marine conditions to support global seafood security.

Author Contributions

Pramod Dhamdhere contributed to conceptualization, methodology, and the preparation of the initial draft.
Swati Dixit provided expertise in electronics and telecommunication aspects, data interpretation, and critical
review of the manuscript. Manjusha Tatiya was responsible for formal analysis, visualization, and refining the
technical discussion on AI and data science applications. Babaso A. Shinde contributed to the design of AI-
based  frameworks,  data  collection,  and  validation.  Anant  Kaulage  supported  software  development,  data
curation,  and  assisted  in  editing.  Yogendra  Patil  participated  in  literature  survey,  technical  validation,  and
manuscript  proofreading.  Rupesh  Gangadhar  Mahajan  provided  resources,  critical  revisions,  and  technical
insights  into  computer  engineering  applications.  Shital  Yashwant  Waware  refined  the  methodology,
supervised the technical content, and contributed to reviewing and editing. Anant Sidhappa Kurhade led the
overall  project  administration,  conceptualization,  supervision,  and  manuscript  review,  and  served  as  the
corresponding author.

17

Acknowledgments

The authors would like to express their sincere gratitude to Dr. D. Y. Patil Institute of Technology and
Dr. D. Y. Patil Dnyan Prasad University, Pimpri, Pune, India, for providing the necessary support and research
infrastructure. The authors also acknowledge the administrative and technical assistance extended during this
study, which contributed significantly to the successful completion of this work.

Conflict of interest

The authors declare no conflict of interest

References
1.  Huang Y, Khabusi SP. Artificial Intelligence of Things (AIoT) Advances in Aquaculture: A Review. Processes.

2025;13(1):73. https://doi.org/10.3390/pr13010073

2.  Channa AA, Munir K, Hansen M, Tariq MF. Optimisation of Small-Scale Aquaponics Systems Using Artificial

Intelligence and the IoT: Current Status, Challenges, and Opportunities. Encyclopedia. 2024;4(1):313.
https://doi.org/10.3390/encyclopedia4010023

3.  Tina FW, Afsarimanesh N, Nag A, Alahi MEE. Integrating AIoT Technologies in Aquaculture: A Systematic

Review. Future Internet. 2025;17(5):199. https://doi.org/10.3390/fi17050199

4.  Capetillo-Contreras O, Pérez-Reynoso FD, Zamora-Antuñano MA, Álvarez-Alvarado JM, Rodríguez‐Reséndiz J.
Artificial Intelligence-Based Aquaculture System for Optimizing the Quality of Water: A Systematic Analysis.
Journal of Marine Science and Engineering. 2024;12(1):161. https://doi.org/10.3390/jmse12010161

5.  Vo TTE, Ko H, Huh J, Kim Y. Overview of Smart Aquaculture System: Focusing on Applications of Machine

Learning and Computer Vision. Electronics. 2021;10(22):2882. https://doi.org/10.3390/electronics10222882
6.  Ubina NA, Lan HY, Cheng S, et al. Digital twin-based intelligent fish farming with Artificial Intelligence Internet

of Things (AIoT). Smart Agricultural Technology. 2023;5:100285. https://doi.org/10.1016/j.atech.2023.100285
7.  Kao CY, Chen IC. Smart City Aquaculture: AI-Driven Fry Sorting and Identification Model. Applied Sciences.

2024;14(19):8803. https://doi.org/10.3390/app14198803

8.  Rather MA, Ahmad I, Shah A, et al. Exploring opportunities of Artificial Intelligence in aquaculture to meet
increasing food demand. Food Chemistry X. 2024;22:101309. https://doi.org/10.1016/j.fochx.2024.101309
9.  Mustapha UF, Alhassan A, Jiang D, Li G. Sustainable aquaculture development: a review on the roles of cloud
computing, internet of things and artificial intelligence (CIA). Reviews in Aquaculture. 2021;13(4):2076.
https://doi.org/10.1111/raq.12559

10.  Danvirutai P, Charoenwattanasak S, Tola S, et al. An integrating RAG-LLM and deep Q-network framework for
intelligent fish control systems. Scientific Reports. 2025;15(1). https://doi.org/10.1038/s41598-025-05892-3
11.  Chang C, Wang JH, Wu J, et al. Applying Artificial Intelligence (AI) Techniques to Implement a Practical Smart

Cage Aquaculture Management System. Journal of Medical and Biological Engineering. 2021.

12.  Kassem T, Shahrour I, Khattabi JE, Raslan A. Smart and Sustainable Aquaculture Farms. Sustainability.

2021;13(19):10685. https://doi.org/10.3390/su131910685

13.  Chahid A, N’Doye I, Majoris JE, Berumen ML, Laleg‐Kirati T. Model Predictive Control Paradigms for Fish

Growth Reference Tracking in Precision Aquaculture. arXiv (Cornell University). 2021.
https://arxiv.org/abs/2102.00004

14.  Zukeram ESJ, Provensi LL, Oliveira M, et al. In Situ IoT Development and Application for Continuous Water

Monitoring in a Lentic Ecosystem in South Brazil. Water. 2023;15(13):2310. https://doi.org/10.3390/w15132310
15.  Gillani SA, Abbasi R, Martínez P, Ahmad R. Review on Energy Efficient Artificial Illumination in Aquaponics.

Cleaner and Circular Bioeconomy. 2022;2:100015. https://doi.org/10.1016/j.clcb.2022.100015

16.  Lu C, Chen S, Hung S. Application of Novel Technology in Aquaculture. In: IntechOpen eBooks. IntechOpen.

2019. https://doi.org/10.5772/intechopen.90142

17.  Gorbunova A, Kostin VE, Pashkevich IL, et al. Prospects and opportunities for the introduction of digital

technologies into aquaculture governance system. IOP Conference Series Earth and Environmental Science.
2020;422(1):12125. https://doi.org/10.1088/1755-1315/422/1/012125

18.  Akram W, Din MU, Soud LS, Hussain I. A Review of Generative AI in Aquaculture: Foundations, Applications,

and Future Directions for Smart and Sustainable Farming. 2025. https://arxiv.org/abs/2507.11974

19.  Small BC, Hardy RW, Tucker CS. Enhancing fish performance in aquaculture. Animal Frontiers. 2016;6(4):42.

https://doi.org/10.2527/af.2016-0043

20.  Melak A, Aseged T, Shitaw T. The Influence of Artificial Intelligence Technology on the Management of

Livestock Farms. International Journal of Distributed Sensor Networks. 2024.
https://doi.org/10.1155/2024/8929748

18

21.  Agrawal K, Goktas P, Holtkemper M, et al. AI-driven transformation in food manufacturing: a pathway to

sustainable efficiency and quality assurance. Frontiers in Nutrition. 2025;12.
https://doi.org/10.3389/fnut.2025.1553942

22.  Føre M, Frank K, Norton T, et al. Precision fish farming: A new framework to improve production in aquaculture.

Biosystems Engineering. 2017;173:176. https://doi.org/10.1016/j.biosystemseng.2017.10.014

23.  Ek A, BT F, OA O. Comparative analysis of production performance in integrated aquaculture system and single
system of production of fish, rice, poultry and pig. International Journal of Aquaculture and Fishery Sciences.
2020;74. https://doi.org/10.17352/2455-8400.000060

24.  Almoselhy RIM, Usmani A. AI in Food Science: Exploring Core Elements, Challenges, and Future Directions.
Open Access Journal of Microbiology & Biotechnology. 2024;9(4):1. https://doi.org/10.23880/oajmb-16000313

25.  Neethirajan S. AI in Sustainable Pig Farming: IoT Insights into Stress and Gait. Agriculture. 2023;13(9):1706.

https://doi.org/10.3390/agriculture13091706

26.  Mana AA, Allouhi A, Hamrani A, et al. Sustainable AI-based production agriculture: Exploring AI applications

and implications in agricultural practices. Smart Agricultural Technology. 2024;7:100416.
https://doi.org/10.1016/j.atech.2024.100416

27.  Sidhu KS, Gill AS, Arora A, et al. Advancements in farming and related activities with the help of artificial

intelligence: a review. Environment Conservation Journal. 2021;22:55. https://doi.org/10.36953/ecj.2021.se.2206

28.  Alkhafaji MA, Ramadan GM, Jaffer Z, Jasim L. Revolutionizing Agriculture: The Impact of AI and IoT. E3S Web

of Conferences. 2024;491:1010. https://doi.org/10.1051/e3sconf/202449101010

29.  Zatsu V, Shine AE, Tharakan JM, et al. Revolutionizing the food industry: The transformative power of artificial

intelligence-a review. Food Chemistry X. 2024;24:101867. https://doi.org/10.1016/j.fochx.2024.101867
30.  Chen T, Lv L, Wang D, et al. Revolutionizing Agrifood Systems with Artificial Intelligence: A Survey. arXiv

(Cornell University). 2023. https://arxiv.org/abs/2305.01899

31.  Hassoun A, Cropotova J, Trollman H, et al. Use of industry 4.0 technologies to reduce and valorize seafood waste
and by-products: A narrative review on current knowledge. Current Research in Food Science. 2023;6:100505.
https://doi.org/10.1016/j.crfs.2023.100505

32.  Artificial Intelligence and Deep Learning in Sensors and Applications. MDPI eBooks. 2024.

https://doi.org/10.3390/books978-3-7258-1452-7

33.  Rana R, Kalia A, Boora A, et al. Artificial Intelligence for Surface Water Quality Evaluation, Monitoring and

Assessment. Water. 2023;15(22):3919. https://doi.org/10.3390/w15223919

34.  Yang H, Liu S. A prediction model of aquaculture water quality based on multiscale decomposition. Mathematical

Biosciences & Engineering. 2021;18(6):7561. https://doi.org/10.3934/mbe.2021374

35.  Ali A, Ali H, Saeed A, et al. Blockchain-Powered Healthcare Systems: Enhancing Scalability and Security with

Hybrid Deep Learning. Sensors. 2023;23(18):7740. https://doi.org/10.3390/s23187740

36.  Li Y, Wu Z, Yu Y, Liu CH. An Improved YOLOv8 and OC-SORT Framework for Fish Counting. Journal of

Marine Science and Engineering. 2025;13(6):1016. https://doi.org/10.3390/jmse13061016

37.  Alim SA, Sumaila M, Ritkangnga IY. Design of a Fuzzy Logic Controller for Optimal African Catfish Water

Production. Mekatronika. 2021;3(2):42. https://doi.org/10.15282/mekatronika.v3i2.7352

38.  Lin J, Tsai HL, Lyu WH. An Integrated Wireless Multi-Sensor System for Monitoring the Water Quality of

Aquaculture. Sensors. 2021;21(24):8179. https://doi.org/10.3390/s21248179

39.  Ubina NA, Cheng S. A Review of Unmanned System Technologies with Its Application to Aquaculture Farm

Monitoring and Management. Drones. 2022;6(1):12. https://doi.org/10.3390/drones6010012

40.  Samatas GG, Moumgiakmas SS, Papakostas GA. Predictive Maintenance -- Bridging Artificial Intelligence and

IoT. arXiv (Cornell University). 2021. https://arxiv.org/abs/2103.11148

41.  Lu X, Zhang H. Sentiment Analysis Method of Network Text Based on Improved AT-BiGRU Model. Scientific

Programming. 2021;2021:1. https://doi.org/10.1155/2021/6669664

42.  Naqa IE, Murphy MJ. What Is Machine Learning? In: Springer eBooks. Springer Nature. 2015:3.

https://doi.org/10.1007/978-3-319-18305-3_1

43.  Sivakumar S, Ramya V. An Intuitive Remote Monitoring Framework for Water Quality in Fish Pond using Cloud

Computing. In: IOP Conference Series Materials Science and Engineering. 2021;12037.
https://doi.org/10.1088/1757-899x/1085/1/012037

44.  Duro N. Sensor Data Fusion Analysis for Broad Applications. Sensors. 2024;24(12):3725.

https://doi.org/10.3390/s24123725

45.  Sarker S, Biswas A, Nasim MAA, et al. Case Studies on X-Ray Imaging, MRI and Nuclear Imaging. arXiv

(Cornell University). 2023. https://arxiv.org/abs/2306.02055

46.  Yu X, Wang Y, An D, Wei Y. Identification methodology of special behaviors for fish school based on spatial

behavior characteristics. Computers and Electronics in Agriculture. 2021;185:106169.
https://doi.org/10.1016/j.compag.2021.106169

47.  Zhao H, Wu J, Liu L, et al. A real-time feeding decision method based on density estimation of farmed fish.

Frontiers in Marine Science. 2024;11. https://doi.org/10.3389/fmars.2024.1358209

48.  Zhang S, Yang X, Wang Y, et al. Automatic Fish Population Counting by Machine Vision and a Hybrid Deep

Neural Network Model. Animals. 2020;10(2):364. https://doi.org/10.3390/ani10020364

19

49.  Kandimalla V, Richard M, Smith FH, et al. Automated Detection, Classification and Counting of Fish in Fish

Passages With Deep Learning. Frontiers in Marine Science. 2022;8. https://doi.org/10.3389/fmars.2021.823173

50.  Lee PG. Process control and artificial intelligence software for aquaculture. Aquacultural Engineering.

2000;23:13. https://doi.org/10.1016/s0144-8609(00)00044-3

51.  Aljehani F, N’Doye I, Laleg‐Kirati T. Feeding control and water quality monitoring in aquaculture systems:

Opportunities and challenges. arXiv (Cornell University). 2023. https://arxiv.org/abs/2306.09920

52.  Chen X, Li D, Mo D, et al. Three-Dimensional Printed Biomimetic Robotic Fish for Dynamic Monitoring of
Water Quality in Aquaculture. Micromachines. 2023;14(8):1578. https://doi.org/10.3390/mi14081578

53.  Kalogiannidis S, Kalfas D, Papaevangelou O, et al. The Role of Artificial Intelligence Technology in Predictive

Risk Assessment for Business Continuity: A Case Study of Greece. Risks. 2024;12(2):19.
https://doi.org/10.3390/risks12020019

54.  Mann K, Good N, Fatehi F, et al. Predicting Patient Deterioration: A Review of Tools in the Digital Hospital

Setting. Journal of Medical Internet Research. 2021;23(9). https://doi.org/10.2196/28209

55.  Amosu OR, Kumar P, Ogunsuji YM, et al. AI-driven demand forecasting: Enhancing inventory management and

customer satisfaction. World Journal of Advanced Research and Reviews. 2024;23(2):708.
https://doi.org/10.30574/wjarr.2024.23.2.2394

56.  Ramani, P., Reji, V., Sathish Kumar, V., et al., 2025. Deep learning-based detection and classification of moss and
crack damage in rock structures for geo-mechanical preservation. Journal of Mines, Metals & Fuels. 73(3), 345–
352.

57.  Chippalkatti, S., Chekuri, R.B., Ohol, S.S., et al., 2025. Enhancing heat transfer in micro-channel heat sinks

through geometrical optimization. Journal of Mines, Metals & Fuels. 73(3), 353–361.

58.  Kurhade, A.S., Siraskar, G.D., Chekuri, R.B., et al., 2025. Biodiesel blends: A sustainable solution for diesel

engine performance improvement. Journal of Mines, Metals & Fuels. 73(3), 362–370.

59.  Kurhade, A.S., Bhavani, P., Patil, S.A., et al., 2025. Mitigating environmental impact: A study on the performance

and emissions of a diesel engine fueled with biodiesel blend. Journal of Mines, Metals & Fuels. 73(4), 981–989.

60.  Wakchaure, G.N., Vijayarao, P., Jadhav, T.A., et al., 2025. Performance evaluation of trapezoidal ducts with delta
wing vortex generators: An experimental investigation. Journal of Mines, Metals & Fuels. 73(4), 991–1003.
61.  Wakchaure, G.N., Jagtap, S.V., Gandhi, P., et al., 2025. Heat transfer characteristics of trapezoidal duct using delta

wing vortex generators. Journal of Mines, Metals & Fuels. 73(4), 1053–1056.

62.  Chougule, S.M., Murali, G., Kurhade, A.S., 2025. Failure investigation of the driving shaft in an industrial paddle

mixer. Journal of Mines, Metals & Fuels. 73(5), 1247–1256.

63.  Kurhade, A.S., Sugumaran, S., Kolhalkar, N.R., et al., 2025. Thermal management of mobile devices via PCM.

Journal of Mines, Metals & Fuels. 73(5), 1313–1320.

64.  Chougule, S.M., Murali, G., Kurhade, A.S., 2025. Finite element analysis and design optimization of a paddle

mixer shaft. Journal of Mines, Metals & Fuels. 73(5), 1343–1354.

65.  Waware, S.Y., Ahire, P.P., Napate, K., et al., 2025. Advancements in heat transfer enhancement using perforated

twisted tapes: A comprehensive review. Journal of Mines, Metals & Fuels. 73(5), 1355–1363.

66.  Patil, Y., Tatiya, M., Dharmadhikari, D.D., et al., 2025. The role of AI in reducing environmental impact in the

mining sector. Journal of Mines, Metals & Fuels, 73(5), 1365–1378.

67.  Napte, K., E. Kondhalkar, G., Vishal Patil, S., Vishnu Kharat, P., Snehal Mayur Banarase, Sidhappa Kurhade, A.,
& Shital Yashwant Waware. (2025). Recent Advances in Sustainable Concrete and Steel Alternatives for Marine
Infrastructure. Sustainable Marine Structures, 7(2), 107–131. https://doi.org/10.36956/sms.v7i2.2072

68.  Sarode, G. C., Gholap, P., Pathak, K. R., Vali, P. S. N. M., Saharkar, U., Murali, G., & Kurhade, A. S. (2025).
Edge AI and Explainable Models for Real-Time Decision-Making in Ocean Renewable Energy Systems.
Sustainable Marine Structures, 7(3), 17–42. https://doi.org/10.36956/sms.v7i3.2239

69.  Kurhade AS, Kharat PV, Chougule SM, Darade MM, Karad MM, Murali G, Charwad GA, Waware SY, Yadav

RS. Harnessing the Power of Plastic Waste: A Sustainable Approach to Fuel Production. Journal of Mines, Metals
& Fuels. 2025 Feb 1;73(2).

70.  Raut PN, Dolas AS, Chougule SM, Darade MM, Murali G, Waware SY, Kurhade AS. Green Adsorbents for

Heavy Metal Removal: A Study on Zinc Ion Uptake by Tinospora cordifolia Biocarbon. Journal of Mines, Metals
& Fuels. 2025 Jan 1;73(1).

20

