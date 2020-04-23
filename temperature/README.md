# Send Temperature via MQTT to FHEM-Server
# main_mqtt_temp.py
        *) to use MQTT download from https://github.com/micropython/micropython-lib
        *) from directory "umqtt.simple/umqtt" rename simple.py to umqttsimple.py
        *) copy umqttsimple.py to ESP-device in root directory
           copy umqttsimple.py /pyboard/
        *) copy boot.py /pyboard/
        *) copy main_mqtt_temp.py /pyboard/main.py

### Serial monitor
        connect ESP via USB cable to PC       
        alias espdev='ls /dev/ttyU*'
        espdev --> /dev/ttyUSB0  --> ESP is connected to ttyUSB0

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
            954 Dec 31 1999  boot.py
            681 Dec 31 1999  main.py

            cat /pyboard/main.py
            
            repl --> STRG +D --> soft reboot --> start boot.py and main.py
            or
            import os
            os.listdir()

            os.chdir('umqtt.simple')    --> change direcory to umqtt.simple 

            os.remove('umqtt.simple')   --> delete direcory umqtt.simple

            os.remove('main.py')        --> delete file main.py
            
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


### MQTT
#### API reference
        https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
        
        rename simple.py file from directory umqtt.simple to umqttsimple.py
        and copy it to root  / directrory from ESP-device (its easiser to use)
        
        connect(...) -  Connect to a server. Returns True if this connection uses
                        persisten session stored on a server (this will be always False
                        if clean_session=True argument is used (default)).
        disconnect() -  Disconnect from a server, release resources
        publish() -     Publish a message
        subscribe() -   Subscribe to a topic
        set_callback()- Set callback for received subscription messages
        set_last_will() Set MQTT "last will" message. Should be called before connect()
        wait_msg() -    Wait for a server message. A subscription message will be delivered
                        to a callback set with set_callback(), any other messages will be
                        processed internally
        check_msg() -   Check if there's pending message from server
                        If yes, process the same way as wait_msg(), if not, return immediately
                        
        MQTT client with automatic reconnect
        There's a separate umqtt.robust module which builds on umqtt.simple and adds
        automatic reconnect support in case of network errors.
        Please see its documentation for further details.
### end