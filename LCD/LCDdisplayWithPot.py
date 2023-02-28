from lcd1602 import LCD1602
from machine import I2C,Pin,ADC
from time import sleep

ROTARY_ANGLE_SENSOR= ADC(0)



i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)

d = LCD1602(i2c, 2, 16) # number of lines and characters per lines
d.display()

while True:
    val = ROTARY_ANGLE_SENSOR.read_u16()
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print(str(val)) # print the value of the ADC
    sleep(1)



