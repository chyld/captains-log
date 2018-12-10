#include "HTS221Sensor.h"

DevI2C *i2c;
HTS221Sensor *sensor;
float humidity = 0;
float temperature = 0;
unsigned char id;

void setup()
{
  i2c = new DevI2C(D14, D15);
  sensor = new HTS221Sensor(*i2c);
  sensor->init(NULL);
}

void loop()
{
  sensor->enable();

  sensor->readId(&id);
  sensor->getHumidity(&humidity);
  sensor->getTemperature(&temperature);

  sensor->disable();
  sensor->reset();

  Serial.println(id);
  Serial.println(temperature);
  Serial.println(humidity);

  delay(1000);
}
