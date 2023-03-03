# DHT11 Temperature and Moisture sensor
# Script in MicroPython for Raspberry pi Pico W
# Script by: MrLunk
# https://github.com/mrlunk/

from machine import Pin
from dht import DHT11
import utime
pin = Pin(28, Pin.IN)
while True:
    utime.sleep(5)
    data_dht = DHT11(pin)
    data_dht.measure()
    temp =(data_dht.temperature())
    humidity = (data_dht.humidity())
    print (" temperature (C) :{}" .format(temp))
    print (" humidity (%): {} " .format(humidity))
