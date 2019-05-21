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
        if gender == "both":
            for result in self.maturaResults:
                if int(result.year) == year:
                    if result.action == 'przystąpiło':
                        temp_attended += int(result.amount)
                    elif result.action == 'zdało':
                        temp_passed += int(result.amount)
        else:
            for result in self.maturaResults:
                if int(result.year) == year:
                    if result.gender == gender:
                        if result.action == 'przystąpiło':
                            temp_attended += int(result.amount)
                        elif result.action == 'zdało':
                            temp_passed += int(result.amount)

        ratio = temp_passed * 100 / temp_attended
        return round(ratio, 3)

    def find_year(self, year):
        for result in self.maturaResults:
            if result.year == str(year):
                return True
        return False

    def regression(self, year_start, year_end, gender="both"):
        if not self.find_year(year_start):
            return -1
        if not self.find_year(year_end):
            return -1

        for year in range(year_start + 1, year_end+1):
            if self.pass_ratio(year) < self.pass_ratio(year-1):
                print('wojewodztwo: ' + str(self.name) + ':' + str(year-1) + ' -> ' + str(year))

    def find_min_max_years(self):
        temp_years = [int(result.year) for result in self.maturaResults]
        return min(temp_years), max(temp_years)

    def pass_ratio_all(self, print_result=True, gender="both"):
        min_year, max_year = self.find_min_max_years()
        result = []
        for year in range(min_year, max_year):
            ratio = self.pass_ratio(year, gender)
            if print_result:
                print(self.name + ' ' + str(year) + ': ' + str(ratio))
            result.append(ratio)
        return result, min_year, max_year

    def approached(self, year, gender="both"):
        temp_attended = 0
        break_point = 0
        if gender == "both":
            for result in self.maturaResults:
                if int(result.year) == year:
                    if result.action == 'przystąpiło':
                        temp_attended += int(result.amount)
                        break_point += 1
                if break_point == 2:
                    break
        else:
            for result in self.maturaResults:
                if int(result.year) == year:
                    if result.action == 'przystąpiło':
                        if result.gender == gender:
                            temp_attended += int(result.amount)
                            break

        return temp_attended

    def __str__(self):
        return self.name + ' ' + str(len(self.maturaResults))
