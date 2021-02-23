from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

class Words:
    '''

    '''
    pass
class Detail:
    pass

@app.route("/")
def index():
    '''
    The home page displays the first word the user need to study. Ideally, there are three buttons that indicate
    the user how familiar to the word.
    User can study the next word if he(or she) click one of the buttons.
    '''
    return "this is home page!"

@app.route("/add_words")
def add_words():
    '''
    add_words page is like the name. the words need to be non-repetitive(database achieve that) and existed
    (dictionary? tiretree?). Also, the ui is different from "word" and "grammar". "word" page emphasizes
    the meaning and the environment it can use, "grammar" page stresses the rule and the enviroment. So the
    example sentence is really important.
    '''
    return "add"

if __name__ == '__main__':
    app.run(debug=True)