from app import db

from models.parent import Parent

class Student(db.Model, Parent):
    """ Student table definition """

    _tablename_ = "student"

    # fields of the Student table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    aggregate = db.Column(db.Integer, nullable=False, default="")

    def __init__(self, name, aggregate):
        """ initialize with name and aggregate """
        self.name = name
        self.aggregate = aggregate
