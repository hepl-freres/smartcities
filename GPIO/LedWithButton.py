#led with button

from machine import Pin


led = Pin(18, Pin.OUT) # pin 18 led output
button = Pin(16, Pin.IN) # pin 16 led input


while True:
    val=button.value() # read the state of the button and put it in val
    if val == 1:
        led.value(1) # turn on the led 
    else:
        led.value(0) # turn off the led 
  
