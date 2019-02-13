import smbus
import RPi.GPIO as gpio
import time

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
    ledPWM.start(0)

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

# Writes an analog value
def analogWrite(value):
    bus.write_byte_data(address, command, value)
    
def loop():
    while 1:
        value = analogRead(0)
        # analogWrite(value) Only required to execute an output
        ledPWM.ChangeDutyCycle(value * 100 / 255)
        # Here is where the analog to digital convertion in taking place
        voltage = value / 255.0 * 3.3
        print('Value %d and voltage %.2f' % (value, voltage))
        time.sleep(interval)
    
def end():
    ledPWM.stop()
    bus.close()
    gpio.cleanup()
    
start()