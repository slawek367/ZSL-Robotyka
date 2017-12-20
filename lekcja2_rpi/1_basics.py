import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM) #odnosimy sie do numeru pinu po GPIO#
GPIO.setmode(GPIO.BOARD) #odnosimy sie do numeru pinu po numerze nozki

'''
Wylaczenie warningow typu:
test.py:12: RuntimeWarning: This channel is already in use, continuing anyway.
Use GPIO.setwarnings(False) to disable warnings.
'''
GPIO.setwarnings(False)

#########################
## sprawdzenie modu
#########################
mode = GPIO.getmode()
print(mode)

#########################
## ustawianie kanalu
#########################

GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

#ustawienie kilku pinow jednoczesnie
channel_list = [3,5,7]
GPIO.setup(channel_list, GPIO.OUT, initial=GPIO.LOW)

#########################
## zmiana stanu pinu
#########################

GPIO.output(10, GPIO.LOW)
GPIO.output(channel_list, GPIO.HIGH)

#przykladowe ustawienie pinu wejsciowego i sprawdzenie stanu
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
print(GPIO.input(12))
print(GPIO.input(13))

#########################
## sprawdzanie informacji o pinie
#########################

func = GPIO.gpio_function(10)
print(str(func))
#zwroci jedna z wartosci ponizej
#GPIO.IN, GPIO.OUT, GPIO.SPI, GPIO.I2C, GPIO.HARD_PWM, GPIO.SERIAL, GPIO.UNKNOWN

#czyszczenie stanu i/o
GPIO.cleanup(3)
GPIO.cleanup(channel_list)
GPIO.cleanup()