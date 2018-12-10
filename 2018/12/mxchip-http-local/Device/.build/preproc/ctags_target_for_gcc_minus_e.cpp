# 1 "/home/chyld/Code/captains-log/2018/12/mxchip-http-local/Device/device.ino"
# 1 "/home/chyld/Code/captains-log/2018/12/mxchip-http-local/Device/device.ino"
# 2 "/home/chyld/Code/captains-log/2018/12/mxchip-http-local/Device/device.ino" 2
# 3 "/home/chyld/Code/captains-log/2018/12/mxchip-http-local/Device/device.ino" 2

// is scoped to local file only
static bool hasWifi = false;

void setup()
{
  char intro[] = "HTTP Demo";
  Screen.print(0, intro);
  Serial.println(intro);

  if (WiFi.begin() == WL_CONNECTED)
  {
    hasWifi = true;
    Screen.print(1, "Yes Wi-Fi");
    IPAddress ip = WiFi.localIP();
    long rssi = WiFi.RSSI();
    Serial.println(ip);
    Serial.printf("Signal Strength: %d \r\n", rssi);
  }
  else
  {
    hasWifi = false;
    Screen.print(1, "No Wi-Fi");
  }
}

void loop()
{
  delay(2000);
}
