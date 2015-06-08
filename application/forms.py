from flask.ext.wtf import Form, html5
from wtforms import StringField, PasswordField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Required
from wtforms.widgets import TextArea

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
    email = html5.EmailField('Email', validators = [DataRequired()])
    alias = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Password (again)', validators = [DataRequired()])

class NewPost(Form):
    '''
        aparently i cant english
    '''
    title = StringField('Title', validators = [DataRequired()])
    body = StringField('Body', widget=TextArea(), validators=[DataRequired()])

class NewComment(Form):
    content = StringField('Your Comment', widget=TextArea())

class ChangePassword(Form):

    password = PasswordField('Password', validators = [DataRequired()])
    newPassword = PasswordField('New Password', validators = [DataRequired()])
    newPassword2 = PasswordField('Verify New Password', validators = [DataRequired()])

class ChangeColor(Form):
    color = StringField('Color', validators = [DataRequired()])

class ForgotPassword(Form):
    email = StringField('Email', validators = [DataRequired()])

class Judge(Form):
    jKey = StringField(widget=TextArea(), validators=[DataRequired()])
    state = HiddenField(validators=[DataRequired()])
