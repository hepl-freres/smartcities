
#Varying LED luminosity
from machine import Pin, PWM
import utime
# 
pwm = PWM(Pin(20)) # PWM for Grove LED
pwm.freq(500)
# 
##linear variation
while True:
    for i in range(20):
        pwm.duty_u16(i*3276)
        utime.sleep_ms(100)
     
## quadratic variation
# lum=[]
for i in range(20):
    lum.append(i*i)
     
while True:
    for i in range(20):
        pwm.duty_u16(i*181)
        utime.sleep_ms(100)


# # Toggling led with push button and interrupt
# from machine import Pin
# import utime
# 
# push = Pin(18, Pin.IN) # Grove push button
# led = Pin(20, Pin.OUT) # Grove LED
# 
# def toggle_led(p):
#     led.toggle()
#     
# push.irq(toggle_led,trigger=Pin.IRQ_RISING)
# 
# #push.irq(lambda p: led.toggle(),trigger=Pin.IRQ_RISING)
# 
# while True:
#     pass
