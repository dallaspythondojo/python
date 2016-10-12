from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'loginreg')
app.secret_key = '123456'
email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)


@app.route('/registration', methods=['POST'])
def create_user():
    if not email_reg.match(request.form['email']):
        flash('Write it like a damn email address.')
        return redirect('/')
    if len(request.form['username']) < 2:
        flash("You must have more character's worth of characters in you than that...")
        return redirect('/')
    if len(request.form['first_name']) < 2 or request.form['first_name'].isalpha() == False:
        flash('Give me your damn name, no numbers and shit.. geez.')
        return redirect('/')
    if len(request.form['last_name']) < 2 or request.form['last_name'].isalpha() == False:
        flash('LAST NAME DUDE!')
        return redirect('/')
    if len(request.form['password']) < 8:
        flash('Does that seem safe to you?')
        return redirect('/')
    if request.form['password'] != request.form['passconfirm']:
        flash("yea, it seems smart to make two passwords...k")
        return redirect('/')
    check = mysql.query_db("SELECT email FROM users")
    for i in check:
        if request.form['email'] == i['email']:
            flash('You think you are unique? Give me an email address that is YOURS!')
            return redirect('/')


    email = request.form['email']
    username = request.form['username']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = bcrypt.generate_password_hash(request.form['password'])
    insert_query = "INSERT INTO users (email, username, first_name, last_name, pw_hash) VALUES (:email, :username, :first_name, :last_name, :password)"


    data = {
             'id': id,
             'email': request.form['email'],
             'username': request.form['username'],
             'first_name': request.form['first_name'],
             'last_name': request.form['last_name'],
             'password': bcrypt.generate_password_hash(request.form['password'])
            }

    mysql.query_db(insert_query, data)

    password = 'password'
    pw_hash = bcrypt.generate_password_hash(password)
    test_password_1 = 'thisiswrong'
    bcrypt.check_password_hash(pw_hash, test_password_1)
    test_password_2 = 'password'
    bcrypt.check_password_hash(pw_hash, test_password_2)
    return redirect('/loginpage')

@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    query="SELECT * FROM users WHERE email = :email LIMIT 1"
    data ={ 'email': request.form['email']}
    users = mysql.query_db(query, data)
    if bcrypt.check_password_hash(users[0]['pw_hash'],request.form['password']):
        return redirect('/congrats')

@app.route('/congrats')
def congrats():
    return render_template('congrats.html')

app.run(debug=True)
