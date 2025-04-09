import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(16, GPIO.IN)

while True:
    GPIO.output(23, GPIO.input(16))
