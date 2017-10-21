
import RPi.GPIO as GPIO
import time
from sensor.distance import ultrasonic_distance_sensor_high_dx
from sensor.photosensor import luce

try:
    while True:
        print (str(ultrasonic_distance_sensor_high_dx.distance) + "  Light value :  " + str(luce))
        time.sleep(0.5)
finally:
    GPIO.cleanup()
    print("exiting main.py")

