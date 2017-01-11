from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        # self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def register(self):
        return self.load_view('register.html')

    def submit_reg(self):
        # reg = request.form.copy()
        user = self.models['User'].create_user(request.form.copy())
        if not user['status'] == True:
            for message in user['errors']:
                flash(message, 'regis_errors')
            return redirect('/registration')
        # if create_status['status'] == True:
        #     return redirect('/')
        # else:
        #     for message in create_status['errors']:
        #         flash(message, 'regis_errors')
        #     return redirect('/registration')
        session['user'] = user['user']
        return redirect('/home')

    def home(self):
        if not 'user' in session:
            return redirect('/')
        return self.load_view('home.html')

    def login(self):
        user = self.models['User'].login(request.form.copy())
        if not user['status'] == True:
            for message in user['errors']:
                flash(message, 'regis_errors')
            return redirect('/')
        session['user'] = user['user']
        return redirect('/home')

    def logout(self):
        session.clear()
        return redirect('/')

    # def verification(self):
    #     if not 'user' in session:
    #         return False
    #     else:
    #         return True
