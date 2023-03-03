"""Basic board information

The information is printed in the interactive shell after running on the board.
"""
import esp
import machine
import sys

# type CTRL-D (soft reset) in the Shell to see the MicroPython version
# current frequency of the CPU
print("{} Hz".format(machine.freq()))
print("{} kHz".format(machine.freq() / 1000))
print("{} MHz".format(machine.freq() / 1000 / 1000))

# total size of the flash memory
print("{} bytes".format(esp.flash_size()))
print("{} kB".format(esp.flash_size()/1024))
print("{} MB".format(esp.flash_size() / 1024 / 1024))
