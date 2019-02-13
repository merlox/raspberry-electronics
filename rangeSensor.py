import RPi.GPIO as gpio
import time

triggerPin = 38
echoPin = 40
maxDistance = 220
timeOut = maxDistance * 60
interval = 1

def start():
    gpio.setmode(gpio.BOARD)
    gpio.setup(triggerPin, gpio.OUT)
    gpio.setup(echoPin, gpio.IN)
    try:
        loop()
    except KeyboardInterrupt:
        gpio.cleanup()

# To obtain the pulse time of a pin (?)
def pulseIn(pin, level, timeOut):
    initialTime = time.time()
    while(gpio.input(pin) != level):
        if((time.time() - initialTime) > timeOut * 0.000001):
            return 0
    initialTime = time.time()
    while(gpio.input(pin) == level):
        if((time.time() - initialTime) > timeOut * 0.000001):
            return 0
    pulseTime = (time.time() - initialTime) * 0.000001
    return pulseTime

# To measure the distance inn centimeters
def getSonar():
    gpio.output(triggerPin, gpio.HIGH)
    time.sleep(0.00001) # 10 nanoseconds
    gpio.output(triggerPin, gpio.LOW)
    pingTime = pulseIn(echoPin, gpio.HIGH, timeOut)
    distance = pingTime * 340.0 / 2.0 * 1000000.0
    return distance

def loop():
    while True:
        distance = getSonar()
        print("The distance is {:.2f}m".format(distance))
        time.sleep(interval)
        
start()