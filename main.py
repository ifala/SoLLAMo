
# import from folder.file
from sensor.distance import sensore_dist_dx
from sensor.distance import sensore_dist_sx
from sensor.photosensor import
from sensor.humtemp import temp




#import from lib
import RPi.GPIO as GPIO
import time
import
GPIO.setmode(GPIO.BCM)


class LED_dx(object):
    pass


while 1:
    if temp() > 50:
    if sensore_dist_sx() < 50:
        GPIO.output(LED_dx, 0)
        GPIO.output(LED_sx, 0)
        time.sleep(1)
        GPIO.output(LED_dx, 1)
    if sensore_dist_sx() < 50:
        GPIO.output(LED_dx, 0)
        GPIO.output(LED_sx, 0)
        time.sleep(1)
        GPIO.output(LED_sx, 1)
        noteGPIO.output(LED_dx, 0)
        GPIO.output(LED_sx, 0)
        time.sleep(1)
        GPIO.output(LED_dx, 1)
