"""
"""
from machine import Pin, PWM
import time

# look at the microcontroller schematic to find the pin numbers
# for the buzz
# Make sure to place the yellow jumper between X4 & X5 to connect the buzzer to
# pin 8
# https://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation
buzz = PWM(Pin(8), freq=200, duty=512)

for i in range(1, 15):
  buzz.freq(i * 100)
  time.sleep_ms(500)

buzz.deinit()

# stop the script by pressing ctrl-C in the shell
