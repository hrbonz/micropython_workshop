from machine import Pin
from neopixel import NeoPixel
import time

import rainbow

rgb =  Pin(4, Pin.OUT)
np = NeoPixel(rgb, 64)
#np = NeoPixel(rgb, 30)



rainbow.set_all(np, (0, 32, 32))
time.sleep(1)
rainbow.clear_all(np)

rainbow.walk(np, (128, 32, 64), 25)
rainbow.walk_bounce(np, (64, 0, 64), 25)
rainbow.fill(np, (64, 64, 0), 25)
rainbow.clear_all(np)
rainbow.fill_bounce(np, (16, 64, 32), 25)
rainbow.clear_all(np)

#for i in range(8):
#    rainbow.hline(np, (32, 0, 32), i)
#    time.sleep_ms(50)
#    rainbow.clear_all(np)

#for i in range(8):
#    rainbow.vline(np, (32, 0, 32), i)
#    time.sleep_ms(50)
#    rainbow.clear_all(np)

for k in range(0, 360 * 2, 10):
    for i in range(np.n):
        # divide 360 in steps based on the number of LEDs so all colors fit in
        # the strip
        angle = int(k + i * 360 / np.n)
        rainbow.sine_dot(np, i, angle , .1)

    time.sleep_ms(5)

rainbow.clear_all(np)

for k in range(0, 360 * 2, 10):
    for i in range(np.n):
        # direct angle
        angle = k
        rainbow.sine_dot(np, i, angle, .1, invert=True)

    time.sleep_ms(5)

rainbow.clear_all(np)
