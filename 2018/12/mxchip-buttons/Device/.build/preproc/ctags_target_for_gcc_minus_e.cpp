# 1 "/home/chyld/Code/captains-log/2018/12/mxchip-buttons/Device/device.ino"
# 1 "/home/chyld/Code/captains-log/2018/12/mxchip-buttons/Device/device.ino"
# 2 "/home/chyld/Code/captains-log/2018/12/mxchip-buttons/Device/device.ino" 2
# 3 "/home/chyld/Code/captains-log/2018/12/mxchip-buttons/Device/device.ino" 2

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
