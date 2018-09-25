# VNC

**Note:** *If you like to connect to your Raspberry from your laptop, we
recommend to use VNC. If you rather like to connect a monitor and
keyboard as well as a mouse to the Raspberry, you can skip the steps
with the VNC update.*

## Setting up VNC


We had some issues with the installed version of VNC that is customized
for connecting a Laptop via the ethernet cable to the PI. However as we
connect wirelessly, our setup is slightly different. The easiest way that
we found is to update the Raspbian OS as follows. In a terminal type

    sudo apt-get update
    sudo apt-get install realvnc-vnc-server 
    sudo apt-get install realvnc-vnc-viewer

Next you enable the VNC server in the configuration panel via the
Raspbian GUI by selecting

     Menu > 
        Preferences > 
           Raspberry Pi Configuration > 
              Interfaces.

Here you toggle the VNC service to enabled. As we are already at it in
our setup we enabled all other services, especially those that deal with
Grove sensor related bins and wires.

Next reboot and double check if the settings are preserved after the
reboot

### Install VNC on macOS

To install a vnc server of your liking on your Mac. You find one at

-   [http://www.realvnc.com/download/vnc/latest/](http://www.realvnc.com/download/vnc/latest/%5D)

Be sure to download the version of the VNC Viewer for the computer you
are going to use to virtually control the Pi (there is a version listed
for Raspberry Pi-- do not download this one. For us this is the Mac
version.)

### Run VNC Viewer on macOS

Once you have downloaded the VNC viewer installed it you can open the
program. Next you can start vnc viewer and enter the ip address of your
raspberry. Make sure you are on the same network. You can find the
address by using ifconfig.
