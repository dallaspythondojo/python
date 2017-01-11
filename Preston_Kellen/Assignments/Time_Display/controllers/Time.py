from system.core.controller import *
from time import strftime, localtime

class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)
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
        date = strftime('%b %d, %Y', localtime())
        time = strftime('%I:%M %p', localtime())
        return self.load_view('index.html', date = date, time = time)
