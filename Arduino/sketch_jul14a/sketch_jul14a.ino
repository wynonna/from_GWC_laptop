// Robotics with the BOD Shield - ForwardThreeSeconds
// Make the BOE Shield-Bot roll forward for three seconds, then stop.

#include <Servo.h>

Servo servoLeft;
Servo servoRight;

void setup() {
  // put your setup code here, to run once:

// tone(4, 3000, 1000);
// delay(1000);
  
  servoLeft.attach(13);
  servoRight.attach(12);
}

void loop() {
  // put your main code here, to run repeatedly:
 // Full speed forward
  servoLeft.writeMicroseconds(1700); 
  servoRight.writeMicroseconds(1300); 
  delay(3000);

  servoLeft.detach();
  servoRight.detach();
}
