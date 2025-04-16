import RPi. GPIO as GPIO

GPIO. setmode (GPIO.BCM)
GPIO. setup (16, GPIO. OUT)

p = GPIO. PWM (16, 1000)

p.start (0)
try:
    while True:
        f = int (input ())
        p. ChangeDutyCycle(f)
        print (3.3*f/100)

finally:
    p.stop( )
    GPIO. output (27, 0)
    GPIO. cleanup ()
