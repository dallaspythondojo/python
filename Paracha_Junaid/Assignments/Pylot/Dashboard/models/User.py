""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model
import re

class User(Model):
	def __init__(self):
		super(User, self).__init__()
	
	def create_user(self, info):
		# We write our validations in model functions.
		# They will look similar to those we wrote in Flask
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		PW_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z])\w{8,}$')
		errors = []
		# Some basic validation
		if not info['first_name']:
			errors.append('First Name cannot be blank')
		elif len(info['first_name']) < 2:
			errors.append('First Name must be at least 2 characters long')
		if not info['last_name']:
			errors.append('Last Name cannot be blank')
		elif len(info['last_name']) < 2:
			errors.append('Last Name must be at least 2 characters long')
		if not info['email']:
			errors.append('Email cannot be blank')
		elif not EMAIL_REGEX.match(info['email']):
			errors.append('Email format must be valid!')
		if not info['password']:
			errors.append('Password cannot be blank')
		elif len(info['password']) < 8:
			errors.append('Password must be at least 8 characters long')
		elif info['password'] != info['confirm_pw']:
			errors.append('Password and confirmation must match!')
		# If we hit errors, return them, else return True.
		if errors:
			return {"status": False, "errors": errors}
		else:
			password = info['password']
			# bcrypt is now an attribute of our model
			# we will call the bcrypt functions similarly to how we did before
			# here we use generate_password_hash() to generate an encrypted password
			hashed_pw = self.bcrypt.generate_password_hash(password)
			create_query = "INSERT INTO user (first_name, last_name, password, email) VALUES (:first_name, :last_name, :pw_hash, :email)"
			create_data = {'first_name': info['first_name'], 'last_name': info['last_name'], 'pw_hash': hashed_pw, 'email':info['email']}
			self.db.query_db(create_query, create_data)
			# Then retrieve the last inserted user.
			get_user_query = "SELECT * FROM user ORDER BY id DESC LIMIT 1"
			users = self.db.query_db(get_user_query)
			return { "status": True, "user": users[0] }

	def login_user(self, info):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		PW_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z])\w{8,}$')
		errors = []
		if not info['email']:
			errors.append('Email cannot be blank')
		elif not EMAIL_REGEX.match(info['email']):
			errors.append('Email format must be valid!')
		if not info['password']:
			errors.append('Password cannot be blank')
		elif len(info['password']) < 8:
			errors.append('Password Invlaid')
		if errors:
			return {"status": False, "errors": errors}
		else:
			password = info['password']
			user_query = "SELECT * FROM user WHERE email = :email LIMIT 1"
			user_data = {'email': info['email']}
	 # same as query_db() but returns one result
			users = self.db.get_one(user_query, user_data)
			
			print users
			if users:
			   # check_password_hash() compares encrypted password in DB to one provided by user logging in
				if self.bcrypt.check_password_hash(users.password, password):
					return { "status": True, "user": users}
			# Whether we did not find the email, or if the password did not match, either way return False
			return {"status": False, "errors": errors}
	"""
	Below is an example of a model method that queries the database for all users in a fictitious application
	
	Every model has access to the "self.db.query_db" method which allows you to interact with the database

	def get_users(self):
		query = "SELECT * from users"
		return self.db.query_db(query)

	def get_user(self):
		query = "SELECT * from users where id = :id"
		data = {'id': 1}
		return self.db.get_one(query, data)

	def add_message(self):
		sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
		data = {'message': 'awesome bro', 'users_id': 1}
		self.db.query_db(sql, data)
		return True
	
	def grab_messages(self):
		query = "SELECT * from messages where users_id = :user_id"
		data = {'user_id':1}
		return self.db.query_db(query, data)

	"""