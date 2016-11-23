"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random, datetime

class Ninja(Controller):
    def __init__(self, action):
        self.gold =0
        super(Ninja, self).__init__(action)

        self.load_model('NinjaModel')
        self.db = self._app.db


    def index(self):

        if not 'score' in session:
            session['score']=0
            session['scores']=0
            session['format']=[]
            session['message']=[]

        return self.load_view('index.html')

    def process(self,id):

        if id == 'farm':
            self.gold = random.randint(10,20)
        elif id == 'cave':
            self.gold = random.randint(5,10)
        elif id == 'house':
            self.gold = random.randint(2,5)
        else: self.gold = random.randint(-50,50)

        session['score'] = self.gold
        session['scores'] += session['score']

        return redirect('/view')

    def view(self):


        if session['score'] > 0:
            session['format'] = 'win'
            session['message'].append("You earned {} gold on {}".format(session['score'], datetime.datetime.now()))
            
        else:
            session['message'].append("You lost {} gold on {}".format(abs(session['score']), datetime.datetime.now()))
            session['format'] = 'lose'

        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')
