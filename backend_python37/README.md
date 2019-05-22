# Program, który pozwala przeanalizować wyniki matur.
### Możliwości:

 1. Pokazanie liczby osób, które przystąpiły do egzaminu w danym roku dla danego województwa.
 2. Obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat.
 3. Znalezienie województwa z najlepszą zdawalnością w danym roku.
 4. Wykrycie regresji na przestrzeni lat.
 5. Porównanie zdawalności w 2 województwach.
 6. Filtrowanie wyników dla płci lub domyślnie wyświetlanie dla obu.
 7. Pobieranie danych z pliku csv.
 8. Pobieranie danych z bazy danych SQLite.
 9. Pobieranie danych z internetowego API.


### Instalacja:
```
git clone https://github.com/kamip123/internship-tasks
cd internship-tasks
cd backend_python37
pip install -r requirements.txt
python main.py
```
### Inne

1. Dane pochodzą z: `https://dane.gov.pl/dataset/1567/resource/17363`

2. Rekordy dla Polski traktuje tak samo jak inne województwa. W ten sposób można porównywać wyniki województwa do wyniku ogólnokrajowego.

3. Zadanie pierwsze zinterpretowałem jako: Pokazanie liczby osób, które przystąpiły do egzaminu dla danego województwa w danym roku z możliwością podziału na płcie.






