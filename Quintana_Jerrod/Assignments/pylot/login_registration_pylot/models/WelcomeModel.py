
from system.core.model import Model
import re

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def register(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not info['first']:
            errors.append('First Name cannot be blank')
        elif len(info['first']) < 2:
            errors.append('First Name must be at least 2 characters long')
        if not info['last']:
            errors.append('Last Name cannot be blank')
        elif len(info['last']) < 2:
            errors.append('Last Name must be at least 2 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['confirm']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        query = 'SELECT * FROM user WHERE email =:email'
        data = { 'email': info['email']}
        check = self.db.query_db(query, data)
        print check
        if len(check) > 0:
            errors.append('That email is already in use')
        if errors:
            result = {"status": False, "errors": errors}
            return result
        else:
            # Code to insert user goes here...
            # Then retrieve the last inserted user.
            query = "INSERT INTO user (first_name, last_name, email, password, created_at) VALUES (:first, :last, :email, :password, Now())"
            data = {
                'first': info['first'],
                'last': info['last'],
                'email': info['email'],
                'password': self.bcrypt.generate_password_hash(info['password'])
                }
            self.db.query_db(query, data)
            query = 'SELECT * FROM user WHERE email = :email'
            data = { 'email': info['email']}
            user = self.db.query_db(query, data)
            result = {'status': True, 'user': user[0]}
            return result

    def check_login(self, info):
        query = 'SELECT * FROM user WHERE email = :email'
        data = { 'email' : info['email']}
        check = self.db.query_db(query, data)
        if len(check) < 1 or self.bcrypt.check_password_hash(check[0]['password'], info['password']) == False:
            return {'status': False, 'error': 'Email or Password is incorrect'}
        else:
            query = 'SELECT * FROM user WHERE email = :email'
            data = { 'email': info['email']}
            user = self.db.query_db(query, data)
            return {'status': True, 'user': user[0]}
