
import RPi.GPIO as GPIO
import time
from sensor.distance import ultrasonic_distance_sensor_high_dx
from sensor.photosensor import pin_to_circuit, rc_time

# todo funziona?
distance = ultrasonic_distance_sensor_high_dx.measure()


try:
    while True:
        luce = rc_time(pin_to_circuit)
        distance = ultrasonic_distance_sensor_high_dx.measure()
        print ("Distance : %.1f cm" % distance)
        print ("Light value :  " + str(luce))
        print (" ")
        time.sleep(0.5)
finally:
    GPIO.cleanup()
    print("exiting main.py")

