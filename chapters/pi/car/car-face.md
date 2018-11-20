# Raspberry Pi Robot Car with Face Recognition and Identification

| Mani Kumar Kagita 
| mkagita@iu.edu 
| Indiana University - Bloomington 
| hid: SP18-711 

Keywords: I523, HID319, SP18-711, Robot Car, Face Recognition

## Introduction

A Computer Vision application which has always encouraged people,
concern about the capability and capacity of robots and computers to
determine, detect, recognize and interact with human
beings [@Boris2014]. We will prevail the advantage of cheaper tools that
are available in the market for computing and detecting a human face
from the image, recognizing the face using hardware like Raspberry Pi
and a video camera that is dedicated to Raspberry Pi. Simple and open
source software like OpenCV is used to detect a human face from the
video that is being captured and the image will be sent to Kairos face
recognition software which allows a high-level approach to this process.

In this fastest information era, every information is travelled in a
split of a second. There is much more need for accurate and fastest
methods for identifying, recognizing and authentication of humans. In
the present world, face recognition had become most important and
crucial form of human identification methods. As per Literature survey
statistics in face recognition, the two trends to receive significant
attention for the past several years are; the first is the law
enforcement applications and also a wide range of commercial techniques,
and the second is exponential booming of applications and feasible
technologies after 30 years of research [@riddhi2013].

The aim is achieved by a possibility to locate human beings or
identities like faces from the live video capture and within the context
of the picture. Most advanced human detection applications have this
functionality already available. When the picture is captured and loaded
into the system, it will scan the picture and will look for human faces
in it. The current implementation is to detect face and register them
with a name. If the face is detected and not recognized, Robot car will
ask to register the detected face with a name. If the human is already
registered in Kairos, then once the face is detected, Robot car will
greet the human with the associated name.This whole process determines
the Face detection and Face recognition techniques using Raspberry Pi
and Robot car.

Facial biometric data is to be computed first in creating a complete
recognition system. This biometric data is then compared with the face
database and to associate with the human identity. The difference
between a human and machine is, a human can easily and quickly identify
characteristics of a human face but then can only save few hundreds of
faces. Whereas a machine or computers prevails at storing and mapping
human characteristics and meta data. In the current generation, facial
recognition software can identify a human face within millions of images
from the database in seconds. Humans tend to forget human faces as time
pass by. Machines store them forever. Most of the Law firms across the
world follow the process and spend huge money on the development of
these facial recognition systems that can easily identify criminals in
real-time. A well-known example is studying human faces in airports and
bus stations.

The design of the Robot car integrated with Face recognition system will
navigate through dangerous or natural disaster locations where humans
unable to enter. Robot car while avoiding obstacles on its way, will
continuously monitor for human faces who got stuck or in danger and will
recognize the faces based on the user database. Once the human face is
recognized, it will intimate to corresponding authorities about the
human and will help in guiding assistance.

## Face Detection

Face Detection is a technique referred to computer vision technology
which is able to identify human faces within digital
images [@divya2013]. Face detection applications work using algorithms
and machine learning formulas for detecting human faces in the visual
images. Identifying only human faces from these images which can contain
landscapes, houses, animals is called Face Detection technique.

Face Detection is termed to only identify if there are any humans
present in the image or a video. It lacks the inability to recognize
which human face is present. Common widely used face detection
techniques are in auto-focus of a digital camera. During auto-focus,
camera lens will look for human faces in the range and identify them to
have focus in that particular area. Face Detection techniques will be
widely used in counting how many numbers of visitors attending a
particular event.

### How Face Detection Works

While Face Detection process is somewhat complex, the algorithms will
start off by searching for human eyes at first. Eyes usually represent a
valley region and its the easiest feature in human face to detect. Once
the eyes are detected, then the algorithms will look for rest of the
characteristics of a human face such as iris, nose, mouth, eyebrows, and
nostrils. Face detection algorithm then summarizes the data and shows
that it has successfully detected a human face from the facial region.
Additional tests can be conducted by the algorithm to make sure and
validate if the human face is detected [@jesse2017].

## Face Recognition

Like most of the biometric solutions, face recognition technology will
be used for identification and authentication purposes by measuring and
matching the unique facial characteristics of a human face. Using a
digital camera connected to the Raspberry Pi, once the face is detected,
face recognition software will quantify the characteristics of face and
then will match with the stored images in the database. Once the match
is positive, then the corresponding name will be displayed as
output [@biometrics2016].

