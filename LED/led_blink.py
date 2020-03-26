# ----------------------------------------------------
# https://www.youtube.com/watch?v=Mku1Bq78nXw
# MicroPython #4 - PWM, ADC, Timers & Interrupts
# ----------------------------------------------------
from machine import Pin, PWM, Timer
from time import sleep

print('\n')


# Helper function to print padded formated data
def print_formatted(d1, d2, d3, d4, cr):
    # cr carriage return is true or false
    # will this include a new line at the start
    new_line = "\n" if cr else ""  # new_line \n if cr is true otherwise ""
    print("{}{:22}   {:>5}   {:>9} {}".format(new_line, d1, d2, d3, d4))


# print the heading
print_formatted("AA Level", "QTY", "Tiny", "", True)  # True --> cr carriage return
print_formatted("----------------------", "-----", "---------", "", False)  # False --> no cr carriage return

# -----------------------------------
s = 'Hello there, how cool is MicroPython!'
i = s.index('cool')
print(s, '\n')
print('At which position is "cool": ', i, '\n')
# -----------------------------------
d = {1: "042", 2: "042 LED RED", 6: "APA102", 10: "CP2104"}
print(d)
print('dictionaries: ', d[2], '\n')

print_formatted(d[2], d[2], i, d[2], False)


for i in d.values():
    print(i)

print('\n')

for i in d.keys():
    print(i)

print('\n')

for index, part in d.items():
    print("{} is in compartment {}".format(part, index))
    # --> {} is a placeholder
# -----------------------------------
# D0 = GPIO16
# D2 = GPIO4
# D4 = GPIO2
# -----------------------------------

GPIO_list = [2, 4, 16]

BLUE = Pin(16, Pin.OUT)  # create output pin on GPIO16
GREEN = Pin(4, Pin.OUT)  # create output pin on GPIO4
RED = Pin(2, Pin.OUT)  # create output pin on GPIO2


def flash_led(timer):
    GREEN.value(not GREEN.value())


# -----------------------------------
# PWM can be enabled on all pins except Pin(16).
# There is a single frequency for all channels,
# with range between 1 and 1000 (measured in Hz).
# The duty cycle is between 0 and 1023 inclusive.
# -----------------------------------

print('\n', 'all LEDs off')
BLUE.off()
GREEN.off()
RED.off()
sleep(5)

counter = 5
while counter > 0:
    print('LED BLUE --> O N\n')
    BLUE.on()
    GREEN.off()
    RED.off()
    sleep(3)
    print('LED GREEN --> O N\n')
    BLUE.off()
    GREEN.on()
    RED.off()
    sleep(3)
    print('LED RED --> O N\n')
    BLUE.off()
    GREEN.off()
    RED.on()
    sleep(3)
    counter -= 1

# pwm0 = PWM(Pin(0))      # create PWM object from a pin
# pwm0.freq()             # get current frequency
# pwm0.freq(1000)         # set frequency
# pwm0.duty()             # get current duty cycle
# pwm0.duty(200)          # set duty cycle
# pwm0.deinit()           # turn off PWM on the pin

RED_pwm = PWM(Pin(2), freq=1, duty=100)  # create and configure in one go

flash = Timer(0)  # hardware timer

flash_led(0)
sleep(3)
flash_led(0)
sleep(3)
flash.init(period=1000, mode=Timer.PERIODIC, callback=flash_led)
RED_pwm.deinit()

"""
# interrupt if you press btn1
from machine import PIN
btn1 = Pin(26, Pin.IN)
btn1.value()

def btn_pressed(pin):
    print(pin)

btn1.irq(trigger=Pin.IRQ_FALLING, handler=btn_pressed)
"""
