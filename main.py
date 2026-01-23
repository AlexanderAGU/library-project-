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

# Login/Password Secuitry UI/Logic
if not os.path.exists(FILE):
    with open("user.json","w") as file:
        json.dump([],file,indent=4)

with open(FILE, "r") as file:
    try:
        users = json.load(file)
    except:
        users = []

print("--- Welcome To Aguirre's library ---")
check = input("Do you have a registered account to Aguirre's library? (y/n): ").strip().lower()

if check == "y":
    login = input("What is your email? ").lower()
    password = input("What is your password? ")

    user = next((u for u in users if u["login"] == login), None)

    if user is None:
        print(Fore.RED + "❌ Account not found.")
        exit()

    if not User.verify_password(password, user["password_hash"]):
        print(Fore.RED + "❌ Incorrect password.")
        exit()

    print(Fore.GREEN + "✅ Login successful!")
    member = Member(name=login, member_id=users.index(user))

elif check == "n":
    new_login = input("Please type a new email: ").lower()
    if any(u["login"] == new_login for u in users):
        print(Fore.RED + "❌ This email is already registered. Please log in instead.")
        exit()
    new_password = input("Please type a new password: ")
    
    new_user = User(new_login, new_password)

    users.append({
        "login": new_user.login,
        "password_hash": new_user.password_hash
    })

    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)

    print(Fore.GREEN + "✅ Account created successfully!")

else:
    print("invalid")
    exit()

print("How can I help you today?")

while True:
    
    print("1. Search by author")
    print("2. Search by title")
    print("3. See recommendations")
    print("4. Check Borrowed list")
    print("5. Exit")
    
    try:
        choice = int(input("Please type 1-5: "))
    except ValueError:
        print(Fore.RED + "Invalid choice. Please Select 1-5")
    
    if choice == 1:
        user_input = str(input("Type the author's name: "))
        library.author_search(user_input, member)
    elif choice == 2:
       user_input = str(input("type the title of the book: "))
       library.title_search(user_input, member)
    elif choice == 3:
        library.recommendations() 
    elif choice == 4:
        member.check_book()
    elif choice == 5:
        exit()
    else:
        print(Fore.RED + "Invalid choice. Please select between 1-5")
        
        

    


      