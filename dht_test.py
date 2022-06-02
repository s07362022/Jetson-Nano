import sys

import Adafruit_DHT

import time
sensor=Adafruit_DHT.AM2302
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
def dht01():
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        time.sleep(2)
        return temperature, humidity
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)

