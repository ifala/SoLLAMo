import distance.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

while 1:

    dis_dx = sensore_dist_dx
    dis_sx = sensore_dist_sx
    if sensore_dist_dx < 50:
        GPIO.output(LED_dx, 0)
        GPIO.output(LED_sx, 0)
        time.sleep(1)
        GPIO.output(LED_dx, 1)
    if sensore_dist_sx < 50:
        GPIO.output(LED_dx, 0)
        GPIO.output(LED_sx, 0)
        time.sleep(1)
        GPIO.output(LED_sx, 1)
        noteGPIO.output(LED_dx, 0)
        GPIO.output(LED_sx, 0)
        time.sleep(1)
        GPIO.output(LED_dx, 1)
