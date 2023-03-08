"""
"""
from machine import Pin, SoftI2C, Timer
from network import WLAN, STA_IF
import time

from ssd1306 import SSD1306_I2C

# look at the microcontroller schematic to find the pin numbers
# create output pin on GPIO2 and set it to '0' (turn off LED)
led = Pin(2, Pin.OUT, value=0)
i2c = SoftI2C(sda=Pin(1), scl=Pin(0))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

oled.fill(0)
oled.show()

# connect to WiFi as a station
wlan = WLAN(STA_IF)
# activate network interface
wlan.active(True)
# if we were previsouly connected, clean that up
wlan.disconnect()

start = time.time()
try:
    if not wlan.isconnected():
        print("Connecting...")
        wlan.connect("ftdata", "q1w2e3r4t5y6")
        while  not wlan.isconnected():
            led.value(1)
            time.sleep_ms(250)
            led.value(0)
            time.sleep_ms(250)
            # test if we've been trying for more than 20 seconds
            if time.time() - start > 20:
                print("Connection timeout")
                raise KeyboardInterrupt

    led.value(1)
    ifconfig = wlan.ifconfig()
    print("network: {}".format(ifconfig))

    oled.fill(0)
    oled.text("IP/Subnet/GW/DNS", 0, 0)
    oled.text(ifconfig[0], 0, 10)
    oled.text(ifconfig[1], 0, 20)
    oled.text(ifconfig[2], 0, 30)
    oled.text(ifconfig[3], 0, 40)
    oled.show()

# stop the script by pressing ctrl-C in the shell
except KeyboardInterrupt:
    wlan.disconnect()
    oled.fill(0)
    oled.show()
