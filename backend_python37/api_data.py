import urllib.request as request
import json
from main import MaturaResults


def get_data():
    with request.urlopen('https://api.dane.gov.pl/resources/17201/data?page=1') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
            return -1

    if data['links']['self'] != data['links']['last']:
        data_of_ssc = [data['attributes'] for data in data['data']]
        last_page = data['links']['last']
        last_page = last_page[last_page.find('page=')+5:]

        for i in range(2, int(last_page)+1):
            with request.urlopen('https://api.dane.gov.pl/resources/17201/data?page=' + str(i)) as response:
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

    file_values = [MaturaResults(values['col1'], values['col2'], values['col3'], values['col4'], values['col5']) for values in data_of_ssc]

    return file_values


def main():
    get_data()


if __name__ == '__main__':
    main()
