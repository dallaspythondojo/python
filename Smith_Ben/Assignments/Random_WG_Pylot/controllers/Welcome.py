
from system.core.controller import *
import random, string


class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

    def index(self):
        if not 'num' in session:
            session['num'] = 1
        session['rando'] = ''
        for x in range(0,14):
            session['rando'] += random.choice(string.ascii_uppercase + string.digits)
        return self.load_view('index.html')

    
    def process(self):
        
        session['rando'] = ''
        for x in range(0,14):
            session['rando'] += random.choice(string.ascii_uppercase + string.digits)
        session['num'] += 1
        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')

        

    

