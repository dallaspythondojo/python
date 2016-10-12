from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = '123456'
mysql = MySQLConnector(app,'fullfriends')

@app.route('/')
def index():
    query = "SELECT * FROM friend"
    friend = mysql.query_db(query)

    return render_template('index.html', all_friend=friend)



@app.route('/friends', methods = ['POST'])
def create():

    query = "INSERT INTO friend (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name': request.form['last_name'],
             'email': request.form['email']
           }

    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    return render_template('edit.html', id = id)

@app.route('/friends/<id>', methods = ['POST'])
def update(id):
    session['id'] = 'id'
    query = "UPDATE friend SET email = :email, first_name = :first_name, last_name = :last_name WHERE id = :id"
    data = {
                'id': id,
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email':  request.form['email']
              }
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods = ['POST'])
def delete(id):
    query = "DELETE FROM friend WHERE id= :id"
    data = { 'id':id }

    mysql.query_db(query, data)

    return redirect('/')
app.run(debug=True)
