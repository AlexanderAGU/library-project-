from colorama import Fore, init
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
            print(Fore.GREEN + f"You borrowed '{book.title}' by {book.author}")
        else:
            raise BookNotAvailableError("This book is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available_copies += 1
            self.borrowed_books.remove(book)
            print(Fore.GREEN + f"You returned '{book.title}' by {book.author}")
        else:
            raise BookNotAvailableError("This member did not borrow this book")      

    def check_book(self):
        if not self.borrowed_books:
            print(Fore.YELLOW + "You have no books in your list.")
            return

        print(Fore.CYAN + "Your borrowed books:")
        for book in self.borrowed_books:
            print(f"- {book.title} by {book.author}")


print("Member.py LOADED") 