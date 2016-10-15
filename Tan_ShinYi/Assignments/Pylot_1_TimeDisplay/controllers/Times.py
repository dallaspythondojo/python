from system.core.controller import *
from time import strftime,localtime

class Times(Controller):
    def __init__(self, action):
        super(Times, self).__init__(action)
    def index(self):
        date= strftime('%b %d, %Y', localtime())
        time= strftime('%I:%M %p')
        return self.load_view('index.html',date=date, time=time)

        #TO DO: How to set it so the date_time updates in real time
        #(because, it currently only captures the time of the page load)
