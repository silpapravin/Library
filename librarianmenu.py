import os
from searchBook import generalSearch
import Users
import booklist

user_list = Users.userList

def clearScreen():
    os.system('cls')

def displayLibrarianMenu():
    clearScreen()
    print(f"Welcome again {user_list[0]}, Menu options:")
    print("1. Search a book")
    print("2. See What books are borrowed")
    print("3. See See What books are overdue")
    print("4. See library Users")
    print("5.See all books")
    print("6. Exit\n")
    
    choice= input("Please choose an option (1-6): \n")

    while(choice != "6"):
        clearScreen()
        if(choice == "1"):
            print("You selected Option one!\n")
            print("===============================")
            generalSearch()
            input("Return to continue...")
        elif(choice == "2"):
            print("You selected Option two!\n")
            input("Return to continue...")

        elif (choice == "3"):
            print("You selected Option three!\n")
            input("Return to continue...")
        elif(choice == "4"):
            print("You selected Option four!\n")
            input("Return to continue...")
        elif(choice != "5"):
            print("Please return to menu and select a digit from 1 to 6")
            input("Return to continue...")

        print("Bye!")
