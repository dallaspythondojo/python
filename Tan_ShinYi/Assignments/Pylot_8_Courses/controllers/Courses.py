from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db
    def index(self):
        if 'name' not in session:
            session['name']=''
            session['description']=''
        courses=self.models['Course'].get_courses()
        return self.load_view('index.html', courses=courses)

    def add(self):
        session['name']= request.form['name']
        session['description']= request.form['description']
        inject={  'name': request.form['name'],
                'description': request.form['description']
        }
        info= self.models['Course'].course_add(inject)

        if info['check']:
            session.clear()
            flash("Thank you, your course has been added!", "confirmation")
            return redirect('/')
        else:
            for message in info['errors']:
                flash(message, "error")
            return redirect('/')

    def show_destory(self, course_id):
        course_info=self.models['Course'].course_info(course_id)
        return self.load_view('destory.html', course_info=course_info[0])

    def destory(self, course_id):
        self.models['Course'].course_delete(course_id)
        flash("Your course has been deleted!", "confirmation")

        return redirect('/')
