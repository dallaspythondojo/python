
from system.core.controller import *

class Surveys(Controller):
	def __init__(self, action):
		super(Surveys, self).__init__(action)
		self.load_model('WelcomeModel')
		self.db = self._app.db
		
	def index(self):
		return self.load_view('index.html')

	def process(self):
		user = {
			'name' : request.form['name'],
			'location' : request.form['locations'],
			'language' : request.form['language'],
			'comment' : request.form['comment']
		}
		return self.load_view('/surveys/result', user = request.form['result'])

	def result(self):
		if not 'counter' in session:
			session['counter'] = 0
		session['counter'] += 1
		user = {
			'name' : request.form['name'],
			'location' : request.form['locations'],
			'language' : request.form['language'],
			'comment' : request.form['comment']
		}
		session['user'] = user
		return self.load_view('/result/result.html', attempt = session['counter'], user = session['user'])

