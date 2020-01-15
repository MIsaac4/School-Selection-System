from app import db

from models.school import School
from models.student import Student
from models.parent import Parent

class Choice(db.Model, Parent):
    """ Students Choice table definition """

    _tablename_ = "choice"

    # fields of the Student table
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey(Student.id, ondelete='CASCADE'), nullable=False)
    first_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    second_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    third_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)        
    fourth_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    is_assigned = db.Column("is_assigned", db.Integer, default=0)

    def __init__(self, student_id, first_choice, second_choice, third_choice, fourth_choice):
        """ initialize """  
        self.student_id = student_id
        self.first_choice = first_choice
        self.second_choice = second_choice
        self.third_choice = third_choice
        self.fourth_choice = fourth_choice

    