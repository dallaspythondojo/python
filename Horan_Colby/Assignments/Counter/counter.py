from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)
app.secret_key = 'SEEEEEEEECRET'


@app.route('/')
def index():
	if not 'counter' in session:
		session['counter'] = 0
	session['counter'] += 1
	return render_template('counter.html', counter = session['counter'])

@app.route('/process_or_some_page', methods=['post'])
def doit():
	if not 'count' in session:
		session['counter'] += 0
	session['counter'] += 1
	return redirect('/')

@app.route('/clear', methods=['post'])
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)
