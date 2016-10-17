
from system.core.controller import *
import random
import datetime

class Gold(Controller):
	def __init__(self, action):
		super(Gold, self).__init__(action)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
		"""
		self.load_model('WelcomeModel')
		self.db = self._app.db
		if not 'user_gold' in session:
			session['user_gold'] = 0
		if not 'done' in session:
			session['done'] = []
		if not 'plays' in session:
			session['plays'] = 0
		if not 'history' in session:
			session['history'] = []

   
	def index(self):
		history_length = len(session['history'])
		return self.load_view('index.html', history_length = history_length)

	def process(self):
		if 'clear' in request.form:
			session['user_gold'] = 0
			session['plays'] = 0
			session['history'] = []
			return redirect('/')

		session['plays'] += 1
		buildings = {
			'farm': random.randint(10,20),
			'cave': random.randint(5,10),
			'house': random.randint(2,5),
			'casino': random.randint(-50,50)
		}
		if 'building' in request.form:
			result = buildings[request.form['building']]
			session['user_gold'] += result
		if result > 0:
			play_result = "You visited the {} and gained {} gold! {}.".format(request.form['building'], result, datetime.datetime.now())
		else: 
			play_result = "You visited the casino and lost {} gold :( {}.".format(result, datetime.datetime.now())
		session['history'].insert(0, play_result)
		return redirect('/')