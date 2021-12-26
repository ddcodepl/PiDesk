import RPi.GPIO as GPIO
import time
import sys

in1 = 18
in2 = 16

with open("/home/ubuntu/desk/height.txt", "r") as file:
    current_height = file.readline()
    for current_height in file:
        pass

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)

if len(sys.argv) > 1:
    height = sys.argv[1]
else:
    height = input("How many cm: ")

GPIO.output(in2, True)

time.sleep(int(height)/2.5)

f = open("/home/ubuntu/desk/height.txt", "w")
f.write(str(int(current_height) + int(height)))
f.close()

GPIO.output(in2, False)

GPIO.cleanup()
