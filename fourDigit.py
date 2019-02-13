import RPi.GPIO as gpio
import time

pinTransistor1 = 40
pinTransistor2 = 38
pinTransistor3 = 36
pinTransistor4 = 32
pinData = 33
pinPush = 35
pinClock = 37

interval = 0.001

def start():
    print('Starting')
    gpio.setmode(gpio.BOARD)
    gpio.setup(pinTransistor1, gpio.OUT)
    gpio.setup(pinTransistor2, gpio.OUT)
    gpio.setup(pinTransistor3, gpio.OUT)
    gpio.setup(pinTransistor4, gpio.OUT)
    gpio.setup(pinData, gpio.OUT)
    gpio.setup(pinPush, gpio.OUT)
    gpio.setup(pinClock, gpio.OUT)
    
    gpio.output(pinTransistor1, gpio.HIGH)
    gpio.output(pinTransistor2, gpio.HIGH)
    gpio.output(pinTransistor3, gpio.HIGH)
    gpio.output(pinTransistor4, gpio.HIGH)
    
    try:
        loop()
    except KeyboardInterrupt:
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

def showNumber(number):
    for i in range(0, 8):
        if(8 - number <= i):
            pushData(True)
        else:
            pushData(False)
    gpio.output(pinPush, gpio.HIGH)
    gpio.output(pinPush, gpio.LOW)
    time.sleep(interval)
    
def showDigit(number):
    if number == 0:
        pushData(False)
        pushData(True)
        pushData(True)
        pushData(True)
        pushData(False)
        pushData(True)
        pushData(True)
        pushData(True)
    elif number == 1:
        pushData(False) # Dot
        pushData(False) # Bot
        pushData(False) # Bot left
        pushData(True) # Bot right
        pushData(False) # Mid
        pushData(False) # Top left
        pushData(False) # Top
        pushData(True) # Top right
    elif number == 2:
        pushData(False) # Dot
        pushData(True) # Bot
        pushData(True) # Bot left
        pushData(False) # Bot right
        pushData(True) # Mid
        pushData(False) # Top left
        pushData(True) # Top
        pushData(True) # Top right
    elif number == 3:
        pushData(False) # Dot
        pushData(True) # Bot
        pushData(False) # Bot left
        pushData(True) # Bot right
        pushData(True) # Mid
        pushData(False) # Top left
        pushData(True) # Top
        pushData(True) # Top right
    elif number == 4:
        pushData(False) # Dot
        pushData(False) # Bot
        pushData(False) # Bot left
        pushData(True) # Bot right
        pushData(True) # Mid
        pushData(True) # Top left
        pushData(False) # Top
        pushData(True) # Top right
    elif number == 5:
        pushData(False) # Dot
        pushData(True) # Bot
        pushData(False) # Bot left
        pushData(True) # Bot right
        pushData(True) # Mid
        pushData(True) # Top left
        pushData(True) # Top
        pushData(False) # Top right
    elif number == 6:
        pushData(False) # Dot
        pushData(True) # Bot
        pushData(True) # Bot left
        pushData(True) # Bot right
        pushData(True) # Mid
        pushData(True) # Top left
        pushData(True) # Top
        pushData(False) # Top right
    elif number == 7:
        pushData(False) # Dot
        pushData(False) # Bot
        pushData(False) # Bot left
        pushData(True) # Bot right
        pushData(False) # Mid
        pushData(False) # Top left
        pushData(True) # Top
        pushData(True) # Top right
    elif number == 8:
        pushData(False) # Dot
        pushData(True) # Bot
        pushData(True) # Bot left
        pushData(True) # Bot right
        pushData(True) # Mid
        pushData(True) # Top left
        pushData(True) # Top
        pushData(True) # Top right
    elif number == 9:
        pushData(False) # Dot
        pushData(True) # Bot
        pushData(False) # Bot left
        pushData(True) # Bot right
        pushData(True) # Mid
        pushData(True) # Top left
        pushData(True) # Top
        pushData(True) # Top right
    gpio.output(pinPush, gpio.HIGH)
    gpio.output(pinPush, gpio.LOW)

def turnTransistorOn(number):
    gpio.output(pinTransistor1, gpio.LOW if (number == 1) else gpio.HIGH)
    gpio.output(pinTransistor2, gpio.LOW if (number == 2) else gpio.HIGH)
    gpio.output(pinTransistor3, gpio.LOW if (number == 3) else gpio.HIGH)
    gpio.output(pinTransistor4, gpio.LOW if (number == 4) else gpio.HIGH)
    time.sleep(interval)

def loop():
    currentTimestamp = time.time()
    counter = 0
    while 1:
        stringCounter = str(counter) # We convert it once for speed
        showDigit(int(stringCounter[::-1][3]) if counter >= 1000 else 0)
        turnTransistorOn(1)
        showDigit(int(stringCounter[::-1][2]) if counter >= 100 else 0)
        turnTransistorOn(2)
        showDigit(int(stringCounter[::-1][1]) if counter >= 10 else 0)
        turnTransistorOn(3)
        showDigit(counter % 10)
        turnTransistorOn(4)
        
        if time.time() - currentTimestamp >= 1:
            counter += 1
            currentTimestamp = time.time()
            if counter >= 10000:
                counter = 0
    
start()