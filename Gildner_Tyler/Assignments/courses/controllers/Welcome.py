from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        courses = self.models['WelcomeModel'].index()
        return self.load_view('index.html', courses = courses)

    def courses(self):
        course = {
            'name': request.form['name'],
            'description': request.form['description']
        }

        self.models['WelcomeModel'].courses(course)
        return redirect('/')

    def delete(self, id):
        courses = self.models['WelcomeModel'].delete(id)
        return self.load_view('delete.html', courses = courses)

    def deletedelete(self, id):
        self.models['WelcomeModel'].deletedelete(id)
        return redirect('/')
