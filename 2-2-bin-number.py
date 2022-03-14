import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = []

GPIO.setmode(GPIO.BCM)

for _ in range(len(dac)):
    number.append(int(input())

GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac,number)

GPIO.output(dac,0)

GPIO.cleanup()

