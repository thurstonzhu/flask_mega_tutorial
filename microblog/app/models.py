from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # [C]
    nickname = db.Column(db.String(64), index=True, unique=True)

    # For a one-to-many relationship, usually define db.relationship on
    # the 'one' side

    # db.relationship()
    # * arg1    = model class for the 'many' relationship
    # * backref = name of field that points back to the 'one' object
    #           = in this case, post.author -> user
    # * lazy    = how the database query will be issued
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # Refer to model by its database table name
    # For db.ForeignKey in SQLAlchemy, use lowercase letters and
    # snake case for multi-word model names
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
