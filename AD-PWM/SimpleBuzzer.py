from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(18)) # pin buzzer
buzzer.freq(500)
buzzer.duty_u16(1000) # duty cycle 
sleep(1)
