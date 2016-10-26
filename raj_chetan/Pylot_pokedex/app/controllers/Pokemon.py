"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *

class Pokemon(Controller):
	def __init__(self, action):
		super(Pokemon, self).__init__(action)

		self.load_model('WelcomeModel')
		self.db = self._app.db


	def index(self):
		test = "test string 123"
		return self.load_view('index.html', test = test)

	def whoDat(self, id):
		return self.load_view('index.html', id = id)