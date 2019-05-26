import urllib.request as request
import json
import threading
import time

from data_class import MaturaResults


def show_loading_screen():
    print('Ładowanie', end="")
    while getattr(threading.currentThread(), "run", True):
        time.sleep(1)
        print('.', end="")


def get_data():
    show_loading = threading.Thread(target=show_loading_screen, daemon=True)
    show_loading.start()

    api_number = open("api_number.txt").readline().rstrip()

    try:
        response = request.urlopen('https://api.dane.gov.pl/resources/' + api_number + '/data?page=1')
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('\nAn error occurred while attempting to retrieve data from the API.\n')
            return 1
    except:
        print('\nAn error occurred while attempting to retrieve data from the API.\n')
        return 1

    if data['links']['self'] != data['links']['last']:
        data_of_ssc = [data['attributes'] for data in data['data']]
        last_page = data['links']['last']
        last_page = last_page[last_page.find('page=') + 5:]

        for i in range(2, int(last_page) + 1):
            with request.urlopen(
                    'https://api.dane.gov.pl/resources/' + api_number + '/data?page=' + str(i)) as response:
                if response.getcode() == 200:
                    source = response.read()
                    data = json.loads(source)

                    for data in data['data']:
                        data_of_ssc.append(data['attributes'])
                else:
                    print('An error occurred while attempting to retrieve data from the API.')
                    return -1
    else:
        data_of_ssc = [data['attributes'] for data in data['data']]

    file_values = [
        MaturaResults(values['col1'], values['col2'], values['col3'], int(values['col4']), int(values['col5'])) for
        values in data_of_ssc]
    show_loading.run = False
    time.sleep(1)
    print('\nDane pobrano pomyślnie.')

    return file_values


def main():
    get_data()


if __name__ == '__main__':
    main()
