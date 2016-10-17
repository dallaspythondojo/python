from system.core.controller import *
from time import strftime, localtime


class Time(Controller):
	def __init__(self, action):
		super(Time, self).__init__(action)

		self.load_model('WelcomeModel')
		self.db = self._app.db

	def index(self):
		# Time = datetime.datetime.now()
		Time = strftime('%b %d, %Y %I:%M %p', localtime())
		return self.load_view('index.html', Time=Time)

