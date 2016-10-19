
from system.core.router import routes

routes['/products'] = 'Products#index'

routes['/products/new'] = 'Products#new'

routes['POST']['/products/create'] = 'Products#create'

routes['/products/show/<id>'] = 'Products#show'

routes['/products/edit/<id>'] = 'Products#edit'

routes['POST']['/products/edit/update/<id>'] = 'Products#update'

routes['/products/destroy/<id>'] = 'Products#destroy'
