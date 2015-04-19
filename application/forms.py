from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = StringField('email', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])

class SignupForm(Form):
    email = StringField('email', validators = [DataRequired()])
    alias = StringField('alias', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    password2 = PasswordField('password (again)', validators = [DataRequired()])
