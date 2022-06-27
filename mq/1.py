import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    while True:
      if GPIO.input(4):
        print("escuchando true en gpio 4")
      else:
        print:("estado en false")
      sleep(1)
finally:
    print("limpiando...")
    GPIO.cleanup()
