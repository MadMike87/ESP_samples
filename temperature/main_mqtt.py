import machine, onewire, ds18x20, time

ds_pin = machine.Pin(4)  # we are reading the temperature from GPIO 4
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

getsensors = ds_sensor.scan()  # the scan() function retrieve all connected DS18B20 sensor addresses
print('Found DS18B20 Sensors: ', getsensors)

while True:  # while loop that gets the temperature 5 seconds
    ds_sensor.convert_temp()  # You need to call convert_temp() each time you want the temperature
    time.sleep_ms(750)  # Add a delay of 750 ms to give enough time to convert the temperature
    for sensor in getsensors:
        print(sensor)
        print(ds_sensor.read_temp(sensor))
    time.sleep(5)


##########################################################################
### https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
##########################################################################
###  publish and receive the messages
def sub_cb(topic, msg):
    ### The first thing is creating a callback function that will run
    ### whenever a message is published on a topic the ESP is subscribed to.
    ### The callback function should accept as parameters the topic and the message
    ### In our callback function, we start by printing the topic and the message.
    ### then we check if the message was published on the '/Haus/OG/Office/Keypad/feedback'
    ### topic, and if the content of the message is ‘received’.
    ### If this if statement is True, it means that ESP received the message sent
    ### from FHEM-server.
    print((topic, msg))
    if topic == b'/Haus/OG/Office/Keypad/feedback' and msg == b'received':
        print('ESP received message from FHEM-server')


def connect_and_subscribe():
    ### This function is responsible for connecting to the broker as well as
    ### to subscribe to a topic
    ###
    ### Start by declaring the client_id, mqtt_server and topic_sub variables
    ### as global variables.
    ### This way, we can access these variables throughout the code.
    global client_id, mqtt_server, topic_sub
    ### Then, create a MQTTClient object called client.
    ### We need to pass as parameters the cliend_id, and IP of mqtt_server
    ### These variables were set on the boot.py file.
    client = MQTTClient(client_id, mqtt_server)
    ### Afterwards  set the callback function to the client (sub_cb)
    client.set_callback(sub_cb)
    ### Next, connect the client to the broker using the connect() method
    ### on the MQTTClient object
    client.connect()
    ### After connecting, we subscribe to the topic_sub topic.
    ### Set the topic_sub on the boot.py file ('/Haus/OG/Office/Keypad/feedback')
    client.subscribe(topic_sub)
    ### Finally, print a message and return the client
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client


def restart_and_reconnect():
    ### This function will be called in case the ESP fails to connect
    ### This function prints a message to inform that the connection was
    ### not successful, wait 10 seconds, then reset the ESP using
    ### the reset() method.
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()


### Receive and publish messages
### Until now, we’ve created functions to handle tasks related with the
### MQTT communication.
### From now on, the code will call those functions to make things happen.
### The first thing connect to MQTT broker and subscribe to a topic.
### So, we create a client by calling the connect_and_subscribe() function.

try:
    client = connect_and_subscribe()
except OSError as e:
    ### In case we’re not able to connect to MQTTT broker, we’ll restart
    ### the ESP by calling the restart_and_reconnect() function
    restart_and_reconnect()

while True:
    ### the while loop is where we’ll be receiving and publishing the messages.
    ### We use try and except statements to prevent the ESP from crashing
    ### in case something goes wrong!
    try:
        ### Inside the try block, we start check_msg() method on the client.
        ### The check_msg() method checks whether a pending message from
        ### the server is available. It waits for a single incoming MQTT message
        ### and process it. The subscribed messages are delivered to the
        ### callback function we’ve defined --> sub_cb() function
        ### If there isn’t a pending message, it returns with None.
        client.check_msg()
        ### We add an if statement to checker whether 15 seconds (message_interval)
        ### have passed since the last message was sent
        if (time.time() - last_message) > message_interval:
            ### If it is time to send a new message, we create a msg variable
            ### with the “Hello WPL” text followed by a counter.
            msg = b'Hello WPL #%d' % counter
            ### To publish a message  we need to apply the publish() method on
            ### the client and pass as arguments, the topic and the message.
            ### The topic_pub variable was set to '/Haus/OG/Office/Keypad'
            ### in boot.py
            client.publish(topic_pub, msg)
            ### After sending the message, we update the last time a message
            ### was received by setting the last_message variable to the current time.
            last_message = time.time()
            ### Finally, we increase the counter variable in every loop.
            counter += 1
    ### If something unexpected happens, call restart_and_reconnect() function.
    except OSError as e:
        restart_and_reconnect()