from flask import Flask,render_template, redirect, request, session
import random 
import datetime
app=Flask(__name__)
app.secret_key = "thebestsecretkeyever"


@app.route('/')
def index():
	if not 'gold' in session:
		session['gold'] = 0
	if not 'activities' in session:
		session['activities']=[]
	return render_template('ninja_gold.html')

@app.route('/process', methods=['POST'])
def process():
	buildings = {
		'farm':random.randint(10,20),
		'cave':random.randint(5,10),
		'house':random.randint(2,5),
		'casino':random.randint(-50,50)}
	print request.form['building']
	if request.form['building'] in buildings:
		income = buildings[request.form['building']]
		print income
		session['gold'] += income
		print session['gold']

	if income >= 0:
		income_string=['gained','!']
	elif income <0:
		income_string=['ouch','...!...']

	timestamp=datetime.datetime.now()
	activity= "you went to the {} and {} {} gold{} ({})".format(request.form['building'],income_string[0], income, income_string[1],
timestamp)
	session['activities'].append(activity)
	return redirect('/')

@app.route('/reset')
def reset_game():
	session.clear()
	return redirect('/')


	












if(__name__) ==('__main__'):
	app.run(debug=True)