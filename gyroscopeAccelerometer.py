import MPU6050
import time

mpu = MPU6050.MPU6050()
acceleration = [0] * 3
gyro = [0] * 3
interval = 0.1

def start():
    mpu.dmp_initialize()
    try:
        loop()
    except KeyboardInterrupt:
        pass
    
def loop():
    while 1:
        acceleration = mpu.get_acceleration()
        gyro = mpu.get_rotation()
        print("Acceleration / Gyro: [{}], [{}], [{}], [{}], [{}], [{}]".format(acceleration[0], acceleration[1], acceleration[2], gyro[0], gyro[1], gyro[2]))
        
        # Acceleration and angular velocity
        print("Normal units: [{:.2f}] g, [{:.2}] g, [{:.2}] g, [{:.2}] d/s, [{:.2}] d/s, [{:.2}] d/s".format(acceleration[0]/16384.0, acceleration[1]/16384.0, acceleration[2]/16384.0, gyro[0]/131.0, gyro[1]/131.0, gyro[2]/131.0))
        time.sleep(interval)
    
start()