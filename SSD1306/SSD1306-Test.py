from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Quick and dirty test of my SSD1306 OLED

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
oled = SSD1306_I2C(128, 64, i2c)
oled.text("NutSoft Ltd", 0, 0)
oled.text("NutSoft Ltd", 0, 16)
oled.text("NutSoft Ltd", 0, 32)
oled.text("NutSoft Ltd", 0, 48)
oled.show()
