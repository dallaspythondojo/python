from system.core.model import Model

class Course(Model):
	def __init__(self):
		super(Course, self).__init__()

	def get_all_courses(self):
		return self.db.query_db("SELECT * from courses")
	
	def get_course_by_id(self, course_id):
		query = "SELECT * from courses where id = :course_id"
		return self.db.get_one(query, {'id': course_id})
	
	def add_course(self, course):
		query = "INSERT INTO courses (title, description, created_at) VALUES (:title, :description, NOW())"
		data = { 'title': course['title'], 'description': course['description'] }
		return self.db.query_db(query, data)

	def update_course(self, course):
		query = "UPDATE courses SET title=:title, description=:description WHERE id = :course_id"
		data = { 'title': course['title'], 'description': course['description'], 'course_id': course['id']}
		return self.db.query_db(query, data)
	
	def delete_course(self, course_id):
		query = "DELETE FROM courses WHERE id = :course_id"
		data = { "course_id": course_id }
		return self.db.query_db(query, data)