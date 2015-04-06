from flask_wtf import Form
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])

class SignupForm(Form):
    #FILL OUT LATER
    pass
