from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep

serial = spi(device=0, port=0)
device = sh1106(serial, rotate=0)

# Box and text rendered in portrait mode
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")

while True:
    for x in range(0,255,5):
        device.contrast(x)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((3, 3), "Brightness:" + str(x/255*100)[0:5] + "%", fill="white")
        sleep(0.05)
    with canvas(device) as draw:
            draw.text((10, 40), "Test done", fill="white")
    sleep(3)
