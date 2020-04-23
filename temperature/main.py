import machine, onewire, ds18x20, time

ds_pin = machine.Pin(4)  # we are reading the temperature from GPIO 4
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

getsensors = ds_sensor.scan()  # the scan() function retrieve all connected DS18B20 sensor addresses
print('Found DS18B20 Sensors: ', getsensors)

while True:  # while loop that gets the temperature 5 seconds
    ds_sensor.convert_temp()  # You need to call convert_temp() each time you want the temperature
    time.sleep_ms(750)  # Add a delay of 750 ms to give enough time to convert the temperature
    for sensor in getsensors:
        temp = ds_sensor.read_temp(sensor)
        print(temp)
    time.sleep(5)
