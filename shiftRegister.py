import RPi.GPIO as gpio
import time

pinData = 40
pinClock = 38
pinPush = 36
interval = 3

def start():
    gpio.setmode(gpio.BOARD)
    gpio.setup(pinData, gpio.OUT)
    gpio.setup(pinClock, gpio.OUT)
    gpio.setup(pinPush, gpio.OUT)
    try:
        loop()
    except KeyboardInterrupt:
        end()

def pushData(on):
    if on:
        gpio.output(pinData, gpio.HIGH)
        gpio.output(pinClock, gpio.HIGH)
        gpio.output(pinClock, gpio.LOW)
        gpio.output(pinData, gpio.LOW)
    else:
        gpio.output(pinData, gpio.LOW)
        gpio.output(pinClock, gpio.HIGH)
        gpio.output(pinClock, gpio.LOW)

def showNumber(number):
    for i in range(0, 8):
        if(8 - number <= i):
            pushData(True)
        else:
            pushData(False)
    gpio.output(pinPush, gpio.HIGH)
    time.sleep(0.01)
    gpio.output(pinPush, gpio.LOW)
    time.sleep(interval)

def loop():
    while True:
        print('Running...')
        showNumber(3)
        showNumber(1)
        showNumber(7)
        showNumber(8)
        showNumber(5)
        showNumber(0)
        showNumber(2)
    
def end():
    gpio.cleanup()

start()