import pytest

from data_class import MaturaResults


@pytest.fixture()
def file_data():
    file_name = 'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv'
    file_values = []
    counter = 0

    for line in open(file_name, "r"):
        if counter != 0:
            values = line.split(';')
            file_values.append(MaturaResults(values[0], values[1], values[2], values[3], values[4]))
        else:
            counter += 1

    return file_values


@pytest.fixture()
def header_names():
    file_name = 'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv'
    for line in open(file_name, "r"):
        values = line.split(';')
        column_names = [value.rstrip() for value in values]
        return column_names


def test_uppercase(header_names):
    for header in header_names:
        assert header[0] == header[0].upper()


def test_contain_header(header_names):
    assert 'Terytorium' in header_names
    assert 'Przystąpiło/zdało' in header_names
    assert 'Płeć' in header_names
    assert 'Rok' in header_names
    assert 'Liczba osób' in header_names


def test_contain_prefecture(file_data):
    names = [data.scope for data in file_data]
    assert 'Dolnośląskie' in names
    assert 'Kujawsko-pomorskie' in names
    assert 'Lubelskie' in names
    assert 'Lubuskie' in names
    assert 'Łódzkie' in names
    assert 'Małopolskie' in names
    assert 'Mazowieckie' in names
    assert 'Opolskie' in names
    assert 'Podkarpackie' in names
    assert 'Podlaskie' in names
    assert 'Pomorskie' in names


def test_pefecture_value(file_data):
    assert 'Dolnośląskie' == file_data[36].scope
    assert 'przystąpiło' == file_data[36].action
    assert 'mężczyźni' == file_data[36].gender
    assert 2010 == int(file_data[36].year)
    assert 9951 == int(file_data[36].amount)

    assert 'Kujawsko-pomorskie' == file_data[73].scope
    assert 'przystąpiło' == file_data[73].action
    assert 'kobiety' == file_data[73].gender
    assert 2010 == int(file_data[73].year)
    assert 10636 == int(file_data[73].amount)


def main():
    test_contain_header()
    test_uppercase()
    test_contain_prefecture()
    test_pefecture_value()


if __name__ == '__main__':
    main()
