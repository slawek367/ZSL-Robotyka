# ZSL-Robotyka
## Folder led_display, 8x8 Led matrix
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
### Virtualenv z zainstalowanymi bibliotekami, w przypadku jak powyższe opcje nie dzialaja
```
Na tej wirtualnej maszynie pythona mamy zainstalowane wszystkie potrzebne biblioteki do uruchomienia skryptów z wyświetlaczem LED matrix 8x8.

sudo pip3 install virtualenv
wchodzimy w repozytorium do: virtual_machine/vm/bin/
odpalamy komende: source activate
przechodzimy do folderu z repo i odpalamy skrypt: python3 screen_test.py
```
