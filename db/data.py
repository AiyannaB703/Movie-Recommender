import csv
import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
from app.models.movie import db, Movie

app = create_app()
def load_csv(csv_file):
    with app.app_context():
        with open(csv_file, newline='', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                movie = Movie(
                    id=row['id'],
                    name=row['name'],
                    category=row['category'],
                    description=row['description']
                )
                db.session.add(movie)
            db.session.commit()
if __name__ == '__main__':
    load_csv('movies.csv')