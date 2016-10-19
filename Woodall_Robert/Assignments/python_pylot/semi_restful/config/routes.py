from system.core.router import routes

routes['default_controller'] = 'Products'
routes['GET']['/products/new'] = 'Products#display_new_product'
routes['POST']['/products/add'] = 'Products#add_product'
routes['POST']['/products/update'] = 'Products#update_product'
routes['GET']['/products/show/<int:product_id>'] = 'Products#display_product'
routes['GET']['/products/edit/<int:product_id>'] = 'Products#edit_product'
routes['GET']['/products/delete/<int:product_id>'] = 'Products#delete_product'
