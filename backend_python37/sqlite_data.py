import sqlite3
from sqlite3 import Error

from csv_data import read_csv
from data_class import MaturaResults


def create_table():
    conn = create_connection("ssc_results.db")

    sql_create_ssc_table = """CREATE TABLE IF NOT EXISTS ssc (
                                    id integer PRIMARY KEY,
                                    scope text NOT NULL,
                                    action text NOT NULL,
                                    gender text NOT NULL,
                                    year integer  NOT NULL,
                                    amount integer  NOT NULL
                                ); """
    try:
        cur = conn.cursor()
        cur.execute(sql_create_ssc_table)
        conn.commit()
    except Error as e:
        print(e)


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def put_data_to_database(file_values):
    conn = create_connection("ssc_results.db")
    cur = conn.cursor()

    if type(file_values) == int:
        print('Otrzymano niepoprawne dane.')
        return -1

    sql = 'DELETE FROM ssc'
    cur.execute(sql)
    conn.commit()

    sql = ''' INSERT INTO ssc(scope,action,gender,year,amount)
                  VALUES(?,?,?,?,?) '''

    for data in file_values:
        data_set = (data.scope, data.action, data.gender, int(data.year), int(data.amount))
        cur.execute(sql, data_set)

    conn.commit()


def get_all_data():
    conn = create_connection("ssc_results.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ssc")
    rows = cur.fetchall()

    if len(rows) < 1:
        column_names, file_values = read_csv('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv')
        put_data_to_database(file_values)
        cur.execute("SELECT * FROM ssc")
        rows = cur.fetchall()

    file_values = [MaturaResults(values[1], values[2], values[3], values[4], values[5]) for values in rows]

    return file_values


def main():
    database = "ssc_results.db"

    conn = create_connection(database)
    if conn is not None:
        create_table()
        print('Connection successful!')
        get_all_data()
    else:
        print('Connection error!')


if __name__ == '__main__':
    main()

