from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_wtf.file import FileAllowed

from adumanai import mongo

class CakeForm(FlaskForm):
    name = StringField('Name of the cake', validators=[DataRequired()])
    description = TextAreaField('Give some description', validators=[DataRequired()])
    picture = FileField('Add a picture', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    price = StringField('Price',validators=[DataRequired()])
    submit = SubmitField('Upload')
    
    def validate_name(self, name):
        if mongo.db.cakes.find_one({'name': name.data}):
            raise ValidationError('Name is already regiestered')