from system.core.controller import *
from time import strftime, localtime

class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)

	def index(self):
		date= strftime('%b %d, %Y', localtime())
		time= strftime('%I:%M %p')
		return self.load_view('time.html',date=date, time=time)