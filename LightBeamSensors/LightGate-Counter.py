import machine
import utime as time
from machine import Pin

# Simple beam break counter program for Raspberry Pi Pico

beam_pin = Pin(15, Pin.IN, Pin.PULL_UP)
old_beam_value = beam_pin.value()
count = 0

while True:
    if old_beam_value != beam_pin.value():
        old_beam_value = not old_beam_value
        if old_beam_value == True:
            count += 1
            print(count)
    time.sleep(0.01)