from machine import Pin
import time

ledRed = Pin(18, Pin.OUT)
ledAmb = Pin(19, Pin.OUT)
ledGrn = Pin(20, Pin.OUT)

while True:
    # Red
    ledRed.value(1)
    ledAmb.value(0)
    ledGrn.value(0)
    
    time.sleep(2)
    
    # Red & Amber
    ledRed.value(1)
    ledAmb.value(1)
    ledGrn.value(0)

    time.sleep(1)
    
    # Green
    ledRed.value(0)
    ledAmb.value(0)
    ledGrn.value(1)
    
    time.sleep(2)
    
    # Amber
    ledRed.value(0)
    ledAmb.value(1)
    ledGrn.value(0)
    
    time.sleep(1)
