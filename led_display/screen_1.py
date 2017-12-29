import max7219.led as led
import time
import string
import random

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
pixel(x, y, value, redraw=True) DONE
scroll_down(redraw=True) DONE
scroll_up(redraw=True) DONE
show_message(text, font=None, delay=0.05, always_scroll=False) TODO

Some methods from base device class:
 brightness(intensity)[source] DONE
 clear(deviceId=None)[source] DONE
 command(register, data)[source] NOT
 flush()[source] NOT
 rotate_left(redraw=True)[source] TODO
 rotate_right(redraw=True)[source] TODO
 scroll_left(redraw=True)[source] TODO
 scroll_right(redraw=True)[source] TODO
 set_byte(deviceId, position, value, redraw=True)[source] NOT
'''
# max7219.led.device functions
	
def test_brightness(screen):
	for light_percent in range(0,16):
		print("Setting brightness to: " + str(light_percent) + " [0-15]")
		screen.brightness(light_percent)
		time.sleep(0.2)

# max7219.led.matrix functions

def test_turn_on(screen):
	screen.clear()
	for x in range(0,8):
		for y in range(0,8):
			screen.pixel(x, y, True, redraw=True)
	pass

def test_letters(screen):
	for letter in string.ascii_lowercase:
		screen.letter(0, ord(letter))
		time.sleep(0.1)
		
	for letter in string.ascii_uppercase:
		screen.letter(0, ord(letter))
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

def test_scroll(screen):
	
	for x in range(8):
		number = random.randint(0,1)
		
		if number == 1:
			print("Scroll up")
			screen.scroll_up()
		else:
			print("Scroll down")
			screen.scroll_down()	
		
		time.sleep(1)

def test_pixel(screen):
	screen.clear()
	on_leds = []
	
	for i in range(64):
		
		isAdded = False
		while True:
			x = random.randint(0,7)
			y = random.randint(0,7)
			pos = [x,y]
			
			if pos in on_leds:
				continue
			else:
				on_leds.append(pos)
				break
	
	for x,y in on_leds:
		print("Set ON led X=" + str(x) + " Y=" + str(y))
		screen.pixel(x, y, True, redraw=True)
		time.sleep(0.05)
			
#########################
## Main program
#########################
'''
delay = 1.0

wait(delay, "Testing of letter functions will start in: ")
test_letters(screen1)

wait(delay, "Testing of invert function will start in: ")
test_invert(screen1)

wait(delay, "Testing of orientation function will start in: ")
test_orient(screen1)

wait(delay, "Testing of scroll down and scroll up function will start in: ")
test_scroll(screen1)
print("Did you saw something wrong? Yess.. that function doesn't save LEDs behind screen...")
time.sleep(1)

wait(delay, "Testing of pixel function will start in: ")
test_pixel(screen1)

#########################
## Base class methods
#########################

wait(1.0, "Screen will be turned on in: ")
test_turn_on(screen1)

wait(delay, "Testing of brightness function will start in: ")
test_brightness(screen1)

screen1.clear()
'''