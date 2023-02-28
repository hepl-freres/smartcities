
# # Varying LED luminosity
from machine import Pin, PWM
import utime
 
pwm = PWM(Pin(20)) # PWM Pin 20
pwm.freq(500)
 
##linear variation
while True:
     for i in range(20):
         pwm.duty_u16(i*3276)
         utime.sleep_ms(100)
#     
# # # quadratic variation
lum=[]
for i in range(20):
     lum.append(i*i)
     
while True:
    for i in range(20):
         pwm.duty_u16(i*181)
         utime.sleep_ms(100)