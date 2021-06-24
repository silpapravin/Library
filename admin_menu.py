from datastore import Datastore
from search import general_search
from search import print_borrowed_book_list
from search import display_users
from search import print_book_list
import menu

class AdminMenu(menu):     

    
    def display_librarian_menu(self, user):
        menu.clear_screen()
        print(f"Welcome again {user['Name']}, Menu options:")
        print("1. Search a book")
        print("2. See What books are borrowed")
        print("3. See See What books are overdue")
        print("4. See library users")
        print("5.See all books")
        print("6. Exit\n")
        
        choice= input("Please choose an option (1-6): \n")

            #while(choice != "6"):
        menu.clear_screen()
        if(choice == "1"):
            print("You selected Option one!\n")
            print("===============================")
            general_search()
            self.display_librarian_menu(user)
        elif(choice == "2"):
            print("You selected Option two!\n")
            print_borrowed_book_list()
            input("Return to continue...")
            self.display_librarian_menu(user)
        elif (choice == "3"):
            print("You selected Option three!\n")
            input("Return to continue...")
            self.display_librarian_menu(user)
        elif(choice == "4"):
            print("You selected Option four!\n")
            display_users()
            input("Return to continue...")
            self.display_librarian_menu(user)
        elif(choice == "5"):
            print("You selected Option five!\n")
            print_book_list
            input("Return to continue...")
            self.display_librarian_menu(user)        
        elif(choice == "6"):
            print("Bye!")
        else:
            print("Please return to menu and select a digit from 1 to 5")
            input("Return to continue...")
            self.display_librarian_menu(user)

