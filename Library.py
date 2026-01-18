import json
import random
from Member import Member
from Book import Book
from colorama import Fore, init

init(autoreset=True)

class Library:

    def __init__(self):
        self.books = []

        with open("collection.json", "r") as file:
            collection = json.load(file)

            for book_dict in collection:
                book_obj = Book(
                    book_check="json",
                    book_id=0,
                    title=book_dict["title"],
                    author=book_dict["author"],
                    pages=book_dict["pages"],
                    genre=book_dict["genre"],
                    available_copies=book_dict["total_copies"],
                    total_copies=book_dict["total_copies"]
                )
                self.books.append(book_obj)

    def author_search(self, search_text, member):
        search_text_lower = search_text.lower()
        matches = [book for book in self.books if search_text_lower in book.title.lower()]

        if not matches:
            print(Fore.RED + "No book was found.")
            return

        for book in matches:
            print(Fore.YELLOW + "Did you mean this book?")
            print(book.info_display())

            response = input("(y/n): ").strip().lower()
            if response == "y":
                print(Fore.GREEN + "Book selected.")
                self._ask_to_borrow(book, member)
                return
            
        print(Fore.RED + "No matching book confirmed. Please try again.")

    def title_search(self, search_text, member):
        search_text_lower = search_text.lower()
        matches = [book for book in self.books if search_text_lower in book.title.lower()]

        if not matches:
            print(Fore.RED + "Book was not found.")
            return

        for book in matches:
            print(Fore.YELLOW + "Did you mean this book?")
            print(book.info_display())

            response = input("(y/n): ").strip().lower()
            if response == "y":
                print(Fore.GREEN + "Book selected.")
                self._ask_to_borrow(book, member)
                return

        print(Fore.RED + "No matching book confirmed. Please try again.")

    def _ask_to_borrow(self, book, member):
        borrow_response = input("Would you like to borrow this book? (y/n) ").strip().lower()
        if borrow_response == "y":
            try:
                member.borrow_book(book)
            except Exception as e:
                print(Fore.RED + str(e))
                return
        
    def recommendations(self):
        if not self.books:
            print(Fore.RED + "No books available for recommendations.")
            return

        count = min(3, len(self.books))
        recommended_books = random.sample(self.books, count)

        print(Fore.CYAN + "📚 Recommended Books:")
        for book in recommended_books:
            print(Fore.YELLOW + book.info_display())