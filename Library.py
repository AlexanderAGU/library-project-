import json
from Book import Book
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

    
    
    