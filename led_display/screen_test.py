import max7219.led as led
from luma.core.interface.serial import spi, noop
serial = spi(port=0, device=0, gpio=noop())
device = led.matrix(cascaded = 1)
device.show_message("Hello world!")
