import RPi.GPIO as gpio
import Keypad

rows = 4
cols = 4
keys = [
    '1', '2', '3', 'A',
    '4', '5', '6', 'B',
    '7', '8', '9', 'C',
    '*', '0', '#', 'D'
]
rowsPins = [32, 36, 38, 40]
colsPins = [31, 33, 35, 37]

def start():
    try:
        loop()
    except KeyboardInterrupt:
        gpio.cleanup()
    
def loop():
    keypad = Keypad.Keypad(keys, rowsPins, colsPins, rows, cols)
    keypad.setDebounceTime(50)
    while 1:
        key = keypad.getKey()
        if(key != keypad.NULL):
            print("You pressed {}".format(key))
    
start()