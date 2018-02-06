# ZSL-Robotyka
## Moduł RFID-RC522
### Podłączenie modułu do RPI Zero
```
SDA connects to Pin 24.
SCK connects to Pin 23.
MOSI connects to Pin 19.
MISO connects to Pin 21.
GND connects to Pin 6.
RST connects to Pin 22.
3.3v connects to Pin 1.
```
### Załączenie spi
```
Załączamy SPI

The SPI master driver is disabled by default on Raspbian. To enable it, use raspi-config, or ensure the line dtparam=spi=on isn't commented out in /boot/config.txt, and reboot. If the SPI driver was loaded, you should see the device /dev/spidev0.0.

Sprawdzamy czy spi działa komendą: 

lsmod | grep -i spi
spi_bcm2835             7424  0
```

https://pimylifeup.com/raspberry-pi-rfid-rc522/

### Instalacja biblioteki, dla python 2.7!!! (biblioteka nie działa dla wersji pythona 3)
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python2.7-dev
cd ~
git clone https://github.com/lthiery/SPI-Py.git
cd ~/SPI-Py
sudo python setup.py install

~ oznacza lokalizacje home, można wybrać dowolną
```

### Testowe repozytorium
```
cd ~
git clone https://github.com/pimylifeup/MFRC522-python.git
```
