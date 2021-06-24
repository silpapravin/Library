from datastore import Datastore
import os
import menu
import search

class UserMenu(menu):

        
    
    def display_user_menu(self, user):
        menu.clear_screen()
        print(f"Welcome to the library {user['Name']}, Menu options:")
        print("1. Search a book")
        print("2. See list of books")
        print("3. See What I am currently borrowing")
        print("4. See What I borrowed before")
        print("5. Exit\n")
        
        choice= input("Please choose an option (1-5): \n")
        
        #while(choice != "5"):
        menu.clear_screen()
        if(choice == "1"):
            print("You selected Option one!\n")
            search.general_search()
            self.display_user_menu(user)
        elif(choice == "2"):
            print("You selected Option two!\n")
            Datastore.loadbook_list()
            input("Return to continue...")
            self.display_user_menu(user)
            
        elif(choice == "3"):
            print("You selected Option three!\n")
            input("Return to continue...")
            self.display_user_menu(user)
                
        elif(choice == "4"):
            print("You selected Option four!\n")
            input("Return to continue...")
            self.display_user_menu(user)
                
        elif(choice == "5"):
            print("Bye!")

        else:
            print("Please return to menu and select a digit from 1 to 5")
            input("Return to continue...")
            self.display_user_menu(user)

        