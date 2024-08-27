from app import app
from database import db
from data_models import Book, Author

with app.app_context():
    db.create_all()
