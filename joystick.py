import RPi.GPIO as gpio
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
command = 0x40

interval = 0.01
swPin = 40
bluePin = 38
greenPin = 36
redPin= 32
    
def setup():
    global bluePWM, greenPWM, redPWM
    gpio.setmode(gpio.BOARD)
    gpio.setup(bluePin, gpio.OUT)
    gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.output(bluePin, gpio.LOW)
    bluePWM = gpio.PWM(bluePin, 1000)
    bluePWM.start(0)
    
    gpio.setup(greenPin, gpio.OUT)
    gpio.output(greenPin, gpio.LOW)
    greenPWM = gpio.PWM(greenPin, 1000)
    greenPWM.start(0)
    
    gpio.setup(redPin, gpio.OUT)
    gpio.output(redPin, gpio.LOW)
    redPWM = gpio.PWM(redPin, 1000)
    redPWM.start(0)

def start():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        end()

# Reads the analog channel which can be 0, 1, 2, 3 from the PCF8591
def analogRead(channel):
    bus.write_byte(address, command + channel)
    value = bus.read_byte(address)
    value = bus.read_byte(address) # Read twice to get the current data
    return value

# Writes an analog value
def analogWrite(value):
    bus.write_byte_data(address, command, value)
    
def loop():
    while 1:
        value = analogRead(0) * 100 / 255
        value2 = analogRead(1) * 100 / 255
        valueZ = gpio.input(swPin)
        # analogWrite(value) Only required to execute an output
        greenPWM.ChangeDutyCycle(value)
        redPWM.ChangeDutyCycle(value2)
        bluePWM.ChangeDutyCycle(valueZ * 100)
        print('Value {} and value2 {} and sw {}'.format(value, value2, valueZ))
        time.sleep(interval)
    
def end():
    greenPWM.stop()
    redPWM.stop()
    bluePWM.stop()
    bus.close()
    gpio.cleanup()
    
start()