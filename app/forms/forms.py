# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UsernameForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    submit = SubmitField('Sprawdź')
