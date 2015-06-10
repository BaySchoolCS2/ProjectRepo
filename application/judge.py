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
    print(key)
    user.judgeKey = sha224(key).hexdigest()
    user.save()
    return render_template("judge_portal/judgekey.html", key = key)

@app.route("/giveJudgement/<user>", methods=('GET', 'POST'))
def gJudgement(user=None):
    judge = Judge()
    try:
        juser = User.objects(alias = session.get("alias"))[0]
    except:
        print('not logged in')
        abort(401)
    if judge.validate_on_submit():
        print type(str(juser.judgeKey))
        print type(str(sha224(judge.jKey.data).hexdigest()))
        if juser.hasJudgeKey and str(juser.judgeKey)  == str(sha224(judge.jKey.data).hexdigest()):
            print(judge.state.data)
            try:
                inquery = Inquery.objects(user=user)[0]
            except IndexError:
                abort(400)
            if judge.state == "True":
                inquery.vote += 1
            else:
                inquery.vote -= 1
            print vote
        else:
            print('auth err')
            print(juser.judgeKey == judge.jKey)
            print(str(juser.judgeKey))
            print()
            print(str(sha224(judge.jKey.data).hexdigest()))
            print()
            print(judge.jKey.data)
            abort(401)
    try:
        user=User.objects(alias=user)[0]
        inquery = Inquery.objects(user=user)[0]
        return render_template("judge_portal/incident.html", user=user.alias, judge=judge)
    except IndexError:
        abort(400)
