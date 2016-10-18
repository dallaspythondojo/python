from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "RedBullGivesMeWings"

mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
    if 'first_name' not in session:
        session['first_name'] = ""
    if 'last_name' not in session:
        session['last_name'] = ""
    if 'email' not in session:
        session['email'] = ""

    query = "SELECT * FROM friend"

    data = mysql.query_db(query)
    return render_template('index.html', data = data)

@app.route('/friends', methods=['POST'])
def friend():
    return render_template('friends.html')

@app.route('/new_friend', methods=['POST'])
def create():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    query = "INSERT INTO friend (first_name, last_name, created_at, updated_at, email) VALUES (:first_name, :last_name, NOW(), NOW(), :email)"

    data = {
        'first_name': session['first_name'],
        'last_name': session['last_name'],
        'email': session['email']
    }

    mysql.query_db(query, data)

    return redirect('/')

@app.route('/friends/<id>/edit', methods=['POST'])
def edit_friend(id):
    session['id'] = id
    query = "SELECT * FROM friend WHERE friend.id = id"

    data = mysql.query_db(query)

    flash(data)

    return render_template('friends.html', data = data, id=id)

@app.route('/friend/<id>/newedit', methods=['POST'])
def update(id):
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    query = "UPDATE friend SET first_name = :first_name, last_name = :last_name, email = :email WHERE friends.id = id"

    data = {
        'id': id,
        'first_name': session['first_name'],
        'last_name': session['last_name'],
        'email': session['email']
    }

    mysql.query_db(query, data)

    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friend WHERE friend.id = id"

    data = {
        'id': id
    }

    mysql.query_db(query, data)

    return redirect('/')

app.run(debug=True)
