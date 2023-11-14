import random
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Quick and dirty test of my SSD1306 display

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
display = SSD1306_I2C(128, 64, i2c)

reset_pin = Pin(10, Pin.IN, Pin.PULL_UP)

def draw_screen():
    # Draw the MicroPython logo and print some text
    display.fill(0)
    display.fill_rect(0, 16, 32, 32, 1)
    display.fill_rect(2, 18, 28, 28, 0)
    display.vline(9, 24, 22, 1)
    display.vline(16, 18, 22, 1)
    display.vline(23, 24, 22, 1)
    display.fill_rect(26, 40, 2, 4, 1)
    display.text('MicroPython', 40, 16, 1)
    display.text('SSD1306', 40, 28, 1)
    display.text('display 128x64', 40, 40, 1)
    display.show()
    for i in range(0, 127):
        time.sleep(0.01)
        display.scroll(1, 0)
        display.fill_rect(i, 16, 1, 32, 0)
        display.fill_rect(0, 0, 127, 15, 1)
        display.text('NutSoft Ltd', 2, 2, 0)
        display.show()
    display.poweroff()

def reset(pin):
    print('RESET')
    display.poweron()
    display.fill(0)
    display.show()
    display.text('RESET', 30, 30)
    display.show()
    time.sleep(1)
    draw_screen()
    
reset_pin.irq(handler = reset, trigger = Pin.IRQ_FALLING)
try:
    while True:
        time.sleep(0.1)
except(KeyboardInterrupt):
    print('Interrupted')
    display.poweroff()

