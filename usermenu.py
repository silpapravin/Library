import os
import searchBook

def clear_screen():
    os.system('cls')

def display_user_menu():
    clear_screen()
    print(f"Welcome to the library, Menu options:")
    print("1. Search a book")
    print("2. See list of books")
    print("3. See What I am currently borrowing")
    print("4. See What I borrowed before")
    print("5. Exit\n")
    
    choice= input("Please choose an option (1-5): \n")

    while(choice != "5"):
        clear_screen()
    if(choice == "1"):
        print("You selected Option one!\n")
        searchBook.general_search()
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