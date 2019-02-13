import RPi.GPIO as gpio
import time

pinData = 36
pinLatch = 38
pinClock = 40
interval = 1

def start():
    print('Starting')
    gpio.setmode(gpio.BOARD)
    gpio.setup(pinData, gpio.OUT)
    gpio.setup(pinLatch, gpio.OUT)
    gpio.setup(pinClock, gpio.OUT)
    try:
        loop()
    except KeyboardInterrupt:
        for i in range(16):
            pushData(False)
        gpio.cleanup()
    
def pushData(on):
    if not on:
        gpio.output(pinData, gpio.HIGH)
        gpio.output(pinClock, gpio.HIGH)
        gpio.output(pinClock, gpio.LOW)
        gpio.output(pinData, gpio.LOW)
    else:
        gpio.output(pinData, gpio.LOW)
        gpio.output(pinClock, gpio.HIGH)
        gpio.output(pinClock, gpio.LOW)
        
def turnSpecificPinsOn(numbers):
    for i in range(16):
        for number in numbers:
            if i == number:
                pushData(True)
            else:
                pushData(False)
    
# Son 16 bites donde
# 00000000 <- la primera parte corresponde a la izquierda, la segunda la derecha -> 00000000
def pushByte(byteString):
    gpio.output(pinLatch, gpio.LOW)
    print('Bytes {}'.format(byteString))
    for i in range(16):
        if int(byteString[i]) == 1:
            pushData(True)
        else:
            pushData(False)
    gpio.output(pinLatch, gpio.HIGH)
    
def loop():
    while 1:
        turnSpecificPinsOn('0000100011111110')
        time.sleep(interval)
start()