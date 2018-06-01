## IU 100 Node Cluster Case :construction:

At Indiana University we have currently about 100 Raspberry Pi's
available for students that work with us as part of classes.

Our goal for the use of these PI's is multitude.

First, we naturally like that all PI's could be used together in a
large cluster. Second we like that student teams up to 3 students can
use a samll cluster of between 6 - 5 Pi's and use them to providsion
their own OS. Third, we like to crate a case and shelf structure that
allows this modular utilization of the cluster while breaking it down
easily, but also assembeling or adding to the cluster easily.

This section will document our efforts to support this. The section is
heavely under construction and currently two STEM students work on the
case. They are joined by an independent study student ofer the summer
that looks at the software for this cluster.

To simplify management we will be using github for managing tasks, but
we will start collecting these tasks here. At this time the STEM
students are using still a google docs document till they migrate to
this or their own github.

The outline of the section is as follows :construction:

### Takss for STEM students


TODO: look ad word document.  reformat this and make sure to put in
relevant information. The questions raised should be excersises?

section for case documentation

* material based on McKay, modified ...
* do not plagiarize

### Designing in CAD for Laser 

We believe the best program for us to design a case for the cluster is
OpenSCAD. Links and tutorials to the software can be found here:

* <http://www.openscad.org/>
* <http://www.openscad.org/cheatsheet/>
* <https://github.com/RigacciOrg/openscad-rpi-library>
* <https://www.youtube.com/watch?v=WQd5db9lsQk>

Although OpenSCAD requires programming, it seems to be easier than
creating the 

this may require programming, but it may be easier to do as we have so view things to design




#### IU Maker Lab standard Software

In order for us to design a case we need to utilize a 3D CAD
program. The IU maker lab recommends to use Fusion 360 which is
available from 

* <https://www.autodesk.com/products/fusion-360/overview>

#### Alternative Free Software

However it does require a license and alternative that can be used for
free. This includes FreeCAD 

* FreeCAD Software <https://www.freecadweb.org/>
* Freccad Documentation <https://www.freecadweb.org/wiki/Main_Page>

This program allows you to design the layout of a 3D case via a
sophisticated GUI just like Fusion 360. 




### Cutting: Using Fusion 360 and a Laser Cutter

### Preparing and Using the Laser Cutter

Turning on laser cutter

Instructor demonstrates how to turn the laser cutter on and carry out other preparations to learners while operating the laser cutter.

1. Turn the laser cutteron. 

   Use key to turn on the laser cutter.

3. Turning the exhaust fan on.  T

   The fan is a separately switched unit. Turn on the switch on the wall next to the laser cutter.

   Question is raised: What is the possible risk of not ensuring the exhaust fan is running during laser cutter operation?
   
   TODO: Insead of doing this question, just provide the answer

3. Putting cutting material onto the laser cutterbed

   The instructor puts the cutting material onto the laser cutter bed.
   
   Question is raised: What will you do if the cutting material is smaller than the honeycomb bed? How will you place it?
Operating the panel

   TODO: Insead of doing this question, just provide the answer

![Figure: Control Panel](images/control-panel-laser-cutter.png)

FIX FORMAT .....

Instructor will demonstrate the use of each button. The middle top one is on- hold button, one can press it to save the power of the laser cutter.
The start/pause button can be used to pause a job in the middle. Once you start from a paused state the job resumes.
The stop button will cancel the job. You will need to restart the job from the beginning if this button is pressed to stop a job.
The four buttons on the bottom left controls the x/y horizontal shift of the laser head. The other two controls the z-axis, or vertical movement of the cutting bed.
Questions raised: What is the difference between stop and pause button?
f. Focusing the laser head
Instructor will move the laser head above the cutting material, then will place the focusing tool on the laser head. Then the instructor carefully raises the cutting bed. When the focusing tool touches the material on the bed it will fall off indicating the laser is focused.

Questions raised: What might be a risk of raising the cutting bed too quickly?
Sending file to job control software and initiate cutting
a. SendfiletoJobControl
The instructor open the saved file in Adobe Illustrator. Then the instructor clicks print in it to set the printer to “Trotec Laser Cutter”.
b. Setlasercuttingparameters
The instructor will change the width and height of the cutting area in the size column. By clicking the “Preferences” tab, the instructor can adjust the settings of different colors (traditionally red lines are for cutting and black lines and areas are for engraving)
c. Move file to Job Control work surface
Then the instructor could click on print to send file to the Job Control surface. Instructor will turn on Job Control software and discover the job is in the queue on the right of screen.
d. DragthefiletobecutontotheJobControlworksurfaceandsetitupin the upper right corner.
e. SelectthePlayarrowinJobControl
f. An exhaust warning will appear. Select OK. The job will start.
Questions raised:
What is the importance of setting cutting parameters?
What will you check before pressing the start button to ensure safety?

## First case

[scad file](images/case-a.scad)

![](images/case-a.png)

## 100 trial

[100-pis](images/100-pis.scad)

![](images/100-pis.png)

## Parts

[100-pis](images/parts.scad)

![](images/parts.png)


## 3D Model RAspbery PI

* STL <https://www.thingiverse.com/thing:1701186>
* <https://grabcad.com/library/raspberry-pi-3-reference-design-model-b-rpi-raspberrypi-raspberry-pi-2>

## Connections

Some ideas

* <http://www.instructables.com/id/How-to-Make-Anything-Using-Acrylic-and-Machine-Sc/>
* <http://skpang.co.uk/blog/archives/152>
* <http://www.uugear.com/product/acrylic-case-for-zero4u-and-raspberry-pi-zero-clear/>
* <https://www.phidgets.com/docs/T-Slot_Primer>
* <https://www.modmypi.com/blog/piot-relay-zero-case-assembly-instructions>
* <https://www.ponoko.com/blog/how-to-make/how-to-make-snug-joints-in-acrylic/>
* <https://www.bit-tech.net/guides/modding/a_modders_guide_to_acrylic/3/>
* <http://store.curiousinventor.com/blog/how-to-make-cheap-lasercut-custom-boxes-for-your-diy-electronics/>
* <http://discuss.arachnidlabs.com/t/easier-lasercut-boxes-with-custom-brackets/177>
* <https://makezine.com/2012/04/13/cnc-panel-joinery-notebook/>
* <https://makezine.com/2015/10/29/skill-builder-acrylic/>

WOuld be good for lego technic if in right distance and right height

* <https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=9048>

## Resources

* Fusion 360 <https://www.autodesk.com/products/fusion-360/overview>
* Q: are there free alternatives for fusion 360?
* Q: what is brand of lasercutter
* Q: if we have brand is there a link to a pdf or online manual 
