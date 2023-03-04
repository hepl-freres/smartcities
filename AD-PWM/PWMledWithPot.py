from machine import Pin, PWM, ADC
adc = machine.ADC(0) # pot pin A0
pwm0 = PWM(Pin(18)) # pin 18 led      
pwm0.freq(1000)         
while True:
    digital_value = adc.read_u16() # read the adc
    pwm0.duty_u16(digital_value)    # duty cycle use the analog value of the pot 