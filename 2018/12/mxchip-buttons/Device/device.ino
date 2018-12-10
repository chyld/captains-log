#include "AZ3166WiFi.h"
#include "RGB_LED.h"

RGB_LED led;

void setup()
{
  char intro[] = "Button Demo";
  Screen.init();
  Screen.print(0, intro);
  Serial.println(intro);
  led.setColor(0, 0, 255);
}

void loop()
{
  int a = digitalRead(USER_BUTTON_A);
  int b = digitalRead(USER_BUTTON_B);
  Serial.printf("a: %d b: %d \r\n", a, b);
  delay(1000);
}
