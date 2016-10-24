
from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register(self, info):
        errors = []
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        if not info['name']:
            errors.append("Name can't be blank")
        elif len(info['name']) < 2:
            errors.append('Name must be at least 2 characters')
        if not info['alias']:
            errors.append("Alias can't be blank")
        elif len(info['alias']) < 2:
            errors.append('Alias must be at least 2 characters')
        if not info['email']:
            errors.append("Email can't be blank")
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email must be in proper format')
        if not info['pwd']:
            errors.append("Password can't be blank")
        elif len(info['pwd']) < 8:
            errors.append('Password must be at least 8 characters long')
        if not info['confirm']:
            errors.append("Confirmation Password can't be blank")
        elif info['pwd'] != info['confirm']:
            errors.append('Password and Confirmation Password must match')
        if errors:
            return {'errors' : errors}
        query = 'INSERT INTO user (name, alias, email, password) VALUES (:name, :alias, :email, :pwd)'
        info['pwd'] = self.bcrypt.generate_password_hash(info['pwd'])
        try:
            user_id = self.db.query_db(query, info)
        except error:
            errors.append('Email or Alias is already in use')
            return {'errors' : errors}
        user = self.db.query_db('SELECT * FROM user WHERE id = :id', {'id': user_id})
        return {'errors': errors, 'user': user[0]}

    def login(self, info):
        query = 'SELECT * FROM user WHERE alias = :alias'
        user = self.db.query_db(query, info)
        if len(user) < 1 or not self.bcrypt.check_password_hash(user[0]['password'], info['pwd']):
            return {'errors': 'Alias or Password incorrect'}
        return {'errors': [], 'user' : user[0]}

    def show(self, id):
        show = self.db.query_db('SELECT * FROM user WHERE id = :id', {'id': id})
        return show

    def user_review(self, id):
        rev = self.db.query_db('SELECT * FROM review WHERE user_id = :id', {'id' : id})
        return rev
