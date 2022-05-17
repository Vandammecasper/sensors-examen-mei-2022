import spidev
import time
import RPi.GPIO as io


class MCP:
    def __init__(self, bus=0, device=0):
        # spidev object initialiseren
        self.spi = spidev.SpiDev()
        # open bus 0, device 0
        self.spi.open(bus, device)
        # stel klokfrequentie in op 100kHz
        self.spi.max_speed_hz = 10 ** 5

    def read_channel(self, ch):
        # commandobyte samenstellen
        channel = ch << 4 | 128
        # list met de 3 te versturen bytes
        bytes_out = [0b00000001, channel, 0b00000000]
        # versturen en 3 bytes terugkrijgen
        bytes_in = self.spi.xfer2(bytes_out)
        # meetwaarde uithalen
        byte1 = bytes_in[1]
        byte2 = bytes_in[2]
        result = byte1 << 8 | byte2
        # meetwaarde afdrukken
        if ch == 0:  # trimmer
            print(str(result) + "\t" +
                  format(value_to_voltage(result), '.2f') + " V")
            servo(result)
        elif ch == 1:  # ldr
            # ldr geeft hoge waardes bij weinig licht, dus 1023 - result om logische waarde te krijgen
            result = 1023 - result
            print(str(result) + "\t" +
                  format(value_to_percentage(result), '.2f') + " %")

    def close_spi(self):
        self.spi.close()
