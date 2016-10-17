"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
import random, datetime
from system.core.controller import *

class Ninja_gold(Controller):
    def __init__(self, action):
        super(Ninja_gold, self).__init__(action)

        """
         
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        if not 'gold' in session:
            session['gold'] = 0
        if not 'activities' in session:
            session['activities'] =[]
        
        return self.load_view('index.html', goldcount = session['gold'])

    def process_money(self):
        buildings={
            'farm' : random.randint(5, 20),
            'cave' : random.randint(5, 10),
            'house': random.randint(2, 5),
            'casino': random.randint(-50, 50)
        }
        if request.form['place'] in buildings:
            result = buildings[request.form['place']]
            session['gold'] = session['gold'] + result
            myStr = "{} {} golds from the {} ({})".format(('lost','Earned')[result > 0], abs(result), request.form['place'], datetime.datetime.now()) 
            session['activities'].append(myStr)
        return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')

