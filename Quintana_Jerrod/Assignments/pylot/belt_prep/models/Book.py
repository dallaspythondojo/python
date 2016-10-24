from system.core.model import Model
import re

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()

    def all(self):
        all = self.db.query_db('SELECT * FROM book')
        return all

    def most_recent(self):
        recent = self.db.query_db('SELECT r.book_id bid, u.alias alias, b.title title, r.rating rating, r.content content, DATE_FORMAT(r.created_at, "%b %d %Y %l:%i %p") date, r.user_id uid FROM review r JOIN book b ON b.id = r.book_id JOIN user u ON u.id = b.user_id ORDER BY date DESC LIMIT 3')
        return recent

    def show(self, id):
        query = 'SELECT b.title title, r.content content, b.user_id uid, b.id bid, a.name aname, r.id rid, r.rating rating, u.alias alias, DATE_FORMAT(r.created_at, "%b %d %Y %l:%i %p") date FROM book b JOIN user u ON u.id = b.user_id JOIN author a ON a.id = b.author_id JOIN review r ON r.book_id = b.id WHERE b.id = :id ORDER BY date DESC'

        show = self.db.query_db(query, {'id': id})
        return show

    # routes['POST']['/review/add'] = 'Books#add_review'
    def add(self, info, uid):
        errors = []
        if not info['content']:
            return {'errors':'Review can\'t be empty'}
        query = 'INSERT INTO review (content, rating, user_id, book_id) VALUES (:content, :rating, :uid, :bid)'
        info['uid'] = uid
        self.db.query_db(query, info)
        return {'errors': errors}

    def create_book(self, info, aid, uid):
        errors = []
        if not(info['title']):
            errors.append('Book title can\'t be empty')
        if errors:
            return {'errors': errors}

        if len(info['new_author']) > 0:
            query = 'INSERT INTO book (title, author_id, user_id) VALUES (:title, :aid, :uid)'
            info['aid'] = aid

        else:
            query = 'INSERT INTO book (title, author_id, user_id) VALUES (:title, :aid, :uid)'

        info['uid'] =uid
        book_id = self.db.query_db(query, info)
        return {'errors': errors, 'book_id': book_id}

    def create_review(self, info, uid, bid):
        errors = []
        if not len(info['content']):
            errors.append('Review field can\'t be empty')
        if errors:
            return {'errors': errors}
        query = 'INSERT INTO review (content, rating, user_id, book_id) VALUES (:content, :rating, :uid, :bid)'
        data = {'content': info['content'], 'rating': info['rating'], 'uid': uid, 'bid':bid}
        self.db.query_db(query, data)
        return {'errors': errors}

    def delete(self, rid):
        delete = self.db.query_db('DELETE FROM review WHERE id =:rid', {'rid': rid})
        return delete

    def check(self, uid, bid):
        errors = []
        query = 'SELECT * FROM review WHERE book_id = :bid and user_id = :uid'
        data = {'bid': bid, "uid": uid}
        check = self.db.query_db(query, data)
        if len(check) > 0:
            errors.append("You can only write a review for a book once")
        return {'errors': errors}
