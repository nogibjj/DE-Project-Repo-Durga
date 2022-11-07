'''Script to create a database and connect to it'''
import sqlite3
import csv

def create_table():
    '''create a database and connect to it'''
    connect = sqlite3.connect("trends.db")
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE if not exists trends
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    location TEXT NOT NULL,
    year INTEGER NOT NULL,
    category TEXT NOT NULL,
    rank INTEGER NOT NULL,
    query TEXT NOT NULL)''')
    connect.commit()
    connect.close()


def insert_data():
    '''insert data into the database'''
    connect = sqlite3.connect("trends.db")
    cursor = connect.cursor()
    with open('data/trends.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cursor.execute('''INSERT INTO trends(location, year,category, rank, query)
            VALUES(?,?,?,?,?)''', row)
        connect.commit()
        connect.close()

def read_data():
    '''read data from the database'''
    connect = sqlite3.connect("trends.db")
    cursor = connect.cursor()
    cursor.execute('''SELECT * FROM trends limit 10''')
    data = cursor.fetchall()
    for row in data:
        print(row)
    connect.close()

if __name__ == "__main__":
    create_table()
    insert_data()
    read_data()
    
