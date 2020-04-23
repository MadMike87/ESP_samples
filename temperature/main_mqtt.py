
from time import sleep

##########################################################################
# https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
##########################################################################
#  publish and receive the messages
def sub_cb(topic, msg):
    # The first thing is creating a callback function that will run
    # whenever a message is published on a topic the ESP is subscribed to.
    # The callback function should accept as parameters the topic and the message
    # In our callback function, we start by printing the topic and the message.
    # then we check if the message was published on the '/Haus/OG/Office/Keypad/feedback'
    # topic, and if the content of the message is ‘received’.
    # If this if statement is True, it means that ESP received the message sent
    # from FHEM-server.
    print((topic, msg))
    if topic == b'/Haus/EG/WZ/ESP8266/Feedback' and msg == b'received':
        print('ESP received message from FHEM-server')


def connect_and_subscribe():
    # This function is responsible for connecting to the broker as well as
    # to subscribe to a topic    #
    # Start by declaring the client_id, mqtt_server and topic_sub variables
    # as global variables.
    # This way, we can access these variables throughout the code.
    global client_id, mqtt_server, topic_sub
    # Then, create a MQTTClient object called client.
    # We need to pass as parameters the cliend_id, and IP of mqtt_server
    # These variables were set on the boot.py file.
    client = MQTTClient(client_id, mqtt_server)
    # Afterwards  set the callback function to the client (sub_cb)
    client.set_callback(sub_cb)
    # Next, connect the client to the broker using the connect() method
    # on the MQTTClient object
    client.connect()
    # After connecting, we subscribe to the topic_sub topic.
    # Set the topic_sub on the boot.py file ('/Haus/EG/WZ/ESP8266/Feedback')
    client.subscribe(topic_sub)
    # Finally, print a message and return the client
    print('Connected to %s MQTT broker' % (mqtt_server))
    return client


def restart_and_reconnect():
    # This function will be called in case the ESP fails to connect
    # This function prints a message to inform that the connection was
    # not successful, wait 10 seconds, then reset the ESP using
    # the reset() method.
    print('Failed to connect to MQTT broker. Reconnecting...')
    sleep(10)
    machine.reset()


# Receive and publish messages
# Until now, we’ve created functions to handle tasks related with the
# MQTT communication.
# From now on, the code will call those functions to make things happen.
# The first thing connect to MQTT broker and subscribe to a topic.
# So, we create a client by calling the connect_and_subscribe() function.

try:
    client = connect_and_subscribe()
except OSError as e:
    # In case we’re not able to connect to MQTTT broker, we’ll restart
    # the ESP by calling the restart_and_reconnect() function
    restart_and_reconnect()

msg = b'Hello FHEM-server'

while True:
    # the while loop is where we’ll be receiving and publishing the messages.
    # We use try and except statements to prevent the ESP from crashing
    # in case something goes wrong!
    try:
        # Inside the try block, we start check_msg() method on the client.
        # The check_msg() method checks whether a pending message from
        # the server is available. It waits for a single incoming MQTT message
        # and process it. The subscribed messages are delivered to the
        # callback function we’ve defined --> sub_cb() function
        # If there isn’t a pending message, it returns with None.
        client.check_msg()

        # To publish a message  we need to apply the publish() method on
        # the client and pass as arguments, the topic and the message.
        # The topic_pub variable was set to '/Haus/EG/WZ/ESP8266' in boot.py
        print('\npublish %s to MQTT-broker' % (msg))
        client.publish(topic_pub, msg)
        sleep(3)
    # If something unexpected happens, call restart_and_reconnect() function.
    except OSError as e:
        restart_and_reconnect()
