from application import app
from flask import render_template

@app.route('/monstersUI')
def monstersUI():
    return render_template('monsterUI.html')
