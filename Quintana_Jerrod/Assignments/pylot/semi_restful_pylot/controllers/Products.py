from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')


    def index(self):
        all = self.models['Product'].select()
        return self.load_view('index.html', all = all)

    def new(self):
        return self.load_view('new.html')

    def create(self):
        create = self.models['Product'].create(request.form.copy())
        if create[0] == False:
            flash(create[1], 'regis_errors')
            return redirect('/products/new')
        return redirect('/products')

    def show(self, id):
        show = self.models['Product'].show(id)
        return self.load_view('show.html', show = show[0])

    def edit(self, id):
        show = self.models['Product'].show(id)
        return self.load_view('edit.html', show = show[0])

    def update(self, id):
        self.models['Product'].update(request.form.copy(), id)
        return redirect('/products')

    def destroy(self, id):
        self.models['Product'].delete(id)
        return redirect('/products')
