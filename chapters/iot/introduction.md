Introduction
============

Internet of Things is one of the driving forces in the modernisation
of today's world. It is based on connecting *things* to the internet
to create a more aware world that can be interfaced with. This not
only includes us humans, but any *thing* that can interact with other
things.  It is clear that such a vision of interconnected devices will
result in billions of devices to communicate with each other. Some of
them may only communicate small number of items, while others will
communicate a large amount. Analysis of this data is dependent on the
capability of the *thing*. If it is to small the analysis can be
conducted on a remote server or cloud while information to act are fed
back from the device.  In other cases the device may be completely
autonomous and does not require any interaction. Yet in other cases
the collaborative information gathered from such devices is used to
derive decisions and actions.

Within this section we are trying to provide you with a small glimpse
into how IoT devices function and can be utilized on small projects.
Ideally if the class has all such a device we could even attempt to
build a cloud based service that collects and redistributes the data.

To keep things simple we are not providing a general introduction in
IoT. For that we offer other classes. However, we will introduce you to
two different devices. These are

* esp8266
* Raspberry Pi

The reasons we chose them is that

1.  They are cheap.
2.  We can program both in python allowing us to use a single
    programming language for all projects and assignments, and
3.  They are sufficiently powerful and we can conduct real projects with
    them beyond toy projects.
4.  The devices, especially the Raspberry PI can be used to also learn
    Linux in case you do not have access to a linux computer. Please
    note however the raspberry will have memory and space limitations
    that you need to deal with.

Projects that you can do to test the devices are

esp8266 (easy-moderate, small memory):

* a LED blinker
* a dendrite :o:
* a robot fish :o:
* a fish swarm :o:
* a robot swarm :o:
* an activity of your desire

Raspberry Pi (easy-moderate, 32GB space limitation):

1.  a LED blinker
2.  a robot car
3.  a robot car with camera
4.  a temperature service
5.  different clusters

<-!--
Crazyflie 2.0 (difficult):

* programming a drone
* programming a drone swarm
->

---

*Indiana University*: Please note that for those at IU we do have a
Lab in which you can use some of the devices pointed out here. You can
arrange for accessing the infrastructure.

In case you want to work on a swarm, we do have positioning sensors
that simplify that task.

---


Due to the small cost involed in these devices you can buy them
also simply yourself.

We provide throughout the book lists of hardware that you will need
for the various projects.


In general we think that these platforms provide a wonderful
introduction into IoT. Such platforms were
just a decade ago not powerful enough or too expensive. However today
the provide a serious platform for developers. Sensors are available
easily as most Android comparable sensors can be used.

Before we jump right into programming the devices, we like to point
out that we did not chose to use Arduinos much, as their price advantage is
no longer valid. They also are mostly using C and as we focus in our
material on python we decided to not spend much time on it.

We also find that esp8266 and Raspberry can interface
with most sensors. Having the ability to easily use WiFi however is
our primary reason for using them. Furthermore being able to attach a
camera to the Raspberry is just superb. Image analysis is one of
the drivers for big data.
