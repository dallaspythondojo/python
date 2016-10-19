
from system.core.model import Model
import re
from flask import session
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def registering(self, user):
		errors = []
		if not user['first']:
			errors.append('First Name cannot be blank')
		elif len(user['first']) < 2:
			errors.append('First Name is too short')
		elif not user ['first'].isalpha():
			errors.append('Letters Only Please')
		if not user['last']:
			errors.append('Last Name cannot be blank')
		elif len(user['last']) < 2:
			errors.append('Last Name is too short')
		elif not user ['last'].isalpha():
			errors.append('Letters Only Please')
		if not user['email']:
			errors.append('Email cannot be Blank')
		elif not EMAIL_REGEX.match(user['email']):
			errors.append('Invalid Email or Password')
		if not user['password']:
			errors.append('Password cannot be blank')
		elif len(user['password']) < 8:
			errors.append('Minimum of 8 Characters Please')
		elif user['password'] != user['confirm']:
			errors.append('Password did not Match')

		if errors:
		    return {"status":False, "errors":errors}
	
		hashed_pw = self.bcrypt.generate_password_hash(user['password'])
		query = "INSERT INTO user (first, last, email, pw_hash, created_at, updated_at) VALUES (:first, :last, :email, :pw_hash, NOW(), NOW())"
		data = {
			'first':user['first'],
			'last':user['last'],
			'email':user['email'],
			'pw_hash':hashed_pw
		}
		self.db.query_db(query, data)
		query = "SELECT * FROM user ORDER BY id DESC LIMIT 1"
		users = self.db.query_db(query)
		return { "status":True, "user":users[0] }

	

		return self.db.query_db(query, data)

	def logining(self, user):
		errors = []
		if not EMAIL_REGEX.match(user['email']):
			errors.append('Invalid Email or Password')
		password = user['password']
		query = "SELECT * FROM user WHERE email = :email LIMIT 1"
		user = self.db.query_db(query, user)
		if user:
			if self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
				return { "status": True, "user":user[0] }
			else:
				errors.append('Invalid Email or Password')
		else:
			errors.append('Invalid Email or Password')
		if errors:
			return { "status":False, 'errors':errors }
		return False

	def dashboarding(self, id):
		query = "SELECT * FROM user WHERE id = :id"
		data = { 'id':id }
		user = self.db.query_db(query, data)

	def logout(self):
		session.clear
		return self

