from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class RegisterStudentForm(FlaskForm):
    studentName = StringField('Name', validators=['DataRequired()'])
    aggregate = IntegerField('Aggregate', validators=['DataRequired()'])
    first_choice = IntegerField('First Choice', validators=['DataRequired()'])
    second_choice = IntegerField('Second Choice', validators=['DataRequired()'])
    third_choice = IntegerField('Third Choice', validators=['DataRequired()'])
    fourth_choice = IntegerField('Fourth Choice', validators=['DataRequired()'])
    submit = SubmitField('Register')

class RegisterSchoolForm(FlaskForm):
    schoolName = StringField('Name', validators=['DataRequired()'])
    cutOffPoints = IntegerField('Cut off Points', validators=['DataRequired()'])
    studentNumber = IntegerField('Number of Students', validators=['DataRequired()'])
    submit = SubmitField('Register')

class GetSchoolForm(FlaskForm):
    schoolId = StringField('Enter Id of a school', validators=['DataRequired()'])
    submit = SubmitField('Submit')