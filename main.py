
import RPi.GPIO as GPIO
import time
from sensor.distance import ultrasonic_distance_sensor_high_dx
from sensor.photosensor import pin_to_circuit, rc_time

# todo aggiungere altri 3 sensori di distanza ultrasonica
distance = ultrasonic_distance_sensor_high_dx.measure()


try:
    while True:
        luce = rc_time(pin_to_circuit)
        distance = ultrasonic_distance_sensor_high_dx.measure()
        print (str("Distance : %.1f cm" % distance) + "  Light value :  " + str(luce))
        time.sleep(0.5)
finally:
    GPIO.cleanup()
    print("exiting main.py")

