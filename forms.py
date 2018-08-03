from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo, Email


class RegistrationForm(Form):
    username = StringField('Username', [Length(min=4, max=30)])
    email = StringField('Email Address', [Email(), DataRequired()])
    password = PasswordField('Password', [DataRequired(),
    EqualTo('confirm', message='Passwords must match'), Length(min=2, max=60)])
    confirm = PasswordField('Confirm Password')
