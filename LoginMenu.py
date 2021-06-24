from user import User
from menu import Menu
#from user_menu import UserMenu

class LoginMenu(Menu):

    # show method provides the logic for displaying the menu options, 
    # getting the user's selection and verifying that selections are valid

    def show_menu(self):
        selection = "0"

        while(selection != "3"):
            self.clearscreen()
            selection = self.process_user_input()

            # handle the case of invalid menu option selected
            if(selection not in ["1", "2", "3"]):
                self.clearscreen()
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

    def user_login(self):
            print("User login")
            print("==========\n")        
            username = input("Please enter your phone number: ")        
            password = input("Password: ")
            email_address = f"hardcoded@domain.com"

            # self.validate_phone_number(username)
            # self.check_phone_number(username)

            user = User()

            input("Login successful - Return to continue to main menu:")

            #user_menu = UserMenu(Menu)
            #user_menu.display_user_menu(user)


        
    def register_user(self):
            print("Register user")
            #user_list=user_file.user_list()
            #count=len(user_list)
            #count=count+1
            print(" Enter registration details")
            #print("ID Number :", count)
            user_name=input("Enter a username :")
            pass_word=input("Enter a password :")
            firstname=input("Enter First Name :")
            surname=input("Enter Surname :")
            books=[]
            #user_list.append({"IDNumber": count, "isLibrarian": False, "Username": user_name, "Password": pass_word, "Name":firstname, "Surname": surname, "BorrowedBooks":[]})
            print("Welcome  ",firstname)
            print("Please Login to your account")
            self.user_login()


    def validate_phone_number(self, phone_number):
            print(f"validate phone number: {phone_number}")

    def check_phone_number(self, phone_number):
            print(f"check phone number: {phone_number}")

Menu_ = LoginMenu()
Menu_.process_user_input()