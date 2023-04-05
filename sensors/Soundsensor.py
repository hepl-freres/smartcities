
from machine import I2C,Pin,ADC
from utime import sleep


SOUND_SENSOR = ADC(1)

while True:
    average = 0

    for i in range (1000):
        noise = SOUND_SENSOR.read_u16()/256
        average += noise
    noise = average/1000
    print(noise)
    
 
    if noise < 45:
        print('peu de bruit')
        sleep(1)
    if noise >= 45 and noise < 60:
        print('bruit moyen')
        sleep(1)
    if noise >= 65:
        print('bruit fort')
        sleep(1)