import machine
import utime as time
from machine import Pin

# Simple beam break IRQ program with duration for Raspberry Pi Pico

beam_pin = Pin(15, Pin.IN, Pin.PULL_UP)
old_beam_value = beam_pin.value()
last_time = time.ticks_us()

def beam_change(pin):
    global last_time
    broken = pin.value() == 0
    if broken:
        last_time = time.ticks_us()
        print('Beam Broken')
    else:
        elapsed_time = time.ticks_diff(time.ticks_us(), last_time)
        elapsed_time /= 1_000_000
        print('Beam Restored', elapsed_time)

beam_pin.irq(handler = beam_change, trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING)

while True:
    time.sleep(0.01)