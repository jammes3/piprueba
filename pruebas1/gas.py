#generic read input (GPIO 23)

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

try:
    while True:

        if GPIO.input(23):
            print("GPIO 23 ON")
        else:
            print("GPIO 23 off")
        sleep(1)

finally:

    print("borrando...")
    GPIO.cleanup()
