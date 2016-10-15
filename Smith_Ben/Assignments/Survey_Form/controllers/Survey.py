
from system.core.controller import *

class Survey(Controller):
    def __init__(self, action):
        super(Survey, self).__init__(action)
        
   
    def index(self):
        if not 'num' in session:
            session['num'] = 1
        return self.load_view('index.html')

    def process(self):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        session['num'] += 1
        return redirect('/survey/results')

    def results(self):

        return self.load_view('results.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])


