from application import app
import os

app.secret_key = os.urandom(16).encode("base_64")
