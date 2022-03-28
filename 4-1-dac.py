import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        number = input()

        if number == 'q':
            break

        else:
            number = int(number)

            if number<0: 
                print('Введено отрицательное значение')
            elif number>255:
                print('Введено значение, превышающее возможности 8-разрядного ЦАП')
        
            else:
                U = (number/255)*3.3
                print(U, 'В')

                number = decimal2binary(number)
                GPIO.output(dac, number)

except ValueError:
    print('Введено не числовое значение или не целое число')
    

finally:
    GPIO.output(dac,0)

    GPIO.cleanup()

