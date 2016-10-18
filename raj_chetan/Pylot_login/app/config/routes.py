"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes


routes['default_controller'] = 'Login'
routes['POST']['/process_registration'] = 'Login#register'
routes['POST']['/process_login'] = 'Login#login'
routes['GET']['/success'] = 'Login#success'
