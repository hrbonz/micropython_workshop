import dht
from machine import Pin, SoftI2C, Timer

from ssd1306 import SSD1306_I2C


# look at the microcontroller schematic to find the pin numbers
# https://docs.micropython.org/en/latest/esp32/quickref.html#onewire-driver
# https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver
blue = dht.DHT11(Pin(10))
i2c = SoftI2C(sda=Pin(1), scl=Pin(0))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

oled.fill(0)
oled.show()

read_count = 0
def read_data(t):
    global read_count
    blue.measure()
    read_count += 1

    oled.fill(0)
    oled.text("Temp: {} C".format(blue.temperature()), 0, 10)
    oled.text("Hu: {} RH%".format(blue.humidity()), 0, 20)
    oled.text("# {}".format(read_count), 0, 50)

    oled.show()


t = Timer(0)
t.init(period=10000, mode=Timer.PERIODIC, callback=read_data)
# first run without waiting
read_data(t)

# stop the script by pressing ctrl-C in the shell
try:
    while True:
        time.sleep_ms(100)
except KeyboardInterrupt:
    t.deinit()
    oled.fill(0)
    oled.show()

