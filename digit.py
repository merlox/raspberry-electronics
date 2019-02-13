import RPi.GPIO as gpio
import time

pins = [40, 38, 37, 36, 35, 33, 32, 31]
interval = 0.1

def start():
    print('Starting...')
    gpio.setmode(gpio.BOARD)
    for pin in pins:
        gpio.setup(pin, gpio.OUT)
    try:
        loop()
    except KeyboardInterrupt:
        end()

def loop():
    while True:
        for pin in pins:
            gpio.output(pin, gpio.HIGH)

def end():
    gpio.cleanup()
    
start()