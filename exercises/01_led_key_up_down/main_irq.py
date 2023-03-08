"""
"""
from machine import Pin
import time

# look at the microcontroller schematic to find the pin numbers
# create outpur pin on GPIO2 and set it to '0' (turn off LED)
led = Pin(2, Pin.OUT, value=0)
key = Pin(9, mode=Pin.IN, pull=Pin.PULL_UP)

def led_btn(p):
  if key.value() == 1:
    led.value(0)
  else:
    led.value(1)

# trigger on both rising and falling
key.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=led_btn)
# stop the script by pressing ctrl-C in the shell
