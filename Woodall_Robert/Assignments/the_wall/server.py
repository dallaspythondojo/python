from flask import Flask, request, redirect, render_template, session, flash
from flask.ext.bcrypt import Bcrypt
from mysql_connection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = ')()#&$$FHSO*#H)(U#@#!@E)'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'the_wall')

def validRegistration():
	if (len(request.form['fname']) < 1 or
	    len(request.form['lname']) < 1 or
	    len(request.form['email']) < 1 or
	    len(request.form['pw']) < 1 or
	    len(request.form['confirm_pw']) < 1):
		flash('All inputs required', 'registration_error')
		return False
	elif (len(request.form['fname']) < 2 or 
	      len(request.form['lname']) < 2):
		flash('First and Last name requires at least 2 characters!', 'registration_error')
		return False
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email address format!', 'registration_error')
		return False
	elif (len(request.form['pw']) < 8 or
		  len(request.form['confirm_pw']) < 8):
		flash('Passwords must be at least 8 characters!', 'registration_error')
		return False
	elif not request.form['pw'] == request.form['confirm_pw']:
		flash('Passwords do not match!', 'registration_error')
		return False
	
	return True
		
def validLogin():
	if (len(request.form['login_email']) < 1 or
	    len(request.form['login_pw']) < 1):
		flash('All inputs required', 'login_error')
		return False
	elif not EMAIL_REGEX.match(request.form['login_email']):
		flash('Invalid email address format!', 'login_error')
		return False
	
	return True

def validMessagePost():
	if len(request.form['message_text']) < 1:
		flash('Message content must contain some text!', 'error')
		return False
	
	return True

def validComment():
	if len(request.form['comment_text']) < 1:
		flash('Comment content must contain some text!', 'error')
		return False
	
	return True

@app.route('/')
def login_register():
	return render_template('login_register.html')

@app.route('/login', methods=['POST'])
def login():
	if not validLogin():
		return redirect('/')
	
	query = 'select * from user where email=:email'
	data = {
		'email': request.form['login_email']
	}
	
	user_data = mysql.query_db(query, data)
	
	if len(user_data) < 1:
		flash('Invalid username, try again or register!', 'login_error')
		return redirect('/')
		
	print('user in database')
	
	# verify login credentials and login user
	if not bcrypt.check_password_hash(user_data[0]['password'], request.form['login_pw']):
		flash('Invalid login credentials, try again!', 'login_error')
		return redirect('/')
		
	if not 'logged_in_userid' in session:
		session['logged_in_userid'] = user_data[0]['id']
		
	return redirect('/user_wall')

@app.route('/register', methods=['POST'])
def register():
	if not validRegistration():
		return redirect('/')
	
	# store user info in db and login user
	query = 'insert into user (first_name, last_name, email, password, created_at, updated_at) values (:first_name, :last_name, :email, :hashed_pw, NOW(), NOW())'
	data = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email'],
		'hashed_pw': bcrypt.generate_password_hash(request.form['pw'])
	}
	
	user_id = mysql.query_db(query, data)
	
	# successful registration
	if not 'logged_in_userid' in session:
		session['logged_in_userid'] = user_id
	
	# redirect then display logged in user's name on index.html
	return redirect('/user_wall')

@app.route('/user_wall')
def user_wall():
	# retrieve user name for session['logged_in_userid'] and other necessary info for user
	query = 'select first_name, last_name from user where id=:id'
	data = {
		'id': session['logged_in_userid']
	}
	
	user_data = mysql.query_db(query, data)
	
	if len(user_data) < 1:
		flash('Internal Error...contact support!', 'login_error')
		return redirect('/')
		# something critical went wrong, non-registered user still got in!!!
		
	# query for all messages, handle if no messages in db
	query = ("select message.id as message_id, user.first_name as fname, user.last_name as lname, date_format(message.created_at, '%M %D, %Y') as date, message.message as content "
			 "from user "
			 "join message on user.id = message.user_id;")
	
	messages = mysql.query_db(query)
	
	if len(messages) == 0:
		messages.append('No posts to display...so post something!')
	
	# TODO: query for all comments
	query = ("select user.first_name fname, user.last_name lname, message.id as message_id, date_format(comment.created_at, '%M %D, %Y') as date, comment.comment as content "
			 "from message "
			 "join comment on comment.message_id = message.id "
			 "join user on comment.user_id = user.id;")
	
	comments = mysql.query_db(query)
	
	if len(comments) == 0:
		comments = None
	print(comments)
	
	return render_template('user_wall.html', user=user_data[0], messages=messages, comments=comments)
	
@app.route('/user_wall/message_post', methods=['POST'])
def post_message():
	if not validMessagePost():
		return redirect('user_wall')
	
	# input post message into message table in db
	query = 'insert into message (user_id, message, created_at, updated_at) values (:user_id, :message_text, NOW(), NOW())'
	data = {
		'user_id': session['logged_in_userid'],
		'message_text': request.form['message_text']
	}
	
	try:
		mysql.query_db(query, data)
	except Exception as error:
		print('post_message: {}'.format(error))
		flash('Error trying to post message...try again!', 'error')
		return redirect('/user_wall')
	
	return redirect('/user_wall')

@app.route('/user_wall/comment/<message_id>', methods=['POST'])
def comment(message_id):
	print('comment: mid = {}'.format(message_id));
	
	#TODO: validate comment input data
	if not validComment():
		return redirect('user_wall')
	
	#insert into db
	query = ("insert into comment (message_id, user_id, comment, created_at, updated_at) "
			 "values (:message_id, :user_id, :comment, NOW(), NOW());")
	
	data = {
		'message_id': message_id,
		'user_id': session['logged_in_userid'],
		'comment': request.form['comment_text']
	}
	
	try:
		mysql.query_db(query, data)
	except Exception as error:
		print('comment: {}'.format(error))
		flash('Error trying to post comment...try again!', 'error')
		return redirect('/user_wall')
		
	return redirect('/user_wall')
	
@app.route('/logout')
def logout():
	session.clear()
	
	return redirect('/')

app.run(debug=True)