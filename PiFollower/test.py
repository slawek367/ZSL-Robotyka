import RPi.GPIO as GPIO
from time import sleep
#GPIO.setmode(GPIO.BCM) #GPIO pins
GPIO.setmode(GPIO.BOARD) #by pin number

GPIO.setwarnings(False)

p = {
    "PWM_a":12, #left engine
    "PWM_b":32, #right engine
    "AIN_2":22, #left engine direction
    "AIN_1":24, #left engine direction
    "BIN_1":26, #right engine direction
    "BIN_2":38, #right engine direction
    "LED_left":16, #left led
#   "LED_right":38, nie uzywac'
    "LED_sensor":40, #sensor led
    "SWITCH_left":18,
    "SWITCH_right":36
}

czujniki = [7, 11, 15, 13, 21, 19, 36, 23, 31, 29, 33, 35] #od lewej do prawej
GPIO.setup(p["AIN_1"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(p["AIN_2"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["BIN_1"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(p["BIN_2"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["PWM_a"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["PWM_b"], GPIO.OUT, initial=GPIO.HIGH)
sleep(3)
GPIO.clean()
