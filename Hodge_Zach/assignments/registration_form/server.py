from flask import Flask, render_template, request, redirect, session, flash
import re
from time import gmtime, strftime
app = Flask(__name__)
app.secret_key = "wheninthecourseofhumanevents"

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
PASSWORD_REGEX=re.compile(r'(?=.*?[A-Z])(?=.*?[0-9])')
@app.route('/')
def index():
    if 'email' not in session:
        session['email'] = ""
    if 'first_name' not in session:
        session['first_name'] = ""
    if 'last_name' not in session:
        session['last_name'] = ""
    if 'password' not in session:
        session['password'] = ""
    if 'confirm_password' not in session:
        session['confirm_password'] = ""
    if 'bday' not in session:
        session['bday'] = str(strftime("%Y-%m-%d", gmtime()))
    return render_template('index.html')

@app.route('/processform', methods=['POST'])
def process_form():
    verity = True;
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    session['bday'] = request.form['bday']

    if len(session['email']) < 1:
        flash("Email cannot be empty")
        verity = False

    if len(session['first_name']) < 1:
        flash("First name cannot be empty")
        verity = False

    if len(session['last_name']) < 1:
        flash("Last name cannot be empty")
        verity = False

    if len(session['password']) < 1:
        flash("Password cannot be empty")
        verity = False

    if len(session['confirm_password']) < 1:
        flash("Confirm password cannot be empty")
        verity = False

    if session['first_name'].isalpha() == False or session['last_name'].isalpha() == False:
        flash("Names cannot contain numbers")
        verity = False

    if len(session['password']) < 8:
        flash("Password cannot be less than 8 characters")
        verity = False

    if not EMAIL_REGEX.match(session['email']):
        flash("Invalid email")
        verity = False

    if session['password'] != session['confirm_password']:
        flash("Passwords should match")
        verity = False

    if not PASSWORD_REGEX.match(session['password']):
        flash("Password should contain 1 uppercase letter and 1 number")
        verity = False

    if session['bday'] >= str(strftime("%Y-%m-%d", gmtime())):
        flash("Babies are not allowed to register.")
        verity = False

    if verity == True:
        flash("Thank you! Information submitted!")

    return redirect('/')
app.run(debug=True)
