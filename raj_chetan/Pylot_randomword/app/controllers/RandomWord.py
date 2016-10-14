"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *
import random, string

class RandomWord(Controller):
	def __init__(self, action):
		super(RandomWord, self).__init__(action)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
		"""
		self.load_model('WelcomeModel')
		self.db = self._app.db
		if 'counter' not in session:
			session['counter'] = 0
		"""
		
		This is an example of a controller method that will load a view for the client 

		"""
   
	def index(self):
		"""
		A loaded model is accessible through the models attribute 
		self.models['WelcomeModel'].get_users()
		
		self.models['WelcomeModel'].add_message()
		# messages = self.models['WelcomeModel'].grab_messages()
		# user = self.models['WelcomeModel'].get_user()
		# to pass information on to a view it's the same as it was with Flask
		
		# return self.load_view('index.html', messages=messages, user=user)
		"""
		random_value = string.uppercase+string.digits
		random_length = ''.join(random.sample(random_value,session['counter']))
		if len(random_length) == 0:
			random_length = "First attempt not yet complete, string does not yet exist."
		return self.load_view('index.html', attempt_number = session['counter'], random_length = random_length)

	def process(self):
		if 'button' in request.form:
			print 'button has been clicked.'
			session['counter'] += 1
		if 'clear_button' in request.form:
			print 'the session counter has been cleared...'
			session['counter'] = 0
		return redirect('/')


