"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import string
import random
class Numgen(Controller):
    def __init__(self, action):
        super(Numgen, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        if not 'counter' in session:
            session['counter'] = 1

        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('index.html')

    def process(self):
        KEY_LEN = 14
        base_str = string.letters+(string.digits)
        keylist = [random.choice(base_str) for i in range(KEY_LEN)]
        code = ("".join(keylist))
        session['counter'] += 1
        print 'IT WORKS!'
        return self.load_view('index.html',code=code)
