"""
"""
from machine import Pin
import time

# look at the microcontroller schematic to find the pin numbers
# create outpur pin on GPIO2 and set it to '0' (turn off LED)
led = Pin(2, Pin.OUT, value=0)
key = Pin(9, mode=Pin.IN, pull=Pin.PULL_UP)

def toggle_led(pin):
    val = (led.value() + 1) % 2
    led.value(val)

key.irq(toggle_led, Pin.IRQ_FALLING)
# stop the script by pressing ctrl-C in the shell
