from machine import Pin
import time

# look at the microcontroller schematic to find the pin numbers
relay = Pin(4, Pin.OUT, value=0)

relay.value(1)
time.sleep(5)
relay.value(0)
# stop the script by pressing ctrl-C in the shell
