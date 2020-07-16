# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    user_character = request.form["character"]
    
    quote=""
    if user_character == "yoda":
        quote = "Do or do not there is no try"
    elif user_character == "anakin skywalker":
        quote = "I don't like sand"
    elif user_character == "obi wan":
        quote = "Hello there"
    elif user_character == "princess leia":
        quote = "May the Force be with you"
    elif user_character == "luke skywalker":
        quote = "You're Overconfidence Is Your Weakness."
    else: 
        return "Please Type a Star Wars character"
    
    return render_template("results.html", user_character=user_character, quote=quote, time=datetime.now())
