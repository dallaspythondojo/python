
from system.core.controller import *
import random
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
        locations = {
            'farm':random.randint(10,20),
            'cave':random.randint(5,10),
            'house':random.randint(2,5),
            'casino':random.randint(-50,50)
        }
        if request.form['location'] in locations:
            result = locations[request.form['location']]
            session['gold'] = session['gold']+result
            result_dictionary = {
                                    'class': ('red','green')[result > 0],
                                    'activity': "You went to the {} and {} {} gold!".format(request.form['location'], ('lost','gained')[result > 0], result)
                                }
            session['activities'].append(result_dictionary)
        return redirect('/')
