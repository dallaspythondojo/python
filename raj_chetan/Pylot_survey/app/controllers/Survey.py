"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *

class Survey(Controller):
	def __init__(self, action):
		super(Survey, self).__init__(action)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
		"""
		self.load_model('WelcomeModel')
		self.db = self._app.db
		if not 'counter' in session:
			session['counter'] = 0
		"""
		
		This is an example of a controller method that will load a view for the client 

		"""
   
	def index(self):
		print 'reached index...'
		return self.load_view('index.html')

	def process(self):
		if 'hidden_form' in request.form:
			print 'server has received user input'
			session['name'] = request.form['name']
			session['location'] = request.form['location']
			session['favorite_language'] = request.form['favorite']
			session['counter'] += 1
			return redirect('/results')

		if 'clear' in request.form:
			session['counter'] = 0
			return redirect('/')
		return redirect('/')
	
	def results(self):
		return self.load_view('results.html')
