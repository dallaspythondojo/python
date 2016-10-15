from system.core.controller import *
import string, random

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
    def index(self):
        if 'counter' not in session:
            session['counter']=0
            session['string']=''
        return self.load_view('index.html')
    def generate(self):
        session['counter']+=1
        session['string'] = ''
        for i in range(0,14):
            let_or_int = random.randint(0,1)
            if let_or_int==1:
                session['string']+=random.choice(string.uppercase)
            else:
                session['string']+=str(random.randint(0,9))
        return redirect('/')
    def reset(self):
        session.clear()
        return redirect('/')