Facial biometrics can be integrated with any system having a camera.
Border control agencies use face recognition to verify identities of the
travellers and can separate them from the trespassers. Government Law
agencies replace all the security cameras around the world with
biometric applications to scan faces in CCTV footage and to identify
persons of interest in the field. Face recognition has become one of the
fastest and human un-intervention techniques to find out the identity of
a particular human [@biometrics2016].

For the past few years, Face recognition has become one of the most
commonly used biometric authentication techniques. It mainly deals with
the pattern recognition and analysing the images. Two main tasks of face
recognition are: Face Verification and Face Identification. Face
Verification is comparing a human face in an image with a template image
and recognizing the correct patterns. Face Identification is comparing
human face in an image with multiple images in the database. Face
recognition techniques have more advantages than any other biometrics.
With well-sophisticated algorithms and coding, face recognition has a
high recognition rate or high identification rate of more than
90% [@riddhi2013]. +@fig:face-recognition shows the various levels 
of face recognition process [@viola2001].


![Block Diagram of a Face Recognition
System](images/Face-recognition.jpg){#fig:face-recognition}


### Face Recognition and Big Data Analysis

Face Recognition and Big Data are two distinct technologies which are
having hardly anything in common. But when they both are put together, a
technology drift takes place in terms of biometric authentication.
Storing a massive unique characteristics and libraries of human faces,
algorithms are used to run on these characteristics to recognize the
human face accurately. Using big data, a real-time analysis can be done
which identifies faces and applies the rules as they are happening.

Robot car is designed to collect all the facial features that are
encountered on its path and store them in the cloud. When the face is
detected by the camera, it sends the picture to the cloud and facial
recognition software will compare with huge database of faces that are
located in the cloud. Once the face features match, robot car will
respond with the unique name that is set for that human face.

## Software and Hardware Specifications

OpenCV is to be installed in Raspberry Pi to detect human faces within
the captured images. Kairos face recognition software is used to
recognize a human face and identify with the corresponding name.

### Software Used

##### Raspbian OS

This is the recommended OS for Raspberry Pi 3. Raspbian OS is Debian
based operating system. It can be installed from NOOBS installer.
Raspbian comes with various pre-installed software such as Python, Sonic
Pi, Java, Mathematica for programming and education.

##### Putty

PuTTY is an SSH and telnet client for the Windows platform. PuTTY is
open source software that is available with source code and is developed
and supported by a group of volunteers. Here we are using putty for
accessing our Raspberry Pi remotely.

##### OpenCV

Open Source Computer Vision Library (OpenCV) is an open source computer
vision and machine learning software library. OpenCV was built to
provide a common infrastructure for computer vision applications and to
accelerate the use of machine perception in the commercial products.
Being a BSD-licensed product, OpenCV makes it easy for businesses to
utilize and modify the code. The library has more than 2500 optimized
algorithms, which includes a comprehensive set of both classic and
state-of-the-art computer vision and machine learning algorithms. These
algorithms can be used to detect and recognize faces, identify objects,
classify human actions in videos, track camera movements, track moving
objects and extract 3D models of objects [@opencv].

##### Python 2 IDE

Python 2.7.x version Integrated Development Environment is used to
compile python program in Raspberry Pi. IDE is a text editor plus
terminal combination which is used to work on large projects with
complex code bases.

##### Kairos Face Recognition Software

Kairos is an artificial intelligence company specializing in face
recognition. Through computer vision and machine learning, Kairos can
recognize faces in videos,photos, and the real-world. A captured image
is sent to Kairos using an API call and then Kairos will search with the
face database. If it matches then will reply with the human name.

-   Identity
-   Emotions
-   Demographics

Kairos navigates the complexities of face analysis technology.

### Hardware Used

##### Raspberry Pi 3

Raspberry Pi 3 is the latest version of Raspberry Pi. Unless previous
versions, this have an inbuilt Bluetooth platform and a wifi support
module. There are total 40 pins in RPI3. Of the 40 pins, 26 are GPIO
pins and the others are power or ground pins (plus two ID EEPROM pins).
There are 4 USB ports, 1 Ethernet slot, one HDMI port, 1 audio output
port and 1 micro USB port. And also we have one micro SD card slot
wherein we have to install the recommended operating system on the micro
SD card. There are two ways to interact with your Raspberry Pi. Either
you can interact directly through HDMI port by connecting HDMI to VGA
cable, and keyboard and mouse or else you can interact from any other
system through Secure Shell (SSH) [@deligence2017].

##### Raspberry Pi Camera

The Raspberry Pi camera module can be used to take high-definition
video, as well as stills photographs. It's easy to use for beginners but
has plenty to offer advanced users if you're looking to expand your
knowledge. There are lots of examples online of people using it for
time-lapse, slow-motion and other video cleverness. You can also use the
libraries we bundle with the camera to create effects.

##### Robot Car Chassis Kit

The Mechanical design of the Robot car includes hardware such as motor
and wheel placement and body set-up. Robot car uses two gear-motors
attached to wheels and one free-wheel for having various movements like
forward, backward, left and right. Free-wheel ball is placed at the rear
side of the robot which helps for 360 degrees free
movement [@arduino2015]. L298N DC Stepper Motor Drive controller is used
to control the speed and direction of the two gear motor wheels.
Ultrasonic sensors are placed on the front side of the robot which is
capable to detect the objects on its path [@gregor2017].

## System Architecture

System Architecture consists of following blocks:

-   Raspberry Pi
-   Raspberry Pi Camera Module
-   L298N Dual H-Bridge Stepper Motor Controller
-   DC power supply 12v and 5v
-   Robot Car chassis kit
-   HC-SR04 Ultrasonic Sensor
-   SG90 Servo Motor.
-   Wires, Breadboard, Small PCB.

## Setup

### Connect Raspberry Pi

This section includes connectivity of Raspberry Pi to wifi.

-   Download Raspbian operating system to an SD card with a minimum
    capacity of 8GB.
-   Plugin USB power cable, keyboard, mouse and monitor cables to
    Raspberry Pi.
-   Insert the SD card with Raspbian OS into Pi and boot the system.
    Once the Pi is booted up, a window will appear with the Raspbian
    operating system. Click on Raspbian and Install.
-   Once the install process has completed, the Raspberry Pi
    configuration menu (raspi-config) will load. Here set the time and
    date for your region.
-   Enable wifi located at the upper right corner of the desktop and
    connect to wifi sid.

### Connect Raspberry Pi Camera Module

Before setting the camera configurations, first connect the camera to
Raspberry Pi. The cable slots into the connector situated between the
Ethernet and HDMI ports, with the silver connectors facing the HDMI
port. Once the connection is completed, boot up the Raspberry Pi and run
the following commands to install various supporting libraries. Skip
first two steps if Python is already installed on Raspberry Pi.

	pi$ sudo apt-get install python-pip
	pi$ sudo apt-get install python-dev
	pi$ sudo pip install picamera
	pi$ sudo pip install rpio

Once the libraries are installed, follow below steps to check if camera
is installed in Raspberry Pi.

	pi$ sudo raspi-config

If the camera option is not listed in the options, run the following
commands to update Raspberry Pi.

	pi$ sudo apt-get update
	pi$ sudo apt-get upgrade

##### Enable Camera

For face detection, PiCamera should be enabled from Raspberry Pi. The
following list of figures shows the detailed steps on how to enable
PiCamera [@boris2014].

As shown in Figure [\[F:raspi\]](#F:raspi){reference-type="ref"
reference="F:raspi"}, execute the configuration command from terminal.
From the listed options, select "Enable Camera" as shown in
Figure [\[F:selcamera\]](#F:selcamera){reference-type="ref"
reference="F:selcamera"}. Click on "Yes" option to enable the camera
interface as shown in
Figure [\[F:enbcamera\]](#F:enbcamera){reference-type="ref"
reference="F:enbcamera"}.


![Enable
Camera[]{label="F:enbcamera"}](images/enablecamera1.jpg)


![Enable
Camera[]{label="F:enbcamera"}](images/enablecamera2.jpg)


![Enable
Camera[]{label="F:enbcamera"}](images/enablecamera3.jpg)

### Install OpenCV and Required Libraries

OpenCV computer vision library is used to for face detection from the
live video streaming. Execute the following commands to install OpenCV
dependencies on the Raspberry Pi.


    pi$ sudo apt-get install build-essential
    pi$ sudo cmake pkg-config python-dev libgtk2.0-dev \
    		libgtk2.0 zlib1g-dev libpng-dev \
    		libjpeg-dev libtiff-dev libjasper-dev \
    		libavcodec-dev swig unzip

Select yes for all options and wait for the libraries and dependencies
to be installed.

Download opencv-2.4.9 zip file to Raspberry Pi. Change to the
corresponding directory and execute the following commands.

    pi$ cd opencv-2.4.9
    pi$ sudo apt-get install build-essential cmake \
    		pkg-config
    pi$ sudo apt-get install libjpeg-dev libtiff5-dev \
    		libjasper-dev libpng12-dev
    pi$ sudo apt-get install python-dev python-numpy \
    		libtbb2 libtbb-dev libjpeg-dev \
    		libpng-dev libtiff-dev libjasper-dev \
    		libdc1394-22-dev
    pi$ sudo apt-get install python-opencv
    pi$ sudo apt-get install python-matplotlib

After executing the commands the latest version of OpenCV is now
installed in Raspberry Pi. Time taken to install OpenCV is about 15
minutes.

### Integration of Raspberry Pi with Robot Car

Raspberry Pi connected with PiCamera is integrated with Robot car to
navigate using a web server. During the navigation, robot car will look
for human faces using PiCamera and then detects the face. Once the face
is detected, python program will call Kairos face detection software to
identify the person and greet with the name. If the human face is
unidentified then robot car will ask human to register their name. The
diagram in Figure [\[F:circuit\]](#F:circuit){reference-type="ref"
reference="F:circuit"} shows the circuit connections of Raspberry Pi to
stepper motor controller and DC motors of a robot car.

![Raspberry Pi Robot Car
Integration[]{label="F:circuit"}](images/RaspPi_Robot.jpg)

Figures [\[F:robotfront\]](#F:robotfront){reference-type="ref"
reference="F:robotfront"}, [\[F:robotside\]](#F:robotside){reference-type="ref"
reference="F:robotside"}, [\[F:robottop\]](#F:robottop){reference-type="ref"
reference="F:robottop"} represents corresponding front view, sideview
and topview of the robot car connections.

![Top view of Robot
Car[]{label="F:robottop"}](images/RobotCar_FrontView.jpg)

![Top view of Robot
Car[]{label="F:robottop"}](images/RobotCar_SideView.jpg)

![Top view of Robot
Car[]{label="F:robottop"}](images/RobotCar_TopView.jpg)

In the Table [\[T:pinlayout\]](#T:pinlayout){reference-type="ref"
reference="T:pinlayout"}, shows the connectivity of Raspberry Pi GPIO
pins to L298N stepper motor controller.

###   Actuator       Raspberry Pi GPIO Pin   L298N Pin
  Motor1A        GPIO23                  IN1
  Motor1B        GPIO24                  IN2
  Motor1Enable   GPIO25                  ENA
  Motor2A        GPIO9                   IN3
  Motor2B        GPIO10                  IN4
  Motor2Enable   GPIO11                  ENB

  : Pin connections of Raspberry Pi to stepper motor
  controller[]{label="T:pinlayout"}

### Kairos Face Recognition Setup

Kairos Face Recognition system has a free developer account which is
used to identify the human name from the images. Once registered a human
name with an image, the code will call Kairos API with a newly detected
human face and will look for the registered name. Kairos will do a quick
look-up in the human database from the registered account and if it
matches, will send the name of the human back to the code.

Setup as follows:

-   Register with Kairos using url "https:/www.kairos.com" as a free
    developer account
-   Login with registered username and password
-   Create an appname
-   An app id and a key will be generated. Save this for future use.
-   Enroll a sample user and a gallery name with the user image using
    following POST request.

            POST /enroll HTTP/1.1
            Content-Type: application/json
            app_id: your-app-id
            app_key: your-app-key
            {
            "image":" http://media.kairos.com/user.jpg ",
            "subject_id":"User",
            "gallery_name":"MyGallery"
            }
            

With the completed steps, Kairos face recognition application will be
created and ready for face recognition from the images.

## Code Explanation

### Face Detection

Before configuring face detection for the robot car, related libraries
including PiCamera and PiRGBArray libraries for camera to operate should
be imported in the code. These libraries will help to capture video and
images from the PiCamera.

    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import time
    import cv2
    import sys
    import imutils
    from fractions import Fraction
    import base64
    import requests
    import json
    import random
    import os

Haar Feature-based cascade classifier is an effective face or object
detection method to capture the frontal features of the
face [@viola2001]. This tool will help to continuous monitoring of any
human face to detect. Once detected a human face, the output values will
provide as Human Face Detected from the capturing video.

    ## Get user supplied values
    cascPath = './haarcascade_frontalface_default.xml'

    ## Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

Camera settings need to be updated in the code as per below suggestions.
The captured image is to be sent to Kairos for face recognition and so
we will set the resolution to a lower level. This will help to send the
image faster over the network without any delay.

    ## initialize the camera 
    #camera capture
    camera = PiCamera()
    camera.resolution = (160, 120)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(160, 120))

