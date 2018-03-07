from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
import os.path
from PIL import Image, ImageSequence
from luma.core.sprite_system import framerate_regulator

def main():
    regulator = framerate_regulator(fps=10)
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'images', 'banana.gif'))
    banana = Image.open(img_path)
    size = [min(*device.size)] * 2
    posn = ((device.width - size[0]) // 2, device.height - size[1])

    while True:
        for frame in ImageSequence.Iterator(banana):
            with regulator:
                background = Image.new("RGB", device.size, "white")
                background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                device.display(background.convert(device.mode))

if __name__ == "__main__":
    try:
        serial = spi(device=0, port=0)
        device = sh1106(serial, rotate=0)
        main()
    except KeyboardInterrupt:
        pass