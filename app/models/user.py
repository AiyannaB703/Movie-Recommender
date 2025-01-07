from app import db
from flask import jsonify

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.Integer, nullable=False)


    def to_dict(self):
        return {
            'id':self.id,
            'usernname':self.name,
            'password':self.category,
            'email':self.description
        }