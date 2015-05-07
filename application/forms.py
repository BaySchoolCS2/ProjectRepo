from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Required

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
    email = StringField('email', validators = [DataRequired()])
    alias = StringField('alias', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    password2 = PasswordField('password (again)', validators = [DataRequired()])

class NewPost(Form):
    '''
        aparently i cant english
    '''
    title = StringField('title', validators = [DataRequired()])
    body = TextAreaField()

class ChangePassword(Form):

    password = PasswordField('Password', validators = [DataRequired()])
    newPassword = PasswordField('New Password', validators = [DataRequired()])
    newPassword2 = PasswordField('Verify New Password', validators = [DataRequired()])
