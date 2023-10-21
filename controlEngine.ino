#include <Servo.h>

Servo servoX;
Servo servoY;
Servo servoZ;
int xPosition = 90;
int yPosition = 90;
int zPosition = 90;

void setup()
{
  Serial.begin(9600);
  servoX.attach(9);
  servoY.attach(10);
  servoZ.attach(11);
}

void loop()
{
  int deg = 2;
  if (Serial.available() > 0)
  {
    char command = Serial.read();
    if (command == 'x')
    {
      xPosition = constrain(xPosition + deg, 0, 180);
      servoX.write(xPosition);
    }
    else if (command == 'X')
    {
      xPosition = constrain(xPosition - deg, 0, 180);
      servoX.write(xPosition);
    }

    if (command == 'y')
    {
      yPosition = constrain(yPosition + deg, 0, 180);
      servoY.write(yPosition);
    }
    else if (command == 'Y')
    {
      yPosition = constrain(yPosition - deg, 0, 180);
      servoY.write(yPosition);
    }

    if (command == 'z')
    {
      zPosition = constrain(zPosition + deg, 0, 180);
      servoZ.write(zPosition);
    }
    else if (command == 'Z')
    {
      zPosition = constrain(zPosition - deg, 0, 180);
      servoZ.write(zPosition);
    }
  }
}
