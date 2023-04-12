

from ws2812 import WS2812
import utime

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

led = WS2812(20,30)#WS2812(pin_num,led_count)
led.brightness=0.05

# displays each colors in sequence on all neopixels
for color in COLORS: 
    led.pixels_fill(color)
    led.pixels_show()
    utime.sleep(0.5)

# dimming function on last displayed color
for br in range(20):
    led.brightness=0.01 * br
    led.pixels_show()
    utime.sleep(0.1)
utime.sleep(1)

# switchs all neopixels off
led.pixels_fill(BLACK)
led.pixels_show()

# Chasing colors with each colors
led.brightness=0.1
for color in COLORS[1:10]: 
    led.color_chase(color,0.1)
    utime.sleep(0.5)   
utime.sleep(1)

# switchs all neopixels off
led.pixels_fill(BLACK)
led.pixels_show()

# blinks red with a 1s period
lit=True
for i in range(20):
    if lit :
        lit=False
        led.pixels_fill(BLACK)
    else :
        lit=True
        led.pixels_fill(RED) 
    led.pixels_show()
    utime.sleep(0.5)

# switchs all neopixels off
led.pixels_fill(BLACK)
led.pixels_show()