
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
    def index(self):
        return self.load_view('index.html')

    def process(self):
        if request.form['home'] == 'register':
            user = {
                'first':request.form['first'],
                'last':request.form['last'],
                'email':request.form['email'],
                'password':request.form['password'],
                'confirm':request.form['confirm']
            }
            create_status = self.models['User'].registering(user)
            if create_status['status'] == True:
                session['first'] = create_status['user']['first']
                return self.load_view('success.html')
            else:
                for message in create_status['errors']:
                    flash(message, 'regis_errors')
                return redirect('/')
            self.models['User'].registering(user)
            return self.load_view('success.html')
        elif request.form['home'] == 'login':
            user = {
                'email':request.form['email'],
                'password':request.form['password']
            }
            create_status = self.models['User'].logining(user)
            if create_status['status'] == True:
                session['first'] = create_status['user']['first']
                return self.load_view('success.html')
            else:
                for message in create_status['errors']:
                    flash(message, 'regis_errors')
                return redirect('/')

    def logout(self):
        self.models['User'].logout()
        return redirect('/')
