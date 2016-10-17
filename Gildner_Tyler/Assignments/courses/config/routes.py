from system.core.router import routes
routes['default_controller'] = 'Welcome'
routes['POST']['/courses'] = 'Welcome#courses'
routes['POST']['/delete/<id>'] = 'Welcome#delete'
routes['POST']['/<id>/delete'] = 'Welcome#deletedelete'
