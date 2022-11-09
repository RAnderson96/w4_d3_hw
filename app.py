from flask import Flask, render_template
from repositories import author_repository, book_repository
from flask import Flask, render_template, request, redirect
from models.author import Author
from models.book import Book


app = Flask(__name__)

from controllers.book_controller import books_blueprint

app.register_blueprint(books_blueprint)



@app.route('/')
def home():
    author = author_repository.select_all()
    return render_template('index.html', all_authors = author)



if __name__ == '__main__':
    app.run(debug=True)