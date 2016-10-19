import re
""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Friend(Model):
    def __init__(self):
        super(Friend, self).__init__()
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
    def add_friend(self,mydata):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not mydata['fname'] or not mydata['lname'] or not mydata['email'] or not mydata['pwhash'] or not mydata['rpwd']:
            errors.append('All fields are required')
        elif len(mydata['fname'])<2 or len(mydata['fname'])<2:
            errors.append('First name and/or Last name must be at least two letter')
        elif not EMAIL_REGEX.match(mydata['email']):
            errors.append('Please enter a valid emial')
        elif len(mydata['pwhash'])< 8:
            errors.append('Password must be at least 8 charaters long')
        elif mydata['pwhash']!= mydata['rpwd']:
            errors.append('Password and confirmation must match!')
            
        if errors:
            return{'status': False, 'errors': errors}
        else:
            data = {
                'fname': mydata['fname'],
                'lname': mydata['lname'],
                'email': mydata['email'],
                'pwhash': self.bcrypt.generate_password_hash(mydata['pwhash'])
            }
            query='INSERT INTO friend (fname, lname, email, pwhash) VALUES (:fname, :lname, :email, :pwhash)'
            self.db.query_db(query,data)
            
            query = "SELECT * FROM friend Where email = :email"
            data = {'email': mydata['email']}
            user = self.db.query_db(query,data)
            return {'status' :True, 'user_created' :user[0]}
        
    def login_check(self, mydata):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if EMAIL_REGEX.match(mydata['email']):
            query = "SELECT id, fname, pwhash FROM friend Where email = :email"
            data = {'email': mydata['email']}
            user = self.db.query_db(query,data)
            if self.bcrypt.check_password_hash(user[0]['pwhash'], mydata['pwd']):
                print user[0]
                return {'status' :True, 'user_login' :user[0] }

            else: 
                errors.append('Please enter a valid email or password')
                return {'status': False, 'errors' :errors }

        else: 
            errors.append('Please enter a valid email or password')
            return {'status': False, 'errors' :errors }

           
            
            
        