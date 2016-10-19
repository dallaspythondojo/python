from system.core.controller import *

def verify_login():
    if not 'id' in session:
        return False
    else:
        return True

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def index(self):
        return self.load_view('index.html')

    def users(self):
        if not verify_login():
            return redirect('/')
        return self.load_view('success.html')

    def create(self):
        user_info = {
        "f_name" : request.form['f_name'], "l_name" : request.form['l_name'], "email" : request.form['email'], "password" : request.form['password'], "pw_confirmation" : request.form['pw_confirmation']
        }

        create_status = self.models['User'].create_user(user_info)

        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
            session['f_name'] = create_status['user']['f_name']
            session['login_type'] = 'registered'

            return redirect('/users')

        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')

            return redirect('/')

    def login(self):
        login_info = {
        "email" : request.form['email'], "password" : request.form['password']
        }

        login_status = self.models['User'].login_user(login_info)

        if login_status['status'] == True:
            session['f_name'] = login_status['user']['f_name']
            session['login_type'] = 'logged in'

            return redirect('/users')

        else:
            for message in login_status['errors']:
                flash(message, 'login_errors')

            return redirect('/')

    def clear(self):
        session.clear()
        return redirect ('/')
