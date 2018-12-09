#include <Arduino.h>
#line 1 "/home/chyld/Code/captains-log/2018/12/mxchip-screen-serial/Device/device.ino"
#line 1 "/home/chyld/Code/captains-log/2018/12/mxchip-screen-serial/Device/device.ino"
#include "AZ3166WiFi.h"

#line 3 "/home/chyld/Code/captains-log/2018/12/mxchip-screen-serial/Device/device.ino"
void setup();
#line 12 "/home/chyld/Code/captains-log/2018/12/mxchip-screen-serial/Device/device.ino"
void loop();
#line 3 "/home/chyld/Code/captains-log/2018/12/mxchip-screen-serial/Device/device.ino"
void setup()
{
  // initialize screen
  Screen.init();
  Screen.print(0, "Screen Initilization");
}

int i = 0;

void loop()
{
  // create a message
  char message[100];
  sprintf(message, "i: %d", i);
  i += 1;

  // send message to screen
  Screen.print(0, "Screen Serial");
  Screen.print(1, message);
  delay(3000);
  Screen.clean();

  // send message to serial port
  Serial.println(message);
}

