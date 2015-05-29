from flask.ext.wtf import Form, html5
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Required
from wtforms.widgets import TextArea
from wtforms_components import ColorField

class LoginForm(Form):
    '''
        WTF-Forms for login, email is a string field,
        password is a password field, both are validated
        so that the data must be thier otherwise the form fails
    '''
    email = StringField('email', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])

class SignupForm(Form):
    '''
        Signup form for signing up
        email is a string field, and is only required to check if data is there
        alias is a string field, this acts as the username
        password is a password field meaning that the characters will be obfuscated
        password2 is compared to password in login.py
    '''
    email = html5.EmailField('email', validators = [DataRequired()])
    alias = StringField('alias', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    password2 = PasswordField('password (again)', validators = [DataRequired()])

class NewPost(Form):
    '''
        aparently i cant english
    '''
    title = StringField('title', validators = [DataRequired()])
    body = StringField('body', widget=TextArea(), validators=[DataRequired()])

class NewComment(Form):
    content = StringField('Your Comment', widget=TextArea())

class ChangePassword(Form):

    password = PasswordField('Password', validators = [DataRequired()])
    newPassword = PasswordField('New Password', validators = [DataRequired()])
    newPassword2 = PasswordField('Verify New Password', validators = [DataRequired()])

class ChangeColor(Form):
    color = ColorField('Color', validators = [DataRequired()])

class ForgotPassword(Form):
    email = StringField('Email', validators = [DataRequired()])
