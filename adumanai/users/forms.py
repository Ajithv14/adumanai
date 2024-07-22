from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from adumanai import mongo

from flask_login import current_user
from adumanai.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    name = StringField('User Name',validators=[DataRequired() ])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm',message="Passwords must match")])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register User')

    def validate_email(self, email):
        if mongo.db.users.find_one({'email': email.data}):
            raise ValidationError('Email is already regiestered')