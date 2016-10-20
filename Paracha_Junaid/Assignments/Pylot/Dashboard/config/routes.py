
from system.core.router import routes


routes['GET']['/'] = 'Landing#index'
routes['GET']['/Users'] = 'Users#index'
routes['GET']['/Users/logged_in'] = 'Users#success'
routes['POST']['/Users/Register'] = 'Users#create'
routes['POST']['/Users/Loggin_user'] = 'Users#loggin'
routes['GET']['/Logout'] = 'Users#logout'
routes['GET']['/Users/registration'] = 'Users#registration'
routes['GET']['/Users/Dashboard'] = 'Dashboards#dashboard'
routes['GET']['/Users/Dashboard/add_new_user'] = 'Dashboards#add_new_user'
routes['POST']['/Users/Dashboard/create'] = 'Dashboards#create'
routes['GET']['/Dashboard/remove/<remove_id>/<remove_email>'] = 'Dashboards#remove'
routes['GET']['/Dashboard/confirm_remove'] = 'Dashboards#confirm_remove'
routes['GET']['/Users/Dashboard/edit/<id>'] = 'Dashboards#edit_user'
routes['POST']['/Users/Dashboard/update/<id>'] = 'Dashboards#update_user'
routes['GET']['/Users/Wall/<id>'] = 'Walls#wall'
routes['POST']['/Users/Wall/post_message/<id>'] = 'Walls#post_message'
routes['POST']['/Users/Wall/post_comment/<mid>/<id>'] = 'Walls#post_comment'
routes['POST']['/Users/Wall/delete_comment/<cid>/<id>'] = 'Walls#delete_comment'


"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

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
