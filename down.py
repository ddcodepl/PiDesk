import RPi.GPIO as GPIO
import time

in1 = 18
in2 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)

try:
    while True:
        GPIO.output(in1, True)


except KeyboardInterrupt:
    GPIO.cleanup()
