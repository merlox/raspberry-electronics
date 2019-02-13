import RPi.GPIO as gpio

ledPin = 40
sensorPin = 37

def start():
    print("Starting")
    gpio.setmode(gpio.BOARD)
    gpio.setup(ledPin, gpio.OUT)
    gpio.setup(sensorPin, gpio.IN)
    try:
        loop()
    except KeyboardInterrupt:
        gpio.cleanup()
       
def loop():
    while True:
        if gpio.input(sensorPin) == gpio.HIGH:
            gpio.output(ledPin, gpio.HIGH)
            print("Body detected...")
        else:
            gpio.output(ledPin, gpio.LOW)
            print("Led off...")
       
start()