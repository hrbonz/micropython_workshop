"""
"""
from machine import Pin
import time

# look at the microcontroller schematic to find the pin number
led = Pin(2, Pin.OUT)

# start an infinite loop
while True:
    led.value(1)
    time.sleep_ms(500)
    led.value(0)
    time.sleep_ms(500)

# stop the script by pressing ctrl-C in the shell