#!/usr/bin/python 
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

# set up the GPIO channels - one input and one output
GPIO.setup(12, GPIO.IN)
# print (GPIO.VERSION)

while (1):
	# input from pin 12 
	input_value = GPIO.input(12)
	print(input_value)

	if (input_value) :
		os.system("curl -X POST \"https://api.prowlapp.com/publicapi/add?application=RaspberryPio&event=someone-entered-office&apikey=YOUR_PROWL_KEY_HERE\"")	
		time.sleep(60)	
	else :
		# do nothing	
		time.sleep(2)


