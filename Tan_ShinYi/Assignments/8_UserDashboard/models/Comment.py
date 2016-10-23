
from system.core.model import Model

class Comment(Model):
    def __init__(self):
        super(Comment, self).__init__()
    def get_comment(self, user_id):
        query="SELECT c.comment, c.created_at, c.message_id, u.first_name, u.last_name, c.created_at AS date_created FROM comment c JOIN user u ON c.user_id= u.id ORDER BY created_at DESC"
        return self.db.query_db(query, {'user_id': user_id})
    def comment(self, info):
        insert_query = "INSERT INTO comment (message_id, user_id, comment) VALUES (:message_id, :user_id, :comment)"
        query_data = { 'message_id': info['message_id'], 'user_id': info['user_id'] , 'comment': info['comment'] }
        self.db.query_db(insert_query, query_data)

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
