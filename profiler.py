#! venv/bin/python

from werkzeug.contrib.profiler import ProfilerMiddleware
from application import app


app.secret_key = "ProfilingKey"
app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
app.run(debug = True)
