from flask import Flask, render_template, session, request, redirect, flash
import re

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<pagename>')
def ninjapage(pagename):
    # ninja = 'images/tmnt.png'
    if pagename == "ninja":
        pagename = 'images/tmnt.png'
    return render_template('ninja.html', pagename=pagename)

@app.route('/ninja/<pagename>')
def show_user_profile(pagename):
    
    if pagename == "blue":
        pagename = 'images/leonardo.jpg'
    elif pagename == "orange":
        pagename = 'images/michelangelo.jpg'
    elif pagename == "red":
        pagename = 'images/raphael.jpg'
    elif pagename == "purple":
        pagename = 'images/donatello.jpg'
    else: pagename = 'images/notapril.jpg'
    return render_template("ninja.html", pagename=pagename)


if __name__ == '__main__':
  app.run(debug = True)

  
