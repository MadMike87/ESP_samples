# Complete project details at https://RandomNerdTutorials.com

try:
    import usocket as socket
except:
    import socket

import network

### The esp module contains specific functions related to both the ESP8266
### and ESP32 modules. Some functions are only available on one or the other
### of these ports.
import esp

### set the debug to None, turn off vendor O/S debugging messages
### esp.osdebug(0) --> redirect vendor O/S debugging messages to UART(0)
esp.osdebug(None)

import gc
# activate the garbage collector interface¶
gc.collect()

# ------ prepare WLAN ssid, password ----- #
ssid = "Aruba_HPE_WLAN"
password = "Werner_Plessl_AP303"


def do_connect():
    # ------ WLAN station interface STA_IF-------------------------- #
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('\n \t connecting to network...\n')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print('\n \t try connecting to network...\n')
    print('\n \t network config: ', wlan.ifconfig())


do_connect()
