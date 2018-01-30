# ZSL-Robotyka
## Folder led_display
### Sprawdzenie wersjii pip3
```
pip3 --version
powinna byc 9.0.1
```

### Biblioteka starsza max7219 (instalujemy najpierw, będziemy korzystać z jej metod)
```
sudo apt-get install python3-dev python3-pip
sudo pip3 install max7219
można ją znalezc rowniez tutaj: https://pypi.python.org/pypi/max7219
```
### Biblioteka nowa luma (instalujemy pozniej, potrzebna tylko do konfiguracji spi)
```
sudo usermod -a -G spi,gpio pi
sudo apt-get install build-essential libfreetype6-dev libjpeg-dev
sudo -i pip3 install --upgrade pip setuptools

te 2 ponizej nie uzywamy
#sudo apt-get purge python3-pip
#sudo apt-get install python3-pip

sudo -H pip3 install --upgrade luma.led_matrix
```
