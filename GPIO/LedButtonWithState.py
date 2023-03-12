from machine import Pin
import utime

led = Pin(18, Pin.OUT) # pin 18 led output
button = Pin(16, Pin.IN) # pin 16 led input

val = 0

while True:
    if button.value() == 1: # if the button is pressed
        val = val+1
        utime.sleep(1)
    elif val == 2:    
        val = 0
        utime.sleep(1)
    led.value(val)   
