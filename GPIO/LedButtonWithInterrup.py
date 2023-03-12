from machine import Pin
import time

pin_button = Pin(16, mode=Pin.IN, pull=Pin.PULL_UP)
pin_led    = Pin(18, mode=Pin.OUT)


def button_isr(pin):
  pin_led.value(not pin_led.value())

pin_button.irq(trigger=Pin.IRQ_FALLING,handler=button_isr)

while True:
  ...