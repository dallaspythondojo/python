
from system.core.router import routes

routes['POST']['/process'] = 'Welcome#process'

routes['POST']['/reset'] = 'Welcome#reset'

routes['default_controller'] = 'Welcome'

