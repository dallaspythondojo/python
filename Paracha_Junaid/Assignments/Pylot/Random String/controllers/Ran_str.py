from system.core.controller import *
import random


class Ran_str(Controller):
	def __init__(self, action):
		super(Ran_str, self).__init__(action)

		self.load_model('WelcomeModel')
		self.db = self._app.db
		self.Attempt = 0
		

	def index(self):
		self.Attempt = 0
		my_string = ''
		
		for i in range (0,15):
			y = random.randint(0,9)
			x = random.randint(0,9)
			if x >= y:
				my_string=str(x) + my_string
			else:
				a = ('A','B','C','D','E','F','G','H')	
				my_string=random.choice(a) + my_string

			i += 1
		
		return self.load_view('index.html', my_string=my_string)

	def process(self):
		self.Attempt = int(request.form['Attempt'])
		self.Attempt += 1
		session['Att'] = self.Attempt
		print session['Att']
		# self.Attempt += 1
		# return self
		return redirect('/')