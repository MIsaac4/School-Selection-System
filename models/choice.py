from app import db
from models.school import School
from models.student import Student

class Choice(db.Model):
    """ Students Choice table definition """

    _tablename_ = "choice"

    # fields of the Student table
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey(Student.id, ondelete='CASCADE'), nullable=False)
    school_id = db.Column("school_id", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    is_assigned = db.Column("is_assigned", db.Boolean, default=False)

    def __init__(self, student_id, school_id, is_assigned):
        """ initialize with name, member and namespace """  
        self.student_id = student_id
        self.school_id = school_id
        self.is_assigned = is_assigned


