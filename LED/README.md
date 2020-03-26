# MicroPython
## Getting the firmware
       http://micropython.org/download#esp8266

- For best results it is recommended to first erase the entire flash
   of your device before putting on new MicroPython firmware.

   - pip3 install esptool
   - erase the flash:
      
           esptool.py --port /dev/ttyUSB0 erase_flash

   - deploy the new firmware using:
   
           esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect 0 esp8266-20191220-v1.12.bin
           
           daily image:
           esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect 0 /home/nuc8/01_smarthome/06_mcu/01_Micropython/esp8266-20200213-v1.12-167-gf020eac6a.bin

   - Serial monitor (STRG-D --> soft reboot --> REPL-mode):
   
           picocom /dev/ttyUSB0 -b 115200
              
           import os
           os.listdir()
           x=open('boot.py','r')
           x.read()
           
           os.chdir('01_smarthome')
           os.listdir()

           from machine import Pin
           led=Pin(2, Pin.OUT)
           led.off()
           led.on()
### end
