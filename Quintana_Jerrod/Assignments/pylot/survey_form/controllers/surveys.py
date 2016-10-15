from system.core.controller import *

class surveys(Controller):
    def __init__(self, action):
        super(surveys, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db
        if not 'new' in session:
            session['new'] = 1

    def index(self):
        return self.load_view('index.html')
    def process(self):
        session['new'] += 1
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment']  = request.form['comment']
        return redirect('/result')
    def result(self):
        return self.load_view('result.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comment'], count = session['new'])
