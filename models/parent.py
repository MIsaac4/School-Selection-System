from app import db

class Parent():
    """ Parent class to be inherited """

    def save(self):
        """  save a data to the database   """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """  delete data to the database   """
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """  update data to the database   """
        db.session.commit()




