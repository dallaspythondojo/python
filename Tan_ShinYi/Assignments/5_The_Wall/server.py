from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import datetime
from datetime import timedelta

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'The_Walldb')
app.secret_key = 'ThisIsSecret'

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  if 'first_name' not in session:
    session['first_name']=""
    session['last_name']=""
    session['email']= ""
    session['con_pw']=""
    session['email1']=""
    session['reg_vs_login'] = "" #this tracks if user is trying to login or register,
                                 #helps to display flash messages on appropriate part
                                 #of page
  if 'id' not in session:
    session['id']= "" # note to self: in the future, store entire user dictionary in session, instead of just id
    userinfo = [{'first_name': "", 'last_name': ""}]
  elif session ['id'] != "":
    return redirect('/wall')
  return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
  verify = True
  session['reg_vs_login'] = "Reg"
  session['first_name'] = request.form['first_name']
  session['last_name'] = request.form['last_name']
  session['email'] = request.form['email']
  session['con_pw'] = request.form['con_password']

  query = "SELECT email FROM users WHERE email= :email"
  data = { 'email': session['email'] }
  test = mysql.query_db(query, data)
  if len(test)>0: #ensures no two users have the same email address
      flash("Please double check your email.", "error")
      verify=False

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
    insert_query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :pw_hash)"
    query_data = { 'first_name': session['first_name'], 'last_name': session['last_name'], 'email': session['email'], 'pw_hash': pw_hash }
    session['id']= mysql.query_db(insert_query, query_data)
    session['reg_vs_login'] = "Reg"
    return redirect('/wall')

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
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': session['email1'] }
    user = mysql.query_db(user_query, query_data)
    if len(user)<1:
        flash("Email and/or Password is incorrect!", "Error")
    elif bcrypt.check_password_hash(user[0]['password'], password):
        session['id'] = user[0]['id']
        return redirect('/wall')
    else:
        flash("Email and/or Password is incorrect!", "Error")
  return redirect('/')

@app.route('/wall')
def wall():
    if session["id"]=="":
        session['reg_vs_login'] = "Login"
        flash("Please login to access The Wall!", "error")
        return redirect('/')

    #TO-DO: Figure out how to query for comments and messages with single query!
    user_query = "SELECT * FROM users WHERE id = :id"
    query_data = { 'id': session['id'] }
    userinfo = mysql.query_db(user_query, query_data)

    query = "SELECT m.id, u.first_name, u.last_name, DATE_FORMAT(m.created_at, '%M %D, %Y') AS date_created, m.created_at , m.message FROM messages m JOIN users u ON u.id = m.user_id ORDER BY m.created_at DESC"
    messages = mysql.query_db(query)

    query = "SELECT c.id, c.user_id, u.first_name, u.last_name, DATE_FORMAT(c.created_at, '%M %D, %Y') AS date_created, c.created_at, DATE_FORMAT(c.created_at, '(%Y,%m,%d,%H,%M,%S)') AS created_at2, c.comment, c.message_id FROM comments c JOIN users u ON u.id = c.user_id ORDER BY c.created_at"
    comments = mysql.query_db(query)

    now = datetime.datetime.now()

    return render_template('wall.html', user=userinfo, messages=messages, comments=comments)

@app.route('/message', methods=['POST'])
def message():
    print request.form
    insert_query = "INSERT INTO messages (user_id, message, updated_at) VALUES (:id, :message, NOW())"
    query_data = { 'id': session['id'], 'message':request.form['message'] }
    mysql.query_db(insert_query, query_data)
    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    insert_query = "INSERT INTO comments (message_id, user_id, comment, updated_at) VALUES (:message_id, :id, :comment, NOW())"
    query_data = { 'message_id': request.form['message_id'], 'id': session['id'] , 'comment': request.form['comment'] }
    mysql.query_db(insert_query, query_data)
    return redirect('/wall')

@app.route('/delete/<comment_id>')
def destroy(comment_id):
    query = "DELETE FROM comments WHERE id = :id"
    data = {'id': comment_id}
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

  #Working idea on how to calculate if a post was made within the last 30 minutes
  # so that a post can only be deleted if it was made within the last 30 minutes.
  # Was trying to stick this on the "wall" template around the "delete post" comment
  # but this python code refuses to run within the view. Keeps saying that it's expecting
  # end of if statement if I put everything in {%%} as below. If I put everything in
  # {{}} I keep getting "unexpected '=' at end of print statement"

  # <indent>
  # {% if c['user_id']==session['id'] %}
  #   {% a = datetime.datetime.strptime(c['created_at'],'%Y-%m-%d %H:%M:%S')%}
  #   {% b = datetime.datetime.now() %}
  #   {% c = b - a %}
  #   {% minutes = divmod(c.days * 86400 + c.seconds, 60) %}
  #   {% if minutes[0]<=30 %}
  # </indent>
app.run(debug=True)
