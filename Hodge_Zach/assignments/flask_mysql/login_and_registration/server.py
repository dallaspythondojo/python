from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "IsTheShipOutOfDanger"

bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login')

@app.route('/', methods=['GET'])
def index():
    if 'first_name' not in session:
        session['first_name'] = ""
    if 'last_name' not in session:
        session['last_name'] = ""
    if 'email' not in session:
        session['email'] = ""
    if 'password' not in session:
        session['password'] = ""
    if 'confirm_password' not in session:
        session['confirm_password'] = ""
    if 'pw_hash' not in session:
        session['pw_hash'] = ""
    if 'id' not in session:
        session['id'] = ""

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    session['email'] = request.form['email']
    session['password'] = request.form['password']

    query = "SELECT user.email, user.pw_hash FROM user WHERE user.email = :email"

    stuff = {
        'email': session['email']
    }

    data = mysql.query_db(query, stuff)

    if session['email'] == data[0]['email'] and bcrypt.check_password_hash(data[0]['pw_hash'], session['password']):
        return render_template('/success.html', type="Login")
    else:
        flash("Invalid login. Please register")

    return redirect('/')

@app.route('/register', methods=['GET'])
def bring_up_register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    NAME_REGEX = re.compile(r'^[a-z]+^[A-Z]+$')
    EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']



    if len(session['first_name']) < 2 and not NAME_REGEX.match(session['first_name']):
        flash("Invalid name")
        return render_template('register.html')
    else:
        flash("Valid name") #for some reason the if statment won't run without the else

    if len(session['last_name']) < 2 and not NAME_REGEX.match(session['last_name']):
        flash("Invalid name")
        return render_template('register.html')
    else:
        flash("Valid name")

    if len(session['email']) < 1 and not EMAIL_REGEX.match(session['email']):
        flash("Invalid email")
        return render_template('register.html')
    else:
        flash("Valid email")

    if len(session['password']) < 8:
        flash("Invalid password. Must be 8 characters")
        return render_template('register.html')
    else:
        flash("Valid password")

    if session['password'] != session['confirm_password']:
        flash("Passwords must match.")
        return render_template('register.html')
    else:
        flash("Valid password")

    session['pw_hash'] = bcrypt.generate_password_hash(session['password'])

    query = "INSERT INTO user (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"

    data = {
        'first_name': session['first_name'],
        'last_name': session['last_name'],
        'email': session['email'],
        'pw_hash': session['pw_hash']
    }

    mysql.query_db(query, data)
    return render_template('success.html', type='Registration')

app.run(debug=True)
