from machine import ADC
from machine import Pin
import utime


pot = ADC(0) # analog pin A0
led = Pin(18, Pin.OUT) # pin 18 led output

while True:
    val= pot.read_u16() # read the analog pin A0 
    print(val) # show the value
    if val > 20000 and val < 40000:
        led.value(1) # turn on the led
        utime.sleep(1)
    else:
        led.value(0) # turn on the led
        utime.sleep(1)
