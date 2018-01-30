from pad4pi import rpi_gpio
import sys

class Keyboard():

    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8):
        self.KEYPAD = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"]
        ]

        self.ROW_PINS = [p1, p2, p3, p4] # BCM numbering (GPIO.. number), first 4 pins
        self.COL_PINS = [p5, p6, p7, p8] # next 4 left pins

        self.factory = rpi_gpio.KeypadFactory()
        self.keypad = self.factory.create_keypad(keypad=self.KEYPAD, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)
        self.keypad.registerKeyPressHandler(self.processKey)

    def processKey(self, key):
        if (key == "1"):
            print("Pressed 1")
        elif (key == "2"):
            print("Pressed 2")
        elif (key == "3"):
            print("Pressed 3")
        elif (key == "4"):
            print("Pressed 4")
        elif (key == "5"):
            print("Pressed 5")
        elif (key == "6"):
            print("Pressed 6")
        elif (key == "7"):
            print("Pressed 7")
        elif (key == "8"):
            print("Pressed 8")
        elif (key == "9"):
            print("Pressed 9")
        elif (key == "0"):
            print("Pressed 0")
        elif (key == "*"):
            print("Pressed *")
        elif (key == "#"):
            print("Pressed #")
        elif (key == "A"):
            print("Pressed A")
        elif (key == "B"):
            print("Pressed B")
        elif (key == "C"):
            print("Pressed C")
        elif (key == "D"):
            print("Pressed D, exiting...")
            sys.exit()

#use this class directly
#keyboard1 = Keyboard(2, 3, 4, 17, 27, 22, 5, 6)

#or create your own  class with own processKey function:
class MyKeyboard(Keyboard):
      
      def processKey(self, key):
            print("Pressed:" + key)

keyboard2 = MyKeyboard(2, 3, 4, 17, 27, 22, 5, 6)

#infinite loop
while True:
    pass