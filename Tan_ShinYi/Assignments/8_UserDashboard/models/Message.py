
from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()
    def get_message(self, user_id):
        query="SELECT m.id, m.message, m.created_at, m.page_user_id, u.first_name, u.last_name, m.created_at AS date_created FROM message m JOIN user u ON m.user_id = u.id WHERE page_user_id = :user_id ORDER BY created_at DESC"
        return self.db.query_db(query, {'user_id': user_id})
    def message(self,info):
        query = "INSERT INTO message (user_id, page_user_id, message) VALUES (:user_id, :page_user_id, :message)"
        self.db.query_db(query, info)


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
