import max7219.led as led
import time
import string
import threading

def wait(wait_time, text):
	actual_time = time.time()
	wait_to = actual_time + wait_time
	
	while time.time() < wait_to:
		print("---> " + text + str(wait_time - (time.time() - actual_time))[0:4], end="\r")
		time.sleep(0.01)
	
	print("\nTesting ongoing...\n")

#Create screen
screen1 = led.matrix(cascaded = 1)
print("Object screen1 created.")

#########################
## Methods
#########################
'''
#There you could see all methods from max7219.led.matrix class
#https://max7219.readthedocs.io/en/0.2.3/max7219.html#module-max7219.led

invert(value, redraw=True) DONE
letter(deviceId, asciiCode, font=None, redraw=True) DONE
orientation(angle, redraw=True) DONE
pixel(x, y, value, redraw=True) TODO
scroll_down(redraw=True) TODO
scroll_up(redraw=True) TODO
show_message(text, font=None, delay=0.05, always_scroll=False) TODO
'''

def test_letters():
	for letter in string.ascii_lowercase:
		screen1.letter(0, ord(letter))
		time.sleep(0.1)
		
	for letter in string.ascii_uppercase:
		screen1.letter(0, ord(letter))
		time.sleep(0.1)

def test_invert(screen):
	is_inverted = False
	
	for x in range(8):
		is_inverted = not is_inverted
		screen.invert(is_inverted)
		time.sleep(0.5)

def test_orient(screen):
	
	degrees = (0, 90, 180, 270)
	
	for degree in degrees:
		print("Set orientation to: " + str(degree) + " degrees")
		screen.orientation(degree)
		time.sleep(1)
	
	screen.orientation(0)

wait(3.0, "Testing of letter functions will start in: ")
test_letters()

wait(3.0, "Testing of invert function will start in: ")
test_invert(screen1)

wait(3.0, "Testing of orientation function will start in: ")
test_orient(screen1)
