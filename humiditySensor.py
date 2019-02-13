import RPi.GPIO as gpio
import time
import Freenove_DHT as DHT
dhtPin = 37

def start():
    try:
        loop()
    except KeyboardInterrupt:
        gpio.cleanup()

def loop():
    dht = DHT.DHT(dhtPin)
    counter = 0
    while(True):
        counter += 1
        read = dht.readDHT11()
        print('{} The read value is {}'.format(counter, read))
        
        if(read is dht.DHTLIB_OK):
            print('The read is normal')
        elif(read is dht.DHTLIB_ERROR_CHECKSUM):
            print('Checksum error')
        elif(read is dht.DHTLIB_ERROR_TIMEOUT):
            print('Timeout error')
        else:
            print('Unknown error')
            
        print('Humidity is {} while temperature is {}'.format(dht.humidity, dht.temperature))
        time.sleep(2)
        
start()