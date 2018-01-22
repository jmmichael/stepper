#http://raspberry-python.blogspot.co.uk/2013/01/pyhacking-step-by-step.html
import RPi.GPIO as gpio
import time

PINS = [12,22,23,24]
SEQA = [(12,),(12,22),(22,),(22,23),(23,),(23,24),(24,),(24,12)]
RSEQA = [(24,),(24,23),(23,),(23,22),(22,),(22,12),(12,),(12,24)]

DELAY = 0.05


gpio.setmode(gpio.BCM)
for pin in PINS:
    gpio.setup(pin, gpio.OUT)

def stepper(sequence, pins):
    for step in sequence:
        for pin in pins:
            gpio.output(pin, gpio.HIGH) if pin in step else gpio.output(pin, gpio.LOW)
        time.sleep(DELAY)


try:
    while True:
        for _ in xrange(512):
            stepper(SEQA,PINS)  # forward
        for _ in xrange(512):
            stepper(RSEQA,PINS)  # reverse
except KeyboardInterrupt:
    gpio.cleanup()
