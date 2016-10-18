"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *

class Login(Controller):
	def __init__(self, action):
		super(Login, self).__init__(action)

		self.load_model('LoginModel')
		self.db = self._app.db

	def index(self):
		all_users = self.models['LoginModel'].get_all()
		return self.load_view('index.html', all_users = all_users)

	def register(self):
		capture = {
					'email': request.form['email'],
					'first_name': request.form['first_name'],
					'last_name': request.form['last_name'],
					'password': request.form['password'],
					'confirm_password': request.form['confirm_password']
					}

		reg_info = self.models['LoginModel'].register_user(capture)
		if reg_info['status'] == True:
			session['user'] = reg_info['user']['first_name']
			session['email'] = reg_info['user']['email']
			session['id'] = reg_info['user']['id']
			return redirect('/success')
		else:
			for var in reg_info['errors']:
				flash(var)
			return redirect('/')
	
	def login(self):
		capture = {
				'email': request.form['email'],
				'password': request.form['password']
		}

		login_info = self.models['LoginModel'].login_user(capture)
		print login_info
		if login_info['status'] == True:
			session['id'] = login_info['user'][0]['id']
			session['user'] = login_info['user'][0]['first_name']
			session['email'] = login_info['user'][0]['email']
			return redirect('/success')
		else:
			print login_info['errors']
			for var in login_info['errors']:
				flash(var)
			return redirect('/')

	def success(self):
		return self.load_view('success.html')