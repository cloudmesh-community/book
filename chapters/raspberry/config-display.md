## Automatic Display Detection [:cloud:](https://github.com/cloudmesh/book/blob/master/cloud-clusters/chapters/raspberry/config-display.md)

### Purpose 

In case you like to use the Raspberry Pi in your office, at home, or
in the field, you may find yourself in a situation where different
monitors with different resolutions are attached. Especially in the
field it is convenient if the Pi coudl do this adjustment for you and
use the resolution seigned for the attached device.

In this section we describe such a solution. We will automatically
detect the resolution based on the monitor attached. Once detected the
config file will be rewritten if necessary and the Pi will be rebooted
with the correct resolution in the configuration file.

### How it works

To achieve this we have developed the file 


[displaydetect.py](https://raw.githubusercontent.com/cloudmesh/cloudmesh.pi/master/displaydetect.py)
that automatically detects and set the display for the pi. To
integrate it in the Rasbian OS please follow these steps 

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
2. look at the prefered resolution
3. create an new elif in the switch

### Exercises

E.Display.1:

> Make the displaydetect.py truly discoverable, find a default
> resolution that you put in to the else statement. Identfy the
> prefered solution from the script and use that. Parse the apropriate
> parameters such as x,y, ans aspect ratio, rotation and other
> parameters.


