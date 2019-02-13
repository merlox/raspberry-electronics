import RPi.GPIO as gpio
import time

relayerPin = 40
buttonPin = 38
debounceTime = 50

def start():
    gpio.setmode(gpio.BOARD)
    gpio.setup(relayerPin, gpio.OUT)
    gpio.setup(buttonPin, gpio.IN)
    try:
        loop()
    except KeyboardInterrupt:
        end()
    
def loop():
    relayerState = False
    lastChangeTime = round(time.time() * 1000)
    buttonState = gpio.HIGH
    lastButtonState = gpio.HIGH
    reading = gpio.HIGH
    while 1:
        reading = gpio.input(buttonPin)
        if reading != lastButtonState:
            lastChangeTime = round(time.time() * 1000)
        if (round(time.time() * 1000) - lastChangeTime) > debounceTime:
            if reading != buttonState:
                buttonState = reading
                if buttonState == gpio.LOW:
                    print('The button has been pressed')
                    relayerState = not relayerState
                    if relayerState:
                        print('Turning on the relay')
                    else:
                        print('Turning off the relay')
                else:
                    print('The button has been released')
        gpio.output(relayerPin, relayerState)
        lastButtonState = reading
    
def end():
    gpio.output(relayerPin, gpio.LOW)
    gpio.cleanup()
    
start()