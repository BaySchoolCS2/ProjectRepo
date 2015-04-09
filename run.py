#! venv/bin/python

from application import app
app.secret_key = "testing key"
app.run(debug=True)
