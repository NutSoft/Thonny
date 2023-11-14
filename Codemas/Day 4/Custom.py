from machine import ADC, Pin, PWM
import time

# Light LEDs depending on the potentiometer value
#
# Rotating the potentiometer from it's lowest setting:
# - Green lights first and brightens to full illumination, followed by...
# - Amber, which also lights and brightens to full illumination, followed by...
# - Red, which also lights and brightens to full illumination.
# Reversing the rotation of the potentiometer has the opposite effect.

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the LED pins
red = PWM(Pin(18, Pin.OUT))
amber = PWM(Pin(19, Pin.OUT))
green = PWM(Pin(20, Pin.OUT))

# Set the PWM Frequency
# Sets how often to switch the power between on and off for the LED
red.freq(1000)
amber.freq(1000)
green.freq(1000)

# Create a variable for our reading
reading = 0
try:
    while True: # Run forever

        reading = potentiometer.read_u16() # Read the potentiometer value and set this as our reading variable value

        print(reading) # Print the reading

        green.duty_u16(int(min(reading, 20000)*3.27675))

        if 20000 < reading < 40000: # If reading is between 20000 and 40000
            amber.duty_u16(int(min(reading-20000, 20000)*3.27675))

        elif reading >= 40000: # If reading is greater than or equal to 40000
            red.duty_u16(int(min(reading-40000, 20000)*3.27675))

        time.sleep(0.001) # Short delay

except(KeyboardInterrupt):
    red.duty_u16(0)
    amber.duty_u16(0)
    green.duty_u16(0)