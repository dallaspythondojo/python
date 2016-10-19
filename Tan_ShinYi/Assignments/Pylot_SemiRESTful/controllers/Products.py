from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
    def index(self):
        products=self.models['Product'].show_all()
        return self.load_view('index.html', products=products)

    def new(self):
        if 'name' not in session:
            session['name']= ''
        if 'description' not in session:
            session['description']=''
        if 'price' not in session:
            session['price']=''
        return self.load_view('new.html')
    def create(self):
        session['name'] = request.form['name']
        session['description'] = request.form['description']
        session['price'] = request.form['price']
        product_info={  'name': request.form['name'],
                        'description': request.form['description'],
                        'price': request.form['price']
        }
        check = self.models['Product'].add_update(product_info, 0)
        if check['check']:
            session.clear()
            flash("Your product has now been added!", "confirmation")
            return redirect('/')
        else:
            for message in check['errors']:
                flash(message, "error")
            return redirect('/products/new')


    def show(self, product_id):
        product = self.models['Product'].show_one(product_id)
        return self.load_view('show.html', product=product)


    def edit(self, product_id):
        product = self.models['Product'].show_one(product_id)
        return self.load_view('edit.html', product=product)

    def update(self, product_id):
        print 'product_id'
        product_info={  'name': request.form['name'],
                        'description': request.form['description'],
                        'price': request.form['price']
        }

        check = self.models['Product'].add_update(product_info, product_id)
        if check['check']:
            flash("Your product has now been updated!", "confirmation")
            return redirect('/')
        else:
            for message in check['errors']:
                flash(message, "error")
            return redirect('/products/edit/'+ str(product_id))

    def destory(self, product_id):
        self.models['Product'].destroy(product_id)
        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')
