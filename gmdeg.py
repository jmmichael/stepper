#taken from Gaven MacDonald youtube.com/watch?v=Dc16mKFA7Fo
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ControlPin = [17,22,23,24]

d = int(raw_input("enter degrees: "))
r = int(d*512/360)
print r

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


for i in range(r):
	for halfstep in range (8):
		for pin in range(4):
		#set each pin
			GPIO.output(ControlPin[pin], seq[halfstep][pin])
		time.sleep(0.001) 
GPIO.cleanup()
