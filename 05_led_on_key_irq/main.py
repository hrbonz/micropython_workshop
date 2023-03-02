"""
"""
from machine import Pin
import time

# look at the microcontroller schematic to find the pin numbers
# create outpur pin on GPIO2 and set it to '0' (turn off LED)
led = Pin(2, Pin.OUT, value=0)
key = Pin(9, mode=Pin.IN, pull=Pin.PULL_UP)

def turn_on(pin):
  if pin.value() == 0:
      led.value(1)

key.irq(turn_on, Pin.IRQ_FALLING)

# stop the script by pressing ctrl-C in the shell
