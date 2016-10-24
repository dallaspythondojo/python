from system.core.model import Model

class Author(Model):
    def __init__(self):
        super(Author, self).__init__()

    def all(self):
        all = self.db.query_db('SELECT * from author')
        return all
# routes['POST']['/books/create'] = 'Books#create'
    def create_author(self, info):
        errors = []
        query = 'INSERT INTO author (name) VALUES (:new_author)'
        print 'fourth'
        try:
            print 'first'
            author_id = self.db.query_db(query, info)
        except:
            print 'second'
            errors.append('Author already exists in the database')
            return {'errors': errors}
        print 'third'
        return {'errors': errors, 'author_id':author_id}
