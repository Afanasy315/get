import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


GPIO.output(dac, number)

time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()
