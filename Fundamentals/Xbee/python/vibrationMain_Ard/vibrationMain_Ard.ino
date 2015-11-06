// Code pieces taken from 
// https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-7-reading-a-temperature-sensor

#include <ctype.h>
#include <stdlib.h>
#include <math.h>

const int sensorPin = A0;
const float baselineTemp = 20.0;
int count = 0;
bool handShakeSuccessful = 0;
char mode;

void setup() {
  Serial.begin(9600);

  
  while (handShakeSuccessful == 0) { 
        ComsHandShake();
    }
}

void loop() {

  // Get mode
  mode = GetMode();


  // Mode 'c': Collect Data
    if (mode == 'c') {        
        CollectData();
    }
  
}








/*
 * Function: ComsHandShake
 * -----------------------------------------
 * Establishes connection with Python script
 * 
 */
 
void ComsHandShake(void) {
    int cnt = 0;
    // Establish connection with Python script
    if (Serial.available() > 0) {
        if (Serial.read() == 123) {
            Serial.write(124);
            
            handShakeSuccessful = 1;
            //digitalWrite(handShakePin, HIGH);
              
        }
    }
    return;

}





/*
 * Function: GetMode
 * -------------------
 * Obtains mode from user (collect data, download data, etc)
 * 
 */

char GetMode(void) {

    int userMode, cnt = 0;
    
    while (1) 
    {
        if (Serial.available() > 0) 
        {
            userMode = Serial.read();
            if (userMode == 0) 
            {
                Serial.write(126);
                //digitalWrite(sendPin, LOW);
                //digitalWrite(collectPin, HIGH);
                
                return 'c';
            }
            else if (userMode == 1) 
            {
                Serial.write(127);
                //digitalWrite(sendPin, HIGH);
                //digitalWrite(collectPin, LOW);
                
                return 'd';
            }
            else 
            {       
                Serial.write(128);
            }
        }
    }
    
    return mode;
}





void CollectData(void){

  while (1)
  {
    Serial.write(analogRead(sensorPin));
 
    delay(15);
  }
}


float getVoltage(int pin) {
  return (analogRead(pin) * 0.004882814);
}
