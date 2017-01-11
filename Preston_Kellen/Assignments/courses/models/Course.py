from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()


    def add_course(self, course):
        # Build the query first and then the data that goes in the query
        query = "INSERT INTO course (name, description) VALUES (:name, :description)"
        if not 'name' in course or not 'description' in course:
            return 0
        self.db.query_db(query, course)

    def course_list(self):
        query = "SELECT * FROM course"
        return self.db.query_db(query)

    def single_class(self, id):
        query = "SELECT name, description FROM course WHERE id = :id"
        data = { 'id' : id }
        return self.db.query_db(query, data)

    def delete(self, id):
        query = "DELETE FROM course WHERE id = :id"
        data = { 'id' : id }
        self.db.query_db(query, data)
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
