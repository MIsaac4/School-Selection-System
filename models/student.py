from app import db

class Student(db.Model, ToDict):
    """ Student table definition """

    _tablename_ = "student"