import os


class Development():
    """ development config """

    DEBUG = (True,)
    SQLALCHEMY_DATABASE_URI = "postgresql:///school_selection_db"


class Testing():
    """ test environment config """

    TESTING = (True,)
    DEBUG = (True,)
    # use a separate db

    SQLALCHEMY_DATABASE_URI = "postgresql:///school_selection_testing"




app_config = {"development": Development, "testing": Testing}