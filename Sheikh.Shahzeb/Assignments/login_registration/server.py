from flask import Flask,request,redirect,render_template,session,flash
import re
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask.ext.bcrypt import Bcrypt
app= Flask(__name__)
bcrypt= Bcrypt(app)
mysql= MySQLConnector(app, 'login_registration')

@app.route('/')
def index():
	if 'user' in session:
		return redirect('/success')
	return render_template('index.html')

@app.route('/sign_up', methods= ['POST'])
def process():
	if len(request.form['email']) >0:
		email=request.form['email']
	if len(request.form['username']) >0:
		username=request.form['username']
	if len(request.form['password']) >0:
		password=request.form['password']
	pw_hash = bcrypt.generate_password_hash(password)
	insert_query= 'INSERT INTO users(email,username, password,created_at) VALUES(:email,:username,:password,NOW())'
	query_data = {'email':email, 'username': username, 'password': pw_hash}
	mysql.query_db(insert_query, query_data)
	return redirect('/success')

@app.route('/success')
def success():
	return render_template('/success.html')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	username = request.form['username']
	password = request.form['password']
	user_query = "SELECT * FROM users WHERE email = :email"
	query_data = {'email':email}
	user = mysql.query_db(user_query, query_data)

	if bcrypt.check_password_hash(user[0]['password'], password):
		return redirect('/success')
	else: 
		flash('there was an error')
		return redirect('/')
	return redirect(/'login_success')

@app.route('/login_success')
def login_success():
	return render_template('login_success.html')








app.run(debug=True)