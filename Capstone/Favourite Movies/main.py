from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import urllib.parse
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Bootstrap5(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add')


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MjBjNDNkOGE2MmZhYjE3YTVmZTllYWQ0YTQ5YTE1YiIsIm5iZiI6MTc1NDk4NjcwMC45MzI5OTk4LCJzdWIiOiI2ODlhZjhjYzdmMjRkYjljMDJiNzA2YWQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.U0Ba4E6VZZxUYQJPk6GD3AXysAVeuVJgmyG-MbWb_HQ"
}

search_url1 = "https://api.themoviedb.org/3/search/movie?query="
search_url2 = "&include_adult=true&language=en-US&page=1"

detail_url = "https://api.themoviedb.org/3/movie/"
detail_url2 = "?language=en-US"

base_img_url = "https://image.tmdb.org/t/p/w500"

# CREATE DB
with app.app_context():
    db.create_all()

class EditForm(FlaskForm):
    rating = StringField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


@app.route('/')
def home():
    movie_list = Movie.query.all()
    movie_list_ordered = Movie.query.order_by(Movie.rating.desc()).all()
    return render_template('index.html', movies=movie_list_ordered)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')  # DB ID, not TMDB ID
    if not movie_id:
        return redirect(url_for('home'))

    movie_to_update = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    # Pre-fill form if editing existing movie
    form.rating.data = movie_to_update.rating if movie_to_update.rating is not None else ""
    form.review.data = movie_to_update.review if movie_to_update.review else ""

    return render_template('edit.html', form=form, movie=movie_to_update)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        print(f"{form.title.data}")
        response = requests.get(search_url1 + urllib.parse.quote(form.title.data) + search_url2, headers=headers)
        # movie_data = json.loads(response.text)
        movie_data = response.json()
        print(response.text)
        return render_template('select.html', movies=movie_data['results'])
    return render_template('add.html', form=form)


@app.route('/find')
def find():
    tmdb_id = request.args.get('id')  # TMDB movie ID from 'select.html'
    if not tmdb_id:
        return redirect(url_for('home'))  # No ID? Just go home.

    # Fetch movie details from TMDB
    response = requests.get(
        f"{detail_url}{tmdb_id}{detail_url2}",
        headers=headers
    )
    if response.status_code != 200:
        return f"Error fetching movie details: {response.text}", 500

    movie_data = response.json()

    # Create and save new Movie entry
    new_movie = Movie(
        title=movie_data['title'],
        year=datetime.strptime(movie_data['release_date'], "%Y-%m-%d").year,
        description=movie_data['overview'],
        img_url=base_img_url + movie_data['poster_path']
    )
    db.session.add(new_movie)
    db.session.commit()

    # Redirect to edit page with the DB's own primary key
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
