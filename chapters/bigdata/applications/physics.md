# Physics

This section starts by describing the LHC accelerator at CERN and
evidence found by the experiments suggesting existence of a Higgs Boson.
The huge number of authors on a paper, remarks on histograms and Feynman
diagrams is followed by an accelerator picture gallery. The next unit is
devoted to Python experiments looking at histograms of Higgs Boson
production with various forms of shape of signal and various background
and with various event totals. Then random variables and some simple
principles of statistics are introduced with explanation as to why they
are relevant to Physics counting experiments. The unit introduces
Gaussian (normal) distributions and explains why they seen so often in
natural phenomena. Several Python illustrations are given. Random
Numbers with their Generators and Seeds lead to a discussion of Binomial
and Poisson Distribution. Monte-Carlo and accept-reject methods. The
Central Limit Theorem concludes discussion.

## Looking for Higgs Particles

### Bumps in Histograms, Experiments and Accelerators

This unit is devoted to Python and Java experiments looking at
histograms of Higgs Boson production with various forms of shape of
signal and various background and with various event totals. The
lectures use Python but use of Java is described.

-   [:scroll:
    Higgs (20)](https://drive.google.com/open?id=0B8936_ytjfjmYXNoM3ZadGR6QlE)

-   <{gitcode}/physics/mr-higgs/higgs-classI-sloping.py>

### Particle Counting

We return to particle case with slides used in introduction and stress
that particles often manifested as bumps in histograms and those bumps
need to be large enough to stand out from background in a statistically
significant fashion.

-   [:clapper: Discovery of Higgs Particle
    (13:49)](https://www.youtube.com/watch?v=iaypHlgFyuU)

We give a few details on one LHC experiment ATLAS. Experimental physics
papers have a staggering number of authors and quite big budgets.
Feynman diagrams describe processes in a fundamental fashion.

-   [:clapper: Looking for Higgs Particle and Counting Introduction II
    (7:38)](http://youtu.be/UAMzmOgjj7I)

### Experimental Facilities

We give a few details on one LHC experiment ATLAS. Experimental physics
papers have a staggering number of authors and quite big budgets.
Feynman diagrams describe processes in a fundamental fashion.

-   [:clapper: Looking for Higgs Particle Experiments
    (9:29)](http://youtu.be/BW12d780qT8)

### Accelerator Picture Gallery of Big Science

This lesson gives a small picture gallery of accelerators. Accelerators,
detection chambers and magnets in tunnels and a large underground
laboratory used fpr experiments where you need to be shielded from
background like cosmic rays.

-   [:clapper: Accelerator Picture Gallery of Big Science
    (11:21)](http://youtu.be/WLJIxWWMYi8)

### Resources

-   <http://grids.ucs.indiana.edu/ptliupages/publications/Where%20does%20all%20the%20data%20come%20from%20v7.pdf>
-   <http://www.sciencedirect.com/science/article/pii/S037026931200857X>
-   <http://www.nature.com/news/specials/lhc/interactive.html>

Looking for Higgs Particles: Python Event Counting for Signal and
Background (Part 2)

This unit is devoted to Python experiments looking at histograms of
Higgs Boson production with various forms of shape of signal and various
background and with various event totals.

-   \[:scroll: Higgs II
    (29)\](https://drive.google.com/open?id=0B8936\_ytjfjmUHRpV2g2V28walE}

Files:

-   <{gitcode}/physics/mr-higgs/higgs-classI-sloping.py>
-   <{gitcode}/physics/number-theory/higgs-classIII.py>
-   <{gitcode}/physics/mr-higgs/higgs-classII-uniform.py>

### Event Counting

We define *event counting* data collection environments. We discuss the
python and Java code to generate events according to a particular
scenario (the important idea of Monte Carlo data). Here a sloping
background plus either a Higgs particle generated similarly to LHC
observation or one observed with better resolution (smaller measurement
error).

-   [:clapper: Event Counting (7:02)](http://youtu.be/h8-szCeFugQ)

### Monte Carlo

This uses Monte Carlo data both to generate data like the experimental
observations and explore effect of changing amount of data and changing
measurement resolution for Higgs.

-   [:clapper: With Python examples of Signal plus Background
    (7:33)](http://youtu.be/bl2f0tAzLj4) This lesson continues the
    examination of Monte Carlo data looking at effect of change in
    number of Higgs particles produced and in change in shape of
    background.

-   [:clapper: Change shape of background & num of Higgs Particles
    (7:01)](http://youtu.be/bw3fd5cfQhk)

### Resources

-   Python for Data Analysis: Agile Tools for Real World Data By Wes
    McKinney, Publisher: O'Reilly Media, Released: October 2012,
    Pages: 472.
-   <http://jwork.org/scavis/api/>
-   <https://en.wikipedia.org/wiki/DataMelt>

### Random Variables, Physics and Normal Distributions

We introduce random variables and some simple principles of statistics
and explains why they are relevant to Physics counting experiments. The
unit introduces Gaussian (normal) distributions and explains why they
seen so often in natural phenomena. Several Python illustrations are
given. Java is currently not available in this unit.

-   [:scroll:
    Higgs (39)](https://drive.google.com/open?id=0B8936_ytjfjmNWhrS0xadk16SWM)
-   <{gitcode}/physics/number-theory/higgs-classIII.py>

### Statistics Overview and Fundamental Idea: Random Variables

We go through the many different areas of statistics covered in the
Physics unit. We define the statistics concept of a random variable.

-   [:clapper: Random variables and normal distributions
    (8:19)](https://www.youtube.com/watch?v=_sLGyt4qWWk)

### Physics and Random Variables

We describe the DIKW pipeline for the analysis of this type of physics
experiment and go through details of analysis pipeline for the LHC ATLAS
experiment. We give examples of event displays showing the final state
particles seen in a few events. We illustrate how physicists decide
whats going on with a plot of expected Higgs production experimental
cross sections (probabilities) for signal and background.

-   [:clapper: Physics and Random Variables I
    (8:34)](http://youtu.be/Tn3GBxgplxg)
-   [:clapper: Physics and Random Variables II
    (5:50)](http://youtu.be/qWEjp0OtvdA)

### Statistics of Events with Normal Distributions

We introduce Poisson and Binomial distributions and define independent
identically distributed (IID) random variables. We give the law of large
numbers defining the errors in counting and leading to Gaussian
distributions for many things. We demonstrate this in Python
experiments.

-   [:clapper: Statistics of Events with Normal Distributions
    (11:25)](http://youtu.be/LMBtpWOOQLo)

### Gaussian Distributions

We introduce the Gaussian distribution and give Python examples of the
fluctuations in counting Gaussian distributions.

-   [:clapper: Gaussian Distributions
    (9:08)](http://youtu.be/LWIbPa-P5W0)

### Using Statistics

We discuss the significance of a standard deviation and role of biases
and insufficient statistics with a Python example in getting incorrect
answers.

-   [:clapper: Using Statistics (14:02)](http://youtu.be/n4jlUrGwgic)

### Resources

-   <http://indico.cern.ch/event/20453/session/6/contribution/15?materialId=slides>
-   <http://www.atlas.ch/photos/events.html>
-   <https://cms.cern/>

### Random Numbers, Distributions and Central Limit Theorem

We discuss Random Numbers with their Generators and Seeds. It introduces
Binomial and Poisson Distribution. Monte-Carlo and accept-reject methods
are discussed. The Central Limit Theorem and Bayes law concludes
discussion. Python and Java (for student - not reviewed in class)
examples and Physics applications are given.

-   [:scroll: Higgs
    III (44)](https://drive.google.com/open?id=0B8936_ytjfjmTUxkZXVRRmlBSUk)

Files:

-   <{gitcode}/physics/calculated-dice-roll/higgs-classIV-seeds.py>

#### Generators and Seeds

We define random numbers and describe how to generate them on the
computer giving Python examples. We define the seed used to define to
specify how to start generation.

-   [:clapper: Higgs Particle Counting Errors
    (6:28)](https://www.youtube.com/watch?v=de4AQ9AFt54)
-   [:clapper: Generators and Seeds II
    (7:10)](http://youtu.be/9QY5qkQj2Ag)

#### Binomial Distribution

We define binomial distribution and give LHC data as an example of where
this distribution valid.

-   [:clapper: Binomial Distribution:
    (12:38)](http://youtu.be/DPd-eVI_twQ)

#### Accept-Reject

We introduce an advanced method **accept/reject** for generating random
variables with arbitrary distributions.

-   [:clapper: Accept-Reject (5:54)](http://youtu.be/GfshkKMKCj8)

#### Monte Carlo Method

We define Monte Carlo method which usually uses accept/reject method in
typical case for distribution.

-   [:clapper: Monte Carlo Method (2:23)](http://youtu.be/kIQ-BTyDfOQ)

#### Poisson Distribution

We extend the Binomial to the Poisson distribution and give a set of
amusing examples from Wikipedia.

-   [:clapper: Poisson Distribution (4:37)](http://youtu.be/WFvgsVo-k4s)

#### Central Limit Theorem

We introduce Central Limit Theorem and give examples from Wikipedia.

-   [:clapper: Central Limit Theorem
    (4:47)](http://youtu.be/ZO53iKlPn7c)

#### Interpretation of Probability: Bayes v. Frequency

This lesson describes difference between Bayes and frequency views of
probability. Bayes's law of conditional probability is derived and
applied to Higgs example to enable information about Higgs from multiple
channels and multiple experiments to be accumulated.

-   [:clapper: Interpretation of Probability
    (12:39)](http://youtu.be/jzDkExAQI9M)

#### Resources

\TODO{integrate physics-references.bib}

## SKA -- Square Kilometer Array

Professor Diamond, accompanied by Dr. Rosie Bolton from the SKA Regional
Centre Project gave a presentation at SC17 "into the deepest reaches of
the observable universe as they describe the SKA's international
partnership that will map and study the entire sky in greater detail
than ever before."

-   <http://sc17.supercomputing.org/presentation/?id=inspkr101&sess=sess263>

A summary article about this effort is available at:

-   <https://www.hpcwire.com/2017/11/17/sc17-keynote-hpc-powers-ska-efforts-peer-deep-cosmos/>
    The video is hosted at
-   <http://sc17.supercomputing.org/presentation/?id=inspkr101&sess=sess263>
    Start at about 1:03:00 (e.g. the one hour mark)

