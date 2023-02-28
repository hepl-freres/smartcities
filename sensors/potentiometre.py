

# # Potentiometer reading    
from machine import ADC
import utime 

pot = ADC(0) # analog pin A0

while True:
    val= pot.read_u16() # read the analog pin A0
    print(val)
    utime.sleep_ms(500)
