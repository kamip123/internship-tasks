from data_class import MaturaResults


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
