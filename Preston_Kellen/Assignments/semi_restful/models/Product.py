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

    def load(self):
        query = "SELECT * FROM product"
        return self.db.query_db(query)

    def new(self, info):
        errors = []
        if not info['name']:
            errors.append('Name field cannot be empty')
        if not info['description']:
            errors.append('Description field cannot be empty')
        if not info['price']:
            errros.append('Price field cannot be empty')
        if errors:
            return {"status": False, "errors": errors}
        else:
            query = "INSERT INTO product (name, description, price) VALUES (:name, :description, :price)"
            data = { 'name' : info['name'], 'description' : info['description'], 'price' : info['price'] }
            return self.db.query_db(query, data)

    def destroy(self, id):
        query = "DELETE FROM product WHERE id = :id"
        data = { 'id' : id }
        self.db.query_db(query, data)

    def edit(self, id):
        query = "SELECT * FROM product WHERE id = :id"
        data = { 'id' : id }
        return self.db.query_db(query, data)

    def update(self, id, info):
        print info['description']
        # query = "UPDATE product SET name = info['name'], description = info['description'], price = info['price'] WHERE id ="+id
        query = "UPDATE product SET name = :name, description = :description, price = :price WHERE id = :id"
        data = { 'name' : info['name'], 'description' : info['description'], 'price' : info['price'], 'id' : id }
        print '34'
        return self.db.query_db(query, data)

    def show(self, id):
        query = "SELECT * FROM product WHERE id = :id"
        data = { 'id' : id }
        return self.db.query_db(query, data)


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
