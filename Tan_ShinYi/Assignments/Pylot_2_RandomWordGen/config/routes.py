from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['GET']['/generate'] ='Welcome#generate'
routes['GET']['/reset'] = 'Welcome#reset'
