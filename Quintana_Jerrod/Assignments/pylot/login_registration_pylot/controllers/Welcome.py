from system.core.controller import *

def check_logged_in():
    if not 'user' in session:
        return False

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def create(self):
        info = {
            'first': request.form['first'],
            'last': request.form['last'],
            'email': request.form['email'],
            'password': request.form['pwd'],
            'confirm': request.form['confirm']
        }
        create = self.models['WelcomeModel'].register(info)
        if create['status'] == False:
            for message in create['errors']:
                flash(message, 'regis_errors')
            return redirect('/')
        else:
            session['answer'] = 'Registered'
            session['user'] = create['user']
            return redirect('/success')

    def success(self):
        if check_logged_in() == False:
            flash ('Must be logged in first')
            return redirect('/')
        return self.load_view('success.html', name = session['user']['first_name'], answer = session['answer'])

    def logout(self):
        session.clear()
        return redirect('/')

    def login(self):
        info = {
            'email': request.form['login_email'],
            'password': request.form['login_pwd']
        }
        log = self.models['WelcomeModel'].check_login(info)
        if log['status'] == False:
            flash(log['error'], 'regis_errors')
            return redirect('/')
        else:
            session['answer'] = 'Logged in'
            session['user'] = log['user']
            return redirect('/success')
