# -----------------------------------------------------------------------------
# https://www.youtube.com/watch?v=WSLSyBNua-4
# ESP32
# -----------------------------------------------------------------------------
from machine import Pin

led = Pin(5, Pin.OUT)
btn = Pin(0, Pin.IN)

while True:
    if btn() == 0:
        led.on()
    else:
        led.off()
# -----------------------------------------------------------------------------
# Interrupt
# from machine import Pin
# led = Pin(5, Pin.OUT)
# btn = Pin(o, Pin.IN)
#
# Intrrupt Request
# btn.irq(my_func)
#
# def my_func(pin):
#    if btn.value() == 0:   # active-low --> pressed
#        led.on()
#    else:
#        led.off()


