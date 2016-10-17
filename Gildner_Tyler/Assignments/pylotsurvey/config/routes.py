"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes


routes['default_controller'] = 'Welcome'
routes['POST']['/users'] = 'Welcome#create_user'
routes['GET']['/show_user'] = 'Welcome#show_user'
