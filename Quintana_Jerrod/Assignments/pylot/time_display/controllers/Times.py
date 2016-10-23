from system.core.controller import *
from time import strftime, localtime

class Times(Controller):
    def __init__(self,action):
        super(Times, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        time = strftime('%h %d, %Y %I:%M %p', localtime())
        return self.load_view('index.html', time = time)
