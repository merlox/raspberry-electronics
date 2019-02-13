import RPi.GPIO as GPIO
import time

firstPin = 7
secondPin = 11
interval = 0.5

def setup():
    GPIO.setmode(GPIO.BOARD)
    # Setup all the pins
    GPIO.setup(firstPin, GPIO.OUT)
    GPIO.setup(secondPin, GPIO.OUT)

def led():
    while True:
        print('Activating first pin')
        runPins(0)    
        print('Activating both')
        runPins(2)
        print('Activating second pin')
        runPins(1)
        print('Activating both')
        runPins(2)

def runPins(position):
    if position == 0:
        GPIO.output(firstPin, GPIO.HIGH)
        GPIO.output(secondPin, GPIO.LOW)
    elif position == 1:
        GPIO.output(firstPin, GPIO.LOW)
        GPIO.output(secondPin, GPIO.HIGH)
    elif position == 2:
        GPIO.output(firstPin, GPIO.HIGH)
        GPIO.output(secondPin, GPIO.HIGH)
    time.sleep(interval)

def end():
    GPIO.output(firstPin, GPIO.LOW)
    GPIO.output(secondPin, GPIO.LOW)
    GPIO.cleanup()


setup()
try:
    led()
except KeyboardInterrupt:
    end()


