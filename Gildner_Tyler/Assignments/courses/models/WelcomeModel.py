from system.core.model import Model

class WelcomeModel(Model):

    def __init__(self):
        super(WelcomeModel, self).__init__()

    def index(self):
        query = "SELECT * FROM courses"
        return self.db.query_db(query)
    def courses(self, course):
        query = "INSERT INTO courses (name, description, created_at) VALUES (:name, :description, NOW())"
        course = {'name': course['name'], 'description': course['description']}
        return self.db.query_db(query, course)
    def delete(self, id):
        query = "SELECT * FROM courses WHERE id = :id"
        data = { 'id':id }
        return self.db.query_db(query, data)
    def deletedelete(self, id):
        query = "DELETE FROM courses WHERE id = :id"
        data = { 'id':id }
        return self.db.query_db(query, data)
