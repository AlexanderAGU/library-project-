from Book import Book
from Member import Member
from Verifcation import User
from Library import Library
from colorama import Fore
from colorama import init
init(autoreset=True)
import json, os
library = Library()
FILE = "user.json"

if not os.path.exists(FILE):
    with open("user.json","w") as file:
        json.dump([],file,indent=4)

with open(FILE, "r") as file:
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        users = []

print("--- Welcome To Aguirre's library ---")
check = input("Do you have an account? (y/n): ").strip().lower()

if check == "y":
    login = input("What is your email? ").lower()
    password = input("What is your password? ")

    user = next((u for u in users if u["login"] == login), None)

    if user is None:
        print(Fore.RED + "❌ Account not found.")
        exit()

    if user["password_hash"] != password:
        print(Fore.RED + "❌ Incorrect password.")
        exit()

    print(Fore.GREEN + "✅ Login successful!")

elif check == "n":
    login = input("Please type a new email: ").lower()
    password = input("Please type a new password: ")

    new_user = User(login, password)

    users.append({
        "login": new_user.login,
        "password_hash": new_user.password_hash
    })

    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)

    print(Fore.GREEN + "✅ Account created successfully!")

else:
    print("invalid")


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
        library.recommendations() 
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print(Fore.RED + "Invalid choice. Please select between 1-4")
        
        

    


      