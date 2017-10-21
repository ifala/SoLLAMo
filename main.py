
# import from folder.file
#from sensor.distance import sensore_dist_dx
import RPi.GPIO as GPIO
import time

from sensor.distance import ultrasonic_distance_sensor_high_dx
from sensor.photosensor import rc_time

print ultrasonic_distance_sensor_high_dx.distance
print rc_time
