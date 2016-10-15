
from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
import re
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'the_wall')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = "ThisIsSecret!"

def verify_login():
    if not 'user' in session:
        return False
    else:
        return True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/wall', methods=['GET'])
def logged():
    if not verify_login():
        return redirect('/')

    query_all = "SELECT message, f_name, l_name, user.id as uid, message.id as mid, message.created_at FROM user JOIN message ON message.user_id = user.id ORDER BY message.created_at DESC;"
    all_messages = mysql.query_db(query_all)

    query_all = ("SELECT message.id as mid, comment, f_name, l_name "
    "FROM user "
    "JOIN comment ON comment.user_id = user.id "
    "JOIN message ON message.id = comment.message_id "
    "ORDER BY comment.created_at DESC;")
    all_comments = mysql.query_db(query_all)

    return render_template('wall.html', all_messages=all_messages, all_comments = all_comments)

@app.route('/post', methods=['POST'])
def post():
    if not 'action' in request.form:
        flash('we have a problem...')

    message = request.form['message']
    print message
    insert_message_query = "INSERT INTO message (message, user_id) VALUES (:message, :id);"
    query_data = { 'message': message, 'id': session['user']['id'] }

    mysql.query_db(insert_message_query, query_data)

    return redirect('/wall')

@app.route('/post_comment', methods=['POST'])
def comment():
    if not 'action' in request.form:
        flash('we have a problem...')

    message_id = request.form['message_id']
    comment = request.form['comment']
    insert_comment_query = "INSERT INTO comment (comment, message_id, user_id) VALUES (:comment, :mid, :id);"
    query_data = { 'comment': comment,'mid': message_id, 'id':  session['user']['id'] }

    mysql.query_db(insert_comment_query, query_data)

    return redirect('/wall')

@app.route('/create_user', methods=['POST'])
def create_user():
    if len(request.form['pw']) <8:
        flash('Password must be at least 8 characters.')
        return redirect('/')
    elif not request.form['f_name'].isalpha():
        flash ('Name must contain characters a-z, A-Z')
        return redirect('/')
    elif not request.form['l_name'].isalpha():
        flash ('Name must contain characters a-z, A-Z')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address!')
        return redirect('/')
    else:
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        email = request.form['email']
        pw = request.form['pw']
        pw_hash = bcrypt.generate_password_hash(pw)

        insert_query = "INSERT INTO user (f_name, l_name, email, pw_hash, created_at) VALUES (:f_name, :l_name, :email, :pw_hash, NOW());"
        query_data = { 'f_name': f_name, 'l_name': l_name, 'email': email, 'pw_hash': pw_hash }

        try:
            user_id = mysql.query_db(insert_query,query_data)
        except Exception as e:
            print e
            flash('We were unable to create your account at this time. If you have already registered, please login with existing email.')
            return redirect('/')

        query_all = "SELECT * FROM user WHERE id = :id;"
        data = {'id': user_id}
        logged_in = mysql.query_db(query_all, data)

        session['user'] = logged_in[0]

        return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    if len(request.form['pw']) <1:
        flash('Please enter password.')
        return redirect('/')
    if len(request.form['email']) <1:
        flash('Please enter valid, registered email.')
        return redirect('/')
    email = request.form['email']
    pw = request.form['pw']
    user_query = "SELECT * FROM user WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    logged_in = mysql.query_db(user_query, query_data) # user will be returned in a list

    if (logged_in) <1:
        flash('Email address not found.  Please register.')
        return redirect('/')

    if bcrypt.check_password_hash(logged_in[0]['pw_hash'], pw):
        session['user'] = logged_in[0]
        return redirect ('/wall')
  # login user
    else:
        flash('Invalid login credentials, please try again.')
        return redirect ('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect ('/')
app.run(debug=True)
