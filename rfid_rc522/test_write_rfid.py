#!/usr/bin/env python

import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522 as RFID

reader = RFID()

try:
        text = raw_input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()
