
from system.core.router import routes


routes['default_controller'] = 'Welcome'

routes['POST']['/process'] = 'Welcome#process'

routes['POST']['/clear'] = 'Welcome#clear'
