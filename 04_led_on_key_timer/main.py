"""
"""
from machine import Pin
import time

# look at the microcontroller schematic to find the pin numbers
# create outpur pin on GPIO2 and set it to '0' (turn off LED)
led = Pin(2, Pin.OUT, value=0)
key = Pin(9, mode=Pin.IN, pull=Pin.PULL_UP)

# start an infinite loop
while True:
    time.sleep_ms(10)
    # when key is pressed, the pin goes to low level
    if key.value() == 0:
        led.value(1)
        while key.value() == 0:
            pass
        led.value(0)

# stop the script by pressing ctrl-C in the shell
