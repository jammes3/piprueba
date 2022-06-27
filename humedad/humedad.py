import pigpio
import DHT22
from time import sleep


# Inicia GPIO for pigpio
pi = pigpio.pi()

# Setup the sensor
dht22 = DHT22.sensor(pi, 4) # usa el actual GPIO BCM pin
dht22.trigger()


# We want our sleep time to be above 2 seconds.
sleepTime = 3

def readDHT22():

    # Get a new reading
    dht22.trigger()

    # Save our values
    humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())

    return (humidity, temp)

try:
    print "onectando..."
    sleep(1)
    print "Listo!"

    while True:

      humidity, temperature = readDHT22()
      print("Humidity is: " + humidity + "%")
      print("Temperature is: " + temperature + "C")
      sleep(sleepTime)

except: KeyboardInterrupt:
    print "Saliendo..."
GPIO.cleanup()
