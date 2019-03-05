import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Notes
    # For configuration variables, take from environment variable or a default
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # Do not signal app every time a change is made to the DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
