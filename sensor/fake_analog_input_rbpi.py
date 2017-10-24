import RPi.GPIO as GPIO
import time


class FakeAnalogInput:
    rb_gpio_pin = 0

    def __init__(self, input_pin):
        self.rb_gpio_pin = input_pin

    def read_fake_analog_value(self):
        count = 0

        GPIO.setup(self.rb_gpio_pin, GPIO.OUT)
        GPIO.output(self.rb_gpio_pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(self.rb_gpio_pin, GPIO.IN)

        # Capacitor charging time --> used for fake analog input
        while GPIO.input(self.rb_gpio_pin) == GPIO.LOW:
            count += 1

        return count
