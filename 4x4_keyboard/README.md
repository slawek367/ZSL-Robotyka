# ZSL-Robotyka
## Folder 4x4 keyboard
### instalacja biblioteki oraz jej repozytorium
```
Instalacja biblioteki: pip3 install pad4pi
https://github.com/brettmclean/pad4pi
```
### Podłączenie
```
Klawiaturę podłączamy do pinow GPIO wg numeracji BCM (nazwy z GPIO).
Następnie przy tworzeniu obiektu klawiatury podajemy w parametrach numery użytych pinów np.
keyboard1 = Keyboard(2, 3, 4, 17, 27, 22, 5, 6) w przypadku bazowej klasy
keyboard2 = MyKeyboard(2, 3, 4, 17, 27, 22, 5, 6) w przypadku klasy dziedziczącej
```
### Zadania
```
1. Stwórz program który na wyświetlaczu matrix będzie wyświetlał liczby/litery wciskane na klawiaturze 4x4.
   np. wciskam 1 wyświetlamy 1, wciskam A wyświetlamy A itp.

2. Stwórz program w którym za pomocą klawiszy 2, 4, 6, 8 będziesz mógł przesuwac kropke na wyświetlaczu w różnych kierunkach.
   
   2 - góra
   4 - lewo
   6 - prawo
   8 - dol
   
   W przypadku dojechania do krawędzi kropka powinna przeskoczyć na drugą stronę bądź nie robić nic.

3. Stwórz program który wyświetli na wyświetlaczu komunikat "Wpisz haslo", następnie będzie oczekiwał na wpisanie 4 cyfrowego pinu i zatwierdzenie klawiszem 'A'. Jeśli kod będzie dobry wyświetl "OK", jeśli nie "Zle haslo" i ponów prośbę. Po 3 nieudanych próbach zablokuj możliwość wpisywania hasła i zakończ program.

4. Mini paint, klawiszami 2, 4, 6, 8 przesuwamy kropkę po wyświetlaczu, klawisz A powoduje, że kropka zostaje zaświecona na wyświetlaczu, klawisz B czyści kropkę z wyświetlacza.
```
