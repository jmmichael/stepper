#taken from Gaven MacDonald youtube.com/watch?v=Dc16mKFA7Fo
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ControlPin = [17,22,23,24]
#r = 99
r = int(raw_input("enter a value: "))
for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False)

seq =	[ [1,0,0,0],
	  [1,1,0,0],
	  [0,1,0,0],
	  [0,1,1,0],
	  [0,0,1,0],
	  [0,0,1,1],
	  [0,0,0,1],
	  [1,0,0,1] ]

#for i in range(512):
for i in range(r):
	#goes through the sequence once
	for halfstep in range (8):
		for pin in range(4):
		#set each pin
			GPIO.output(ControlPin[pin], seq[halfstep][pin])
		time.sleep(0.001) 
GPIO.cleanup()
