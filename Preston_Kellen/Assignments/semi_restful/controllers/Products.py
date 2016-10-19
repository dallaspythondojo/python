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

        """

        This is an example of a controller method that will load a view for the client

        """
    def home(self):
        return redirect('/products')

    def index(self):
        products = self.models['Product'].load()
        return self.load_view('index.html', products = products)

    def new(self):
        return self.load_view('new.html')

    def create(self):
        new = self.models['Product'].new(request.form.copy())
        return redirect('/')

    def edit(self, id):
        edit = self.models['Product'].edit(id)
        return self.load_view('edit.html', item = edit[0])

    def update(self, id):
        update = self.models['Product'].update(id, request.form.copy())
        return redirect('/')

    def destroy(self, id):
        self.models['Product'].destroy(id)
        return redirect('/')

    def show(self, id):
        show_info = self.models['Product'].show(id)
        return self.load_view('view.html', show = show_info[0])
