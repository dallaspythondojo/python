from system.core.controller import *
import random, string

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        if not 'count' in session:
            session['count'] = 0
        return self.load_view('index.html')

    def generate(self):
        if not 'count' in session:
            return redirect('/')
        session['count'] += 1
        session['rng'] = ''
        for value in range(14):
            session['rng'] += random.choice(string.ascii_uppercase + string.digits)
# ASK AUTHMAN about passing var in redirect
        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')
