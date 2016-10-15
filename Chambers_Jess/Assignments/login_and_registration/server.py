
from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
import re
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_registration')

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

@app.route('/logged', methods=['GET'])
def logged():
    if not verify_login():
        return redirect('/')
    return render_template('logged.html')

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

        insert_query = "INSERT INTO user (f_name, l_name, email, pw_hash, created_at) VALUES (:f_name, :l_name, :email, :pw_hash, NOW())"
        query_data = { 'f_name': f_name, 'l_name': l_name, 'email': email, 'pw_hash': pw_hash }

        user_id = mysql.query_db(insert_query, query_data)

        query_all = "SELECT * FROM user WHERE id = :id"
        data = {'id': user_id}
        logged_in = mysql.query_db(query_all, data)

        session['user'] = logged_in[0]

        return render_template('logged.html')

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
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if bcrypt.check_password_hash(user[0]['pw_hash'], pw):
        return redirect ('/logged')
  # login user
    else:
        flash('Invalid login credentials, please try again.')
        return redirect ('/')

app.run(debug=True)


# if (len(request.form['fname']) < 1 or len(request.form['lname']) < 1 or len(request.form['email']) < 1 or len(request.form['pw'] <1)):
