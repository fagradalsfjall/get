import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]



p = GPIO.PWM(22, dc)
p.start(0)

try: 
    while True:
    
dc = float(input())


