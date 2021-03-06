''' My models.py module defines the structure of the database. Data stored in 
the database will be represented by a collection of classes, usually called 
database models. The ORM layer within SQLAlchemy does the translations required 
to map objects created from these classes into rows in the proper database tables.
'''

from datetime import datetime
from app import db

# Post class
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), default='johncollins')
    title = db.Column(db.String(250))
    body = db.Column(db.String(25000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.body)

# Contact class, for contact form on me page
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    message = db.Column(db.String(640))

    def __repr__(self):
        return '<Contact {}'.format(self.message)






