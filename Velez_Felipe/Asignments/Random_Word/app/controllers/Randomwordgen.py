"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random
import string
class Randomwordgen(Controller):
    def __init__(self, action):
        super(Randomwordgen, self).__init__(action)
   
    def index(self):
        return self.load_view('index.html')

    def process(self):
        session['generator'] = ""

        if not 'Number' in session:
            session['Number'] = 0
        session['Number'] += 1
        print session['Number']

        for rand in range(14):
            session['generator']+= random.choice(string.ascii_uppercase + string.digits)
            print session['generator']
        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')
   

