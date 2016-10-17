from system.core.controller import *
from time import strftime
class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)


    def index(self):
        time = strftime('%b %d %Y %H:%M %p')
        return self.load_view('index.html', time=time)
