from app import db
from flask import jsonify

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=False, nullable=False)


    def to_dict(self):
        return {
            'id':self.id,
            'usernname':self.username,
            'password':self.password,
            'email':self.email
        }
    
    @staticmethod
    def get_by_auth(username, password):
        user = db.session.execute(db.select(User).where(username = username))
        return User.query.filter_by(username=username, password=password).first()

    