/*Modified By: Callam Josef Jackson-Sem
	Project: Johnny 5 Robot
  Purpose Of File: Having servos simulate eye tracking via the use of infrared sensors.
	Description: This File was to be used as the main drivinbg mechanism for the robot's head via the use of infrared sensors. The sensors
  would then follow the white of the eye's iris, where the value of the eye would move the servo based on its value.
*/



#include <Servo.h>          //include the servo library
int servoPosition;         //the servo will move to this position
Servo myservo;              //create a servo object

int QRE1113_Pin = A2; 
void setup()
{
  myservo.attach(9);        //tell the servo object that its servo is plugged into pin 9
  pinMode(A2, INPUT);
  Serial.begin(9600);
}
 
void loop()
{
  int QRE_Value = analogRead(QRE1113_Pin);  

  servoPosition = map(0, 20, 40, 60, 160);

  if(analogRead(QRE1113_Pin) > 600)
  {
    myservo.writeMicroseconds(1700);
    myservo.write(1700);
    delay(30);

  }

  else if(analogRead(QRE1113_Pin) < 600)
  {
    myservo.writeMicroseconds(1300);
    myservo.write(1300);
    delay(30);

  }
  Serial.println(QRE_Value);
  delay(200);
}
