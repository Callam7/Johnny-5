/*Modified By: Callam Josef Jackson-Sem
	Project: Johnny 5 Robot
  Purpose Of File: Testing Communication between OpenCv Python Code, Servos, And Raspberry Pi
	Description: This File is being used to help combine all components for the head into one working module.
    It makes use of the voiceBox, servos, OpenCV, WebCamera, and rasbperry pi controller.
*/
#include<Servo.h> //include the Servo.h library so that any command or function to do with the servo can be used.

//SD Card Libraries need to run Johnny 5's voiceBox files
#include <pcmConfig.h>
#include <pcmRF.h>
#include <TMRpcm.h>

#include "SD.h"
#define SD_ChipSelectPin 10 //this is the pin needed for the speaker and the microSD shield to
//communicate with each other

#include "TMRpcm.h"
#include "SPI.h"

TMRpcm tmrpcm;

Servo servoVer; //Vertical Servo
Servo servoHor; //Horizontal Servo

//int values are set to hold the current x and y-axis positions
int x; 
int y; 

//used to determine what was the previous x-axis and y-axis
int prevX; 
int prevY;

void setup() //sets up the pin positions and variables for use.
{
  while (!Serial);

  //the serial payload has been preset to the highest, as this slightly improves the quality of the output devices
  Serial.begin(115200);
  Serial.println("Arduino is alive!");

  servoVer.attach(4); //Attach Vertical Servo to Pin 4
  servoHor.attach(5); //Attach Horizontal Servo to Pin 5

  //assigns each servo to a pre-set position. Keep in mind that the servos only turn up to 180 degrees, any larger than that will
  //put strain on the gears.
  servoVer.write(90);
  servoHor.write(90);
}

//The pos function is in charge of mapping out how far the servos should be able to turn.
//The function is called once either X or Y is recognised from the OpenCv library.
void Pos()
{

  if(prevX != x || prevY != y) //prevY is being ignored by the code and the y-axis servo
  //for now, both servos respond to all variables that include the value of X (i.e. serial.read() == 'X', servoX, int x).
  {
    int servoX = map(x, 600, 0, 70, 179);
    //int servoY = map(y, 450, 0, 179, 95);
    servoX = min(servoX, 180);
    servoX = max(servoX, 70);
    //servoY = min(servoY, 180);
    //servoY = max(servoY, 70);
    
    //assigns servoX and Y to Vertical and Horizontal positions
    servoHor.write(servoX);
    servoVer.write(servoX);
  }
}

void loop()
{
  //reads out the string values grabbed from the xml files.
  String strRead;

//determines if the serial is available for use.
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'X')
    {
      //if the serial.Read equals an X value, then it will be parsed in as an int value.
      //depending on the value, the servo will attempt to shift to that position. 
      x = Serial.parseInt();
      strRead = Serial.readStringUntil('\r');
      Serial.println(strRead);
      Pos();

    if(Serial.read() == 'Y')
    {
      //if the serial.Read equals a Y value, then it will be parsed in as an int value.

      y = Serial.parseInt();
      strRead = Serial.readStringUntil('\r');
      Serial.println(strRead);
      Pos();
        
    }

    }

    while(Serial.available() > 0)
    {
      //runs a while loop that contiuiously reads out the values from the xml files.
      Serial.read();

    }
  }
}

