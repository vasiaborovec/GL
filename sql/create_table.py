import sqlite3
from sqlite3 import Error

def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None
def main():
    database = "pythonsqlite.db"

    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS Users (
                                        id_user integer PRIMARY KEY,
                                        first_name text NOT NULL,
                                        status text,
                                        block_date DATE,
                                        attempt_date DATE 
                                    ); """

    sql_create_comment_table = """CREATE TABLE IF NOT EXISTS Comments (
                                    id_comment integer PRIMARY KEY,
                                    comment text NOT NULL,
                                    id_user INTEGER ,
                                    FOREIGN KEY (id_user) REFERENCES Users (id_user)
                                );"""


    conn = create_connection(database)

    if conn is not None:

        create_table(conn, sql_create_user_table)
        create_table(conn, sql_create_comment_table)

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()


