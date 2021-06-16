import os
from searchBook import generalSearch

user_list =["Silpa", "Megan", "Bruna", "Sumaya"]

def clearScreen():
    os.system('cls')

def displayUserMenu():
    clearScreen()
    print(f"Welcome to the library {user_list[0]}, Menu options:")
    print("1. Search a book")
    print("2. See list of books")
    print("3. See What I am currently borrowing")
    print("4. See What I borrowed before")
    print("5. Exit\n")
    
    return input("Please choose an option (1-5): \n")

selection = "0"

while(selection != "5"):
    selection = displayUserMenu()
    clearScreen()
    if(selection == "1"):
        print("You selected Option one!\n")
        generalSearch()
        input("Return to continue...")
    elif(selection == "2"):
        print("You selected Option two!\n")
        input("Return to continue...")
    elif(selection == "3"):
        print("You selected Option three!\n")
        input("Return to continue...")
    elif(selection == "4"):
        print("You selected Option four!\n")
        input("Return to continue...")
    elif(selection != "5"):
        print("Please return to menu and select a digit from 1 to 5")
        input("Return to continue...")

print("Bye!")