from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegisterStudent(FlaskForm):
    studentName = StringField('Name')
    aggregate = StringField('Aggregate')
    submit = SubmitField('Register')
    