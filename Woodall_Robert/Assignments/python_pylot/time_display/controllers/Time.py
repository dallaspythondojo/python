from system.core.controller import *
from time import strftime

class Time(Controller):
	def __init__(self, action):
		super(Time, self).__init__(action)
	
	def index(self):
		#Oct 26, 2013 \n 11:26 AM
		the_time = strftime('%b %d %Y %I:%M %p')
		print('Current time is {}'.format(the_time))
		return self.load_view('index.html', current_time=the_time)
	