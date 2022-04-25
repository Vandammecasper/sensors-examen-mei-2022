from RPi import GPIO
import spidev
import time


class MCP:
    def __init__(self, bus=0, device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 10 ** 5
        time.sleep(0.1)

    def read_channel(self, bit):

        commando_byte = bit << 4 | 128
        bytes_out = [0b00000001, commando_byte, 0b00000000]
        bytes_in = self.spi.xfer(bytes_out)
        byte1 = bytes_in[1]
        byte2 = bytes_in[2]
        result = byte1 << 8 | byte2
        return result

    def close_spi(self):
        self.spi.close()
