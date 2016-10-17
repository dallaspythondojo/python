from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    color = 'tmnt'
    return render_template('ninja.html', color=color)

@app.route('/ninja/<hue>')
def ninja_color(hue):
    ninja_dict = {'blue': 'leonardo', 'red': 'raphael', 'purple': 'donatello', 'orange': 'michelangelo'}

    if hue in ninja_dict:
        color = ninja_dict[hue]
    else:
        color = 'notapril'

    return render_template('ninja.html', color=color)
app.run(debug=True)
