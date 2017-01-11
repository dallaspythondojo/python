from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Below is how we will utilize md5
# password = 'password';
# encrypted_password = md5.new(password).hexdigest();

app = Flask(__name__)
app.secret_key = 'authenticate!@%#'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'walldb')

# valid_form runs all our 'new user' validation requirements
def valid_logon():
    if (len(request.form['username']) < 1 or
    len(request.form['password']) < 1):
        flash('Please enter your username and password', 'error')
        return False
    return True

def valid_form():
    if (len(request.form['first_name']) < 1 or
    len(request.form['last_name']) < 1 or
    len(request.form['last_name']) < 1 or
    len(request.form['email']) < 1 or
    len(request.form['password']) < 1 or
    len(request.form['confpwd']) < 1 or
    len(request.form['username']) < 1):
        flash('Please fill out all forms', 'error')
        return False
    elif (not request.form['first_name'].isalpha() or not
    request.form['last_name'].isalpha()):
        flash('A name not a number', 'error')
        return False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address', 'error')
        return False
    elif len(request.form['password']) < 8:
        flash('Password must be at least 8 characters', 'error')
        return False
    elif request.form['password'] != request.form['confpwd']:
        flash('Passwords must match', 'error')
        return False
    query = "SELECT un FROM user"
    # data = { 'username': username }
    username_list = mysql.query_db(query)
    for val in username_list:
        if val['un'] == request.form['username']:
            flash('username already exsists', 'error')
            return False
    return True

def verification():
    if not 'user' in session:
        return False
    else:
        return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def register():
    return render_template('register.html')

@app.route('/registration/submit', methods = ['POST'])
def submit_reg():
    if not valid_form():
        return redirect('/registration')

    password = bcrypt.generate_password_hash(request.form['password'])
    query = "INSERT INTO user (un, fn, ln, email, pw) VALUES (:username, :first_name, :last_name, :email, :password)"
    data = {
        'username': request.form['username'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': password
        }
    user_id = mysql.query_db(query, data)

    query = "SELECT * FROM user WHERE id = :id"
    data = { 'id': user_id }
    logged = mysql.query_db(query, data)

    session['user'] = logged[0]

    return redirect('/home')

@app.route('/home')
def home():
    if not verification():
        return redirect('/')

    return render_template('home.html')

@app.route('/login', methods = ['POST'])
def login():
    if not valid_logon():
        return redirect('/')

    login_query = "SELECT * FROM user WHERE un = :username"
    login_data = { 'username': request.form['username'] }
    logged = mysql.query_db(login_query, login_data)
# Below ensures that no errors occur when failing to login. The first ensures that if the username doesn't exsist it will return: invalid username. It does this by checking the variable 'logged' right after creating it. If the user name is wrong logged will be empty.
    if request.form['username'].lower() != logged[0]['un'].lower():
        flash('Invalid username', 'error')
        return redirect('/')
# Below checks hashed pass with entered hashed pass.
    if bcrypt.check_password_hash(logged[0]['pw'],request.form['password']):
        session['user'] = logged[0]
        return redirect('/home')
# Below will only ever run if the system found the user name but the passwords did not match.
    else:
        flash ('Invalid username / password', 'error')
        return redirect('/')

@app.route('/wall')
def wall():
    if not verification():
        return redirect('/')

    query = "SELECT post.comment, user.id AS uid, DATE_FORMAT(post.created_at,'%d/%m/%Y %h:%i %p') as created_at, user.un, post.id FROM post LEFT JOIN user ON user.id = post.user_id ORDER BY post.created_at DESC;"
    posts = mysql.query_db(query)

    query = "SELECT DATE_FORMAT(reply.created_at,'%d/%m/%Y %h:%i %p') as created_at, reply.reply, reply.post_id, user.un FROM reply LEFT JOIN user ON reply.user_id = user.id"
    replys = mysql.query_db(query)

    return render_template('wall.html', post = posts, reply = replys)

@app.route('/post', methods=['POST'])
def post():
    if not verification():
        return redirect('/')

    query = "INSERT INTO post (comment, user_id) VALUES (:comment, :user_id)"
    data = { 'comment' : request.form['comment'], 'user_id' : session['user']['id']}

    mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/reply', methods=['POST'])
def reply():
    if not verification():
        return redirect('/')
    print request.form['post-id']

    query = "INSERT INTO reply (reply, user_id, post_id) VALUES (:reply, :user_id, :post_id)"
    data = { 'reply' : request.form['reply'], 'user_id' : session['user']['id'], 'post_id' : request.form['post-id']}

    mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/delete', methods=['POST'])
def delete():
    print request.form['deleteme']
    delete_query = "DELETE FROM post WHERE id = :id"
    data = { 'id' : request.form['deleteme'] }

    print mysql.query_db(delete_query, data)

    return redirect('/wall')

app.run(debug=True)
