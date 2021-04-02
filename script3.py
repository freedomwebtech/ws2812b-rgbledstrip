from machine import Pin
from neopixel import NeoPixel
from time import sleep
np = NeoPixel(Pin(5), 60)
while True:
     for i in range (59):
      np[i]=(100,0,0)
      np.write()
      sleep(0.1)
      np[i]=(0,0,0)
      np.write()
     for i in range(59,0,-1): 
      np[i]=(0,0,255)
      np.write()
      sleep(0.1)
      np[i]=(0,0,0)
      np.write()
