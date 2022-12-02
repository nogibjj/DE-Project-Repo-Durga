'''query data from the database'''
import sqlite3


def query_print(query):
    '''query data from the database'''
    connect = sqlite3.connect("movies.db")
    cursor = connect.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connect.close()

if __name__ == "__main__":
    query_print('''SELECT * FROM movies limit 10''')
    query_print('''SELECT * FROM ratings limit 10''')
    query_print('''SELECT * FROM tags limit 10''')
    query_print('''SELECT * FROM links limit 10''')
    query_print('''SELECT * FROM genome_scores limit 10''')
    query_print('''SELECT * FROM genome_tags limit 10''')
    query_print('''SELECT * FROM links limit 10''')
    

