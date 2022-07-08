from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class InfoForm(FlaskForm):
    breed = StringField('What type of breed are you?')
    submit = SubmitField('')