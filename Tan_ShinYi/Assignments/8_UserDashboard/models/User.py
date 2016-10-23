
from system.core.model import Model
import re

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def signin(self, login_info):
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
            elif self.bcrypt.check_password_hash(user[0]['password'], login_info['password']):
                return {'check': True, 'user': user[0]}
            else:
                errors.append("Email and/or Password is incorrect!")
        return {'check': False, 'errors': errors }
    def register(self, reg_info, id):
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

        if len(reg_info['password'])<8:
            errors.append("Password must contain at least 8 characters!!")
            verify=False
        elif reg_info['password'] != reg_info['con_password']:
            errors.append("Passwords do not match!!")
            verify=False

        if verify==True:
            if id==0:
                pw_hash = self.bcrypt.generate_password_hash(reg_info['password'])
                insert_query = "INSERT INTO user (first_name, last_name, email, password, user_level) VALUES (:first_name, :last_name, :email, :pw_hash, 1)"
                query_data = { 'first_name': reg_info['first_name'], 'last_name': reg_info['last_name'], 'email': reg_info['email'], 'pw_hash': pw_hash }
                temp = self.db.query_db(insert_query, query_data)
                if temp ==1: #sets first user to sign in as admin
                    self.db.query_db("UPDATE user SET user_level=9 WHERE id=1")
                query= "SELECT * FROM user WHERE id= :id LIMIT 1"
                data= { 'id': temp }
                user= self.db.query_db(query, data)
                return {'check': True, 'user': user[0]}
            else:
                pw_hash = self.bcrypt.generate_password_hash(reg_info['password'])
                insert_query = "INSERT INTO user (first_name, last_name, email, password, user_level) VALUES (:first_name, :last_name, :email, :pw_hash, 1)"
                query_data = { 'first_name': reg_info['first_name'], 'last_name': reg_info['last_name'], 'email': reg_info['email'], 'pw_hash': pw_hash }
                self.db.query_db(insert_query, query_data)
                return {'check': True}


        return {'check': False, 'errors': errors }

    def get_users(self):
        query="SELECT *, DATE_FORMAT(created_at, '%b. %D %Y') date_reg, CONCAT_WS(' ', first_name, last_name) name FROM user"
        return self.db.query_db(query)

    def show_user(self, user_id):
        query="SELECT * FROM user WHERE id= :id"
        data= {'id': user_id}
        return self.db.query_db(query, data)

    def update(self, info, user_level):
        print info['action']
        if info['action']=='info':
            verify=True
            errors=[]

            if len(info['first_name']) < 2 or len(info['last_name']) < 2:
                errors.append("Name (First and Last) cannot be less than 2 characters!")
                verify=False
            elif info['first_name'].isalpha() == False or info['last_name'].isalpha() == False:
                errors.append("Name (First or Last) can only contain letters!")
                verify=False

            if len(info['email']) < 1:
                errors.append("Email field cannot be empty!")
                verify=False
            elif not EMAIL_REGEX.match(info['email']):
                errors.append("Invalid Email Format!")
                verify=False

            if verify==True:
                if user_level==9:
                    query="UPDATE user SET first_name= :first_name, last_name = :last_name, email= :email, user_level = :user_level, updated_at= NOW() WHERE id= :user_id"
                    self.db.query_db(query, info)
                    return {'check': True, 'errors': errors, 'user': None }
                else:
                    query="UPDATE user SET first_name= :first_name, last_name = :last_name, email= :email, user_level = :user_level, updated_at= NOW() WHERE id= :user_id"
                    self.db.query_db(query, info)
                    query="SELECT * FROM user WHERE id= :id"
                    user= self.db.query_db(query, info)
                    return {'check': True,'errors': errors, 'user': user[0]}
            else:
                return {'check': False, 'errors': errors, 'user': None }


        if info['action']=='pw':
            verify=True
            errors=[]

            if len(info['password'])<8:
                errors.append("Password must contain at least 8 characters!!")
                verify=False
            elif info['password'] != info['con_password']:
                errors.append("Passwords do not match!!")
                verify=False

            if verify==True:
                if user_level==9:
                    query="UPDATE user SET password= :password, updated_at= NOW() WHERE id= :id"
                    self.db.query_db(query, {'password':  self.bcrypt.generate_password_hash(info['password']), 'id': info['user_id']})
                    return {'check': True, 'errors': errors, 'user': None }
                else:
                    query="UPDATE user SET password= :password, updated_at= NOW() WHERE id= user_id"
                    self.db.query_db(query, {'password':  self.bcrypt.generate_password_hash(info['password'])})
                    query="SELECT * FROM user WHERE id= :user_id"
                    user= self.db.query_db(query, info)
                    return {'check': True,'errors': errors, 'user': user[0]}
            else:
                return {'check': False, 'errors': errors, 'user': None }

        if info['action']=='desc':
            query="UPDATE user SET description= :description, updated_at=NOW() WHERE id= :user_id"
            self.db.query_db(query, info)
            return {'check': True}


    def destroy(self, user_id):
        query="DELETE FROM user WHERE id= :id"
        data = {'id': user_id}
        self.db.query_db(query, data)

    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_user(self):
        query = "SELECT * from table_name where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

        query = "INSERT into table_name (message, created_at, users_id) values(:message, NOW(), :users_id)"

        query="UPDATE table_name SET name= :name, description = :description, price= :price WHERE id= :id"

        query="DELETE FROM table_name WHERE id= :id"
    """
