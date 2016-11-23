
from system.core.controller import *
import string
import random

class Generate(Controller):
    def __init__(self, action):
        super(Generate, self).__init__(action)

   
    def index(self):
       
	
        if not 'word' in session:
            session['word']='Random Word'
            session['counter']=0
            
        return self.load_view('index.html')
    
    def random(self):
        session['word']=''
        for i in range (0,14):
            session['word']+=random.choice(string.letters + string.digits)
        print(session['word'])
        session['counter']+=1
        
        return redirect('/')
    
    def signout(self):
        session.clear()
        return redirect('/')
