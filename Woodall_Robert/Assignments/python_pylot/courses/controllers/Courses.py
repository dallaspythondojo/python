from system.core.controller import *

class Courses(Controller):
	def __init__(self, action):
		super(Courses, self).__init__(action)
		self.load_model('Course')
		self.db = self._app.db
	
	def index(self):
		if not 'courses' in session:
			session['courses'] = []
		
		session['courses'] = self.models['Course'].get_all_courses()
		
		print session['courses']
		
		return self.load_view('index.html', courses=session['courses'])
	
	def add(self):
		# validate inputs
		# course name required and at least 15 characters long
		# course desc optional
		
		data = {
			'title': request.form['name'],
			'description': request.form['description']
		}
		
		self.models['Course'].add_course(data)
		
		return redirect('/')
	
	def remove_course(self, course_id):
		self.models['Course'].delete_course(course_id)
		
		return redirect('/')
	