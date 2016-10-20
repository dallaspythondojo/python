from system.core.controller import *

class Dashboards(Controller):
	def __init__(self, action):
		super(Dashboards, self).__init__(action)

		self.load_model('Dashboard')
		self.load_model('User')
		self.db = self._app.db	
		
	def dashboard(self):
		print session
		if not 'id' in session:
			return redirect('/Users')
		users = self.models['Dashboard'].get_all_users()
		print users
		session['delete_user'] = False
		return self.load_view('Dashboard/dashboard.html', users=users)
	
	def add_new_user(self):
		print session
		if not 'id' in session:
			return redirect('/Users')
		if not session['user_level'] == 9:
			return redirect('/Users/Dashboard')
		
		
		return self.load_view('Dashboard/Add.html')
	
	def create(self):
	
		user_info = {
		"first_name" : request.form['first_name'],
		"last_name" : request.form['last_name'],
		"email" : request.form['email'],
		"password" : request.form['password'],
		"confirm_pw" : request.form['confirm_pw']
		}
		# call create_user method from model and write some logic based on the returned value
		# notice how we passed the user_info to our model method
		user_status = self.models['User'].create_user(user_info)
		if user_status['status'] == True:

			return redirect('/Users/logged_in')
		else:
			# set flashed error messages here from the error messages we returned from the Model
			for message in user_status['errors']:
				flash(message, 'regis_errors')
			# redirect to the method that renders the form
			return redirect('/Users/Dashboard/add_new_user')
	
	def remove(self, remove_id, remove_email):
		if not 'id' in session:
			return redirect('/Users')
		if not session['user_level'] == 9:
			return redirect('/Users/Dashboard')
		session['delete_user'] = True
		session['delete_id'] = remove_id
		session['delete_email'] = remove_email


		users = self.models['Dashboard'].get_all_users()
		return self.load_view('Dashboard/dashboard.html', users=users )
		

	def confirm_remove(self):
		if not 'id' in session:
			return redirect('/Users')
		if not session['user_level'] == 9:
			return redirect('/Users/Dashboard')
		
		self.models['Dashboard'].delete_user(session['delete_id'])
		
		session['delete_user'] = False
		session['delete_id']=0
		session['delete_email']=''

		return redirect('/Users/logged_in')
	
	def edit_user(self, id):
		print session
		if not 'id' in session:
			return redirect('/Users')
		if not session['user_level'] == 9:
			return redirect('/Users/Dashboard')
		
		user = self.models['Dashboard'].get_user_by_id(id)
		edit_user = user[0]
		return self.load_view('Dashboard/edit.html', edit_user=edit_user)

	def update_user(self, id):
		user_details = {
			'id': id,
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email']
		}
		self.models['Dashboard'].update_user(user_details)
		return redirect('/Users/Dashboard')