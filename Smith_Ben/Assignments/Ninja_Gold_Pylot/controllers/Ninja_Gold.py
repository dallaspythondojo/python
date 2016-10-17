
from system.core.controller import *
import random, datetime
class Ninja_Gold(Controller):
    def __init__(self, action):
        super(Ninja_Gold, self).__init__(action)


    def index(self):
        if not 'gold' in session:
            session['gold'] = 0
        if not 'activities' in session:
            session['activities'] = []
        return self.load_view('index.html', )


    def process(self):
        locations = {
        'farm':random.randint(10,20),
        'casino':random.randint(-50,50),
        'cave':random.randint(5,10),
        'house':random.randint(2,5)
        }
        if request.form['location'] in locations:
            result = locations[request.form['location']]
            session['gold'] = session['gold']+result
            result_dictionary = {
                                    'class': ('red','green')[result > 0],
                                    'activity': "You went to the {} and {} {} gold! You now have {} gold.".format(request.form['location'], ('lost','gained')[result > 0], result, session['gold'])
                                }
            session['activities'].append(result_dictionary)
        return redirect('/')
            


    if __name__ == '__main__':
        app.run(debug = True)










