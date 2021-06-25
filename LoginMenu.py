from admin_menu import AdminMenu
from user import User
from menu import Menu
from user_menu import UserMenu
import datastore

class LoginMenu(Menu):

    # show method provides the logic for displaying the menu options, 
    # getting the user's selection and verifying that selections are valid

        def show_menu(self):
                selection = "0"

                while(selection != "3"):
                        self.clear_screen()
                        selection = self.process_user_input()

                        # handle the case of invalid menu option selected
                        if(selection not in ["1", "2", "3"]):
                                self.clear_screen()
                                print(f"Invalid menu option [{selection}]. Press return to try again.")
                                input()

    # print the menu and retrieve the users selection and taking the appropriate 
    # action if the selection is one of the supported options

        def process_user_input(self):
            print("Menu options:")
            print("1. Login")
            print("2. Register")
            print("3. Exit\n")

            selection = input("Please choose an option (1-3): ")

            if(selection == "1"):
                self.user_login()
            elif(selection == "2"):
                self.register_user()

            return selection

        def user_login(datastore):
                active_user=""
                user_list = datastore.user_list
                count=len(user_list)
                found=False
                user_name=input("Enter Username:  ")
                for user in user_list:
                        if (user['Username']==user_name):
                                pass_word=input("Enter password:  ")
                        if (user['Password']==pass_word):
                                found=True
                                status=user['isLibrarian']
                                active_user=user
                                break
                        else:
                                found=False
                        break
                        
                if (found==True):
                        print("Login Sucesssful")
                        if (status==True): 
                                AdminMenu.display_librarian_menu(active_user)
                                print("")
                        else:
                                UserMenu.display_user_menu(active_user)
                        print("")
                else:
                        print("Login Unsuccessful")
                        #user_login()
                return
        
        def register_user(self,datastore):
            print("Register user")
            #user_list=user_file.user_list()
            count=len(datastore.user_list)
            print(count)
            count=count+1
            print(" Enter registration details")
            user_name=input("Enter a username :")
            pass_word=input("Enter a password :")
            firstname=input("Enter First Name :")
            surname=input("Enter Surname :")
            books=[]
            datastore.user_list.append(User(user_name, pass_word, count, firstname, surname, "", "", True ))
            
            print("Welcome  ",firstname)
            print("Please Login to your account")
            self.user_login()
  
        
        

        def validate_phone_number(self, phone_number):
            print(f"validate phone number: {phone_number}")

        def check_phone_number(self, phone_number):
            print(f"check phone number: {phone_number}")


#Menu_ = LoginMenu()
#Menu_.show_menu()