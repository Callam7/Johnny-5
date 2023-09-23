# Hardware Blueprint Notes
--------------------------
Due to the large size of the files, I cannot upload all the CAD files to Github. However, the full files can be found either on my gitlab under the same name or through the original site linked below.

The following details what is actually finished and what cannot be currently reproduced into a working module,
for more information about the general design and structure of the hardware module type, please visit the INput Inc website
https://input-inc.com/


# INPUT-INC PROJECT J5 CAD
2020-01-01

# GENERAL NOTES:

Due to the long filenames, extract the CAD to the root of one of your drives (ex. C:\, D:\, E:\, etc). Otherwise you may get a 255 character limit error from Windows.

We highly recommend SolidWorks 2015 or newer. We cannot guarantee these files will open correctly in other programs such as Fusion 360 or Inventor as we have very little experience with them. Most of the assemblies have the ability to move - this is an absolutely vital function to understand how the robot operates. Also, the majority of the hardware, some of the electronics, and other parts have had descriptions and PART NUMBERS for ordering/sourcing added to their File Properties, which as far as we know is only viewable in SolidWorks. Everything you need is in SolidWorks.

Some assemblies/parts are not in the "Full" assemblies. For example, the Arm Coverings, Wrist, Tool Arm, and Toolbox are not in any large assembly, but are still included in this release. Browse the folders.

The larger assemblies WILL bring your computer to it's knees. There are over 6000 parts in our Johnny Five: over 3500 in his Lower Half, and over 2500 in his Upper Half.

Many assemblies have been reworked from the ground up; there are major over-arcing changes that all play into each other. Think of a butterfly effect, so-to-speak. The entire Cradle Base is significantly different, as the 2013 one did not have a proper parallelogram. As such, the 2013 Cradle Base will most likely not work with the new A-Frames, Eccentric Drive, and other subassemblies. BE AWARE if you already started your build (which we said time and time again ad nauseam you shouldn't), you will have to throw away a lot of your previous work. Even his eyebrows have changed, now having a more accurate shape!

The Head has been completely reworked. If you have already built one, we STRONGLY recommend this one, no matter how long it takes to print (did we mention not to make anything from the old CADs?). The new mechanisms will not work or fit the old Head. The overall shape and contours on the Head are 100% accurate now - this was at least a 6-month-long effort alone. There were numerous things visually wrong and outright incorrect with the 2013/2014 Head. Also, don't glue it together - it's meant to be modular for when it breaks/chips/is changed!

ALL coverings have changed and are significantly more accurate. Every single one. Many of these coverings will NOT fit anything from the 2013/2014 CADs without significant handiwork and butchering.

There have been many subtle changes to various mechanical parts, including the Track Drive Side Plates ("Boomerang Plates" as we call them). Inspect every single part and assembly or you will miss something small that will bite you later.

CHECK THE CONFIGURATIONS TAB! Many parts and assemblies have multiple versions under Configurations. As a rule of thumb, by default when you open a part my/our preferred version is shown, but oftentimes there are others "hidden" away. Also, should you try to open these files in another program, I do not believe you get ANY configurations aside from the one last open when it was saved.

Check the Resources folder for decals, renders, PDF documentation, hydraulic system information, paint information/color codes, and more.

Sharing your progress, design ideas, or improvements in our Facebook group is encouraged!

# ISSUES:
---------

Eye Tubes (part# HEAD-C-LEFT-COMN-00-L & HEAD-C-LEFT-COMN-00-R) are NOT SAFE to make. The blue vents that go inside them are unfinished, and thus if you machine this part from aluminum tube, you may make a costly mistake if we change it.

A number of parts of the Head Top Shell (parts in HEAD-A-B) will change VERY soon. There is currently no way to locate the nurnies atop the Head other than carefully measuring and placing them. Each individual nurnie will be receiving a small locating key on the bottom, and a corresponding keyhole for each one on the Head. However, I will call it SAFE to make as it still works and is the crown jewel of this new CAD.

Upper Torso Front Plate (part# TUPR-A-COMN-01) will be changing in the future. We modified all sheet metal assemblies to use angle iron, and I forgot to do that one. It is SAFE to go ahead and make that structure as-is, but it will be difficult to bend AND roll the sheet metal without specialized equipment.

The Electronics Carrier inside the Tool Arm (asy# TUPR-F-V2) will be changing in the future. There is currently no way to attach the Intel NUC, and the entire assembly is able to rotate freely about the Horizontal Rod (part# TUPR-F-COMN-01), which it definitely should not (this is a flaw of the original as well). It is NOT SAFE make that assembly.

Laser Master (part# ACC-LASR-MSTR-COMN-00) is not shelled out nor has any mechanisms inside. We simply didn't have time. It is SAFE to make, provided you shell it yourself as it is a completely solid model.

The mounting plates underneath the Laser (parts in ACC-LASR-MSTR-COMN-A) are entirely eyeballed to the best of my ability, as the Laser prop we own is a stunt version and not the hero. The stunt and hero versions differ greatly in their mounting systems. These various plates will most likely change in the future. I will call these aluminum plates as NOT SAFE.

Laser Vertical Support (asy# TUPR-E-LASR) will be changing in the future. The Hinge (part# TUPR-E-LASR-COMN-02) is not able to be used with a functioning, tilt-able Laser (it needs to be extended past the pivot hole). Thus the Hinge (part# TUPR-E-LASR-COMN-02) as currently designed is NOT SAFE to make other than for cosmetic purposes.

SKF Actuator Simulate (Laser Version) (part# TUPR-E-COVR-02-LASR) has two large counterbores in the side. These two holes are meant for M5 socket head cap screws - which are entirely cosmetic - in order to simulate the appearance of a real SKF actuator. These two screws are not present in the CAD because the access hole is larger than an M5, thus they would just fall out. I would call this part SAFE to make since it is 3D-printed and not terribly time-consuming to print if we adjust it on our end.

All of the coverings except for the Shoulder Coverings (part# ARM-A-COVR-00-L & ARM-A-COVR-00-R) do not have any method of attachment. We will be going with neodymium magnets. All coverings are SAFE to make, provided you find a way to attach them to your robot.

# MISSING ITEMS:
----------------

	Head - Blue Eye Vents (approx. 10% complete)
	Head - Eye Mechanisms, Lights, and Pop (approx. 75% complete)
	Head - Speaker (0% complete)
	Head - Mounting surface for the Lip Light Driver PCB (0% complete)
	Head - Military Headwear (80% complete)
	Upper Arm (approx. 50% complete)
	Lower Arm (approx. 50% complete)
	Hands (approx. 90% complete)
	Upper Torso Covering Nurnies (approx. 90% complete)
	Four of the five Tool Arm Coverings (approx. 75% complete)
	Laser Mechanisms (0% complete)
	Lower Torso Covering (approx. 25% complete)
	Upper A-Frame Kill Switch (0% complete)

Best Regards and Good Luck,
The Input-Inc Team
https://www.input-inc.com
https://www.facebook.com/inputinc/
https://www.facebook.com/groups/inputinc/