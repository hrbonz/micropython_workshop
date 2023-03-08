"""
"""
from machine import Pin, PWM
import random
import time

# look at the microcontroller schematic to find the pin numbers
# create outpur pin on GPIO2 and set it to '0' (turn off LED)
buzz = PWM(Pin(8), freq=200, duty=512)
key = Pin(9, mode=Pin.IN, pull=Pin.PULL_UP)


def randbuzz(p):
    i = random.randrange(1, 15)
    buzz.freq(i * 100)

key.irq(trigger=Pin.IRQ_FALLING, handler=randbuzz)

try:
    while True:
        time.sleep_ms(100)
except KeyboardInterrupt:
    buzz.deinit()

# stop the script by pressing ctrl-C in the shell
