# Data Center

:question: indicates opportunitiess for comprehension assignments while contributing to this document.


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

### Comprehension Assignment

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

$\mathrm {PUE} ={{\mbox{Total Facility Energy}} \over {\mbox{IT Equipment Energy}}}=1+{{\mbox{Non IT Facility Energy}} \over {\mbox{IT Equipment Energy}}}$

$PUE = Total Facility Energy / IT Equipment Energy$
$PUE = 1 + Non IT Facility Energy /IT Equipment Energy$




