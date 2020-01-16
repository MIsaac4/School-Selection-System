from flask import Blueprint, render_template, request, flash, redirect
from forms import *
from models.student import Student
from models.school import School

# Index blueprint
index_bp = Blueprint("user", __name__)

@index_bp.route("/", methods=['GET', 'POST'])
@index_bp.route("/home", methods=['GET', 'POST'])
def home():
    schools = School.query.all()
    student=[]
    students = Student.query.all()
    unassigned = Student.query.filter_by(assigned=0).all()
    school = None
    form = GetSchoolForm()
    if form.is_submitted():
        school = School.query.filter_by(id=form.schoolId.data).first()
        if not school:
            flash('School Doesnt Exist', 'error')
        student = Student.query.filter_by(assigned=school.id).all()
        return render_template("home.html", schools=schools, studentNo=len(students), unassigned=len(unassigned), schoolNo=len(schools), form=form, school=school, students= student, stno=len(student))
    return render_template("home.html", schools=schools, studentNo=len(students), unassigned=len(unassigned), schoolNo=len(schools), form=form, school=school, students= student, stno=len(student))

@index_bp.route("/register/student", methods=['GET', 'POST'])
def registerStudent():
    form = RegisterStudentForm()
    if form.is_submitted():
        student = Student(name=form.studentName.data, aggregate=form.aggregate.data, first_choice=form.first_choice.data, second_choice=form.second_choice.data, third_choice=form.third_choice.data, fourth_choice=form.fourth_choice.data)
        if contains(str(form.studentName.data), Student):
            flash('Student Exists', 'error')
        else:
            student.save()
            flash('Student Registered!', 'success')
    return render_template('studentpage.html', form=form, schools=getSchools())


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
    return render_template('schoolpage.html', form=form, schools=getSchools())

@index_bp.route("/show/students", methods=['GET', 'POST'])
def showStudentsInSchool():
    school = School.query.filter_by(id=2).first()
    students = Student.query.filter_by(assigned=school.id).all()
    stu = Student.query.filter_by(assigned=0).all()
    return render_template('home.html', school=school, students= students, stno=len(students), unassigned= len(stu))



# Checking if name exists
def contains(new_name, model):
    obj = model.query.filter_by(name=new_name).first()
    if obj:
        return True
    return False


# Get all schools
def getSchools():
    schools =School.query.all()
    return schools



def sortedStudents():
    student = Student.query.order_by(Student.aggregate).all()
    return student

def getStudentsInSchool(id):
    students = Student.query.filter_by(assigned=id).all()
    return len(students)

@index_bp.route("/first")
def assignfirstchoice():
# btn 4 - 8
    students = Student.query.filter(Student.aggregate<9).all()
    arr=[]
    for student in students:
        student.assigned = student.first_choice
        student.update()
        arr.append(student.assigned)

    return str(arr)

def schoolIsFull(schoolId):
    # check students availabe in school
    school = School.query.filter_by(id=schoolId).first()
    students = Student.query.filter_by(assigned=school.id).all()
    num = len(students)

    if(num<school.number_of_students):
        return True
    else:
        return False

# for cut off points
def jambia(aggregate, schoolId):
    school = School.query.filter_by(id=schoolId).first()
    if(school.cut_off_points >= aggregate):
        return True
    return False

@index_bp.route("/delete")
def unassignAllStudents():
    students = Student.query.all()
    for student in students:
        student.assigned = 0
        student.update()
    return redirect("/")


    
@index_bp.route("/assign")
def checkStudentAssigned():
    # assign bwats
    asas = assignfirstchoice()
    # check if student has been assigned
    students = sortedStudents()
    arr = []
    for student in students:
        if(student.assigned == 0):
            # 1st choice
            if(schoolIsFull(student.first_choice) and jambia(student.aggregate, student.first_choice)):
                student.assigned = student.first_choice
                student.update()
                
            elif(schoolIsFull(student.second_choice) and jambia(student.aggregate, student.second_choice)):
                student.assigned = student.second_choice
                student.update()
                
            elif(schoolIsFull(student.third_choice) and jambia(student.aggregate, student.third_choice)):
                student.assigned = student.third_choice
                student.update()
                
            elif(schoolIsFull(student.fourth_choice) and jambia(student.aggregate, student.fourth_choice)):
                student.assigned = student.fourth_choice
                student.update()
                
    return redirect("/")
