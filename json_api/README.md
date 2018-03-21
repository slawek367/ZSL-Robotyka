### JSON & API REQUESTS
##Przydatne linki
```
Korzystanie z JSON: https://automatetheboringstuff.com/chapter14/
API jakości powietrza: http://powietrze.gios.gov.pl/pjp/content/api
Requests: https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3
```
##Instrukcja
Przykłady znajdziesz w:
examples_json.py
examples_requests.py
##Zadania
```
1. Utwórz klase Player, zawierającą kilka pól np. nickname, gold, map itp,
a następnie stwórz kilka jej obiektów umieszczając je w liście players,
utwórz funkcję Save() która w parametrze przyjmie liste graczy i zapisze ją do pliku,
w formacie JSON oraz Load() która odczyta liste graczy z pliku i zwróci ich listę

2. Za pomocą biblioteki Requests za pomocą zapytania GET pobierz z API: http://api.gios.gov.pl/pjp-api/rest/station/findAll
listę wszystkich stacji pomiarowych powietrza i zapisz do listy tylko te,
które znajdują się w Krakowie

3. Posiadając liste stacji z Krakowa, pobierz z pierwszych pięciu ich id,
a następnie wyślij 5 requestów na adres http://api.gios.gov.pl/pjp-api/rest/station/sensors/id -> gdzie id podaj numer stacji,
w odpowiedzi otrzymasz listy sensorów jakie dana stacja zawiera, wyświetl te informacje dla konsoli

4. Dla danych id czujników z określonej stacji, wyślij requesty na adres,
http://api.gios.gov.pl/pjp-api/rest/data/getData/id_czujnika,
a następnie wyświetl pomiary z danego czujnika na konsoli
```