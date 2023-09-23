/*Modified By: Callam Josef Jackson-Sem
	Project: Johnny 5 Robot
  Purpose Of File: Establishing A simulated voiceBox for the robot
	Description: This File is communicating with a flashed SD card to play sound files from the Short Circuit movies. Commands are used to play specific sounds through the serial command line.
*/

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
String command; //a string object called command is needed to assign a string to the command 
//variable.


void setup(){
  tmrpcm.speakerPin = 9;
  pinMode(10,OUTPUT);
  Serial.begin(9600);

  if (!SD.begin(SD_ChipSelectPin)) {
    Serial.println("SD fail");//if the SD card cannot be read, then this fail message will be 
    //printed
    return;
    }    

}

void loop()
{
  command = Serial.readStringUntil('\n'); //reads the string command until the next line is typed
  //into the serial command line.

  if(command == "hi Johnny"){
    tmrpcm.play("hello.wav");
    tmrpcm.setVolume(5);}
  
  if(command == "how are you feeling"){
    tmrpcm.play("fitFiddle.wav");
    tmrpcm.setVolume(5);}  
  
  if(command == "time to unplug"){
    tmrpcm.play("disassemble.wav");
    tmrpcm.setVolume(5);}  
  
  if(command == "you need anything"){
    tmrpcm.play("questions.wav");
    tmrpcm.setVolume(5);}  
    
  if(command == "sing me a song"){
    tmrpcm.play("humming.wav");
    tmrpcm.setVolume(5);}  
  
  if(command == "like my outfit"){
    tmrpcm.play("niceSoftware.wav");
    tmrpcm.setVolume(5);}  
  
  if(command == "the camera isnt working"){
    tmrpcm.play("ohSwear.wav");
    tmrpcm.setVolume(5);}  
  
  if(command == "Johnny wanna go somewhere"){
    tmrpcm.play("youGotIt.wav");
    tmrpcm.setVolume(5);}  
  
  if(command == "hey keep it down"){
    tmrpcm.play("noWay.wav");
    tmrpcm.setVolume(5);}  

}
