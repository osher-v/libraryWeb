from flask import Flask, render_template, request, redirect, url_for, flash
from database import db
from data_models import Author, Book
import datetime
import requests
import os

app = Flask(__name__)
app.secret_key = 'vaza'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'library.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


def get_cover_image_url(isbn):
    url = f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form.get('birth_date')
        date_of_death = request.form.get('date_of_death')

        birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date() if birth_date else None
        date_of_death = datetime.datetime.strptime(date_of_death, '%Y-%m-%d').date() if date_of_death else None

        new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()
        flash('Author added successfully!')
        return redirect(url_for('add_author'))
    return render_template('add_author.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        isbn = request.form['isbn']
        publication_year = request.form['publication_year']
        author_id = request.form['author_id']

        cover_image_url = get_cover_image_url(isbn)

        new_book = Book(title=title, isbn=isbn, publication_year=publication_year, cover_image_url=cover_image_url,
                        author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!')
        return redirect(url_for('add_book'))

    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)


@app.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    books = Book.query.filter(Book.title.like('%{}%'.format(query))).all()
    return render_template('home.html', books=books)

@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    author_id = book.author_id
    db.session.delete(book)
    if not Book.query.filter_by(author_id=author_id).first():
        author = Author.query.get_or_404(author_id)
        db.session.delete(author)
    db.session.commit()
    flash('Book deleted successfully!')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
