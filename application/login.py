from application import app

@app.route("/login", methods=["POST","GET"])
def login():
    
