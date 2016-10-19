"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def select(self):
        return self.db.query_db('SELECT * FROM product')

    def create(self, info):
        try:
            float(info['price'])
        except ValueError:
            return [ False, 'Price must be a number']

        query = 'INSERT INTO product (name, description, price) VALUES (:name, :description, :price)'
        data = {
            'name': info['name'],
            'description': info['description'],
            'price': info['price']
        }
        self.db.query_db(query, data)
        return [True]

    def show(self, id):
        query = 'SELECT * FROM product WHERE id = :id'
        data = { 'id' : id}
        return self.db.query_db(query, data)

    def update(self, info, id):
        query = 'UPDATE product SET name = :name, description = :description, price = :price WHERE id = :id'
        data = {
            'name': info['name'],
            'description': info['description'],
            'price': info['price'],
            'id': id
        }
        return self.db.query_db(query, data)

    def delete(self, id):
        query = 'DELETE FROM product WHERE id = :id'
        data = { 'id': id}
        return self.db.query_db(query, data)
