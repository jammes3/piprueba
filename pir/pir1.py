# Importar librerias
import time
import RPi.GPIO as GPIO

# Usa BCM GPIO como referencia
# en vez de los pines fisicos
GPIO.setmode(GPIO.BCM)

# Define el pin a utilizar
GPIO_PIR = 7

print("Prueba basica del modulo PIR (CTRL-C para salir)")

GPIO.setwarnings(False)

# Configurar pin como escucha estado in
GPIO.setup(GPIO_PIR,GPIO.IN)

try:

    print("Conectando PIR ...")
    time.sleep(1)
    print "  Listo!!"

  # Bucle hasta que se precione CTRL-C
    while True :
      if GPIO.input(GPIO_PIR):
        print("Se detecta  presencia")
        time.sleep(0.5)
      else :
        print("No hay presencia")
        time.sleep(0.5)
except KeyboardInterrupt:
        print("  Saliendo")
  # Restablece la configuracion de GPIO
GPIO.cleanup()
