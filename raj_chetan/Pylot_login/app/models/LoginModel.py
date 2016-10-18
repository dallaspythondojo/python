from system.core.model import Model
import re
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
name_regex = re.compile(r'^[a-zA-Z]+$')

class LoginModel(Model):
    def __init__(self):
        super(LoginModel, self).__init__()
    
    def get_all(self):
        return self.db.query_db('SELECT * from user')

    def register_user(self, info):
        print info['first_name']
        errors = []
        query = "INSERT INTO user (first_name, last_name, email, password_hash, created_at) VALUES (:first_name, :last_name, :email, :password_hash, NOW())"
        if (len(info['first_name']) > 2 and name_regex.match(info['first_name'])):
            valid_first_name = info['first_name']
        else:
            errors.append('First name is not valid.')
            print "first name error."
        if len(info['last_name']) > 2 and name_regex.match(info['last_name']):
            valid_last_name = info['last_name']
        else:
            errors.append('Last name is not valid.')
            print "last name error."
        if email_regex.match(info['email']):
            valid_email = info['email']
            print 'Email is valid.'
        else:
            errors.append('Email address is not valid')
            print "email error."
        if ((len(info['password']) > 8) and (info['password'] == info['confirm_password'])):
            password_hash = self.bcrypt.generate_password_hash(info['password'])
        else:
            errors.append('Your password entry is not valid or did not match.')
            print "password error."
        if errors:
            return {'status': False, 'errors': errors}
            print "ERRORS DETECTED!!!!"
        else:
            print "reached final else!"
            data = {'first_name': valid_first_name, 'last_name': valid_last_name, 'email': valid_email, 'password_hash': password_hash}
            self.db.query_db(query, data)
            user_return = self.db.query_db('SELECT * from user ORDER BY id DESC LIMIT 1')
            return {'status': True, 'user': user_return[0]}

    def login_user(self, info):
        errors = []
        if ((len(info['email']) > 1) and (len(info['password']) > 1)):
            query = "SELECT * FROM user WHERE email = :email LIMIT 1"
            data = {'email': info['email']}
            user = self.db.query_db(query, data)
            if user:
                if self.bcrypt.check_password_hash(user[0]['password_hash'], info['password']):
                    return {'status': True, 'user': user}
                else: 
                    errors.append("Password validation fail")
                    return {'status': False, 'errors': errors}
            else: 
                errors.append("User does not exist.")
        
#I know this is giving the user back too much data but I've split PW and email failures into two seperate sections for debugging
                return {'status': False, 'errors': errors}
        else:
            errors.append("You must enter an email and/or password")
            return {'status': False, 'errors': errors}

