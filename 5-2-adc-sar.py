import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():

    k = 7
    N = 0
    while k:
        N += 2**k
        GPIO.output(dac, decimal2binary(N))
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            N -= 2**k
        k  -= 1
    return N


try:
    while True:
        N = adc()
        print(N, N/256*3.3)

finally:
    GPIO.output(dac,0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()