from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = 'ThisIsSecret'

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'email' not in session:
        session['email']= ""
    return render_template('index.html')

@app.route('/add_email', methods=['POST'])
def add_email():
    verify=True
    session['email'] = request.form['email']

    if len(session['email']) < 1:
        flash("Email field cannot be empty!", "error")
        verify=False
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Format!", "error")
        verify=False

    if verify==True:
        query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"
        data = { 'email': request.form['email'] }
        mysql.query_db(query, data)
        session.clear()
        flash("The email addres you entered ({}) is a VALID email address! Thank you!".format(request.form['email']), "success")
        return redirect('/success')

    return redirect('/')

@app.route('/success')
def success():
    query = "SELECT email_id, email, DATE_FORMAT(created_at, '%c/%d/%y %l:%i %p') AS created_at FROM email"
    emails = mysql.query_db(query)
    print emails
    return render_template('success.html', all_emails=emails)


@app.route('/delete/<email_id>')
def delete(email_id):
    query = "DELETE FROM email WHERE email_id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)
