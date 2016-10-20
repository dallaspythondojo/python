from system.core.controller import *

class Walls(Controller):
	def __init__(self, action):
		super(Walls, self).__init__(action)

		self.load_model('Wall')
		self.load_model('Dashboard')
		self.db = self._app.db	
		
	def wall(self, id):
		print session
		if not 'id' in session:
			return redirect('/Users')
		user = self.models['Dashboard'].get_user_by_id(id)
		profile_user = user[0]
		
		user_messages = self.models['Wall'].user_messages(id)
		message_comment = self.models['Wall'].message_comment()
		return self.load_view('Wall/wall.html', profile_user=profile_user, user_messages=user_messages, message_comment=message_comment )
	
	def post_message(self, id):
		message_details = {
			'message': request.form['message'] ,
			'user_id': session['id'],
			'message_to': id
		}
		self.models['Wall'].post_message(message_details)
		user = self.models['Dashboard'].get_user_by_id(id)
		profile_user = user[0]
		
		user_messages = self.models['Wall'].user_messages(id)
		message_comment = self.models['Wall'].message_comment()
		return self.load_view('Wall/wall.html', profile_user=profile_user, user_messages=user_messages, message_comment=message_comment )
	
	def post_comment(self, mid, id):
		comment_details = {
			'comment': request.form['comment'],
            'message_id': mid,
            'user_id': session['id']
		}
		self.models['Wall'].post_comment(comment_details)
		user = self.models['Dashboard'].get_user_by_id(id)
		profile_user = user[0]
		
		user_messages = self.models['Wall'].user_messages(id)
		message_comment = self.models['Wall'].message_comment()
		return self.load_view('Wall/wall.html', profile_user=profile_user, user_messages=user_messages, message_comment=message_comment )
	
	def delete_comment(self, cid, id):
		self.models['Wall'].delete_comment(cid)
		user = self.models['Dashboard'].get_user_by_id(id)
		profile_user = user[0]
		
		user_messages = self.models['Wall'].user_messages(id)
		message_comment = self.models['Wall'].message_comment()
		return self.load_view('Wall/wall.html', profile_user=profile_user, user_messages=user_messages, message_comment=message_comment )
	