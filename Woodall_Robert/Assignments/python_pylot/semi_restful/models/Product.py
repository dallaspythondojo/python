from system.core.model import Model

class Product(Model):
	def __init__(self):
		super(Product, self).__init__()
		
	def get_products(self):
		response = {
			'products': [],
			'errors': []
		}
		
		try:
			response['products'] = self.db.query_db('select * from product')
		except Exception as error:
			print('get_products(): {}'.format(error))
			response['errors'].append('There was an issue retrieving the products!')
		
		return response
	
	def get_product(self, product_id):
		response = {
			'product': {},
			'errors': []
		}
		
		query = 'select * from product where id = :id'
		
		try:
			response['product'] = self.db.query_db(query, {'id': product_id})
		except Exception as error:
			print('get_product(): {}'.format(error))
			response['errors'].append('There was an issue retrieving the products!')
			return response
		
		if len(response['product']) < 1:
			response['errors'].append('Unable to retrieve product!')
			return response
		
		# return just row data
		response['product'] = response['product'][0]
		
		return response
	
	def add_product(self, product):
		response = {
			'product': 0,
			'errors': []
		}
		
		# validate product
		if (len(product['name']) < 1 or
		    len(product['description']) < 1 or
		    len(product['price']) < 1):
			response['errors'].append('All inputs required')
			return response
		elif float(product['price']) < 0:
			response['errors'].append('Price cannot be less than 0.00')
			return response
		
		query = ('insert into product (name, description, price) '
				 'values (:name, :description, :price)')
		
		data = {
			'name': product['name'],
			'description': product['description'],
			'price': float(product['price'])
		}
		
		try:
			response['product'] = self.db.query_db(query, data)
		except Exception as error:
			print('add_product(): {}', error)
			response.append('There was an issue creating your product...try again!')
		
		return response
	
	def update_product(self, product):
		response = {
			'errors': []
		}
		
		query = ('update product '
				 'set name = :name, description = :description, price = :price, updated_at = NOW() '
				 'where id = :id')
		
		data = {
			'name': product['name'],
			'description': product['description'],
			'price': product['price'],
			'id': product['update_product_id']
		}
		
		try:
			self.db.query_db(query, data)
		except Exception as error:
			print('update_product(): {}', error)
			response.append('There was an issue updating your product...try again!')
		
		return response
	
	def delete_product(self, product_id):
		response = {
			'errors': []
		}
		
		query = ('delete from product '
				 'where id = :id')
		
		try:
			self.db.query_db(query, {'id': product_id})
		except Exception as error:
			print('delete_product(): {}', error)
			response.append('There was an issue deleting your product...try again!')
		
		return response
		