import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("J. R. R. Tolkien")
author_repository.save(author1)
author2 = Author("Victor Hugo")
author_repository.save(author2)

author_repository.select_all()

book_1 = Book("The Fellowship of the Ring", author1, "Fantasy")
book_repository.save(book_1)

book_2 = Book("Les Miserable", author2, "Fantasy")
book_repository.save(book_2)

book_3 = Book("The Two Towers", author1, "Fantasy")
book_repository.save(book_3)

book_4 = Book("The Return of the King", author1, "Fantasy")
book_repository.save(book_4)

book_5 = Book("The Hobbit", author1, "Fantasy")
book_repository.save(book_5)



pdb.set_trace()
