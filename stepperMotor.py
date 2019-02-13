import RPi.GPIO as gpio
import time

motorPins = (32, 36, 38, 40)
clockwiseOrder = (0x01, 0x02, 0x03, 0x04)
antiClockwiseOrder = (0x04, 0x03, 0x02, 0x01)

def start():
    print('Starting...')
    gpio.setmode(gpio.BOARD)
    for pin in motorPins:
        gpio.setup(pin, gpio.OUT)
    try:
        loop()
    except KeyboardInterrupt:
        end()
    
def rotateOnce(direction, ms):
    # This is the power supply order
    for i in range(0, 4):
        for a in range(0, 4):
            if direction == 1:
                gpio.output(motorPins[a], ((clockwiseOrder[i] == 1 << a) and gpio.HIGH) or gpio.LOW)
            else:
                gpio.output(motorPins[a], ((antiClockwiseOrder[i] == 1 << a) and gpio.HIGH) or gpio.LOW)
        # The delay can't be less than 3 ms cuz it would exceed the speed of the motor
        if ms < 3:
            ms = 3
        time.sleep(ms * 0.001)
        
def rotateSteps(direction, ms, steps):
    for i in range(steps):
        rotateOnce(direction, ms)

def rotateStop():
    for pin in motorPins:
        gpio.output(pin, gpio.LOW)

def loop():
    while True:
        # To rotate 360 degrees we need 2048 steps which is equivalent to 512 steps
        rotateSteps(1, 3, 512)
        time.sleep(1)
        rotateSteps(0, 3, 512)
        time.sleep(1)

def end():
    for pin in motorPins:
        gpio.output(pin, gpio.LOW)
    gpio.cleanup()
    
start()