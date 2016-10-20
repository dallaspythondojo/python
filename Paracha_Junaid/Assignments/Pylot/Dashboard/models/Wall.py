""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model
import re

class Wall(Model):
	def __init__(self):
		super(Wall, self).__init__()
	
	def user_messages(self,id):
		query = ('SELECT u.first_name, u.last_name, u.id as user_id, m.message, m.id mid, date_format(m.created_at, "%M %D %Y") created_at FROM message m Join user u on u.id= m.user_id where message_to = :id ORDER BY m.created_at DESC')
		data = {'id': id}
		return self.db.query_db(query, data)

	def message_comment(self):
		return self.db.query_db('SELECT c.message_id, u.first_name, u.last_name, u.id as user_id, c.comment, c.id cid, date_format(c.created_at, "%M %D %Y") created_at FROM comment c Join user u on u.id= c.user_id ORDER BY c.created_at DESC')


	def post_message(self, message):
		Str = "INSERT INTO message(message, user_id, message_to) VALUE (:message, :user_id, :message_to)"
		data = { 
				'message': message['message'],
				'user_id': message['user_id'],
				'message_to': message['message_to']

		}
		try:
			return self.db.query_db(Str,data)
		except Exception as error:
			print error
			return 

	def post_comment(self, comment):
   
		Str = "INSERT INTO comment(comment, message_id, user_id) VALUE (:comment, :message_id, :user_id)"
		data = { 
				'comment': comment['comment'],
				'message_id': comment['message_id'],
				'user_id': comment['user_id']
		}
		try:
			return self.db.query_db(Str,data)
		except Exception as error:
			print error
			return    
	
	def delete_comment(self, cid):
		Str = "DELETE FROM wall.comment WHERE id= :id"
		data = { 'id':cid }
		try:
			return self.db.query_db(Str,data)
		except Exception as error:
			print error
			return  







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