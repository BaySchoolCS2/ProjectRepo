#! venv/bin/python

from application import app

app.secret_key = "testing key"

app.run(debug=True, host="0.0.0.0")
