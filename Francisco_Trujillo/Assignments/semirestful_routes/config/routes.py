"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Products'
routes['POST']['/add'] = 'Products#add'
routes['/addproduct'] = 'Products#addproduct'
routes['/product/<int:id>'] = 'Products#show'
routes['/product/edit/<int:id>'] = 'Products#showe'
routes['POST']['/update/<int:id>'] = 'Products#update'
routes['/product/remove/<int:id>'] = 'Products#remove'

