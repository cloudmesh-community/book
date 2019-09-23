# Data Center {#sec:data-center}

---

![](images/learning.png) **Learning Objectives**

* What is a data center.
* What are import metrics.
* What is the difference between a Cloud data center and a traditional
  datacenter.
* What are examples of Cloud data centers.

---

## Motivation: Data

Before we go into more details of a data center we like to motivate why
we need them.  Here we start with looking at the amount of data that
recently got created and provide one of many motivational aspects. Not
all data will or should be stored in data centers. However a
significant amount of data will be in such centers.

### How much data?

One of the issues we have is to comprehend how much data is created. 
It's hard to imagine and put into a perspective how much total data 
is created over a year, a month, a week, a day or even just an hour. 
Instead to easily visualize the amount of data produced we often find 
graphics easier to comprehend that shows how much data was generated in 
a minute. Such depictions usually include examples of data generated as 
a part of popular cloud services or the internet in general.




One such popular depiction is *Data Never Sleeps* (see
@fig:data-never-sleeps). It has been produced a number of times over the
years and is now at version 7.0 released in 2019. If you identify a
newer version, please let us know.

Observations for 2019:  It is worth while to study this image
in detail and identify some of the data that you can relate to of
service you use. It is also a possible indication to study other
services that are mentioned. For the data for 2019 we observe that a
staggering ~4.5Mil google searches are executed every minute which is
slightly lower than the number of videos watched on youtube. 18Mil text
messages are send every minute. Naturally the numbers are averages over
time.

