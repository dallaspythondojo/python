from system.core.controller import *

class Logins(Controller):
	def __init__(self, action):
		super(Logins, self).__init__(action)
		self.load_model('Login')


	def index(self):
		if 'user' in session:
			return redirect('/success')
		return self.load_view('index.html')

	def create(self):
		user = {
			'firstname' : request.form['firstname'],
			'lastname'	: request.form['lastname'],
			'email' : request.form['email'],
			'password' : request.form['password'],
			'confirm' : request.form['confirm']
		}

		create_status = self.models['Login'].create_user(user)
		if create_status['status'] == True:
			session['user'] = user['user']
			session['loginreg'] = 'registered.'
			return redirect('/success')
		else:
			for message in create_status['errors']:
				flash(message, 'regis_errors')
			return redirect('/')

	def login(self):
		user = {
			'email' : request.form['email'],
			'password' : request.form['password']
		}
		login_status = self.models['Login'].login_user(user)
		if login_status['status'] == True:
			session['user'] = login_status['user']
			session['loginreg'] = 'logged in.'
			return redirect('/success')
		else:
			for message in login_status['errors']:
				flash(message, 'logins_errors')
			return redirect('/')

	def success(self):
		return self.load_view('success/success.html', name = session['user']['firstname'], loginreg= session['loginreg'])

	def logout(self):
		session.clear()
		return redirect('/')







