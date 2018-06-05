## Run Commands at Boot time

In many cases we need to provide configurations and programs that run
at boot time.  A number of different methods exist to run commands and
programs at boot time.


We will be focusing here only a few of them

### rc.local

On your Pi you will find under `/etc/rc.local` a file in which you can
list programs that are started up at boot time. The programs should
success fully run and exit with the status 0, and they must not
continuously run in which case they need to be started in background.

To make sure you do not forget it, simply add the following line at
the end of your program

    exit 0

indicating that the start was successful. Programs in rc.local must
use the absolute file path.

### Crontab


Crontab is a service the schedules jobs that can run at
various times repeatedly.  For example we can use corontab to run
commands every hour, every day, every half hour or other time
intervals or at reboot.

To use crontab follow these steps


1. Open a terminal and enter the command

   ```bash
   $ crontab -e
   ```
   
   If you are doing this for the first time, you will be asked to chose
   an editor. Please, choose your favorite editor
2. To run the program at boot time, add the following line to the at the end
   of the file

   ```
   @reboot <command>
   ```


Let us look at an example and assume we have test.py program in your
home directory at `/home/pi/test.py`. Once you add it to crontab with

     @reboot python /home/pi/test.py

it will be run at boot time

It is important to provide the absolute path to the file. In case your
file produces output you need to redirect it into a file

      @reboot python /home/pi/test.py > /home/pi/test.log


* When the raspberry pi reboots, the program will run automatically.


### References

A good introduction to the various methods is provided at

* <https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/>

For more information on crontab see for example:

* <http://www.adminschoice.com/crontab-quick-reference>

