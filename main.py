

from sensor.distance import ultrasonic_distance_sensor_high_dx
# from sensor.photosensor import luce

try:
    while True:
        print ("test" + str(ultrasonic_distance_sensor_high_dx.distance))
finally:
    GPIO.cleanup()
    print("exiting main.py")

