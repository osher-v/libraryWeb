# Library Management System

This is a Flask-based Library Management System. The application allows users to manage authors and books, including adding, deleting, and searching for books. The app also displays book covers using the Open Library Covers API.

## Features

- **Add Author:** Add new authors with their name, birth date, and date of death.
- **Add Book:** Add new books with their title, ISBN, publication year, and associated author.
- **Search Books:** Search for books by their title.
- **Delete Books:** Delete books from the library. If an author has no books left, the author will also be deleted.
- **View Books:** View all books in a grid format, including their cover images.

## Technologies Used

- **Flask:** Web framework for Python.
- **SQLAlchemy:** ORM for interacting with the SQLite database.
- **Jinja2:** Templating engine for rendering HTML.
- **Open Library Covers API:** Used to fetch book cover images based on ISBN.
- **SQLite:** Database for storing authors and books.

## Installation

### 1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>
