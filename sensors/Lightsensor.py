
from machine import I2C,Pin,ADC
from utime import sleep


LIGHT_SENSOR = ADC(0)


while True:
   
    light = LIGHT_SENSOR.read_u16()/256
   
    if light < 80:
        print('peu de lumiere')
        sleep(0.2)
    if light >=80:ç
        print('bcp de lumiere')
        sleep(0.2)
    