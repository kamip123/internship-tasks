from data_class import Prefecture
import sqlite_data
from api_data import get_data
from csv_data import read_csv


def compare_two_prefectures(prefectures, first_prefecture, second_prefecture):
    print('\nPorównanie 2 województw\n')
    print('Porównywanie ' + prefectures[first_prefecture].name + ' i ' + prefectures[second_prefecture].name)

    ratios_first, min_year_first, max_year_first = prefectures[first_prefecture].pass_ratio_all(False)
    ratios_second, min_year_second, max_year_second = prefectures[second_prefecture].pass_ratio_all(False)

    if min_year_first > min_year_second:
        print('Ilość danych o pierwszym województwie różni się od drugiego. Przerywam działanie...')
    elif min_year_first < min_year_second:
        print('Ilość danych o drugim województwie różni się od pierwszego. Przerywam działanie...')
    elif max_year_first > max_year_second:
        print('Ilość danych o pierwszym województwie różni się od drugiego. Przerywam działanie...')
    elif max_year_first < max_year_second:
        print('Ilość danych o drugim województwie różni się od pierwszego. Przerywam działanie...')
    else:
        temp_year = min_year_first
        for i in range(len(ratios_first)):
            if ratios_first[i] > ratios_second[i]:
                print(str(temp_year) + ' ' + str(prefectures[first_prefecture].name))
            elif ratios_first[i] < ratios_second[i]:
                print(str(temp_year) + ' ' + str(prefectures[second_prefecture].name))
            else:
                print(str(temp_year) + ' ' + str(prefectures[first_prefecture].name) + ' ' + str(
                    prefectures[second_prefecture].name))
            temp_year += 1


def switch_task(value):
    switch_tasks = {
        '1': "amount",
        '2': "ratio all",
        '3': "best prefecture",
        '4': "regression",
        '5': "compare",
        '6': "quit",
    }
    return switch_tasks.get(value, "wrong")


def switch_data_source(value):
    switch_tasks = {
        '1': "csv",
        '2': "database",
        '3': "api",
        '4': "read from api to database",
    }

    return switch_tasks.get(value, "wrong")


def get_user_request_task():

    print('\n')
    for index in range(48):
        if index == 0:
            print('+', end="")
        elif index == 47:
            print('+')
        else:
            print('-', end="")

    print('| Program do sprawdzania wyników matury:       |')
    print('|                                              |')
    print('| 1: Sprawdz ile osob przystąpiło do egzaminu. |')
    print('| 2: Procentowa zdawalność dla województwa.    |')
    print('| 3: Najlepsze województwo w danym roku.       |')
    print('| 4. Wykrycie regresji na przestrzeni lat.     |')
    print('| 5. Porównanie 2 wojewodztw.                  |')
    print('| 6. Wyjdź z programu.                         |')

    for index in range(48):
        if index == 0:
            print('+', end="")
        elif index == 47:
            print('+')
        else:
            print('-', end="")
    print('Twój wybór: ', end="")
    task_to_do = input()

    task_to_do = switch_task(task_to_do)

    if task_to_do == "wrong":
        return "wrong", "wrong"

    if task_to_do == "quit":
        return "quit", "quit"

    for index in range(45):
        if index == 0:
            print('+', end="")
        elif index == 44:
            print('+')
        else:
            print('-', end="")

    print('| Dane mają być pobrane z:                  |')
    print('|                                           |')
    print('| 1: Plik csv                               |')
    print('| 2: Baza SQLite                            |')
    print('| 3: Api - wymagane połaczenie z internetem |')
    print('| 4. Pobierz dane z api i zapisz do bazy    |')

    for index in range(45):
        if index == 0:
            print('+', end="")
        elif index == 44:
            print('+')
        else:
            print('-', end="")

    print('Twój wybór: ', end="")
    data_source = input()

    data_source = switch_data_source(data_source)

    if data_source == "wrong":
        return "wrong", "wrong"

    return task_to_do, data_source


def main():
    while True:
        # static default values
        file_name = 'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv'
        year = 2010
        first_prefecture = 1
        second_prefecture = 2
        regression_year_start = 2010
        regression_year_end = 2018

        while True:
            task_to_do, data_source = get_user_request_task()
            if task_to_do == "wrong" or data_source == "wrong":
                print('Proszę podać poprawne dane.')
            elif data_source == "read from api to database":
                exam_data_from_api = get_data()
                sqlite_data.create_table()
                sqlite_data.put_data_to_database(exam_data_from_api)
            else:
                break

        if task_to_do == 'quit':
            return 'quit'

        if data_source == "database":
            file_values = sqlite_data.get_all_data()
        elif data_source == "api":
            file_values = get_data()
            if file_values == 1:
                print('Wystąpił błąd w czasie pobierania danych. Wykorzystam plik csv.')
                column_names, file_values = read_csv(file_name)
        else:
            column_names, file_values = read_csv(file_name)

        prefectures_names = []
        for value in file_values:
            if value.scope not in prefectures_names:
                prefectures_names.append(value.scope)

        prefectures = [Prefecture(scope) for scope in prefectures_names]

        for index, prefecture in enumerate(prefectures):
            for value in file_values:
                if value.scope == prefecture.name:
                    prefectures[index].maturaResults.append(value)

        if task_to_do == 'amount':
            print('\nIlośc osób, które podeszły do egzminu\n')
            print(str(prefectures[first_prefecture].name) + ' ' + str(prefectures[first_prefecture].approached(year)))

        elif task_to_do == 'ratio all':
            print('\nŚrednia dla województwa\n')
            prefectures[first_prefecture].pass_ratio_all()

        elif task_to_do == 'best prefecture':
            temp_ratios = [prefecture.pass_ratio(year) for prefecture in prefectures]
            print('\nNajlepsze województwo w roku: ' + str(year) + ' to: ' + str(
                prefectures[temp_ratios.index(max(temp_ratios))].name) + ' z średnią: ' + str(max(temp_ratios)))

        elif task_to_do == 'regression':
            print('\nRegresja w województwach: \n')
            for prefecture in prefectures:
                prefecture.regression(regression_year_start, regression_year_end)

        elif task_to_do == 'compare':
            compare_two_prefectures(prefectures, first_prefecture, second_prefecture)


if __name__ == '__main__':
    main()

# todo
# manually select year and gender
# tests / almost
# readme
