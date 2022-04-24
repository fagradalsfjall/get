import RPi.GPIO as GPIO
import matplotlib.pyplot as plt

import time
from datetime import datetime


GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
comp = 4
GPIO.setup(comp, GPIO.IN)
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = 0)
leds = [21, 20, 16, 12, 7, 8, 25, 24][::-1]
GPIO.setup(leds, GPIO.OUT)


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    k = 7
    n = 0
    while k:
        n += 2**k
        GPIO.output(dac, decimal2binary(n))
        time.sleep(0.01)
        if GPIO.input(comp) == 0: 
            n -= 2**k
        k -= 1
    return n


def set_volume(value):
    value += 14 
    light = value*8//256
    GPIO.output(leds[:light], 1)
    GPIO.output(leds[light:], 0)


values = []
high = 0.98 
low = 0.02 

try:
    start_time = time.time()
    GPIO.output(troyka, 1)

    while True:
        n = adc()
        set_volume(n)
        values.append(n)
        print(f"n={n}    ", end='\r')
        if n >= high * 255:
            break
    
    high_time = time.time() - start_time
    print(high_time)
    GPIO.output(troyka, 0)

    while True:
        n = adc()
        set_volume(n)
        values.append(n)
        print(f"n={n}    ", end='\r')
        if n <= low * 255:
            break
    
    low_time = time.time() - start_time
    print(low_time)

    date = datetime.now().strftime('%y.%m.%d-%H.%M.%S')
    with open(f"data-{date}.txt", 'w') as f:
        f.write('\n'.join(str(i) for i in values))
    
    with open(f"settings-{date}.txt", 'w') as f:
        f.write(f"Средняя частота: {low_time/len(values)} с \nДискретизация {3.3/256} В\n")

    print(
        f"Длительность эксперимента: {low_time} с", 
        f"Среднее время измерения: {low_time/2} с", 
        f"Средняя частота: {low_time/len(values)} с", 
        f"Дискретизация {3.3/256} В", 
        sep='\n'
    )

    plt.plot(values)
    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
