from Book import Book
from Member import Member
from Library import Library
from colorama import Fore
from colorama import init
init(autoreset=True)
library = Library()

print("--- Welcome To Aguirre's library ---")
print("How can I help you today?")

while True:
    
    print("1. Search by author")
    print("2. Search by title")
    print("3. See recommendations")
    print("4. Exit")
    try:
        choice = int(input("Please type 1-4: "))
    except ValueError:
        print(Fore.RED + "Invalid choice. Please Select 1-4")
    
    if choice == 1:
        user_input = str(input("Type the author's name: "))
        library.author_search(user_input)
    elif choice == 2:
       user_input = str(input("type the title of the book: "))
       library.title_search(user_input)
    elif choice == 3:
        print(Fore.YELLOW + "You chose to see recommendations")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print(Fore.RED + "Invalid choice. Please select between 1-4")
        
        

    


      