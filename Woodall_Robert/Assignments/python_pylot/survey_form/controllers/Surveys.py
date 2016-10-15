from system.core.controller import *

class Surveys(Controller):
	def __init__(self, action):
		super(Surveys, self).__init__(action)
	
	def index(self):
		if not 'submission_count' in session:
			session['submission_count'] = 0
			
		return self.load_view('index.html')
	
	def process(self):
		# validate form data here
		
		if not 'submission_count' in session:
			session['submission_count'] = 0
		else:
			session['submission_count'] += 1
		
		session['form_data'] = {
			'name': request.form['name'],
			'location': request.form['location'],
			'fav_lang': request.form['fav_lang'],
			'comment': request.form['comment'],
			'submission_count': session['submission_count']
		}
		
		return redirect('/result')
	
	def display_result(self):
		if not 'submission_count' in session:
			session['submission_count'] = 0
			
		flash('Thanks for submitting this form! You have submitted this form {} times now.'.format(session['submission_count']), 'alert alert-success')
		
		return self.load_view('result.html', data=session['form_data'])
	
	def reset_session(self):
		session.clear()
		return redirect('/')