import smbus
import RPi.GPIO as gpio
import time

address = 0x48
bus = smbus.SMBus(1)
command = 0x40

interval = 0.01
ledPin1 = 40
ledPin2 = 38
ledPin3 = 36
    
def setup():
    global ledPWM1, ledPWM2, ledPWM3
    gpio.setmode(gpio.BOARD)
    gpio.setup(ledPin1, gpio.OUT)
    gpio.output(ledPin1, gpio.LOW)
    ledPWM1 = gpio.PWM(ledPin1, 1000)
    ledPWM1.start(0)
    
    gpio.setup(ledPin2, gpio.OUT)
    gpio.output(ledPin2, gpio.LOW)
    ledPWM2 = gpio.PWM(ledPin2, 1000)
    ledPWM2.start(0)
    
    gpio.setup(ledPin3, gpio.OUT)
    gpio.output(ledPin3, gpio.LOW)
    ledPWM3 = gpio.PWM(ledPin3, 1000)
    ledPWM3.start(0)

def start():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        end()

# Reads the analog channel which can be 0, 1, 2, 3 from the PCF8591
def analogRead(channel):
    value = bus.read_byte_data(address, command + channel)
    value = bus.read_byte_data(address, command + channel) # Run it twice to get the current value otherwise you'll get the last value instead
    return value
    
def loop():
    while 1:
        # You can now convert these analog values to digital if you want and to voltages
        value1 = analogRead(0)
        value2 = analogRead(1)
        value3 = analogRead(2)
        ledPWM1.ChangeDutyCycle(value1 * 100 / 255)
        ledPWM2.ChangeDutyCycle(value2 * 100 / 255)
        ledPWM3.ChangeDutyCycle(value3 * 100 / 255)

        print('Values %d - %d - %d' % (value1, value2, value3))
        time.sleep(interval)
    
def end():
    ledPWM1.stop()
    ledPWM2.stop()
    ledPWM3.stop()
    bus.close()
    gpio.cleanup()
    
start()