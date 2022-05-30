import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
    print("Sensor detectando accion")
    return

GPIO.add_event_detect(23, GPIO.RISING)
GPIO.add_event_callback(23, action)

try:
    while True:
        print("alive")
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
