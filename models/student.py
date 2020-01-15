from app import db

from models.parent import Parent
from models.school import School

class Student(db.Model, Parent):
    """ Student table definition """

    _tablename_ = "student"

    # fields of the Student table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)
    aggregate = db.Column(db.Integer, nullable=False)
    first_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    second_choice = db.Column("second_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    third_choice = db.Column("third_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)        
    fourth_choice = db.Column("fourth_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    is_assigned = db.Column("is_assigned", db.Integer, default=0)

    def __init__(self, name, aggregate, first_choice, second_choice, third_choice, fourth_choice):
        """ initialize with name and aggregate """
        self.name = name
        self.aggregate = aggregate

        self.first_choice = first_choice
        self.second_choice = second_choice
        self.third_choice = third_choice
        self.fourth_choice = fourth_choice

   
