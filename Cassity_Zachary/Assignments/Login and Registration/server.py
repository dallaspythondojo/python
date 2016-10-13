from flask import Flask, render_template, request, redirect,session,flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app =Flask(__name__)
app.secret_key = "secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'registration')
@app.route('/')
def login():
    return render_template('main_page.html')
@app.route('/login', methods=['POST'])
def login_attempt():
    email = request.form['email_login']
    password = request.form['password_login']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1" #Checks if the email stored matches the email entered into the form with only 1 match
    query_data = {'email':email}
    user = mysql.query_db(user_query, query_data)
    if len(request.form['email_login'] and request.form['email_password']) < 1:
        flash('Email and password cannot be blank!')
        return redirect('/')
    if bcrypt.check_password_hash(user[0]['pw_hash'], password): #compares the password entered to the hashed password for a match
        return redirect('/success')
    else:
        flash('Passwords do not match!')
        return redirect('/')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/register_user', methods=['POST'])
def register_user():
    password = request.form['register_password']
    pw_hash = bcrypt.generate_password_hash(password)
    query = 'INSERT INTO users (first_name,last_name,email,pw_hash,created_at,updated_at)VALUES(:first_name,:last_name,:email,:pw_hash,NOW(),NOW())'
    data = {'first_name':request.form['register_first'],'last_name':request.form['register_last'],'email':request.form['register_email'],'pw_hash':pw_hash}
    mysql.query_db(query,data)
    return redirect('/success')
@app.route('/success')
def success():
    return render_template('success.html')
app.run(debug=True)
