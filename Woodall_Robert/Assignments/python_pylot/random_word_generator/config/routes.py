from system.core.router import routes

routes['default_controller'] = 'RandomWordGenerator'
routes['POST']['/generate'] = 'RandomWordGenerator#generate'
routes['GET']['/reset'] = 'RandomWordGenerator#reset'
