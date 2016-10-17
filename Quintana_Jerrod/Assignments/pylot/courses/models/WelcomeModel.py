from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    def get_all_courses(self):
        return self.db.query_db('SELECT id, name, description, Date_format(created_at, "%b %d, %Y %h:%i %p") date FROM course ORDER BY created_at DESC')
    def add(self, course):
        query = ('INSERT INTO course (name, description, created_at) VALUES (:name, :desc, Now())')
        data = { 'name': course['name'], 'desc': course['description']}
        return self.db.query_db(query, data)
    def check(self, id):
        query = ('SELECT * FROM course WHERE id = :id')
        data = { 'id': id}
        return self.db.query_db(query,data)
    def delete(self, id):
        query = ('DELETE FROM course WHERE id = :id')
        data = { 'id': id}
        return self.db.query_db(query, data)
    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    Every model has access to the "self.db.query_db" method which allows you to interact with the database

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
