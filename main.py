from Book import Book
from Member import Member
from Library import library
from colorama import Fore

print("--- Welcome To Aguirre's library ---")
print("How can I help you today?")

while True:
    
    print("1. Search by author")
    print("2. Search by title")
    print("3. See recommendations")
    print("4. Exit")
    try:
        choice = int(input("Please type 1-4"))
    except ValueError:
        print(Fore.RED + "Invalid choice. Please Select 1-4")
    
    if choice == 1:
        print(Fore.YELLOW + "You chose search by author")
    elif choice == 2:
        print(Fore.YELLOW + "You chose search by title")
    elif choice == 3:
        print(Fore.YELLOW + "You chose to see recommendations")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print(Fore.RED + "Invalid choice. Please select between 1-4")
        
        

    


      