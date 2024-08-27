from app import app, get_cover_image_url
from database import db
from data_models import Author, Book
import datetime

def populate_db():
    # רשימת סופרים וספרים לדוגמה
    authors_books = [
        {
            "name": "J.K. Rowling",
            "birth_date": "1965-07-31",
            "date_of_death": None,
            "books": [
                {"title": "Harry Potter and the Sorcerer's Stone", "isbn": "9780747532699", "publication_year": 1997},
                {"title": "Harry Potter and the Chamber of Secrets", "isbn": "9780747538493", "publication_year": 1998},
                {"title": "Harry Potter and the Prisoner of Azkaban", "isbn": "9780747542155", "publication_year": 1999},
            ]
        },
        {
            "name": "George R.R. Martin",
            "birth_date": "1948-09-20",
            "date_of_death": None,
            "books": [
                {"title": "A Game of Thrones", "isbn": "9780553103540", "publication_year": 1996},
                {"title": "A Clash of Kings", "isbn": "9780553108033", "publication_year": 1998},
            ]
        },
        {
            "name": "J.R.R. Tolkien",
            "birth_date": "1892-01-03",
            "date_of_death": "1973-09-02",
            "books": [
                {"title": "The Hobbit", "isbn": "9780618260300", "publication_year": 1937},
                {"title": "The Lord of the Rings: The Fellowship of the Ring", "isbn": "9780618260263", "publication_year": 1954},
                {"title": "The Lord of the Rings: The Two Towers", "isbn": "9780618260270", "publication_year": 1954},
            ]
        },
        {
            "name": "Agatha Christie",
            "birth_date": "1890-09-15",
            "date_of_death": "1976-01-12",
            "books": [
                {"title": "Murder on the Orient Express", "isbn": "9780062073501", "publication_year": 1934},
                {"title": "The Murder of Roger Ackroyd", "isbn": "9780062073563", "publication_year": 1926},
            ]
        },
        {
            "name": "Stephen King",
            "birth_date": "1947-09-21",
            "date_of_death": None,
            "books": [
                {"title": "The Shining", "isbn": "9780307743657", "publication_year": 1977},
                {"title": "It", "isbn": "9781501142970", "publication_year": 1986},
            ]
        },
        {
            "name": "Isaac Asimov",
            "birth_date": "1920-01-02",
            "date_of_death": "1992-04-06",
            "books": [
                {"title": "Foundation", "isbn": "9780553293357", "publication_year": 1951},
                {"title": "I, Robot", "isbn": "9780553382563", "publication_year": 1950},
            ]
        },
        {
            "name": "Arthur C. Clarke",
            "birth_date": "1917-12-16",
            "date_of_death": "2008-03-19",
            "books": [
                {"title": "2001: A Space Odyssey", "isbn": "9780451452733", "publication_year": 1968},
                {"title": "Rendezvous with Rama", "isbn": "9781857987324", "publication_year": 1973},
            ]
        },
        {
            "name": "H.G. Wells",
            "birth_date": "1866-09-21",
            "date_of_death": "1946-08-13",
            "books": [
                {"title": "The War of the Worlds", "isbn": "9780141441030", "publication_year": 1898},
                {"title": "The Time Machine", "isbn": "9780141439976", "publication_year": 1895},
            ]
        },
        {
            "name": "Ernest Hemingway",
            "birth_date": "1899-07-21",
            "date_of_death": "1961-07-02",
            "books": [
                {"title": "The Old Man and the Sea", "isbn": "9780684830490", "publication_year": 1952},
                {"title": "A Farewell to Arms", "isbn": "9780684801469", "publication_year": 1929},
            ]
        },
        {
            "name": "F. Scott Fitzgerald",
            "birth_date": "1896-09-24",
            "date_of_death": "1940-12-21",
            "books": [
                {"title": "The Great Gatsby", "isbn": "9780743273565", "publication_year": 1925},
                {"title": "Tender Is the Night", "isbn": "9780684801544", "publication_year": 1934},
            ]
        }
    ]

    for author_data in authors_books:
        birth_date = datetime.datetime.strptime(author_data["birth_date"], '%Y-%m-%d').date()
        date_of_death = datetime.datetime.strptime(author_data["date_of_death"], '%Y-%m-%d').date() if author_data["date_of_death"] else None

        new_author = Author(name=author_data["name"], birth_date=birth_date, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.flush()  # שומר את ה-id של המחבר לפני הוספת הספרים

        for book_data in author_data["books"]:
            cover_image_url = get_cover_image_url(book_data["isbn"])  # הוסף את קריאת הפונקציה לכתובת תמונה
            new_book = Book(
                title=book_data["title"],
                isbn=book_data["isbn"],
                publication_year=book_data["publication_year"],
                cover_image_url=cover_image_url,  # הוסף את כתובת התמונה
                author_id=new_author.id
            )
            db.session.add(new_book)

    db.session.commit()
    print("Database populated successfully!")

if __name__ == '__main__':
    with app.app_context():
        populate_db()
