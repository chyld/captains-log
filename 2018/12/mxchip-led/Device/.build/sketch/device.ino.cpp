#include <Arduino.h>
#line 1 "/home/chyld/Code/captains-log/2018/12/mxchip-led/Device/device.ino"
#line 1 "/home/chyld/Code/captains-log/2018/12/mxchip-led/Device/device.ino"
#include "AZ3166WiFi.h"
#include "RGB_LED.h"

#line 4 "/home/chyld/Code/captains-log/2018/12/mxchip-led/Device/device.ino"
void setup();
#line 14 "/home/chyld/Code/captains-log/2018/12/mxchip-led/Device/device.ino"
void loop();
#line 4 "/home/chyld/Code/captains-log/2018/12/mxchip-led/Device/device.ino"
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

