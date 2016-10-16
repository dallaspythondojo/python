
from system.core.controller import *
import string
string.letters
import random


class Werdz(Controller):
	def __init__(self, action):
		super(Werdz, self).__init__(action)
		self.load_model('WelcomeModel')
		self.db = self._app.db
	
	def index(self):
		if not 'counter' in session:
			session['counter'] = 0
		session['counter'] += 1

		#I know this isn't right, but I don't know how to do it.  I tried a few different ways and looked over the internets and so I just went with this

		werd = random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters) + random.choice(string.letters)


		return self.load_view('index.html', werd = werd, attempt = session['counter'])

	def generate(self):
		return redirect('/')

