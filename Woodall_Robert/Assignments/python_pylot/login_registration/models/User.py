from system.core.model import Model
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def add_user(self, user_data):
		response = {
			'user_id': 0,
			'errors': []	
		}
		
		# validate user_data
		if (len(user_data['first_name']) < 1 or
		    len(user_data['last_name']) < 1 or
		    len(user_data['email']) < 1 or
		    len(user_data['password']) < 1 or
		    len(user_data['confirm_password']) < 1):
			response['errors'].append('All inputs are required to register!')
			return response
		elif (len(user_data['first_name']) < 2 or 
			  len(user_data['last_name']) < 2):
			response['errors'].append('First and last name require at least 2 characters!')
			return response
		elif not EMAIL_REGEX.match(user_data['email']):
			response['errors'].append('Invalid email address format!')
			return response
		elif (len(user_data['password']) < 8 or
			  len(user_data['confirm_password']) < 8):
			response['errors'].append('Password must be at least 8 characters!')
			return response
		elif not user_data['password'] == user_data['confirm_password']:
			response['errors'].append('Passwords do not match!')
			return response
		
		# insert into db
		query = ('insert into user (first_name, last_name, email, password, created_at, updated_at) '
				 'values (:fname, :lname, :email, :hashed_pw, NOW(), NOW())')
		
		data = {
			'fname': user_data['first_name'],
			'lname': user_data['last_name'],
			'email': user_data['email'],
			'hashed_pw': self.bcrypt.generate_password_hash(user_data['password'])
		}
		
		try:
			response['user_id'] = self.db.query_db(query, data)
		except Exception as error:
			print('add_user(): {}'.format(error))
			response['errors'].append('Error registering user, please try again!')
			return response
		
		#success
		return response
	
	def get_user_by_id(self, user_id):
		response = {
			'user': None,
			'errors': []
		}
		
		query = 'select * from user where id = :id'
		
		try:
			response['user'] = self.db.query_db(query, {'id': user_id})
		except Exception as error:
			print('get_user_by_id(): {}'.format(error))
			response['errors'].append('Error registering user, please try again!')
			return response
		
		if len(response['user']) < 1:
			response['errors'].append('Error during registration, please try logging in!')
			return response
		
		# success
		return response
	
	def get_user_by_email(self, login_data):
		response = {
			'user': None,
			'errors': []
		}
		
		query = 'select * from user where email = :email'

		try:
			response['user'] = self.db.query_db(query, {'email': login_data['email']})
		except Exception as error:
			print('get_user_by_email(): {}'.format(error))
			response['errors'].append('Error logging user, please try again!')
			return response
		
		# user not registered
		if len(response['user']) < 1:
			response['errors'].append('Error logging in with provided email/password...try again!')
			return response
		
		# verify password
		if not self.bcrypt.check_password_hash(response['user'][0]['password'], login_data['password']):
			response['errors'].append('Error logging in with provided email/password...try again!')
			return response
		
		# success
		return response