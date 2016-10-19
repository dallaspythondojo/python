from system.core.controller import *

class Dashboards(Controller):
	def __init__(self, action):
		super(Dashboards, self).__init__(action)

		self.load_model('Dashboard')
		self.db = self._app.db	
		
	def dashboard(self):
		print session
		if not 'id' in session:
			return redirect('/Users')
		users = self.models['Dashboard'].get_all_users()
		print users
		return self.load_view('Dashboard/dashboard.html', users=users)
	
	