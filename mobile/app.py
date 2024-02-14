from flask import Flask, render_template, request, url_for, flash, redirect
import os

print(os.urandom(24).hex())
app = Flask(__name__)

app.config['SECRET_KEY'] = '6cddf7756b9c57390fb7630019a7da4bb1ac822ccbcbaba1'

# user instructions
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

        form_list = []

        # pill 1's fields
        name1 = request.form['1name']
        form_list.append(name1)

        dispense1 = request.form['1dispense']
        form_list.append(dispense1)

        times1 = request.form['1times']
        form_list.append(times1)

        days1 = request.form['1days']
        form_list.append(days1)

        # pill 2's fields
        name2 = request.form['2name']
        form_list.append(name2)

        dispense2 = request.form['2dispense']
        form_list.append(dispense2)

        times2 = request.form['2times']
        form_list.append(times2)

        days2 = request.form['2days']
        form_list.append(days2)

        # pill 3's fields
        name3 = request.form['3name']
        form_list.append(name3)

        dispense3 = request.form['3dispense']
        form_list.append(dispense3)

        times3 = request.form['3times']
        form_list.append(times3)

        days3 = request.form['3days']
        form_list.append(days3)

        # making sure each field on form contains information
        if not name1:
            flash("Pill 1's name is required!")
        elif not dispense1:
            flash("Pill 1's dispense is required!")
        elif not times1:
            flash("Pill 1's times are required!")
        elif not days1:
            flash("Pill 1's days are required!")
        elif not name2:
            flash("Pill 2's name is required!")
        elif not dispense2:
            flash("Pill 2's dispense is required!")
        elif not times2:
            flash("Pill 2's times are required!")
        elif not days2:
            flash("Pill 2's days are required!")
        elif not name3:
            flash("Pill 3's name is required!")
        elif not dispense3:
            flash("Pill 3's dispense is required!")
        elif not times3:
            flash("Pill 3's times are required!")
        elif not days3:
            flash("Pill 3's days are required!")
        else:
            # messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

        # user_input = request.form['pill_data']
        # with open('test.txt', 'w') as f:
        #     f.write(str(user_input))

        f = open('test.txt', 'a')
        with open('test.txt', 'w') as f:
            f.write(str(form_list))
            # for entry in form_list:
            #     f.write(entry)

    return render_template('create.html')

# @app.route('/', methods=['POST'])
# def write_data():
#     user_input = request.form['pill_data']
#     with open('test.txt', 'w') as f:
#         f.write(str(user_input))
#     return ('create.html')

# make sure this is the last line in file
app.run()