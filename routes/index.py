from flask import Blueprint, render_template, request, flash
from forms.studentForm import RegisterStudentForm
from models.student import Student

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
        student.save()
        flash('Student Registered!', 'success')
    return render_template('studentpage.html', form=form)
