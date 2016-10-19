from system.core.router import routes

routes['default_controller'] = 'Logins'
routes['POST']['/create'] = 'Logins#create'
routes['POST']['/login'] = 'Logins#login'
routes['/success'] = 'Logins#success'
routes['/logout'] = 'Logins#logout'

