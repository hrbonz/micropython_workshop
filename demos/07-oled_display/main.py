"""
"""
from machine import Pin, SoftI2C

from ssd1306 import SSD1306_I2C

# look at the microcontroller schematic to find the pin numbers
# https://docs.micropython.org/en/latest/library/machine.I2C.html?highlight=softi2c#machine.SoftI2C
i2c = SoftI2C(sda=Pin(1), scl=Pin(0))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

oled.text("IoT workshop", 0, 0)
oled.text("09/03/2023 18:30", 0, 20)
oled.text("250 Tongren lu", 0, 30)
oled.text("FT data", 0, 50)

oled.show()
# stop the script by pressing ctrl-C in the shell
