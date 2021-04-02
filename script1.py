from machine import Pin
from neopixel import NeoPixel
from time import sleep
np = NeoPixel(Pin(5), 60)
np[0]=(255,0,0)
np.write()
