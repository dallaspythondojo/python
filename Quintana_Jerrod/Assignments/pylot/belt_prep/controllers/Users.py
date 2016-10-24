from system.core.controller import *

def Valid():
    if 'user' in session: return True

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

# routes['/'] = 'Users#index'
    def index(self):
        if Valid() == True: return redirect('/books')
        return self.load_view('index.html')

# routes['POST']['/registration'] = 'Users#registration'
    def registration(self):
        user = self.models['User'].register(request.form.copy())
        if user['errors']:
            for i in user['errors']:
                flash(i, 'register')
            return redirect('/')
        session['user'] = user['user']
        return redirect('/books')
# routes['POST']['/login'] = 'Users#login'
    def login(self):
        user = self.models['User'].login(request.form.copy())
        if user['errors']:
            flash(user['errors'], 'login')
            return redirect('/')
        session['user'] = user['user']
        return redirect('/books')

# routes['POST']['/logout'] = 'Users#logout'
    def logout(self):
        session.clear()
        return redirect('/')

# routes['/users/<id>'] = 'Users#show'
    def show(self, id):
        show = self.models['User'].show(id)
        rev = self.models['User'].user_review(id)
        return self.load_view('user_show.html', show = show[0], review = rev, count = len(rev))
