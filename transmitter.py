import time
import sys
import RPi.GPIO as GPIO
from codes import *

TRANSMIT_PIN = 24 # this is the data pin of the transmitter

def transmit_code(channel):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    patterns = codes[channel]['code']
    repeats  = codes[channel]['repeat']
    for code, repeat in zip(patterns, repeats):
        for _ in range(repeat):
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(leading_1)
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(leading_0)
            for i in code:
                if i == '1':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(long_1)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(short_0)
                elif i == '0':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(short_1)
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(long_0)
                else:
                    continue
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(trailing_0)
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(gap_0)        
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        transmit_code(argument)
