import RPi.GPIO as gpio
import time
import smbus

interval = 0.1
pinInput1 = 38
pinInput2 = 36
pinEnable = 40

address = 0x48
bus = smbus.SMBus(1)
command = 0x40

def setup():
    global motorPWM
    gpio.setmode(gpio.BOARD)
    gpio.setup(pinInput1, gpio.OUT)
    gpio.setup(pinInput2, gpio.OUT)
    gpio.setup(pinEnable, gpio.OUT)
    
    motorPWM = gpio.PWM(pinEnable, 207)
    motorPWM.start(0)
    
def start():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        end()
    
def analogRead(channel):
    value = bus.read_byte_data(address, command + channel)
    value = bus.read_byte_data(address, command + channel)
    return value

def mapRanges(value, fromMin, fromMax, toMin, toMax):
    return (toMax - toMin) * (value - fromMin) / (fromMax - fromMin) + toMin

def loop():
    while 1:
        value = analogRead(0)
        runMotor(value)
        time.sleep(interval)
    
# Determines the direction and intensity of the motor. It runs 128 to one direction and 128 to the other.
def runMotor(analogInput):
    intensity = analogInput - 128
    
    # If we are running it in the right direction meaning 0 to 128 max, these if statements are just to control direction or to stop it
    if intensity > 0:
        gpio.output(pinInput1, gpio.HIGH)
        gpio.output(pinInput2, gpio.LOW)
        print('Running forward')
    elif intensity < 0:
        gpio.output(pinInput1, gpio.LOW)
        gpio.output(pinInput2, gpio.HIGH)
        print('Running backwards')
    elif intensity == 0:
        gpio.output(pinInput1, gpio.LOW)
        gpio.output(pinInput2, gpio.LOW)
        print('Stopped')
        
    # Here's where we determine the speed of the motor
    speedConverted = mapRanges(abs(intensity), 0, 128, 0, 100)
    motorPWM.ChangeDutyCycle(speedConverted)
    print('The speed of the motor is {}%'.format(speedConverted))

def end():
    motorPWM.stop()
    bus.close()
    gpio.cleanup()
    
start()