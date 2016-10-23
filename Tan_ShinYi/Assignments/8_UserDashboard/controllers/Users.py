from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
    def new(self):
        return self.load_view('new_user.html')
    def signin(self):
        session['email'] = request.form['email']
        status = self.models['User'].signin(request.form.copy())
        if status['check'] == False:
            for message in status['errors']:
                flash(message, "error")
            return redirect('/signin')
        else:
            session.clear()
            session['user']= status['user']
            return redirect('/dashboard')
    def register(self):
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        temp=0

        if session['user']: #this allows us to use register path for both
            temp=1          #new users and admins trying to add a user
                            #by preventing logout of admins when they
                            #register a new user

        status = self.models['User'].register(request.form.copy(),temp)
        if status['check'] == False:
            for message in status['errors']:
                flash(message, "error")
            if temp==1:
                return redirect('/users/new')
            else:
                return redirect('/register')
        else:
            if temp==1:
                x = session['user']
                session.clear()
                session['user'] = x
                return redirect('/dashboard/admin')
            else:
                session.clear()
                session['user']= status['user']
                return redirect('/dashboard')

    def show(self):
        return self.load_view('show.html')
    def dash_admin(self):
        if session['user']['user_level']!=9: #only allows admins on admin dash
            return redirect('/dashboard')
        users=self.models['User'].get_users()
        return self.load_view('A_dashboard.html',users=users)
    def dash(self):
        if session['user']['user_level']==9:
            return redirect('/dashboard/admin')
        users=self.models['User'].get_users()
        return self.load_view('dashboard.html', users=users)
    def edit_admin(self, user_id):
        user=self.models['User'].show_user(user_id)
        print user
        return self.load_view('A_edit.html', user=user[0])
    def edit(self):
        user=self.models['User'].show_user(session['user']['id'])
        return self.load_view('edit.html', user=user[0])
    def update(self):
        if session['user']['user_level']==9:

            status = self.models['User'].update(request.form.copy(), 9)
            if status['check']==False:
                for message in status['errors']:
                    flash(message, "error")
            else:
                flash("Your changes have been saved!", "confirmation")
            return redirect('/users/edit/' + str(request.form['user_id']))
        else:
            user= request.form.copy()
            user['user_id']= session['user']['id']
            status = self.models['User'].update(user, 1)
            if status['check']==False:
                for message in status['errors']:
                    flash(message, "error")
            else:
                flash("Your changes have been saved!", "confirmation")

            return redirect('/users/edit')

    def destroy(self, user_id):
        self.models['User'].destroy(user_id)
        return redirect('/dashboard/admin')
