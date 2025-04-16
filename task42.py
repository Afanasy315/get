import dtb
import RPi.GPIO as GPIO
import time

GPIO.setwarnings (False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO. setmode (GPIO.BCM)
GPIO. setup (dac, GPIO. OUT)
a = 1
x = 0

try:
    period = float (input ("input: "))
    while True:
        GPIO.output (dac, dtb.dtb(x))
        print(x)
        if x == 0: a = 1
        elif x == 255: a = 0
        x = x + 1 if a == 1 else x - 1
        time. sleep(period/512)
except ValueError:
    print ("error")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
