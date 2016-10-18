from flask import Flask, render_template, session, flash, redirect, request
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "I'malumberjackandI'mokay"

mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
    if 'email' not in session:
        session['email'] = ""

    return render_template('index.html')

@app.route('/email', methods=['POST'])
def email_process():
    session['email'] = request.form['email']

    EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

    if len(session['email']) < 1 and not EMAIL_REGEX.match(session['email']):
        flash("Invalid email!")
        return redirect('/')

    flash("It worked!")

    query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"

    data = {
        'email': session['email']
    }

    mysql.query_db(query, data)

    query = "SELECT * FROM email"

    data = mysql.query_db(query)
    return render_template('emails.html', email = session['email'], data = data)

app.run(debug=True)
