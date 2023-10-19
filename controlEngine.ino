#include <Servo.h>

Servo servoX; // Servo object for movement in the X-axis

Servo servoY; // Servo object for movement in the Y-axis

Servo servoZ; // Servo object for movement in the Z-axis

int xPosition = 90; // Initial position in the X-axis (0 to 180 degrees)

int yPosition = 90; // Initial position in the Y-axis (0 to 180 degrees)

int zPosition = 90; // Initial position in the Z-axis (0 to 180 degrees)

void setup()
{

  Serial.begin(9600); // Start serial communication

  servoX.attach(9); // Attach servo to pin 9

  servoY.attach(10); // Attach servo to pin 10

  servoZ.attach(11); // Attach servo to pin 11
}

void loop()
{

  if (Serial.available() > 0)
  {

    char command = Serial.read(); // Read the command from the serial monitor

    // X-axis control

    if (command == 'x')
    {

      xPosition = constrain(xPosition + 10, 0, 180); // Increase X position by 10 degrees

      servoX.write(xPosition);
    }
    else if (command == 'X')
    {

      xPosition = constrain(xPosition - 10, 0, 180); // Decrease X position by 10 degrees

      servoX.write(xPosition);
    }

    // Y-axis control

    if (command == 'y')
    {

      yPosition = constrain(yPosition + 10, 0, 180); // Increase Y position by 10 degrees

      servoY.write(yPosition);
    }
    else if (command == 'Y')
    {

      yPosition = constrain(yPosition - 10, 0, 180); // Decrease Y position by 10 degrees

      servoY.write(yPosition);
    }

    // Z-axis control

    if (command == 'z')
    {

      zPosition = constrain(zPosition + 10, 0, 180); // Increase Z position by 10 degrees

      servoZ.write(zPosition);
    }
    else if (command == 'Z')
    {

      zPosition = constrain(zPosition - 10, 0, 180); // Decrease Z position by 10 degrees

      servoZ.write(zPosition);
    }
  }
}
