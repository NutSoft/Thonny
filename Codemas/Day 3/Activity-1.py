from machine import ADC, Pin
import time

# Prints the analogue reading from our potentiometer

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

while True: # Loop forever

    print(potentiometer.read_u16()) # Read the potentiometer value

    time.sleep(1) # Wait a second