![Data Never Sleeps  [@www-image-data-never-sleeps-7]](images/data-never-sleeps-7.jpg){#fig:data-never-sleeps-7}


In contrast in 2017 we observed: A 3.8Mil google searches are
executed every minute. Surprisingly the weather channel receives over
18Mil forecast requests which is even higher than the 12Mil text
messages send every minute. Youtube certainly serving a significant
number of users by 4.3Mil videos watched every minute. 

![Data Never Sleeps  [@www-image-data-never-sleeps-6]](images/data-never-sleeps-6.png){#fig:data-never-sleeps}

A different source publishes what is happening on the internet in a
minute, but we have been able to locate a version from 2018 (see
@fig:internet-minutes-2018). While some data seems the same, others are
slightly different. For example this graph has a lower count for Google
searches, while the number of text messages send is significantly higher
in contrast to @fig:data-never-sleeps.

![Internet Minute 2018 [@www-internet-minute-2017-2018]](images/internet-minute-2018.jpg){#fig:internet-minutes-2018}

While reviewing the image from last year from the same author, we find
not only increases, but also declines. Looking at facebook showcases a
loss of 73000 logins per minute. This loss is substantial. We can see
that facebook services are replaced by other services that are more
popular with the younger generation who tend to pick up new services
quickly (see @fig:internet-minutes-2017-2018).


![Internet Minute 2017-2018 [@www-internet-minute-2017-2018]](images/internet-minute-2017-2018.jpg){#fig:internet-minutes-2017-2018}


It is also interesting to compare such trends over a longer period of
time (see @fig:google-search-per-year, @fig:big-data-trend-2012). An
example is provided by looking at Google searches

* <http://www.internetlivestats.com/google-search-statistics/>.

and visualized in @fig:google-search-per-year.

![Google searches over time](images/google-search.png){#fig:google-search-per-year}


![Big data trend. 2012 [@www-bigdata-36-month]](images/bd-forbes-trend.png){#fig:big-data-trend-2012}


When looking at the trends, many predict an exponential growth in data.
This trend is continuing.



<!--
![](images/bd-landsscape-2018.png)

**Figure:** Big Data Landscape
-->

## Cloud Data Centers

A *data center* is a facility that hosts the information technology
related to servers and data serving a large number of customers. data
centers evolved from the need to originally have large rooms as the
original computers filled in the early days of the compute revolution
filled rooms. Once multiple computers were added to such facilities
super computer centers created for research purposes. With the
introduction of the internet and offering services such as Web
hosting large business oriented server rooms were created. The need
for increased facilities was even accelerated by the development of
virtualization and servers being rented to customers in shared
facilities. As the need of web hosting still is important but has
been taken over by cloud data centers, the terms internet data center,
and cloud data center are no longer used to distinguish it. Instead we
use today just the term *data center*. There may be still an important
difference between research data centers offered in academia and
industry that focus on providing computationally potent clusters focus
on numerical computation. Such data centers are typically centered
around the governance around a smaller number of users that are either
part of an organization or a virtual organization. However, we see
that even in the research community data centers not only host
supercomputers, but also Web server infrastructure and these days even
private clouds that support the organizational users. In case of the
latter we speak about supporting the *long tail about science*.

The latter is driven by the 80%-20% rule. E.g. 20% of the users use 80%
of the compute power. This means that the top 20% of scientists are
served by the leadership class super computers in the nation, while
the rest are either served by other servers, cloud offerings through
research and public clouds.


## Data Center Infrastructure

Due to the data and the server needs in the cloud and in research such
data centers may look very different. Some focus on large scale
computational resources, some on commodity hardware offered to the
community. The size of them is also very different. While a
supercomputing center as part of a university was one of the largest
such data centers two decades ago, they dwarf the centers now deployed
by industry to serve the long tail of customers.

In general a data center will have the following components:

* Facility: the entire data center will be hosted in a building.  The
  building may have specific requirements related to security,
  environmental concerns, or even the integration into the local
  community with for example providing heat to surrounding residences.

* Support infrastructure: This building will include a significant
  number of support infrastructure that addresses for example
  continuous power supply, air conditioning, and security For this
  reason you find in such centers

  * Uninterruptible Power Sources (UPS)
  * Environmental Control Units
  * Physical Security Systems

* Information Technology Equipment: Naturally the facility will host
  the IT equipment including the following:

  * Servers
  * Network Services
  * Disks
  * Data Backup Services

* Operations staff: The facility will need to be staffed with the
  various groups that support such data centers. It includes

  * IT Staff
  * Security and Facility Staff
  * Support Infrastructure Staff

  With regards to the number of people serving such a facility it is
  obvious that through automation is quite low. According to
  [@www-datacenter-staffing] proper data center staffing is a key to a
  reliable operation (see @fig:datacenter-staff-impact).

  According to @fig:datacenter-staff-impact
  operational sustainability contains three elements of operational
  sustainability, namely  management and operations, building
  characteristics, and site location [@www-datacenter-staffing].

![Datacenter Staff Impact [@www-datacenter-staffing]](images/datacenter-staff-impact.jpg){#fig:datacenter-staff-impact}

Another interesting observation is the root cause of incidents in a
data center. Everyone has probably experienced some outage, so it is
important to identify where they come from in order to prevent them.
As we see in @fig:datacenter-outage not every error is caused by an
operational issue. External, installation, design, and manufacturer
issues are together the largest issue for datacenter incidents (see
@fig:datacenter-outage). Figure Outage. According to the Uptime
Institute Abnormal Incident Reports (AIRs) database, the root cause of
39% of data center incidents falls into the operational area
[@www-datacenter-staffing].


![Datacenter outage [@www-datacenter-staffing]](images/datacenter-outage.jpg){#fig:datacenter-outage}



## Data Center Characteristics

Next we identify a number of characteristics when looking at different
data centers.

* **Variation in Size**: Data centers range in size from small *edge*
 facilities to megascale or hyperscale filling large ware houses.

* **Variation in cost per server**: Although many data centers
  standardize their components, specialized services may be offered not on
  a 1K server, but on a 50K server.

* **Variation in Infrastructure:** Servers in centers serve a variation
  of needs and motivate different infrastructure: Use cases, Web
  Server, E-mail, Machine Learning, Pleasantly Parallel problem,
  traditional super computing jobs.

* **Energy Cost:** Data centers use a lot of energy. The energy cost
  varies per region.  A motivation to reduce energy use and cost is also
  been trended by environmental awareness, not only by the operators,
  but by the community in which such centers operate.

* **Reliability:** Although through operational efforts the data center
  can be made more reliable, failure still can happen. Examples are

* <https://www.zdnet.com/article/microsoft-south-central-u-s-datacenter-outage-takes-down-a-number-of-cloud-services/>
* <https://www.datacenterknowledge.com/archives/2011/08/07/lightning-in-dublin-knocks-amazon-microsoft-data-centers-offline>
* <https://techcrunch.com/2012/10/29/hurricane-sandy-attacks-the-web-gawker-buzzfeed-and-huffington-post-are-down/>

Hence Data Center IaaS advantages include

* Reduced operational cost
* Increased reliability
* Increased scalability
* Increased flexibility
* Increased support
* Rapid deployment
* Decrease management: Outsourcing expertise that is not related to
  core business

Datacenter disadvantages include

* Loss of control of the HW
* Loss of control of the data
* Model is preferring many users
* Software to control infrastructure is not accessible
* Variations in performance due to sharing
* Integration requires effort beyond login
* Failures can have a humongous impact


## Data Center Metrics

One of the most important factor to ensure smooth operation and
offering of services is to employ metrics that will be able to provide
significant impacting the operations. Having metrics allows the staff
to monitor and adapt to dynamic situations but also to plan
operations.

### Data Center Energy Costs

One of the easiest to monitor metrics for a datacenter is the cost
of energy used to operate all of the equipment. Energy is one of
the largest costs a datacenter incurs during its operation as all of
the servers, networking, and cooling equipment require power 24/7. For
electricity, billing is usually measured in terms of kilowatt hours
(kWh) and kilowatts (kW). Depending on circumstances, there may also be
costs for public purpose programs, cost recovery, and stranded costs, but
they are beyond the scope of this book.

To provide a quick understanding, it is best to understand the relation
between kilowatt hours and kilowatts. kWh is typically referred to as
consumption while kW is referred to as demand and it's important to
understand how these two concepts relate to each other. The easiest
analogy to describe the relationship is to think of kilowatts (demand)
as the size of a water pipe while kilowatt-hours (consumption) is how
much water has passed through the pipe. If a server requires 1.2 kW to
operate then, after an hour has passed, it will have consumed 1.2 kWh.
However, if the server operates at 1.2 kW for 30 minutes and then goes
idle and drops to 0.3 kW for another 30 minutes, then total power
consumed will be:

$$kWh=0.3*30/60+1.2*30/60=0.75$${#eq:Energy-Calculation}

Energy costs for a datacenter, then, are composed of two things:
charges for energy and charges for demand. Energy is the amount of total
energy consumed by the datacenter and will be the total kWh multiplied
by the cost per kWh. Demand is somewhat more complicated: it is the
highest total consumption measured in a 15 minute period. Taking the
previous example, if a datacenter has 1,000 servers, the total energy
consumption would be 750 kWh in the hour, but the demand charge would be
based off of 1,200 kW (or 1.2 MW).

The costs, then, are how the utility company recoups its expenses: the
charge per kWh is it recouping the generation cost while the kW charge
is recouping the cost of transmission and distribution (T&D). Typically,
the demand charge is much higher and will depend on utility constraints -
if a utility is challenged on the T&D front, expect these costs to be over
$6-$10/kW. If the assumed cost-per-kWh is $0.12 and cost-per-kW is $8,
the cost to run our servers for a month would be:

$$kWh=0.75*24*30*0.12*1000=64,800$${#eq:kWh-Cost-Calculation}
$$kW=1.2*8*1000=9,600$${#eq:kW-Cost-Calculation}

This would total to $74,400. It's important to note that fixing demand
charges can have a tremendous payback: had the servers simply consumed
750 kW over the course of the hour, then our demand charges would've
been halved to $4,800 while the energy costs remained the same. This is
also why server virtualization can have a positive impact on energy costs:
by having fewer servers running at a higher utilization, the demand charge
will tend to level itself out as, on average, each server will be more
fully utilized. For example, it's better to pay for 500 servers at
100% utilization than 1000 servers at 50% utilization even though the amount
of work done is the same since, if the 1,000 servers momentarily all operate
at 100% utilization for even a brief amount of time in a month, the demand
charge for the datacenter will be much higher.

### Data Center Carbon Footprint

Scientists world wide have identified a link between carbon emission
and global warming. As the energy consumption of a data center is
substantial, it is prudent to estimate the overall carbon emission.
Schneider Electric (formerly APC) has provided a report on how to
estimate the Carbon footprint of a data center [@schneider-footprint].
Although this report is already a bit older, it provides still
valuable information. It defines key terms such as

Carbon dioxide emissions coefficient (*carbon footprint*):

* With the increasing demand of data, bandwidth and high performance
  systems, there is substantial amount of power consumption. This
  leads to high amount of greenhouses gases emission into the
  atmosphere, released due to any kind of basic activities like driving
  a vehicle or running a power plant.

  > "The measurement includes power generation plus transmission and
  > distribution losses incurred during delivery of the electricity to
  > its point of use."

   Data centers in total used 91 billion kilowatt-hours (kWh) of
   electrical energy in 2013, and they will use 139 billion kWh by
   2020. Currently, data centers consume up to 3 percent of all
   global electricity production while producing 200 million metric tons
   of carbon dioxide. Since world is moving towards cloud, causing more
   and more data center capacity leading more to power consumption.

Peaker plant:

* Peaking power plants, also known as peaker plants, and
  occasionally just *peakers*, are power plants that generally run
  only when there is a high demand, known as peak demand, for
  electricity. Because they supply power only occasionally, the power
  supplied commands a much higher price per kilowatt hour than base
  load power. Peak load power plants are dispatched in combination
  with base load power plants, which supply a dependable and
  consistent amount of electricity, to meet the minimum demand.
  These plants are generally coal-fired which causes a huge amount
  of CO2 emissions. A peaker plant may operate many hours a day, or
  it may operate only a few hours per year, depending on the
  condition of the region's electrical grid. Because of the cost of
  building an efficient power plant, if a peaker plant is only going
  to be run for a short or highly variable time, it does not make
  economic sense to make it as efficient as a base load power plant.
  In addition, the equipment and fuels used in base load plants are
  often unsuitable for use in peaker plants because the fluctuating
  conditions would severely strain the equipment. For these reasons,
  nuclear, geothermal, waste-to-energy, coal and biomass are rarely,
  if ever, operated as peaker plants.

Avoided emissions:

* Emissions avoidance is the most effective carbon management
  strategy over a multi-decadal timescale to achieve atmospheric CO2
  stabilization and a subsequent decline. This prevents, in the first
  place, stable underground carbon deposits from entering either the
  atmosphere or less stable carbon pools on land and in the oceans.

  Carbon offsets based on energy efficiency rely on technical
  efficiencies to reduce energy consumption and therefore reduce CO2
  emissions. Such improvements are often achieved by introducing more
  energy efficient lightening, cooking, heating and cooling systems.
  These are real emission reduction strategies and have created valid
  offset projects.

  This type of carbon offset provides perhaps the simplest options
  that will ease the adoption of low carbon practice. When these practices
  become generally accepted (or compulsory), they will no longer qualify
  as offsets and further efficiencies will need to be promoted.

CO2 (carbon dioxide, or *carbon*):

* Carbon dioxide is the main cause of the greenhouse effect, it is
  emitted in huge amount into our atmosphere with a life cycle of
  almost 100 years. Data centers emit during the manufacturing process
  of all the components that populate a data center (servers, UPS,
  building shell, cooling, etc.) and during operation of data centers
  (in terms of electricity consumed), the maintenance of the data
  centers (i.e. replacement of consumables like batteries, capacitors,
  etc.), and the disposal of the components of the data centers at the
  end of the lifecycle. Until now, power plants have been allowed to
  dump unlimited amounts of carbon pollution into the atmosphere - no
  rules were in effect that limited their emissions of carbon dioxide,
  the primary driver of global warming. Now, for the first time, the EPA
  has finalized new rules, or standards, that will reduce carbon
  emissions from power plants. Known as the Clean Power Plan, these
  historic standards represent the most significant opportunity in years
  to help curb the growing consequences of climate change.

The data center will have a total carbon profile, that includes the
many different aspects of a data center contributing to carbon
emissions. This includes manufacturing, packaging, transportation,
storage, operation of the data center, and decommissioning. Thus it is
important to notice that we not only need to consider the operation
but also the construction and decommission phases.

### Data Center Operational Impact {#sec:operation-impact}

One of the main operational impacts is the cost and emissions of a
data center cause by running, and cooling the servers in the data
center. Naturally this is dependent on the type of fuel that is used
to produce the energy. The actual carbon impact using electricity
certainly depends on the type of powerplant that is used to provide
it. These energy costs and distribution of where the energy comes from
can often be looked up by geographical regions on the internet or form
the local energy provider. Municipal government organizations may also
have such information. Tools such as the [Indiana State Profile and
Energy Use](https://www.eia.gov/state/?sid=IN) [@www-indiana-eia].

may provide valuable information to derive such estimates. Correlating
a data center with cheap energy is a key factor. To estimate both
costs in terms of price and carbon emission Schneider provides a
convenient Carbon estimate calculator based on energy consumption.

* <https://www.schneider-electric.com/en/work/solutions/system/s1/data-center-and-network-systems/trade-off-tools/data-center-carbon-footprint-comparison-calculator/tool.html>
* <http://it-resource.schneider-electric.com/digital-tools/calculator-data-center-carbon>

If we calculate the total cost, we need naturally add all costs
arising from build and teardown phase as well as operational upgrades.

### Power Usage Effectiveness

One of the frequent measurements in data centers that is used is the
Power usage effectiveness or PUE in short. It is a measurement to
identify how much energy is ued for the computing equipment versus
other energy costs such as air conditioning.

Formally we define it as

> *PUE is the ratio of total amount of energy used by a computer data
> center facility to the energy delivered to computing equipment.*

PUE was published in 2016 as a global standard under
[ISO/IEC 30134-2:2016](https://www.iso.org/standard/63451.html).

The inverse of PUE is the data center infrastructure efficiency (DCIE).

The best value of PUE is 1.0. Any data center must be higher than
this value as offices and other cost surely will arise when we look at
the formula

$\mathrm{PUE} = \frac{\mathrm{Total~Facility~Energy}}{\mathrm{IT~Equipment~Energy}}$

$\mathrm{PUE} = 1 + \frac{\mathrm{Non~IT~Facility~Energy}}{\mathrm{IT~Equipment~Energy}}$


According to the PUE calculator at

* <https://www.42u.com/measurement/pue-dcie.htm>

The following ratings are given

| PUE | DCIS | Level of Efficiency |
| --- | --- | --- |
| 3.0 | 33% | Very Inefficient |
| 2.5 | 40% | Inefficient |
| 2.0 | 50% | Average |
| 1.5 | 67% | Efficient |
| 1.2 | 83% | Very Efficient |

PUE is a very popular metric as it is relatively easy to calculate and
provides a metric that can easily compare data centers between each
other.

This metric comes also with some drawbacks:

* It does not integrate for example climate based differences, such as
  that the energy use to cool a data center in colder climates is
  less than in warmer climates. However, this may actually be a good
  side-effect as this will likely result in less cooling needs sand
  therefor energy costs.
* It also forces large data centers with many shared servers in
  contrast to small data centers where operational cost may become
  relevant.
* It does not take in consideration recycled energy to for example
  heat other buildings outside of the data center.

Hence it is prudent not to just look at the PUE but also at other
metrics that lead to the overall cost and energy usage of the total
ecosystem the data center is located in.


Already in 2006, Google reported its six data centers efficiency as
1.21 and Microsoft as 1.22 which at that time were considered very
efficient. However over time these target has shifted and today's data
centers achieve much lower values. The Green IT Cube in Darmstadt,
Germany even reported 1.082. According to Wikipedia an unnamed Fortune
500 company achieved with 30000 SuperMicro blades a PUE of 1.06 in
2017.


**Exercises**

**E.PUE.1:** Lowest PUE you can find

> What is the lowest PUE you can find.
> Provide details about the system as well as
> the date when the PUE was reported.

### Hot-Cold Aisle

To understand hot-cold aisles, one must take a brief foray into the
realm of physics and energy. Specifically, understanding how a
temperature gradient tries to equalize. The most important formula
to know is the heat transfer @eq:heat-transfer.

$$q=h_{c}A(t_{a}-t_{s})$${#eq:heat-transfer}

Here, *q* is the amount of heat transferred for a given amount of time.
For this example, we will calculate it as W/hour as that is, conveniently,
how energy is billed. Air moving at a moderate speed will transfer
approximately 8.47 Watts per Square Foot per Hour. A 1U server is
19 inches wide and about 34 inches deep. Multiplying the two values gives us
a cross section of 646 square inches, or 4.48 square feet. Plugging these values
into our @eq:heat-transfer us:

$$q=8.47*4.48*(t_{a}-t_{s}))$${#eq:heat-transfer-example}

This begins to point us towards why hot-cold aisles are important. If
we introduce cold air from the AC system into the same aisle that the
servers are exhausting into, the air will mix and begin to average
out. For example, if our servers are producing exhaust at 100F and our
AC unit provides 65F at the same rate, then the average air
temperature will become 82.5F (assuming balanced air pressure). This
has a deleterious effect on our server cooling - warmer air takes heat
away from warmer surfaces slower than cooler air:

$$1,328.2=8.47*4.48*(100-65)$$

$$664.0=8.47*4.48*(100-82.5))$$

From the previous listing, we can see that a 35 degree delta allows
the center to dissipate 1,300 Watts of waste heat from a 1U server
while a 17.5 degree delta allows us to only dissipate 664 Watts of
energy. If a server is consuming more than 664 Watts, it'll continue
to get warmer and warmer until it eventually reaches a temperature
differential high enough to create an equilibrium (or reaches a
thermal throttle and begins to reduce performance).

To combat this, engineers developed the idea of designating
alternating aisles as either hot or cold. All servers in a given aisle
are then oriented such that the AC system provides cool air into the
cold aisle where it is drawn in by the server which then exhausts it
into the hot aisle where the ventilation system removes it from the
room. This has the benefit of maximizing the temperature delta between
the provided air and the server's processor(s), reducing the amount of
quantity of air that must be provided in order to cool the server and
improving overall system efficiency.

See @fig:hot-cold-isle to understand how the hot-cold isle configuration is
setup in a data center.

![Hot Cold Isle [@hot-cold-isle]](images/hot-cold-isle.jpg){#fig:hot-cold-isle}

#### Containment

While modern data centers employ highly sophisticated mechanisms to be as
energy efficient as possible. One such mechanism which can be seen as a
improvement on top of the Hot-Cold isle arrange is to use either hot isle
containment or cold isle containment. Using a containment system can remove the
issue with free flowing air.

As the name somewhat implies in cold air containment, the data centers is
designed so that only cold air goes into the cold isle, this makes sure that
the system only draws in cold air for cooling purposes. Conversely in hot isle
containment design, the hot isle is contained so that the hot air collected
in the hot isle is drawn out by the cooling system and so that the cold air
does not flow into the hot isles[@hot-cold-containment].

##### Water Cooled Doors {#sec:datacenter-doors}

Another good way of reducing the energy consumption is to install water
cooled doors directly at he rack as shown in @fig:watercooleddoor.
Cooling even can be actively controlled so that in case of idle servers
less energy is spend to conduct the cooling. There are many vendors that
provide such cooling solutions.


![Active Rear Door [link](https://www.mainlinecomputer.com/t/product-lines/cabinets-and-racks/rear-door-heat-exchangers/chilled-doorr-high-density-rack-cooling-system/)](images/active-rear-door-rack-cooling-system-high.jpg){#fig:watercooleddoor}




### Workload Monitoring

#### Workload of HPC in the Cloud

Clouds and especially university data centers do not just provide
virtual machines but provide traditional super computer services. This
includes the NSF sponsored XSEDE project. As part of this project the
"XDMoD auditing tool provides, for the first time, a comprehensive
tool to measure both utilization and performance of high-end
cyberinfrastructure (CI), with initial focus on XSEDE. Several case
studies have shown its utility for providing important metrics
regarding resource utilization and performance of TeraGrid/XSEDE that
can be used for detailed analysis and planning as well as improving
operational efficiency and performance. Measuring the utilization of
high-end cyberinfrastructure such as XSEDE helps provide a detailed
understanding of how a given CI resource is being utilized and can
lead to improved performance of the resource in terms of job
throughput or any number of desired job characteristics.

Detailed historical analysis of XSEDE usage data using XDMoD clearly
demonstrates the tremendous growth in the number of users, overall
usage, and scale" [@las-xdmod].

Having access to a detailed metrics analysis allows users and center
administrators, as well as project managers to better evaluate the use
and utilization of such large facilities justifying their existence (see @fig:datacenter-xdmod)


![XDMod: XSEDE Metrics on Demand](images/datacenter-xdmod.png){#fig:datacenter-xdmod}

Additional information is available at

* <https://open.xdmod.org/7.5/index.html>

#### Scientific Impact Metric

Gregor von Laszewski and Fugang Wang are providing a scientific impact
metric to XDMoD and XSEDE. It is a framework that (a) integrates
publication and citation data retrieval, (b) allows scientific impact
metrics generation at different aggregation levels, and (c) provides
correlation analysis of impact metrics based on publication and
citation data with resource allocation for a computing facility. This
framework is used to conduct a scientific impact metrics evaluation of
XSEDE, and to carry out extensive statistical analysis correlating
XSEDE allocation size to the impact metrics aggregated by project and
Field of Science. This analysis not only helps to provide an
indication of XSEDE’S scientific impact, but also provides insight
regarding maximizing the return on investment in terms of allocation
by taking into account Field of Science or project based impact
metrics. The findings from this analysis can be utilized by the XSEDE
resource allocation committee to help assess and identify projects
with higher scientific impact. Through the general applicability of
the novel metrics we invented, it can also help provide metrics
regarding the return on investment for XSEDE resources, or campus
based HPC centers [@las-impact].


#### Clouds and Virtual Machine Monitoring

Although no longer in operation in its original form
[FutureGrid](http://archive.futuregrid.org/metrics/html/results/2014-Q3/reports/rst/india-All.html) [@www-fg-metrics]
has pioneered the extensive monitoring and publication of its virtual
machine and project usage. We are not aware of a current system that
provides this level of detail as sof yet. However, efforts as part of
XSEDE within the XDMoD project are under way at this time but are not
integrated.

Futuregrid provided access to all virtual machine information, as well
as usage across projects. An archived portal view is available at
[FutureGrid Cloud Metrics](http://archive.futuregrid.org/metrics/html/results/2014-Q3/reports/rst/india-All.html)
[@www-fg-metrics].

![FutureGrid Cloud Metric](images/datacenter-fg-metric.png){#fig:datacenter-fg-metric}

Futuregrid offered multiple clouds including clouds based on
OpenStack, Eucalyptus, and Nimbus. Nimbus and Eucalyptus are systems
that are no longer used in the community. Only OpenStack is the only
viable solution in addition to the cloud offerings by Comet that do
not uses OpenStack (see @fig:datacenter-fg-metric).

Futuregrid, could monitor all of them and published its result in its
Metrics portal. Monitoring the VMs is an important activity as they
can identify VMs that may no longer be used (the user has forgotten to
terminate them) or too much usage of a user or project can be detected
in early stages.

We like to emphasize several examples where such monitoring is helpful:

* Assume a student participates in a class, metrics and logs allow to
  identify students that do not use the system as asked for by the
  instructors. For example it is easy to identify if they logged on and
  used VMs. Furthermore the length of running a VM ba
* Let us assume a user with willful ignorance does not
  shut down VMs although they are not used because research clouds are
  offered to us for free. In fact, this situation happened to us
  recently while using another cloud and such monitoring capacities were
  not available to us (on jetstream). The user single-handedly used up
  the entire allocation that was supposed to be shared with 30 other
  users in the same project. All accounts of all users were quasi
  deactivated as the entire project they belonged to were deactivated.
  Due to allocation review processes it took about 3 weeks to reactivate
  full access. sed on the tasks to be completed can be compared
  against other student members.
* In commercial clouds you will be charged money. Therefore, it is
  less likely that you forget to shutdown your machine
* In case you use GitHub carelessly and post your cloud passwords or
  any other passwords in it, you will find that within five minutes your
  cloud account will be compromised. There are individuals on the
  network that cleverly mine GitHub for such security lapses and will
  use your password if you indeed have stored them in it. In fact
  GitHub's deletion of a file does not delete the history, so as a non
  expert deleting the password form GitHub is not sufficient. You will
  have to either delete and rewrite the history, but definitely in this
  case you will need to reset the password. Monitoring the public cloud
  usage in the data center is important not only in your region but
  other regions as the password is valid also there and intruders could
  hijack and start services in regions that you have never used.

In addition to FutureGrid, we like to point out Comet (see other
sections). It contains an exception for VM monitoring as it uses a
regular batch queuing system to manage the jobs. Monitoring of the
jobs is conducted through existing HPC tools.

#### Workload of Containers

Monitoring tools for containers such as for kubernetes are listed at:

* <https://kubernetes.io/docs/tasks/debug-application-cluster/resource-usage-monitoring/>

Such tools can be deployed alongside kubernetes in the data center,
but will likely have restrictions to its access. They are for those
who operate such services for example in kubernetes. We will discuss
this in future sections in more detail.

## Example Data Centers

In this section we will be giving some data center examples while
looking at some of the mayor cloud providers.

### AWS

AWS focuses on security aspects of their data centers that include
four aspects [@www-aws-datacenters]:

* [Perimeter Layer](https://aws.amazon.com/compliance/data-center/perimeter-layer/)
* [Infrastructure Layer](https://aws.amazon.com/compliance/data-center/infrastructure-layer/)
* [Data Layer](https://aws.amazon.com/compliance/data-center/data-layer/)
* [Environmental Layer](https://aws.amazon.com/compliance/data-center/environmental-layer/)

The [global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
[@www-aws-infrastructure] as of January 2019 includes 60 Availability
Zones within 20 geographic Regions. Plans exists to add 12
Availability Zones and four additional Regions in Bahrain, Hong Kong
SAR, Sweden, and a second AWS GovCloud Region in the US (see
@fig:datacenter-aws-region).

![AWS regions [@www-aws-infrastructure]](images/datacenter-aws-region.png){#fig:datacenter-aws-region}

Amazon strives to achieve high availability through multiple
availability zones, improved continuity with replication between
regions, meeting compliance and data residency requirements as well as
providing geographic expansion. See @fig:datacenter-azure-region

The regions and number of availability zones are as follows:

* Region US East: N. Virginia (6), Ohio (3) US West N. California (3),
  Oregon (3)
* Region: Asia Pacific Mumbai (2), Seoul (2), Singapore (3), Sydney
  (3), Tokyo (4), Osaka-Local (1)1 Canada Central (2) China Beijing (2),
  Ningxia (3)
* Region: Europe Frankfurt (3), Ireland (3), London (3), Paris (3)
  South America São Paulo (3)
* Region Gov Cloud: AWS GovCloud (US-West) (3)
* New Region (coming soon): Bahrain, Hong Kong SAR, China, Sweden, AWS
  GovCloud (US-East)

### Azure

Azure claims to have more global
[regions](https://azure.microsoft.com/en-us/global-infrastructure/regions/)
[@www-azure-regions] than any other cloud provider. They motivate this
by their advertisement to bring and applications to the users around
the world. The goal is similar as other commercial hyprescale
providers by introducing preserving data residency, and offering
comprehensive compliance and resilience. As of Aug 29, 2018 Azure
supports 54 regions worldwide. These regions can currently be accessed
by users in 140 countries (see @fig:datacenter-azure-region). Not
every service is offered in every region as the service to region
matrix shows:

* <https://azure.microsoft.com/en-us/global-infrastructure/services/>


![Azure regions [@www-azure-regions]](images/datacenter-azure-region.png){#fig:datacenter-azure-region}


### Google


From
[Google](https://www.google.com/about/datacenters/inside/locations/index.html) [@www-google-locations]
we find that on Aug. 29th Google has the following data center
locations (see @fig:datacenters-google):

* **North America:** Berkeley County, South Carolina; Council Bluffs,
  Iowa; Douglas County, Georgia; Jackson County, Alabama; Lenoir, North
  Carolina; Mayes County, Oklahoma; Montgomery County, Tennessee; The
  Dalles, Oregon
* **South America:** Quilicura, Chile
* **Asia:** Changhua County, Taiwan; Singapore
* **Europe:** Dublin, Ireland; Eemshaven, Netherlands; Hamina, Finland;
  St Ghislain, Belgium


![Google data centers [@www-google-locations]](images/datacenters-google.png){#fig:datacenters-google}

Each data center is advertised with a special environmental impact
such as a unique cooling system, or wildlife on premise. Google's data
centers support its service infrastructure and allow hosting as well
as other cloud services to be offered to it's customers.

Google highlights its efficiency strategy and methods here:

* <https://www.google.com/about/datacenters/efficiency/>

They summarize their offers are based on

* Measuring the PUE
* Managing airflow
* Adjusting the temperature
* Use free Cooling
* Optimizing the power distribution


![PUE data for all large-scale Google data centers](images/datacenter-google-pue.png){#fig:datacenter-google-pue}

The
[PUE](https://www.google.com/about/datacenters/efficiency/internal/) [@www-google-eficiency]
data for all large-scale Google data centers is shown in
@fig:datacenter-google-pue


An important lesson from Google is the PUE boundary. That is the
different efficiency based on the closeness of the IT infrastructure
to the actual data center building. This indicates that it is
important to take at any providers definition of PUE in order not to
report numbers that are not comparable between other vendors and are
all encompassing.

![Google data center PUE measurement boundaries [@www-google-eficiency]](images/datacenter-google-boundary.png){#fig:datacenter-google-boundary}

@fig:datacenter-google-boundary shows the Google data center PUE
measurement boundaries. The
[average PUE](https://www.google.com/about/datacenters/efficiency/internal/) [@www-google-eficiency]
for all Google data centers is 1.12, although we could boast a PUE as
low as 1.06 when using narrower boundaries.

 As a consequence, Google is defining its PUE in detail in @eq:pue-google.

$$PUE=\frac{ESIS + EITS + ETX + EHV + ELV + EF}{EITS - ECRAC - EUPS - ELV + ENet1} $${#eq:pue-google}

where the abbreviations stand for

* ESIS = Energy consumption for supporting infrastructure power
  substations feeding the cooling plant, lighting, office space, and
  some network equipment
* EITS = Energy consumption for IT power substations feeding servers,
  network, storage, and computer room air conditioners (CRACs)
* ETX = Medium and high voltage transformer losses
* EHV = High voltage cable losses
* ELV = Low voltage cable losses
* EF = Energy consumption from on-site fuels including natural gas &
  fuel oils
* ECRAC = CRAC energy consumption
* EUPS = Energy loss at uninterruptible power supplies (UPSes) which
  feed servers, network, and storage equipment
* ENet1 = Network room energy fed from type 1 unit substitution

For more
[details](https://www.google.com/about/datacenters/efficiency/internal/)
see [@www-google-eficiency].


### IBM

IBM maintains almost 60 data centers, which are placed globally in 6
regions and 18 availability zones. IBM targets businesses while
offering local access to its centers to allow for low latency. IBM
states that trough this localization users can decide where and how
data and workloads and address availability, fault tolerance and
scalability. As IBM is business oriented it also stresses its
certified security.

More information can be obtained from:

* <https://www.ibm.com/cloud/data-centers/>

A special service offering is provided by Watson.

* <https://www.ibm.com/watson/>

which is focusing on AI based services. It includes PaaS services for
deep learning, but also services that are offered to the healthcare
and other communities as SaaS

### XSEDE

XSEDE is an NSF sponsored large distributed set of clusters,
supercomputers, data services, and clouds, building a "single virtual
system that scientists can use to interactively share computing
resources, data and expertise". The Web page of XSEDE is located at

* <https://www.xsede.org/>

Primary compute resources are listed in the resource monitor at

* <https://portal.xsede.org/resource-monitor>

For cloud Computing the following systems are of especial importance
although selected others may also host container based systems while
using singularity (see @fig:datacenter-xsede):

* Comet virtual clusters
* Jetstream OpenStack

![XSEDE distributed resource infrastructure](images/datacenter-xsede.jpg){#fig:datacenter-xsede}

#### Comet

The comet machine is a larger cluster and offers bare metal
provisioning based on KVM and SLURM. Thus it is a unique system that
can run at the same time traditional super computing jobs such as MPI
based programs, as well as jobs that utilize virtual machines. With
its availability of >46000 cores it provides one of the larges NSF
sponsored cloud environment. Through its ability to provide bare metal
provisioning and the access to infiniband between all virtual machines
it is an ideal machine for exploring performance oriented
virtualization techniques.

Comet has about 3 times more cores than Jetstream.

#### Jetstream

Jetstream is a machine that specializes in offering a user friendly
cloud environment. It utilizes an environment called atmosphere that
is targeting inexperienced scientific cloud users. It also offers an
OpenStack environment that is used by atmosphere and is for classes
such as ours the preferred access method. More information about the
system can be found at

* <https://dcops.iu.edu/>


### Chameleon Cloud

Chameleon cloud is a configurable experimental environment for
large-scale cloud research. It is offering OpenStack as a service
including some more advanced services that allow experimentation with
the infrastructure.

* <https://www.chameleoncloud.org/>

An overview of the hardware can be obtained from

* <https://www.chameleoncloud.org/hardware/>

### Indiana University

Indiana University has a data center in which many different systems
are housed. This includes not only jetstream, but also many other
systems. The systems include production, business, and research
clusters and servers. See @fig:datacenter-iu

![IU Data Center](images/datacenter-iu.jpg){#fig:datacenter-iu}

On the research cluster side it offers Karst and Carbonate:

* <https://kb.iu.edu/d/bezu> (Karst)
* <https://kb.iu.edu/d/aolp> (Carbonate)

One of the special systems located in the data center and managed by
the Digital Science Center is called Futuresystems, which provides a
great resource for the advanced students of Indiana University
focusing on data engineering. While systems such as Jetstream and
Chameleon cloud specialize in production ready cloud environments,
Futuresystems, allows the researchers to experiment with
state-of-the-art distributed systems environments supporting research.
It is available with Comet and thus could also serve as an on-ramp to
using larger scale resources on comet while experimenting with the
setup on Futuresystems.

Such an offering is logical as researchers in the data engineering
track want to further develop systems such as Hadoop, SPark, or
container based distributed environments and not use the tools that
are released for production as they do not allow improvements to the
infrastructure. Futuresystems is managed and offered by by the Digital
Science Center.

Hence IU offers very important but needed services

* Karst for traditional supercomputing
* Jetstream for production use with focus on virtual machines
* Futuresystems for research experiment environments
  with access to bare metal.

### Shipping Containers

A few years ago data centers build from shipping containers were very
popular. This includes several main Cloud providers. Such providers
have found that they are not the best way to develop centers at scale.
This includes
[Microsoft](https://www.datacenterknowledge.com/archives/2016/04/20/microsoft-moves-away-from-data-center-containers)
and
[Google](https://blogs.technet.microsoft.com/msdatacenters/2013/04/22/microsofts-itpac-a-perfect-fit-for-off-the-grid-computing-capacity/)
The current trend however is to build mega or hyperscale data centers.

## Server Consolidation

One of the driving factors in cloud computing and the rise of large
scale data centers is the ability to use server virtualization to
place more than one server on the same hardware. Formerly the services
were hosted on their own servers. Today they are managed on the sae
hardware although they look to the customer like separate servers.

As a result we find the following advantages:

* **reduction of administrative and operations cost:** While we reduce
  the number of servers and utilize hardware to host multiple on them
  management cost, space, power, and maintenance cost are reduced.

* **better resource utilization:** Through load balancing strategies
  servers can be better utilized while for example increase load so
  resource idling is avoided.

* **increased reliability:** As virtualized servers can be
  snapshotted, and mirrored, these features can be utilized in
  strategies to increase reliability in case of failure.

* **standardization:** As the servers are deployed in large scale, the
  infrastructure is implicitly standardized based on server, network,
  and disk, making maintenance and replacements easier. This also
  includes the software that is running on such servers (OS, platform
  and may even include applications).

## Data Center Improvements and Consolidation

Due to the immense number of servers in data centers, as well as the
increased workload on its servers, the energy consumption of data
centers is large not only to run the servers, but to provide the
necessary cooling. Thus it is important to revisit the impact such
data centers have on the energy consumption. One of the studies that
looked into this is from 2016 and is published by
[LBNL](https://cloudfront.escholarship.org/dist/prd/content/qt84p772fc/qt84p772fc.pdf)
[@lbl-energy-usage] In this study the data center electricity
consumption back to 2000 is analyzed while using previous studies and
historical shipment data. A forecast is with different assumption is
contrasts till 2020

Figure Energy Forecast depicts "an estimate of total U.S.  data center
electricity use (servers, storage, network equipment, and
infrastructure) from 2000-2020" (see @fig:datacenter-energy-use).

While in "2014 the data centers in the U.S. consumed an estimated 70
billion kWh" or "about 1.8% of total U.S. electricity consumption".
However, more recent studies find an increase by about 4% from
2010-2014.  This contrasts a large derivation from the 24% that were
originally predicted several years ago. The study finds that the
predicted energy use would be approximately 73 billion kWh in 2020.

![Energy Forecast [@lbl-energy-usage]](images/datacenter-energy-use.png){#fig:datacenter-energy-use}


It is clear that the original prediction of large energy consumption
motivated a trend in industry to provide more energy efficient data
centers. However if such energy efficiency efforts would not be
conducted or encouraged we would see a completely different scenario.

The scenarios are identified  that will significantly impact the prediction:

* **improved management** increases energy-efficiency through
  operational or technological changes with minimal
  investment. Strategies include improving the least efficient
  components.

* **best practices** increases the energy-efficiency gains that can be obtained
  through the widespread adoption the most efficient technologies and best management
  practices applicable to each data center type. This scenario focuses on maximizing the
  efficiency of each type of data center facility.

* **hyperscale data centers** where the infrastructure will be moved
  from smaller data centers to larger *hyperscale* data centers.

## Project Natick {#sec:natick}

To reduce energy consumption in data centers and reduce cost of
cooling Microsoft has developed *Project Natick*. To tackle this
problem Microsoft has built underwater datacenter. Another benefit of
this project is that data center can be deployed in large bodies of
water to serve customers residing in that area so it helps to reduce
latency by reducing distance to users and therefore increasing data
transfer speed. There are two phases of this project.

The project was executed in two phases.

Phase 1 was executed between August to November 2015.  In this phase
Microsoft was successfully able to deploy and operate vessel
underwater. The vessel was able to tackle cooling issues and effect of
biofouling as well. Biofouling is referred to as the fouling of pipes
and underwater surfaces by organisms such as barnacles and algae.

The PUE (Power Usage Effectiveness) of Phase1 vessel was 1.07 which is
very efficient and a perfect WUE (Water Usage Effectiveness) of
exactly 0, while land data centers consume ~4.8 liters of water per
KWH. This vessel consumed computer power equivalent to 300 Desktop PCs
and was of 38000 lbs and it operated for 105 days.

![The Leona Philpot prototype](images/project-natick-phase1.png){#fig:project-natick-phase1}

See @fig:project-natick-phase1, The *Leona Philpot* prototype was
deployed off the central coast of California on Aug. 10, 2015. Source:
[Microsoft](https://news.microsoft.com/features/microsoft-research-project-puts-cloud-in-ocean-for-the-first-time/)
[@microsoft-first-datacenter]


The phase 2 started in June 2018 and lasted for 90 days. Microsoft
deployed a vessel at the European Marine Energy Center in UK.

The phase 2 vessel was 40ft long and had 12 racks containing 864
servers. Microsoft powered this data center using 100% renewable
energy. This data ceter is claimed to be able to operate without
maintenance for 5 years. For cooling Microsoft used infrastructure
which pipes sea water through radiators in back on server racks and
then move water back in to ocean.

The total estimated lifespan of a Natick datacenter is around 20 years, after
which it will be retrieved and recycled.


![The Northern Isles prototype](images/project-natick-phase2.png){#fig:project-natick-phase2}

Source: [Microsoft](https://news.microsoft.com/features/under-the-sea-microsoft-tests-a-datacenter-thats-quick-to-deploy-could-provide-internet-connectivity-for-years/) [@microsoft-second-datacenter]


@fig:project-natick-phase2  shows the *Northern Isles* prototype being deployed near
Scotland.


Although the cooling provides a significant benefit while using
seawater, it is clear that long time studies need to be conducted with
this approach and not just studies over a very short period of
time. The reason for this is not just the measurement of a PUE factor
or the impact of algae on the infrastructure, but also how such a
vessel impacts the actual ecosystem itself.

Some thought on this include:

1. How doe the vesil increase the surrounding water temperature and
   effects the ecosystem
2. If places in saltwater, corrosion can occur that may not only
   effect the vesel, but also the ecosystem
3. Positive effects could also be created on ecosystems, which is for
   example demonstrated by creation of artificial reefs. However if
   the structure has to be removed after 20 years, which impat has it
   than on the ecosystem.

Find more about this at [@nytimes-datacenter]

## Renewable Energy for Data Centers {#sec:energy-renewable}

Due to the high energy consumption of data-centers, especially of
hyper-scale data centers. It is prudent to evaluate renewable energies
for the operation of such data centers. In particular this includes:

* Solar: <https://9to5google.com/2019/01/17/largest-ever-solar-farms-google/>
* Wind: <https://www.datacenterknowledge.com/wind-powered-data-centers>
* Hydro:
  <http://www.hydroquebec.com/data-center/advantages/clean-energy.html>
  there will be others
* Thermal: find better resource
  <https://spectrum.ieee.org/energywise/telecom/internet/iceland-data-center-paradise>
* Recyclers:
  <https://www.datacenterknowledge.com/data-centers-that-recycle-waste-heat>

Other aspects may include the storage of energy including:

* Batteries
* Store energy in other forms such as potential energy.

## Societal Shift Towards Renewables {#sec:energy-society}

We find a world wide trend in society to shift towards renewables. This
includes government efforts to support renewable in benefit of the
society:

* Germany, China, Island, and many more, 

but it also includes commitments by Corporations such as
 
* Google, AWS, IBM, ...

Also look at the US state of California and others that project
renewable energy.

Information about this is provided for example in 

* <https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2018/Jan/IRENA_2017_Power_Costs_2018.pdf>

We predict that any country not being heavily committed in renewable
energies will fall behind while missing out on reserach opportunities in
renewable energies themselfs. Today the cost of renewable energy
producing powerplants have so drastically improeved they they are not
only producting less green hous gasses but are today ifen cheper to
operate and build than combustion based energy producing power plants.


## Datacenter Risks and Issues 

Data Centers may be encounter issues such as outages of a variety of
reasons. In this section you will identify risks and issues that you
encounter as part of information you find on the Web or literature.


It is important that we recognize that datacenter outages can happen and
thus such autages must be build into the operations of the cloud
services that are offered to th customers to assure an expetcation level
of quality of service.

Here is an example:

* Date: Mar 02 2017
* Datacenter: AWS
* Category: Operator error
* Description: Mistake during a routine debugging exercise.
* Duration: Several hours
* Impact: large
* Cost impact > $160 million
* [Reference](https://www.datacenterknowledge.com/archives/2017/03/02/aws-outage-that-broke-the-internet-caused-by-mistyped-command/)

*
  [FACEBOOK, WHATSAPP, INSTAGRAM DOWN? WORLD'S BIGGEST SOCIAL NETWORKS SUFFER OUTAGES AND STOP LOADING IMAGES, Newsweek](https://www.newsweek.com/facebook-whatsapp-instagram-down-offline-outages-social-media-not-working-1447367)


![Instagram Outage [Ref](https://downdetector.com/status/instagram/map/?ref=DJ-D-L-CC-)](images/instagram-outage-jul-3-2019.png){#fig:inst-outage}



## Exercises {#sec:exercises-energy}


**Exercises**

**Prerequisite**: Knowledge about plagiarism.

**E.Datacenter.1:** Carbon footprint of a data center

> Complete the definitions of the terms used in the relevant section

**E.Datacenter.2:** Carbon footprint of data centers

**E.Datacenter.2.a:** Table

> World wide we have many data centers. Your task will be to find the
> carbon emission of a data center and its cost in $ based on energy
> use on a yearly basis. Make sure you avoid redundant reporting and
> find a new datacenter. Add your data to the table in this [link](https://docs.google.com/spreadsheets/d/1gh869zfjA4sVxL8-ga0af2_HLTTuOoD1IReuRSrbq4I/edit?usp=sharing)
under the Sheet *DataCenter*

**E.Datacenter.2.b:** Table

place a file in your repository called *datacenter.md* (note the
spelling all lower case) and describe details about you data center
without plagiarizing. Provide references to back up your data and
description.

TAs will integrate your information into the following table

**Table:** Cost of the data center

.<div class="smalltable">

| Data Center | Location | Year | Electricity Cost* | IT Load | Yearly Cost | Yearly CO2 Footprint | Equivalent in Cars |   |
|-------------|----------|------|-------------------|---------|-------------|----------------------|--------------------|---|
| ![No](images/no.png)  | ![No](images/no.png) | ![No](images/no.png)  | ![No](images/no.png)               | ![No](images/no.png)     | ![No](images/no.png)         | ![No](images/no.png)                  | ![No](images/no.png)                |   |
|             |          |      |                   |         |             |                      |                    |   |
|             |          |      |                   |         |             |                      |                    |   |

</div>

*as adjusted in calculator

> If you find other estimates for a data center or an entire data
> center fleet such as AWS world wide, please provide citations.

**E.Datacenter.3:** Your own Carbon footprint

> It is interesting to compare and measure your own carbon footprint.
> We will ask you anonymously to report your carbon footprint via a
> form we will prepare in future. As the time to do this is less than
> 2 minutes, We ask all students to report their footprint.
>
> Please use the calculator at:
>
> * <http://carbonfootprint.c2es.org/>
>
> Add your data to the table in this
> [link](https://docs.google.com/spreadsheets/d/1gh869zfjA4sVxL8-ga0af2_HLTTuOoD1IReuRSrbq4I/edit?usp=sharing)
> under the Sheet *CarbonFootPrint*

E.Datacenter.4:

> Pick a renewal energy from @sec:energy-renewable  and describe what
> it is. Find data centers that use this energy form.
> Include the information in your hid directory under the file
> datacenter.md.
>
> You will do the energy form based on taking the last digit from your
> HID and getting the modulo 6 and looking up the value in this table
>
> 0. Solar
> 1. Wind
> 2. Hydro
> 3. Thermal
> 4. Recyclers
> 5. Others
>
> If your modulo is undefined please use 5 (e.g. if your digit at the
> end of your hid 0)


E.Datacenter.5:

> Pick a country, state, or company from @sec:energy-society and
> summarize their efforts towards renewable energy and impacts within
> the society. Create a section and contribute it to the datacenter.md
> file. Use internet resources and cite them.

E.Datacenter.6:

> Write about cooling technologies in datacenter rack doors so it can
> be contributed to  @sec:datacenter-doors.

E.Datacenter.7:

> Review: [Nature Article](https://www.nature.com/articles/d41586-018-06610-y).
> Is there any more up to data available? What lessons do we take away from the
> article?

E.Datacenter.8:

> Find major data center outages and discuss the *concrete* impact on
> the internet and user community. Concrete means here not users of
> the center xyz lost services, but can you identify how many users or
> how many services were impacted and which? Is there a cost revenue
> loss projected somewhere? If you find an outage do significant
> research on it. For example other metrics could include what media
> impact did this outage have?


E.Datacenter.9:

> We encourage you to contribute to this section if you like and enjoy
> doing so.
