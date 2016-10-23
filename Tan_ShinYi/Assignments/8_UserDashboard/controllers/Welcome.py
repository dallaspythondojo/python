from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        # self.load_model('WelcomeModel')
    def index(self):
        return self.load_view('index.html')
    def signin(self):
        return self.load_view('signin.html')
    def register(self):
        return self.load_view('register.html')
    def logoff(self):
        session.clear()
        return redirect('/')
