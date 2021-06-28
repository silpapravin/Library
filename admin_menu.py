from search import Search
#from search import print_borrowed_book_list
#from search import print_user_list
#from search import print_book_list
from datastore import Datastore
from util import Util
import datetime

class AdminMenu():     

    
    def display_librarian_menu(self, user, datastore):
        Util.clear_screen()
        print(f"Welcome again {user.name}, Menu options:")
        print("1. Search a book")
        print("2. See What books are borrowed")
        print("3. See What books are overdue")
        print("4. See library users")
        print("5.See all books")
        print("6. Exit\n")
        
        choice= input("Please choose an option (1-6): \n")

            #while(choice != "6"):
        Util.clear_screen()
        if(choice == "1"):
            print("You selected Option one!\n")
            print("===============================")
            Search.general_search(datastore.book_list)
            self.display_librarian_menu(user, datastore)
        elif(choice == "2"):
            print("You selected Option two!\n")
            Search.print_borrowed_book_list(datastore.book_list)
            input("Return to continue...")
            self.display_librarian_menu(user, datastore)
        elif (choice == "3"):
            print("You selected Option three!\n")
            self.is_overdue(datastore.book_list)
            input("Return to continue...")
            self.display_librarian_menu(user, datastore)
        elif(choice == "4"):
            print("You selected Option four!\n")
            Search.print_user_list(datastore.user_list)
            input("Return to continue...")
            self.display_librarian_menu(user, datastore)
        elif(choice == "5"):
            print("You selected Option five!\n")
            Search.print_book_list(datastore.book_list)
            input("Return to continue...")
            self.display_librarian_menu(user, datastore)    
        elif(choice == "6"):
            print("Bye!")
        else:
            print("Please return to menu and select a digit from 1 to 5")
            input("Return to continue...")
            self.display_librarian_menu(user, datastore)

    def is_overdue(self, book_list):
        today = datetime.datetime.now()
        for book in book_list:
            if book.on_loan == True:
                print(today)