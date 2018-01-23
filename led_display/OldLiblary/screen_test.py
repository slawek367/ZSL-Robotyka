import max7219test.led as led

device = led.matrix(cascaded = 1)
device.show_message("Hello world!")
