from flask import Flask, redirect, session, render_template, request, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall')
app.secret_key = 'jamesBrown'
nameReg = re.compile(r'.a-z{2, 60}/i')
emailReg = re.compile(r'[^@]+@[^@]+\.[^@]+')

@app.route('/')
def index():
   if not 'email' in session:
      session['email'] = ''
   if not 'id' in session:
      session['id'] = 0
   if not 'first_name' in session:
      session['first_name'] = ''
   if not 'last_name' in session:
      session['last_name'] = ''
   return render_template('index.html')

@app.route('/process', methods=['POST'])
def submitUser():
   insertUser = "INSERT INTO user (first_name, last_name, email, password, created_at, update_at) VALUES (:firstname, :lastname, :email, :password, Now(), Now())"
   if len(request.form['first_name']) >= 2:
      fname = request.form['first_name']
      session['first_name'] = request.form['first_name']
   else:
      flash("Please enter Valid name:")
      return redirect('/')
   if len(request.form['last_name']) >= 2:
      lname = request.form['last_name']
   else:
      flash("Please enter valid name: ")
      return redirect('/')
   if emailReg.match(request.form['email']):
      email = request.form['email']
   else:
      flash("Please enter valid email:")
      return redirect('/')
   passw = request.form['password']
   confirm = request.form['confirm']
   if not passw == confirm:
      flash("Fix your passwords:")
      redirect('/')
   pw_hash = bcrypt.generate_password_hash(passw)
   dataCheck = {
		'firstname' : fname,
		'lastname'	: lname,
		'email'	: email,
		'password' : pw_hash,
		'password_confirmation' : pw_hash
	}

   result = mysql.query_db(insertUser, dataCheck)
   print dataCheck
   return redirect('/result')

@app.route('/result')
def pageLoad():
    return render_template('result.html', name = session['first_name'])


@app.route('/getuser', methods=['POST'])
def login():
    select = "SELECT first_name, last_name, password, id FROM user WHERE email = :email"
    dataCheck = {
        'email' : request.form['email']
        }
    password = request.form['password']
    user = mysql.query_db(select, dataCheck)
    if bcrypt.check_password_hash(user[0]['password'], password):
        session['email'] = request.form['email']
        session['id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        session['last_name'] = user[0]['last_name']
        print user
        return redirect('/wall')
    else:
        flash("User Not found")
        return redirect('/')

@app.route('/wall')
def wall():
    select = "SELECT first_name, last_name, m.messages AS messages, m.created_at AS message_date, m.id AS message_id, u.id AS user_id FROM user u JOIN messages AS m on m.user_id = u.id ORDER BY m.created_at ASC"
    comments = "SELECT c.messages_id, c.comment, c.created_at, u.first_name, u.last_name, u.id FROM comments c JOIN user u ON c.user_id = u.id"

    print session['id']
    id = {
        'id' : session['id']
        }
    commentInfo = mysql.query_db(comments)
    messageInfo = mysql.query_db(select)
    print commentInfo
    return render_template('wall.html', comments = commentInfo, messages = messageInfo, fullname = session['first_name'] + ' ' + session['last_name'])

@app.route('/postmessage', methods=['POST'])
def postMessage():
    post = "INSERT INTO messages (messages, created_at, update_at, user_id) VALUES (:messages, Now(), Now(), :user_id)"
    values = {
        'messages' : request.form['textArea'],
        'user_id' : session['id']
        }
    result = mysql.query_db(post, values)
    return redirect('/wall')

@app.route('/deleteComment/<id>', methods=['GET'])
def delete(id):
    print 'delete proccessing'
    deleteComments = "DELETE FROM comments WHERE comments.messages_id = :message_id"
    deleteMessage = "DELETE FROM messages WHERE messages.id = :message_id"
    message_id = {
        'message_id': int(id)
        }
    m = mysql.query_db(deleteMessage, message_id)
    print m
    result = mysql.query_db(deleteComments, message_id)
    print 'delete complete'
    return redirect('/')

@app.route('/postComment', methods=['POST'])
def postComment():
    print 'commentArea'
    comment = "INSERT INTO comments (comment, created_at, updated_at, user_id, messages_id) VALUES (:comment, Now(), Now(), :user_id, :messages_id)"
    print session['id']
    print request.form['message_id']
    values = {
        'comment': request.form['commentArea'],
        'user_id': session['id'],
        'messages_id': request.form['message_id']
        }
    print 'insert query...'
    result = mysql.query_db(comment, values)
    print 'success...'
    print result
    return redirect('/wall')

@app.route('/logOff', methods=['POST'])
def logOut():
    if 'id' in session:
        session['id'] = 0
        return redirect('/')

app.run(debug=True)