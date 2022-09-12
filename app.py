'''File to run the application'''
from flask import Flask
app = Flask(__name__)

'''Returns a Hello World message when the user visits the root of the website.'''
@app.route("/")
def hello():
    '''Returns a Hello World message when the user visits the root of the website.'''
    return "Hello World!"

if __name__ == "__main__":
    app.run()
