## Pi Clusters on the Internet

There is a large number of projects related to creating Pi clusters on
the internet. They vary in size and software installed on
them. Naturally a Pi cluster is a useful training and development
environment for research organizations and thus many bigger projects
are located at universities as well as government labs. However, we
also have many projects done by enthusiasts.

We distinguish two different efforts. First, we often find projects
that target the creation of cases for such clusters and second, we
find projects that develop software fort these clusters.  This section
will provide an overview of these activities and provide links to
these activities.


### Cluster Cases

#### Lego

When looking at the placement of the wholes on the Raspberry Pi, the
width between the wholes on the small side seems to be exactly 7 Lego
technic beam wholes apart. This has the advantage that one could
build a quick frame form Lego pieces such as a

- 2 * 11 ($0.22) piece
  * <https://www.brickowl.com/catalog/lego-beam-11-32525-64290>
- 2 * two piece * 4 * 4 ($0.192)
  * <https://www.brickowl.com/catalog/lego-beam-2-43857>
- A number of connector pins
  * <https://www.brickowl.com/catalog/lego-technic-pin-with-lengthwise-friction-ridges-and-center-slots-2780>
  * <https://www.brickowl.com/catalog/lego-long-pin-with-friction-6558>
  
The cost is about $0.25 per piece = $2.74 per pi.

So if we are having 100 pis we end up with $274. However
we also need still to get screw and Lego connectors which we at this
time have not counted and included in this calculation.


Naturally Lego's have been explored by others

* [Images on google](https://www.google.com/search?q=raspberry+pi+case+lego+technic&rlz=1C5CHFA_enUS727US727&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwjYwYbni6vbAhWJy4MKHaiiCmYQsAQIMw&biw=1648&bih=883)
* University of Southampton:
  <https://www.theregister.co.uk/2012/09/12/raspberry_pi_supercomputer/>
  Instructions are no longer at the original link
  TODO: can they be found
* Lego Technic:
  <https://www.reddit.com/r/raspberry_pi/comments/39kwjc/pidra_my_7_headed_rpi_cluster_with_99_lego/>,
  <https://imgur.com/a/rYybo>
* Lego Technic <https://www.flickr.com/photos/fotero/7954299054/>
* Old style Lego <https://www.uweziegenhagen.de/?p=3155>


Other ideas using Lego's include:

* Compact case: Single board No screws <https://www.youtube.com/watch?v=UYY72a6wWqs>
* Zero 3D print Thingverse <https://www.thingiverse.com/thing:1427245>
* B+ 3D Pi case <https://www.thingiverse.com/thing:1007347>

Other interesting but not cluster related links include

* Lego hat <https://www.elektor.de/lego-rpi-board-159010-91>
* Brick Pi <https://www.dexterindustries.com/shop/brickpi-advanced-for-raspberry-pi/>

#### Beast by resion.io

This company has provided some larger designs for Raspberry Pi clusters
and tries to create a modular system to put a number of Pis on plates
that than can be connected.

* <https://www.youtube.com/watch?v=A5VsfcnfeR0>
* <https://resin.io/blog/the-evolution-of-the-beast-continues/?utm_content=buffer11bf2&utm_medium=social&utm_source=facebook.com&utm_campaign=buffer>
* <https://resin.io/blog/good-better-beast-week-2/>


### Clusters


Additional links which could be useful include:

* <https://github.com/sdsc/sandbox-cluster-guide>
* <https://thenewstack.io/6-common-errors-when-building-a-raspberry-pi-cluster/>
* <http://www.mindkits.co.nz/blog/5-Most-Popular-Raspberry-Pi-Cluster-Supercomputer-Projects>
* <https://www.networkworld.com/article/3156748/computers/10-amazing-raspberry-pi-clusters.html>
* <https://projects.raspberrypi.org/en/projects/build-an-octapi>

An older document on how to create an MPI cluster is located at

* Pi 2 MPI cluster, Boise State <http://coen.boisestate.edu/ece/files/2013/05/Creating.a.Raspberry.Pi-Based.Beowulf.Cluster_v2.pdf>

#### Swarm

How to set up docker swarm is documented here

* <https://medium.com/@bossjones/how-i-setup-a-raspberry-pi-3-cluster-using-the-new-docker-swarm-mode-in-29-minutes-aa0e4f3b1768>
