from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class RegisterStudentForm(FlaskForm):
    studentName = StringField('Name', validators=['DataRequired()'])
    aggregate = IntegerField('Aggregate', validators=['DataRequired()'])
    submit = SubmitField('Register')

class RegisterSchoolForm(FlaskForm):
    schoolName = StringField('Name', validators=['DataRequired()'])
    cutOffPoints = IntegerField('Cut off Points', validators=['DataRequired()'])
    studentNumber = IntegerField('Number of Students', validators=['DataRequired()'])
    submit = SubmitField('Register')