Below code represents PiCamera continuously monitor for human faces
detected from the grayscale video capture. Once the human face is
detected, espeak function in Raspberry Pi will send the voice to a
connected speaker and will output as "Human face detected". This
detected image is then saved as "User-Image.jpg" which is then will be
sent to Kairos during Face recognition.

Images in Figures [\[F:frontview\]](#F:frontview){reference-type="ref"
reference="F:frontview"}, [\[F:sideview1\]](#F:sideview1){reference-type="ref"
reference="F:sideview1"}, [\[F:sideview2\]](#F:sideview2){reference-type="ref"
reference="F:sideview2"} represents face detection of front and side
views within the circle using OpenCV.


![Side view 2 Face
detection[]{label="F:sideview2"}](images/Face-detect-frontview.png)


![Side view 2 Face
detection[]{label="F:sideview2"}](images/Face-detect-sideview1.png)


![Side view 2 Face
detection[]{label="F:sideview2"}](images/Face-detect-sideview2.png)

    ## allow the camera to warm-up
    time.sleep(0.1)
    lastTime = time.time()*1000.0
    ## capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, \ 
    	format="bgr", use_video_port=True):
    	## grab the raw NumPy array representing the image, 
    	## then initialize the timestamp and 
    	## occupied/unoccupied text
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        ## Detect faces in the image
        faces = faceCascade.detectMultiScale(
        	gray,
        	scaleFactor=1.1,
        	minNeighbors=5,
        	minSize=(30, 30),
        	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        print time.time()*1000.0-lastTime," \
        Found {0} faces!".format(len(faces))
        lastTime = time.time()*1000.0

        ## Draw a circle around the faces
        for (x, y, w, h) in faces:
            cv2.circle(image, (x+w/2, y+h/2), \
            int((w+h)/3), (255, 255, 255), 1)
        ## show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        if len(faces) == 1:
            print("Taking image...")
    	camera.capture("foo.jpg")
    	os.system('espeak "Human face detected"')
    	inputImage= "./foo.jpg"
    	del camera
    	break 
    	## clear the stream in preparation for the 
    	#next frame
        rawCapture.truncate(0)
        
    	## if the `q` key was pressed, break from 
    	#the loop
        if key == ord("q"):
            del camera
            exit()

### Face Recognition

For the Face Recognition, we use Kairos to detect the facial
characteristics. A JSON config file is to be placed in the same folder
as of the code with Kairos API app id and key value. When the human face
is detected, the code will generate an API call to Kairos software along
with the gallery name, API app id and key values. Image when sending to
Kairos, it will be base64 encrypted and will send over the network for
security purpose. This encrypted image will then be decrypted at Kairos
platform.

    KAIROS = "api.kairos"
    KairosGallery = 'MyFace'
    KairosConfig = './kairos_config.json'

    def trainKairos(image, name):
        global KairosGallery
        headers = {
            'app_id': 'your-app-idd39fc1b1',
            'app_key': 'your-app-key'
        }
        data = {
            'image': base64.b64encode(image),
            'gallery_name': KairosGallery,
            'subject_id': name
        }
        r = requests.post('http://api.kairos.com/enroll', \ 
            headers=headers, data=json.dumps(data))
        print(r.text)
        return(None)

    class Recognize():
        def __init__(self, API, config_file):
            self.api = API
            self.config = config_file

        #def recognize(self, image_path):
        ##    return self.__recognizeKairos(image_path)
        
        def recognizeKairos(self, image):
            with open(image, "rb") as image_file:
                encoded_string = base64.b64encode\
                (image_file.read())
            with open(self.config, "rb") as config_file:
                config = json.loads \ 
                (config_file.read())
            data = {
                "image": encoded_string,
                "gallery_name": config["gallery_name"]
            }

            headers = {
                "Content-Type": "application/json",
                "app_id": config["app_id"],
                "app_key": config["app_key"]
            }

The output from Kairos software is in JSON format. The output is then
segregated as per the key-value pairs and then saved into local
variables. When the image is recognized, a success transaction message
will be obtained from Kairos along with subject id and face id.

    try:
        r = requests.post("https://api.kairos.com/recognize", \ 
                     headers=headers, data=json.dumps(data))
        data = r.json()
        print data
        ## print json.dumps(data, indent=4)
        faces = []
        if "images" in data:
            for obj in data["images"]:
                if obj["transaction"]["status"] == \
                "success":
                    face_obj = {}
                    face_obj["person"] = \
                    obj["transaction"]["subject_id"]\
                    .decode("utf_8")
                    #face_obj["faceid"] = \
                    obj["candidates"][0]["face_id"]\
                    .decode("utf_8")
                    face_obj["confidence"] = \
                    obj["transaction"]["confidence"]
                    faces.append(face_obj)
                elif obj["transaction"]["status"] == \
                "failure":
                    face_obj = {}
                    face_obj["person"] = "unidentified"
                    face_obj["confidence"] = 0
                    faces.append(face_obj)
                else:
                    print "its in last loop"
                return faces
     except requests.exceptions.RequestException as \
     exception:
           print exception
            return None

The output from Kairos face recognition software is to be read to
understand if the person name is identified or not. If it is identified
then the person name will be listed according to the corresponding
person in the image. If the human is not identified, then the code will
suggest if the user wants to registered for face recognition. Once the
user key in the name, Kairos API call is generated while sending newly
registered name and the gallery name to that corresponding application
id. Here the newly recognized user will be registered with the name and
his image. When the user is recognized by the camera in next
corresponding events, then Robot car will greet the user with his name.

    if __name__ == "__main__":
        r = Recognize(KAIROS, "kairos_config.json")
        x = r.recognizeKairos(inputImage)
        
        #print x
        #print x["person"]
        #print x[0]["person"]
        string1 = x[0]["person"]
        #print string1
        os.system('espeak "Hello...""{}"'.format(string1))
        if x[0]["person"] == "unidentified":
            os.system('espeak "Please enter your \ 
                      name to Register"')
            nameToRegister = raw_input("Please enter \ 
                            your name to Register :")
            binaryData = open(inputImage, 'rb').read()
            print('Enrolling to Kairos')
            trainKairos(binaryData, nameToRegister)
            print "You are now Registered as :", \ 
            nameToRegister os.system('espeak \ 
            "Hello...""{}"'.format(nameToRegister))
            exit()

### Robot Car Navigation

    import RPi.GPIO as GPIO
    from time import sleep

    GPIO.setmode(GPIO.BOARD)

    #Connecting two wheel motors to Raspberry Pi GPIO 
    #Left Motor (Motor 1) connections
    Motor1A = 16 #(GPIO 23 - Pin 16)
    Motor1B = 18 #(GPIO 24 - Pin 18)
    Motor1Enable = 22 #(GPIO 25 - Pin 22)

    #Right Motor (Motor 2) Connecctions
    Motor2A = 21 #(GPIO 9 - Pin 21)
    Motor2B = 19 #(GPIO 10 - Pin 19)
    Motor2Enable = 23 #(GPIO 11 - Pin 23)

    #Ouptut of Morors to set as OUT
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1Enable,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2Enable,GPIO.OUT)

    ## Defining function for Robot car to move forward
    def forward():
    	GPIO.output(Motor1A,GPIO.HIGH)
    	GPIO.output(Motor1B,GPIO.LOW)
    	GPIO.output(Motor1Enable,GPIO.HIGH) 
    	GPIO.output(Motor2A,GPIO.HIGH)
    	GPIO.output(Motor2B,GPIO.LOW)
    	GPIO.output(Motor2Enable,GPIO.HIGH) 

    	sleep(2)

    ## Defining function for Robot car to move backward
    def backward():
    	GPIO.output(Motor1A,GPIO.LOW)
    	GPIO.output(Motor1B,GPIO.HIGH)
    	GPIO.output(Motor1Enable,GPIO.HIGH)
    	GPIO.output(Motor2A,GPIO.LOW)
    	GPIO.output(Motor2B,GPIO.HIGH)
    	GPIO.output(Motor2Enable,GPIO.HIGH)

    	sleep(2)

    ## Defining function for Robot car to turn right
    def turnRight():
    	print("Going Right")
    	GPIO.output(Motor1A,GPIO.HIGH)
    	GPIO.output(Motor1B,GPIO.LOW)
    	GPIO.output(Motor1Enable,GPIO.HIGH)
    	GPIO.output(Motor2A,GPIO.LOW)
    	GPIO.output(Motor2B,GPIO.LOW)
    	GPIO.output(Motor2Enable,GPIO.LOW)

    	sleep(2)

    ## Defining function for Robot car to turn left
    def turnLeft():
    	print("Going Left")
    	GPIO.output(Motor1A,GPIO.LOW)
    	GPIO.output(Motor1B,GPIO.LOW)
    	GPIO.output(Motor1Enable,GPIO.LOW)
    	GPIO.output(Motor2A,GPIO.HIGH)
    	GPIO.output(Motor2B,GPIO.LOW)
    	GPIO.output(Motor2Enable,GPIO.HIGH)

    	sleep(2)

    ## Defining function for Robot car to stop
    def stop():
    	print("Stopping")
    	GPIO.output(Motor1A,GPIO.LOW)
    	GPIO.output(Motor1B,GPIO.LOW)
    	GPIO.output(Motor1Enable,GPIO.LOW)
    	GPIO.output(Motor2A,GPIO.LOW)
    	GPIO.output(Motor2B,GPIO.LOW)
    	GPIO.output(Motor2Enable,GPIO.LOW)

### Controling Robot Car using webserver

    from flask import Flask, render_template, \ 
    request, redirect, url_for, make_response
    import RPi.GPIO as GPIO
    import motors

    #set up GPIO
    GPIO.setmode(GPIO.BOARD) 

    #set up flask server
    app = Flask(__name__) 

    #when the root IP is selected, return index.html page
    @app.route('/')
    def index():

    	return render_template('index.html')

    #recieve which pin to change from the button press on \ 
    #index.html
    #each button returns a number that triggers a command in \ 
    #this function
    #
    #Uses methods from motors.py to send commands to the GPIO \ 
    ## to operate the motors
    @app.route('/<changepin>', methods=['POST'])
    def reroute(changepin):

    	changePin = int(changepin) #cast changepin to an int

    	if changePin == 1:
    		motors.turnLeft()
    	elif changePin == 2:
    		motors.forward()
    	elif changePin == 3:
    		motors.turnRight()
    	elif changePin == 4:
    		motors.backward()
    	else:
    		motors.stop()


    	response = make_response(redirect(url_for('index')))
    	return(response)

    #set up the server in debug mode to the port 8000
    app.run(debug=True, host='0.0.0.0', port=8000) 

## Applications

There are lots of applications of face recognition. Face recognition is
already being used to unlock phones and specific applications. Face
recognition is also used for biometric surveillance. Banks, retail
stores, stadiums, airports and other facilities use face recognition to
reduce crime and prevent violence.

## Conclusion

A robot car using Raspberry Pi is designed to detect and recognize the
human faces from the images taken from PiCamera attached to the
Raspberry Pi. Using Python programming language, the system is being
built such that it can face detect and recognize in real time scenarios.
For this solution Kairos Face recognition software is being used which
have a free developer account. Face recognition is tested with various
types of facial views like the front view and side view. The Round Trip
Time for robot car to take picture and recognize face is nearly 3
seconds. The efficiency of the system was analysed based on the rate of
face detection in real time. As per the analysis, this current system
shows tremendous performance efficiency where the face detection and
recognition can be performed even with very low-quality images.

The authors would like to thank Dr. Gregor von Laszewski for his support
and suggestions in writing this paper.

## Links

The code is located at

* <https://github.com/cloudmesh-community/hid-sp18-711/tree/master/project-code>
