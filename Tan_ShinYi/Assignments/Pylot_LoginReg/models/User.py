
from system.core.model import Model
import re

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def login(self, login_info):
        verify=True
        errors=[]

        if len(login_info['email']) < 1:
            errors.append("Email field cannot be empty!")
            verify=False
        elif not EMAIL_REGEX.match(login_info['email']):
            errors.append("Invalid Email Format!")
            verify=False

        if verify==True:
            user_query = "SELECT * FROM user WHERE email = :email LIMIT 1"
            query_data = { 'email': login_info['email'] }
            user = self.db.query_db(user_query, query_data)
            if len(user)<1: #checks if the email exist in database
                errors.append("Email and/or Password is incorrect!")
            elif self.bcrypt.check_password_hash(user[0]['password'], login_info['pw']):
                return {'check': True, 'user': user[0]}
            else:
                errors.append("Email and/or Password is incorrect!", "Error")

        return {'check': False, 'errors': errors }

    def register(self, reg_info):
        verify=True
        errors=[]

        query = "SELECT email FROM user WHERE email= :email"
        data = { 'email': reg_info['email'] }
        test = self.db.query_db(query, data)
        if len(test)>0: #ensures no two users have the same email address
            errors.append("Please double check your email.")
            verify=False

        if len(reg_info['first_name']) < 2 or len(reg_info['last_name']) < 2:
            errors.append("Name (First and Last) cannot be less than 2 characters!")
            verify=False
        elif reg_info['first_name'].isalpha() == False or reg_info['last_name'].isalpha() == False:
            errors.append("Name (First or Last) can only contain letters!")
            verify=False

        if len(reg_info['email']) < 1:
            errors.append("Email field cannot be empty!")
            verify=False
        elif not EMAIL_REGEX.match(reg_info['email']):
            errors.append("Invalid Email Format!")
            verify=False

        if len(reg_info['pw'])<8:
            errors.append("Password must contain at least 8 characters!!")
            verify=False
        elif reg_info['pw'] != reg_info['con_pw']:
            errors.append("Passwords do not match!!")
            verify=False

        if verify==True:
            pw_hash = self.bcrypt.generate_password_hash(reg_info['pw'])
            insert_query = "INSERT INTO user (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :pw_hash)"
            query_data = { 'first_name': reg_info['first_name'], 'last_name': reg_info['last_name'], 'email': reg_info['email'], 'pw_hash': pw_hash }
            temp = self.db.query_db(insert_query, query_data)
            query= "SELECT * FROM user WHERE user_id= :id LIMIT 1"
            data= { 'id': temp }
            user= self.db.query_db(query, data)
            return {'check': True, 'user': user[0]}

        return {'check': False, 'errors': errors }
