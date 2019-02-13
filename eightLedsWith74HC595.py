import RPi.GPIO as gpio
import time

lsbFirst = 1
msbFirst = 2
dataPin = 36
latchPin = 38
clockPin = 40

low = gpio.LOW
high = gpio.HIGH
out = gpio.OUT
interval = 0.1

def start():
    gpio.setmode(gpio.BOARD)
    gpio.setup(dataPin, gpio.OUT)
    gpio.setup(latchPin, gpio.OUT)
    gpio.setup(clockPin, gpio.OUT)
    try: loop()
    except KeyboardInterrupt: end()
    
# To make bit serial transmission
def shiftOut(dPin, cPin, order, value):
    for i in range(0, 8):
        gpio.output(cPin, low)
        if order == lsbFirst:
            gpio.output(dPin, ((0x01 & (value >> 1) == 0x01) and high) or low)
        elif order == msbFirst:
            gpio.output(dPin, ((0x80 & (value << 1) == 0x80) and high) or low)
        gpio.output(cPin, high)

def loop():
    while True:
        print('Looping')
        x = 0x01
        for i in range(0, 8):
            gpio.output(latchPin, low) # Set the latch to low
            shiftOut(dataPin, clockPin, lsbFirst, x)
            gpio.output(latchPin, high) # Set the latch to high, when set to high, it updates the parallel data output
            x <<= 1 # Move one bit to the left, which activates the next led
            time.sleep(interval)
        x = 0x80
        for i in range(0, 8):
            gpio.output(latchPin, low) # Set the latch to low
            shiftOut(dataPin, clockPin, lsbFirst, x)
            gpio.output(latchPin, high) # Set the latch to high, when set to high, it updates the parallel data output
            x >>= 1 # Move one bit to the right
            time.sleep(interval)
    
def end():
    gpio.cleanup()
    
start()