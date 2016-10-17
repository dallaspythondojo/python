from system.core.router import routes
routes['default_controller'] = 'Randoword'
routes['POST']['/process'] = 'Randoword#process'
routes['POST']['/clear'] = 'Randoword#clear'
