
from system.core.router import routes


routes['default_controller'] = 'Users'

routes['POST']['/users/create'] = 'Users#create'

routes['GET']['/users'] = 'Users#users'

routes['POST']['/login'] = 'Users#login'

routes['GET']['/clear'] = 'Users#clear'

"""
    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
