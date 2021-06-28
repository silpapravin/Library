from util import Util
from datastore import Datastore
from admin_menu import AdminMenu
from user_menu import UserMenu
from user import User

class LoginMethods():
    


    def __init__(self):
        self.active_user=""
        #count=len(user_list)
        self.status=False


    def login_menu(self, datastore):
        Util.clear_screen()
        print("Menu Options")
        print(" 1:  User Login")
        print(" 2:  User Registration")
        choice=(input("Enter your choice:  "))
        if(choice=="1"):
            self.user_login(datastore)
        elif(choice=="2"):
            self.newRegistration(datastore)
        else:
            answer=str(input("Invalid Entry..Do you want to try again? [Y/N]"))
            answer=answer.upper()
            if (answer=="Y"):
                self.login_menu()
            else:
                exit()


    def user_login(self, datastore):

        found=False 
        user_name=input("Enter Username:  ")
        for user in datastore.user_list:
            if (user.username==user_name):
                pass_word=input("Enter password:  ")
                if (user.password==pass_word):
                    found=True
                    self.status=user.is_librarian
                    #global active_user
                    self.active_user=user
                    break
                else:
                    found=False
                    break
            
        if (found==True):
            print("Login Sucesssful")
            
            if (self.status==True):
                admin_menu = AdminMenu() 
                admin_menu.display_librarian_menu(self.active_user, datastore)
                print("")

            else:
                user_menu = UserMenu()
                user_menu.display_user_menu(self.active_user, datastore)
                print("")
        else:
            print("Login Unsuccessful")
            #user_login()
        return

    def newRegistration(self, datastore):
        count=len(datastore.user_list)
        count=count+1
        print(" Enter registration details")
        print("ID Number :", count)
        user_name=input("Enter a username :")
        pass_word=input("Enter a password :")
        firstname=input("Enter First Name :")
        surname=input("Enter Surname :")
        datastore.user_list.append(User(user_name, pass_word, count, firstname, surname, [], [], False))
        print("Welcome  ",firstname)
        print("Please Login to your account")
        self.user_login(datastore)
        
    #calling function
            
    #login_menu()