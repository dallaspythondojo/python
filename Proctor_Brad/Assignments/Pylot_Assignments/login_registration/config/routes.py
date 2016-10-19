
from system.core.router import routes


routes['default_controller'] = 'Users'
routes['POST']['/process'] = 'Users#process'
routes['/success'] = 'Users#success'
routes['/logout'] = 'Users#logout'
