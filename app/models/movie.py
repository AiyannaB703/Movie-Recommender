from app import db
from flask import jsonify
#from flask_sqlalchemy import SQLAlchemy
#from flask import Flask, jsonify
#app = Flask(__name__)
#app.debug = True

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
#db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    category = db.Column(db.String(20), unique=False, nullable=False)
    description = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'category':self.category,
            'description':self.description
        }

    @staticmethod
    def display_all():
        movies = Movie.query.all()
        return [movie.to_dict() for movie in movies]

