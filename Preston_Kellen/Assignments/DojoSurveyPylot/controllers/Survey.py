from system.core.controller import *

class Survey(Controller):
    def __init__(self, action):
        super(Survey, self).__init__(action)

    def index(self):
        return self.load_view('index.html')

    def submit(self):
        if not request.form['name'].isalpha():
            flash('please enter a name')
            return redirect('/')
        if not 'dictionary' in session:
            session['dictionary'] = {}

        if not 'counter' in session:
            session['counter'] = 0

        session['counter'] += 1

        session['dictionary'] = {
            'name' : request.form['name'],
            'location' : request.form['location'],
            'language' : request.form['language'],
            'comment' : request.form['comment']
        }

        return redirect('/display')

    def display(self):
        return self.load_view('display.html')
