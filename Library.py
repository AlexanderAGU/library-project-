import json
from Book import Book
from colorama import Fore
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

    def author_search(self, search_text):
        search_text_lower = search_text.lower()
        found_match = False

        for book in self.books:
            author_lower = book.author.lower()

        if search_text_lower in author_lower:
            print(book.info_display())
            found_match = True

        if not found_match:
            print(Fore.RED + "No books found for that author.")
    
    def title_search(self,search_text):
        search_text_lower = search_text.lower()
        found_match = False
        
        for book in self.books:
            text_lower = book.text_lower()

        if search_text_lower in text_lower:
            print(book.info_display())
            found_match = False

        if not found_match:
            print(Fore.RED + "No books found for that title")
    
    
    