from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        if 'user' in session:
            return redirect('/success')
        elif 'first_name' not in session:
            session['first_name']=""
            session['last_name']=""
            session['email']= ""
            session['con_pw']=""
            session['email1']=""
        return self.load_view('index.html')

    def success(self):
        if 'user' not in session:
            return redirect('/')
        print session['user']
        return self.load_view('success.html')

    def login_reg(self):
        if request.form['action']=='login':
            session['email1'] = request.form['email1']
            session['login_v_reg'] = "login"

            login_info = {  'email': request.form['email1'],
                            'pw': request.form['password1']
                         }

            print 'inside login'
            status = self.models['User'].login(login_info)
            if status['check'] == False:
                for message in status['errors']:
                    flash(message, "error")
                return redirect('/')
            else:
                session.clear()
                session['user']= status['user']
                flash("Successfully logged in!", "confirmation")
                return redirect('/success')

        if request.form['action']=='reg':
            session['first_name'] = request.form['first_name']
            session['last_name'] = request.form['last_name']
            session['email'] = request.form['email']
            session['login_v_reg'] = "reg"

            reg_info={  'first_name' : request.form['first_name'],
                        'last_name' : request.form['last_name'],
                        'email' : request.form['email'],
                        'pw' : request.form['password'],
                        'con_pw' : request.form['con_password']
                     }

            status = self.models['User'].register(reg_info)
            if status['check'] == False:
                for message in status['errors']:
                    flash(message, "error")
                return redirect('/')
            else:
                session.clear()
                session['user']= status['user']
                flash("Successfully registered!", "confirmation")
                return redirect('/success')

    def logout(self):
        session.clear()
        return redirect('/')
