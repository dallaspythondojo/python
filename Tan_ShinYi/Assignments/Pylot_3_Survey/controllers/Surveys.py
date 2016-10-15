from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
    def index(self):
        if 'name' not in session:
            session['name'] = ''
            session['comment'] = ''
        if 'counter' not in session:
            session['counter'] = 0
        print 'name: ' + session['name']
        print 'counter: ' + str(session['counter'])
        return self.load_view('index.html')

    def process(self):
        verify=True
        session['name']= request.form['name']
        session['comment']= request.form['comment']
        session['location']=request.form['location']
        session['language']=request.form['language']

        if len(session['name']) < 1:
            flash('Name field cannot be empty!')
            verify=False
        elif not session['name'].isalpha():
            flash('Name can only contain letters!')
            verify=False

        if session['location']=='':
            flash('Please pick a location!')
            verify=False
        if session['language']=='':
            flash('Please pick a language!')
            verify=False

        if verify:
            session['counter'] +=1
            flash('Thanks for submitting this form! You have submitted this form ' + str(session['counter']) + ' time(s) now.')
            return redirect('/result')
        return redirect('/')

    def result(self):
        return self.load_view('result.html')

    def reset(self):
        temp=session['counter']
        session.clear()
        session['counter']=temp
        return redirect('/')
