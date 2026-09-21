from mfrc522 import SimpleMFRC522
import gpiozero
import time

led = gpiozero.RGBLED(red=17, green=27, blue=22)
reader = SimpleMFRC522()

def couleur(r, g, b):
    led.color = (r/255, g/255, b/255)

idAutorise = [789002705379, 689160823902]

print("En attente de badge...")

id, text = reader.read()

print(f"ID détecté : {id}")

if id in idAutorise:
    print("Accès autorisé")
    couleur(0, 255, 0)
    time.sleep(0.25)
    couleur(0,0,0)
    time.sleep(0.25)
    couleur(0, 255, 0)
    time.sleep(0.25)
    couleur(0,0,0)
    time.sleep(0.25)
    couleur(0, 255, 0)
    time.sleep(0.25)
    couleur(0,0,0)
else:
    print("Accès refusé")
    couleur(255, 0, 0)
    time.sleep(0.25)
    couleur(0,0,0)
    time.sleep(0.25)
    couleur(255, 0, 0)
    time.sleep(0.25)
    couleur(0,0,0)
    time.sleep(0.25)
    couleur(255, 0, 0)
    time.sleep(0.25)
    couleur(0,0,0)

#689160823902
#789002705379