##Modified By: Callam Josef Jackson-Sem

##Project: Johnny 5 Robot

##Purpose Of File: To Send OpenCV face values to an arudino serial and simulate face tracking functionality in servos.

##Description: This is the primary OpenCV file that communicates the robot's head articulation movement. This is done by connecting
# to an arduino through a raspberry pi and sending the output xml values to the serial. These values will then print out in the serial
# and will be assigned to two servos that will respond based on the x y positions of the data sent.

#Note: The code is very similar to the faceRecognition file with the exception of using one xml file and it is sending data rather than just
#reading it to the IDLE serial.

import cv2 #imports the OpenCV library and its tools.
import numpy as np #import numpy in order to access the face tracking algorithm
import serial # imports serial so that a connection is established with the arduino
import sys #sys is the basic module needed for most if not all python code
import time #time is imported in case there is a need for a time.sleep function
import string # string imported so that xml values can be converted into string utf-8 format

arduino = serial.Serial('/dev/ttyUSB0', 115200, 8, 'N', 1, timeout=1) #arduino connection established by grabing its port directory, serial rate,
#bit rate, string, and timeout in case the connection is lost or interrupted.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #face cascade using the frontal_face xml file

cap = cv2.VideoCapture(0) #VideoCapture object created

while (True): #while loop runs if statement is true

    ret, frame = cap.read()
    cv2.resizeWindow('frame', 800, 800)
    cv2.circle(frame, (250, 250), 5, (255, 125, 255), -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w ,h) in faces:
        cv2.rectangle(frame,(x, y),(x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
    
            
        arr = {y:y+h, x:x+w}
        print(arr)
        
        print ('X :'+str(x))
        print('Y :' +str(y))
        print('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))
        
        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2
        
        print (xx)
        print (yy)
        
        center = (xx, yy)
        
        print("Center of Rectangle is :", center)
        data = "X{0:1}Y{1:1}Z".format(xx, yy)
        print ("output = '" +data+ "'")
        #the data is then encoded into utf-8 format so that the arduino serial can read the data correctly.
        arduino.write((data).encode('utf-8'))
        arduino.readline()

    cv2.imshow("Camera", frame)
    k= cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cap.destroyAllWindows()
