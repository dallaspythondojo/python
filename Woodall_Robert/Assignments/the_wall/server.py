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
	
	try:
		user_data = mysql.query_db(query, data)
	except Exception as error:
		print('validLogin(): {}'.format(error))
	
	if len(user_data) < 1:
		flash('Uh oh, not a good email/password combo...try again or register!', 'login_error')
		return redirect('/')
	
	# verify login credentials and 'log user in'
	if not bcrypt.check_password_hash(user_data[0]['password'], request.form['login_pw']):
		flash('Invalid login credentials, try again!', 'login_error')
		return redirect('/')
	
	# store all data for that user
	session['logged_in_user_data'] = user_data[0]
		
	return redirect('/user_wall')

@app.route('/register', methods=['POST'])
def register():
	if not validRegistration():
		return redirect('/')
	
	query = 'insert into user (first_name, last_name, email, password, created_at, updated_at) values (:first_name, :last_name, :email, :hashed_pw, NOW(), NOW())'
	data = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email'],
		'hashed_pw': bcrypt.generate_password_hash(request.form['pw'])
	}
	
	try:
		user_id = mysql.query_db(query, data)
	except Exception as error:
		print('register(): {}'.format(error))
		flash('An error occured during registration...try again!', 'registration_error')
		return redirect('/')
	
	# registered successfully, retrieve all data for user and 'log user in'
	query = 'select * from user where id=:id'
	
	try:
		user_data = mysql.query_db(query, {'id': user_id})
	except Exception as error:
		print('register(): {}'.format(error))
		flash('Registration successful, but an error occured during login...login again!', 'registration_error')
		return redirect('/')
	
	session['logged_in_user_data'] = user_data[0]
	
	return redirect('/user_wall')

@app.route('/user_wall')
def user_wall():
	# verify user is logged in
	if not 'logged_in_user_data' in session:
		flash('Your previous session has ended...login!')
		return redirect('/')
	
	# query for all messages and handle if no messages in db
	query = ("select message.id as message_id, user.first_name as fname, user.last_name as lname, date_format(message.created_at, '%M %D, %Y - %h:%i %p') as date, message.message as content "
			 "from user "
			 "join message on user.id = message.user_id "
			 "order by date desc;")
	
	try:
		messages = mysql.query_db(query)
	except Exception as error:
		print('user_wall(): {}'.format(error))
		flash('Error retrieving posts...sorry!', 'error')
	
	if len(messages) == 0:
		messages.append('No posts to display...so post something!')
	
	# query for all comments and handle if no comments in db for a message
	query = ("select user.first_name fname, user.last_name lname, message.id as message_id, date_format(comment.created_at, '%M %D, %Y - %h:%i %p') as date, comment.comment as content "
			 "from message "
			 "join comment on comment.message_id = message.id "
			 "join user on comment.user_id = user.id;")
	
	try:
		comments = mysql.query_db(query)
	except Exception as error:
		print('user_wall(): {}'.format(error))
		flash('Error retrieving comments...sorry!', 'error')
		
#	if len(comments) == 0:
#		comments = None
	
	return render_template('user_wall.html', user=session['logged_in_user_data'], messages=messages, comments=comments)
	
@app.route('/user_wall/message_post', methods=['POST'])
def post_message():
	if not validMessagePost():
		return redirect('user_wall')
	
	query = 'insert into message (user_id, message, created_at, updated_at) values (:user_id, :message_text, NOW(), NOW())'
	data = {
		'user_id': session['logged_in_user_data']['id'],
		'message_text': request.form['message_text']
	}
	
	try:
		mysql.query_db(query, data)
	except Exception as error:
		print('post_message(): {}'.format(error))
		flash('Error posting message...try again!', 'error')
		return redirect('/user_wall')
	
	return redirect('/user_wall')

@app.route('/user_wall/comment/<message_id>', methods=['POST'])
def comment(message_id):
	if not validComment():
		return redirect('user_wall')
	
	query = ("insert into comment (message_id, user_id, comment, created_at, updated_at) "
			 "values (:message_id, :user_id, :comment, NOW(), NOW());")
	data = {
		'message_id': message_id,
		'user_id': session['logged_in_user_data']['id'],
		'comment': request.form['comment_text']
	}
	
	try:
		mysql.query_db(query, data)
	except Exception as error:
		print('comment(): {}'.format(error))
		flash('Error posting comment...try again!', 'error')
		return redirect('/user_wall')
		
	return redirect('/user_wall')
	
@app.route('/logout')
def logout():
	session.clear()
	
	return redirect('/')

app.run(debug=True)