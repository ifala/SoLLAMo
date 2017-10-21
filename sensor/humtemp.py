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
import RPi.GPIO as GPIO
import time


def bin2dec(string_num):
    return str(int(string_num, 2))


data = []

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
time.sleep(0.05)
GPIO.output(17, GPIO.LOW)
time.sleep(0.05)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in range(0, 500):
    data.append(GPIO.input(17))

bit_count = 0
tmp = 0
count = 0
HumidityBit = ""
TemperatureBit = ""
crc = ""

try:
    while data[count] == 1:
        tmp = 1
        count = count + 1

    for i in range(0, 32):
        bit_count = 0

        while data[count] == 0:
            tmp = 1
            count = count + 1

        while data[count] == 1:
            bit_count = bit_count + 1
            count = count + 1

        if bit_count > 3:
            if i >= 0 and i < 8:
                HumidityBit = HumidityBit + "1"
            if i >= 16 and i < 24:
                TemperatureBit = TemperatureBit + "1"
        else:
            if i >= 0 and i < 8:
                HumidityBit = HumidityBit + "0"
            if i >= 16 and i < 24:
                TemperatureBit = TemperatureBit + "0"

except:
    print "ERR_RANGE0"
    exit(0)

try:
    for i in range(0, 8):
        bit_count = 0

        while data[count] == 0:
            tmp = 1
            count = count + 1

        while data[count] == 1:
            bit_count = bit_count + 1
            count = count + 1

        if bit_count > 3:
            crc = crc + "1"
        else:
            crc = crc + "0"
except:
    print "ERR_RANGE1"
    exit(0)

Humidity = bin2dec(HumidityBit)
Temperature = bin2dec(TemperatureBit)

if int(Humidity) + int(Temperature) - int(bin2dec(crc)) == 0:
    print "Humidity:" + Humidity + "%"
    print "Temperature:" + Temperature + "C"
else:
    print "ERR_CRC"