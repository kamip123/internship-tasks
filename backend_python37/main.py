import random


class MaturaResults:
    def __init__(self, scope, action, gender, year, amount):
        self.scope = scope
        self.action = action
        self.gender = gender
        self.year = year
        self.amount = amount

    def __str__(self):
        return self.scope + ' ' + self.action + ' ' + self.gender + ' ' + self.year + ' ' + self.amount


class Prefecture:
    def __init__(self, name):
        self.name = name
        self.maturaResults = []

    def pass_ratio(self, year, gender="both"):
        temp_attended = 0
        temp_passed = 0
        for result in self.maturaResults:
            if int(result.year) == year:
                if result.action == 'przystąpiło':
                    temp_attended += int(result.amount)
                elif result.action == 'zdało':
                    temp_passed += int(result.amount)
        ratio = temp_passed * 100 / temp_attended
        return ratio

    def find_year(self, year):
        for result in self.maturaResults:
            if result.year == str(year):
                return True
        return False

    def regression(self, year_start, year_end):
        if not self.find_year(year_start):
            return -1
        if not self.find_year(year_end):
            return -1

        for year in range(year_start + 1, year_end):
            if self.pass_ratio(year) < self.pass_ratio(year-1):
                print('wojewodztwo: ' + str(self.name) + ':' + str(year-1) + ' -> ' + str(year))

    def find_min_max_years(self):
        temp_years = [int(result.year) for result in self.maturaResults]
        return min(temp_years), max(temp_years)

    def pass_ratio_all(self, print_result=True):
        min_year, max_year = self.find_min_max_years()
        result = []
        for year in range(min_year, max_year):
            ratio = self.pass_ratio(year)
            if print_result:
                print(self.name + ' ' + str(year) + ': ' + str(ratio))
            result.append(ratio)
        return result, min_year, max_year

    def __str__(self):
        return self.name + ' ' + str(len(self.maturaResults))


def read_csv(file_name):
    column_names = None
    file_values = []
    counter = 0

    for line in open(file_name, "r"):
        if counter == 0:
            values = line.split(';')
            column_names = [value.rstrip() for value in values]
            counter += 1
        else:
            values = line.split(';')
            file_values.append(MaturaResults(values[0], values[1], values[2], values[3], values[4]))

    return column_names, file_values


def main():
    # static values
    file_name = 'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv'
    year = 2010
    first_prefecture = 1
    second_prefecture = 2
    regression_year_start = 2010
    regression_year_end = 2018

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

    # ratio all
    print('\nratio for first prefecture\n')
    prefectures[first_prefecture].pass_ratio_all()

    # ratio one year for everything
    print('\nratio for all prefectures\n')
    for index in range(len(prefectures_names)):
        print(str(prefectures[index].name) + ' ' + str(prefectures[index].pass_ratio(year)))

    # best prefecture
    temp_ratios = []
    for prefecture in prefectures:
        temp_ratios.append(prefecture.pass_ratio(year))

    print('\nBest prefecture in year: ' + str(year) + ' is: ' + str(prefectures[temp_ratios.index(max(temp_ratios))].name) + ' with a score of: ' + str(max(temp_ratios)))

    # regression
    print('\nRegression in prefectures: \n')
    for prefecture in prefectures:
        prefecture.regression(regression_year_start, regression_year_end)

    # compare
    print('\nCompare 2 prefectures\n')
    print('Comparing ' + prefectures[first_prefecture].name + ' and ' + prefectures[second_prefecture].name)
    ratios_first, min_year_first, max_year_first = prefectures[first_prefecture].pass_ratio_all(False)
    ratios_second, min_year_second, max_year_second = prefectures[second_prefecture].pass_ratio_all(False)

    if min_year_first > min_year_second:
        print('There are more results for first set. Can not compare. Aborting...')
    elif min_year_first < min_year_second:
        print('There are more results for second set. Can not compare. Aborting...')
    else:
        temp_year = min_year_first
        for i in range(len(ratios_first)):
            if ratios_first[i] > ratios_second[i]:
                print(str(temp_year) + ' ' + str(prefectures[first_prefecture].name))
            elif ratios_first[i] < ratios_second[i]:
                print(str(temp_year) + ' ' + str(prefectures[second_prefecture].name))
            else:
                print(str(temp_year) + ' ' + str(prefectures[first_prefecture].name) + ' ' + str(prefectures[second_prefecture].name))
            temp_year += 1


if __name__ == '__main__':
    main()

# todo
# obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa w danym roku, np. 2015 - 123456
# api
# test / almost
# sqlite / almost
# readme
