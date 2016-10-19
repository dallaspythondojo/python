"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Friend')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        if 'id' in session:
            return redirect('view')
        else: 
            session['id'] = 0
            session['registration']='show'
            session['success']='hide'
            
        return self.load_view('index.html')
    
    def add_friend(self):
        mydata ={
            'fname' :request.form['fname'],
            'lname' :request.form['lname'],
            'email' :request.form['email'],
            'pwhash':request.form['pwhash'],
            'rpwd' :request.form['rpwd']
        }
        
        user = self.models['Friend'].add_friend(mydata)
        
        if user['status'] == True:
            session['id'] = user['user_created']['id']
            session['fname'] = user['user_created']['fname']
            return redirect('/view')
            
        else: 
            for message in user['errors']:
                flash(message, 'regis_error')
            
            return redirect('/')
        
    
    def login(self):
        mydata = {'email' :request.form['email'], 'pwd' :request.form['pwd']}
        
        user = self.models['Friend'].login_check(mydata)
        if user['status'] == True:
            print "printing user at loging {}".format(user)
            session['id'] = user['user_login']['id']
            session['fname'] = user['user_login']['fname']
            return redirect('/view')
        
        else:
            for message in user['errors']:
                flash(message, 'regis_error')
            return redirect('/')
        
    def view(self):
        return self.load_view('success.html')
    
        
    def logout(self):
        session.clear()
        return redirect('/')
