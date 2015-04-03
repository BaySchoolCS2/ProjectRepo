from application import app

@app.route("/login", methods=["POST","GET"])
def login():
    return "i am a login page"

@app.route("/logout")
def logout():
    return "log out"
