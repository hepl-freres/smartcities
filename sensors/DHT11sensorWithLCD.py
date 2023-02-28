#from lcd1602 import LCD1602_RGB  #LCD1602 RGB grove
from lcd1602 import LCD1602
from dht11 import *
from machine import I2C,Pin,ADC
from time import sleep
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)

d = LCD1602(i2c, 2, 16) # number of lines and characters per lines
d.display()
dht = DHT(18) # pin 18 dht 11 

while True:
    temp,humid = dht.readTempHumid() #Temp Humid
    sleep(1)
    d.clear()
    d.setCursor(0, 0)
    d.print("Temp :"+str(temp)) # display the temperature on the first ligne
    d.setCursor(0, 1)
    d.print("Humid :"+str(humid)) # display the temperature on the second ligne
    sleep(1)
    
    
    

sleep(1)
d.home()
d.print('hello')

sleep(1)
d.setCursor(0, 1) # set display position 
d.print('world')
