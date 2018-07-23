from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo, Email

class RegistrationForm(Form):
    username = StringField('Username', [Length(min=4, max=20)])
    email = StringField('Email Adress', [Email(), DataRequired()])
    password = PasswordField('New Password', [DataRequired(),
    EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
