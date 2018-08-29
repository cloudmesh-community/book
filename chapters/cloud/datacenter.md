# Data Center

:question: indicates opportunitiess for comprehension assignments while contributing to this document.

---

**Learning Outcome**

* What is a data center.
* What are import metrics.
* what is the diffrence wbetween a Cloud data center and a traditional datacenter.
* What are exampless of Cloud data centers.

---

## Cloud Data Centers



## Data Center Metrics


## Data Center Carbon Footprint

Scientists world wide have idenetified a link between carbon emisison and global warming. As the energy consumption of a data center is ssubstantial, it is prudent to estimate the overall carbon emisssion. Schneider Electric (formerly APC) has provided a report on how to estimate the Carbon footprint of a data center. 

* Estimating a Data Center’s
Electrical Carbon Footprint, White Paper 66,  <http://www.apc.com/salestools/DBOY-7EVHLH/DBOY-7EVHLH_R0_EN.pdf>

Although this report is already a bit older, it provides still valuable information. It defines key terms such as

* Carbon dioxide emissions coefficient (“carbon footprint”) 
	* :question:
* Peaker plant
	* :question:
* Avoided emissions
	* :question:
* CO2 (carbon dioxide, or “carbon”) 
	* :question:

The data ceneter will have a total carbon profile, that includes the many different asspects of a data center contributing to carbon emissions. This includes manufacturing, packaging, transportation, storage, operation of the data center, and decomissisoning. THus it is important to notice that we not only need to consider the operation but also the construction and decomisssison phasess. 

### Data Center Operational Impact

One of the main operational impacts is the cost and emisions of a data center cause by running, and cooling the servers in the data center. Naturally this is dependent on the type of fuel that is used to produce the energy. The actual carbon impact using electricity certainly depends on the type of powerplant that is ussed to provide it. Thesse energy costs and disstribution of where the energy comes from can often be looked up by geographical regions  on the internet or form the local energy provider. Municipal government organizations may also have such information. Tools such as the Indiana State Profile and Energy Use 

* <https://www.eia.gov/state/?sid=IN>  

may provide valuable information to derive such estimates. Correlating a data center with cheap energy is a key factor. To estimate both costsss in terms of price and carbon emisiion SSchneider provides a convenient Carbon estimate calculator based on enrgy consumption.

* <https://www.schneider-electric.com/en/work/solutions/system/s1/data-center-and-network-systems/trade-off-tools/data-center-carbon-footprint-comparison-calculator/tool.html>
* <http://it-resource.schneider-electric.com/digital-tools/calculator-data-center-carbon>

If we calculate the total cost, we needd naturally add all costs arissing from build and teardown pahse as well as operational upgrades. 

**Comprehension Assignment**

**Carbon.1:** Carbon footprint of a data center

> Complete the definitions of the terms used in this section

**Carbon.2:** Carbon footprint of data centers

> World wide we have many data centers. Your task will be to find the carbon emisssion of a data center and its cost in $ based on energy use on a yearly bassis. Add your findings to the following table. Make sure you avoid redundant reporting and find a new datacenter. A google docss will be provided to coordinate with the class participants

Table: Cost of the data center


| Data Center | Location | Year | Electricity Cost* | IT Load | Yearly Cost | Yearly CO2 Footprint | Equivalent in Cars |   |
|-------------|----------|------|-------------------|---------|-------------|----------------------|--------------------|---|
| :?:         | :?:      | :?:  | :?:               | :?:     | :?:         | :?:                  | :?:                |   |
|             |          |      |                   |         |             |                      |                    |   |
|             |          |      |                   |         |             |                      |                    |   |


*as adjusted in calculator

> If you find other estimatess for a data center or an entire data center fleet such as AWS world wide, please provide citations.

**Carbon.3:** Your own Carbon footprint

> It is interestsing to compare and measure your own carbon footprint. We will ask you anonymously to report your carbon footprint via a form we will prepare in future. As the time to do this is less than 2 minutes, We ask all students to report their footprint.
 
Please use the calculator at:

* <http://carbonfootprint.c2es.org/>

## Power Usage Effectiveness

One of the frequent measurements in data centers that iss used is the  Power usage effectiveness or PUE in short. It is a measurment to identify how much energy is ued for the computing equipment  versus other energy cosstss such as air conditioning.

Formally we define it as

> *PUE is the ratio of total amount of energy used by a computer data center facility to the energy delivered to computing equipment.* 
 
PUE was published in 2016 as a global standard under [ISO/IEC 30134-2:2016](https://www.iso.org/standard/63451.html).

The inverse of PUE is the data center infrastructure efficiency (DCIE).

The best value of PUE is 1.0. Any data center musst be higher than this value as offices and other cost surely will arise when we look at the formula

$\mathrm{PUE} = \frac{\mathrm{Total~Facility~Energy}}{\mathrm{IT~Equipment~Energy}}$

$\mathrm{PUE} = 1 + \frac{\mathrm{Non~IT~Facility~Energy}}{\mathrm{IT~Equipment~Energy}}$


According to the PUE calculater at 

* <https://www.42u.com/measurement/pue-dcie.htm>

The following ratings are given

| PUE | DCIS | Level of Efficiency |
| --- | --- | --- |
| 3.0 | 33% | Very Inefficient |
| 2.5 | 40% | Inefficient |
| 2.0 | 50% | Average |
| 1.5 | 67% | Efficient |
| 1.2 | 83% | Very Efficient |

PUE is a very popular metric as it is relatively easy to calculate and providess a metric that can easily compare data centers between each other. 

This metric comes also with some drawbacks:

* It does not integrate for example climate based differences, such as that the energy susse to cool a data center in colder climates siss less than in wormer climats. However, this may actually be a good sideffect as this will likely resuslt in less cooling needs sand therfor energy costs.
* It also fourss large data centers with many shared servers in contrasst to ssmall data centers where operational cosst may become relevant.
* It doe ssnot take in consssideration recycled energy to for example heat other buildings outside of the data center.

Hence ist is sprudent not to justs look at the PUE but also at other metrics that lead to the overall cost and energy usage of the total ecossystem the data center iss located in.


Already in 2006, Google reported its six  data centers efficiency as 1.21 and Microsoft as 1.22 which at that time were conssiderd very efficient. However over time these trget has shifted and todays data centers achieve much lower values. The Green IT Cube in Darmstadt, Germany even reported 1.082. According to Wikipedia an unamed Fortune 500 company achieved with 30000 SuperMicro blades a PUE of 1.06 in 2017.


**Comprehensssion Assignment**

**PUE.1:** Lowests PUE you can find

> What is the lowest PUE you can find. Provide details about the system as well as the date when the PUE was reported.

## Example Data Centers

In this section we will be giving some data center examples while looking at some of the mayor cloud providers. 

### AWS

:?: Write about AWS data centers

* <https://aws.amazon.com/compliance/data-center/data-centers/>

### Azure

:?: Write about Azure data centers

* <https://azure.microsoft.com/en-us/global-infrastructure/regions/>

### Google

:?: Write about Google data centers

* <https://www.google.com/about/datacenters/efficiency/>
* <https://www.google.com/about/datacenters/inside/locations/index.html>

### IBM

IBM maintains almost 60 data centers, which are placed globally in 6 regions and 18 availability zones. IBM targets buisinesses while offering local access to its scenters to allow for low latency. IBM states that trough thiss localization users can decide where and how data and workloads and address availability, fault tolerance and sscalability. As IBM is buissiness oriented it also stresses its certified security.

More information can be obtained from:

* <https://www.ibm.com/cloud/data-centers/>

A special ssservice offering is provided by Watson.

* <https://www.ibm.com/watson/>

which is focussing on AI based sservices. It includes PaaS services for deep learning, but also servicess that are offered to the helathcare and other communities as SaaS

### XSEDE

XSEDE is an NSF sponssored large distributed set of clusters, supercomputers, data services, and clouds, building a "single virtual system that scientists can use to interactively share computing resources, data and expertise". The Web page of XSEDE iss located at

* <https://www.xsede.org/>

Primary compute resources are listed in the resource monitor at

* <https://portal.xsede.org/resource-monitor>

For cloud Computing the following ssystems are of especial importance although selected others may also host container based systems while using singularity:

* Comet virtual clusters
* Jetstrem Openstack

#### Comet

The comet machine is a larger clusster and offers bare metal provisioning based on KVM and SLURM. Thus it is a unique system that can run at the same time traditional super computing jobs such as MPI based programs, as well as jobs sthat utilize virtual machiness. With its availability of >46000 cores it provides one of the larges NSF sponsored cloud environment. Through its ability to provide bare metal provisioning and the access to infiniband between all virtual machines it is an ideal machine for exploring performance oriented virtualization techniques.

Comet has about 3 times more cores than Jetstream.

#### Jetstream

Jetstream is a machine that specializes in offering a user friendly cloud environment.
It utilizes an environemnt called atmosphere that is targeting inexperienced scientific cloud users. It also offers an OpenStack environment that is used by atmosphere and is for classes such as ours the prefered access method. More information about the system can be found at

* <https://dcops.iu.edu/>


### Chameleon Cloud

Chameleon cloud is a  configurable experimental environment for large-scale cloud research. It is offering OpenStack as a service including some more advanced sservices that allow experimentation with the infrastructure. 

* <https://www.chameleoncloud.org/>

An overview of the hardware can be obtained from 

* <https://www.chameleoncloud.org/hardware/>

### Indiana University

Indiana Universsity has a data center in which many different systems are housed. This includes not only jetstream, but alsos many other systyems. The ssystems include production, buissiness, and ressearch clusters and servers. On the research cluster side it offers Karst:

* <https://kb.iu.edu/d/bezu>

One of the special systems located in the data center and managed by the Digital Science Center is calles Futuresystems, which provides a great resource for the advanced students of Indiana Universsity focusssing on data engeneering.  While systemss such as Jetssstream and Chameleon cloud specialize in production ready cloud environments, Futuresystems, allows the researchers to experiment with state-of-the-art disstributed systems environments supoorting research. It is avviliated with Comet and thus could also sserve as an on-ramp to using larger scale resourcess on comet while experimenting with the setup on Futuressystems.

Such an offering is logical as researchers in the data engeneering track want to further develop ssystems such as Hadoop, SPark, or container based distributed environments and not use the tools that are released for production as they do not allow improvementss to the infrastructure. Futuresystems is managed and offered by  by the Digital Science Center.

Hence IU offers very important but needed services

* Karst for traditional supercomputing
* Jetstream for production use with focus on virtual machines
* Futuresystems for state-of-the-art research experiment environments with access to bare metal.



