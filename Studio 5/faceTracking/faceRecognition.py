##Modified By: Callam Josef Jackson-Sem

##Project: Johnny 5 Robot

##Purpose Of File: To Identify And Track Multiple Faces Using OpenCv Libraries

##Description: This file is implementing the full scope of the facial recognition feature of the OpenCV library.
## It is identifying a set value of faces and tracking their eyes, face shape, and whether or not the subject is smiling.
## The values of the faces will be then printed out in the IDLE serial port showing each face's location on a x and y axis.


import numpy as np #numpy is imported as np in order to implement and manipulate the face tracking library tools 
import sys #the sys module must always be imported in python in order to provide information about various
# constants, functions, and methods.
import cv2 #cv2 is the module needed to access the OpenCV library and its various tools.

# The xml files are assigned to a cascade identifier to reference their xy values as data strings.
# These files must be kept in the same directory as the .py file in order for the code to locate them correctly.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

#cap is established as a cv2 object for VideoCapture. The number value in the brackets is the ID of that object.
# This is so that if we are using one color frame and one greyscale frame, the code can distinguish between the two using their IDs.
cap = cv2.VideoCapture(0)

while 1: #a while loop is established, then runs if the face values are 1.
    ret, frame = cap.read() #ret and frame variables are assigned to the cap.read() function
    cv2.resizeWindow('frame', 500,500) #creates the dimentions of the window for the camera to open in.
    cv2.circle(frame, (250, 250), 5, (255, 255, 255), -1) #creates a circle object 
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # the color variable is set up as Gray for now.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # the faces variable is established with a color scheme, ratio, and how many
    # faces the program can read on screen. The face value MUST be established or the program will crash after more than one face is on screen.


    for (x,y,w,h) in faces: #loops through the four xml values found in faces
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 3) #rectangle object is drawn to capture the face shape
        #the roi values are assigned with the xml values to establish proper RGB color capture.
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(roi_gray, 1.5) #assigns the eye cascade variable with multiscale and ratio of 1.5

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        smile = smileCascade.detectMultiScale(roi_gray, 1.5)

        for (xx, yy, ww, hh) in smile:
            cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 255, 0), 2)

        # the code below assigns each xml value with a string object or variable in order for them to
        #be printed as readable data to the python IDLE serial.
        arr = {y:y+h, x:x+w}
        print (arr)
        
        print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))

        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2

        print (xx)
        print (yy)

        center = (xx,yy)

        print("Center of Rectangle is :", center)
        data = "X{0:1}Y{1:1}Z".format(xx, yy)
        print ("output = '" +data+ "'")
    

    cv2.imshow('Camera', frame) #the imshow object opens a window that displays the camera feed, so that users can see how the values are
    #being captured. You can add in as many imshow objects as there are VideoCapture objects.

    #Establishes a kill switch to close the camera window. In this case, it is the escape key.
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
#once the program finishes, the capture is released and all camera objects are destroyed.
cap.release()
cv2.destroyAllWindows()


