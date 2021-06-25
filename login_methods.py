from menu import Menu
from datastore import user_list
from admin_menu import display_librarian_menu
from user_menu import display_user_menu

active_user=""
count=len(user_list)


def login_menu(Menu):
    #clear_screen()
    print("Menu Options")
    print(" 1:  User Login")
    print(" 2:  User Registration")
    choice=(input("Enter your choice:  "))
    if(choice=="1"):
      user_login()
    elif(choice=="2"):
       newRegistration()
    else:
        answer=str(input("Invalid Entry..Do you want to try again? [Y/N]"))
        answer=answer.upper()
        if (answer=="Y"):
          login_menu()
        else:
           exit()


def user_login():
    found=False
    user_name=input("Enter Username:  ")
    for user in user_list:
        if (str(getattr(user, 'username'))==user_name):
           pass_word=input("Enter password:  ")
           if (user['Password']==pass_word):
              found=True
              status=user['isLibrarian']
              global active_user
              active_user=user
              break
           else:
               found=False
               break
          
    if (found==True):
        print("Login Sucesssful")
        if (status==True): 
           display_librarian_menu(active_user)
           print("")
        else:
            display_user_menu(active_user)
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
    user_login()
    
#calling function
        
#login_menu()