from system.core.controller import *
from time import strftime
import random


class NinjaGold(Controller):
	def __init__(self, action):
		super(NinjaGold, self).__init__(action)
	
	def index(self):
		if not 'gold_count' in session:
			session['gold_count'] = 0
			session['activities'] = []
		
		return self.load_view('index.html', gold_count=session['gold_count'], log=session['activities'])
	
	def process_gold(self):
		location = {
			'farm': random.randint(10, 20),
			'cave': random.randint(5, 10),
			'house': random.randint(2, 5),
			'casino': random.randint(-50, 50)
		}
		
		gold = location[request.form['location']]
		session['gold_count'] += gold
		
		if request.form['location'] == 'casino':
			session['activities'].append(
				{ 'outcome': 'gained' if gold > 0 else 'lost',
				  'activity': 'Entered a casino and {} {} golds! {}'.format('gained' if gold > 0 else 'lost', abs(gold), strftime('%b %d %Y %I:%M %p'))
				})
		else:
			session['activities'].append(
				{ 'outcome': 'gained',
				  'activity': 'Earned {} golds from the {}! {}'.format(gold, request.form['location'], strftime('%b %d %Y %I:%M %p'))
				})
		
		return redirect('/')
	
	def reset(self):
		session.clear()
		return redirect('/')
	