from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime

PCF8574_address = 0x27
PCF8574A_address = 0x3F

def start():
    global mcp, lcd
    print('Starting..')
    try:
        mcp = PCF8574_GPIO(PCF8574_address)
    except:
        try:
            mcp = PCF8574_GPIO(PCF8574A_address)
        except:
            print('I2C address error')
            exit(1)
    
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)
    
    try:
        loop()
    except KeyboardInterrupt:
        end()
    
def getCpuTemperature():
    temperature = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = temperature.read()
    temperature.close()
    return ' {:.2f}'.format(float(cpu) / 1000) + ' C'
    
def getTime():
    return datetime.now().strftime('    %H:%M:%S')
    
def loop():
    mcp.output(3, 1)
    lcd.begin(16, 2)
    while True:
        lcd.setCursor(0, 0)
        lcd.message('CPU:  ' + getCpuTemperature() + '\n')
        lcd.message(getTime())
        sleep(1)

def end():
    lcd.clear()
    
start()