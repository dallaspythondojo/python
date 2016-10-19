
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/process'] = 'Users#process'
routes['/dashboard'] = 'Users#dashboard'
routes['/logout'] = 'Users#logout'
