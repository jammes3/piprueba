import RPi.GPIO as GPIO
from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
ledRed = 22
ledYlw = 19
ledGrn = 17
#initialize GPIO status variables
ledRedSts = 0
ledYlwSts = 0
ledGrnSts = 0
# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   
GPIO.setup(ledYlw, GPIO.OUT) 
GPIO.setup(ledGrn, GPIO.OUT) 
# turn leds OFF 
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYlw, GPIO.LOW)
GPIO.output(ledGrn, GPIO.LOW)
	

def hello():
    while True:
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        templateDataTime = {
            'time': timeString,
            }
        return render_template('index.html', **templateDataTime)


@app.route("/")
def index():
	# Read Sensors Status
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	ledGrnSts = GPIO.input(ledGrn)
	templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : ledRedSts,
              'ledYlw'  : ledYlwSts,
              'ledGrn'  : ledGrnSts,
        }
	return render_template('index.html', **templateData)



@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
	if deviceName == 'ledYlw':
		actuator = ledYlw
	if deviceName == 'ledGrn':
		actuator = ledGrn
   
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	ledGrnSts = GPIO.input(ledGrn)
   
	templateData = {
              'ledRed'  : ledRedSts,
              'ledYlw'  : ledYlwSts,
              'ledGrn'  : ledGrnSts,
	}
	return redirect(url_for('index'))

@app.errorhandler(404)
def internal_error(error):
    return redirect(url_for('index'))

config = {
    "DEBUG": True  # run app in debug mode
}

if __name__ == "__main__":
    app.config.from_mapping(config)
    app.run(host='0.0.0.0', port=80, debug=True)