import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #zawsze uzywajmy tego modu
GPIO.setwarnings(False)

#######################################################################################
## Pull up and pull down
#######################################################################################

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(10):
	print("Pin [10] state High")
else:
	print("Pin [10] state Low")
	
#######################################################################################
## Oczekiwanie na zbocze np. opadajace (GPIO.RISING, GPIO.FALLING, GPIO.BOTH)
#######################################################################################

GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) #stan wysoki, wyzwalanie stanem niskim
print("Waiting 5 for low state on pin [37]")
response = GPIO.wait_for_edge(37, GPIO.FALLING, timeout=5000)

if response is None:
	print("State was not changed")
else:
	print("Failing edge detected!")

#########################
## event_detected()
#########################

GPIO.cleanup(37)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) #stan wysoki, wyzwalanie stanem niskim

GPIO.add_event_detect(37, GPIO.FALLING, bouncetime=200)

counter = 0
print("Testing event_detected, please press 5 times pin 37")
while counter < 5:
	if GPIO.event_detected(37):
		counter+=1
		print("Button [37] pressed " + str(counter) + " times")

#########################
## threaded callback
#########################

def someFunction(channel):
	print("Some function started")

GPIO.cleanup(37)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(37, GPIO.FALLING, bouncetime=200)

#adding function to event
GPIO.add_event_callback(37, someFunction)

while True:
	print("while loop running...")
	time.sleep(1)
	
#########################
## removing detection
#########################

GPIO.remove_event_detect(37)

#Clean
GPIO.cleanup()