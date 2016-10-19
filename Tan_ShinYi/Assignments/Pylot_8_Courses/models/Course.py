
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    def get_courses(self):
        query = "SELECT *, DATE_FORMAT(created_at, '%b %D, %Y %h:%i%p') AS date_created FROM course ORDER BY created_at DESC"
        return self.db.query_db(query)
    def course_add(self, inject):
        errors=[]
        if len(inject['name'])<15:
            errors.append("Name must be at least 15 characters long!")
        if errors==[]:
            query= "INSERT INTO course (name, description) VALUES (:name, :description)"
            data= { 'name': inject['name'], 'description': inject['description'] }
            self.db.query_db(query, data)
            return {'check': True, 'errors': 'None'}
        return {'check': False, 'errors': errors}

    def course_info(self, course_id):
        query = "SELECT id, name, description FROM course WHERE id = :id"
        data = { 'id': course_id }
        return self.db.query_db(query, data)
    def course_delete(self, course_id):
        query="DELETE FROM course WHERE id= :id"
        data = { 'id': course_id }
        self.db.query_db(query, data)
