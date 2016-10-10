from flask import Flask, render_template, session, request, redirect, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'/^(?=.*[0-9])(?=.*[A-Z])\w{8,}$/')
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    if len(request.form['email']) < 1 or len(request.form['f_name']) < 1 or len(request.form['l_name']) < 1:
        flash("Fields cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif not request.form['f_name'].isalpha():
        flash("Invalid Name! First Name cannot contain and characters or numbers")
    elif not request.form['l_name'].isalpha():
        flash("Invalid Name! Last Name cannot contain and characters or numbers")
    elif not PW_REGEX.match(request.form['password']):
        print request.form['password']
        print type(request.form['password'])
        flash("Invalid password!password must have at least 1 uppercase letter and 1 numeric value")
    elif request.form['password'] != request.form['c_password']:
        flash('Password does not match the confirmation')
    else:
        flash("Success!")
        print 'Success'
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)
  