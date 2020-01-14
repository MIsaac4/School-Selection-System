from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, app

# import models
from models.school import School
from models.student import Student
from models.choice import Choice

# register app and db with migration class
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()