from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class RegisterStudentForm(FlaskForm):
    studentName = StringField('Name')
    aggregate = IntegerField('Aggregate')
    submit = SubmitField('Register')
