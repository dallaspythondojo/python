from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'restfulusersdb')
app.secret_key = 'ThisIsSecret'
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

def check():
    verify=True
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    if len(session['first_name']) < 1 or len(session['last_name']) < 1:
        flash("Name (First and Last) cannot be empty!", "error")
        verify=False
    elif session['first_name'].isalpha() == False or session['last_name'].isalpha() == False:
        flash("Name (First or Last) can only contain letters!", "error")
        verify=False
    if len(session['email']) < 1:
        flash("Email cannot be empty!", "error")
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Format!", "error")
        verify=False

    return verify


@app.route('/users')
def index():
    query = "SELECT *, DATE_FORMAT(created_at, '%M %D, %Y') created_at2 FROM user"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create():

    if check():
        query = "INSERT INTO user (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
        data = {
                'first_name': session['first_name'],
                'last_name':  session['last_name'],
                'email': session['email']
           }
        session.clear()
        user_id = mysql.query_db(query, data)
        return redirect('/users/'+ str(user_id))

    return redirect('/users/new')

@app.route('/users/<user_id>')
def show(user_id):
    query = "SELECT * FROM user WHERE id = :id"
    data = { 'id': user_id }
    user_info = mysql.query_db(query, data)
    return render_template('show.html', user=user_info)

@app.route('/users/<user_id>/edit')
def edit(user_id):
    query = "SELECT * FROM user WHERE id = :id"
    data = { 'id': user_id }
    user_info = mysql.query_db(query, data)
    return render_template('edit.html', user= user_info)

@app.route('/users/<user_id>', methods=['POST'])
def update(user_id):

    if check():
        query = "UPDATE user SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email'],
                 'id': user_id
               }
        mysql.query_db(query, data)
        session.clear()
        return redirect('/users/' + user_id)

    return redirect('/users/' + user_id + '/edit')


@app.route('/users/<user_id>/destroy')
def destroy(user_id):
    query = "DELETE FROM user WHERE id = :id"
    data = {'id': user_id}
    mysql.query_db(query, data)
    return redirect('/users')

app.run(debug=True)
