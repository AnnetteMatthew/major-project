int relayPin = 12;                // choose the pin for the Relay Pin


int inputPin1 = 2;                 // choose the input pin (for PIR sensor 1)
int inputPin2 = 3;               // choose the input pin (for PIR sensor 2)


int pirState = LOW;         // at start, assuming no motion detected
int val1 = 0;                     // variable for reading the status for pin 1
int val2 = 0;                    // variable for reading the status for pin 2
 
void setup() 
{
  pinMode(relayPin, OUTPUT);      // declare Relay as output
  pinMode(inputPin1, INPUT);         // declare sensor as input
  pinMode(inputPin2, INPUT);  
  Serial.begin(9600);
}
 
void loop()
{
  val1 = digitalRead(inputPin1);  // read input value
  val2 = digitalRead(inputPin2);  // read input value

  if (val1 == HIGH || val2 == HIGH)		// check if the input is HIGH
  {                
   digitalWrite(relayPin, HIGH);  // turn Relay ON
    	   if (pirState == LOW) 	     // turned on
          {
            Serial.println("Motion detected!");
      			delay(15000);				// 15 sec delay
      			pirState = HIGH;
    		  }
   }
   else 
   {
    	digitalWrite(relayPin, 0); // turn Relay OFF
    	if (pirState == HIGH)		 // turned off
      {
           	Serial.println("Motion ended!");
      			pirState = LOW;
    	}
   }
  
}
