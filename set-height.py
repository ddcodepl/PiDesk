import RPi.GPIO as GPIO
import time

in1 = 16
in2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)

with open("/home/ubuntu/desk/height.txt", "r") as file:
    current_height = file.readline()
    for current_height in file:
        pass

height = input("Set height: ")

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

f = open("/home/ubuntu/desk/height.txt", "w")
f.write(str(height))
f.close()

GPIO.output(activeSwitch, False)

GPIO.cleanup()
