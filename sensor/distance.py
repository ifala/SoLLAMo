import RPi.GPIO as GPIO
import time

class ultrasonic_distance_sensor:
    ultrasonic_trig = 0
    ultrasonic_echo = 0
    distance = 0

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

        return self.distance


# referring to the pins by GPIO numbers
GPIO.setmode(GPIO.BCM)


ultrasonic_distance_sensor_high_dx = ultrasonic_distance_sensor(23, 24)
# todo aggiungere altri 3 sensori di distanza ultrasonica

try:
    while True:
        distance = ultrasonic_distance_sensor_high_dx.measure()
        print "Distance : %.1f cm" % distance
        # send data to the host every 0.5 sec
        time.sleep(0.5)
finally:
    GPIO.cleanup()

#
# def sensore_dist_dx():
#     global ECHO_dx
#     global LED_dx
#     global TRIG_dx
#
#     print ("Distance Measurement In Progress")
#
#     GPIO.output(TRIG, False)  # Set TRIG as LOW
#     print ("Waitng For Sensor To Settle")
#     time.sleep(2)  # Delay of 2 seconds
#     GPIO.output(TRIG, True)  # Set TRIG as HIGH
#     time.sleep(0.00001)  # Delay of 0.00001 seconds
#     GPIO.output(TRIG, False)  # Set TRIG as LOW
#     while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
#         pulse_start = time.time()  # Saves the last known time of LOW pulse
#     while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
#         pulse_end = time.time()  # Saves the last known time of HIGH pulse
#     pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable
#     distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
#     distance = round(distance, 2)  # Round to two decimal points
#     if distance > 2 and distance < 400:  # Check whether the distance is within range
#         print ("Distance:", distance + 0.5, "cm")  # Print distance with 0.5 cm calibration
#     else:
#         print ("Out Of Range")  # display out of range
#     return distance
#
#
# def sensore_dist_sx():
#     global ECHO_sx
#     global LED_sx
#     global TRIG_sx
#     #	global distance
#
#     print ("Distance Measurement In Progress")
#
#     GPIO.output(TRIG, False)  # Set TRIG as LOW
#     print ("Waitng For Sensor To Settle")
#     time.sleep(2)  # Delay of 2 seconds
#     GPIO.output(TRIG, True)  # Set TRIG as HIGH
#     time.sleep(0.00001)  # Delay of 0.00001 seconds
#     GPIO.output(TRIG, False)  # Set TRIG as LOW
#     while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
#         pulse_start = time.time()  # Saves the last known time of LOW pulse
#     while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
#         pulse_end = time.time()  # Saves the last known time of HIGH pulse
#     pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable
#     distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
#     distance = round(distance, 2)  # Round to two decimal points
#     if distance > 2 and distance < 400:  # Check whether the distance is within range
#         print ("Distance:", distance + 0.5, "cm")  # Print distance with 0.5 cm calibration
#     else:
#         print ("Out Of Range")  # display out of range
#     return distance
#
#
# # sensore_dist(distance)
# # while 1:
#
# #	#sensore_dist(distance)
#
# #	def Dis(distance):
# while True:
#     d = sensore_dist()
#     if d > 100:
#         GPIO.output(LED, 1)
#     else:
#         GPIO.output(LED, 0)
#
