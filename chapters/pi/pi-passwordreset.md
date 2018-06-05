
## Change Password on the SD-Card :o:

from 418

Gregor: Incomplete description, unclear

* Unplug the raspberry pi cluster and remove the SD card from the slot
* Insert the SD card into a computer, and make sure we should have
  root  access on that computer
* Locate and edit the etc/shadow file on the SD card
* Run the command

  ```$ openssl passwd -1 -salt <unique string>```

* We must find the line that starts with pi and replace the text
  between the first and second with the output from the above command
  we had executed 
* Eject the SD card from the computer
* Insert the SD card back into the pi cluster
* Boot the raspberry pi
* SSH to log into raspberry pi and set up the password
