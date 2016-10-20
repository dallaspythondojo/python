"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Product')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        products = self.models['Product'].load()
        
        return self.load_view('product.html', products=products)
    
    def add(self):
        
        data = {'name' :request.form['name'],
               'description' :request.form['description'],
               'price' :request.form['price']}
        
        product = self.models['Product'].add_product(data)
        
        if product['status'] == True:
            return redirect('/')
        
        return redirect('/addpage')
    
    def addproduct(self):
        return self.load_view('productadd.html')
    
    def show(self,id):
        product = self.models['Product'].show_product(id)
        
        print"from Show{}".format(product)
        return self.load_view('productView.html', product=product[0])    
    
    def showe(self,id):
        product = self.models['Product'].show_product(id)

        print"from Show{}".format(product)
        return self.load_view('productEdit.html', product=product[0])
    
    def update(self,id):
        
        data= {'name': request.form['name'],
              'description' :request.form['description'],
              'price' :request.form['price'],
              'id' : id}
        
        self.models['Product'].update(data)
        
        return redirect('/')
    
    def remove(self,id):
        print id
        self.models['Product'].remove(id)
        return redirect ('/')
