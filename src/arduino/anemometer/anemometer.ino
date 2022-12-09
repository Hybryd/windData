/*
  Test script for Arduino-RPI USB communication
*/

int cpt = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("Test ");
  Serial.println(cpt);
  
  ++cpt;
  
  if(cpt > 10)
    cpt=0;
    
  delay(1000);
}
