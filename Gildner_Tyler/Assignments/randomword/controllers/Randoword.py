from system.core.controller import *
import string
import random
class Randoword(Controller):
    def __init__(self, action):
        super(Randoword, self).__init__(action)

    def index(self):
        if not 'attempt' in session:
            session['attempt'] = 0
        else:
            session['attempt'] += 1

        if not 'random' in session:
            session['random'] = " BEGIN  "

            for i in range(0,14):
                session['random'] += random.choice(string.ascii_uppercase + string.digits)

        return self.load_view('index.html', attempt=session['attempt'], random=session['random'])

    def process(self):
        session['random'] = ''
        for i in range(0,14):
            session['random'] += random.choice(string.ascii_uppercase + string.digits)

        return redirect('/')

    def clear(self):
        session.clear()

        return redirect('/')
