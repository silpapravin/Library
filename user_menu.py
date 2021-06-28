from util import Util
from search import Search
from datastore import book_list


class UserMenu():
      
    @staticmethod
    def display_user_menu(user):
        Util.clear_screen()
        print(f"Welcome to the library {user.name}, Menu options:")
        print("1. Search a book")
        print("2. See list of books")
        print("3. See What I am currently borrowing")
        print("4. See What I borrowed before")
        print("5. Exit\n")
        
        choice= input("Please choose an option (1-5): \n")
        
        #while(choice != "5"):
        Util.clear_screen()
        if(choice == "1"):
            print("You selected Option one!\n")
            Search.general_search(book_list)
            UserMenu.display_user_menu(user)
        elif(choice == "2"):
            print("You selected Option two!\n")
            Search.print_book_list(book_list)
            input("Return to continue...")
            UserMenu.display_user_menu(user)
            
        elif(choice == "3"):
            print("You selected Option three!\n")
            if len(user.borrowing) > 0:
                UserMenu.currently_borrowing(user)
            else:
                print("You are not Borrowing any books")
            input("Return to continue...")
            UserMenu.display_user_menu(user)
                
        elif(choice == "4"):
            print("You selected Option four!\n")
            input("Return to continue...")
            UserMenu.display_user_menu(user)
                
        elif(choice == "5"):
            print("Bye!")

        else:
            print("Please return to menu and select a digit from 1 to 5")
            input("Return to continue...")
            UserMenu.display_user_menu(user)

    def currently_borrowing(user):
        for book in user.borrowing:
            print(book.description)