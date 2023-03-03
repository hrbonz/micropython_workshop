from machine import Pin
from neopixel import NeoPixel
import time


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

# look at the microcontroller schematic to find the pin numbers
rgb = Pin(8, Pin.OUT)
np = NeoPixel(rgb, 1)

try:
    while True:
        np[0] = RED
        np.write()
        time.sleep(2)

        np.write()
        np[0] = GREEN
        np.write()
        time.sleep(2)

        np[0] = BLUE
        np.write()
        time.sleep(2)

except KeyboardInterrupt:
    # turn LED off
    np[0] = OFF
    np.write()

# stop the script by pressing ctrl-C in the shell
