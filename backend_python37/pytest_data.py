import pytest
from main import MaturaResults


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


def main():
    test_contain_header()
    test_uppercase()
    test_contain_prefecture()


if __name__ == '__main__':
    main()
