import RPi.GPIO as GPIO
import time

pins = [38, 7, 13, 11, 15, 31, 33, 35, 37, 40]
interval = 0.005
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
        runPWMPulsating()

def runPWMPulsating():
    firstLedPWM = GPIO.PWM(pins[0], 100)
    firstLedPWM.start(0)
    for i in range(0, 100):
        firstLedPWM.ChangeDutyCycle(i)
        time.sleep(interval)

    for i in range(0, 100):
        firstLedPWM.ChangeDutyCycle(100 - i)
        time.sleep(interval)

    firstLedPWM.stop()

def runPWM():
    # First pin at 50%, second at 100%
    firstLedPWM = GPIO.PWM(pins[0], 100)
    firstLedPWM.start(5)

    secondLedPWM = GPIO.PWM(pins[1], 100)
    secondLedPWM.start(100)

    time.sleep(interval)

    firstLedPWM.ChangeDutyCycle(100)
    secondLedPWM.ChangeDutyCycle(5)

    time.sleep(interval)

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


