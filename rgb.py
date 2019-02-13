import RPi.GPIO as gpio
import time
import random

pins = [40, 38, 26]
interval = 0.01

def setup():
    global firstPinPwm, secondPinPwm, thirdPinPwm
    gpio.setmode(gpio.BOARD)
    for i in pins:
        gpio.setup(i, gpio.OUT)
        gpio.output(i, gpio.HIGH)
    firstPinPwm = gpio.PWM(pins[0], 2000)
    secondPinPwm = gpio.PWM(pins[1], 2000)
    thirdPinPwm = gpio.PWM(pins[2], 2000)
    firstPinPwm.start(0)
    secondPinPwm.start(0)
    thirdPinPwm.start(0)

def setColor(r, g, b):
    firstPinPwm.ChangeDutyCycle(r)
    secondPinPwm.ChangeDutyCycle(g)
    thirdPinPwm.ChangeDutyCycle(b)

def loop():
    while True:
        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(0, 100)
        print('Color {} - {} - {}'.format(r, g, b))
        setColor(r, g, b)
        time.sleep(interval)

def loopAll():
    while True:
        for i in range(0, 100):
            setColor(i, 0, 0)
            time.sleep(interval)


def end():
    firstPinPwm.stop()
    secondPinPwm.stop()
    thirdPinPwm.stop()
    gpio.cleanup()

setup()
try:
    loopAll()
except KeyboardInterrupt:
    end()
