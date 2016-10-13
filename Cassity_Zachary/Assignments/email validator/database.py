from flask import Flask, render_template, request, redirect, session,flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'email')
@app.route('/')
def main_page():
    return render_template('sign_up.html')

@app.route('/submit',methods=['POST'])
def submit():
    if not(EMAIL_REGEX.match(request.form['email'])):
        flash('Email is not valid!')
        return redirect('/')
    elif (len(request.form['email']) < 1):
        flash('Email cannot be blank!')
        return redirect('/')
    else:
        flash('Success!')
    session['email'] = request.form['email']
    session['email_list'] = request.form['email']
    query = "INSERT INTO emails (email) VALUES(:email)"
    data = {'email':request.form['email']}
    mysql.query_db(query,data)
    return redirect('/success')

@app.route('/success')
def success():
    query = 'SELECT * FROM emails'
    email = mysql.query_db(query)
    return render_template('success_page.html',email = email)
app.run(debug=True)
