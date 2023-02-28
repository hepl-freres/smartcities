# intro "never gonna give you up" 


from machine import Pin, PWM
from time import sleep
#import utime

buzzer = PWM(Pin(27)) #pin 27 pwm
vol = 1000 # sound volume

#while True:
#    buzzer.freq(1046) #DO
#    buzzer.duty_u16(1000)
#    utime.sleep(1)
    
def DO(time):
    buzzer.freq(1046)#1
    buzzer.duty_u16(vol)
    sleep(time)
def RE(time):
    buzzer.freq(1175)#2
    buzzer.duty_u16(vol)
    sleep(time)
def MI(time):
    buzzer.freq(1318)#3
    buzzer.duty_u16(vol)
    sleep(time)
def FA(time):
    buzzer.freq(1397)#4
    buzzer.duty_u16(vol)
    sleep(time)
def SO(time):
    buzzer.freq(1568)#5
    buzzer.duty_u16(vol)
    sleep(time)
def LA(time):
    buzzer.freq(1760)#6
    buzzer.duty_u16(vol)
    sleep(time)
def SI(time):
    buzzer.freq(1967)#7
    buzzer.duty_u16(vol)
    sleep(time)
def DOO(time):            # do 6th octave
    buzzer.freq(2093)#8
    buzzer.duty_u16(vol)
    sleep(time)
def REE(time):            # RE 6th octave
    buzzer.freq(2349)#8
    buzzer.duty_u16(vol)
    sleep(time)      
def N(time):
    buzzer.duty_u16(0)
    sleep(time)
      
                
  
while True:  
    SO(0.75)   
    LA(0.75)  
    RE(0.50)
    LA(0.75)
    SI(0.75)
    REE(0.125)
    DOO(0.125)
    SI(0.25)
    SO(0.75)
    LA(0.75)
    RE(0.595)
    N(0.30)
    RE(0.125)
    N(0.065)
    RE(0.125)
    MI(0.25)
    SO(0.30)
    SO(0.30)
    N(0.125)
    
    
    
    
