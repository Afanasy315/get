import dtb
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
dac = [8,11, 7, 1, 0, 5, 12, 6]
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO. OUT)

try:
    while True:
        num = input ("your number: ")
        try:
            num = int (num)
            if 0 <= num <= 255:
                GPIO. output (dac, dtb.dtb (num))
                voltage = float (num) *3.3 / 256
                print (f"voltage = {voltage: 4}")
            else:
                if num > 255:
                    print("number is to big")
                elif num < 0:
                    print("number is to small")
        except Exception:
            if num == 'q': break
            print("this is not a number")
finally:
    GPIO. output (dac, 0)
    GPTO. Cleanup ()
