
from system.core.model import Model

def isNum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    def show_all(self):
        query = "SELECT * from product"
        return self.db.query_db(query)
    def add_update(self, product_info, product_id):
        errors=[]
        print product_id

        if not product_info['name']:
            errors.append("Product name cannot be empty!")
        if not product_info['description']:
            errors.append("Product must have a description!")
        elif len(product_info['description'])>250:
            errors.append("Product description can't be longer than 250 characters!")
        if not isNum(product_info['price']):
            errors.append("Price must be an integer or decimal number!")


        if errors==[]:
            if product_id==0:
                query="INSERT INTO product (name, description, price) VALUES (:name, :description, :price)"
                data= { 'name': product_info['name'],
                        'description': product_info['description'],
                        'price': float(product_info['price'])
                }
                self.db.query_db(query, data)
                return {'check': True, 'errors': 'None'}
            else:
                query="UPDATE product SET name= :name, description = :description, price= :price WHERE id= :id"
                data ={ 'name': product_info['name'],
                        'description': product_info['description'],
                        'price': float(product_info['price']),
                        'id': product_id
                      }
                self.db.query_db(query,data)
                return {'check': True, 'errors': 'None'}

        return {'check': False, 'errors': errors}

    def show_one(self, product_id):
        query="SELECT * FROM product WHERE id= :id"
        data={ 'id': product_id }
        return self.db.get_one(query,data)

    def destroy(self, product_id):
        query="DELETE FROM product WHERE id= :id"
        data={ 'id': product_id }
        return self.db.query_db(query,data)


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
