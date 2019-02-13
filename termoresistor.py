import smbus
import RPi.GPIO as gpio
import time
import math

address = 0x48
bus = smbus.SMBus(1)
command = 0x40

interval = 0.01
ledPin = 40
    
def setup():
    global ledPWM
    gpio.setmode(gpio.BOARD)
    gpio.setup(ledPin, gpio.OUT)
    gpio.output(ledPin, gpio.LOW)
    ledPWM = gpio.PWM(ledPin, 1000)
    ledPWM.start(30)

def start():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        end()

# Reads the analog channel which can be 0, 1, 2, 3 from the PCF8591
def analogRead(channel):
    value = bus.read_byte_data(address, command + channel)
    return value

# To map values from a scale of 0 to 255 to 100% to 0%
def translateValues(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)
    
def loop():
    while 1:
        value = analogRead(0)
        voltage = value / 255.0 * 3.3
        resistanceT = 10 * voltage / (3.3 - voltage)
        temperatureKelvin = 1 / (1 / (273.15 + 25) + math.log(resistanceT / 10) / 3950.0)
        celsius = temperatureKelvin - 273.15
        
        print('Temperature in celsius %d C' % (celsius))
        #ledPWM.ChangeDutyCycle(percentageOfLight)
        time.sleep(interval)
    
def end():
    ledPWM.stop()
    bus.close()
    gpio.cleanup()
    
start()