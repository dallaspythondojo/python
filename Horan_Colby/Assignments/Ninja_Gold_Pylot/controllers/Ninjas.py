
from system.core.controller import *
import random

class Ninjas(Controller):
	def __init__(self, action):
		super(Ninjas, self).__init__(action)
		self.load_model('WelcomeModel')
		self.db = self._app.db
		
	def index(self):
		if not 'gold' in session:
			session['gold'] = 0
		if not 'activities' in session:
			session['activities'] = []
		return self.load_view('index.html')

	def process_money(self):
		locations = {
			'farm' : random.randint(10, 20),
			'cave' : random.randint(5, 10),
			'house' : random.randint(2, 5),
			'casino' : random.randint(-50, 50)
		}
		if request.form['location'] in locations:
			result = locations[request.form['location']]
			session['gold'] += result
			result_dictionary = {
				'class' : ('red', 'green')[result > 0],
				'activity' : "You went to the {} and {} {} gold!".format(request.form['location'], ('lost', 'gained')[result>0], result)
			}
		session['activities'].append(result_dictionary)
		return self.load_view('index.html')

