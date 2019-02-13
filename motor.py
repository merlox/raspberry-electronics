import RPi.GPIO as gpio
import time

interval = 0.01

gpio.setmode(gpio.BOARD)
gpio.setup(40, gpio.OUT)
motorPWM = gpio.PWM(40, 207)
motorPWM.start(0)

try:
	while True:
		print('Running')
		for i in range(0, 100):
			motorPWM.ChangeDutyCycle(i)
			time.sleep(interval)
		for i in range(0, 100):
			motorPWM.ChangeDutyCycle(100 - i)
			time.sleep(interval)
except KeyboardInterrupt:
	motorPWM.stop()
	gpio.cleanup()
	
