import RPi.GPIO as GPIO
import time

pins = [38, 7, 13, 11, 15, 31, 33, 35, 37, 40]
interval = 0.1
lastPosition = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    # Setup all the pins
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def led():
    while True:
        global lastPosition
        print('Running pins...')
        runPinsIncreasing(pins[lastPosition])

def runPins(position):
    # Turn off all of them and then turn the right one on
    global lastPosition
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.output(position, GPIO.HIGH)
    if lastPosition < len(pins) - 1:
        lastPosition += 1
    else:
        lastPosition = 0
    time.sleep(interval)

def runPinsIncreasing(position):
    global lastPosition
    global pins
    if lastPosition == 0:
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)

    GPIO.output(position, GPIO.HIGH)
    if lastPosition < len(pins):
        lastPosition += 1

    # Reverse the order in the last position
    if lastPosition == len(pins):
        lastPosition = 0
        pins = pins[::-1]

    time.sleep(interval)

def end():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

setup()
try:
    led()
except KeyboardInterrupt:
    end()


