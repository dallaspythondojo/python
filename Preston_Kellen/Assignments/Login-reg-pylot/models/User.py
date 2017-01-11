from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not info['fn']:
            errors.append('First Name cannot be blank')
        elif len(info['fn']) < 2:
            errors.append('First Name must be at least 2 characters long')
        if not info['ln']:
            errors.append('Last Name cannot be blank')
        elif len(info['ln']) < 2:
            errors.append('Last Name must be at least 2 characters long')
        if not info['un']:
            errors.append('Username cannot be blank')
        elif len(info['un']) < 5:
            errors.append('Username must be at least 5 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['pw']:
            errors.append('Password cannot be blank')
        elif len(info['pw']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['pw'] != info['conf']:
            errors.append('Password and confirmation must match!')
        if errors:
            return {"status": False, "errors": errors}
        else:
            query = "INSERT INTO user (fn, ln, un, email, pw) VALUES (:fn, :ln, :un, :email, :pw)"
            data = { 'fn' : info['fn'], 'ln' : info['ln'], 'un' : info['un'], 'email' : info['email'], 'pw' : self.bcrypt.generate_password_hash(info['pw'])}
            self.db.query_db(query, data)

            query = "SELECT * FROM user WHERE un = :un"
            data = { 'un' : info['un'] }
            users = self.db.query_db(query, data)
            return { "status": True, "user": users[0] }

    def login(self, info):
        errors = []
        if not info['un']:
            errors.append('Username cannot be blank')
        elif len(info['un']) < 5:
            errors.append('Username must be at least 5 characters long')
        if not info['pw']:
            errors.append('Password cannot be blank')
        elif len(info['pw']) < 8:
            errors.append('Password must be at least 8 characters long')
        if errors:
            return {"status": False, "errors": errors}
        else:
            query = "SELECT * FROM user WHERE un =:un"
            data = { 'un' : info['un'] }
            user_pull = self.db.query_db(query, data)
            if len(user_pull) < 1 or not self.bcrypt.check_password_hash(user_pull[0]['pw'],info['pw']):
                return { 'status' : False, 'errors' : 'Email or Password incorrect' }
            else:
                return { 'status' : True , 'user' : user_pull[0] }
    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):2
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
