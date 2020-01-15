from flask import Blueprint, render_template, request, flash
from forms import *
from models.student import Student
from models.school import School

# Index blueprint
index_bp = Blueprint("user", __name__)

@index_bp.route("/")
def index():
    return render_template("index.html")

@index_bp.route("/register/student", methods=['GET', 'POST'])
def registerStudent():
    form = RegisterStudentForm()
    if form.is_submitted():
        student = Student(name=form.studentName.data, aggregate=form.aggregate.data)
        if contains(str(form.studentName.data), Student):
            flash('Student Exists', 'error')
        else:
            student.save()
            flash('Student Registered!', 'success')
    return render_template('studentpage.html', form=form)


@index_bp.route("/register/school", methods=['GET', 'POST'])
def registerSchool():
    form = RegisterSchoolForm()
    if form.is_submitted():
        school = School(name=form.schoolName.data, cut_off_points=form.cutOffPoints.data, number_of_students=form.studentNumber.data)
        if contains(str(form.schoolName.data), School):
            flash('School Exists', 'error')
        else:
            school.save()
            flash('School Registered!', 'success')
    return render_template('schoolpage.html', form=form)


# Checking if name exists
def contains(new_name, model):
    obj = model.query.filter_by(name=new_name).first()
    if obj:
        return True
    return False
