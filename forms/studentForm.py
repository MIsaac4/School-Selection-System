from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class RegisterStudentForm(FlaskForm):
    studentName = StringField('Name', validators=['DataRequired()'])
    aggregate = IntegerField('Aggregate', validators=['DataRequired()'])
    submit = SubmitField('Register')
