from application import app
from collections import User, Inquery
from flask import session, abort

@app.route('/startInquery/<alias>')
def startInquery(alias):
    if not(session.get('logged_in')):
        return redirect(url_for('login'))
    user = User.objects(alias = session.get("alias")).get()
    try:
        ruser = User.objects(alias = alias)[0]
    except IndexError:
        abort(400)
    inquery = Inquery(user = ruser, reporters = [user])
    inquery.save()
    
    return 'true'
