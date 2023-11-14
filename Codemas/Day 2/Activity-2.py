from machine import Pin
import time

#Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1 # Set the counter to start at 1

while counter < 11: # While count is less than 11...
    
    print(counter) # Print the current counter
    
    # LEDs all on
    red.value(1)
    amber.value(1)
    green.value(1)
    
    time.sleep(0.5) # Wait half a second
    
    # LEDs all off
    red.value(0)
    amber.value(0)
    green.value(0)
    
    time.sleep(0.5) # Wait half a second
    
    counter += 1 # Add 1 to our counter