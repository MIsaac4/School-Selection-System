from app import db

class Student(db.Model, ToDict):
    """ Student table definition """

    _tablename_ = "student"

    # fields of the Student table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    aggregate = db.Column(db.Int(256), unique=True, nullable=False, default="")

    def __init__(self, name, aggregate):
        """ initialize with name and aggregate """
        self.name = name
        self.aggregate = aggregate
        