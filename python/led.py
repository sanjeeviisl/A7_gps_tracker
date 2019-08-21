#!/usr/bin/python

#import the library
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

#initialize the gpio module
gpio.init()

#setup the port (same as raspberry pi's gpio.setup() function)
gpio.setcfg(port.PA7, gpio.OUTPUT)

while(1) :
	sleep(1)
	#now we do something (light up the LED)
	gpio.output(port.PA7, gpio.HIGH)
	print ("LED ON")

	#turn off the LED after 2 seconds
	sleep(1)
	gpio.output(port.PA7, gpio.LOW)
	print ("LED OFF")


