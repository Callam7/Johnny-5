<b>Author's Note: If You Are Using The Currently Flashed SD Card For The Pi, The Password is Pl@yWoWASVulperaMONK</b>

# Studio 5
------------

This Folder is dedicated to the gathering and general understanding of research topics that relate to the task in Project 2.

The research conducted contains the following mechanisms that utilize the open-cv library:
```
Face Recognition & Tracking
Glyph Recognition
Color Tracking & Recognition
```

# Set Up Raspberry Pi OS
------------------------

In order to have the main controller for the robot set up, we first must flash the raspberry pi OS to an SD card.
For documentation purposes, the rasbian and raspberry pi links are added in as research content.

The hardware required for set up is as follows:
```
An Micro SD card (Recommened size of 16GB+)
Raspberry Pi 3+ (The Higher The Better)
HDMI Cable
USB Keyboard
USB Mouse
SD Card USB Adapter
```


## Step 1: Download The Rasbian OS File
----------------------------------------
First off, download the rasbian installation file from [here](https://www.raspberrypi.org/software/) preferably the latest version for windows.
Once done, open the program so you will see the following on screen:

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/raspberry1.PNG" alt = "first rasp" height = "400">

## Step 2: Selecting The OS
---------------------------

Next, select the correct rasbian OS from the Operating System tab. We will need the 32 bit version.
<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/raspberry2.PNG" alt = "second rasp" height = "400">


## Step 3: Select SD Card Source
---------------------------------
Once done make sure to have the SD Card Adapter plugged in with the SD card inserted in it. Then select the <b>Multiple Flash Reader USB Device</b>
as the source to flash the OS to.

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/raspberry3.PNG" alt = "third rasp" height = "400">

Once done, write the OS to the SD Card and wait for the process to complete.

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/raspberry4.PNG" alt = "fourth rasp" height = "400">

## Step 4: Finish The Installation
----------------------------------

Once the write process has completed, the window will let you know that it is safe to remove the Flash Reader.
<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/raspberry5.PNG" alt = "final rasp">

Now that you have the OS on the SD Card, we can now get set up to use the raspberry pi.


# Setting Up The Raspberry Pi UI
--------------------------------
Now that we have our operating system flashed and ready to go, we now need to hook up the raspberry pi. The diagram below will aid you in the physical set up (<b>Note: This is a guide, the diagram may not reflect your pi set up.</b>):

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/piPic.png" alt = "pi picture" height = "400">

Once your all set up, follow the steps to ensure you have all necessary settings established.


## Step 1: The Start Up
------------------------

Boot up the raspberry pi on a display that supports HDMI cable ports, and then you will see this on screen:

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/windowA.png" alt = "window 1" height = "400">

Once this appears, hit next and you will see the set up for the country and region time. Select New Zealand as the country, English as the language, 
and Auckland as the timezone (<b>Note: This can vary depending on where you are setting the rasbian OS from.</b>). Your settings should match the below example:

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/windowB.png" alt = "window 2" height = "400">

Next, we'll want to establish an network connection for the raspberry pi. If you have a wifi connection that the raspberry can detect, simply select that network. Otherwise, we'll simply use the ethernet port as out connection so you can click next.

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/windowC.png" alt = "window 3" height = "400">

You have the option to update the software if there is one available:

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/windowD.png" alt = "window 4" height = "400">

Otherwise, skip to the next screen for the final set up. You will need to restart the raspberry pi in order for it to establish and apply the new settings that you have choosen. Simply restart and wait for the pi to reboot.

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/windowE.png" alt = "window 5" height = "400">

Great! We can now begin setting up our software for communicating with our devices.

## Step 2: Configuration
------------------------

Now that the raspberry pi can begin being used, we now need to ensure we have some security set up as well as the camera. First, click on the raspberry icon on the top left of the screen under Preferences and select <b>"Raspberry Pi Configuration"</b>.

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/piConfig.PNG" alt = "config pi">

Once you have the Configuration open, modify the settings under <b>System</b> so that they match the below example:

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/password.PNG" alt = "pass pi">

It is optional to include a password, however, if you are booting the raspberry pi with the SD card already flashed please refer to the password at the top of this document.

Next in the <b>Interface</b> tab, ensure that the camera and serial console is enabled for use. This will allow for our python code to access the camera that has been plugged in (either webcam or piCam).

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/cameraSetup.PNG" alt = "cam pi">

Once the preferences have been established, reboot the raspberry pi so that the system can apply the new configurations on start up.


## Step 3: Installing Dependencies
----------------------------------

Now that we have our configurations, we need to start installing the programmes needed to send code from the pi to multiple devices. The programmes we will require is as follows:
```
Arduino IDE
python3 & IDLE
picamera
OpenCV
```

On the top of the screen you'll see the commandline we'll be using for the raspberry pi, open the window and type in the below command.

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/command1.PNG" alt = "command pi">

This will ensure that we have the picamera drivers installed and updated. Once thats done, we'll need to install python3-pip so we can use the commandline to send pip commands for python formats and files. Type in `sudo apt install python3-pip` then hit enter.

Next we will need to install the IDLE for python3, allowing us to edit python code and debug it within the IDLE window. Type in
`sudo apt install python3 idle3` then hit enter. If for some reason the below message appears:

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Studio%205/SetUpImages/command3.PNG" alt = "third pi">

type in Y for yes and allow the commandline to continue installing the idle3 and python3 packages.

Once that's done, type in `sudo apt-get update && sudo apt-get upgrade` to check for any upgrades or updates needed for the pi kernel. This is so we dont run into any compatability issues with our programming tools.

Next we need to install the dependencies needed to access the OpenCV python library and its machine learning tools. First, type in
`pip install numpy` for the numpy python module. Once that's done, we will need the following commands:
```
sudo apt install cmake build-essential pkg-config git
sudo apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev
```
This will installed the required packages to use OpenCV in the python3 idle.

Finally, we will need to ensure that the Arduino IDE is installed. Type in `sudo apt-get install arduino` and hit enter, this will install our arduino programming tool. 

When you have all tools installed and downloaded, click on the raspberry icon on the tool bar and select <b>Programming</b> of which you should see all your python command line tools and Arduino IDE programmes installed and ready for use. If for some reason a programme or dependency fails to download and install, reboot the raspberry pi and they should appear in their respective locations and directories.

# Links Containing Relavence: 
-----------------------------
Below is the list of links I found to aid in my research around the raspberry pi as a controller, as well as the implementation of OpenCV and machine learning libraries. They are mainly for my reference during research and may become redundant depending on any alterations you commit to the project in general. 

OpenCV Object Tracking
https://www.pyimagesearch.com/2015/09/21/opencv-track-object-movement/

Glyph Recognition 
https://rdmilligan.wordpress.com/2015/07/19/glyph-recognition-using-opencv-and-python/

Raspberry Pi Website
https://www.raspberrypi.org/

Facetracking Program Using Arduino
https://create.arduino.cc/projecthub/WolfxPac/face-tracking-using-arduino-b35b6b

OpenCV Facetracking Tutorial
https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html

Set Up For Raspberry Pi Software Interface
https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started/5

Input Inc Robotics Group (Origin Of All 3D printed designs)
https://input-inc.com/#j5project

Pan Tilt Assembly
https://learn.adafruit.com/mini-pan-tilt-kit-assembly/the-pan-base

Johnny 5 Soundboard Files
http://johnnyfivesoundboard.com/

