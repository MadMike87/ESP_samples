import machine, onewire, ds18x20, time

ds_pin = machine.Pin(4)  # we are reading the temperature from GPIO 4
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()  # the scan() function retrieve the DS18B20 address
print('Found DS18B20 Sensors: ', roms)

while True: # while loop that gets the temperature 5 seconds
    ds_sensor.convert_temp()  # You need to call convert_temp() on the ds_sensor object each time you want to sample temperature.
    time.sleep_ms(750)  # Add a delay of 750 ms to give enough time to convert the temperature
    for rom in roms:
        print(rom)
        print(ds_sensor.read_temp(rom))
    time.sleep(5)
