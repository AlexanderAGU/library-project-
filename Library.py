import json
import random
from Member import Member
from Book import Book
from colorama import Fore, init
init(autoreset=True)

COLLECTION_FILE = "collection.json"

class Library:

    def __init__(self):
        self.books = []
        self.load_books()
    
    
    def load_books(self):    
        with open(COLLECTION_FILE, "r") as file:
            data = json.load(file)

            for book_dict in data:
                book = Book(
                    book_check="json",
                    book_id=0,
                    title=book_dict["title"],
                    author=book_dict["author"],
                    pages=book_dict["pages"],
                    genre=book_dict["genre"],
                    available_copies=book_dict["total_copies"],
                    total_copies=book_dict["total_copies"]
                )
                self.books.append(book)

    def save_book(self):
        data = []
        for book in self.books:
            data.append({
                "title": book.title,
                "author": book.author,
                "pages": book.pages,
                "total_copies": book.total_copies,
                "available_copies": book.available_copies
            })
        
        with open(COLLECTION_FILE,"w") as file:
            json.dump(data, file, indent=4)

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