from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

    def index(self):
        return self.load_view('index.html')
    def create_user(self):
        print "Got Post Info"
        session['name'] = request.form['name']
        session['comment'] = request.form['comment']
        session['favorite_language'] = request.form['favorite_language']
        session['dojo_select'] = request.form['dojo_select']
        return redirect('/show_user')
    def show_user(self):
        return self.load_view('user.html')
