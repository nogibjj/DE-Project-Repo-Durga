'''Script to create a database and connect to it'''
import sqlite3
import csv

def create_table(query,db_name):
    '''create a database and connect to it'''
    connect = sqlite3.connect(db_name)
    cursor = connect.cursor()
    cursor.execute(query)
    connect.commit()
    connect.close()


def insert_data(query,db_name,filePath):
    '''insert data into the database'''
    connect = sqlite3.connect(db_name)
    cursor = connect.cursor()
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #ignore first row
            if reader.line_num == 1:
                continue
            cursor.execute(query, row)
            print(row)
        connect.commit()
        connect.close()

def read_data(query,db_name):
    '''read data from the database'''
    connect = sqlite3.connect(db_name)
    cursor = connect.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connect.close()

if __name__ == "__main__":
    create_table('CREATE TABLE if not exists movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, genres TEXT NULL)', 'movies.db')
    insert_data('INSERT INTO movies(id, title,genres) VALUES(?,?,?)', 'movies.db','/workspaces/DE-Project-Repo-Durga/data/ml-25m/movies.csv')
    read_data('''SELECT * FROM movies limit 10''', 'movies.db')
    

    #create a table for ratings
    create_table('CREATE TABLE if not exists ratings (userId INTEGER NOT NULL, movieId INTEGER NOT NULL, rating REAL NOT NULL, timestamp INTEGER NOT NULL)', 'movies.db')
    insert_data('INSERT INTO ratings(userId, movieId,rating,timestamp) VALUES(?,?,?,?)', 'movies.db','/workspaces/DE-Project-Repo-Durga/data/ml-25m/ratings.csv')
    read_data('''SELECT * FROM ratings limit 10''', 'movies.db')

    #create a table for tags
    create_table('CREATE TABLE if not exists tags (userId INTEGER NOT NULL, movieId INTEGER NOT NULL, tag TEXT NOT NULL, timestamp INTEGER NOT NULL)', 'movies.db')
    insert_data('INSERT INTO tags(userId, movieId,tag,timestamp) VALUES(?,?,?,?)', 'movies.db','/workspaces/DE-Project-Repo-Durga/data/ml-25m/tags.csv')
    read_data('''SELECT * FROM tags limit 10''', 'movies.db')

    #create a table for links
    create_table('CREATE TABLE if not exists links (movieId INTEGER NOT NULL, imdbId INTEGER NOT NULL, tmdbId INTEGER NOT NULL)', 'movies.db')
    insert_data('INSERT INTO links(movieId, imdbId,tmdbId) VALUES(?,?,?)', 'movies.db','/workspaces/DE-Project-Repo-Durga/data/ml-25m/links.csv')
    read_data('''SELECT * FROM links limit 10''', 'movies.db')

    #create a table for genome_scores
    create_table('CREATE TABLE if not exists genome_scores (movieId INTEGER NOT NULL, tagId INTEGER NOT NULL, relevance REAL NOT NULL)', 'movies.db')
    insert_data('INSERT INTO genome_scores(movieId, tagId,relevance) VALUES(?,?,?)', 'movies.db','/workspaces/DE-Project-Repo-Durga/data/ml-25m/genome-scores.csv')
    read_data('''SELECT * FROM genome_scores limit 10''', 'movies.db')

    #create a table for genome_tags
    create_table('CREATE TABLE if not exists genome_tags (tagId INTEGER NOT NULL, tag TEXT NOT NULL)', 'movies.db')
    insert_data('INSERT INTO genome_tags(tagId, tag) VALUES(?,?)', 'movies.db','/workspaces/DE-Project-Repo-Durga/data/ml-25m/genome-tags.csv')
    read_data('''SELECT * FROM genome_tags limit 10''', 'movies.db')

    #create a table for links
    create_table('CREATE TABLE if not exists links (movieId INTEGER NOT NULL, imdbId INTEGER NOT NULL, tmdbId INTEGER NOT NULL)', 'movies.db')
    insert_data('INSERT INTO links(movieId, imdbId,tmdbId) VALUES(?,?,?)', 'movies.db','/workspaces/DE-Project-Repo-Durga/data/ml-25m/links.csv')
    read_data('''SELECT * FROM links limit 10''', 'movies.db')
