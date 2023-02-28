# blink with external led


from machine import Pin
import utime 

led = Pin(20, Pin.OUT) # pin 20 out 

while True:
    led.toggle() # change de state of th pin 20
    utime.sleep_ms(500) # delay 500ms
  