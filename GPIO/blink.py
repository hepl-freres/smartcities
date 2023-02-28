# File : blink.py
# Simple blink program
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# philippe.camus@hepl.be
# 7/8/2022

from machine import Pin
import utime

#led = Pin(25, Pin.OUT) # on-board LED on Pico
led = Pin("LED", Pin.OUT) # on-board LED Pico W

while True:
    led.toggle() # change the state of the output
    utime.sleep_ms(500) # 500 ms of delay

# while True:
#     led.value(1)
#     utime.sleep_ms(500)
#     led.value(0)
#     utime.sleep_ms(500)
    
# while True:
#     led.high()
#     utime.sleep_ms(500)
#     led.low()
#     utime.sleep_ms(500)    