from machine import Pin, SoftI2C, Timer, UART
import struct
import time

from ssd1306 import SSD1306_I2C


# look at the microcontroller schematic to find the pin numbers
# https://docs.micropython.org/en/latest/library/machine.I2C.html?highlight=softi2c#machine.SoftI2C
i2c = SoftI2C(sda=Pin(1), scl=Pin(0))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

#: per docs
MAGIC = bytearray(b'\x42\x4d') # BM in ascii

CMD_READ = b'\xe2\x00\x00'

FIELDS = [
    "pm1",
    "pm25",
    "pm10",
    "pm1_atm",
    "pm25_atm",
    "pm10_atm",
    "pc03",
    "pc05",
    "pc1",
    "pc25",
    "pc5",
    "pc10",
]


class ReadTimeoutError(RuntimeError):
    pass


class FrameFormatError(RuntimeError):
    pass


def cmd_frame(cmd):
    frame = bytearray()
    frame.extend(MAGIC)
    frame.extend(cmd)
    frame.extend(sum(frame).to_bytes(2, "big"))
    return frame


class PMS7003:

    def __init__(self, rx_pin=7, tx_pin=6):
        # default pins are for the UART socket
        # plug tx to rx and vice versa
        self._com = UART(
          1,
          baudrate=9600,
          rx=rx_pin,
          tx=tx_pin,
        )
        # empty any leftover buffer from previous run
        self._com.read()

    def wait_bytes(self, num_bytes, timeout=1000):
        start = time.ticks_ms()
        while self._com.any() < num_bytes:
            elapsed = time.ticks_ms() - start
            if elapsed > timeout:
                raise ReadTimeoutError("Read timeout: waited {} ms for {} bytes".format(elapsed, num_bytes))
            time.sleep_ms(10)

    def read_data(self):
        frame = cmd_frame(CMD_READ)
        self._com.write(frame)
        # check magic prefix
        self.wait_bytes(2)
        prefix = self._com.read(2)
        if prefix != MAGIC:
            raise FrameFormatError("Frame prefix is wrong ({}))".format(data))

        # check data length
        self.wait_bytes(2)
        data = self._com.read(2)
        datalen = struct.unpack(">H", data)[0]

        # get actual measurement data
        self.wait_bytes(datalen)
        data = self._com.read(datalen)
        dataframe = struct.unpack(">HHHHHHHHHHHHHH", data)
        #crc = dataframe[-1]
        #checksum = sum(MAGIC) + sum(dataframe[:-2]) + sum(bytearray(datalen))
        measurements = dict(zip(FIELDS, dataframe[:-1]))
        return measurements


pms = PMS7003()

read_count = 0
def read_data(t):
    global read_count
    measurements = pms.read_data()
    read_count += 1

    oled.fill(0)
    oled.text("PM2.5:", 0, 0)
    oled.text("{} ug/m3".format(measurements["pm25"]), 0, 10)
    oled.text("# {}".format(read_count), 0, 30)

    oled.show()


t = Timer(0)
t.init(period=10000, mode=Timer.PERIODIC, callback=read_data)
# first run without waiting
read_data(t)
