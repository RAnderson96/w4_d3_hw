from repositories import author_repository, book_repository
from flask import Flask, render_template, request, redirect
from models.author import Author
from models.book import Book


# Import Blueprint class from flask
from flask import Blueprint

# Create a new instance of Blueprint called "books"
books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    book = book_repository.select_all()
    return render_template("books/index.html", all_books=book)




@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')



@books_blueprint.route("/books/new")
def new_book():
    author = author_repository.select_all()
    return render_template("/books/new.html", all_authors = author)

# CREATE
# POST '/tasks'

@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    
    author = author_repository.select(author_id)
    book = Book(title, author, genre)
    book_repository.save(book)
    return redirect('/books')


@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book=book_repository.select(id)
    author = author_repository.select_all()
    return render_template('books/edit.html', book = book, all_authors = author)


# UPDATE
# PUT '/tasks/<id>'

@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book():
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    
    author = author_repository.select(author_id)
    book = Book(title, author, genre)
    book_repository.update(book)
    return redirect('/books')
 