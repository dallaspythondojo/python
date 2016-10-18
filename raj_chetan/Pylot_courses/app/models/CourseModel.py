""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class CourseModel(Model):
    def __init__(self):
        super(CourseModel, self).__init__()

    def add_course(self, course):
        query = "INSERT INTO course (coursename, description, created_at) values (:coursename, :coursedescription, now())"
        data = {'coursename': course['coursename'], 'coursedescription': course['coursedescription']}
        return self.db.query_db(query, data)

    def get_all_data(self):
        query = "SELECT * FROM course"
        return self.db.query_db(query)

    def destroy_course(self, id):
        query = "DELETE FROM course WHERE id = :course_id"
        data = {'course_id': id}
        return self.db.query_db(query, data)