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
        
    def add_product(self, data):
        errors = []
        if len(data['name'])<2 or len(data['description'])<2:
            errors.append("Name and or description must be greater than 2 characters")
        
        if errors:
            return{ 'status':false, 'errors': errors}
        my_data = {'name' :data['name'], 'description':data['description'], 'price' :float(data['price'])}
        query = "INSERT INTO products (name, description, price) VALUES (:name, :description, :price)"
        
        pid = self.db.query_db(query, my_data)
        query = "SELECT * FROM products WHERE id = :id"
        
        product = self.db.query_db(query, {'id' :pid})

        
        return {'status': True, 'product': product[0]}
    
    def load(self):
        query = 'SELECT id, name, description, price FROM products'
        
        products = self.db.query_db(query)
        print"Product from model{}".format(products)
        return products
    
    def show_product(self, id):
        
        query = "SELECT * FROM products WHERE id = :id"
        
        product = self.db.query_db(query, {'id' :id})
        return product
    
    def update(self, data):
        query = 'UPDATE products SET name = :name, description = :description, price = :price, updated = NOW() WHERE id =:id'
        
        mydata = {'name' :data['name'], 'description': data['description'], 'price' :float(data['price']), 'id':int(data['id'])}
        
        self.db.query_db(query,data)
        
    def remove(self, id):
        self.db.query_db('DELETE FROM products WHERE id = :id', {'id' :id})
        
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """