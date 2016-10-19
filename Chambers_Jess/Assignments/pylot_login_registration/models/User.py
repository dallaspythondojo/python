from system.core.model import *
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def create_user(self, user_info):

        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not user_info['f_name']:
            errors.append('Name cannot be blank')
        elif len(user_info['f_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not user_info['l_name']:
            errors.append('Name cannot be blank')
        elif len(user_info['l_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not user_info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append('Email format must be valid')
        if not user_info['password']:
            errors.append('Password cannot be blank')
        elif len(user_info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif user_info['password'] != user_info['pw_confirmation']:
            errors.append('Password and confirmation must match')

        if errors:
            return {"status": False, "errors": errors}

        else:
            f_name = user_info['f_name']
            l_name = user_info['l_name']
            email = user_info['email']
            password = user_info['password']
            pw_hash = self.bcrypt.generate_password_hash(password)

            insert_query = "INSERT INTO user (f_name, l_name, email, pw_hash) VALUES (:f_name, :l_name, :email, :pw_hash)"
            insert_data = { 'f_name': f_name, 'l_name': l_name, 'email': email, 'pw_hash': pw_hash }

            try:
                user_id = self.db.query_db(insert_query, insert_data)
            except Exception as e:
                print e
                errors.append('We were unable to create your account at this time. If you have already registered, please login with existing email.')
                return {"status": False, "errors": errors}

            get_user_query = "SELECT * FROM user WHERE id = :id"
            data = {'id': user_id}
            user = self.db.query_db(get_user_query, data)

            return { "status": True, "user": user[0] }

    def login_user(self, login_info):
        errors = []

        if len(login_info['password']) <1:
            errors.append('Please Enter Password')

        elif len(login_info['email']) < 1:
            errors.append('Please Enter Email')

        if errors:
            return {"status": False, "errors": errors}

        else:
            email = login_info['email']
            password = login_info['password']
            user_query = "SELECT * FROM user WHERE email = :email LIMIT 1"
            user_data = {'email': login_info['email']}

            user = self.db.query_db(user_query, user_data)
            if user:
                if self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
                    return { "status": True, "user": user[0] }

            else:
                errors.append('Please Enter Valid Password')

                return {"status": False, "errors": errors}
