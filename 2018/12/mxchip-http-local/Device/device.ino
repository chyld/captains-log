#include "AZ3166WiFi.h"
#include "http_client.h"

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
  Serial.println("Sending HTTP Request");
  HTTPClient *httpClient = new HTTPClient(HTTP_GET, "http://192.168.1.35:3000/");
  const Http_Response *result = httpClient->send();

  if (result != NULL)
  {
    Serial.println("Request Body");
    Serial.println(result->body);
  }
  else
  {
    Serial.println("HTTP Error");
    Serial.println(httpClient->get_error());
  }

  delay(3000);
}
