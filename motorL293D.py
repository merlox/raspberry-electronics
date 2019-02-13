import RPi.GPIO as gpio
import time

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

try:
    while True:
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
except KeyboardInterrupt:
    motorPWM.stop()
    gpio.cleanup()
	
