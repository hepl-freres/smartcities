from lcd1602 import LCD1602
from machine import I2C,Pin,ADC
from time import sleep

ROTARY_ANGLE_SENSOR= ADC(0)



i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)


d = LCD1602(i2c, 2, 16) # number of lines and characters per lines
d.display()



while True:
    
    val = ROTARY_ANGLE_SENSOR.read_u16()/65535
    valdegre =val*300
    sleep(0.25)
    d.clear()
    d.print("angle:")
    d.setCursor(7,0)
    d.print(str(int(valdegre))) # print the value of the ADC
    d.setCursor(10,0)
    d.write(0b11011111) 
    sleep(1)



