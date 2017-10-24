
import RPi.GPIO as GPIO
import time
from sensor.distance import ultrasonic_distance_sensor_high_dx
from sensor.photosensor_OO import photosensor

# from sensor.photosensor import pin_to_circuit, rc_time

# todo funziona bo
#distance = ultrasonic_distance_sensor_high_dx.measure()
#luce = rc_time(pin_to_circuit)

try:
    while True:
        distance = ultrasonic_distance_sensor_high_dx.measure()
        # luce = rc_time(pin_to_circuit)
        light = photosensor.read_fake_analog_value()
        print("Light level revelated is: ")
        print(light)

        print(" Distance : %.1f cm" % distance)
        # print("Light value :  " + str(luce))
        print(" ")
        time.sleep(1)
finally:
    GPIO.cleanup()
    print("exiting main.py")

