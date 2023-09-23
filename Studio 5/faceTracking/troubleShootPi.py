##Modified By: Callam Josef Jackson-Sem
##Project: Johnny 5 Robot
##Purpose Of File: To Test The Integrity Of The Python-Arduino Connection
##Description: This file is being used to ensure that there is a connection between the Python-IDLE and
## the Arduino Serial. It is used as a troubleshooting tool in case the Arduino fails to recieve any xml output from
## the Python IDLE.

#Serial is import so that we can communicate with the Arudino via sending and recieving messages.
import serial
#The string is imported for the use of impliementing string or char values.
import string
import sys

output = " "
#The ser variable is establishing the Arduino connection. The dev may need to be edited based on what USB port is being used
#by the Arduino
ser = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)
ser.write(('Are you alive?').encode('utf-8')) #Writes a message to the Arduino Serial. The string must first be encoded
#into utf-8 format in order for the Serial to be read.

while True:
    while output != "":
        #if the output does not equal a string, the while loop will try to read and split the lines into
        # a temp printed variable.
        output = ser.readline()
        temp = output.split()
        try:
            print (temp[0])
        except:
            #if the output does equal a string, however, then the loop will pass the arguement value.
            pass
        output = " "
        ser.write(('Go on...convince me').encode('utf-8'))
