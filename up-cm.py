import RPi.GPIO as GPIO
import time
import sys

in1 = 18
in2 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)

if sys.argv[1]:
    height = sys.argv[1]
else:
    height = input("How many cm: ")

GPIO.output(in2, True)

time.sleep(int(height)/2.5)

GPIO.output(in2, False)

GPIO.cleanup()
