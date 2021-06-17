import os
import search_book
import user_file
import see_list_of_books

user_list = user_file.user_list
book_list = see_list_of_books.book_list

def clear_screen():
    os.system('cls')

def display_librarian_menu():
    clear_screen()
    print(f"Welcome again #####name, Menu options:")
    print("1. Search a book")
    print("2. See What books are borrowed")
    print("3. See See What books are overdue")
    print("4. See library users")
    print("5.See all books")
    print("6. Exit\n")
    
    choice= input("Please choose an option (1-6): \n")

    while(choice != "6"):
        clear_screen()
        if(choice == "1"):
            print("You selected Option one!\n")
            print("===============================")
            search_book.general_search()
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
            print("You selected Option five!\n")
            see_list_of_books.printbook_list()
            input("Return to continue...")
        elif(choice != "6"):
            print("Please return to menu and select a digit from 1 to 6")
            ("Return to continue...")

        print("Bye!")
