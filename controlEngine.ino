#include <Servo.h>

Servo servoX;   // Servo object for movement in the X-axis
Servo servoY;   
Servo servoZ;   

int xPosition = 90;  // Initial position in the X-axis (0 to 180 degrees)
int yPosition = 90;  
int zPosition = 90;  

void setup()
{
  Serial.begin(9600);  // Start serial communication

  servoX.attach(9);  
  servoY.attach(10);  
  servoZ.attach(11);  
}

void loop()
{
  int deg = 2;  

  if (Serial.available() > 0)
  {
    char command = Serial.read();  // Read the command from the serial monitor

    // X-axis control
    if (command == 'x')
    {
      xPosition = constrain(xPosition + deg, 0, 180);  // Increase x position
      servoX.write(xPosition);
    }
    else if (command == 'X')
    {
      xPosition = constrain(xPosition - deg, 0, 180);  // Decrease X position 
      servoX.write(xPosition);
    }

    // Y-axis control
    if (command == 'y')
    {
      yPosition = constrain(yPosition + deg, 0, 180);  // Increase y position 
      servoY.write(yPosition);
    }
    else if (command == 'Y')
    {
      yPosition = constrain(yPosition - deg, 0, 180);  // Decrease Y position 
      servoY.write(yPosition);
    }

    // Z-axis control
    if (command == 'z')
    {
      zPosition = constrain(zPosition + deg, 0, 180);  // Increase z position 
      servoZ.write(zPosition);
    }
    else if (command == 'Z')
    {
      zPosition = constrain(zPosition - deg, 0, 180);  // Decrease Z position
      servoZ.write(zPosition);
    }
  }
}
