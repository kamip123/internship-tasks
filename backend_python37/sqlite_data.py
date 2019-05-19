import sqlite3
from sqlite3 import Error
from main import read_csv
from api_data import get_data


def create_table(conn, create_table_ssc):
    try:
        c = conn.cursor()
        c.execute(create_table_ssc)
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


def put_data_to_database(conn, cur, file_values):
    sql = ''' INSERT INTO ssc(scope,action,gender,year,amount)
                  VALUES(?,?,?,?,?) '''

    for data in file_values:
        data_set = (data.scope, data.action, data.gender, int(data.year), int(data.amount))
        cur.execute(sql, data_set)

    conn.commit()


def get_all_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM ssc")
    rows = cur.fetchall()

    if len(rows) < 1:
        # column_names, file_values = read_csv('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv')
        file_values = get_data()
        put_data_to_database(conn, cur, file_values)
        cur.execute("SELECT * FROM ssc")
        rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = "ssc_results.db"
    sql_create_ssc_table = """CREATE TABLE IF NOT EXISTS ssc (
                                id integer PRIMARY KEY,
                                scope text NOT NULL,
                                action text NOT NULL,
                                gender text NOT NULL,
                                year integer  NOT NULL,
                                amount integer  NOT NULL
                            ); """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_ssc_table)
        print('Connection successful!')
        get_all_data(conn)
    else:
        print('Connection error!')


if __name__ == '__main__':
    main()

