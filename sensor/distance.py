import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG_dx = 23
ECHO_dx = 24
LED_sx = 3
TRIG_sx = 14
ECHO_sx = 15
LED_sx = 2

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)  # Set pin as GPIO out
GPIO.setup(ECHO, GPIO.IN)  # Set pin as GPIO in


def sensore_dist_dx():
    global ECHO_dx
    global LED_dx
    global TRIG_dx

    print ("Distance Measurement In Progress")

    GPIO.output(TRIG, False)  # Set TRIG as LOW
    print ("Waitng For Sensor To Settle")
    time.sleep(2)  # Delay of 2 seconds
    GPIO.output(TRIG, True)  # Set TRIG as HIGH
    time.sleep(0.00001)  # Delay of 0.00001 seconds
    GPIO.output(TRIG, False)  # Set TRIG as LOW
    while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
        pulse_start = time.time()  # Saves the last known time of LOW pulse
    while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
        pulse_end = time.time()  # Saves the last known time of HIGH pulse
    pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable
    distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)  # Round to two decimal points
    if distance > 2 and distance < 400:  # Check whether the distance is within range
        print ("Distance:", distance + 0.5, "cm")  # Print distance with 0.5 cm calibration
    else:
        print ("Out Of Range")  # display out of range
    return distance


def sensore_dist_sx():
    global ECHO_sx
    global LED_sx
    global TRIG_sx
    #	global distance

    print ("Distance Measurement In Progress")

    GPIO.output(TRIG, False)  # Set TRIG as LOW
    print ("Waitng For Sensor To Settle")
    time.sleep(2)  # Delay of 2 seconds
    GPIO.output(TRIG, True)  # Set TRIG as HIGH
    time.sleep(0.00001)  # Delay of 0.00001 seconds
    GPIO.output(TRIG, False)  # Set TRIG as LOW
    while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
        pulse_start = time.time()  # Saves the last known time of LOW pulse
    while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
        pulse_end = time.time()  # Saves the last known time of HIGH pulse
    pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable
    distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)  # Round to two decimal points
    if distance > 2 and distance < 400:  # Check whether the distance is within range
        print ("Distance:", distance + 0.5, "cm")  # Print distance with 0.5 cm calibration
    else:
        print ("Out Of Range")  # display out of range
    return distance


# sensore_dist(distance)
# while 1:

#	#sensore_dist(distance)

#	def Dis(distance):
while True:
    d = sensore_dist()
    if d > 100:
        GPIO.output(LED, 1)
    else:
        GPIO.output(LED, 0)

