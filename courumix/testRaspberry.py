import gpiozero
import time

led = gpiozero.RGBLED(red=17, green=27, blue=22)

def couleur(r, g, b):
    led.color = (r/255, g/255, b/255)

couleur(255,0,0)
time.sleep(2)
couleur(0,0,0)