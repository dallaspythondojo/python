from system.core.model import Model
import re
from flask import session
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def registering(self,user):
        errors = []
        if not user['first']:
            errors.append('First name cannot be blank')
        elif len(user['first']) < 2:
            errors.append('First name must be at least 2 characters long')
        elif not user['first'].isalpha():
            errors.append('Letters only')
        if not user['last']:
            errors.append('Last name cannot be blank')
        elif len(user['last']) < 2:
            errors.append('Last name must be at least 2 characters long')
        elif not user['last'].isalpha():
            errors.append('Letters only')
        if not user['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(user['email']):
            errors.append('Email format must be valid!')
        if not user['password']:
            errors.append('Password cannot be blank')
        elif len(user['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif user['password'] != user['confirm']:
            errors.append('Password and confirmation must match!')
        if errors:
            return {"status": False, "errors": errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(user['password'])
            query = "INSERT INTO user (first,last,email,pw_hash,created_at,updated_at) VALUES (:first,:last,:email,:pw_hash,NOW(),NOW())"
            data = {
            'first':user['first'],
            'last':user['last'],
            'email':user['email'],
            'pw_hash':hashed_pw
            }
            self.db.query_db(query,data)
            query = "SELECT * FROM user ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(query)
            return { "status": True, "user": users[0] }


    def logining(self,user):
        errors = []
        if not EMAIL_REGEX.match(user['email']):
            errors.append('Email format must be valid!')
        password = user['password']
        query = "SELECT * FROM user WHERE email = :email LIMIT 1"
        data = {'email':user['email']}
        user = self.db.get_one(query,data)
        if user:
            if self.bcrypt.check_password_hash(user.pw_hash,password):
                return { "status": True, "user": user }
            else:
                errors.append('Email or password incorrect!')
        else:
            errors.append('Email or password incorrect!')
        if errors:
            return {"status": False, "errors": errors}
        return False

    def logout(self):
        session.clear()
        return self
