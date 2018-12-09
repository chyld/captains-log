#include "AZ3166WiFi.h"
#include "RGB_LED.h"

void setup()
{
  char intro[] = "LED Demo";
  Screen.init();
  Screen.print(0, intro);
  Serial.println(intro);
}

RGB_LED led;

void loop()
{
  for (int i = 0; i < 10; i++)
  {
    int r = random(256);
    int g = random(256);
    int b = random(256);
    Serial.printf("r: %d g: %d b: %d", r, g, b);
    Serial.println();
    led.setColor(r, g, b);
    delay(500);
  }

  led.turnOff();
  delay(1000);
}
