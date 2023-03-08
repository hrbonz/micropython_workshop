"""Upload modeul/mqtt.py to the board
"""
from machine import Pin, SoftI2C, Timer
from network import WLAN, STA_IF
import time

from mqtt import MQTTClient

IO_USER = "user"
IO_KEY = "key"
IO_FEED = "{}/feeds/ftdata".format(IO_USER)

WIFI_SSID = "ssid"
WIFI_PWD = "password"

# look at the microcontroller schematic to find the pin numbers
# create output pin on GPIO2 and set it to '0' (turn off LED)
led = Pin(2, Pin.OUT, value=0)

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
        wlan.connect(WIFI_SSID, WIFI_PWD)
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

    # create MQTT client instance
    mc = MQTTClient("iot", "io.adafruit.com", port=1883, user=IO_USER, password=IO_KEY)


    mc.connect()
    print("send MQTT message to {}".format(IO_FEED))
    mc.publish(IO_FEED, "hello world")
    mc.disconnect()

    wlan.disconnect()
    led.value(0)

# stop the script by pressing ctrl-C in the shell
except KeyboardInterrupt:
    wlan.disconnect()
    led.value(0)
