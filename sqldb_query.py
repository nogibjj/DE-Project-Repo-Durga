'''query data from the database'''
import sqlite3


def query_print(query):
    '''query data from the database'''
    connect = sqlite3.connect("trends.db")
    cursor = connect.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connect.close()

if __name__ == "__main__":
    print('\n1. Printing top queries for each year')
    QUERY = '''SELECT year, min(rank),query FROM trends GROUP BY year'''
    query_print(QUERY)

    print('\n1. Printing top 5 queries for year 2020')
    QUERY = '''SELECT query,rank FROM trends where year='2020' GROUP BY rank'''
    query_print(QUERY)

    print('\n3. Printing top searched queries location wise')
    QUERY = '''SELECT distinct location,query from trends where year='2020' and rank='1' group by location'''
    query_print(QUERY)

    print('\n4. Printing top searched queries in the movies category in 2020')
    QUERY = '''SELECT query,rank FROM trends where category='Movies' and year='2020' GROUP BY rank'''
    query_print(QUERY)


