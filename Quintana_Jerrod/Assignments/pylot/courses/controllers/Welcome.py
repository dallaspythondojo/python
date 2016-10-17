from system.core.controller import *
class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        all = self.models['WelcomeModel'].get_all_courses()
        return self.load_view('index.html', all = all)
    def add(self):
        if len(request.form['name']) < 15:
            flash('Course name must at least 15 characters long')
            return redirect('/')
        course={
            'name': request.form['name'],
            'description': request.form['description']
        }
        self.models['WelcomeModel'].add(course)
        return redirect('/')
    def delete_check(self, id):
        check = self.models['WelcomeModel'].check(id)
        return self.load_view('check.html', check = check)
    def delete(self, id):
        self.models['WelcomeModel'].delete(id)
        return redirect('/')
