import random
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Quick and dirty test of my SSD1306 display

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
display = SSD1306_I2C(128, 64, i2c)

# NutSoft Ltd
# display.fill(0)
# display.text("NutSoft Ltd", 0, 0)
# display.text("NutSoft Ltd", 0, 16)
# display.text("NutSoft Ltd", 0, 32)
# display.text("NutSoft Ltd", 0, 48)
# display.show()
# time.sleep(5)

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
    display.show()
display.poweroff()

# # Pixels
# display.fill(0)
# while True:
#     xx = random.randint(0, 127)
#     yy = random.randint(0, 63)
#     display.pixel(xx, yy, 1)
#     display.show()
#     time.sleep(0.1)

display.poweroff()