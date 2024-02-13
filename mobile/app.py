from flask import Flask, render_template, request, url_for, flash, redirect
import os

print(os.urandom(24).hex())
app = Flask(__name__)

app.config['SECRET_KEY'] = '6cddf7756b9c57390fb7630019a7da4bb1ac822ccbcbaba1'

messages = [{'title': 'Instructions',
             'content': 'Navigate to the form tab at the top of the page. Please enter '
                        'pill information for three pills along with the various information '
                        'listed. If multiple values correspond to an entry, please separate them '
                        'with a comma. Please enter times in this format: 9:00am. '}
            ]

# returns index template
@app.route('/')
def index():
    return render_template('index.html', messages=messages)

# error checking for data in title and content fields
@app.route('/create/', methods=('GET', 'POST'))
def create():

    if request.method == 'POST':
        1name = request.form['1name']
        1dispense = request.form['1dispense']
        1times = request.form['1times']
        1days = request.form['1days']

        if not 1name:
            flash('Name is required!')
        elif not 1dispense:
            flash('Dispense is required!')
        elif not 1times:
            flash('Times is required!')
        elif not 1days:
            flash('Days is required!')
        else:
            # messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')

# make sure this is the last line in file


# git add/commit
app.run()