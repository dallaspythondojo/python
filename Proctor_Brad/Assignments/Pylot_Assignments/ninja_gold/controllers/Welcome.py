import random
import datetime
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)


    def index(self):
        if not 'gold' in session:
            session['gold'] = 0
        if not 'activities' in session:
            session['activities'] = []
        return self.load_view('index.html')

    def process(self):
        brad = {'farm':random.randrange(10,20),'cave':random.randint(5,10),'house':random.randint(2,5),'casino':random.randint(-50,50)}

        if request.form['building'] in brad:

            result = brad[request.form['building']]

            if request.form['building'] == 'farm':
                session['gold'] += result
                session['activities'].append('Earned ' + str(brad['farm']) + ' golds from the farm! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

            elif request.form['building'] == 'cave':
                session['gold'] += result
                session['activities'].append('Earned ' + str(brad['cave']) + ' golds from the cave! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

            elif request.form['building'] == 'house':
                session['gold'] += result
                session['activities'].append('Earned ' + str(brad['house']) + ' golds from the house! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

            elif request.form['building'] == 'casino':
                session['gold'] += result
                if brad['casino'] >= 0:
                    session['activities'].append('Entered a casino and gained ' + str(brad['casino']) + ' golds... YaY!.. {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
                else:
                    session['activities'].append('Entered a casino and lost ' + str(abs(brad['casino'])) + ' golds... Ouch.. {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

        return redirect('/')
