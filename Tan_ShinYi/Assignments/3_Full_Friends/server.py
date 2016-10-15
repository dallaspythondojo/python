from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'friendshipsdb')
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
        verify=False
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Format!", "error")
        verify=False
    return verify


@app.route('/')
def index():
    if 'first_name' not in session:
        session['first_name']=""
    if 'last_name' not in session:
        session['last_name']=""
    if 'email' not in session:
        session['email']= ""
    query = "SELECT * FROM user"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

@app.route('/friends', methods=['POST'])
def create():
    verify= check()

    if verify==True:
        query = "INSERT INTO user (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
        data = {
                'first_name': session['first_name'],
                'last_name':  session['last_name'],
                'email': session['email']
           }
        mysql.query_db(query, data)
        session.clear()

    return redirect('/')


@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    query = "SELECT * FROM user WHERE id = :id"
    data = { 'id': friend_id }
    edit_this_friend = mysql.query_db(query, data)
    return render_template('edit.html', friend=edit_this_friend)

@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    verify= check()

    if verify==True:
        query = "UPDATE user SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email'],
                 'id': friend_id
               }
        mysql.query_db(query, data)
        session.clear()
        return redirect('/')

    return redirect('/friends/' + friend_id + '/edit')


@app.route('/friends/<friend_id>/delete', methods=['POST'])
def destroy(friend_id):
    query = "DELETE FROM user WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
