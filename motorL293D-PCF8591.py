import RPi.GPIO as gpio
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
command = 0x40

interval = 0.1

motorOnePin = 36
motorTwoPin = 38
enablePin = 40

gpio.setmode(gpio.BOARD)
gpio.setup(motorOnePin, gpio.OUT)
gpio.setup(motorTwoPin, gpio.OUT)
gpio.setup(enablePin, gpio.OUT)

motorPWM = gpio.PWM(enablePin, 207)
motorPWM.start(0)

def analogRead(channel):
    value = bus.read_byte_data(address, command + channel)
    value = bus.read_byte_data(address, command + channel)
    return value

def mapRanges(value, fromMin, fromMax, toMin, toMax):
    return (toMax - toMin) * (value - fromMin) / (fromMax - fromMin) + toMin

def runMotor2():
    intensity = analogRead(0) - 128
    if intensity > 0:
        gpio.output(motorOnePin, gpio.HIGH)
        gpio.output(motorTwoPin, gpio.LOW)
        print('Running forward')
    elif intensity < 0:
        gpio.output(motorOnePin, gpio.LOW)
        gpio.output(motorTwoPin, gpio.HIGH)
        print('Running backwards')
    elif intensity == 0:
        gpio.output(motorOnePin, gpio.LOW)
        gpio.output(motorTwoPin, gpio.LOW)
        print('Stopped')
    speedConverted = mapRanges(abs(intensity), 0, 128, 0, 100)
    motorPWM.start(speedConverted)
    print('The speed of the motor is {}%'.format(speedConverted))
    time.sleep(interval)

def runMotor(direction, speedPercent):
    gpio.output(motorOnePin, gpio.HIGH)
    gpio.output(motorTwoPin, gpio.LOW)
    for i in range(0, 100):
        print('Spinning right up {}'.format(i))
        motorPWM.ChangeDutyCycle(i)
        time.sleep(interval)
    for i in range(0, 100):
        print('Spinning right down {}'.format(100 - i))
        motorPWM.ChangeDutyCycle(100 - i)
        time.sleep(interval)
        
    gpio.output(motorOnePin, gpio.LOW)
    gpio.output(motorTwoPin, gpio.HIGH)
    for i in range(0, 100):
        print('Spinning left up {}'.format(i))
        motorPWM.ChangeDutyCycle(i)
        time.sleep(interval)
    for i in range(0, 100):
        print('Spinning left down {}'.format(100 - i))
        motorPWM.ChangeDutyCycle(100 - i)
        time.sleep(interval)

try:
    while True:
        runMotor2()
except KeyboardInterrupt:
    motorPWM.stop()
    bus.close()
    gpio.cleanup()