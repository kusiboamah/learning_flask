from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Sign Up')
    
class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Sign in")