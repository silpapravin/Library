from util import Util
from datastore import user_list
from datastore import book_list
from admin_menu import AdminMenu
from user_menu import UserMenu

class LoginMethods():
    
    active_user=""
    count=len(user_list)
    status=False


    def login_menu():
        Util.clear_screen()
        print("Menu Options")
        print(" 1:  User Login")
        print(" 2:  User Registration")
        choice=(input("Enter your choice:  "))
        if(choice=="1"):
            LoginMethods.user_login()
        elif(choice=="2"):
            LoginMethods.newRegistration()
        else:
            answer=str(input("Invalid Entry..Do you want to try again? [Y/N]"))
            answer=answer.upper()
            if (answer=="Y"):
                LoginMethods.login_menu()
            else:
                exit()


    def user_login():
        found=False
        
        user_name=input("Enter Username:  ")
        for user in user_list:
            if (user.username==user_name):
                pass_word=input("Enter password:  ")
            if (user.password==pass_word):
                found=True
                LoginMethods.status=user.is_librarian
                #global active_user
                LoginMethods.active_user=user
                break
            else:
                found=False
                break
            
        if (found==True):
            print("Login Sucesssful")
            print(LoginMethods.active_user.description)
            if (LoginMethods.status==True): 
                AdminMenu.display_librarian_menu(LoginMethods.active_user)
                print("")

            else:
                UserMenu.display_user_menu(LoginMethods.active_user)
                print("")
        else:
            print("Login Unsuccessful")
            #user_login()
        return

    def newRegistration():
        #user_list=user_file.user_list()
        count=len(user_list)
        count=count+1
        print(" Enter registration details")
        print("ID Number :", count)
        user_name=input("Enter a username :")
        pass_word=input("Enter a password :")
        firstname=input("Enter First Name :")
        surname=input("Enter Surname :")
        books=[]
        user_list.append({"IDNumber": count, "isLibrarian": False, "Username": user_name, "Password": pass_word, "Name":firstname, "Surname": surname, "BorrewedBooks":[]})
        print("Welcome  ",firstname)
        print("Please Login to your account")
        LoginMethods.user_login()
        
    #calling function
            
    #login_menu()