# Set Up Guide For CAD Files.
------------------------------

In order to view the .STL and .SLDASM, you must first get eDrawings software from Solidworks installed, of which can be found [here](https://www.solidworks.com/sw/support/edrawings/e2_register.htm).

The eDrawings software is a CAD design viewer for viewing and designing hardware blueprints on a professional level. The viewer has the ability to supply various methods of organising and viewing various types of designs. In addition, it allows for certain design parts to be saved as an STL file so that the user has the option to 3-D print the parts. Furthermore, the software has the ability to allow the user to add annotations and dimensions to out-of-date drawing views and attach these annotations and dimensions to the model geometry within the out-of-date views; thus adding a certain complexity to documenting blueprints.

# How To Install eDrawings:
--------------------------
Below is a step by step guide on how to properly install and use the software.


## Step 1: Installing The Files
---------
Once you have found the download page for eDrawings, select eDrawings viewer only and eDrawings publisher by Solidworks. Then, once you have accepted the terms and conditions, download the installation file. After that, run the .exe file and you should see the following on screen:

![Step One](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/FirstStep.PNG)

Ensure that you select to install the software on the computer.


## Step 2: Avoid Serial Number
---------

Next, you will come across the Serial Number part of the installation process, do not fill this out. Simply select SOLIDWORKS under 3-D design and click next.

![Step Two](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/SecondStep.PNG)


## Step 3: Select Products
---------

The next window will show the Solidworks products that you can select for installation, in our case we only want the eDrawings product as we are simply viewing the CAD files in a read-only mode.

![Step Three](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/ThirdStep.PNG)


## Step 4: Installation And Download Locations
----------
On the next window, it will detail a summary of what is about to be set up. Under both the download options and installation location, ensure that youy select an appropriate location so that you know where the necessary files will go. It is recommended that you select your personal drive so you can guarentee that they wont be lost, however, this also depends on whether you are installing from your home computer.

![Step Four](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/ForthStep.PNG)

Once done, click download and install. You have the option to choose to be notified by Solidworks Customer Experience, but it is not required for set up.

![Step Five](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/FifthStep.PNG)




## Step 5: Run The Program
----------

Once installed, run the program and the window should look like this:

![Step Six](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/SixthStep.PNG)


To view a CAD file, click on File->Open to select a file from the hardware model folder to view.

![Open File](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/OpenFileStep.PNG)


The file will take a bit to load depending on the size and scope of the design, but once done you should be able to view something like this:

![Johnny 5](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/Johnny5.PNG)


## Step Six: Exploring The View Features
------------

Now that we have the software set up, you can now explore what eDrawings has to offer. For starters, eDrawings allows you to break down the design model in three different ways. First off is the explode view, which is only available to designs that have complex enough parts to it. Hover the cursor down to the tool bar below the design and select "Explode", this will result in the design being split into its seperate parts that build it as a whole:

![Explode Me](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/ExplodeView.PNG)

The Second view option is the section-off view, which allows for the user to explore the inner workings of the model either from a x-axis or y-axis point of view. In the tool bar, select "Section" and then click "XY Plane" of which will give us a front view of what the model looks like on the inside:

![Section](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/SectionView.PNG)

This view is quite versatile as it has such viewing options as "YZ Plane", "XZ Plane", "Face Plane", "Flip", and "Show Cap".

Finally, there is the move parts feature which allows you to simply drag parts off of the model to view theme as a seperate entity. Select "Move" in the tool bar so that the cursor will turn into a hand image. You will then be able to drag objects off of the model as you see fit:

![Move](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/MoveParts.PNG)


## Step Seven: Saving A Design As An STL File
--------------

Now that we are familiar with the ins and outs of eDrawings, you should be able to start saving certain files as an STL format for 3D printing. It should be noted that only certain parts from the johnny 5 hardware model can be 3D printed, as the dremel cannot open an STL file that is either too complex or was not converted correctly. You should only save designs as STL IF the part is being viewed by itself (i.e. there is no explode view option)

Open a CAD file that includes a single part, for example, the head shell, then select File->Save As.

![Heads Up](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/HeadDesign.PNG)

Be sure to save it as an STL format and select an appropriate location for all your custom saved 3D files. You will want to save your own 3D files as this will make it easier to scale the designs to your choosing during the 3D set up process.

The saved STL will then look something like this:

![STL](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/STLHead.PNG)


Follow this guide from steps 6-7 for the 3D version as well, as that version is fully 3D printable.


# Using The Dremel 3D Slicer
----------------------------

The Dremel 3D slicer is incredably useful in terms of customizing the size and scale of each 3D design, as although STL files will be saved with pre-set dimentions the Dremel slicer allows
 you to modify the scale of it within the software with ease. If you do not already have the Dremel slicing tool installed, follow the guide below for installation instructions, otherwise simply 
 read through step 3.
 
 
# Step 1: Installation
----------------------

First off, download the Dremel slicer installer from the following [link](https://digilab.dremel.com/3D-software).
Once done, follow the Dremel wizard installer until you get to this window:

![dremel](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/dremelStep.PNG)

It is recommended to select an appropriate location so that it is easy to find later on. The next window will ask for you to select a start menu
 location, this can be skipped as it will be added in by default.


# Step 2: Select Components
---------------------------

Next is selecting the proper components we wish to have added to the dremel slicer. As all our 3D models will be saced as STL files, we
 really only need the bare essentials.

![dream](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/dremelComponent.PNG)

Once the components have been selected, simply click the install button.


# Step 3: Using The Dremel Slicer
---------------------------------

Now that we have installed the slicer, open the program up so that you can see the following on your screen:

![buildA](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/build1.PNG)

It is crucial to pay close attention to the settings on the side, as they must match the appropriate settings on the Dremel that uses the same
 material (i.e. PLA must be set as the material if printing with PLA).
	
Next, got to File->Open to select a STL model to view in this case the master shell of the head. You will then see the model in the center of the build plate, of which will be scaled 
based on its original size:

![buildC](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/build3.PNG)
	
Seeing as we kind of want a relatively large scale Johnny 5 robot, we need to scale up the model to fit our needs. Select the model with the cursor and then go to the 
tool bar on the left to select "Scale".

![buildD](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/build4.PNG)
	
We will want to keep uniform and snap scaling selected as this will allow us to scale the model evenly across the x-y axis. Change one of the values to 40000% and hit enter, you should
 see the following as a result:

![buildE](https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/build5.PNG)

Use the box of the build plate as a guide, as any part of the model that is either red or greyed out with lines will not be printed.

Next we want to reduce the amount of time it takes to print the model, so start off by selecting the model and rotating it until it is flat like the example below.

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/build6.PNG" alt = "buildF" height = "637px" width = "773px">

This is so that there will be as little support structure needed as possible, as too much will result in affecting the general design of the print as pulling support off can be daunting
 depending on what material has been used.
 
Finally, we need to adjust the print settings. Take note that unless you prioratize the file's settings on the Dremel printer, only the material, quality, and support will be noticed by the
printer. The quality should only be set to anything above medium if the design has a significant amount of detail, of which includes:

````
	Joints
	Screw Holes
	Articulated Features
	Drill Spaces
````

<img src= "https://gitlab.com/Callam7/johnny-5-project/-/raw/master/Project%202/SetUpImages/build7.PNG" alt = "buildG" height = "697px" width = "322px">

Unless prototyping or printing a particularly fragile part, support structure should always be set to "Touching The Plate" as we only wish to have the base of the print supported.

Once the print has been prepared, save it to a removeable drive or USB and begin printing.


# Step 4: Dremel Printer Settings
---------------------------------

Below is the settings I found to be best fitted for each material:

	PLA:
		Nozzle Temperature = 220 degrees
		Build Plate Temperature = 60 degrees
		Print Speed = 100%
	
	PA:
		Nozzle Temperature = 235 degrees
		Build Plate Temperature = 70 degrees
		Print Speed = 100%
	
	ABS:
		Nozzle Temperature = 240 degrees
		Build Plate Temperature = 70 degrees
		Print Speed = 120%

Note: All temperature settings should be within the recommended range shown on the filament roll and should not be exceeded.

	




 














