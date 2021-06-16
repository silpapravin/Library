import os
import searchBook

def clearScreen():
    os.system('cls')

def displayUserMenu():
    clearScreen()
    print(f"Welcome to the library, Menu options:")
    print("1. Search a book")
    print("2. See list of books")
    print("3. See What I am currently borrowing")
    print("4. See What I borrowed before")
    print("5. Exit\n")
    
    choice= input("Please choose an option (1-5): \n")

    while(choice != "5"):
        clearScreen()
    if(choice == "1"):
        print("You selected Option one!\n")
        searchBook.generalSearch()
        input("Return to continue...")
    elif(choice == "2"):
        print("You selected Option two!\n")
        input("Return to continue...")
    elif(choice == "3"):
        print("You selected Option three!\n")
        input("Return to continue...")
    elif(choice == "4"):
        print("You selected Option four!\n")
        input("Return to continue...")
    elif(choice != "5"):
        print("Please return to menu and select a digit from 1 to 5")
        input("Return to continue...")

    print("Bye!")