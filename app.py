from flask import render_template

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', user=name)
