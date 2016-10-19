from system.core.controller import *
import random
from time import localtime, strftime

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
    def index(self):
        if 'gold' not in session:
            session['gold']=0
            session['activities']=[]
        return self.load_view('index.html')
    def process(self):
        location = {
            'farm':random.randint(10,20),
            'cave':random.randint(5,10),
            'house':random.randint(2,5),
            'casino':random.randint(-50,50),
        }
        if request.form['location'] in location:
            result = location[request.form['location']]
            session['gold'] = session['gold']+result
            result_dictionary = {
                                    'activity': ("Entered a casino and lost {} gold(s)... Ouch..".format(result),
                                    "Earned {} gold(s) from the {}!".format(result, request.form['location']))[result>0],
                                    'time': strftime("%Y/%m/%d %I:%M %p", localtime())
                                }
            session['activities'].insert(0,str(result_dictionary['activity'])+ " ( " + str(result_dictionary['time']) + " ) ")
        return redirect('/')
    def reset(self):         #for the purposes of debugging
        session.clear()
        return redirect('/')
