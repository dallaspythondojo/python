from system.core.controller import *
import random
import string


class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

    def index(self):
        if not 'attempt' in session:
            session['attempt'] = 1
        else:
            session['attempt'] += 1

        if not 'random' in session:
            session['random'] = ''

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
