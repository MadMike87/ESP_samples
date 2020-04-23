import network
from umqttsimple import MQTTClient
import ubinascii
import machine
import esp
import gc

esp.osdebug(None)
gc.collect()

ssid = "Aruba_HPE_WLAN"
password = "Werner_Plessl_AP303"
mqtt_server = '192.168.1.8'


### To create an MQTT client, we need to get the ESP unique ID
client_id = ubinascii.hexlify(machine.unique_id())


# topicname to publish
topic_pub = b'/Haus/EG/WZ/ESP8266'
topic_sub = b'/Haus/EG/WZ/ESP8266/Feedback'


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('\n \t connecting to network...\n')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print('\n \t try connecting to network...\n')
    print('\n \t network config: ', wlan.ifconfig())


do_connect()
