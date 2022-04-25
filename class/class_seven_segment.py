import spidev
import time
import serial
from RPi import GPIO
import math
from subprocess import check_output


class seven_segment:
    def __init__(self):
        self.ser = serial.Serial('/dev/serial0')
        time.sleep(0.5)
        self.previous_time = None

    def get_time(self):
        return time.strftime("%H:%M")

    def send_time(self):
        if self.get_time() != self.previous_time:
            self.previous_time = self.get_time()
            self.ser.write(self.get_time().encode())
            print(self.ser.readline().decode().strip('\n'))
