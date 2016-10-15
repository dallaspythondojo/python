from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'loginregdb')
app.secret_key = 'ThisIsSecret'

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

# To fix for later: I want to make it so that when user logs in, the session will clear
# but the userid is saved so that they can stay logged in. However, if I clear the session
# before index reloads, my successful login/registration flash messages are also destoryed.
# Played with different solutions including .pop('first_name') but that also erases my
# flash messages somehow.

@app.route('/')
def index():
  print session
  if 'first_name' not in session:
    session['first_name']=""
    session['last_name']=""
    session['email']= ""
    session['con_pw']=""
    session['email1']=""
    session['reg_vs_login'] = "" #this tracks if user is trying to login or register
  if 'id' not in session:
    session['id']= ""
    userinfo = [{'first_name': "", 'last_name': ""}]
  else:
    user_query = "SELECT * FROM user WHERE user_id = :id"
    query_data = { 'id': session['id'] }
    userinfo = mysql.query_db(user_query, query_data)
    if not userinfo:
      userinfo = [{'first_name': "", 'last_name': ""}]
  print userinfo
  return render_template("index.html", user=userinfo)

@app.route('/register', methods=['POST'])
def register():
  verify = True
  session['reg_vs_login'] = "Reg"
  session['first_name'] = request.form['first_name']
  session['last_name'] = request.form['last_name']
  session['email'] = request.form['email']
  session['con_pw'] = request.form['con_password']

  #note to future self: maybe it's possible to separate this check into a different funtion 'check()'
  # and instead of if verify==True, I can do if check(): then run this.
  # to reuse this same check function for the login, maybe make a separate check2() function
  # that checks just the email and password parameters that can be called within check() to
  # simplify code

  if len(session['first_name']) < 2 or len(session['last_name']) < 2:
    flash("Name (First and Last) cannot be less than 2 characters!", "error")
    verify=False
  elif session['first_name'].isalpha() == False or session['last_name'].isalpha() == False:
    flash("Name (First or Last) can only contain letters!", "error")
    verify=False

  if len(session['email']) < 1:
    flash("Email field cannot be empty!", "error")
    verify=False
  elif not EMAIL_REGEX.match(session['email']):
    flash("Invalid Email Format!", "error")
    verify=False

  if len(request.form['password'])<8:
    flash("Password must contain at least 8 characters!!", "error")
    verify=False
  elif request.form['password'] != session['con_pw']:
    flash("Passwords do not match!!", "error")
    verify=False

  if verify==True:
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    insert_query = "INSERT INTO user (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :pw_hash)"
    query_data = { 'first_name': session['first_name'], 'last_name': session['last_name'], 'email': session['email'], 'pw_hash': pw_hash }
    session['id']= mysql.query_db(insert_query, query_data)
    session['reg_vs_login'] = "Reg"
    flash("Thank you! Your information has been submitted!", "confirmation")
    flash("Login Successful!", "confirmation")
    user_query = "SELECT * FROM user WHERE user_id = :id"
    query_data = { 'id': session['id'] }
    userinfo = mysql.query_db(user_query, query_data)
    return render_template('success.html', user=userinfo)

  return redirect('/')

@app.route('/login', methods=['POST'])
def login():
  verify = True
  session['reg_vs_login'] = "Login"
  session['email1'] = request.form['email1']

  if len(session['email1']) < 1:
      flash("Email field cannot be empty!", "error")
      verify=False
  elif not EMAIL_REGEX.match(session['email1']):
      flash("Invalid Email Format!", "error")
      verify=False

  if verify==True:
    password = request.form['password1']
    user_query = "SELECT * FROM user WHERE email = :email LIMIT 1"
    query_data = { 'email': session['email1'] }
    user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['password'], password):
        session['id'] = user[0]['user_id']
        flash("Login Successful!", "confirmation")
        user_query = "SELECT * FROM user WHERE user_id = :id"
        query_data = { 'id': session['id'] }
        userinfo = mysql.query_db(user_query, query_data)
        return render_template('success.html', user=userinfo)
    else:
        flash("Email and/or Password is incorrect!", "Error")
  return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
