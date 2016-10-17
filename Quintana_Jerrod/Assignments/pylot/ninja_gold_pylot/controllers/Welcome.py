from system.core.controller import *
from datetime import datetime
import random

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        if not ('gold') in session:
            session['gold'] = 0;
        if not ('activities') in session:
            session['activities'] = {}
        return self.load_view('index.html',gold = session['gold'], activities = session['activities'])

    def money(self):
        now = datetime.now()
        buildings = {
            'farm': random.randrange(10,21),
            'cave': random.randrange(5,11),
            'house': random.randrange(2,6),
            'casino': random.randrange(0,51)
        }
        session['green'] = 'green'
        session['red']='red'
        if request.form['building'] == 'casino':
            result = buildings[request.form['building']]
            rand = random.randrange(0,2)
            if rand == 0:
                session['gold'] += result
                session['activities'].update({'Entered a casion and gained {} gold! ({})'.format(buildings[request.form['building']], now): session['green']})
            else:
                session['gold'] -= result
                session['activities'].update({'Entered a casion and lost {} gold...Ouch... ({})'.format(buildings[request.form['building']], now): session['red']})
        elif request.form['building'] in buildings:
            result = buildings[request.form['building']]
            session['gold'] += result
            session['activities'].update({'Earned {} gold from the farm! ({})'.format(buildings[request.form['building']], now): session['green']})
        return redirect('/')
