##########################################################################
### https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
### WPL 13.02.2020
##########################################################################

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(0.5)

