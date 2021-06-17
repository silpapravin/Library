import os
from searchBook import general_search
import Users
import booklist

user_list = Users.user_list

def clear_screen():
    os.system('cls')

def display_librarian_menu():
    clear_screen()
    print(f"Welcome again #####name, Menu options:")
    print("1. Search a book")
    print("2. See What books are borrowed")
    print("3. See See What books are overdue")
    print("4. See library Users")
    print("5.See all books")
    print("6. Exit\n")
    
    choice= input("Please choose an option (1-6): \n")

    while(choice != "6"):
        clear_screen()
        if(choice == "1"):
            print("You selected Option one!\n")
            print("===============================")
            general_search()
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
