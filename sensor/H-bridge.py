import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.output(3, GPIO.LOW)
GPIO.output(2, GPIO.LOW)
p = GPIO.PWM(4, 50)
p.start(50)

def forward(x):
    GPIO.output(2, GPIO.HIGH)
    p.ChangeDutyCycle(25)
    print("avanti")
    sleep(x)
    GPIO.output(2, GPIO.LOW)

def reverse(x):
    GPIO.output(3, GPIO.HIGH)
    p.ChangeDutyCycle(100)
    print("idietro")
    sleep(x)
    GPIO.output(3, GPIO.LOW)
while(1):
	forward(5)
	sleep(0.5)
	reverse(5)

GPIO.cleanup()
