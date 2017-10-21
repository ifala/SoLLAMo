# import RPi.GPIO as GPIO
# import dht11
#
# # initialize GPIO
# # GPIO.setwarnings(False)
# # GPIO.setmode(GPIO.BCM)
# # # GPIO.cleanup()
# #
# # instance = dht11.DHT11(17)
# # result = instance.read()
#
# # if result.is_valid():
# #     print("Temperature: %d C" % result.temperature)
# #     print("Humidity: %d %%" % result.humidity)
# # else:
# #     print("Error: %d" % result.error_code)
# #
# print("Temperature: %d C" % result.temperature)
# print("Humidity: %d %%" % result.humidity)
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 17)  # GPIO27 (BCM notation)
    print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))