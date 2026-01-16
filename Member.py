from colorama import Fore
from colorama import init
init(autoreset=True)

class BookNotAvailableError(Exception):
    pass


class Member:
    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            book.available_copies -= 1
            self.borrowed_books.append(book)
        else:
            raise BookNotAvailableError("This book is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available_copies += 1
            self.borrowed_books.remove(book)
        else:
            raise BookNotAvailableError("This member did not borrow this book")      

      
