import RPi.GPIO as gpio
import math
import time

buzzerPin = 40
buttonPin = 38
interval = 0.001

# Setup the pins and the board
def setup():
    global buzzerPWM
    gpio.setmode(gpio.BOARD)
    gpio.setup(buzzerPin, gpio.OUT)
    gpio.setup(buttonPin, gpio.IN, pull_up_down=gpio.PUD_UP)
    buzzerPWM = gpio.PWM(buzzerPin, 1)

# Loop and detect if the button is pressed by reading the signal LOW or HIGH
def loop():
    while True:
        print('Running loop...')
        if gpio.input(buttonPin) == gpio.LOW:
            buzzerPWM.start(1)
            for i in range(0, 361):
                sin = math.sin(i * (math.pi / 180.0))
                tone = 1000 + sin * 500
                buzzerPWM.ChangeFrequency(tone)
                time.sleep(interval)
        else:
            buzzerPWM.stop()

def end():
    buzzerPWM.stop()
    gpio.cleanup()

def start():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        end()

start()
