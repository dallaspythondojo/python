
from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['/signin'] = 'Welcome#signin'
routes['/register'] = 'Welcome#register'
routes['/logoff'] = 'Welcome#logoff'

routes['POST']['/users/signin'] = 'Users#signin'
routes['POST']['/users/register'] = 'Users#register'
routes['/users/new'] = 'Users#new'
routes['/dashboard/admin'] = 'Users#dash_admin'
routes['/users/edit/<int:user_id>'] = 'Users#edit_admin'
routes['/users/edit'] = 'Users#edit'
routes['POST']['/users/update'] = 'Users#update'
routes['/users/destroy/<int:user_id>'] = 'Users#destroy'
routes['/dashboard'] = 'Users#dash'

routes['/users/show/<int:user_id>'] = 'Interactions#show'
routes['POST']['/message'] = 'Interactions#message'
routes['POST']['/comment'] = 'Interactions#comment'


"""

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path).
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
