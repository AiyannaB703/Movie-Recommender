import csv
import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
from app.models.movie import db, Movie
from app.models.user import User

app = create_app()
def load_movies(csv_file):
    with app.app_context():
        db.session.query(Movie).delete()
        db.session.commit()
        with open(csv_file, newline='', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
               # print(row)
                movie = Movie(
                    id=row['id'],
                    name=row['name'],
                    category=row['category'],
                    description=row['description']
                )
                db.session.add(movie)
            db.session.commit()
    
def load_users(csv_file):
        with app.app_context():
            db.session.query(User).delete()
            db.session.commit()
            with open(csv_file, newline='', encoding='utf-8') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    user = User(
                    id=row['id'],
                    username=row['username'],
                    password=row['password'],
                    email=row['email']
                    )
                    db.session.add(user)
                db.session.commit()
if __name__ == '__main__':
    load_movies('movies.csv')
    #print(Movie.display_all())
    load_users('users.csv')