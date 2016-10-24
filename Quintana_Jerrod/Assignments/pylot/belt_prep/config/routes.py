
from system.core.router import routes


routes['/'] = 'Users#index'
routes['/users/<id>'] = 'Users#show'
routes['POST']['/login'] = 'Users#login'
routes['POST']['/register'] = 'Users#registration'
routes['/logout'] = 'Users#logout'


routes['/books'] = 'Books#index'
routes['/books/add'] = 'Books#add'
routes['/books/<id>'] = 'Books#show'
routes['/destroy/<rid>/<bid>'] = 'Books#delete'
routes['POST']['/books/create'] = 'Books#create'
routes['POST']['/review/add/<bid>'] = 'Books#add_review'
