# LED blink
## ESP8266, ESP32
        connect ESP via USB cable to PC       
        alias espdev='ls /dev/ttyU*'
        espdev --> /dev/ttyUSB0  --> ESP is connected to ttyUSB0

### Serial monitor
        alias espsh='rshell --buffer-size=30 -p /dev/ttyUSB0 -a -e nano'
        espsh
            Using buffer-size of 30
            Connecting to /dev/ttyUSB0 (buffer-size 30)...
            Trying to connect to REPL  connected
            Testing if ubinascii.unhexlify exists ... Y
            Retrieving root directories ... /boot.py/ /main.py/
            Setting time ... Apr 22, 2020 12:10:06
            Evaluating board_name ... pyboard
            Retrieving time epoch ... Jan 01, 2000
            Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
            
            ls -al /pyboard
            954 Dec 31 1999  a.py
            681 Dec 31 1999  led_blink.py

            cat /pyboard/main.py
            
            repl --> STRG +D --> soft reboot --> start boot.py and main.py
            import led_blink
            
            or
            
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

        or
           
        picocom /dev/ttyUSB0 -b 115200
        --> cancel session press STRG + A + X  --> Thanks for using picocom


### end