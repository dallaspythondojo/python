
from system.core.router import routes

routes['default_controller'] = 'Products'
routes['/products/new'] = 'Products#new'
routes['POST']['/products/create'] = 'Products#create'
routes['/products/show/<int:product_id>'] = 'Products#show'
routes['/products/edit/<int:product_id>'] = 'Products#edit'
routes['POST']['/products/update/<int:product_id>'] = 'Products#update'
routes['POST']['/products/destroy/<int:product_id>'] = 'Products#destroy'

routes['/reset'] = 'Products#reset'

"""
    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
