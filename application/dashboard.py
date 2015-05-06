from application import app
from collections import Following, User
from flask import render_template, session, redirect, url_for

@app.route('/dashboard')
def dashboard():
    if session.get("logged_in"):
        user = User.objects(alias = session.get("alias"))
        Following.objects(user=user)

        {% extends 'header.html' %}
        {% block title %}Welcome{% endblock %}

        {% block body %}
        	{% if len(posts) > 0 %}
        		{% for post in posts %}
        			<div class="row npf">
        				<div class="col-md-10">
        					<a href="{{ url_for('post', uid=post.id) }}">{{ post.title }}</a>
        				</div>
        				<div class="col-md-2 by">
        					By <a href="{{ url_for('profile',  name=post.author.alias) }}">{{ post.author.alias }}</a>
        				</div>
        			</div>
        		{% endfor %}
        	{% else %}
        		<h2 class="npf"> No Posts Found :( </h2>
        	{% endif %}

        	{% endblock %}



        return str(Following.following)
    else:
        return redirect(url_for("index"))
