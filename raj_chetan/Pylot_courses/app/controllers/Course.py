"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *

class Course(Controller):
	def __init__(self, action):
		super(Course, self).__init__(action)

		self.load_model('CourseModel')
		self.db = self._app.db

   
	def index(self):
		all_data = self.models['CourseModel'].get_all_data()
		return self.load_view('index.html', all_data = all_data)

	def addCourse(self, method = 'POST'):
		if 'add_course_hidden' in request.form:
			if len(request.form['course_name'])	> 15:	
				course_name = request.form['course_name']
			else:
				print 'course name is not long enough...'
				return redirect('/')
			course_description = request.form['course_description']
		print course_name, course_description
		course_dict = {'coursename': course_name, 'coursedescription': course_description}

		self.models['CourseModel'].add_course(course_dict)

		return redirect('/')

	def destroyCourse(self, id):
		self.models['CourseModel'].destroy_course(id)
		return redirect('/')