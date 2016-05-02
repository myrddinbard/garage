import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)



GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback)


while True:
	if (GPIO.input(17)):
		print "Garage Closed"










os.system('/usr/bin/pushbullet.sh "Garage Open"')
