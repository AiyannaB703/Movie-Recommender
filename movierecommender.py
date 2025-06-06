from flask import Flask, render_template, request, redirect, url_for
from app import create_app, db
from app.models.movie import Movie
from flask_login import login_user, logout_user, current_user
from app.models.user import User
from flask_login import login_user
app = create_app() 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movies')
def display_movies():
    movies = Movie.display_all()
    return render_template('movies.html', movies=movies)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('index.html'))
    if request.method == "POST":
            user = User.query.filter_by(username=request.form.get("username")).first()        
            if user.password == request.form.get('password'):
                return redirect(url_for('index.html'))
    return render_template('login.html')

@app.route('/create_account', methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        user = User(username=request.form.get('username'),
                    password=request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login_page"))
    return render_template('createaccount.html')
if __name__ == '__main__':
    app.run(debug=True)
