'''Movies Microservice'''
import sqlite3
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    '''Return a friendly HTTP greeting.'''
    return "Hello World!"

#query movies.db and return top 10 movies
@app.route("/movies")
def movies():
    '''Return a list of top 10 movies'''
    conn = sqlite3.connect('movies.db')
    crsr = conn.cursor()
    crsr.execute("SELECT title FROM movies DESC LIMIT 10")
    _movies = crsr.fetchall()
    _movies = [movie[0] for movie in _movies]
    return jsonify(_movies)

#query movies.db and return top 10 movies of a given genre
@app.route("/movies/<genre>")
def movies_genre(genre):
    '''Return a list of top 10 movies of a given genre'''
    conn = sqlite3.connect('movies.db')
    crsr = conn.cursor()
    crsr.execute("SELECT title FROM movies WHERE genres LIKE '%"+genre+"%' LIMIT 10")
    _movies = crsr.fetchall()
    _movies = [movie[0] for movie in _movies]
    return jsonify(_movies)

#query movies.db and return top 10 movies based on a given tag
@app.route("/movies/tag/<tag>")
def movies_tag(tag):
    '''Return a list of top 10 movies based on a given tag'''
    conn = sqlite3.connect('movies.db')
    crsr = conn.cursor()
    crsr.execute("SELECT title FROM movies WHERE id IN (SELECT movieId FROM tags WHERE tag LIKE '%"+tag+"%') LIMIT 10")
    _movies = crsr.fetchall()
    _movies = [movie[0] for movie in _movies]
    return jsonify(_movies)

#query movies.db and return top 10 movies based on a given rating
@app.route("/movies/rating/<rating>")
def movies_rating(rating):
    '''Return a list of top 10 movies based on a given rating'''
    conn = sqlite3.connect('movies.db')
    crsr = conn.cursor()
    crsr.execute("SELECT title FROM movies WHERE id IN (SELECT movieId FROM ratings WHERE rating = "+rating+") LIMIT 10")
    _movies = crsr.fetchall()
    _movies = [movie[0] for movie in _movies]
    return jsonify(_movies)

#query movies.db and return top 10 movies based on a given year
@app.route("/movies/year/<year>")
def movies_year(year):
    '''Return a list of top 10 movies based on a given year'''
    conn = sqlite3.connect('movies.db')
    crsr = conn.cursor()
    crsr.execute("SELECT title FROM movies WHERE year = "+year+" LIMIT 10")
    _movies = crsr.fetchall()
    _movies = [movie[0] for movie in _movies]
    return jsonify(_movies)

if __name__ == "__main__":
    app.run(host='localhost', port=8080)



