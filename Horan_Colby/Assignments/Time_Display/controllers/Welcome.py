
from system.core.controller import *
from time import strftime, localtime

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        time = strftime("%b %d, %Y %I:%M %p", localtime())
        return self.load_view('index.html', time = time)

