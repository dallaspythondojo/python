from system.core.controller import *
import random, string

class RandomWordGenerator(Controller):
	def __init__(self, action):
		super(RandomWordGenerator, self).__init__(action)
	
	def index(self):
		if not 'attempt_count' in session:
			session['attempt_count'] = 0
			self.generate()
		
		return self.load_view('index.html', attempt_count=session['attempt_count'], random_string=session['random_string'])
	
	def generate(self):
		if not 'attempt_count' in session:
			return redirect('/')
		
		session['attempt_count'] += 1
		session['random_string'] = ''
		
		for value in range(14):
			session['random_string'] += random.choice(string.ascii_uppercase + string.digits)
		
		return redirect('/')
	
	def reset(self):
		session.clear()
		return redirect('/')
	