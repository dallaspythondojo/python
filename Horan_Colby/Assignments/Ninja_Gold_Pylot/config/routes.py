
from system.core.router import routes


routes['default_controller'] = 'Ninjas'
routes['POST']['/process_money'] = 'Ninjas#process_money'