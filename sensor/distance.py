import RPi.GPIO as GPIO
import time

class ultrasonic_distance_sensor:
    ultrasonic_trig = 0
    ultrasonic_echo = 0
    distance = 0
    is_string = False

    def __init__(self, actual_ultrasonic_trig, actual_ultrasonic_echo):
        self.ultrasonic_echo = actual_ultrasonic_echo
        self.ultrasonic_trig = actual_ultrasonic_trig
        GPIO.setup(self.ultrasonic_echo, GPIO.IN)
        GPIO.setup(self.ultrasonic_trig, GPIO.OUT)
        GPIO.output(self.ultrasonic_trig, False)

    def measure(self):
        """
        measure distance
        """
        GPIO.output(self.ultrasonic_trig, True)
        time.sleep(0.00001)
        GPIO.output(self.ultrasonic_trig, False)
        start = time.time()

        while GPIO.input(self.ultrasonic_echo) == 0:
            start = time.time()

        while GPIO.input(self.ultrasonic_echo) == 1:
            stop = time.time()

        elapsed = stop-start
        self.distance = (elapsed * 34300)/2  # si suppone che la funzione di calcolo distanza sia giusta
        self.is_string = False

        if self.distance>150.0 :
            self.distance = "Too far"
            self.is_string = True

        if self.distance>150.0 :
            self.distance = "Too far"

        return self.distance

    def get_is_string(self):
        return self.is_string

# referring to the pins by GPIO numbers
GPIO.setmode(GPIO.BCM)


ultrasonic_distance_sensor_high_dx = ultrasonic_distance_sensor(23, 24)
# todo aggiungere altri 3 sensori di distanza ultrasonica

try:
    while True:
        distance = ultrasonic_distance_sensor_high_dx.measure()
        if ultrasonic_distance_sensor_high_dx.get_is_string():
            print (distance)
        else:
            print ("Distance : %.1f cm" % distance)
        # send data to the host every 0.5 sec
        time.sleep(0.5)
finally:
    GPIO.cleanup()

