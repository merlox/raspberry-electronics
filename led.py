import RPi.GPIO as GPIO
import time

selectedPin = 11
interval = 0.05

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(selectedPin, GPIO.OUT)
    GPIO.output(selectedPin, GPIO.HIGH)

def led():
    while True:
        print('running loop')
        GPIO.output(selectedPin, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(selectedPin, GPIO.LOW)
        time.sleep(interval)

def end():
    GPIO.output(selectedPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        led()
    except KeyboardInterrupt:
        end()


