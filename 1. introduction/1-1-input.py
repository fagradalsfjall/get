import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

if GPIO.input(15) == 1:
    GPIO.output(14, 1)
else:                                         
    GPIO.output(14, 0)

