from machine import Pin
from neopixel import NeoPixel
from time import sleep

while True:
     for i in range(60):
      np[i]=(10,0,20)
      np.write()
      sleep(0.05)
      for i in range(60):
      np[i]=(0,0,0)
      np.write()
      sleep(0.05)
     for i in range(59,0,-1):
      np[i]=(0,0,100)
      np.write()
      sleep(0.05)
     for i in range(59,0,-1):
      np[i]=(0,0,0)
      np.write()
      sleep(0.05) 
