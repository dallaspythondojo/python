from system.core.controller import *

class Products(Controller):
	def __init__(self, action):
		super(Products, self).__init__(action)
		self.load_model('Product')
	
	def index(self):
		response = self.models['Product'].get_products()
		
		if len(response['errors']) > 0:
			for error in response['errors']:
				flash(error)
				return redirect('/')
		
		return self.load_view('index.html', products=response['products'])
	
	def display_new_product(self):
		return self.load_view('new_product.html')
	
	def add_product(self):
		response = self.models['Product'].add_product(request.form)
		
		if len(response['errors']) > 0:
			for error in  response['errors']:
				flash(error)
				return redirect('/products/new')
		
		return redirect('/')
	
	def display_product(self, product_id):
		response = self.models['Product'].get_product(product_id)
		
		if len(response['errors']) > 0:
			for error in  response['errors']:
				flash(error)
				return redirect('/')
		
		return self.load_view('product.html', product=response['product'])
	
	def edit_product(self, product_id):
		response = self.models['Product'].get_product(product_id)
		
		if len(response['errors']) > 0:
			for error in  response['errors']:
				flash(error)
				return redirect('/')
			
		return self.load_view('edit.html', product=response['product'])
	
	def update_product(self):
		response = self.models['Product'].update_product(request.form)
		
		if len(response['errors']) > 0:
			for error in  response['errors']:
				flash(error)
				return redirect('/products/update')
			
		return redirect('/')
	
	
	def delete_product(self, product_id):
		response = self.models['Product'].delete_product(product_id)
		
		if len(response['errors']) > 0:
			for error in  response['errors']:
				flash(error)
				
		return redirect('/')
			
		
	