class Book:

    def __init__(self, book_check: str, book_id: int, title: str, author: str, pages: int, genre: str, available_copies: int, total_copies: int ):
        self.book_check = book_check    
        self.book_id = book_id      
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.available_copies = available_copies 
        self.total_copies = total_copies
    
    def info_display(self):
        return f"{self.title} by {self.author} ({self.available_copies}/{self.total_copies} available)"
            
    def is_available(self):
        if self.available_copies > 0:
            return f"This book is still available for checkout"