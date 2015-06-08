from application import app
from collections import User, Inquery
from flask import redirect, url_for, abort, session, render_template
from hashlib import sha224
from os import urandom
from forms import Judge

@app.route("/judge")
def judge():
    if not session.get("logged_in"):
        abort(404)

    user = User.objects.get(alias = session.get("alias"))

    if not user.isJudge:
        abort(404)
    
    inqueries = Inquery.objects()

    return render_template("judge_portal/index.html", user = user, inqueries = inqueries)

@app.route("/generate-judge-key")
def generateJudgeKey():
    if not session.get("logged_in"):
        abort(404)

    user = User.objects.get(alias = session.get("alias"))

    if not user.isJudge:
        abort(404)
    key = urandom(1000).encode("base_64").replace("=","")
    user.judgeKey = sha224(key).hexdigest()
    user.save()
    return render_template("judge_portal/judgekey.html", key = key)

@app.route("/giveJudgement/<user>", methods=('GET', 'POST'))
def gJudgement(user=None):
    judge = Judge()
    if judge.validate_on_submit():
        print(form.state)
    try:
        user=User.objects(alias=user)[0]
        inquery = Inquery.objects(user=user)[0]
        return render_template("judge_portal/incident.html", user=user.alias, judge=judge)
    except IndexError:
        abort(400)
