import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM) #odnosimy sie do numeru pinu po GPIO#
GPIO.setmode(GPIO.BOARD) #odnosimy sie do numeru pinu po numerze nozki

GPIO.setwarnings(False)

p = {
    "PWM_a":12,
    "PWM_b":32,
    "AIN_2":22,
    "AIN_1":24,
    "BIN_1":26,
    "BIN_2":28,
    "LED_left":16,
    "LED_right":38,
    "LED_sensor":40,
    "SWITCH_left":18,
    "SWITCH_right":36,
}

czujniki = [35, 33, 29, 31, 23, 27, 19, 21, 13, 15, 11, 7]
GPIO.setup(p["BIN_1"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(p["BIN_2"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["PWM_a"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["PWM_b"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["AIN_1"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(p["AIN_2"], GPIO.OUT, initial=GPIO.HIGH)
