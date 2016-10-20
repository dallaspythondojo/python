""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model
import re

class Dashboard(Model):
	def __init__(self):
		super(Dashboard, self).__init__()
	
	def get_all_users(self):
		print 'hello'
		return self.db.query_db('SELECT first_name, last_name, id, date_format(created_at, "%M %D %Y") created_at, user_level, email FROM user')
	
	def delete_user(self, remove_id):
		query = "DELETE FROM user WHERE id = :remove_id"
		data = { "remove_id": remove_id }
		return self.db.query_db(query, data)

	def get_user_by_id(self, id):
		query = "SELECT * FROM user WHERE id = :id"
		data = { 'id': id}
		return self.db.query_db(query, data)

	def update_user(self, user):
	 
		query = "UPDATE user SET first_name=:first_name, last_name=:last_name, email=:email WHERE id = :id"
	
		data = { 'first_name': user['first_name'], 'last_name': user['last_name'], 'email': user['email'], 'id': user['id']}
	
		return self.db.query_db(query, data)
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