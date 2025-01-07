from flask import Flask, render_template
from app import create_app
from app.models.movie import Movie

app = create_app() #Flask(__name__,  template_folder='app/templates', static_folder='app/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movies')
def display_movies():
    movies = Movie.display_all()
    return render_template('movies.html', movies=movies)
@app.route('/login')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
