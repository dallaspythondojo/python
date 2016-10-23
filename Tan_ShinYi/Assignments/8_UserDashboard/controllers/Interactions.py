from system.core.controller import *

class Interactions(Controller):
    def __init__(self, action):
        super(Interactions, self).__init__(action)
        self.load_model('Message')
        self.load_model('Comment')
        self.load_model('User')
    def show(self, user_id):
        session['viewing']=user_id
        user = self.models['User'].show_user(user_id)
        messages = self.models['Message'].get_message(user_id)
        print messages
        comments = self.models['Comment'].get_comment(user_id)
        return self.load_view('show.html', user=user[0], messages=messages, comments=comments)
    def message(self):
        info={ 'user_id': session['user']['id'],
               'message': request.form['message'],
               'page_user_id': request.form['page_user_id']
        }
        self.models['Message'].message(info)
        return redirect('/users/show/'+ str(session['viewing']))
    def comment(self):
        info={ 'user_id': session['user']['id'],
               'comment': request.form['comment'],
               'message_id': request.form['message_id']
        }
        self.models['Comment'].comment(info)
        return redirect('/users/show/'+ str(session['viewing']))
