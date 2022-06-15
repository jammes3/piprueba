
#Add Phidgets library
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.DigitalOutput import *
#Required for sleep statement
import time

#Create
temperatureSensor = TemperatureSensor()
statusLED = DigitalOutput()

#Address
statusLED.setHubPort(1)
statusLED.setIsHubPortDevice(True)

#Open
temperatureSensor.openWaitForAttachment(1000)
statusLED.openWaitForAttachment(1000)

#Use your Phidgets
while (True):
    #Write data to file in CSV format
    with open ('/var/www/html/data.csv','a') as datafile:
        datafile.write(str(temperatureSensor.getTemperature()) + "\n")    
    #Blink LED
    statusLED.setState(not statusLED.getState())
    
    time.sleep(1.0)
  