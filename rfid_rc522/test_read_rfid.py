#!/usr/bin/env python

import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522 as RFID
from time import sleep

reader = RFID()

while True:

    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
#        GPIO.cleanup()
        sleep(0.5)
