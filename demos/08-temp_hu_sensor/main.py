import dht
import ds18x20
from machine import Pin
import onewire
import time

# look at the microcontroller schematic to find the pin numbers
# https://docs.micropython.org/en/latest/esp32/quickref.html#onewire-driver
# https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver
ow = onewire.OneWire(Pin(5))
black = ds18x20.DS18X20(ow)
blue = dht.DHT11(Pin(10))

rom = black.scan()
black.convert_temp()
temp = black.read_temp(rom[0])
print("Black sensor (DS18B20)")
print(str('%.2f' % temp) + ' C')

time.sleep(2)
blue.measure()
print("Blue sensor (DH11)")
print(str(blue.temperature()) + ' C')
print(str(blue.humidity()) + ' RH%')
# stop the script by pressing ctrl-C in the shell
