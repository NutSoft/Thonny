from machine import Pin
import time

#led1 = Pin(18, Pin.OUT)
#led2 = Pin(19, Pin.OUT)
#led3 = Pin(20, Pin.OUT)

#led1.value(1)
#led2.value(1)
#led3.value(1)

#time.sleep(5)

#led1.value(0)
#led2.value(0)
#led3.value(0)

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
