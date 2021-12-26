import RPi.GPIO as GPIO
import time
import sys
import os

cwd = os.getcwd()
filepath = cwd + "/height.txt"

in1 = 16
in2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)

with open(filepath, "r") as file:
    current_height = file.readline()
    for current_height in file:
        pass

if len(sys.argv) > 1:
    height = sys.argv[1]
else:
    height = input("How many cm: ")

if int(height) < 71:
    height = 71
elif int(height) > 115:
    height = 115

if int(current_height) > int(height):
    diff = int(current_height) - int(height)
    activeSwitch = in2
else:
    diff = int(height) - int(current_height)
    activeSwitch = in1

GPIO.output(activeSwitch, True)

time.sleep(int(diff)/2.5)

f = open(filepath, "w")
f.write(str(height))
f.close()

GPIO.output(activeSwitch, False)

GPIO.cleanup()
