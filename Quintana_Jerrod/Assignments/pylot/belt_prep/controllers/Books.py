from system.core.controller import *
# for message in create['errors']:
#     flash(message, 'regis_errors')
def Valid():
    if 'user' in session: return True

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model('Book')
        self.load_model('Author')

# routes['/books'] = 'Books#index'
    def index(self):
        if not Valid():
            flash('You must be logged in to view homepage', 'register')
            return redirect('/')
        recent = self.models['Book'].most_recent()
        all = self.models['Book'].all()
        print all
        return self.load_view('books.html', all = all, recent = recent)

# routes['/books/add'] = 'Books#add'
    def add(self):
        all = self.models['Author'].all()
        return self.load_view('create.html', all = all)

# routes['/books/<id>'] = 'Books#show'
    def show(self, id):
        book = self.models['Book'].show(id)
        return self.load_view('book_show.html', book = book)

# routes['POST']['/books/create'] = 'Books#create'
    def create(self):
        if len(request.form['new_author']) > 0:
            author_id = self.models['Author'].create_author(request.form.copy())
            if author_id['errors']:
                flash(author_id['errors'][0])
                return redirect('/books/add')
        else: author_id = request.form['aid']
        author_id = author_id['author_id']
        book_id = self.models['Book'].create_book(request.form.copy(),author_id, session['user']['id']  )
        if book_id['errors']:
            flash(book_id['errors'][0])
            return redirect('/books/add')
        book_id = book_id['book_id']
        review = self.models['Book'].create_review(request.form.copy(), session['user']['id'], book_id)
        if review['errors']:
            flash(review['errors'][0])
            return redirect('/books/add')
        return redirect('/books')

        # I have a problem where if I hit the error messages for the create review model function, it still runs the first two functions, so it creates an author or just creates a book. How could i fix this without added delete queries in the flash errors part where it tells it to flash messages and redirects.

# routes['POST']['/review/add/<bid>'] = 'Books#add_review'
    def add_review(self, bid):
        check = self.models['Book'].check(session['user']['id'], bid)
        if check['errors']:
            flash(check['errors'])
            return redirect('/books/'+bid)
        add = self.models['Book'].add(request.form.copy(), session['user']['id'])
        if add['errors']:
            flash(add['errors'][0])
            return redirect('/books/'+bid)
        return redirect('/books/'+bid)

# routes['/destroy/<mid>'] = 'Books#delete'
    def delete(self, rid, bid):
        self.models['Book'].delete(rid)
        return redirect('/books/'+bid)
