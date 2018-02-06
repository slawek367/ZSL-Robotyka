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
git clone https://github.com/pimylifeup/MFRC522-python.git - stąd pobrane zostały potrzebne biblioteki,
jest to już zawarte w naszym repo więc nie musisz tego pobierać
```
### Uruchomienie
```
Zaktualizuj repozytorium ZSL-Robotyka przy pomocy komendy: git pull -r bądź pobierz na nowo:
git clone https://github.com/slawek367/ZSL-Robotyka.git

Wykonaj pierwsze kroki z instrukcji, podłączenie modułu, włączenie SPI, instalacja potrzebnych bibliotek.
Następnie przejdź do folderu ZSL-Robotyka/rfid_rc522 i zweryfikuj czy wszystko działa poprawnie.

Znajdują się w nim skrypty:

MFRC522.py - potrzebna biblioteka, musi sie znajdować w folderze z odpalanym skryptem
SimpleMFRC522.py - potrzebna biblioteka, musi sie znajdować w folderze z odpalanym skryptem

test_write_rfid.py - Test zapisu karty, odpal jako pierwszy i sprawdź czy karta zapisuje się poprawnie
test_read_rfid.py - Test odczytu, jeśli wszystko zapisało się dobrze powinieneś zobaczyć odczytaną wiadomość z karty oraz jej ID
test_user_managment.py - Wstęp do projektu zarządzania użytkownikami, na tym projekcie możesz bazować wykonując swój

Używamy pythona 2.7 dlatego skrypty uruchamiaj tak: python test_write_rfid.py zamiast python3
```

### Projekt
```
Wykonaj projekt sklepu, który prowadzi sprzedaż za pomocą swoich kart podarunkowych,
Zadbaj o to by znajdowało się tutaj:
- dodawanie/kasowanie użytkowników (klasa User i Users podobnie jak w przykładzie)
- obciążanie użytkownika jakąś kwotą, np kwota 100 zł i pobranie jej po przyłożeniu karty
- wyświetlanie informacji o użytkowniku po przyłożeniu karty
- klasa Store zawierająca listę przedmiotów wraz z ich cenami
- klasa Cart przechowująca listę przedmiotów jakie chcemy kupić

Projekt wykonujemy przez 2-3 zajęcia,
każdy robi tyle ile jest w stanie :)
```
