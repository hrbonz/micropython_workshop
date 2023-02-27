"""
"""
from machine import Pin

# look at the microcontroller schematic to find the pin number
led = Pin(2, Pin.OUT)
led.value(1)
# stop the script by pressing ctrl-C in the shell