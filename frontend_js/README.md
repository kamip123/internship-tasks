# Program, który pobiera dane z api i pozwala nimi manipulować.

### Możliwości:

 1. Pobranie danych z internetowego api.
 2. Przekształcenie danych do prostszej w zrozumieniu struktury.
 3. Sortowanie po title(alfabetycznie), upvotes, score, number of comments, i date of creation.
 4. Znalezienie postu z najwyższym stosunkiem głosów dodatnich do liczby komentarzy.
 5. Wyświetlenie postów tylko z ostatniego dnia (24h wstecz)
 6. Interfejs graficzny.

### Instalacja
```
git clone https://github.com/kamip123/internship-tasks
cd internship-tasks
cd frontend_js
```
Uruchomić index.html za pomocą dowolnie wybranej przeglądarki. 

### Sposób użycia

 1. Po uruchomieniu strony zgodnie z podpunktami w instalacji czekamy na pobranie danych.
 2. Sortujemy dane za pomocą nagłówków lub przycisków na dole strony.
 3. Po kliknięciu na przycisk z ostatnimi postami tabela zostanie zaktualizowana i pokaże ostatnie posty.
 4. Po kliknięciu na najlepszy stosunek polubień do komentarzy, pod przyciskiem wyświetli się wynik.

### Testy

 1. Uruchamiamy tests.html 
 2. Czekamy aż się zakończą.
 3. Sprawdzamy czy wszystkie przeszły. 

### Inne

 1. Dane pochodzą z ```https://www.reddit.com/r/funny.json```
 2. Dane, które pobieram z api i przekształcam do prostszej struktury "posts" mają pole created, które jest w postaci timestamp, aby ułatwić sortowanie. W czasie wyświetlania w tabeli timestamp jest formatowany na datę dd.mm.yyyy hh:mm. 
