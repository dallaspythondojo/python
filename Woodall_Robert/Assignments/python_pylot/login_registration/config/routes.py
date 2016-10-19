from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/login'] = 'Users#login'
routes['POST']['/register'] = 'Users#register'
routes['GET']['/success'] = 'Users#success'
routes['GET']['/logout'] = 'Users#logout'
