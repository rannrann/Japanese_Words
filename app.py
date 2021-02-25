from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

class WordsType(enum.Enum):
    WORD = 1
    GRAMMAR=2
    COMMON_SAYING=3

class Words(db.Model):
    '''
    id,the mark of every words
    add_time, the time of adding the word
    type, 1 word, 2 grammar, 3 common saying
    '''
    id = db.Column(db.Integer,primary_key=True)
    add_time=db.Column(db.DateTime,default=datetime.utcnow())
    type = db.Column(db.Enum(WordsType))
    detail_words=db.relationship('Detail_Words',backref='words',lazy=True)
    detail_grammar = db.relationship('Detail_Grammar', backref='words', lazy=True)
    statue = db.relationship('Status', backref='words', lazy=True)
class Detail_Words(db.Model):
    '''
    id
    words_id, the mark of the words, linked with Words id
    kana
    meaning
    exemple_sentence
    note
    '''
    id = db.Column(db.Integer, primary_key=True)
    words_id = db.Column(db.Integer,db.ForeignKey('words.id'))
    kana = db.Column(db.Text,nullable=False)
    meaning=db.Column(db.Text,nullable=False)
    exemple_sentence=db.Column(db.Text,nullable=False)
    note=db.Column(db.Text,nullable=True)
class Detail_Grammar(db.Model):
    '''
    id
    words_id,the mark of the words, linked with Words id
    meaning
    noun+
    verb+
    adj-i
    adj-na
    exemple_sentence
    note
    '''
    id = db.Column(db.Integer, primary_key=True)
    words_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    meaning=db.Column(db.Text,nullable=False)
    noun=db.Column(db.Text,nullable=False)
    verb = db.Column(db.Text,nullable=False)
    adj_i=db.Column(db.Text,nullable=False)
    adj_na=db.Column(db.Text,nullable=False)
    exemple_sentence = db.Column(db.Text, nullable=False)
    note = db.Column(db.Text, nullable=True)

class status(db.Model):
    '''
    id
    words_id, the mark of the words, linked with Words id
    last_time, the last time when user click the button
    weight, y is memory rate, x is the hour the time has gone. y=1-0.56^0.06. If the user click the "认识" lower
     0.06, click the other button increase 0.06.
    index index is the number of "0.06"
    '''
    id = db.Column(db.Integer, primary_key=True)
    words_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    last_time=db.Column(db.DateTime,default=datetime.utcnow())
    index=db.Column(db.Float,nullable=False,default=0.06)

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
    if request.method == 'POST':
        pass
    else:
        return render_template("add_words.html")

if __name__ == '__main__':
    app.run(debug=True)