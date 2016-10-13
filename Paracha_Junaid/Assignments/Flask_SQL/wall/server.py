
from flask import Flask, render_template, session, request, redirect, flash
from flask.ext.bcrypt import Bcrypt
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z])\w{8,}$')
app = Flask(__name__)
app.secret_key = 'my_secret_key'
mysql = MySQLConnector(app, 'wall')
bcrypt = Bcrypt(app)
@app.route('/')
def index():
    session['Register_class'] = 'hide'
    session['Login_class'] = 'show'
    if 'user' in session:
        return redirect('/logged_in')
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    print request.form
    if not 'action' in request.form:
        flash('we got a problem...')
        print "Ibrokere"
        return redirect('/')
    valid = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("User name is invalid!")
        valid = False
        print valid        
        return redirect('/')
    elif not PW_REGEX.match(request.form['password']):
        flash("Password is invalid!")        
        valid = False        
        return redirect('/')
    else: 
        Str = "SELECT * FROM user WHERE email= :email"
        data = {
                 'email':request.form['email'], 
                }
        user_data = mysql.query_db(Str,data)
        print user_data
        if user_data != []:
            print 'point1'
            session['user info'] = user_data[0]

            if session['user info']['email'].lower() != request.form['email'].lower():
                flash("Bad email/pass combination")
                session['Login_class'] = 'hide'
                session['Register_class'] = 'show'
                valid = False
                return redirect('/register')
            
            elif not bcrypt.check_password_hash(session['user info']['password'], request.form['password']):
                flash("Bad email/pass combination")
                valid = False
                return redirect('/')

            if valid == True :           
                return redirect('/logged_in')
        else:  
            flash("You are not a Registered user please register")
            session['Login_class'] = 'hide'
            session['Register_class'] = 'show'
            valid = False
            print 'point2'
            return render_template('index.html')     

@app.route('/logged_in')
def logged_in():

    user_messages = mysql.query_db('SELECT u.first_name, u.last_name, u.id as user_id, m.message, m.id mid, date_format(m.created_at, "%M %D %Y") created_at FROM message m Join user u on u.id= m.user_id ORDER BY m.created_at DESC')
    message_comment = mysql.query_db('SELECT c.message_id, u.first_name, u.last_name, u.id as user_id, c.comment, c.id cid, date_format(c.created_at, "%M %D %Y") created_at FROM comment c Join user u on u.id= c.user_id ORDER BY c.created_at DESC')

    return render_template('user.html', user_messages = user_messages, message_comment = message_comment)


@app.route('/logout')
def logout():
    flash("You are logged out")
    session.clear()
    return redirect('/')

@app.route('/register', methods = ['POST'])
def register():
    Reg_valid = True
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1:
        flash("Fields cannot be blank!")
        Reg_valid = False
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        Reg_valid = False
        return redirect('/')
    elif not request.form['first_name'].isalpha():
        flash("Invalid Name! First Name cannot contain and characters or numbers")
        Reg_valid = False
        return redirect('/')
    elif not request.form['last_name'].isalpha():
        flash("Invalid Name! Last Name cannot contain and characters or numbers")
        Reg_valid = False
        return redirect('/')
    elif not PW_REGEX.match(request.form['password']):
        print request.form['password']
        print type(request.form['password'])
        flash("Invalid password!password must have at least 1 uppercase letter and 1 numeric value")
        Reg_valid = False
        return redirect('/')
    elif request.form['password'] != request.form['c_password']:
        flash('Password does not match the confirmation')
        Reg_valid = False
        return redirect('/')
    if Reg_valid == True:
       
        pwd = bcrypt.generate_password_hash(request.form['password'])
        Str = "INSERT INTO user(first_name, last_name, password, email, created_at, updated_at) VALUE (:first_name, :last_name, :password, :user_email, NOW(), NOW())"
        data = { 
                'first_name': request.form['first_name'] ,
                'last_name': request.form['last_name'] ,
                'password': pwd ,
                'user_email': request.form['email'] 
                }
        try:
            print mysql.query_db(Str,data)
        except Exception as e:
            print e
            flash("Hey, there was a problem creating that account")
            return redirect('/')
        
        session['added_email'] = request.form['email']
        return redirect('/')
    return redirect('/')

@app.route('/post_message', methods = ['POST'])
def post_message():
    Str = "INSERT INTO message(message, user_id, created_at, updated_at) VALUE (:message, :user_id, NOW(), NOW())"
    data = { 
            'message': request.form['message'] ,
            'user_id': session['user info']['id']
    }
    try:
        print mysql.query_db(Str,data)
    except Exception as error:
        print error
        flash("There is issue in your post please try again")
        return redirect('/logged_in')    
    # session['user_messages'] = mysql.query_db('SELECT u.first_name, u.last_name, m.message, m.id mid, date_format(m.created_at, "%M %D %Y") created_at FROM message m Join user u on u.id= m.user_id ORDER BY m.created_at DESC')
    return redirect('/logged_in' )  

@app.route('/post_comment/<mid>', methods = ['POST'])
def post_comment(mid):
    Str = "INSERT INTO comment(comment, message_id, user_id, created_at, updated_at) VALUE (:comment, :message_id, :user_id, NOW(), NOW())"
    data = { 
            'comment': request.form['comment'],
            'message_id': mid,
            'user_id': session['user info']['id']
    }
    try:
        print mysql.query_db(Str,data)
    except Exception as error:
        print error
        flash("There is issue in your message please try again")
        return redirect('/logged_in')    
    # session['user_messages'] = mysql.query_db('SELECT u.first_name, u.last_name, m.message, m.id mid, date_format(m.created_at, "%M %D %Y") created_at FROM message m Join user u on u.id= m.user_id ORDER BY m.created_at DESC')
    return redirect('/logged_in' )  

@app.route('/delete_comment/<cid>', methods = ['POST']) 
def delete_comment(cid):
    Str = "DELETE FROM wall.comment WHERE id= :id"
    data = { 'id':cid }
    print data
    try:
        print mysql.query_db(Str,data)
    except Exception as error:
        print error
        flash("There is issue in your message please try again")
        return redirect('/logged_in')   
    return redirect('logged_in')



if __name__ == '__main__':
  app.run(debug = True)
  

