# Visual Feedback Management

Now that we have a Pi configured we need to make sure that we can
send sometimes visual clues about its operations. This can be done via
displays and LEDs. In case no display is available we can even connect
to the PI with a virtual display redirection.

## Default Display Setup

The raspberry pi comes with a defualt setup and any modern HDMI enabled 
TV or monitor will most likely work out of the box without any modifications. 
Just plug the HDMI cable in and start the Pi and you will probably see some 
boot messages and after a while see the splash screen for your installed 
operating system.

## Automatic Display Detection

In case you like to use the Raspberry Pi in your office, at home, or
in the field, you may find yourself in a situation where different
monitors with different resolutions are attached. Especially in the
field it is convenient if the Pi could do this adjustment for you and
use the resolution assigned for the attached device.

In this section we describe such a solution. We will automatically
detect the resolution based on the monitor attached. Once detected the
config file will be rewritten if necessary and the Pi will be rebooted
with the correct resolution in the configuration file.

:warning: In order for your monitor to work, you will need to add it
to the script we provide. Use the following program and add
appropriate cases for your monitor

    /usr/bin/tvservice -d /boot/edid.dat
    /usr/bin/edidparser /boot/edid.dat

### How it works

To achieve this we have developed the file 
[displaydetect.py](https://raw.githubusercontent.com/cloudmesh/cloudmesh.pi/master/displaydetect.py)
that automatically detects and set the display for the pi. To
integrate it in the Raspbian OS please follow these steps 

1. Install the display detect script. Run this as root:

   ```
   $ wget https://raw.githubusercontent.com/cloudmesh/cloudmesh.pi/master/displaydetect.py -O /bin/displaydetect.py
   $ chmod a+x /bin/displaydetect.py
   ```

2. Create a copy of `/boot/config.txt` and rename it to
   `/boot/config.txt.in`

   ```bash
   $ cp /boot/config.txt /boot/config.txt.in
   ```

3. Add the following lines to the end of the config.txt.in file:

   ```python
   # customized display setting
   hdmi_group=2
   hdmi_mode=87
   hdmi_cvt {x} {y} 60 6 0 0 0
   display_rotate={display_rotate}
   ```

4. Add the display detect script to rc.local so it runs every time the
   pi is booting. Add this to end of /etc/rc.local before the "exit 0" line:

   ```bash
   $ /usr/bin/python /bin/displaydetect.py
   ```

5. Make sure rc.local would be running during boot.

   ```bash
   $ systemctl status rc-local.service
   ```

6. Check if the service is 'active'.

   Once it is installed, the pi will be check the display during the
   first boot, and it will set the correct display parameters if found
   necessary and do a second boot to finish the configuration change.


Now you can go in the filed and use the monitor of your choice

### Adding new monitors

1. Look at the monitor name
2. look at the preferred resolution
3. create an new condition in the switch


## Using the Laptop as a monitor

In case you do not have a monitor at hand there are various ways on
using your computer as a monitor fo the Pi. The initial setup is
recommended to do with an HDMI monitor. There are instructions on the
Web that will let you set up the PI even without such a monitor, but
here we go the simpler route to set it up once, so you can access it
without monitor once you completed the setup.

First, install the remote desktop program on the Pi with

```bash
pi$ sudo apt-get install xrdp
```

Second, connect now your Laptop with an an ethernet cable to the
Laptop. As services start up automatically, you will have to wait for
a while. till the LAptop has assigned an IP address. Furthermore you
may need to allow the Laptop to assign DHCP addresses when you plug in
the ethernet cable.

:o: we could need your help here telling us how you do this for your
machine.

After some time you will see that the Laptop has assigned an ip
address

You can run on your Pi, but also on your Laptop (if it supports
`ifconfig`)

the command

```bash
pi$ ifconfig
```

and on your laptop

```bash
laptop$ ifconfig
```


You will see the typical output from `ifconfig`

look on the pi for the line that starts with

`inet addr`

it will be followed by an ip address such as

`192.168.10.1`

Now you can connect to this address, with the help of a program such
as *Remote Desktop Connection* on Windows or Bonjour on OSX.

Type in the ip address and you will see the desktop.

In order to avoid always having to do the first step and getting
different ip addresses, we recommend that you set up a static address
for the raspberry.

:o: please help identifying how to do this

:warning: We recommend not to use the WiFi and the ethernet adapter at the same
time as it can come to issues when you boot them up while they are
both connected.
 

## Exercises


E.Display.1:

: Configure your Raspberry Pi so you can access it via VNC.

E.Display.2:

: Make the displaydetect.py truly discoverable, find a default
  resolution that you put in to the else statement. Identify the
  preferred solution from the script and use that. Parse the appropriate
  parameters such as x,y, ans aspect ratio, rotation and other
  parameters.


