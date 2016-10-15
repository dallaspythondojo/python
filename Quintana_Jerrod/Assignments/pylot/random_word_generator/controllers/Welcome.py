
from system.core.controller import *
import random
import string
string.letters


def generate_random():
    session['random'] = ''
    for i in range(14):
        lett = random.choice(string.letters)
        session['random'] += lett

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db
        if 'random' not in session:
            session['count'] = 0
        if not 'random':
            session['random'] = ''

    def index(self):
        generate_random()
        return self.load_view('index.html', count = session['count'], random = session['random'])
    def process(self):
        session['count'] += 1
        return redirect('/')
