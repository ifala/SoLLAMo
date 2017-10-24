# photo sensors
#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# define the pin that goes to the circuit
pin_to_circuit = 4


def rc_time(gpio_pin):
    count = 0

    # Output on the pin for
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(gpio_pin, GPIO.IN)

    # Count until the pin goes high
    while (GPIO.input(gpio_pin) == GPIO.LOW):
        count += 1

    return count



#Catch when script is interrupted, cleanup correctly
# try:
#     # Main loop
#     while True:
#         luce = rc_time(pin_to_circuit)
#         # print(luce)
#         print(rc_time(pin_to_circuit))
# except KeyboardInterrupt:
#     pass
# finally:
#     GPIO.cleanup()