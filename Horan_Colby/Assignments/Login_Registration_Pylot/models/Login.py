from system.core.model import Model
import re

class Login(Model):
	def __init__(self):
		super(Login, self).__init__()

	def create_user(self, info):
		email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors = []

		if len(info['email']) < 1:
			errors.append('Please enter a valid email.')
		if not email_regex.match(info['email']):
			errors.append('Invalid Email Address!')
		if len(info['firstname']) < 2 or not info['firstname'].isalpha():
			errors.append('Please enter your first name.')
		if len(info['lastname']) < 2 or not info['lastname'].isalpha():
			errors.append('Please enter your last name.')
		if info['password'] <= 8:
			errors.append('Password must be at least 8 characters.')
		if not info['password'] == info['confirm']:
			errors.append('Password\'s do not match.')

		add_query = "INSERT INTO user (firstname, lastname, email, password, created_at) VALUES (:firstname, :lastname, :email, :password, NOW())"
		user = { 
			'firstname' : info['firstname'],
			'lastname' : info['lastname'],
			'email' : info['email'],
			'password' : self.bcrypt.generate_password_hash(info['password'])
		}

		get_user_query = 'SELECT * FROM user ORDER BY id DESC LIMIT 1'
		users = self.db.query_db(get_user_query)
		try:
			self.db.query_db(add_query, user)
		except:
			errors.append('Email address in use')
			
		if errors:
			return {'status' : False, 'errors': errors}
		return {'status' : True, 'user' : users[0]}

	def login_user(self, info):
		password = info['password']
		user_query = "SELECT * FROM user WHERE email = :email LIMIT 1"
		user_data = {'email': info['email']}
		errors = ['Invalid username/password']
		user = self.db.query_db(user_query, user_data)
		if user:
			if self.bcrypt.check_password_hash(user[0]['password'], password):
				return {'status' : True, 'user' : user[0]}
		return {'status' : False, 'errors': errors}








