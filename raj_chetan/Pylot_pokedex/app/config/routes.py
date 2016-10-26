"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes


routes['default_controller'] = 'Pokemon'

routes['GET']['/<id>'] = 'Pokemon#whoDat'
