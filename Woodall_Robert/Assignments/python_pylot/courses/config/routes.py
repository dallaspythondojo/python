from system.core.router import routes

routes['default_controller'] = 'Courses'
routes['POST']['/courses/add'] = 'Courses#add'
routes['GET']['/courses/destroy/<int:course_id>'] = 'Courses#remove_course'
