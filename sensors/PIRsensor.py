from machine import Pin
from utime import sleep

miniPir = Pin(18, Pin.IN)

while True:
    if miniPir.value()== 1:
        print('Motion Detected')
        sleep(1)
    if miniPir.value()== 0:
        print('nothing')
        sleep(1)        