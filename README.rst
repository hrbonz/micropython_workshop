####################
Micropython workshop
####################

Workshop to introduce microcontroller programming and basic IoT concepts.

Microcontroller: ESP32-C3

Folders
=======

Demos
-----

1_basic_info
    Explore the board, basic micropython mechanisms and running code on the
    microcontroller.
2_simple_pin_output
    Simple pin control (up and down status).
3_led_blink
    Use timers to make the board LED blink.
4_led_on_key_timer
    Turn the LED on when pressing the board "key" button.
5_led_on_key_irq
    Do it again.
6_buzz_pwm
    Make some noise wityh on-board buzzer.
7_oled_display
    Display tiny things.
8_temp_hu_sensor
    Get temperature & humidity from two onboard sensors.
9_relay_on_off
    Close & open a relay.
10_multi_color_led
    Go through R/G/B in a loop, stop with ctrl-C.
11-mqtt_hello_world
    Hello world through MQTT

Modules
-------

``ssd1306.py``
    OLED display driver for I2C
``mqtt.py``
    `umqtt.simple <https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py>`_ MQTT module.

Exercises
---------

Solutions to exercises.

Bonus
-----

Bonus scripts for LED rainbow and PM2.5 sensor.


License
=======

The code for this workshop is published under a BSD 3-clause license, see the
LICENSE file distributed with the project.

References
==========

* `MicroPython: An Intro to Programming Hardware in Python <https://realpython.com/micropython/>`_
* `MicroPython documentation <https://docs.micropython.org/en/latest/index.html>`_
* `MicroPython Quick reference for the ESP32 <https://docs.micropython.org/en/latest/esp32/quickref.html>`_
