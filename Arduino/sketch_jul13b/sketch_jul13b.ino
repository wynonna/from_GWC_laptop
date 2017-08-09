void setup() {
  // put your set up code here, to run code: 
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly: 
  digitalWrite(13, HIGH);   
  delay(1000);              
  digitalWrite(13, LOW);
  delay(1000);  
  digitalWrite(12, HIGH);   
  delay(1000);              
  digitalWrite(12, LOW);
  delay(1000);            
}

// go to File
// Examples
// 0.1Basics
// Blink 
  // new window opens, where you need to Verify, Upload 
  // and then exit to original window --> this window

// Now Upload in this window
