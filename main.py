from turtle import begin_fill


from RPi import GPIO
import time


def setup():
    GPIO.setmode(GPIO.BCM)


print('Script is running!')
try:
    setup()
    while True:
        print('test')

except KeyboardInterrupt as e:
    print(e)

finally:
    GPIO.cleanup()
    print('Script has stopped')
