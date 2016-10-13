from flask import Flask, redirect, render_template, flash, session, request
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'restful')
app.secret_key = 'ThisIsSecret'

@app.route('/users')
def index():
    all = mysql.query_db('SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, "%b %d, %Y ") date FROM users')
    return render_template('index.html', all = all)

@app.route('/users/new')
def new():
    session['which'] = 'add'
    return render_template('show.html')
@app.route('/users/create', methods=['POST'])
def create():
    query= 'INSERT INTO users (first_name, last_name, email, created_at) VALUES (:first, :last, :email, NOW())'
    data = {
        'first': request.form['first'],
        'last': request.form['last'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<id>')
def show(id):
    session['which'] = 'show'
    query ='SELECT first_name, last_name, id, email, DATE_FORMAT(created_at, "%b %d, %Y ") date FROM users WHERE id = :id'
    data = { 'id': id}
    all = mysql.query_db(query, data)
    return render_template('show.html', id = id, all = all)

@app.route('/users/<id>/edit')
def edit(id):
    session['which'] = 'edit'
    query = 'SELECT * FROM users WHERE id =:id'
    data = { 'id': id}
    keep = mysql.query_db(query, data)
    return render_template('show.html', id = id, keep = keep)
@app.route('/users/<id>', methods=['POST'])
def finish_edit(id):
    query = "UPDATE users SET first_name = :first, last_name = :last, email = :email WHERE id = :id"
    data = {
        'first' : request.form['edit_first'],
        'last' : request.form['edit_last'],
        'email' : request.form['edit_email'],
        'id' : id
    }
    print mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<id>/destroy')
def delete(id):
    query= 'DELETE FROM users WHERE id = :id'
    data = { 'id': id}
    mysql.query_db(query, data)
    return redirect('/users')

app.run(debug=True)
